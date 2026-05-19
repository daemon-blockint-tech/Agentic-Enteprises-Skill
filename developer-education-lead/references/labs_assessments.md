# Labs, sandboxes, and assessments

## Table of contents

1. [Lab design](#lab-design)
2. [Sandbox hygiene](#sandbox-hygiene)
3. [Assessments](#assessments)
4. [Academic integrity](#academic-integrity)

## Lab design

Good lab properties:

- **Reproducible** — script or container; pinned versions
- **Inspectable** — clear success criteria (URL returns 200, test passes)
- **Incremental** — checkpoint commits or steps
- **Forgiving** — reset command documented
- **Realistic** — mirrors prod patterns, not toy APIs only

Avoid labs that require **undocumented secrets** or production access.

Pair with `tech-writer-researcher` for reference accuracy; education owns pedagogy.

## Sandbox hygiene

| Control | Purpose |
|---|---|
| Isolated accounts/projects | Blast radius |
| TTL on resources | Cost control |
| Quota alerts | Prevent runaway |
| No real PII | Compliance |
| Teardown automation | Clean state |

Document **cost estimate** per learner per lab run.

## Assessments

| Type | Use |
|---|---|
| Knowledge check | Terminology, when-to-use |
| Practical task | Build/deploy in sandbox |
| Code review rubric | Capstone quality |
| Pair observation | Certification integrity |

Rubrics use **levels** (meets / exceeds / not yet) with concrete signals.

Provide **sample solutions** and **common mistake** notes for graders.

## Academic integrity

- Rotate challenge prompts periodically
- Use private test cases for autograder
- Plagiarism policy for public cohorts
- Proctoring only when credential has external value

Balance integrity with **open learning** — share concepts, vary implementations.
