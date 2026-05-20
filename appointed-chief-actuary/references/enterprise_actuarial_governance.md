# Enterprise actuarial governance

## Table of contents

1. [Governance stack](#governance-stack)
2. [Actuarial standards manual](#actuarial-standards-manual)
3. [Model risk management](#model-risk-management)
4. [Assumption oversight](#assumption-oversight)
5. [Independent review and EQ](#independent-review-and-eq)
6. [Metrics and reporting](#metrics-and-reporting)

## Governance stack

```
Board / risk committee
        │
Actuarial governance policy (approved by board or delegated)
        │
Chief / appointed actuary
        │
├── Actuarial standards & methods
├── Model risk framework
├── Assumption committee (partner: assumption-setting)
├── Validation & peer review
└── Documentation & retention
```

**Objectives:**

- **Consistency** across LOBs and entities
- **Traceability** from opinion to data and model version
- **Challenge** through tiered review and independence
- **Resilience** via succession and deputy coverage

## Actuarial standards manual

Minimum contents (enterprise level):

| Section | Examples |
|---|---|
| **Scope** | LOBs, entities, bases (statutory, GAAP, IFRS 17) |
| **Methods** | Approved reserving, pricing, crediting approaches |
| **Data** | Sources, cutoff, quality thresholds |
| **Materiality** | When to escalate to chief actuary or board |
| **Documentation** | Workpaper IDs, retention, sign-off matrix |
| **Ethics** | Conflicts, gifts, external work |

**Change control:** Version the manual; train staff; audit compliance sampling.

## Model risk management

Align with enterprise **model risk** policy (may overlap `ai-risk-governance` for ML).

| Tier | Typical criteria | Governance |
|---|---|---|
| **Tier 1** | Opinion-critical, material pricing, capital models | Full validation, annual review, board summary |
| **Tier 2** | Material but not opinion-direct | Validation plan, periodic review |
| **Tier 3** | Tools, spreadsheets, immaterial | Standards + spot checks |

**Lifecycle controls:**

1. **Inventory** — Owner, purpose, tier, last validation
2. **Development** — Requirements, testing, approval to prod
3. **Change** — Impact assessment, re-validation triggers
4. **Use** — Restrictions (e.g., not for filing without approval)
5. **Retirement** — Archive and dependency check

**Chief actuary role:** Set **tiering** and **escalation**; sponsor remediation of critical gaps before opinion sign-off.

## Assumption oversight

Partner with **`assumption-setting`** for enterprise policy; chief actuary typically:

- Chairs or approves **assumption committee** recommendations
- Ensures **opinion-year** assumptions are approved and versioned
- Reviews **emerging experience** triggers for off-cycle changes
- Documents **judgment** when data is thin or regimes change

| Activity | Owner split |
|---|---|
| Assumption **policy** | `assumption-setting` |
| Assumption **application** in models | Fellows / `actuary` |
| **Approval** for opinion | Appointed / chief actuary |
| **Disclosure** in opinion and board pack | Appointed / chief actuary |

## Independent review and EQ

| Mechanism | Purpose |
|---|---|
| **Peer review** | Method and calculation challenge within function |
| **EQ / second line** | Independent actuary review per policy |
| **Internal audit** | Process compliance (not substitute for EQ) |
| **External audit** | Financial statement audit reliance |

**Independence threats:** Combined pricing and reserving without review, pressure to smooth results, compensation tied to short-term earnings.

**Mitigations:** Rotation, EQ on material opinions, documented exceptions, whistleblower channel.

## Metrics and reporting

Dashboard themes for chief actuary (examples):

| Metric | Use |
|---|---|
| Open validation findings (Tier 1) | Opinion blockers |
| Assumption changes pending approval | Cycle risk |
| PYD volatility by LOB | Board narrative prep |
| Model change volume | Control health |
| Staff credential mix | Succession planning |
| CE compliance rate | Professionalism |

Report **exceptions** and **remediation SLAs** to risk committee quarterly when material.
