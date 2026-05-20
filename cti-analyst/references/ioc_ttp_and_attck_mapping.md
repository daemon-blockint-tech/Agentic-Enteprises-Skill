# IOC, TTP, and ATT&CK mapping

## Table of contents

1. [IOC types and quality](#ioc-types-and-quality)
2. [IOC package standards](#ioc-package-standards)
3. [TTP documentation](#ttp-documentation)
4. [MITRE ATT&CK mapping](#mitre-attck-mapping)
5. [Consumer guidance](#consumer-guidance)

## IOC types and quality

| Type | Examples | Quality checks |
|---|---|---|
| **Network** | IP, domain, URL, JA3/JA4, User-Agent | Shared CDN/hosting? Active vs historical? |
| **Host** | File hash, mutex, registry, path | Sample availability? Prevalence? |
| **Email** | Subject, sender pattern, attachment hash | Campaign-specific vs generic spam? |
| **Cloud** | Account IDs, bucket names, OAuth app IDs | Tenant-specific vs public artifact? |

Reject or downgrade **low-fidelity IOCs** (popular cloud ranges, generic strings, one-time scan noise).

## IOC package standards

Each IOC entry should include:

1. **Value** — normalized (lowercase domain, SHA-256, etc.)
2. **Type** — per taxonomy used by consumers (STIX indicator types as reference)
3. **Context** — campaign, malware, role (C2, staging, phishing)
4. **First seen / last seen** — UTC; note if estimated
5. **Source** — feed, report ID, internal case
6. **Confidence** — for this IOC’s maliciousness in stated context
7. **Recommended action** — block, hunt, monitor, do not block (with rationale)
8. **Expiration** — review date; auto-expire noisy indicators
9. **False positive notes** — known benign use (CDN, updater, security tool)

Provide **machine-readable export** (CSV, STIX bundle) and **human summary** (top 10 priority).

## TTP documentation

Document TTPs at two levels:

- **Technique** — ATT&CK technique ID (e.g., T1566 Phishing)
- **Procedure** — actor-specific implementation (lure themes, attachment types, follow-on)

For each TTP:

1. Link **evidence** (report excerpt, detection, sample behavior)
2. Note **required telemetry** — what logs prove or disprove the TTP
3. List **detection ideas** — sigma/KQL concepts for `threat-hunter` / detection engineering
4. State **gaps** — if procedure is inferred not observed

## MITRE ATT&CK mapping

1. Map to **enterprise** (or ICS/mobile/cloud) matrix as appropriate
2. Prefer **sub-technique** granularity when evidence supports it
3. Build **ATT&CK navigator layer** for campaigns when consumers use it
4. Document **coverage**: reported TTP vs org visibility to detect
5. Avoid **checkbox mapping** — only map techniques with evidence or strong inference (labeled)

Cross-check vendor ATT&CK mappings; they are starting points, not ground truth.

## Consumer guidance

| Consumer | Deliver | Avoid |
|---|---|---|
| **SOC** | High-confidence block IOCs; enrichment context; FP warnings | Huge untiered feed dumps |
| **Threat hunt** | TTPs + seed IOCs + hypotheses + data sources | Premature attribution certainty |
| **IR** | Timeline-aligned TTPs; evolving IOCs; attribution uncertainty | Blocking actions without IR coordination |
| **Engineering** | STIX objects, feed requirements, parser fields | Policy mandates without implementation detail |
| **Leadership** | Risk themes, targeting relevance | Raw indicator tables |

Coordinate blocklist changes with `information-security-engineer` and incident state with `incident-responder` when active.
