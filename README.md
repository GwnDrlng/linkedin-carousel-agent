# LinkedIn Carousel Agent

A Claude skill that turns **any topic you give it** into a finished, ready-to-build LinkedIn carousel — actual slide-by-slide copy in your voice, ready to drop into Canva. It runs a short discovery interview first so the content is genuinely yours, then writes the slides. A **separate evaluator agent** independently grades the result after every session, without prompting.

**The deliverable is a carousel about your topic — not a carousel about how carousels work.** The 2026 engagement research lives under the hood as craft knowledge that shapes *how* the slides are written (sharp hook, tight copy, ~7 slides). It is never quoted back at you unless you ask.

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

## What the Skill Covers

1. **Strategy & Planning** - Hook formulas, narrative structure, content type selection
2. **Content Development** - Slide-by-slide outlines, text density rules, headline writing
3. **Design Specifications** - Dimensions, typography, color, mobile readiness
4. **Workflow** - Tools, export settings, file preparation
5. **Quality Checks** - Pre-publication validation checklist
6. **LinkedIn Posting** - Upload steps, caption formula, timing optimization
7. **Performance Tracking** - Metrics, benchmarks, iteration strategies

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

### Main Skill File (the generator)
- `SKILL.md` - Complete skill guidance including the discovery interview and the dispatch-to-evaluator retry loop
  - Discovery interview that personalizes the carousel to you before drafting
  - 7-part craft workflow from strategy through publication (used silently to shape the slides)
  - Common mistakes and how to fix them
  - Content templates for 5 different carousel types
  - Instructions to hand the output to the independent evaluator and act on its verdict

### Independent Evaluator (`.claude/agents/`)
- `carousel-evaluator.md` - A separate judge subagent. Sees only the brief + the carousel, scores it blind against the rubric, and returns a pass/fail scorecard with specific gaps. It does not write or revise carousels — keeping the creator and the grader cleanly separated.

### Evaluation Framework (`linkedin_carousel_eval/`)
- `evaluation-guide.md` - How to interpret scores, run manual evals, and use results to improve the skill
- `grading-rubric.json` - Machine-readable rubric: 6 content-first dimensions (75% content / 25% craft), score levels, and 12 assertion tests (including an anti-stat-recitation check)
- `test-cases.json` - 11 test cases covering content creation (incl. a non-business topic), design/timing Q&A, deck review, troubleshooting, and a discovery-first / anti-stat-dump guard

### Supporting References (`references/`)
- `quick-reference.md` - 60-second summary with checklists and formulas
- `planning-worksheet.md` - Fillable worksheet for planning a carousel step-by-step
- `research-summary.md` - Complete research data and evidence behind all recommendations

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

## Quick Start

1. Load the skill into Claude Code
2. Prompt Claude with what you want to create (e.g., "Help me create a LinkedIn carousel about [topic]")
3. Claude completes the guidance, then automatically scores and revises its output
4. If the score doesn't reach 90% after two attempts, a manual review flag is shown with specific gaps to address

## Contents of Each Part

### Part 1: Strategy & Planning
- How to write a hook that earns the swipe
- 5 narrative arc templates
- Specific hook formulas that work

### Part 2: Content Development
- Slide-by-slide outline template
- The 5-second rule and text density rules
- Avoiding common dead carousels

### Part 3: Design Specifications
- Recommended dimensions (1080 × 1350px portrait)
- Font, color, and spacing rules
- What NOT to do (common design mistakes)

### Part 4: Technical Workflow
- Recommended tools (Canva, Google Slides, PowerPoint, Figma)
- Export settings and checklist

### Part 5: Pre-Publication Quality Check
- Content validation checklist
- Design consistency verification
- Mobile readiness testing

### Part 6: LinkedIn Posting
- Step-by-step upload process
- Caption formula
- Timing optimization

### Part 7: Performance Tracking
- Metrics to monitor (saves, dwell time, comments)
- 2026 benchmarks
- Iteration strategies

### Appendix: Templates by Content Type
- Framework (e.g., "The 3-C Model")
- Step-by-Step Process
- Contrarian Argument
- Data Visualization
- Personal Narrative

## How to Use the References

**For quick answers:** Use `quick-reference.md`
- 60-second summary
- Hook formulas
- Caption formula
- Design checklist
- Timing recommendations

**For planning:** Use `planning-worksheet.md`
- Fillable worksheet
- Strategy section
- Outline template
- Checklist for all steps
- Post-publish evaluation

**For deep research:** Use `research-summary.md`
- All 2026 engagement data
- Why each recommendation works
- Performance benchmarks by audience size
- What works vs what doesn't
- Data sources and caveats

## Evidence & Research

All recommendations are based on 2026 LinkedIn research from:
- Oktopost B2B benchmarks (1,000+ company pages)
- Buffer State of Social Media (52M+ posts analyzed)
- LinkedIn official algorithm research
- Multiple independent carousel studies

See `research-summary.md` for complete citations and data.

## Best Practices Summary

**Content**
- 7 slides optimal (range: 5-10)
- 30 words max per slide
- One idea per slide
- Specific, not generic
- Frameworks are saveable

**Design**
- 1080 × 1350px (portrait, mobile-first)
- 2 fonts, 3 colors throughout
- High contrast, readable on phone
- One focal point per slide

**Strategy**
- Strong hook on slide 1 (determines 80% of performance)
- Clear narrative arc throughout
- Named frameworks people can reuse
- Save-worthy content (treats reader time as precious)

**Engagement**
- Tuesday-Wednesday posting
- 10 AM-12 PM local time
- Monitor saves (most important metric)
- Target: 15-20 seconds dwell time
- 5-10% save rate

## Top 3 Reasons Carousels Fail

1. **Weak hook** - First slide doesn't earn the swipe
2. **Text walls** - Too much content per slide (over 30 words)
3. **No clear structure** - Reads like scattered thoughts instead of progression

## Top 3 Reasons Carousels Succeed

1. **Specific frameworks** - People save things they can reuse
2. **Clear progression** - Each slide creates curiosity for the next
3. **Save-driven content** - Educational value + referenceable content

## For More Help

**If you're stuck on:**
- **Strategy** → Read Part 1 and the narrative arc templates
- **Writing** → Use the quick-reference hook formulas
- **Design** → Check Part 3 design specifications
- **Posting** → Follow Part 6 step-by-step
- **Performance** → Compare to Part 7 benchmarks

## Improving the Skill

The evaluation framework is designed to surface where the skill falls short. If a dimension consistently scores below 3:

1. **Topical Substance** — sharpen the discovery prompts so the skill pulls the user's real material; reinforce "use their specifics"
2. **Hook & Narrative** — expand the hook formulas and narrative-arc templates in `SKILL.md` Part 1
3. **Personalization & Voice** — make the discovery interview more pointed about audience and voice
4. **Silent Craft Adherence** — reinforce the "internal-only, never recite the research" rule
5. **Discovery & Fit** — make the discovery step earlier and clearer in the workflow

Re-run the affected test cases from `test-cases.json` after any update to verify improvement.

## Updates & Maintenance

This skill is based on 2026 LinkedIn research. As the algorithm evolves:
- Track saves, dwell time, and engagement rate against your own carousels
- Run the 11 test cases periodically to catch skill drift
- Update `SKILL.md` and `research-summary.md` with new findings

---

**Created:** June 2026
**Version:** 1.1
**Research cutoff:** June 2026
**Tested:** Based on 2M+ LinkedIn posts analyzed in 2026
