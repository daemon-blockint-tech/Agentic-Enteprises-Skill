# Collection and source vetting

## Table of contents

1. [Intelligence requirements](#intelligence-requirements)
2. [Collection sources](#collection-sources)
3. [Vetting framework](#vetting-framework)
4. [Fusion and deconfliction](#fusion-and-deconfliction)
5. [Bias and gaps](#bias-and-gaps)

## Intelligence requirements

1. State the **decision** the consumer will make (hunt, block, brief leadership, IR scope, risk treatment)
2. Write IRs as answerable questions: “What TTPs is actor X using against sector Y this quarter?”
3. Prioritize **P1/P2/P3** IRs when timeboxed; defer nice-to-have collection
4. Record **deadline**, **classification**, and **handling** before collection starts
5. Revisit IRs when incidents or new reporting change the priority stack

## Collection sources

| Source type | Typical use | Caveats |
|---|---|---|
| **OSINT** | Infrastructure, leaks, actor claims, malware repos | Poisoned data, impersonation, outdated posts |
| **Commercial feeds** | IOCs, YARA, actor reports, sector overlays | Vendor bias, delayed visibility, license limits |
| **Government / CERT** | Advisories, sector alerts, national priorities | Generalized IOCs, delayed publication |
| **ISAC / ISAO** | Sector campaigns, victim patterns, MISP shares | Need-to-know, handling rules, anonymization |
| **Internal telemetry** | Incidents, hunts, detection hits | Survivorship bias, org-specific noise |
| **Partner / vendor trust** | Closed sharing, incident co-analysis | Trust but verify; contractual limits |

Document **collection plan**: sources per IR, expected latency, owner, and legal/export constraints.

## Vetting framework

Evaluate **source** and **information** separately (adopt or adapt NATO-style axes):

**Source reliability (A–F or High/Med/Low):**

- History of accuracy, transparency, access, and motivation
- Potential for deception, sales bias, or state influence

**Information credibility (1–6 or High/Med/Low):**

- Corroboration, specificity, consistency with other reporting, plausibility
- Proximity to events (primary vs hearsay)

**Vetting steps:**

1. Identify **provenance** — who published, when, under what handling
2. Seek **corroboration** from independent sources before high-confidence claims
3. Flag **circular reporting** — multiple articles citing one original blog
4. Validate **technical artifacts** — sample hashes, passive DNS, certificate overlaps where possible
5. Record **dissent** — conflicting actor attribution or TTP claims
6. Assign **overall confidence** for the analytic line (see `sharing_stix_and_confidence.md`)

## Fusion and deconfliction

1. Normalize IOCs (case, defang format, strip noise) before merging
2. Track **first seen / last seen** and **context** (malware, phishing, C2, scan noise)
3. Merge duplicate actor names; maintain **alias table** with source tags
4. Build **timeline** of reporting vs observed activity (reporting lag is common)
5. When sources disagree, publish **alternative hypotheses** rather than forcing consensus

## Bias and gaps

Document explicitly:

- **Collection gaps** — regions, cloud providers, mobile, OT, languages not covered
- **Visibility bias** — commercial sensors vs government vs victim-only reporting
- **Sector bias** — finance-heavy ISAC vs your industry
- **Recency bias** — over-weighting last 48 hours of news
- **Confirmation bias** — IR or leadership pre-beliefs; seek disconfirming evidence

State what evidence would **raise or lower** confidence (e.g., internal detection of same C2, third-party malware report).
