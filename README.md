# LinkedIn Carousel Agent

A Claude skill for creating high-performing LinkedIn carousel posts based on 2026 engagement research — with a built-in self-evaluation and auto-retry loop that runs after every session without prompting.

## How It Works

Every session follows this flow:

```
User prompt
    ↓
Carousel guidance (strategy, slides, design, posting)
    ↓
Self-evaluation — scored on 5 dimensions (0–4 pts each)
    ↓
Score ≥ 90%? ──Yes──→ Done ✓
    ↓ No
Revise response targeting every gap (Attempt 2)
    ↓
Re-score
    ↓
Score ≥ 90%? ──Yes──→ Done ✓
    ↓ No
⚠️ Manual review flagged — stops and waits for input
```

Claude scores itself after every session, revises once if below 90%, and flags for manual review if it doesn't reach 90% after two attempts. No prompting required.

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

### Main Skill File
- `SKILL.md` - Complete skill guidance including the self-evaluation and retry loop
  - 7-part workflow from strategy through publication
  - Evidence-based best practices from 2026 research
  - Common mistakes and how to fix them
  - Content templates for 5 different carousel types
  - Self-evaluation rubric and retry loop instructions

### Evaluation Framework (`linkedin_carousel_eval/`)
- `evaluation-guide.md` - How to interpret scores, run manual evals, and use results to improve the skill
- `grading-rubric.json` - Machine-readable rubric: 5 dimensions, weights, score levels, and 12 assertion tests
- `test-cases.json` - 10 test cases covering creation, design, troubleshooting, posting, and iteration

### Supporting References (`references/`)
- `quick-reference.md` - 60-second summary with checklists and formulas
- `planning-worksheet.md` - Fillable worksheet for planning a carousel step-by-step
- `research-summary.md` - Complete research data and evidence behind all recommendations

## Evaluation Dimensions

After every session, Claude scores its own output across 5 dimensions:

| Dimension | Weight | What it measures |
|---|---|---|
| Evidence-Based Recommendations | 25% | Cites 2026 research data; explains why recommendations work |
| Actionable Specificity | 25% | Specific numbers (px, words, timing) vs. vague advice |
| Content-Type Matching | 20% | Tailors guidance to framework vs. narrative vs. contrarian |
| Problem Diagnosis & Root Cause | 15% | Identifies root causes, not just symptoms (troubleshooting sessions) |
| Workflow Clarity & Completeness | 15% | Step-by-step with tools, checkpoints, and sequencing |

**Pass threshold:** 70% overall, with all dimensions ≥ 2.0
**Excellence threshold:** 90% (triggers auto-retry if not met)

## Key Stats (2026 Data)

- **Carousel engagement rate**: 6.60% average (3.4x more reach than single posts)
- **Ideal slide count**: 7 slides (18% better than other lengths)
- **Optimal dwell time**: 15-20 seconds
- **Best timing**: Tuesday-Wednesday, 10 AM-12 PM local time
- **Most valuable metric**: Saves (5x more valuable than likes)

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

1. **Evidence-Based** — add newer or more specific research citations to `SKILL.md`
2. **Actionable Specificity** — add missing specs (dimensions, word counts, timing) where the output was vague
3. **Content-Type Matching** — expand the type-specific playbooks in the Appendix
4. **Problem Diagnosis** — add more troubleshooting scenarios to the common mistakes section
5. **Workflow Clarity** — add numbered steps or checkpoints to the relevant part

Re-run the affected test cases from `test-cases.json` after any update to verify improvement.

## Updates & Maintenance

This skill is based on 2026 LinkedIn research. As the algorithm evolves:
- Track saves, dwell time, and engagement rate against your own carousels
- Run the 10 test cases periodically to catch skill drift
- Update `SKILL.md` and `research-summary.md` with new findings

---

**Created:** June 2026
**Version:** 1.1
**Research cutoff:** June 2026
**Tested:** Based on 2M+ LinkedIn posts analyzed in 2026
