# Assumption categories and sources

## Table of contents

1. [Category taxonomy](#category-taxonomy)
2. [Common drivers by category](#common-drivers-by-category)
3. [Source hierarchy](#source-hierarchy)
4. [Prescribed vs company-specific](#prescribed-vs-company-specific)
5. [Benchmarking and industry data](#benchmarking-and-industry-data)
6. [Data quality and metadata](#data-quality-and-metadata)

## Category taxonomy

| Category | Nature | Update cadence (typical) |
|---|---|---|
| **Economic** | Market-observable or macro | Frequent (quarterly+) |
| **Demographic** | Population risk characteristics | Annual or at experience review |
| **Behavioral** | Policyholder actions | Annual; some dynamic models |
| **Operational** | Company process, expense, systems | Annual |
| **Underwriting / claims** | Loss cost and emergence | Quarterly–annual by line |

Tag each assumption with **one primary category**; note **secondary** links (e.g., lapse behavioral + economic).

## Common drivers by category

### Economic

- Risk-free or portfolio **discount rate** curve
- **Inflation** (medical, wage, general)
- **Interest rate** paths for ALM and dynamic lapse
- **FX** (multi-currency blocks)

### Demographic

- **Mortality / longevity** tables and improvement scales
- **Morbidity** incidence and continuance
- **Retirement age** and turnover (group benefits)

### Behavioral

- **Lapse / persistency** by duration and product
- **Withdrawal** and partial surrender (annuities, UL)
- **Renewal** and re-underwriting take-up
- **Claim reporting** and settlement patterns (as behavior of emergence)

### Operational

- **Expense** ratios (acquisition, maintenance)
- **Commission** and premium taxes
- **Reinsurance** terms embedded as assumptions (cession %, attachment)

### Underwriting / claims (P&C-heavy)

- **Frequency** and **severity** by peril
- **Loss development** factors and tail
- **Catastrophe** models or load factors
- **Large loss** thresholds and pooling

## Source hierarchy

Prefer the **highest-quality** source available for the decision:

| Priority | Source | When to use |
|---|---|---|
| 1 | **Company experience** | Credible volume; stable definitions |
| 2 | **Blended** experience + industry | Partial credibility |
| 3 | **Industry / regulatory tables** | Thin data; new product |
| 4 | **Vendor / index** | Cat models, medical trend indices |
| 5 | **Expert judgment** | Documented override with approval |

Always record **study period**, **exposure basis**, and **segmentation** used to derive company experience.

## Prescribed vs company-specific

| Type | Implication |
|---|---|
| **Prescribed** | Regulatory or accounting standard mandates table or method (jurisdiction-specific) |
| **Company-specific** | Appointed actuary or internal governance approves company view |
| **Locked-in** | Historical assumptions fixed for in-force (e.g., some GAAP/IFRS contexts)—flag block |

Do not substitute legal advice on what is prescribed; outline **questions for qualified reviewers**.

## Benchmarking and industry data

Use benchmarks to **sense-check**, not to copy blindly:

- Industry **experience studies** (mortality, LTC, auto, etc.)
- **Ratemaking organizations** and bureau filings (P&C)
- **Reinsurance** market commentary (trend, cat)
- **Rating agency** and public peer disclosures (high-level)

Document **differences** in mix, geography, and underwriting when deviating from benchmark.

## Data quality and metadata

Minimum metadata per assumption in the register:

| Field | Example |
|---|---|
| Assumption ID | `MORT-ULT-NA-2025Q1` |
| Value / curve | Table reference or scalar |
| Unit | Rate per 1,000, %, factor |
| Source type | Experience study ES-2024-03 |
| Effective date | 2025-03-31 |
| Next review | Annual or trigger-based |
| Limitations | COVID distortion excluded 2020–2021 |

Flag **stale** assumptions when experience period ended before material market or portfolio shifts.
