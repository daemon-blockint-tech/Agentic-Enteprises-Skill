# Alert triage and classification

## Table of contents

1. [Triage sequence](#triage-sequence)
2. [Severity matrix](#severity-matrix)
3. [Incident categories](#incident-categories)
4. [False positive handling](#false-positive-handling)
5. [Escalation triggers](#escalation-triggers)

## Triage sequence

Execute in order; do not skip validation for noisy rules.

1. **Acknowledge** — claim case; start SLA clock
2. **Normalize** — extract entities (user, host, IP, hash, domain, process)
3. **Enrich** — asset owner, criticality, recent similar alerts
4. **Decide** — FP / benign TP / TP requiring investigation
5. **Classify** — severity + category + scope count
6. **Act** — playbook, monitor, or escalate

## Severity matrix

Align to org SEV definitions (`incident-management-engineer`). Default mapping:

| Level | Indicators | SOC response |
|---|---|---|
| **SEV1** | Active ransomware, mass exfil, domain-wide compromise | Immediate escalation; 24/7 IR; commander |
| **SEV2** | Confirmed account takeover, privilege escalation, C2 on critical asset | < 1 hour; IR engaged; containment per runbook |
| **SEV3** | Suspicious activity; single-system malware; policy violation with risk | Same business day; Tier 2 owner |
| **SEV4** | Recon, blocked attack, low-confidence signal | Queue; trend; batch review |

**Customer impact** and **data class** override raw alert priority.

## Incident categories

Use one primary category per case for reporting:

| Category | Examples |
|---|---|
| Malware | EDR block, suspicious binary, persistence |
| Phishing | Credential harvest, malicious link |
| Account compromise | Impossible travel, MFA fatigue, token theft |
| Insider / policy | DLP, unauthorized access, data mishandling |
| Network | C2 beacon, port scan, firewall deny spikes |
| Cloud | Anomalous API, IAM change, public exposure |
| Vulnerability | Exploit attempt on known CVE |
| Other | Document when none fit; propose new taxonomy |

## False positive handling

Document before close:

- Detection or rule ID
- Why benign (maintenance, known tool, expected admin, mis-tuned threshold)
- Proposed tuning (threshold, enrichment, time window, scoped allowlist)
- **Expiry date** for any allowlist
- Approver for changes affecting critical ATT&CK techniques

Never permanently suppress high-fidelity techniques without detection review.

## Escalation triggers

Escalate immediately when any apply:

- Executive or break-glass account involved
- Regulated or restricted data (PHI, PCI, export-controlled)
- Lateral movement or scope unknown beyond **10** hosts/users
- Active C2 or encryption of production data
- Legal, regulatory notification, or external comms may be required
- Playbook has no approved branch for observed behavior

Package escalation: 2-line executive summary, timeline link, IOC list, actions taken, open questions.
