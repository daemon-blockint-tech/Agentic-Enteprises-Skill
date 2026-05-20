# Financial analysis and typologies

## Table of contents

1. [Analysis framework](#analysis-framework)
2. [Flow reconstruction](#flow-reconstruction)
3. [Networks and counterparties](#networks-and-counterparties)
4. [Typology catalog](#typology-catalog)
5. [Crypto and VASP considerations](#crypto-and-vasp-considerations)
6. [Innocent explanations](#innocent-explanations)
7. [External intelligence](#external-intelligence)

## Analysis framework

1. **Scope** — subjects, accounts, date range, products, jurisdictions
2. **Baseline** — expected activity from KYC, RM notes, and historical profile
3. **Deviation** — quantify vs baseline (amount, count, velocity, geography)
4. **Hypothesis** — typology-led; multiple hypotheses allowed
5. **Test** — gather evidence; reject or support each hypothesis
6. **Conclusion** — suspicion level for internal use; gaps and next steps

Separate **verified data** (core banking, TM, KYC) from **inference** (heuristic blockchain labels, media).

## Flow reconstruction

| Element | Document |
|---|---|
| **Timeline** | Ordered events with UTC/local assumption stated |
| **Legs** | Debit/credit, rail (wire, ACH, card, crypto), fees |
| **Aggregation** | Related txs grouped (same counterparty, round amounts, rapid in/out) |
| **Round-tripping** | Funds leaving and returning via related accounts |
| **Layering indicators** | Multiple hops, pass-through, short dwell time |

Use tables: date, amount, currency, account, counterparty, type, reference, analyst note.

## Networks and counterparties

- Map **direct** counterparties (name, country, bank, VASP if applicable)
- Identify **related parties** (UBO, common address, device, IP where policy allows)
- Flag **high-risk** jurisdictions and sectors per risk assessment
- Document **unknown** counterparties explicitly—do not invent entity names
- For nested relationships, attach **simple diagram** or adjacency list in case file

## Typology catalog

| Typology | Observable indicators (examples) |
|---|---|
| **Structuring** | Just-below threshold deposits; smurfing patterns |
| **Layering** | Rapid movement across accounts/institutions; pass-through |
| **Integration** | Sudden use of funds for assets inconsistent with profile |
| **Trade-based ML** | Over/under invoicing; mismatched goods and flows |
| **Mule / funnel** | Many small inflows, single outflow; dormancy then burst |
| **Correspondent abuse** | Nested accounts; payable-through without due diligence |
| **VASP / crypto** | Exchange hops, mixer exposure (heuristic), travel rule gaps |
| **Identity abuse** | Profile mismatch; synthetic identity signals from KYC |

Tie each indicator to **specific transactions or events**—avoid generic typology labels without facts.

## Crypto and VASP considerations

- Use blockchain analytics as **decision support**; document label confidence
- Record **wallet addresses**, chains, and tx hashes in exhibit index
- Note **travel rule** data completeness where relevant
- Route deep forensic narratives to blockint skills; FIU integrates summary into case file
- Do not treat heuristic clustering as proof of ownership

## Innocent explanations

For each material deviation, record:

- **Hypothesis** (e.g., payroll, tuition, property sale, intra-group transfer)
- **Evidence checked** (payslip, invoice, public record, RM confirmation)
- **Outcome** — supported, rejected, or unresolved

Unresolved explanations **increase** escalation likelihood; do not close solely because a plausible story exists without evidence.

## External intelligence

| Source | Use in FIU |
|---|---|
| **Adverse media** | High-level relevance check; route NLP depth to `sentiment-analysis-engineer` |
| **Commercial screening** | True-match disposition already in KYC; do not re-litigate without new hits |
| **Law enforcement / partner bank** | Restricted handling; document receipt and response |
| **Blockchain intelligence** | Summary with confidence; attach provider report as exhibit |

Record **date, source, and analyst interpretation** for each external pull.
