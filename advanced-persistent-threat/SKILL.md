---
name: advanced-persistent-threat
description: |
  Guides advanced persistent threat (APT) analysis—nation-state and sophisticated criminal
  campaigns, long-dwell intrusions, campaign lifecycle tracking, MITRE ATT&CK TTP mapping,
  infrastructure and malware correlation, attribution with explicit confidence levels,
  intel fusion for hunts and IR, detection-engineering handoffs, and executive strategic
  briefings. Use for APT, advanced persistent threat, nation-state threat, state-sponsored
  campaign, long-dwell intrusion, APT attribution, campaign tracking, APT infrastructure,
  strategic threat briefing, sophisticated intrusion analysis—not routine SOC alert triage
  (soc-analyst), generic proactive hunt playbooks only (threat-hunter), CTI feed and source
  management only (cti-analyst), incident command (incident-responder), penetration testing
  (penetration-tester), or AI/LLM red team (ai-redteam).
---

# Advanced Persistent Threat (APT) Analyst

## When to Use

- Analyze **nation-state or sophisticated criminal** operations with **long dwell times** and multi-stage objectives
- **Track campaigns** across victims, infrastructure, malware families, and time (lifecycle, resurgence, retooling)
- Map adversary behavior to **MITRE ATT&CK** at technique and procedure level with evidence and coverage gaps
- Correlate **infrastructure, malware, and tradecraft** into activity clusters before naming actors
- Apply **attribution discipline**—confidence levels, alternative hypotheses, and leadership-appropriate language
- **Fuse intelligence** from CTI, internal telemetry summaries, IR timelines, and hunt findings into APT assessments
- Package **detection-engineering and hunt handoffs** prioritized for sustained, evasive adversaries
- Draft **strategic briefings** for leadership on threat landscape, sector risk, and defensive investment implications

## When NOT to Use

- Triage SIEM/EDR alerts, run SOAR playbooks, or close SOC queues → `soc-analyst`
- Execute hypothesis-driven hunt campaigns and query packs (primary) → `threat-hunter`
- Manage CTI collection plans, source vetting, STIX/TAXII sharing, or feed operations (primary) → `cti-analyst`
- Declare incidents, lead containment, or draft regulatory/legal conclusions → `incident-responder`
- Authorized exploitation, vuln validation, or pentest deliverables → `penetration-tester`
- AI/LLM application red team, prompt injection, or model abuse testing → `ai-redteam`
- Define enterprise security strategy, ISMS, or board GRC roadmaps (primary) → `cybersecurity`
- Implement SIEM rules, feed parsers, or platform engineering (primary) → `information-security-engineer`

## Related skills

| Need | Skill |
|---|---|
| CTI collection, source vetting, IOC/TTP packages, STIX sharing | `cti-analyst` |
| Proactive hunt campaigns, SIEM query packs, hunt reporting | `threat-hunter` |
| Alert triage, enrichment playbooks, SOC escalation | `soc-analyst` |
| Declared incident command, containment, stakeholder IR | `incident-responder` |
| Security program, threat-informed strategy, governance | `cybersecurity` |
| Feed ingestion, detection platform implementation | `information-security-engineer` |
| Enterprise security architecture, control frameworks | `enterprise-security-architect` |
| Board and executive security communications | `chief-information-security-officer` |

## Consumer handoff chain

1. **`cti-analyst`** — vets sources and produces IOC/TTP packages; APT analysis **consumes** and **extends** with campaign depth and attribution rigor.
2. **`advanced-persistent-threat`** — synthesizes long-horizon campaign picture, infrastructure graphs, attribution confidence, and strategic implications.
3. **`threat-hunter`** — falsifiable hypotheses and query packs for evasive, low-signal adversaries.
4. **`soc-analyst`** — enrichment context for rare alerts tied to known APT campaigns (not campaign analysis).
5. **`incident-responder`** — operational timeline support; APT does **not** command incidents.

Escalate **active compromise** immediately to `incident-responder`. Do not delay containment for finished attribution.

## Core Workflows

### 1. Scope and definitions

1. Confirm the ask is **APT-shaped** (sustained, resourced, multi-stage—not commodity smash-and-grab)
2. Define analytic horizon (active campaign, historical cluster, sector watch)
3. Set audience, classification, and **attribution publication bar**
4. Document known gaps and what evidence would change the assessment

**See `references/apt_scope_and_definitions.md`.**

### 2. Campaign tracking and TTPs

1. Build **campaign timeline**—first seen, peaks, retooling, suspected end or ongoing flag
2. Map **attack chain** from initial access through objectives with evidence pointers
3. Align behaviors to **MITRE ATT&CK**; note procedure detail and detection data sources
4. Track **victimology** and sector/geography patterns without overfitting single incidents

**See `references/campaign_tracking_and_ttps.md`.**

### 3. Infrastructure and malware

1. Graph domains, IPs, certs, hosting, CDNs, and fast-flux or bulletproof patterns
2. Cluster **malware families**, loaders, configs, and code-signing abuse
3. Record infrastructure **resurrection** after takedowns and shared-hosting false leads
4. Separate **commodity overlap** from actor-specific tradecraft

**See `references/infrastructure_and_malware_analysis.md`.**

### 4. Attribution and confidence

1. Maintain **activity cluster IDs** until naming threshold is met
2. Score confidence per analytic line; document **alternative explanations**
3. Separate “cluster behavior” from “equals public group X” claims
4. Route state-sponsored or naming publications through leadership/comms review

**See `references/attribution_and_confidence.md`.**

### 5. Detection and hunting handoffs

1. Prioritize **durable behaviors** over brittle IOCs for APT tradecraft
2. Package hunt hypotheses, data-source requirements, and expected false-positive notes
3. Draft **detection-engineering backlog**—candidate logic, tuning, logging gaps
4. Link artifacts to campaign ID and confidence metadata

**See `references/detection_and_hunting_handoffs.md`.**

### 6. Strategic briefings

1. Lead with **bottom line**—who, what risk, what changed, what to do
2. Separate observations, judgments, and assumptions for executive readers
3. Tie recommendations to **risk appetite**, sectors, and control investments
4. Coordinate with `chief-information-security-officer` for board-ready narratives when needed

**See `references/strategic_briefings_and_stakeholders.md`.**

## When to load references

- **Role boundaries and APT definitions** → `references/apt_scope_and_definitions.md`
- **Campaign lifecycle and ATT&CK** → `references/campaign_tracking_and_ttps.md`
- **Infrastructure and malware correlation** → `references/infrastructure_and_malware_analysis.md`
- **Attribution and confidence** → `references/attribution_and_confidence.md`
- **Hunt and detection handoffs** → `references/detection_and_hunting_handoffs.md`
- **Executive and stakeholder briefings** → `references/strategic_briefings_and_stakeholders.md`

## Outputs

- **APT assessment** — campaign summary, timeline, TTPs, infrastructure/malware clusters, confidence, gaps
- **Activity cluster profile** — internal ID, aliases, targeting, tradecraft themes, linked incidents
- **ATT&CK coverage map** — observed techniques, procedures, detection opportunities, telemetry gaps
- **Infrastructure/malware annex** — graphs, IOC context, resurrection notes, commodity-overlap flags
- **Attribution memo** — evidence lines, confidence, alternatives, publication recommendations
- **Hunt/detection handoff** — prioritized hypotheses, query seeds, detection backlog, consumer routing
- **Strategic brief** — leadership-ready threat landscape and defensive implications
