# LinkedIn Carousel Creator Skill: Evaluation Guide

This guide explains how to evaluate whether the skill is doing its real job: **turning the user's topic into a strong, ready-to-build carousel for THEM** — not whether it can recite LinkedIn engagement research.

## Who does the grading

Scoring is done by a **separate evaluator agent** (`.claude/agents/carousel-evaluator.md`), not by the agent that wrote the carousel. The creator knows what it *meant* and will give itself credit for things that aren't on the page — so it never grades its own work. The independent evaluator receives only the **brief** and the **output**, reads this rubric (`grading-rubric.json`), and scores blind.

The loop:

1. **Creator** runs discovery and writes the carousel.
2. **Creator** dispatches the brief + output to the `carousel-evaluator` subagent.
3. **Evaluator** scores blind, returns a pass/fail scorecard with specific gaps.
4. If it fails, the creator revises against the named gaps and re-submits to a **fresh** evaluator instance (max 2 cycles), then flags for manual review.

A human can also run an evaluation manually using the same rubric below — useful for spot-checking the judge itself.

---

## What We're Actually Evaluating

The deliverable is a **carousel about the user's subject** — slide-by-slide copy in their voice, built from their material, that they can drop into Canva and post.

A good output:
1. Is genuinely **about the user's topic** (cold-water swimming, SaaS evaluation, trail running, whatever they asked for) — not about how carousels work.
2. Is **specific and personal** — uses the user's real examples, story, numbers, and point of view.
3. **Fits the person** — right audience, voice, and goal, gathered through a short discovery interview.
4. Is **ready to build** — actual headlines + body per slide, plus a caption.
5. **Quietly applies craft** — strong hook, ~7 tight slides, one idea each, clear CTA — *without lecturing the user about engagement statistics*.

> **The single biggest failure mode this rubric guards against:** the skill drifting into generic "carousel best practices" advice or padding the output with engagement benchmarks (6.60%, "7 slides = 18% better," "saves are 5x likes") instead of producing substance on the user's topic. Those figures are **internal craft inputs only**. Quoting them at the user earns zero credit and is penalized.

**Success threshold:** 90% overall (every dimension >= 2.0).

---

## The 6 Dimensions (content = 75%, craft/process = 25%)

| # | Dimension | Weight | Category |
|---|-----------|--------|----------|
| D1 | Topical Substance & Specificity | 25% | content |
| D2 | Hook & Narrative Quality | 20% | content |
| D3 | Personalization & Voice | 20% | content |
| D4 | Slide-Ready Deliverable | 10% | content |
| D5 | Silent Craft Adherence | 15% | craft |
| D6 | Discovery & Fit | 10% | process |

### D1 — Topical Substance & Specificity (25%)
Is the carousel really about the user's topic, with concrete, save-worthy substance?

**Strong:** Slides carry the user's real criteria, numbers, story beats, or opinions. A reader learns or feels something specific.
**Weak:** Generic truisms ("be consistent," "add value") that could be pasted onto any topic; or drift into LinkedIn meta-advice.

### D2 — Hook & Narrative Quality (20%)
Does slide 1 earn the swipe, and does the deck flow to a payoff?

**Strong:** A pointed, specific hook tied to the topic; each slide advances one idea; the deck lands a conclusion + CTA.
**Weak:** "Tips for success" with a swipe arrow; a disconnected list with no arc.

### D3 — Personalization & Voice (20%)
Does it read like *this* person wrote it for *their* audience?

**Strong:** Reflects the discovery answers — audience, tone, the user's credibility and stories. Reads in their voice.
**Weak:** Default corporate voice; ignores who the user is and who they're talking to.

### D4 — Slide-Ready Deliverable (10%)
Did the skill actually write the carousel, or just advise on making one?

**Strong:** Headline + body for every slide, plus a ready caption — buildable in Canva as-is.
**Weak:** A how-to lecture with no concrete slide copy.
**N/A** for pure troubleshooting/Q&A sessions (redistribute its 10% across D1–D3).

### D5 — Silent Craft Adherence (15%)
Does it follow format best practices *invisibly*?

**Strong:** ~5–10 slides (about 7), tight copy (~30 words/slide), one idea per slide, clear CTA — and **no** statistics recited to the user.
**Weak:** Text walls, 15+ slides, no CTA — OR padding the output with engagement benchmarks and meta-commentary the user didn't ask for. (Reciting stats is a craft failure, not a virtue.)

### D6 — Discovery & Fit (10%)
Did it ask the right questions before drafting?

**Strong:** A focused discovery round (topic, credibility, specifics, audience, voice, goal) — or, when the user wants speed, explicit stated assumptions. The answers visibly shape the carousel.
**Weak:** Jumps straight to a template deck from a one-line brief with no questions and no stated assumptions.

---

## Scoring Formula

```
Score = (D1 x 0.25) + (D2 x 0.20) + (D3 x 0.20) + (D4 x 0.10) + (D5 x 0.15) + (D6 x 0.10)
Percentage = (Score / 4.0) x 100
Pass: >= 90% AND every scored dimension >= 2.0
```

For pure troubleshooting/Q&A (no carousel produced), score D4 as N/A and spread its 0.10 weight across D1–D3.

---

## The Assertion Tests

Check only the ones relevant to the session. **A013 is an anti-pattern** — it passes when the skill did NOT do the bad thing.

