---
name: Advanced Long-Term Actuarial Mathematics
description: |
  Guides advanced long-term actuarial mathematics (SOA ALTAM)—survival models, life insurance and
  annuity APVs, premiums and reserves (equivalence principle, Thiele), multiple decrement and
  Markov states, yield-curve discounting, mortality improvement, longevity risk, profit testing,
  and mortality graduation. Tool-agnostic, concept-first. Use when the user mentions advanced
  long-term actuarial mathematics, ALTAM, survival model, life insurance reserve, annuity valuation,
  equivalence principle, Thiele equation, multiple decrement, force of mortality, longevity risk,
  mortality improvement, actuarial present value, or net premium reserve—not ASTAM/P&C
  (advanced-short-term-actuarial-mathematics), workpapers only (actuarial-analyst), appointed actuary
  (appointed-chief-actuary), assumption governance (assumption-setting), ALM detail
  (asset-liability-management), or exam-only deliverables.
---

# Advanced Long-Term Actuarial Mathematics

## When to Use

- Build and interpret **survival models**: \(l_x\), \(q_x\), \(\mu_x\), select vs ultimate mortality
- Value **life insurance** and **annuity** benefits (term, whole life, endowment, temporary/whole life annuities)
- Derive **premiums and reserves** via equivalence principle, Thiele, prospective vs retrospective views
- Model **multiple decrements** and **Markov/multi-state** paths (disability, pension, active/retired)
- Apply **yield curves** and discounting for long-dated liability cash flows
- Frame **mortality improvement** and **longevity risk** at a technical level
- Outline **profit testing** and **emerging cost** for life products (conceptual)
- **Estimate and graduate** mortality tables; document data and smoothing choices
- Connect math to **pricing, reserving, and pension liability** measurement; hand execution to `actuarial-analyst`

## When NOT to Use

- P&C frequency-severity, aggregate loss, credibility, or short-tail reserving math → `advanced-short-term-actuarial-mathematics`
- Triangle workbooks, exhibits, statutory tie-outs, or model run packs only → `actuarial-analyst`
- Appointed actuary opinions, regulatory sign-off, or enterprise capital policy → `actuary`, `appointed-chief-actuary`
- Enterprise **assumption governance**, assumption papers, and change control → `assumption-setting`
- ALM duration matching, LDI hedge design, and investment policy depth → `asset-liability-management`
- Life/health product mechanics, underwriting, or claims without contingency math focus → `life-health-insurance`
- Pension ERISA, PBGC, fiduciary, or plan design narrative without contingency formulas → `pension-retirement-funds`
- Exam cram or past-exam solutions as the **sole** deliverable (support professional application; exam study is secondary)
- General data science, ML pipelines, or quant research without life-contingency framing → `data-scientist`, `quantitative-researcher`
- Credential pathway and exam strategy only → `associate-actuary`

## Related skills

| Need | Skill |
|---|---|
| Workpapers, model I/O, exhibits, analyst QA | `actuarial-analyst` |
| Sign-off, capital overview, governance memos | `actuary` |
| Appointed actuary / chief actuary regulatory framing | `appointed-chief-actuary` |
| ASA/FSO exam pathways and professional standards | `associate-actuary` |
| Assumption governance and enterprise change control | `assumption-setting` |
| Life/health products, benefits, and distribution context | `life-health-insurance` |
| DB/DC pensions, funding policy, liability overview | `pension-retirement-funds` |
| ALM, duration, LDI, and asset–liability strategy | `asset-liability-management` |
| Short-term loss models (ASTAM) | `advanced-short-term-actuarial-mathematics` |
| Statistical/ML modeling beyond standard actuarial methods | `quantitative-researcher` |
| General ML and predictive pipelines | `data-scientist` |

## Core Workflows

### 1. Problem framing (ALTAM-aligned)

Before deriving formulas:

1. **Horizon** — Long-duration; valuation vs pricing vs funding purpose
2. **State space** — Single life, joint life, or multi-state (active/disabled/retired/dead)
3. **Benefit/premium basis** — Net vs gross; continuous vs discrete; payment timing
4. **Mortality basis** — Ultimate vs select; table vintage; improvement scale (if any)
5. **Interest/discount** — Flat rate vs term structure; real vs nominal
6. **Deliverable** — Formula spec, APV tables, reserve recursion, sensitivity—not filing sign-off
7. **Peer execution** — Route spreadsheet builds and filing exhibits to `actuarial-analyst`

**See `references/altam_scope_and_principles.md`.**

