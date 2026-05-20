# Targeted financial sanctions and asset freeze

## Table of contents

1. [Concepts](#concepts)
2. [TFS lifecycle](#tfs-lifecycle)
3. [Screening integration](#screening-integration)
4. [Match disposition](#match-disposition)
5. [Asset freeze workflow](#asset-freeze-workflow)
6. [Delisting and licenses](#delisting-and-licenses)
7. [Governance and records](#governance-and-records)
8. [Limitations](#limitations)

## Concepts

**Targeted financial sanctions (TFS)** — financial measures directed at named **persons, entities, vessels, aircraft**, or groups (terrorist, proliferation, territorial integrity, etc.) without necessarily imposing comprehensive country embargoes.

**Asset freeze (blocking)** — obligation to **prevent** access to funds and economic resources, hold assets without transfer, and reject transactions benefiting designated parties, subject to jurisdictional rules and exceptions.

**Consolidated lists** — national and international lists (e.g., UN, OFAC, EU, UK) updated frequently. **Multiple list regimes** may apply to a single institution.

This reference describes **operational concepts**—not legal interpretation of sanctions programs.

## TFS lifecycle

```text
List update → Screening refresh → Match → Investigation → Disposition
     │                                              │
     └──────────── Freeze / Block / Reject ◄────────┘
```

1. **Ingest** list updates on schedule (intraday where required)
2. **Rescreen** customer and transaction populations per policy
3. **Detect** matches (name, alias, ID, vessel IMO, etc.)
4. **Investigate** true vs false positive with audit trail
5. **Act** freeze, block, or reject; notify compliance/legal
6. **Report** to competent authority when mandated
7. **Review** periodic unfreeze/delisting and license grants

## Screening integration

| Layer | CFT role |
|---|---|
| Customer onboarding | Sanctions + PEP at admission; block account opening on true TFS |
| Periodic rescreen | Event-driven and scheduled; include NPO and MVTS agents |
| Payments | Real-time or near-real-time wire screening |
| Trade | Party, bank, vessel, port screening where supported |
| Crypto | Address screening (heuristic); treat as decision support only |

Coordinate with `information-security-engineer` for feed latency, parsing, and case tooling—not list legal interpretation.

Pointer: `chainalysis-sanctions-screening` for public API/oracle engineering patterns.

## Match disposition

| Outcome | Action |
|---|---|
| False positive | Document rationale; allow processing; retain evidence |
| Possible true match | Hold transaction/account; escalate to sanctions team |
| True match / confirmed designation | **Freeze**; stop outflows; restrict services per policy |
| Inconclusive | Escalate; do not release pending senior/compliance decision |

Record: analyst, timestamp, list version, matching fields, rationale, approver.

**Do not** inform the customer of a filing or investigation in ways that violate tipping-off rules—follow local law and policy.

## Asset freeze workflow

Conceptual steps (adapt to jurisdictional and institutional policy):

1. **Hold** accounts and pending transactions immediately on confirmed match
2. **Block** cards, wires, trading, and crypto withdrawals as applicable
3. **Inventory** balances, positions, and economic resources (including joint accounts per policy)
4. **Notify** internal legal/compliance and MLRO
5. **File** required reports to competent authority within prescribed timelines (counsel confirms)
6. **Communicate** with relationship managers only on need-to-know basis
7. **Document** all actions for exam and audit

**Reject** incoming funds that would benefit a designated party when policy requires rejection vs freeze.

## Delisting and licenses

| Situation | Guidance |
|---|---|
| Delisting / name removal | Rescreen; documented unfreeze approval; release holds |
| General or specific **license** | Only legal/counsel initiates; operations execute approved payments |
| Humanitarian exceptions | Jurisdiction-specific; never assume without written approval |
| Partial hits (e.g., common names) | Enhanced due diligence; do not auto-freeze without policy |

## Governance and records

- **Policy** — TFS scope, roles (first/second line), escalation, freeze authority
- **Procedures** — match investigation, freeze, rejection, reporting, unfreeze
- **Training** — tellers, payments ops, trade finance, crypto desk
- **Testing** — independent review of sample matches and timeliness
- **Retention** — list versions, match records, freeze logs, authority communications

Map themes to **FATF Recommendation 6** (TFS) in program documentation.

## Limitations

- Do not advise whether a party **is** legally designated—that is counsel/list publisher domain
- Do not configure vendor rules as sole compliance control without governance
- No circumvention guidance—ever
- Public screening APIs (e.g., Chainalysis public sanctions) are **supplemental**, not exhaustive
