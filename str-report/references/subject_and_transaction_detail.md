# Subject and transaction detail

## Table of contents

1. [Subject identification fields](#subject-identification-fields)
2. [Related parties and counterparties](#related-parties-and-counterparties)
3. [Account and product appendix](#account-and-product-appendix)
4. [Transaction selection rules](#transaction-selection-rules)
5. [Aggregation methods](#aggregation-methods)
6. [Chronology table template](#chronology-table-template)
7. [Currency and rounding](#currency-and-rounding)
8. [Exhibits and data lineage](#exhibits-and-data-lineage)

## Subject identification fields

Capture fields required by local filing system—below is a **jurisdiction-agnostic superset**. Map to FinCEN SAR, goAML, or national forms during formatting (see `references/jurisdiction_formats_and_filing.md`).

### Primary subject (customer)

| Field | Notes |
|---|---|
| Legal name | As per KYC; include former names if relevant |
| Customer ID | Internal CIF / party ID |
| Type | Individual, corporate, trust, partnership, VASP |
| Date of birth / incorporation | |
| Nationality / jurisdiction of incorporation | |
| Tax identifier | Where collected |
| Government ID type and number | Passport, national ID—per retention policy |
| Residential / registered address | |
| Contact | Phone, email—if narrative relevant |
| Occupation / business activity | From KYC |
| Stated source of wealth / funds | |
| PEP status | Factual: matched / not matched / former PEP |
| Risk rating | At time of review |
| Relationship start date | Onboarding date |
| Account signatory / BO | List with ownership % |

### When subject is unknown or partial

Document **unknown counterparty** fields explicitly: “Beneficiary name per wire message: [X]; KYC not available to reporting institution.”

## Related parties and counterparties

| Party type | Include when |
|---|---|
| Joint account holder | Account in scope |
| Beneficial owner | Corporate/trust customer |
| Authorized user | Activity attributed to them |
| Originator / beneficiary on wires | Material to flow |
| Nested respondent bank | Correspondent cases |
| Merchant / VASP | Crypto or payment flows |

For each counterparty: name (as received), account/IBAN/wallet, institution, country, relationship to customer if known.

## Account and product appendix

| Element | Detail |
|---|---|
| Account numbers / IBANs | All in-scope |
| Product type | Checking, savings, brokerage, wallet, loan |
| Currency | Base and transaction currencies |
| Status | Open, closed, frozen, restricted |
| Branch / channel | Where material |
| Linked accounts | Transfers between owned accounts—note to avoid double-count |

## Transaction selection rules

Define **in-scope** transactions explicitly in the narrative opening:

1. **Alert-driven**: all transactions in alert window
2. **Lookback**: standard 90/180-day policy from institution
3. **Counterparty cluster**: all txs with same originator
4. **Materiality threshold**: exclude below X unless part of pattern

**Include**:

- Transactions that **triggered** or **explain** suspicion
- **Bookends** (first/last in pattern)
- **Offsetting** txs that show layering

**Exclude** (with note): routine payroll if clearly unrelated—explain exclusion to avoid MLRO challenge

## Aggregation methods

| Method | Use when |
|---|---|
| **Daily total per account** | Structuring velocity |
| **Counterparty rollup** | Mule networks |
| **Corridor summary** | Cross-border patterns |
| **Instrument split** | Cash vs wire vs crypto |
| **Running balance** | Account draining / buildup |

Present **summary in narrative**, **detail in appendix table**.

Example summary line:

> “In March 2024, the customer conducted 47 incoming wires totaling USD 892,100 from 31 unique senders, compared with 2 incoming wires totaling USD 3,400 in March 2023.”

## Chronology table template

| Date (UTC) | Event type | Account | Direction | Amount | Currency | Counterparty | Reference / TX ID | Notes |
|---|---|---|---|---|---|---|---|---|
| 2024-03-01 | Wire in | …123 | Credit | 9,800 | USD | Sender A | MT103 ref | 1 of 12 similar |
| 2024-03-01 | Internal xfer | …123 → …456 | Debit | 9,750 | USD | Own account | | Same day |

Attach as **Exhibit A**; narrative references row numbers or dates—not “see spreadsheet” without exhibit ID.

## Currency and rounding

- State **FX rates source** if converting to reporting currency
- Round **consistently** (e.g., two decimals fiat); do not round per row then sum differently
- For crypto, note **valuation timestamp** and unit (BTC vs satoshis)

## Exhibits and data lineage

| Exhibit | Typical content |
|---|---|
| A | Chronology table |
| B | Account statements (redacted) |
| C | KYC / CDD summary |
| D | Wire messages / SWIFT copies |
| E | Blockchain analytics summary |
| F | Customer correspondence log |
| G | Prior STR/SAR copy (if continuing) |

Document **data extract date**, **system source**, and **analyst** who validated totals.