### 2. Survival models and mortality

1. Define **life table** functions: \(l_x\), \(d_x\), \(q_x\), \(p_x\), \(\mu_x\)
2. Distinguish **ultimate** vs **select** mortality and duration since selection
3. State **independence** assumptions for joint lives unless modeling dependence
4. Document **radix**, age basis, and table source (regulatory, industry, experience)
5. Link **force of mortality** to discrete \(q_x\) under stated assumptions

**See `references/survival_models_and_mortality.md`.**

### 3. Life insurance and annuities

1. Map **benefit types**: level term, whole life, endowment, deferred benefits
2. Write **actuarial present value (APV)** with correct survival and payment timing
3. Cover **annuities**: temporary, whole life, due vs immediate, varying payments
4. Address **joint-life** and **last-survivor** structures at formula level
5. Flag **riders** and options for product context → `life-health-insurance`

**See `references/life_insurance_and_annuities.md`.**

### 4. Premiums and reserves

1. Apply **equivalence principle** for net/gross premiums; define expense and profit loadings
2. Build **prospective** and **retrospective** reserves; reconcile where standard
3. Use **Thiele's equation** for continuous reserves; discrete analogs where needed
4. Distinguish **net level premium** vs **gross premium** reserves
5. Summarize **deficiency** and **emerging cost** implications (conceptual)

**See `references/premiums_and_reserves.md`.**

### 5. Multiple decrement and state models

1. Set up **multiple decrement** table: dependent vs independent decrements
2. Compute **probabilities** of single and combined decrements; associated single decrement rates
3. Extend to **Markov** multi-state models (transition intensities, Kolmogorov forward equations)
4. Apply to **disability**, **pension**, and **long-term care** state spaces (math only)
5. Hand pension plan law and governance narrative to `pension-retirement-funds`

**See `references/multiple_decrement_and_state_models.md`.**

### 6. Longevity, improvement, estimation, and discounting

1. Frame **mortality improvement** scales and **longevity risk** (framework-level)
2. Describe **estimation** from experience; **graduation** and smoothing methods
3. Apply **yield curves** to long cash flows; note ALM interaction at high level → `asset-liability-management`
4. Outline **profit testing** cash flows and **sensitivity** to mortality and interest
5. Package assumptions for actuary review; governance → `assumption-setting`

**See `references/longevity_improvement_and_estimation.md`.**

## Deliverable standards

| Deliverable | Minimum content |
|---|---|
| Model specification | States, benefits, premium type, mortality/interest basis, payment timing |
| Formula sheet | APV, premium, reserve recursions with defined notation |
| Numerical illustration | Small worked example or table with stated assumptions |
| Sensitivity | Mortality, interest, improvement, or lapse drivers (as relevant) |
| Limitations | Table vintage, extrapolation, select period, data volume |

Label output as **technical modeling support**, not actuarial opinion, legal advice, or filed regulatory submission.

## Assignment type matrix

| Trigger phrase | Primary workflow | Lead reference |
|---|---|---|
| survival model / force of mortality | Life table and \(\mu_x\) | `survival_models_and_mortality.md` |
| life insurance APV / endowment | Benefit APVs | `life_insurance_and_annuities.md` |
| annuity valuation | Annuity due/immediate | `life_insurance_and_annuities.md` |
| equivalence principle / net premium | Premium derivation | `premiums_and_reserves.md` |
| Thiele equation / reserve | Reserve recursion | `premiums_and_reserves.md` |
| multiple decrement | Decrement table | `multiple_decrement_and_state_models.md` |
| Markov / disability / pension states | State models | `multiple_decrement_and_state_models.md` |
| mortality improvement / longevity risk | Improvement frameworks | `longevity_improvement_and_estimation.md` |
| graduation / mortality table | Estimation and smooth | `longevity_improvement_and_estimation.md` |
| yield curve / discount long cash flows | Discounting + ALM cross-ref | `longevity_improvement_and_estimation.md` |

## When to load references

- **Scope, ALTAM alignment, principles** → `references/altam_scope_and_principles.md`
- **Survival models and mortality** → `references/survival_models_and_mortality.md`
- **Life insurance and annuities** → `references/life_insurance_and_annuities.md`
- **Premiums and reserves** → `references/premiums_and_reserves.md`
- **Multiple decrement and state models** → `references/multiple_decrement_and_state_models.md`
- **Longevity, improvement, estimation, discounting** → `references/longevity_improvement_and_estimation.md`