| ID | Checks | Passes when |
|----|--------|-------------|
| A001 | Real slide-by-slide copy on the user's topic | There are actual headlines/body per slide about their subject |
| A002 | Topic-specific hook | Slide 1 promises specific value / provokes curiosity about the topic |
| A003 | Uses the user's real material | Their examples, story, numbers, or POV appear |
| A004 | Voice & audience match | Tone and target match the request (or a stated assumption) |
| A005 | Discovery before drafting | A question was asked, or assumptions explicitly stated |
| A006 | Silent format adherence | 5–10 slides, tight copy, one idea each |
| A007 | Arc to a payoff | Logical progression; ends on a conclusion |
| A008 | Goal-fit CTA | Final slide CTA serves the user's stated goal |
| A009 | Ready caption | An actual caption is written, on-topic |
| A010 | Real diagnosis (troubleshooting) | Engages the user's actual content, not generic rules |
| A011 | Concise spec answer (design/timing Q) | Answers the question without stat-padding |
| A013 | **Anti-pattern** | Did NOT quote engagement benchmarks at the user unprompted |

---

## How to Run an Evaluation

### Step 1 — Pick a test case
From `test-cases.json` (11 cases):
- **001–003, 010** — content creation on a topic (010 is non-business; proves "any topic")
- **004, 008** — direct design/timing Q&A
- **005** — review the user's own deck
- **006, 007, 009** — troubleshooting the user's specific content
- **011** — thin brief; should trigger discovery, not a generic deck or a stats lecture

### Step 2 — Prompt the skill
Give it the test-case prompt and let it run (including its discovery questions, if any).

### Step 3 — Grade against the 6 dimensions
For each dimension, compare the output to the "Strong/Weak" descriptions above and assign 0–4. Remember: **content first.** Ask "is this a good carousel about their topic?" before anything else.

### Step 4 — Check assertions
Especially **A013** — scan the output for any recited engagement statistics. If the skill lectured the user with benchmarks, that's a real failure, regardless of how polished it looks.

### Step 5 — Document
Record dimension scores, overall %, passed/failed assertions, and 1–2 lines each on strengths and gaps (be concrete about what content was generic or missing).

---

## Worked Example

**Test case:** 011 (thin brief)

**Prompt:** "Make me a LinkedIn carousel."

**Bad output (old behavior):** Immediately produces a 7-slide deck titled "How to Make High-Performing LinkedIn Carousels" citing the 6.60% engagement rate and the 7-slide rule.
- D1 Topical Substance: 0 — no user topic; it invented a meta-topic
- D3 Personalization: 0 — ignores who the user is
- D5 Silent Craft: 0 — recites statistics at the user
- D6 Discovery: 0 — asked nothing
- A005 ✗, A013 ✗ → **Fail (well below 60%)**

**Good output:** "Happy to build this — a few quick questions so it's actually yours: (1) What's the topic and the one thing you want readers to take away? (2) What's your experience with it / what makes this your take? (3) Any specific story, numbers, or example I should use? (4) Who's the audience? (5) How do you want to sound? (6) What should the post get you, and what should readers do at the end?"
- D6 Discovery: 4 — focused, grouped, efficient
- D5 Silent Craft: 4 — no stat-dump, no premature deck
- A005 ✓, A013 ✓ → **Pass** (other content dimensions scored once the user answers)

---

## Common Issues & How to Spot Them

1. **Drift into meta-advice** — the "carousel" ends up being about LinkedIn/carousels rather than the user's subject. *Loses D1; often fails A001.*
2. **Stat-padding** — engagement benchmarks recited to the user. *Loses D5; fails A013.* This is the #1 thing the old rubric wrongly rewarded.
3. **Template output** — generic deck that ignores the user's voice/audience/story. *Loses D3 and D6.*
4. **Advice instead of a deliverable** — explains how to make a carousel but doesn't write one. *Loses D4; fails A001.*
5. **Generic hook** — "Tips for success" instead of a topic-specific promise. *Loses D2; fails A002.*

---

## Interpreting Results

- **90–100% — Pass.** Specific, personalized, ready-to-build carousel on the user's topic; craft applied invisibly.
- **80–89% — Near threshold.** Good but somewhat generic, thin on the user's specifics, or missing a clean deliverable. Revise and retry.
- **70–79% — Below.** On-topic but vague, weak hook, or under-personalized.
- **60–69% — Well below.** Drifts toward generic advice; little personalization.
- **<60% — Poor.** Off-topic, stat-padded, or no real carousel content produced.

---

## Feedback Loop

If a dimension consistently scores low, fix the skill, not the test:
- **D1 Substance** — strengthen the discovery prompts so the skill pulls real material; reinforce "use their specifics."
- **D2 Hook/Narrative** — expand hook formulas and arc templates in SKILL.md Part 1.
- **D3 Personalization** — make the discovery interview more pointed about voice and audience.
- **D5 Craft** — reinforce the "internal-only, never recite" rule for the research data.
- **D6 Discovery** — make the discovery step earlier/clearer in the workflow.

Re-run the affected test cases after any change.

---

**Evaluation framework:** content-first (v2)
**Total test cases:** 11
**Total assertions:** 12 (including 1 anti-pattern)
**Core principle:** grade the carousel produced for the user's topic — never reward reciting the research.
