# Red flags and typologies

## Table of contents

1. [How to use this reference](#how-to-use-this-reference)
2. [Mapping facts to suspicion](#mapping-facts-to-suspicion)
3. [General red flags](#general-red-flags)
4. [Typology catalog](#typology-catalog)
5. [Sector-specific indicators](#sector-specific-indicators)
6. [Crypto and virtual assets](#crypto-and-virtual-assets)
7. [Narrative phrasing examples](#narrative-phrasing-examples)
8. [Anti-patterns](#anti-patterns)

## How to use this reference

Red flags are **prompts for explanation**, not automatic suspicion. For each flag used in an STR narrative:

1. Cite the **observable fact** (transaction, document, statement)
2. State why it is **inconsistent** with customer profile or policy
3. Note **alternative explanations** if investigated

For enterprise TM scenario design, route to **`aml-compliance`**. For TF/PF-specific angles, cross-check **`aml-cft`**.

## Mapping facts to suspicion

| Step | Action |
|---|---|
| 1 | List indicators observed in the case |
| 2 | Group by typology (structuring, layering, etc.) |
| 3 | Remove indicators not supported by evidence |
| 4 | Draft one paragraph per typology with fact citations |
| 5 | MLRO review for cumulative suspicion |

**Cumulative suspicion**: multiple weak indicators may combine; document the **pattern**, not isolated trivia.

## General red flags

| Red flag | Example factual anchor |
|---|---|
| Profile mismatch | Student account with large wire inflows unrelated to stated support |
| Unexplained wealth | Deposits inconsistent with declared income/source of funds |
| Rapid movement | Funds in and out within short window with minimal economic purpose |
| Round amounts | Repeated just-below-threshold deposits (cite thresholds only if factual) |
| Third-party payments | Unrelated parties paying customer obligations |
| Dormant activation | Long inactive account suddenly used at scale |
| Documentation refusal | Customer unable/unwilling to explain despite requests (document outreach) |
| Adverse media / PEP | Verified match with unresolved risk (factual disposition) |
| Sanctions proximity | Transactions involving listed parties or blocked jurisdictions (per policy) |

## Typology catalog

### Structuring (smurfing)

- **Pattern**: multiple cash or electronic deposits/withdrawals sized to avoid internal or regulatory attention
- **Facts to include**: dates, amounts, branches/channels, cumulative totals, known thresholds only as context
- **Avoid**: asserting intent to evade reporting unless institution counsel approves phrasing

### Layering

- **Pattern**: complex chains obscuring origin—multiple accounts, FX, intermediaries
- **Facts**: path of funds, account hops, timing, related parties

### Integration

- **Pattern**: introducing illicit funds into legitimate economy—property, business revenue disguise
- **Facts**: purchases, invoices, commingling with payroll/revenue

### Trade-based money laundering (TBML)

- **Pattern**: mispriced goods, phantom shipments, over/under invoicing
- **Facts**: trade documents, invoice values vs market, shipping anomalies

### Correspondent / nested accounts

- **Pattern**: downstream banks or PSPs unable to identify underlying customers
- **Facts**: respondent relationship, wire messages, missing originator/beneficiary info

### Identity fraud / shell entities

- **Pattern**: synthetic IDs, nominee directors, no physical presence
- **Facts**: KYC anomalies, registry checks, address verification results

### Terrorist financing (TF)

- **Pattern**: small repeatable flows, charitable fronts, high-risk corridors
- **Cross-reference**: `aml-cft` for TF-specific narrative supplements

### Proliferation financing (PF)

- **Pattern**: dual-use goods, sanctioned end-users, trade route anomalies
- **Cross-reference**: `aml-cft`

## Sector-specific indicators

| Sector | Examples |
|---|---|
| **Retail banking** | Cash intensity, remittance corridors, mule behavior |
| **Private banking** | Undisclosed accounts, offshore structures, bearer instruments |
| **MSB / MVTS** | Agent fraud, commingling, incomplete KYC on senders |
| **Securities** | Pump-and-dump funding, insider-linked flows |
| **Insurance** | Early surrender, third-party premium payers |
| **Real estate** | Third-party purchases, rapid flip, opaque sources |
| **VASP / crypto** | Peel chains, mixer exposure, inconsistent travel rule data |

## Crypto and virtual assets

Summarize **on-chain analytics** in STR narratives at institution-approved depth:

| Observation | Narrative approach |
|---|---|
| Exchange deposit from high-risk service | State service category per vendor taxonomy; cite tx hashes if policy allows |
| Rapid chain hops | Describe timing and amounts; attach analytics exhibit |
| Wallet clustering | Present as “analytics indicate possible common control” with confidence caveat |

Deep tracing, attribution claims, or victim recovery → **blockint skills**, not STR drafting alone.

## Narrative phrasing examples

**Weak**: “Customer is laundering money.”

**Strong**: “Between 2024-01-10 and 2024-01-20, account 456 received twelve incoming wires totaling USD 118,400 from nine unrelated individuals. This activity is inconsistent with the customer’s declared employment income (USD 42,000 annually) and prior 12-month average inflow of USD 1,200 per month.”

**Weak**: “Blockchain proves criminal wallet.”

**Strong**: “Blockchain analytics (Exhibit 7) show that deposit address [redacted] received funds from an entity categorized as [high-risk category] on [date]; the customer did not disclose crypto activity during onboarding.”

## Anti-patterns

- Listing **every alert rule** fired without synthesis
- Using **industry buzzwords** without facts
- Importing **unverified social media** as fact
- Stating **sanctions violations** without official list match disposition
- Confusing **fraud loss** with ML suspicion without explaining ML nexus
