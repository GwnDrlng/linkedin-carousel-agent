# LinkedIn Carousel Creator Skill: Evaluation Guide

This guide explains how to evaluate whether Claude using the LinkedIn Carousel Creator skill is providing high-quality, evidence-based guidance.

---

## Quick Overview

**What we're evaluating:** Does the skill help users create high-performing LinkedIn carousels by providing:
1. Evidence-based recommendations grounded in 2026 research
2. Specific, actionable guidance (not generic advice)
3. Content-type-matched strategies (frameworks vs. narratives vs. contrarian)
4. Clear workflows and checklists
5. Accurate problem diagnosis when troubleshooting

**Success threshold:** 70% overall (≥ 2.0 on all dimensions)

---

## The 5 Evaluation Dimensions

### 1. Evidence-Based Recommendations (25% weight)

**What we're measuring:** Does output cite 2026 research data and explain why recommendations work?

**Strong output looks like:**
- "Carousel engagement rate averages 6.60% (vs 0.8% for static images)"
- "7-slide carousels perform 18% better than other slide counts"
- "Saves are 5x more valuable than likes in LinkedIn's algorithm"
- Explanations of *why* (algorithm logic, user behavior, research findings)

**Weak output looks like:**
- "Make your carousel engaging" (no specifics)
- "Use what works for you" (no guidance)
- "Most carousels perform well" (no metrics)
- Claims without sourcing

**Scoring:**
- **0**: No data or research mentioned
- **1**: Data mentioned but vague or unsourced
- **2**: References specific 2026 benchmarks (6.60%, 7-slide optimal, etc.)
- **3**: Consistently cites research with metrics and explains reasoning
- **4**: Comprehensively grounds all recommendations in 2026 research with comparative data

**How to evaluate:**
1. When output discusses performance, is a specific percentage mentioned?
2. When recommending slide count, are the 7-slide optimal and 18% improvement mentioned?
3. When discussing timing, is research backing provided?
4. When metrics are discussed, are they compared to benchmarks?

---

### 2. Actionable Specificity (25% weight)

**What we're measuring:** Are recommendations specific and executable, or vague and generic?

**Strong output looks like:**
- "Use 1080 × 1350px portrait orientation (mobile engagement, 67% of users)"
- "Write a hook formula: '[Stat/Question/Claim] + [Value] + [Swipe indicator]'"
- "Post Tuesday-Wednesday, 10 AM-12 PM local time"
- "Maximum 30 words per slide; if you exceed this, users will scroll past"

**Weak output looks like:**
- "Make your design appealing" (no specifics)
- "Post when your audience is active" (no specific time)
- "Keep text manageable" (no word limit)
- "Choose a good narrative structure" (no templates)

**Scoring:**
- **0**: Generic advice without specifics
- **1**: Some specific guidance but missing details
- **2**: Specific in most areas (e.g., slide count with reason) but missing some
- **3**: Specific across all areas (dimensions, font sizes, timing, formulas)
- **4**: Detailed step-by-step with examples, templates, decision trees, edge cases

**How to evaluate:**
1. Are dimensions specified (1080 × 1350px)?
2. Are font sizes specified (24px body, 36px headlines)?
3. Is timing specific (day + time, not just "business hours")?
4. Are hook formulas provided with examples?
5. Are word limits specified (30 words max)?
6. Are workflows numbered/step-by-step?

---

### 3. Content-Type Matching (20% weight)

**What we're measuring:** Does output tailor guidance to the specific carousel type (framework, narrative, contrarian, etc.)?

**Strong output looks like:**
- **Framework**: "Name your framework (e.g., 'The 5-C Model'). Named frameworks drive saves because people reference them later."
- **Contrarian**: "Lead with a controversial claim, then back with data. This type drives comments more than saves."
- **Narrative**: "Structure: Hook (outcome) → Story (2-4 slides) → Insight → Application. Authenticity matters."
- **Data-driven**: "One visualization per slide. Lead with stat, provide context, explain implication."

**Weak output looks like:**
- Same advice regardless of carousel type
- Doesn't acknowledge different content types perform differently
- Wrong structure recommended for content type

**Scoring:**
- **0**: No tailoring; generic advice for all types
- **1**: Acknowledges content type but doesn't adapt
- **2**: Some tailoring by type (different hooks, structures)
- **3**: Tailored narrative structure, hook formula, and design guidance by type
- **4**: Complete playbooks by type (arc, hook, structure, expected performance, CTA)

**How to evaluate:**
1. When user specifies content type, does output distinguish it?
2. Are narrative arcs different by type?
3. Are hook formulas tailored (contrarian hook ≠ framework hook)?
4. Does output explain why each type works differently?
5. Are expected engagement patterns (save rate, comments) explained by type?

