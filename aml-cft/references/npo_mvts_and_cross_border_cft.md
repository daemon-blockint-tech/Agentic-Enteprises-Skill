# NPO, MVTS, and cross-border CFT

## Table of contents

1. [NPO sector risk](#npo-sector-risk)
2. [NPO due diligence](#npo-due-diligence)
3. [MVTS and remittance](#mvts-and-remittance)
4. [Cross-border and correspondent TF](#cross-border-and-correspondent-tf)
5. [De-risking governance](#de-risking-governance)
6. [Monitoring scenarios](#monitoring-scenarios)
7. [Limitations](#limitations)

## NPO sector risk

Nonprofit and charitable organizations are **legitimate** and often essential. A subset is abused for **terrorist financing** through diverted donations, affiliate entities, and weak governance.

FATF **Recommendation 8** calls for focused, risk-based oversight of NPOs—not blanket exclusion of the sector.

| Risk factor | Examples |
|---|---|
| Governance | No board oversight; related-party transactions |
| Geography | Operations or transfers to conflict/high-TF regions |
| Transparency | No public annual reports; unaudited accounts |
| Flows | Round amounts; rapid pass-through; cash intensity |
| Affiliation | Links to designated persons or sanctioned entities (screening) |

## NPO due diligence

Apply **proportionate** measures by risk tier:

| Tier | Examples | Measures |
|---|---|---|
| Low | Registered local charity, transparent accounts | Standard CDD + sanctions |
| Medium | Cross-border programs, cash collection | EDD elements, purpose verification |
| High | High-risk geography, opaque governance, law enforcement interest | Senior approval, enhanced monitoring, possible exit |

**Due diligence elements** (select by tier):

1. Verify legal registration and governance structure
2. Understand mission, programs, and geographic footprint
3. Obtain financial statements or alternative assurance where available
4. Identify **beneficial owners**, directors, and signatories; screen all
5. Document **intended use** of accounts and expected transaction profile
6. Set **transaction limits** and alert scenarios aligned to stated purpose
7. Refresh on triggers (media, designation, suspicious activity)

Route **legal** questions on NPO regulation to `commercial-counsel`; route **CDD policy** gaps to `aml-compliance`.

## MVTS and remittance

**Money or value transfer services** (including remittance providers, currency exchanges, and agent networks) are high-risk for **TF** when agents lack oversight.

| Control theme | Implementation concepts |
|---|---|
| Licensing | Verify regulatory authorization in each jurisdiction |
| Agent management | Agent agreements, audits, termination for breaches |
| KYC | Sender and beneficiary identification per corridor rules |
| Limits | Caps, velocity controls, structuring detection |
| Corridors | Country risk scoring; deny high-risk where policy requires |
| Settlement | Reconcile nostro/vostro; detect pass-through without economic purpose |

**Red flags:** unlicensed agents; smurfing across branches; beneficiary lists inconsistent with sender profile; commingling with unrelated commercial flows.

## Cross-border and correspondent TF

| Risk | Mitigation concepts |
|---|---|
| Nested accounts | Identify underlying customers; refuse opaque nesting |
| Payable-through | Restrict where policy prohibits |
| Respondent banks | Due diligence, certifications, periodic review |
| Wire stripping | Detect missing originator/beneficiary information |
| Trade overlap | Coordinate with trade finance PF/TF typologies |
| Crypto corridors | VASP due diligence; travel rule where applicable (`aml-compliance`) |

Document **correspondent risk assessment** updates when corridors or products change.

## De-risking governance

**De-risking** (terminating relationships or corridors) may be necessary but should be governed:

1. **Risk-based** decision with documented rationale—not reputation alone
2. **Approval** by committee or second line for high-impact exits
3. **Consider** humanitarian impact where relevant (counsel input)
4. **Avoid** tipping off where law restricts customer explanation
5. **Monitor** for **displacement** to less regulated channels (inform management)

Do not use this skill to advise evading regulatory expectations through offshore shells.

## Monitoring scenarios

Examples to map to TM or manual review (calibrate locally):

- NPO account outflows to unrelated commercial entities
- Donation spikes after geopolitical events then rapid outbound wires
- MVTS same beneficiary from many senders (mule-like)
- Cross-border wires with incomplete originator data
- Correspondent concentration to high-TF jurisdiction without business rationale

Separate **CFT** queue or tags where possible for analyst training.

## Limitations

- NPO regulatory requirements vary widely by country
- Do not label organizations terrorist without designation or lawful process
- MVTS licensing research is not legal advice
- Correspondent exit decisions need compliance and business alignment
