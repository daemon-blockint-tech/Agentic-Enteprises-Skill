---
name: pre-actuarial-foundations
description: |
  Guides pre-credential actuarial foundations—probability and statistics for actuaries,
  financial math (interest, annuities, loans, duration intro), insurance risk concepts,
  spreadsheet/R/Python literacy, SOA/CAS/IAI path overview, and quantitative study discipline.
  Use for pre-actuarial, actuarial foundations, probability for actuaries, financial
  mathematics basics, interest theory, starting actuarial career, SOA exam path, actuarial
  science basics, learn actuarial math, or entry level actuary preparation—not ASTAM/ALTAM
  (advanced-short-term-actuarial-mathematics, advanced-long-term-actuarial-mathematics),
  workpapers (actuarial-analyst), signing/governance (associate-actuary,
  appointed-chief-actuary), generic calculus homework, or ML (data-scientist,
  quantitative-researcher).
---

# Pre-Actuarial Foundations

## When to Use

- Build **probability and statistics** intuition for actuarial exams and early coursework (distributions, expectation, conditioning, LLN/CLT)
- Explain **financial mathematics** basics: interest, annuities certain, loans, yield, introductory duration/convexity
- Introduce **insurance and risk** concepts: pooling, insurability, moral hazard, adverse selection (concept level)
- Orient **tools and data literacy**: Excel/R/Python for actuarial-style tasks—not full data-science pipelines
- Map **credential paths** (SOA, CAS, IAI at overview) and early career expectations
- Structure **quantitative study** habits, problem-solving frameworks, and exam-prep discipline (not past-exam solution dumps)
- Bridge learners toward `actuarial-analyst`, ASTAM/ALTAM skills, or `associate-actuary` when scope advances

## When NOT to Use

- Advanced short-term loss models, credibility math, ASTAM-level compound losses → `advanced-short-term-actuarial-mathematics`
- Long-term life contingencies, mortality reserves, ALTAM depth → `advanced-long-term-actuarial-mathematics`
- Triangle workbooks, IBNR execution, pricing exhibits, model run packs → `actuarial-analyst`
- ASA/FSA exam strategy, signing authority, professional standards depth → `associate-actuary`
- Appointed actuary, ORSA, enterprise governance → `appointed-chief-actuary`
- Enterprise assumption governance and assumption papers → `assumption-setting`
- P&C legal, underwriting authority, claims operations depth → `property-casualty-insurance`
- Life/health product and reserving sign-off depth → `life-health-insurance`
- General university calculus/algebra homework **without** actuarial framing → generic math tutoring unless reframed actuarially
- ML pipelines, feature engineering, quant research → `data-scientist`, `quantitative-researcher`

## Related skills

| Need | Skill |
|---|---|
| Reserving, pricing support, triangles, workpapers | `actuarial-analyst` |
| ASTAM: severity/frequency, aggregate loss, credibility math | `advanced-short-term-actuarial-mathematics` |
| ALTAM: life contingencies, long-term math | `advanced-long-term-actuarial-mathematics` |
| Credential pathways, ethics, signing overview | `associate-actuary` |
| Appointed actuary, regulatory accountability | `appointed-chief-actuary` |
| Enterprise assumption governance | `assumption-setting` |
| P&C products, claims, underwriting context | `property-casualty-insurance` |
| Life/health benefits and mechanics | `life-health-insurance` |
| Statistical/ML beyond actuarial foundations | `quantitative-researcher` |
| General ML and predictive pipelines | `data-scientist` |

## Core Workflows

### 1. Learner intake and goal

Before teaching formulas:

1. **Background** — Student, career-switcher, or analyst upskilling; prior math exposure
2. **Target path** — SOA life/health vs CAS P&C vs local body (IAI, etc.) at high level
3. **Horizon** — Course support, first exams (P, FM, etc.), or conceptual only
4. **Deliverable** — Concept explanation, study plan, worked example, tool orientation—not filing or sign-off
5. **Escalation** — Route professional execution to `actuarial-analyst`; advanced math to ASTAM/ALTAM skills