---

### 4. Problem Diagnosis & Root Cause (15% weight)

**What we're measuring:** When user reports poor performance, does output identify root causes?

**Strong output looks like:**
- **Low engagement**: "Your first slide hook 'LinkedIn tips' is too generic. Specific claims ('5 tactics that generated 500 leads') earn swipes. Rewrite hook and repost to test improvement."
- **Low completion**: "Each slide averages 100 words. At 5 seconds per slide, readers take 30 seconds total. Most scroll past after slide 5. Solution: Split into more slides, aim for 30 words max."
- **No comments**: "Contrarian content drives comments, but your carousel doesn't challenge thinking. Reframe as 'Why X is wrong' instead of 'How to do X'."

**Weak output looks like:**
- Doesn't diagnose problem
- Identifies only symptoms, not root cause
- Suggests wrong solution

**Scoring:**
- **0**: Misidentifies or doesn't diagnose
- **1**: Identifies one cause without depth
- **2**: Identifies primary + secondary causes with explanations
- **3**: Comprehensive diagnosis with algorithmic impact explained
- **4**: Diagnostic framework with questions, prioritization, testing strategy

**How to evaluate:**
1. When user reports low engagement, is "weak hook" mentioned?
2. When user reports low completion, is "text density" mentioned?
3. Is diagnostic reasoning explained (why this causes the symptom)?
4. Is algorithmic impact explained (how it affects distribution)?
5. Does output help user test/verify hypothesis?

---

### 5. Workflow Clarity & Completeness (15% weight)

**What we're measuring:** Are step-by-step workflows clear, complete, and easy to follow?

**Strong output looks like:**

**LinkedIn Upload Process:**
1. Click "Start a post"
2. Click + icon (add document)
3. Click "Document"
4. Upload your PDF file
5. Add document title (clear, specific)
6. Write caption (3-4 lines, hook + context + CTA)
7. Click "Post"

**Carousel Creation Workflow:**
1. Plan: Define hook, choose narrative structure, target 7 slides
2. Outline: Write 7 headlines, one idea per slide
3. Content: Add body text (30 words max per slide)
4. Design: Apply 2 fonts, 3 colors, high contrast
5. Export: PDF Standard, 1080×1350px, test on phone
6. Publish: Upload to LinkedIn, post Tuesday-Wednesday 10 AM-12 PM
7. Monitor: Track saves (primary metric), dwell time (15-20 sec target)

**Weak output looks like:**
- Missing steps or out of order
- Significant steps omitted (no mention of testing)
- Vague instructions

**Scoring:**
- **0**: No workflow or extremely vague
- **1**: Workflow provided but missing steps or unclear
- **2**: Complete workflow but could use more detail
- **3**: Clear step-by-step with all major steps and detail
- **4**: Comprehensive with numbered steps, examples, decision points, checkpoints

**How to evaluate:**
1. Are steps numbered or clearly sequenced?
2. Are all major phases included (planning, content, design, technical, posting, tracking)?
3. Are tools recommended?
4. Are there checkpoints or quality checks?
5. Is there a worked example or case study?

---

## The 12 Assertion Tests

Assertion tests check for specific claims that must be accurate.

### Critical Assertions (should always pass)

**Assert 001:** Should reference 6.60% engagement rate benchmark
- PASS: Output mentions "6.60% average" or "6.60% engagement rate"
- FAIL: No specific rate, or wrong rate

**Assert 003:** Should recommend 1080 × 1350px dimensions
- PASS: Exact dimensions specified, identified as portrait, reasoning given
- FAIL: Vague ("use portrait"), wrong dimensions, or no mention

**Assert 004:** Should specify 30-word maximum per slide
- PASS: "30 words" or "30-word maximum" stated, 5-second rule mentioned
- FAIL: Vague ("keep text short"), wrong number, or no guidance

**Assert 009:** Should recommend Tuesday-Wednesday, 10 AM-12 PM
- PASS: Day (Tue/Wed) and time (10-12 PM) mentioned with reasoning
- FAIL: Wrong timing, vague, or no recommendation

**Assert 010:** Should emphasize saves as most valuable metric
- PASS: Saves listed first, "5x value of likes" or similar mentioned
- FAIL: Likes/comments prioritized, or no mention of saves

---

## How to Run an Evaluation

### Step 1: Pick a Test Case

