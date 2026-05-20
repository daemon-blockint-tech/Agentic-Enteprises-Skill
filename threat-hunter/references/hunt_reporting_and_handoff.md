# Hunt reporting and handoff

## Table of contents

1. [Report structure](#report-structure)
2. [Findings table](#findings-table)
3. [Escalation to IR](#escalation-to-ir)
4. [Return to SOC](#return-to-soc)
5. [Metrics and program feedback](#metrics-and-program-feedback)

## Report structure

Every hunt ends with a written report (ticket wiki or doc). Minimum sections:

1. **Executive summary** — hypothesis, outcome (found / not found / inconclusive), business impact
2. **Scope** — time range (UTC), systems, data sources, exclusions
3. **Method** — queries, baselines, intel used (with citations)
4. **Findings** — table below with confidence
5. **ATT&CK coverage** — techniques observed or ruled out
6. **Actions** — detections filed, IR escalation, IT fixes, monitoring
7. **Appendix** — query pack, IOC list, redacted samples

Separate **facts** from **inferences**. Mark speculative links clearly.

## Findings table

| ID | Entity | Behavior | Technique | Evidence | Confidence | Action |
|---|---|---|---|---|---|---|
| F-1 | user@corp | Impossible travel + new device | T1078 | IdP logs link | High | Escalate IR |
| F-2 | host-12 | Rare PowerShell parent | T1059.001 | EDR link | Medium | Monitor 72h |

Confidence:

- **High** — ready for containment discussion with IR
- **Medium** — needs SOC monitoring or short follow-up hunt
- **Low** — document only; do not drive disruptive response

## Escalation to IR

Hand off to `incident-responder` when declaration criteria are met (confirmed malicious activity, data exposure suspected, ransomware, active C2, widespread compromise, regulatory trigger).

**IR handoff package** must include:

- Hunt ID and hypothesis
- UTC timeline of key events (attacker-relevant and defender-relevant)
- Affected users, hosts, accounts, apps, regions, data classes (if known)
- IOC table (type, value, first/last seen, source)
- Saved searches or log excerpts with pointers (not unbounded exports)
- Actions already taken (if any) and approval chain
- Open questions and recommended next containment steps (suggestions only—IR commands)

**Do not** declare the incident in place of IR unless you are the designated incident commander.

If live attacker activity is suspected, **notify IR immediately** by phone/page per severity matrix; finish the written package in parallel.

## Return to SOC

When hunts close **without** incident criteria:

- Send summary to originating analyst with **tuning guidance**
- List alerts to close or link to parent ticket
- Note **benign root causes** (change ticket, new software, pen test IP ranges)
- Attach detection tickets for long-term improvement

SOC owns ongoing alert queue health; hunters do not become permanent tier-3 backlog.

## Metrics and program feedback

Track for hunt program maturity (share with `cybersecurity`):

- Hunts per quarter by trigger type
- **Time to first finding** and total effort
- **Detection yield** — new or improved rules from hunts
- **Incidents spawned** — hunts that escalated to IR
- **Inconclusive rate** and top data gaps

Use metrics to justify logging investments, not to penalize “not found” hunts—negative results improve coverage maps.