**See `references/pre_actuarial_scope.md`.**

### 2. Probability and statistics foundations

1. Clarify **random variables**, pmf/pdf, and common actuarial distributions (Bernoulli, binomial, Poisson, exponential, normal)
2. Teach **expectation, variance, moments**; linearity and when independence matters
3. Introduce **conditioning**, law of total probability/expectation with insurance examples
4. Build **LLN/CLT intuition** for risk pooling (not rigorous measure theory unless asked)
5. Connect to future **frequency/severity** and credibility topics in advanced skills

**See `references/probability_and_statistics_foundations.md`.**

### 3. Financial mathematics foundations

1. **Interest theory** — effective vs nominal rates, force of interest, equivalence
2. **Annuities certain** — immediate vs due; level and simple patterns
3. **Loans and amortization** — payment, outstanding balance, yield problems
4. **Bond basics** — price, yield, introductory **duration and convexity** (conceptual)
5. Flag bridge to life contingencies and ALTAM—not full long-term reserve math here

**See `references/financial_mathematics_foundations.md`.**

### 4. Insurance and risk concepts

1. Explain **risk pooling** and role of **law of large numbers**
2. Distinguish **insurable risk** vs speculative; role of insurer
3. Introduce **moral hazard** and **adverse selection** with simple examples
4. Overview **life vs health vs P&C** economics without line legal depth
5. Point line detail to `life-health-insurance` or `property-casualty-insurance` when needed

**See `references/insurance_and_risk_concepts.md`.**

### 5. Credential landscape and career orientation

1. Summarize **SOA vs CAS** (and IAI/local) paths at overview level
2. Map typical **preliminary exam sequence** (names vary by society)—no exam cheating or live exam content
3. Set expectations for **internships**, actuarial clubs, and early roles
4. Bridge to `associate-actuary` for credential ethics and progression detail

**See `references/actuarial_credential_landscape.md`.**

### 6. Quantitative study discipline and tools

1. Teach **problem-solving loop**: read → define → plan → compute → check units/reasonability
2. Recommend **spaced practice**, error logs, and timed sets (framework only)
3. Orient **Excel** for tables and recursion; **R/Python** for reproducible drills—not production ML
4. Document **notation** and calculator conventions consistently
5. Refuse **sole** deliverable of past-exam solutions without learning objectives

**See `references/quantitative_study_and_tools.md`.**

## Deliverable standards

| Deliverable | Minimum content |
|---|---|
| Concept explainer | Definition, actuarial example, common pitfalls, one worked step |
| Study plan | Weekly topics, resources, practice type, review cadence |
| Formula sheet | Symbols defined; assumptions stated; link to reference section |
| Tool walkthrough | Reproducible steps (Excel/R/Python); no opaque cell magic |
| Career orientation | Path options, next exams at label level, related skills table |

Label output as **educational support**, not actuarial opinion, legal advice, exam authority, or regulatory guidance.

## Assignment type matrix

| Trigger phrase | Primary workflow | Lead reference |
|---|---|---|
| probability for actuaries / distributions | Probability foundations | `probability_and_statistics_foundations.md` |
| financial mathematics basics / interest theory | Interest and annuities | `financial_mathematics_foundations.md` |
| risk pooling / moral hazard (intro) | Insurance economics | `insurance_and_risk_concepts.md` |
| SOA exam path / starting actuarial career | Credentials overview | `actuarial_credential_landscape.md` |
| actuarial science basics / pre-actuarial | Scope and intake | `pre_actuarial_scope.md` |
| learn actuarial math / exam study habits | Study discipline and tools | `quantitative_study_and_tools.md` |

## When to load references

- **Scope, boundaries, learner intake** → `references/pre_actuarial_scope.md`
- **Probability and statistics** → `references/probability_and_statistics_foundations.md`
- **Financial mathematics** → `references/financial_mathematics_foundations.md`
- **Insurance and risk concepts** → `references/insurance_and_risk_concepts.md`
- **Credentials and career paths** → `references/actuarial_credential_landscape.md`
- **Study discipline and tools** → `references/quantitative_study_and_tools.md`
