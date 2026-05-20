# Treatment and acceptance

## Table of contents

1. [Treatment options](#treatment-options)
2. [Decision criteria](#decision-criteria)
3. [Mitigation plans](#mitigation-plans)
4. [Transfer and avoid](#transfer-and-avoid)
5. [Risk acceptance](#risk-acceptance)
6. [Re-review triggers](#re-review-triggers)

## Treatment options

| Option | When to use |
|---|---|
| **Mitigate** | Cost-effective controls reduce residual below appetite |
| **Transfer** | Insurance, contractual liability shift, outsourced control with assurance |
| **Avoid** | Stop activity, retire system, or exclude data from scope |
| **Accept** | Residual within appetite, or cost exceeds benefit with executive approval |

Record **one primary** treatment per risk; secondary actions in mitigation plan notes.

## Decision criteria

Compare options on:

- **Residual risk** after treatment (re-score)
- **Cost** (CapEx, OpEx, opportunity cost)
- **Time** to implement vs regulatory or contract deadline
- **Dependencies** (other projects, vendors)
- **Side effects** (UX, availability, technical debt)

Document why rejected options were not chosen for audit and committee readability.

## Mitigation plans

Each mitigation task needs:

| Field | Requirement |
|---|---|
| Owner | Named individual, not a team mailbox |
| Due date | Realistic; tie to release or vendor milestone |
| Success criteria | Measurable (e.g., MFA enforced 100% admins) |
| Verification | Rescan, test, or control attestation |
| Risk link | Register ID |

Escalate overdue **high/critical** mitigations to risk committee monthly.

## Transfer and avoid

**Transfer:**

- Cyber insurance: confirm coverage matches scenario (ransomware, privacy liability)
- Contracts: security exhibits, SLAs, audit rights—coordinate with legal; risk analyst frames **residual** after contract controls
- Cloud shared responsibility: inherit provider controls only with cited evidence (`cloud-compliance-specialist`)

**Avoid:**

- Decommission system, disable feature, or stop processing sensitive data class
- Update register: status **closed** or **avoided** with approver and date

## Risk acceptance

Required when residual remains **above appetite**:

1. Written rationale (business benefit, constraints, compensating controls)
2. **Approver** at delegated authority level (see governance reference)
3. **Expiry date** (max 12 months; critical max 6 months)
4. **Compensating controls** if any (monitoring, manual checks)
5. Link to incident and audit obligations if acceptance fails

Store acceptance in the same system as the risk register; no oral-only acceptances.

## Re-review triggers

Re-open treatment or acceptance when:

- Expiry date reached
- Related incident or near-miss
- Material control change or audit failure
- Vendor breach or contract change
- Risk appetite statement updated

Default: full register review **quarterly**; critical rows **monthly** until residual within appetite.
