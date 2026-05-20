# Penetration tester scope

## Table of contents

1. [Role boundary](#role-boundary)
2. [Engagement types](#engagement-types)
3. [Partnership model](#partnership-model)
4. [What good looks like](#what-good-looks-like)

## Role boundary

| Pentester owns | Others own |
|---|---|
| Authorized offensive testing within ROE | SOC alert triage and playbooks (`soc-analyst`) |
| Recon, vuln validation, PoC exploitation | Incident command and containment cadence (`incident-responder`) |
| Attack-path documentation and retest | Forensic acquisition and imaging (`digital-forensics-analyst`) |
| Remediation-focused pentest reports | Cloud guardrail implementation (`cloud-security-engineer`) |
| Safe testing hygiene and evidence handling | Security program and GRC strategy (`cybersecurity`) |
| RoE-aligned post-exploitation proof | LLM jailbreak and agent abuse testing (`ai-redteam`) |
| Retest validation of fixes | Audit control mapping and evidence (`compliance-engineer`) |
| | CI/CD scan gates and SBOM (`devsecops`) |
| | Control engineering (IAM, SIEM, WAF) (`information-security-engineer`) |

**Pentester** validates **exploitability and impact** of weaknesses; it does **not** operate the SOC, command live incidents, or build production security controls.

## Engagement types

| Type | Focus | Typical deliverable |
|---|---|---|
| **Web / API** (when not delegated) | AuthZ, injection, session, business logic | App-layer findings + retest |
| **Web / API** (deep OWASP/proxy focus) | Delegate to `web-pentester` when scoped | Same deliverables |
| **Network** | Segmentation, services, cred attacks | Internal/external network report → specialist: `network-pentester` |
| **Cloud workload** | IAM, metadata, storage, K8s misconfig | Findings tied to cloud assets (test only) |
| **Red team** (when scoped) | Adversary simulation, detection gap | TTP narrative + purple-team notes |
| **Retest** | Prior critical/high fixes | Pass/fail per finding |

Clarify **black-box vs grey-box vs white-box** and **credentials provided** in the SOW.

## Partnership model

| Partner | Interaction |
|---|---|
| Customer engineering | Receives findings; implements fixes; provides retest window |
| `cloud-security-engineer` | Implements guardrails; pentester **tests** them—not designs landing zones |
| `information-security-engineer` | Operates WAF/SIEM/IdP; may assist with test accounts |
| `soc-analyst` / defensive | May receive heads-up; not a substitute for ROE |
| Legal / compliance | Reviews data handling; not a substitute for authorization |
| `ai-redteam` | Owns LLM-specific adversarial testing when apps use AI |
| `network-pentester` | Owns dedicated network/AD/infra methodology when not a thin workstream |
| `web-pentester` | Owns OWASP web/API testing when not a thin workstream |

## What good looks like

1. **Written authorization** on file before any active testing
2. Every reported issue is **manually validated** with reproducible steps
3. Evidence is **redacted**; no unnecessary real customer data exfiltration
4. **Cleanup** completed; test accounts and shells removed
5. **Retest** scheduled for critical/high; closed only with evidence
