# Standards and assessment

## Table of contents

1. [IEC 62443 (high level)](#iec-62443-high-level)
2. [NIST SP 800-82 (high level)](#nist-sp-800-82-high-level)
3. [Assessment approach](#assessment approach)
4. [Gap matrix template](#gap-matrix-template)
5. [Maturity and security levels](#maturity-and-security-levels)
6. [Evidence and limitations](#evidence-and-limitations)

## IEC 62443 (high level)

IEC 62443 (ISA/IEC) is the primary **industrial automation and control systems** security framework family.

| Part / concept | Practitioner use |
|---|---|
| 62443-2-1 | Security management system for IACS — policies, org, risk |
| 62443-2-4 | Service provider security capabilities |
| 62443-3-2 | **Zones and conduits** — aligns with architecture work |
| 62443-3-3 | **System security requirements** — technical controls catalog |
| 62443-4-1 / 4-2 | Product development and component requirements |

**Security Levels (SL-T):** target rigor for a zone or system (SL 1–4). Document **current vs target SL** with compensating controls where target is not achievable short term.

**Do not** claim certification or SL achievement without qualified assessors and site-specific evidence.

## NIST SP 800-82 (high level)

NIST SP 800-82 Rev. 3 provides **guide to ICS security** for U.S. federal and general industry reference.

| Section theme | Map to deliverables |
|---|---|
| ICS characteristics | Justify why IT controls fail (availability, legacy, protocols) |
| Risk management | OT-specific risk register tied to process impact |
| Recommended controls | Crosswalk to architecture, monitoring, IR |
| Network architectures | Purdue, segmentation, wireless |
| Security capabilities | Monitoring, vulnerability, configuration management |

Use 800-82 as **structuring guide** for gap assessments and roadmaps; pair with site standards and sector regulators (NERC CIP, FDA, etc.) when applicable — **not legal interpretation**.

## Assessment approach

1. **Kickoff** — scope sites/units, safety rules, blackout periods, interview list (OT ops, IT, vendors)
2. **Documentation** — network diagrams, asset lists, change control, remote access, prior incidents
3. **Walkthrough** — physical and logical; identify shadow IT and ad-hoc conduits
4. **Passive observation** — where approved: SPAN/tap, asset discovery tools in listen-only mode
5. **Control testing** — configuration review, sampling; **no active exploit or production scanning**
6. **Gap analysis** — map findings to IEC 62443-3-3 / 800-82 control families
7. **Roadmap** — phased remediation with operations-owned change windows

| Phase | Duration (typical) | Output |
|---|---|---|
| Scoping | 1–2 weeks | Charter, RACI, safety agreement |
| Assess | 2–8 weeks | Findings, evidence index |
| Remediate planning | 2–4 weeks | Prioritized roadmap |
| Validate | Per phase | Retest checklist, metrics |

## Gap matrix template

| ID | Finding | Zone/asset | IEC 62443 ref | NIST 800-82 ref | Severity | Compensating control | Owner | Target date |
|---|---|---|---|---|---|---|---|---|
| OT-001 | Example: flat VLAN between HMI and PLC | L2/L1 | SR 5.1 | Network segmentation | High | ACL on switch (interim) | OT network | Q3 |

Severity guidance: combine **cyber exposure** with **process/safety impact** (not CVSS alone).

## Maturity and security levels

| Maturity (example) | Characteristics |
|---|---|
| 1 Initial | Informal OT security; shared passwords; flat networks |
| 2 Managed | Asset list started; some segmentation; patch ad hoc |
| 3 Defined | Zones/conduits documented; remote access controlled; IR exercised |
| 4 Measured | Metrics on vulns, sessions, anomalies; regular tabletops |
| 5 Optimized | Continuous improvement; vendor assurance; aligned SL-T |

## Evidence and limitations

Collect: diagrams, firewall exports, jump server configs, patch records, training logs, tabletop AARs.

**Limitations to state explicitly:**

- Passive-only assessment may miss misconfigurations on unused ports
- Vendor black-box PLCs limit firmware assurance
- Safety systems may be out of scope for cyber assessors
- This skill does not provide **legal compliance opinions** — route to `compliance-specialist` and counsel
