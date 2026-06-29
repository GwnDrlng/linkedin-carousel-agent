# LinkedIn Carousel Agent

A Claude Code **plugin** that turns **any topic you give it** into a finished, ready-to-build LinkedIn carousel — actual slide-by-slide copy in your voice, ready to drop into Canva. It runs a short discovery interview first so the content is genuinely yours, then writes the slides. A **separate evaluator agent** independently grades the result after every session, without prompting.

**The deliverable is a carousel about your topic — not a carousel about how carousels work.** The 2026 engagement research lives under the hood as craft knowledge that shapes *how* the slides are written (sharp hook, tight copy, ~7 slides). It is never quoted back at you unless you ask.

## Install

This repo is a Claude Code plugin marketplace. To install the skill:

```text
/plugin marketplace add GwnDrlng/linkedin-carousel-agent
/plugin install linkedin-carousel@linkedin-carousel-agent
```

Then run `/plugin` to confirm it's enabled. Once installed you can either invoke the skill directly:

```text
/linkedin-carousel:linkedin-carousel-creator
```

…or just describe what you want in plain language ("help me make a LinkedIn carousel about cold-water swimming") and Claude will load the skill automatically. The bundled `carousel-evaluator` agent comes with it and scores the output after each session.

**Local development / testing** (no install needed) — from a clone of this repo:

```bash
claude --plugin-dir ./plugins/linkedin-carousel
```

`/help` will then list `/linkedin-carousel:linkedin-carousel-creator` and `/agents` will list `carousel-evaluator`. Run `/reload-plugins` to pick up edits without restarting.

## How It Works

