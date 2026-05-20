# Line-of-business assumption packs

## Table of contents

1. [Pack types by use case](#pack-types-by-use-case)
2. [Property and casualty pack](#property-and-casualty-pack)
3. [Life and health pack](#life-and-health-pack)
4. [Pension and retirement pack](#pension-and-retirement-pack)
5. [Multi-line and reinsurance](#multi-line-and-reinsurance)
6. [Cross-skill routing](#cross-skill-routing)

## Pack types by use case

Same LOB often maintains **separate packs**:

| Use case | Emphasis |
|---|---|
| **Pricing** | Prospective trend, competitive loads, near-term frequency/severity |
| **Reserving / valuation** | Development, tail, case adequacy, PYD sensitivity |
| **Capital** | Stress calibrations, tail scenarios, correlation (overview) |
| **ALM** | Discount paths, crediting, asset assumptions, liability cash flows |

Document **differences** when the same driver name differs across packs (e.g., pricing loss trend vs reserving trend).

## Property and casualty pack

Core drivers (illustrative—not exhaustive):

| Driver | Pricing | Reserving |
|---|---|---|
| Frequency / severity by class | Central | Emergence vs paid |
| Loss development | Indication trend | Factor picks, tail |
| Expense | ULAE % | ALAE treatment |
| Catastrophe | Load or model output | Event year handling |
| Large loss | Threshold, pooling | Case vs bulk |
| Trend / inflation | Prospective | Historical vs forward |

**Product context** → `property-casualty-insurance` (coverages, FNOL, reinsurance structures).

**Technical triangles** → `actuary` (`references/reserving_and_loss_development.md`).

## Life and health pack

| Driver | Life | Health | Annuity |
|---|---|---|---|
| Mortality / longevity | ✓ | — | ✓ (longevity) |
| Morbidity | Rider-specific | ✓ central | — |
| Lapse / persistency | ✓ | ✓ | Withdrawal |
| Expense | ✓ | ✓ | ✓ |
| Interest / crediting | UL/VUL | — | ✓ ALM link |

**Product context** → `life-health-insurance` (benefits, networks, risk adjustment overview).

**Experience studies** → coordinate with `actuary` (`references/assumptions_experience_studies.md`).

## Pension and retirement pack

| Driver | DB plans | DC / hybrid |
|---|---|---|
| Mortality / longevity | ✓ | Payout annuity blocks |
| Withdrawal / retirement age | ✓ | Cash balance |
| Salary / wage inflation | ✓ | — |
| Discount rate | Funding / accounting basis | — |
| Expense | Admin, PBGC (US context overview) | — |

**Plan design and ERISA context** → `pension-retirement-funds`—not duplicate plan administration detail here.

Assumption packs for pensions should state **measurement basis** (funding vs accounting vs economic).

## Multi-line and reinsurance

| Topic | Pack note |
|---|---|
| **Allocations** | Corporate expense, capital allocation keys |
| **Reinsurance** | Cession %, reinstatement, collectibility |
| **FX** | Functional currency per block |
| **Group vs individual** | Separate tables where mix differs |

Reinsurance assumed business: align **ceding company** experience with **terms** in treaty assumptions.

## Cross-skill routing

| User need | Primary skill |
|---|---|
| Assumption governance, packs, documentation | `assumption-setting` (this skill) |
| Run pricing, reserves, triangles, studies | `actuary` |
| Consulting engagement, SOW, DD | `actuarial-consulting` |
| P&C product / claims education | `property-casualty-insurance` |
| Life / health product education | `life-health-insurance` |
| Pension plan design / funding policy | `pension-retirement-funds` |
| Non-insurance FP&A metrics | `financial-analyst` (if installed) |
| Executive strategy without assumptions | `business-consultant` |

When building a **new LOB pack**, start from the closest template above, then trim immaterial drivers via materiality workflow.
