#!/usr/bin/env python3
"""SkillOpt-style optimizer: treat SKILL.md as trainable state.

Loop (rollout -> reflect -> gate): replay the eval test cases through a
headless Claude Code session (`claude -p`) with a candidate SKILL.md, grade
each output with an independent headless judge against eval/grading-rubric.json,
have an optimizer model propose bounded anchor-based edits from the train-set
verdicts, and accept a proposal only if the mean judge score on held-out
validation cases improves by epsilon. Every experiment is appended to
optimizer/results/optimizer_log.jsonl and every candidate skill is versioned
in optimizer/skill_history/ (winner: best.md).

Run from anywhere (stdlib only; requires the `claude` CLI on PATH):

    python3 optimizer/optimize.py                # train
    python3 optimizer/optimize.py --apply        # also deploy the winning skill
    python3 optimizer/optimize.py --selftest     # offline checks, no claude calls

The live SKILL.md is never modified unless --apply is passed.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import statistics
import subprocess
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
PLUGIN = HERE.parent
SKILL_DIR = PLUGIN / "skills" / "linkedin-carousel-creator"
SKILL_PATH = SKILL_DIR / "SKILL.md"
RUBRIC_PATH = PLUGIN / "eval" / "grading-rubric.json"
CASES_PATH = PLUGIN / "eval" / "test-cases.json"
HISTORY_DIR = HERE / "skill_history"
LOG_PATH = HERE / "results" / "optimizer_log.jsonl"

CONFIG = json.loads((HERE / "config.json").read_text())

_FRONTMATTER_RE = re.compile(r"\A---\n.*?\n---\n", re.DOTALL)


class BudgetExceeded(RuntimeError):
    pass


class Meter:
    """Accumulate reported `claude -p` cost; 0.0 on subscription plans is fine —
    the experiments cap still bounds the session."""

    def __init__(self, max_usd: float):
        self.usd = 0.0
        self.max_usd = max_usd

    def add(self, usd: float) -> None:
        self.usd += usd or 0.0
        if self.usd > self.max_usd:
            raise BudgetExceeded(f"cost ${self.usd:.2f} exceeds cap ${self.max_usd}")


# ── Pure helpers (covered by --selftest) ──


def extract_json(text: str) -> dict | None:
    """Pull the first JSON object out of a model response (fences tolerated)."""
    m = re.search(r"\{.*\}", text, re.DOTALL)
    if not m:
        return None
    try:
        return json.loads(m.group(0))
    except json.JSONDecodeError:
        return None


def apply_edits(skill: str, edits: list[dict]) -> tuple[str | None, str]:
    """Apply bounded edits; return (new_skill, "") or (None, reason)."""
    if not 1 <= len(edits) <= 4:
        return None, f"proposal has {len(edits)} edits (must be 1-4)"
    text = skill
    for e in edits:
        anchor, op = e.get("anchor", ""), e.get("op", "")
        n = text.count(anchor) if anchor else 0
        if n != 1:
            return None, f"anchor matches {n} times (must be exactly 1): {anchor[:60]!r}"
        if op == "replace":
            text = text.replace(anchor, e.get("text", ""))
        elif op == "insert_after":
            text = text.replace(anchor, anchor + "\n" + e.get("text", ""))
        elif op == "delete":
            text = text.replace(anchor, "")
        else:
            return None, f"unknown op: {op!r}"
    if not text.strip():
        return None, "edits produced an empty skill"
    fm_before = _FRONTMATTER_RE.match(skill)
    fm_after = _FRONTMATTER_RE.match(text)
    if fm_before and (not fm_after or fm_after.group(0) != fm_before.group(0)):
        return None, "edits modified the YAML frontmatter (not allowed)"
    if len(text.split()) > CONFIG["max_skill_words"]:
        return None, f"skill grew past {CONFIG['max_skill_words']} words"
    return text.strip() + "\n", ""


def weighted_pct(scores: dict, rubric: dict) -> float | None:
    """Judge dimension scores (0-4, or None for N/A deliverable) -> 0-100.

    Mirrors the evaluator agent: a null Slide-Ready Deliverable redistributes
    its weight equally across the three content dimensions D1-D3.
    """
    dims = {d["name"]: float(d["weight"]) for d in rubric["grading_rubric"]["dimensions"]}
    weights = dict(dims)
    na = [n for n, s in scores.items() if s is None]
    if "Slide-Ready Deliverable" in na:
        redist = weights.pop("Slide-Ready Deliverable") / 3.0
        for n in ("Topical Substance & Specificity", "Hook & Narrative Quality",
                  "Personalization & Voice"):
            weights[n] += redist
    total_w = total_s = 0.0
    for name, w in weights.items():
        s = scores.get(name)
        if s is None:
            return None  # judge skipped a required dimension — invalid verdict
        total_w += w
        total_s += w * float(s)
    return round(total_s / (4.0 * total_w) * 100, 1) if total_w else None


# ── Headless Claude Code calls ──


def claude_call(prompt: str, model: str, meter: Meter, cwd: Path | None = None,
                max_turns: int | None = None) -> str:
    cmd = ["claude", "-p", prompt, "--model", model, "--output-format", "json"]
    if max_turns:
        cmd += ["--max-turns", str(max_turns)]
    proc = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True,
                          timeout=CONFIG["call_timeout_seconds"])
    if proc.returncode != 0:
        raise RuntimeError(f"claude -p failed ({proc.returncode}): {proc.stderr[:300]}")
    data = json.loads(proc.stdout)
    meter.add(float(data.get("total_cost_usd") or 0.0))
    return data.get("result", "")


def rollout(case: dict, skill_text: str, meter: Meter) -> str:
    """Run one test-case brief against a candidate skill in a throwaway workspace."""
    with tempfile.TemporaryDirectory() as td:
        ws = Path(td)
        dest = ws / ".claude" / "skills" / "linkedin-carousel-creator"
        shutil.copytree(SKILL_DIR, dest)
        (dest / "SKILL.md").write_text(skill_text)
        try:
            out = claude_call(f"/linkedin-carousel-creator {case['prompt']}",
                              CONFIG["rollout_model"], meter, cwd=ws, max_turns=8)
            if out.strip() and "unknown command" not in out.lower():
                return out
        except RuntimeError:
            pass  # fall back to natural-language invocation
        return claude_call(
            "Use the linkedin-carousel-creator skill for this request.\n\n" + case["prompt"],
            CONFIG["rollout_model"], meter, cwd=ws, max_turns=8)


def judge(case: dict, output: str, rubric: dict, meter: Meter) -> dict:
    """Grade one rollout; returns {pct, scores, gaps, fixes} (pct None if unparseable)."""
    case_block = {k: case[k] for k in ("id", "name", "prompt", "expected_outputs",
                                       "success_criteria")}
    prompt = (
        (HERE / "judge-prompt.md").read_text()
        + "\n\nGRADING RUBRIC (JSON):\n" + json.dumps(rubric["grading_rubric"])
        + "\n\nTEST CASE:\n" + json.dumps(case_block, indent=1)
        + "\n\nOUTPUT UNDER TEST:\n<<<OUTPUT\n" + output + "\nOUTPUT\n"
    )
    verdicts, pcts = [], []
    for _ in range(CONFIG["judge_samples"]):
        raw = claude_call(prompt, CONFIG["judge_model"], meter, max_turns=1)
        v = extract_json(raw)
        if not v or "scores" not in v:
            continue
        pct = weighted_pct(v["scores"], rubric)
        if pct is not None:
            verdicts.append(v)
            pcts.append(pct)
    if not pcts:
        return {"pct": None, "scores": {}, "gaps": "judge output unparseable", "fixes": []}
    v = verdicts[0]
    return {"pct": round(statistics.mean(pcts), 1), "scores": v["scores"],
            "gaps": v.get("gaps", ""), "fixes": v.get("fixes", [])}


def rollout_set(case_list: list[dict], skill_text: str, rubric: dict, meter: Meter,
                label: str) -> list[dict]:
    def one(case: dict) -> dict:
        out = rollout(case, skill_text, meter)
        verdict = judge(case, out, rubric, meter)
        print(f"    {label} {case['id']}: {verdict['pct']}", flush=True)
        return {"case": case, **verdict}

    with ThreadPoolExecutor(max_workers=CONFIG["workers"]) as pool:
        return list(pool.map(one, case_list))


def mean_pct(rollouts: list[dict]) -> float:
    scored = [r["pct"] for r in rollouts if r["pct"] is not None]
    if len(scored) < len(rollouts):
        print(f"    warning: {len(rollouts) - len(scored)} unscored rollout(s) excluded")
    return round(statistics.mean(scored), 1) if scored else 0.0


# ── Reflect: verdicts -> bounded edit proposal ──


def propose(skill_text: str, train_rollouts: list[dict], history: list[dict],
            meter: Meter) -> dict | None:
    verdict_block = "\n\n".join(
        f"### {r['case']['id']} — {r['case']['name']} (score {r['pct']})\n"
        f"scores: {json.dumps(r['scores'])}\ngaps: {r['gaps']}\n"
        f"fixes: {json.dumps(r['fixes'])}"
        for r in train_rollouts
    )
    hist_lines = "\n".join(
        f"- exp {h['exp']} [{'ACCEPTED' if h['accepted'] else 'rejected'}, "
        f"val {h['val_mean']}]: {h['hypothesis']}" for h in history
    ) or "(first experiment this session)"
    prompt = (
        (HERE / "optimizer-prompt.md").read_text()
        + "\n\nCURRENT SKILL:\n<<<SKILL\n" + skill_text + "\nSKILL\n"
        + "\nTRAIN ROLLOUT VERDICTS:\n" + verdict_block
        + "\n\nEXPERIMENT HISTORY (this session):\n" + hist_lines
        + "\n\nPropose the next experiment."
    )
    raw = claude_call(prompt, CONFIG["optimizer_model"], meter, max_turns=1)
    proposal = extract_json(raw)
    if not proposal or "edits" not in proposal:
        return None
    return proposal


# ── Session ──


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _log(row: dict) -> None:
    LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with LOG_PATH.open("a") as f:
        f.write(json.dumps(row) + "\n")


def _save(name: str, text: str) -> None:
    HISTORY_DIR.mkdir(parents=True, exist_ok=True)
    (HISTORY_DIR / name).write_text(text)


def run(n_experiments: int, apply: bool, case_filter: list[str] | None) -> int:
    rubric = json.loads(RUBRIC_PATH.read_text())
    all_cases = json.loads(CASES_PATH.read_text())["test_cases"]
    if case_filter:
        all_cases = [c for c in all_cases if c["id"] in case_filter]
    val_ids = set(CONFIG["val_case_ids"])
    train = [c for c in all_cases if c["id"] not in val_ids]
    val = [c for c in all_cases if c["id"] in val_ids]
    if not train or not val:
        print(f"Bad split: {len(train)} train / {len(val)} val "
              f"(check val_case_ids in config.json)", file=sys.stderr)
        return 1

    session = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    meter = Meter(CONFIG["max_usd"])
    original = SKILL_PATH.read_text()
    best, best_val = original, 0.0
    _save(f"{session}-original.md", original)
    print(f"[{session}] {len(train)} train / {len(val)} val "
          f"(val: {', '.join(sorted(val_ids))}); budget ${CONFIG['max_usd']:.2f}")

    history: list[dict] = []
    epsilon = CONFIG["epsilon_pct"]
    try:
        print("[baseline] rollouts…", flush=True)
        train_rollouts = rollout_set(train, best, rubric, meter, "train")
        val_rollouts = rollout_set(val, best, rubric, meter, "val")
        best_val = mean_pct(val_rollouts)
        print(f"  baseline: train={mean_pct(train_rollouts)} val={best_val}")
        _log({"ts": _now(), "session": session, "exp": 0, "hypothesis": "(baseline)",
              "edits": [], "val_mean": best_val, "train_mean": mean_pct(train_rollouts),
              "accepted": True, "reason": "baseline", "est_cost_usd": round(meter.usd, 3)})

        for i in range(1, n_experiments + 1):
            print(f"[exp {i}/{n_experiments}] propose…", flush=True)
            proposal = propose(best, train_rollouts, history, meter)
            if proposal is None:
                print("  optimizer output unparseable, skipping")
                continue
            print(f"  hypothesis: {proposal.get('hypothesis', '(none)')}")
            candidate, err = apply_edits(best, proposal["edits"])
            if candidate is None:
                print(f"  invalid proposal: {err}")
                _log({"ts": _now(), "session": session, "exp": i,
                      "hypothesis": proposal.get("hypothesis", ""),
                      "edits": proposal["edits"], "val_mean": None, "accepted": False,
                      "reason": f"invalid: {err}", "est_cost_usd": round(meter.usd, 3)})
                history.append({"exp": i, "hypothesis": proposal.get("hypothesis", ""),
                                "accepted": False, "val_mean": "n/a (invalid edits)"})
                continue

            cand_rollouts = rollout_set(val, candidate, rubric, meter, "val")
            val_mean = mean_pct(cand_rollouts)
            accepted = val_mean >= best_val + epsilon
            verdict = ("ACCEPTED" if accepted
                       else f"rejected ({val_mean} < {round(best_val + epsilon, 1)})")
            print(f"  val={val_mean} vs best={best_val} -> {verdict}")

            _save(f"{session}-exp{i}-{'accepted' if accepted else 'rejected'}.md", candidate)
            _log({"ts": _now(), "session": session, "exp": i,
                  "hypothesis": proposal.get("hypothesis", ""), "edits": proposal["edits"],
                  "val_mean": val_mean, "best_val_before": best_val, "accepted": accepted,
                  "reason": verdict, "est_cost_usd": round(meter.usd, 3)})
            history.append({"exp": i, "hypothesis": proposal.get("hypothesis", ""),
                            "accepted": accepted, "val_mean": val_mean})

            if accepted:
                best, best_val = candidate, val_mean
                _save("best.md", best)
                print("  refresh train rollouts…", flush=True)
                train_rollouts = rollout_set(train, best, rubric, meter, "train")

    except BudgetExceeded as e:
        print(f"\nBUDGET EXHAUSTED: {e} — keeping best result so far.", file=sys.stderr)

    improved = best != original
    print(f"\nsession {session}: best val={best_val} "
          f"({'improved' if improved else 'no accepted edits'}), "
          f"est cost ${meter.usd:.2f}")
    if improved:
        _save("best.md", best)
        if apply:
            SKILL_PATH.write_text(best)
            print(f"APPLIED to {SKILL_PATH}")
        else:
            print(f"best skill at {HISTORY_DIR}/best.md — re-run with --apply to deploy")
    return 0


# ── Selftest (offline, no claude calls) ──


def selftest() -> int:
    fm = "---\nname: x\ndescription: d\n---\n"
    body = "# Title\n\nRule one stays.\n\nRule two goes.\n"
    skill = fm + body
    out, err = apply_edits(skill, [{"op": "delete", "anchor": "Rule two goes.\n"}])
    assert err == "" and "Rule two" not in out, err
    out, err = apply_edits(skill, [{"op": "replace", "anchor": "name: x", "text": "name: y"}])
    assert out is None and "frontmatter" in err, err
    out, err = apply_edits(skill, [{"op": "replace", "anchor": "Rule", "text": "x"}])
    assert out is None and "matches 2 times" in err, err
    out, err = apply_edits(skill, [{"op": "insert_after", "anchor": "# Title",
                                    "text": "New rule."}])
    assert err == "" and "# Title\nNew rule." in out, err
    assert extract_json("noise ```json\n{\"a\": 1}\n``` tail") == {"a": 1}
    assert extract_json("no json here") is None
    rubric = json.loads(RUBRIC_PATH.read_text())
    full = {"Topical Substance & Specificity": 4, "Hook & Narrative Quality": 4,
            "Personalization & Voice": 4, "Slide-Ready Deliverable": 4,
            "Silent Craft Adherence": 4, "Discovery & Fit": 4}
    assert weighted_pct(full, rubric) == 100.0
    na = dict(full, **{"Slide-Ready Deliverable": None})
    assert weighted_pct(na, rubric) == 100.0  # redistribution keeps a perfect score perfect
    assert weighted_pct({"Topical Substance & Specificity": 4}, rubric) is None
    print("selftest ok")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description="Metric-gated SKILL.md optimization loop")
    p.add_argument("--experiments", type=int, default=CONFIG["experiments"])
    p.add_argument("--apply", action="store_true",
                   help="write the winning skill to the live SKILL.md")
    p.add_argument("--cases", help="comma-separated case ids to restrict the run")
    p.add_argument("--selftest", action="store_true",
                   help="run offline checks of the pure helpers and exit")
    args = p.parse_args()
    if args.selftest:
        return selftest()
    return run(args.experiments, args.apply,
               args.cases.split(",") if args.cases else None)


if __name__ == "__main__":
    raise SystemExit(main())