The generator and the judge are **two separate agents** — the one that writes the carousel never grades its own work (that's the bias LLM-as-judge best practice exists to avoid). The independent `carousel-evaluator` only sees your brief and the output, and scores it blind against the rubric.

```
User prompt
    ↓
Discovery interview (topic, your expertise, specifics, audience, voice, goal)
    ↓
Carousel written for YOUR topic (slide-by-slide copy + caption)
    ↓
Dispatch to INDEPENDENT carousel-evaluator agent
  (sees only the brief + the output; scores blind on 6 dimensions, 75% content / 25% craft)
    ↓
PASS (≥ 90%, all dims ≥ 2.0)? ──Yes──→ Done ✓
    ↓ No
Creator revises, targeting the evaluator's named gaps
    ↓
Re-dispatch to a FRESH evaluator instance (Attempt 2)
    ↓
PASS? ──Yes──→ Done ✓
    ↓ No
⚠️ Manual review flagged — stops and waits for input
```

The creator interviews you, writes the carousel for your subject, then hands it to the independent evaluator. The evaluator decides pass/fail; the creator reacts — revising once if it fails and re-submitting to a fresh judge, then flagging for manual review if it still falls short after two attempts. The creator never overrules the score.

## When to Use This Skill

Trigger this skill when you want to:
- Create a new LinkedIn carousel from scratch
- Structure existing content as a carousel
- Optimize carousel design or engagement
- Understand what makes carousels perform well
- Get step-by-step guidance on carousel creation

**Example prompts:**
- "Help me create a LinkedIn carousel about [topic]"
- "I have content about [topic]. How should I structure it as a carousel?"
- "What makes LinkedIn carousels perform well?"
- "Guide me through carousel creation for [topic]"
- "Should this be a carousel or a text post?"

## Inside This Repo

```
linkedIn_carousel_creator/                 # marketplace root
├── .claude-plugin/marketplace.json        # lists the plugin (used by /plugin marketplace add)
└── plugins/linkedin-carousel/             # the plugin
    ├── .claude-plugin/plugin.json         # plugin manifest (name, version, author)
    ├── skills/linkedin-carousel-creator/
    │   ├── SKILL.md                        # the generator skill + dispatch-to-evaluator retry loop
    │   └── references/                     # supporting craft docs (see below)
    ├── agents/carousel-evaluator.md        # the independent judge subagent
    └── eval/                               # evaluation framework
        ├── grading-rubric.json             # machine-readable rubric (source of truth)
        ├── evaluation-guide.md             # how to interpret scores / run manual evals
        └── test-cases.json                 # 11 regression test cases
```

### Main Skill File (the generator)
- `skills/linkedin-carousel-creator/SKILL.md` — Complete skill guidance: the discovery interview, the 7-part craft workflow (used silently to shape the slides), common mistakes, content templates for 5 carousel types, and the dispatch-to-evaluator retry loop. References to the rubric and evaluator use `${CLAUDE_PLUGIN_ROOT}` so they resolve wherever the plugin is installed.

### Independent Evaluator (`agents/`)
- `carousel-evaluator.md` — A separate judge subagent. Sees only the brief + the carousel, scores it blind against the rubric, and returns a pass/fail scorecard with specific gaps. It does not write or revise carousels — keeping the creator and the grader cleanly separated.

### Evaluation Framework (`eval/`)
- `evaluation-guide.md` — How to interpret scores, run manual evals, and use results to improve the skill
- `grading-rubric.json` — Machine-readable rubric: 6 content-first dimensions (75% content / 25% craft), score levels, and 12 assertion tests (including an anti-stat-recitation check)
- `test-cases.json` — 11 test cases covering content creation (incl. a non-business topic), design/timing Q&A, deck review, troubleshooting, and a discovery-first / anti-stat-dump guard

### Supporting References (`skills/linkedin-carousel-creator/references/`)
- `quick-reference.md` — 60-second summary with checklists and formulas
- `planning-worksheet.md` — Fillable worksheet for planning a carousel step-by-step
- `research-summary.md` — Complete research data and evidence behind all recommendations

## Evaluation Dimensions

After every session, the **independent `carousel-evaluator` agent** (not the creator) scores the output across 6 dimensions. **Content quality is 75% of the score; silent craft + discovery is 25%.** The eval grades the carousel produced *for your topic* — it does **not** reward (and actively penalizes) reciting engagement statistics at you.

| Dimension | Weight | What it measures |
|---|---|---|
| Topical Substance & Specificity | 25% | Real, save-worthy content on YOUR topic — not generic filler |
| Hook & Narrative Quality | 20% | Swipe-earning hook tied to the topic; coherent arc to a payoff |
| Personalization & Voice | 20% | Built from your audience, expertise, story, and voice |
| Slide-Ready Deliverable | 10% | Actual paste-able slide copy + caption, not advice about making one |
| Silent Craft Adherence | 15% | Applies format best practices invisibly — no stat-padding |
| Discovery & Fit | 10% | Ran the discovery interview (or stated assumptions) before drafting |

**Pass threshold:** 90% — Claude auto-retries once if it falls below this, and flags for manual review if it fails to reach 90% after two attempts.

## Under the Hood (Internal Craft — Not Shown to You)

These figures shape *how* the skill writes your slides. They are never quoted back to you unless you ask:

- Ideal slide count ~7 (range 5–10)
- ~30 words max per slide; one idea per slide
- Portrait 1080 × 1350px, 2 fonts / 3 colors, high contrast
- Strong hook on slide 1; clear CTA on the last
- Post timing and metric priorities for when you ask about posting/performance

## Improving the Skill

The evaluation framework is designed to surface where the skill falls short. If a dimension consistently scores below 3, sharpen the matching part of `SKILL.md` (discovery prompts for Topical Substance / Personalization, hook formulas and narrative arcs for Hook & Narrative, the "never recite the research" rule for Silent Craft), then re-run the affected cases from `eval/test-cases.json` to verify improvement.

## Updates & Maintenance

This skill is based on 2026 LinkedIn research. As the algorithm evolves:
- Track saves, dwell time, and engagement rate against your own carousels
- Run the 11 test cases periodically to catch skill drift
- Update `SKILL.md` and `references/research-summary.md` with new findings
- Bump `version` in `plugins/linkedin-carousel/.claude-plugin/plugin.json` so installed users receive the update

---

**Created:** June 2026
**Version:** 1.1.0
**Research cutoff:** June 2026
**Tested:** Based on 2M+ LinkedIn posts analyzed in 2026
