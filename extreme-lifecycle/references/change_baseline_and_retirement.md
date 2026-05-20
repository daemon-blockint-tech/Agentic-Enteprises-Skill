# Change, baseline, and retirement

## Table of contents

1. [Configuration baseline concepts](#configuration-baseline-concepts)
2. [Baseline types](#baseline-types)
3. [Change categories](#change-categories)
4. [Change authorization workflow](#change-authorization-workflow)
5. [Promotion across environments](#promotion-across-environments)
6. [Decommissioning planning](#decommissioning-planning)
7. [Data disposition](#data-disposition)
8. [Retirement verification and closeout](#retirement-verification-and-closeout)

## Configuration baseline concepts

A **configuration baseline** is an identified, approved set of configuration items at a point in time.

| Term | Meaning |
|---|---|
| **Configuration item (CI)** | Software, hardware, IaC, doc, or interface under CM |
| **Baseline ID** | Unique label (e.g., BL-2026.03.1-prod) |
| **Manifest** | Enumerated CIs with versions, hashes, locations |
| **Delta** | Approved change set from prior baseline |

**Authoritative source:** manifest in CM repository—not tribal knowledge.

## Baseline types

| Type | When established |
|---|---|
| **Functional baseline** | Approved requirements/design snapshot |
| **Allocated baseline** | Design allocated to build elements |
| **Product baseline** | Build verified, ready for deploy |
| **Operational baseline** | Running in production |
| **Retired baseline** | Final snapshot before destruction |

Align naming with org CM standards; consistency matters more than terminology.

## Change categories

| Category | Examples | Governance |
|---|---|---|
| **Standard** | Pre-approved low-risk (patch cadence) | Catalog + audit |
| **Normal** | Feature, config, dependency upgrade | CAB or tiered review |
| **Emergency** | Active incident mitigation | Expedited approve + reconcile |
| **Major** | Architecture shift, platform migration | Full design/verify cycle |

Map categories to **criticality tier** (`mission-critical`) when available.

## Change authorization workflow

Minimum workflow:

1. **Request** — description, rationale, affected CIs, rollback
2. **Impact** — traceability, dependents, security/privacy
3. **Approve** — authority per category and tier
4. **Implement** — in controlled environments
5. **Verify** — tests and scans per policy
6. **Promote** — update manifest; archive prior baseline
7. **Communicate** — ops, dependents, assurance consumers

**Reject** changes that lack rollback or baseline update plan.

## Promotion across environments

| Environment | Purpose | Baseline rule |
|---|---|---|
| Dev | Experimentation | May lag; not authoritative |
| Test / staging | Verification | Must match candidate product baseline |
| Production | Authoritative ops | Only promoted operational baseline |

**Promotion record** links: source tag, target tag, gate ID, approver, timestamp.

Pair `build-validator` for **pre-flight** on major promotions—not as substitute for baseline CM.

## Decommissioning planning

Start decommissioning plan when dispose phase triggers (see `operate_sustain_and_obsolescence.md`).

Plan sections:

| Section | Content |
|---|---|
| Scope | Systems, environments, integrations to shut down |
| Dependencies | Consumers notified; migration paths |
| Sequence | Order of shutdown (stop ingress → drain → disable → remove) |
| Roles | Who executes, who witnesses, who approves |
| Rollback window | If any, time-boxed and tested |
| Communications | Internal/external notification (generic templates) |
| Evidence | Logs and sign-offs required |

## Data disposition

Classify data **generically**; execute per organizational policy and legal hold:

| Disposition | When | Evidence |
|---|---|---|
| **Retain / archive** | Regulatory or business retention | Archive location, index, access controls |
| **Migrate** | Successor system needs data | Migration verification, cutover record |
| **Destroy** | No retention requirement | Certificate of destruction, crypto erase logs |
| **Anonymize** | Analytics-only residual | Method doc and validation sample |

**Do not** specify destruction of data under **legal hold**—escalate to counsel.

Include:

- Backup and replica retirement
- Key and secret revocation
- SaaS tenant closure
- Log pipeline shutdown

## Retirement verification and closeout

Closeout checklist:

- [ ] Production traffic drained; DNS/routes removed
- [ ] Accounts and keys revoked
- [ ] Data disposition completed per plan
- [ ] Final retired baseline archived
- [ ] CMDB status = retired; dependents updated
- [ ] Assurance notified; control inheritance updated (interface)
- [ ] Financial assets and licenses retired (`vp-of-infrastructure` if shared)
- [ ] Lessons learned captured

**Output:** retirement certificate signed by system owner and lifecycle sponsor.
