---
name: defensive-security-analyst
description: |
  Guides defensive security analysis—alert triage, log and SIEM investigation, threat hunting, detection
  engineering basics, MITRE ATT&CK mapping, incident scoping, containment recommendations, and DFIR
  evidence handling for SOC and blue-team analysts.
  Use when investigating security alerts, writing detection rules, tuning false positives, analyzing
  EDR/network/auth logs, building timelines of suspicious activity, recommending containment steps,
  or documenting findings for incident command—not for enterprise security strategy (cybersecurity),
  CI/CD pipeline hardening (devsecops), offensive pentest execution (authorize red team separately), or
  LLM adversarial testing (ai-redteam), or designing on-call rotations and postmortem programs
  (incident-management-engineer).
---

# Defensive Security Analyst

## When to Use

- Triage security alerts from SIEM, EDR, identity, cloud, network, or email systems
- Investigate suspicious activity and build an evidence-backed timeline
- Tune detections, reduce false positives, or map behavior to MITRE ATT&CK
- Run threat hunts from hypotheses, indicators, or recent incident patterns
- Package findings, IOCs, and containment recommendations for incident command

## When NOT to Use

- Define enterprise security strategy, policy, or GRC roadmap → `cybersecurity`
- Execute penetration tests or exploit validation → `offensive-security-analyst`
- Add CI/CD, SBOM, or supply-chain security gates → `devsecops`
- Design SEV programs, on-call rotations, or postmortem process → `incident-management-engineer`
- Implement IdP, KMS, SIEM, EDR, or guardrails as engineering controls → `information-security-engineer`

## Related skills

| Need | Skill |
|---|---|
| Security program, GRC, architecture | `cybersecurity` |
| Pipeline and IaC security | `devsecops` |
| Rollout during active incident | `deployment-strategist` |
| Platform logs and infra forensics | `infrastructure-engineer` |
| Incident comms documentation | `tech-writer-researcher` |
| Authorized pentest or red-team execution | `offensive-security-analyst` |
| Incident commander process, SEV, postmortems | `incident-management-engineer` |

## Core Workflows

### 1. Alert triage

**Triage in order (first 15 minutes):**

1. **Validate alert** — true positive vs false positive vs benign true positive
2. **Scope** — single host, user, tenant, or org-wide?
3. **Severity** — active exploitation vs recon vs policy violation
4. **Priority** — data class, exposure, privilege level of actor
5. **Assign** — owner, escalate to IR lead if SEV1–2

| Outcome | Next step |
|---|---|
| False positive | Tune detection; document FP reason |
| Benign TP | Close with justification; optional allowlist |
| True positive | Open incident; begin investigation |

**See `references/alert_triage.md` for severity matrix and escalation.**

### 2. Investigation and timeline

```
collect sources → normalize UTC timeline → identify IOCs → map ATT&CK → hypothesis → validate
```

**Primary sources:** EDR, auth logs (IdP), proxy/DNS, firewall, cloud audit (CloudTrail etc.), email gateway, DLP.

**Timeline fields:** timestamp UTC, host/user, action, source log, analyst note.

**See `references/investigation_timeline.md` for query patterns and correlation tips.**

### 3. Detection engineering (analyst-facing)

When creating or tuning detections:

1. Define threat behavior in plain language
2. Map to MITRE ATT&CK tactic/technique
3. Specify data source and required fields
4. Write detection logic (Sigma-style or SIEM SPL/KQL)
5. Estimate false positive rate; test on 7–30 days historical data
6. Document response playbook link

**See `references/detection_engineering.md` for rule template and tuning loop.**

### 4. Threat hunting

**Hunt hypothesis format:** "If adversary [objective], we might see [observable] in [data source]."

1. Pick hypothesis from intel, recent incidents, or ATT&CK gap
2. Run hunts across SIEM/data lake
3. Pivot on entities (user, IP, hash, domain)
4. Document negative results (still valuable)

**See `references/threat_hunting.md` for hunt cycles and pivot table.**

### 5. Containment and handoff

**Recommend containment only with approval per runbook:**

| Action | When |
|---|---|
| Disable user session | Compromised credentials |
| Isolate host (EDR network containment) | Active malware/C2 |
| Block IOC at proxy/firewall | Confirmed malicious comms |
| Revoke OAuth/app tokens | Token theft |

Preserve evidence before destructive actions when possible (memory/disk snapshot per policy).

Hand off to IR lead: timeline, IOCs, affected assets, recommended containment, open questions.

**See `references/containment_handoff.md` for IR handoff template and evidence checklist.**

### 6. Reporting

**Analyst finding summary:**

- Executive: 2–3 sentences impact and status
- Technical: timeline, IOCs, root cause hypothesis, evidence refs
- Actions: containment taken, detections added, tickets opened

Redact PII per policy; store raw logs in secure case folder.

**See `references/investigation_timeline.md` for report outline.**

## When to load references

- **Alert triage and severity** → `references/alert_triage.md`
- **Investigation and reporting** → `references/investigation_timeline.md`
- **Detections and tuning** → `references/detection_engineering.md`
- **Threat hunting** → `references/threat_hunting.md`
- **Containment and IR handoff** → `references/containment_handoff.md`