Choose from 10 test cases covering different scenarios:
- **001**: Basic framework carousel creation
- **002**: Contrarian argument carousel
- **003**: Personal narrative carousel
- **004**: Design & technical specifications
- **005**: Pre-publication quality check
- **006**: Weak hook diagnosis (low engagement)
- **007**: Text wall problem (low completion)
- **008**: Timing & posting workflow
- **009**: Performance iteration (above/below benchmark)
- **010**: Format rotation strategy

### Step 2: Prompt Claude with Skill

Give the test case prompt to Claude (with the skill loaded):

**Example from Test 006:**
"My carousel about LinkedIn tips only got 50 impressions. The first slide just says 'LinkedIn Tips for Success' with a swipe arrow. Why didn't it perform?"

### Step 3: Grade the Output

Using the grading rubric:

**For each of 5 dimensions:**
1. Read the "Strong output looks like" section
2. Compare Claude's output against success criteria
3. Assign a score: 0-4 points

**Example scoring:**
- Evidence-Based (25%): Score 3 (references hook determines 80% of performance, mentions specific metrics)
- Actionable Specificity (25%): Score 3 (provides hook rewrites with specific formulas)
- Content-Type Matching (20%): Score 2 (doesn't distinguish framework vs narrative vs contrarian)
- Problem Diagnosis (15%): Score 4 (clearly identifies weak hook as root cause, explains algorithmic impact, provides testing strategy)
- Workflow Clarity (15%): Score 2 (mentions next steps but not numbered/detailed)

**Total Score:** (3×0.25) + (3×0.25) + (2×0.20) + (4×0.15) + (2×0.15) = 0.75 + 0.75 + 0.40 + 0.60 + 0.30 = 2.80 / 4.00 = **70%** ✓ PASS

### Step 4: Verify Assertions

Check that critical assertions passed:
- Assert 006 (hook as root cause): ✓ PASS
- Assert 007 (text walls): N/A (not in this test)

### Step 5: Document Results

Record:
- Test case ID and name
- Dimension scores (0-4 for each)
- Overall percentage
- Passed/failed assertions
- Strengths
- Areas for improvement

---

## What Good Scores Look Like

### Excellent (90-100%)
- Comprehensive, research-backed guidance
- Specific details across all areas
- Tailored to content type
- Clear step-by-step workflows
- Accurate problem diagnosis
- **Example:** Test 006 scored 95% - identifies weak hook, explains 80% impact, provides specific rewrites, suggests testing strategy

### Good (80-89%)
- Strong recommendations with evidence
- Mostly specific (may lack some examples)
- Some tailoring by type
- Mostly complete workflows
- **Example:** Test 001 scored 85% - provides framework template, explains save-ability, lacks some design detail

### Acceptable (70-79%)
- Addresses key areas
- Some generic language
- Basic tailoring
- Incomplete workflows
- **Example:** Test 003 scored 72% - understands narrative but lacks specific structure template

### Below Threshold (60-69%)
- Lacks evidence or specificity
- Generic advice
- Incomplete guidance
- **Example:** If output says "make it engaging" with no specifics, would score 65%

### Poor (<60%)
- Fails to meet multiple criteria
- Contradicts research
- Doesn't use skill effectively
- **Example:** Recommends landscape orientation, no research backing, generic advice

---

## Common Issues & How to Spot Them

### Issue 1: Generic Advice Without Specifics
**What it looks like:** "Use a catchy hook" (no formula), "Keep design consistent" (no specs)
**Impact:** Loses 10-15 points on Actionable Specificity
**How to fix:** Check if specific numbers/dimensions/formulas are provided

### Issue 2: No Evidence-Based Support
**What it looks like:** Claims made without research backing or specific metrics
**Impact:** Loses 10-15 points on Evidence-Based Recommendations
**How to fix:** Verify 6.60%, 7-slide optimal, 30-word max, etc. are mentioned

### Issue 3: No Content-Type Tailoring
**What it looks like:** Same advice for framework carousels as contrarian or narrative
**Impact:** Loses 10-15 points on Content-Type Matching
**How to fix:** Check if guidance differs by type (frameworks = named + saveable, contrarian = data-backed + comments)

### Issue 4: Incomplete Root Cause Diagnosis
**What it looks like:** Identifies symptom (low engagement) but not cause (weak hook)
**Impact:** Loses 10-15 points on Problem Diagnosis
**How to fix:** Verify hook, text density, and CTA are checked in troubleshooting

### Issue 5: Missing Workflow Steps
**What it looks like:** Explains concept but doesn't provide step-by-step process
**Impact:** Loses 10-15 points on Workflow Clarity
**How to fix:** Check for numbered steps, tools, checkpoints, examples

---

## Test Case Selection Strategy

**For a comprehensive evaluation, run at least these 5 core tests:**
1. **Test 001** (Basic creation) - Tests overall guidance quality
2. **Test 004** (Design specs) - Tests technical accuracy
3. **Test 006** (Weak hook diagnosis) - Tests problem diagnosis
4. **Test 007** (Text walls) - Tests root cause analysis
5. **Test 008** (Posting workflow) - Tests workflow clarity

**For a focused evaluation, run:**
1. **Test 006** (Weak hook) - Most common user issue
2. **Test 001** (Basic creation) - Most common use case

---

## Interpreting Results

### If Overall Score is 90%+:
✓ Skill is performing excellently. Claude is providing comprehensive, research-backed, specific guidance tailored to content types with clear workflows and accurate problem diagnosis.

### If Overall Score is 80-89%:
✓ Skill is performing well. Most areas strong; may lack depth in some dimensions (e.g., fewer examples, less content-type tailoring).

### If Overall Score is 70-79%:
⚠ Skill meets minimum threshold but has clear areas for improvement. Review dimension breakdown to identify weak areas (Evidence-Based, Actionable Specificity, etc.). Improvement opportunities exist.

### If Overall Score is 60-69%:
✗ Skill underperforming. Missing evidence backing, lacks specificity, or doesn't tailor by content type. Recommend reviewing skill content for accuracy and completeness.

### If Overall Score is <60%:
✗ Skill not functioning as intended. Major issues with accuracy, completeness, or structure. Recommend skill revision or replacement.

---

## Example: Full Evaluation Run

**Test Case:** 006 (Weak Hook Diagnosis)

**Prompt:** "My carousel about LinkedIn tips only got 50 impressions. The first slide just says 'LinkedIn Tips for Success' with a swipe arrow. Why didn't it perform?"

**Claude's Output:**
> "Your hook is too generic. 'LinkedIn Tips for Success' doesn't promise specific value, so people scroll past without swiping. Instead, try: 'The 5 LinkedIn tactics that generated 500 leads in Q3' or 'Why most LinkedIn profiles fail to attract recruiters.' These are specific and show value upfront. The hook determines about 80% of whether someone swipes, so this is likely your main issue. Try rewriting the hook, reposting, and comparing impressions."

**Scoring:**

| Dimension | Score | Reasoning |
|-----------|-------|-----------|
| Evidence-Based (25%) | 3/4 | References 80% rule, mentions algorithm impact. Lacks specific 6.60% benchmark or comparison data. |
| Actionable Specificity (25%) | 4/4 | Provides specific hook rewrites with concrete formulas. Explains exactly what's wrong. |
| Content-Type Matching (20%) | 2/4 | Doesn't address that different content types need different hooks. Treats all carousels same. |
| Problem Diagnosis (15%) | 4/4 | Identifies weak hook as root cause, explains why it matters (80% impact), suggests testing. |
| Workflow Clarity (15%) | 2/4 | Mentions next steps but not detailed. Could explain full retest workflow. |

**Total:** (3×0.25) + (4×0.25) + (2×0.20) + (4×0.15) + (2×0.15) = 2.90 / 4.00 = **72.5%** ✓ PASS

**Assertions:**
- Assert 006 (hook diagnosis): ✓ PASS
- Assert 010 (saves metric): N/A

**Summary:**
- ✓ Correctly identifies hook as root cause
- ✓ Provides specific hook rewrites
- ✓ Explains algorithm impact
- ✗ Doesn't mention content-type specific hooks (frameworks vs contrarian need different approaches)
- ⚠ Could provide more detail on testing/iteration strategy

**Recommendation:** Skill functioning well; minor improvement in content-type tailoring would raise score to 80+%.

---

## Feedback Loop

After running evaluations:

1. **Document results:** Record scores, assertions, strengths, and weaknesses
2. **Identify patterns:** Are certain dimensions consistently low?
3. **Prioritize improvements:** Which dimension has highest impact?
4. **Test improvements:** If skill is updated, re-run same test cases
5. **Track progress:** Compare before/after scores to measure improvement

---

## Questions to Ask When Evaluating

- Is the skill grounded in 2026 research, or does it rely on outdated best practices?
- Are recommendations specific enough that a user can implement them immediately?
- Does the skill treat all carousels the same, or does it account for frameworks vs narratives?
- When diagnosing problems, does it identify root causes or just describe symptoms?
- Are workflows presented step-by-step, or do users have to fill in gaps?
- Does the skill explain *why* recommendations work (algorithm logic, research backing)?
- Are examples and templates provided, or just conceptual guidance?

---

**Evaluation Framework Created:** June 2026
**Total Test Cases:** 10
**Total Assertions:** 12
**Evaluation Depth:** Comprehensive (5 dimensions, multiple assertion tests)
