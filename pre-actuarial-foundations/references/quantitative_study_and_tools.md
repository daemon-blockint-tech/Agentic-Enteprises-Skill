# Quantitative study and tools

## Table of contents

1. [Problem-solving framework](#problem-solving-framework)
2. [Study habits](#study-habits)
3. [Excel for actuarial learning](#excel-for-actuarial-learning)
4. [R and Python orientation](#r-and-python-orientation)
5. [Notation and documentation](#notation-and-documentation)
6. [Academic integrity](#academic-integrity)

## Problem-solving framework

Use on every quantitative question:

1. **Read** — List given, unknown, and assumptions
2. **Define** — Variables, units, payment timing
3. **Plan** — Formula or method (diagram for cashflows)
4. **Compute** — Algebra first; calculator last
5. **Check** — Units, magnitude, boundary cases (\(n=1\), \(i=0\) if valid)

For multi-step exam-style problems, **box final answers** and show one line of reasonability (e.g., PV < sum of undiscounted payments).

## Study habits

| Habit | Implementation |
|---|---|
| Spaced repetition | Revisit weak topics on a schedule |
| Error log | Missed problems → tag by topic (Poisson, annuity due, …) |
| Timed sets | Simulate exam pacing after concepts are stable |
| Mixed review | Avoid only single-topic drills before comprehensive exams |
| Teach-back | Explain solution aloud without notes |

Provide **templates**, not guarantees. Refuse to optimize solely for one exam score without learning objectives.

## Excel for actuarial learning

| Use | Pattern |
|---|---|
| Interest timelines | One row per period; explicit \(i\) cell |
| Amortization | Cumulative principal/interest columns |
| Small simulations | Data table or simple RAND() with fixed seed for class |
| Version control | Name files `topic_YYYYMMDD_v01`; avoid hard-coded magic numbers without comment |

Prefer **transparent formulas** over hidden macros for learning. Production models → `actuarial-analyst`.

## R and Python orientation

| Task | Minimal approach |
|---|---|
| Vectorized means/variances | `mean`, `var` / `numpy` |
| Plot histogram / QQ | Check distributional assumptions (intro) |
| Reproducibility | Set seed; script runs top-to-bottom |

**Not in scope**: sklearn pipelines, deep learning, production ETL → `data-scientist`.

Suggest libraries only when they reinforce **probability/statistics** concepts taught in references.

## Notation and documentation

- One symbol per meaning per problem
- Distinguish **effective** vs **nominal** rates in headers
- State **continuous vs discrete** for survival/failure (preview)
- For spreadsheets: **input / calc / output** tabs when models grow

## Academic integrity

- Teach **methods** for homework-style questions; require user to disclose course rules
- Do not complete graded assignments as a **black-box** service
- For exam prep, use **original** practice problems or licensed materials—not scraped live exams

When user only wants answers, redirect to **framework + similar worked example** with different numbers.
