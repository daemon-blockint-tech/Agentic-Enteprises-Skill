# Narrative structure and quality

## Table of contents

1. [Standard narrative arc](#standard-narrative-arc)
2. [Who what when where why](#who-what-when-where-why)
3. [Opening and closing paragraphs](#opening-and-closing-paragraphs)
4. [Fact vs inference vs opinion](#fact-vs-inference-vs-opinion)
5. [Tone and language](#tone-and-language)
6. [Common defects](#common-defects)
7. [Quality review checklist](#quality-review-checklist)

## Standard narrative arc

Use a **pyramid + chronology** hybrid:

1. **Lead** — one paragraph stating suspicion in plain language
2. **Subject context** — who the customer is, relationship, risk rating, KYC highlights
3. **Chronological facts** — what happened, in order
4. **Suspicion synthesis** — why the pattern is unusual vs expected profile
5. **Actions taken** — holds, EDD, account restrictions (factual)
6. **Closing** — ongoing monitoring, continuing activity flag, request for MLRO decision

Regulators often skim the **first and last** paragraphs first—make them precise.

## Who what when where why

### Who

- Legal name, aliases, customer type (individual, corporate, trust, VASP)
- Identifiers: national ID, tax ID, LEI, registration number (as available)
- **Beneficial owners** and control persons when relevant
- **Related parties**: joint account holders, authorized signers, nested counterparties
- Role of **reporting institution** (account holder, intermediary, correspondent)

### What

- Products: accounts, wires, cards, crypto, trade finance, lending
- **Instruments** and channels: online, branch, ATM, API, DeFi interface (describe factually)
- **Transaction types**: deposits, withdrawals, internal transfers, FX, trade settlements
- **Volumes**: counts, totals, velocity—aggregated where helpful

### When

- Anchor dates: account opening, profile changes, alert generation, key transactions
- State **timezone** assumption (UTC vs local)
- Note **gaps** in data (missing statements, delayed feed)

### Where

- Countries of customer, counterparty, and transaction endpoints
- **High-risk geography** references only when tied to facts (not generic lists)
- IP or device geolocation **only** if verified and policy-allowed

### Why (suspicious)

- Link each **red flag** to specific facts (see `references/red_flags_and_typologies.md`)
- Compare activity to **stated purpose**, **KYC occupation/source of funds**, and **peer group**
- Document **benign hypotheses** considered and why insufficient

## Opening and closing paragraphs

### Opening (example structure—not boilerplate to copy)

> [Institution] reports suspicion regarding [subject], account(s) [IDs], for the period [dates]. Activity is inconsistent with the customer’s known profile because [2–3 fact-based reasons]. Total in-scope volume is [amount] across [n] transactions.

### Closing (example structure)

> Based on the above, [institution] requests MLRO review for [STR/SAR filing / internal escalation]. Continuing activity [is / is not] expected. Open items: [list].

Avoid **legal conclusions** (“money laundering occurred”) unless institution policy and counsel direct specific phrasing.

## Fact vs inference vs opinion

| Category | Usage in STR narrative |
|---|---|
| **Fact** | “On 2024-03-12, account 123 received EUR 9,800 from counterparty X.” |
| **Inference** | Label clearly: “This pattern is consistent with structuring because…” |
| **Opinion** | Minimize; prefer “appears inconsistent with profile” over “customer is dishonest” |

Use footnotes or exhibit IDs for **document-derived** facts: “(Exhibit 4 — March statement).”

## Tone and language

- **Objective**, **professional**, **active voice** where clarity helps
- Avoid jargon unless standard in your jurisdiction (define once)
- Do not include **alert rule names** unless policy requires—describe behavior
- Redact **unnecessary PII** in wide-distribution drafts
- No **marketing** language or customer praise/discount narratives unrelated to suspicion

### Sensitive topics

- **Tipping-off**: do not inform customer of STR preparation in narrative drafts circulated broadly
- **Sanctions/PEP**: factual status only; disposition per policy
- **Crypto**: describe on-chain facts at summary level unless MLRO wants annex; deep traces → blockint skills

## Common defects

| Defect | Fix |
|---|---|
| Narrative contradicts transaction table | Reconcile amounts and dates |
| Suspicion with no supporting transaction | Add facts or remove assertion |
| Wall of unaggregated transactions | Summarize + appendix |
| Copy-paste alert text without context | Rewrite in plain language |
| Missing subject identifiers | Complete KYC appendix |
| Speculation about criminal organization | Stick to observable patterns |
| Duplicate STR for same facts | Check prior filings; note continuing activity |

## Quality review checklist

Before MLRO submission, confirm:

- [ ] Lead paragraph states suspicion and scope
- [ ] All five W dimensions addressed
- [ ] Chronology matches source systems
- [ ] Amounts and currencies consistent throughout
- [ ] Red flags explicitly tied to facts
- [ ] Benign explanations addressed
- [ ] PII minimized per distribution policy
- [ ] Exhibits referenced and listed
- [ ] Prior STR/SAR noted if relevant
- [ ] Open questions listed for MLRO
- [ ] Disclaimer: draft for compliance—not legal filing advice
