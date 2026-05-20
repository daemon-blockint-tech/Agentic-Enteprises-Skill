---
name: cti-analyst
description: |
  Guides cyber threat intelligence (CTI)—collection and vetting of intel from OSINT, commercial feeds,
  and ISACs; threat actor and campaign analysis; IOC/TTP production with MITRE ATT&CK mapping;
  STIX/TAXII and sharing concepts; strategic, tactical, and operational intel briefs; fusion with
  hunts and incident response; confidence scoring and source handling. Use for CTI, threat
  intelligence, threat actor profiling, IOC production, TTP analysis, intel briefs, STIX, ISAC
  reporting, campaign analysis, APT reporting—not proactive hunt execution (threat-hunter), SOC alert
  triage (soc-analyst), adversary simulation ops (red-team-specialist), incident command
  (incident-responder), or legal conclusions.
---

# CTI Analyst (Cyber Threat Intelligence)

## When to Use

- **Collect and vet** intelligence from OSINT, commercial feeds, government advisories, and ISACs
- **Profile threat actors** and **analyze campaigns** (objectives, targeting, infrastructure, timing)
- **Produce IOCs and TTPs** with MITRE ATT&CK mapping and consumer-ready context
- **Draft intel briefs** (strategic, tactical, operational) for leadership, SOC, hunts, and IR
- **Package sharing artifacts** (STIX concepts, TAXII awareness, distribution tiers, handling rules)
- **Fuse intel** into hunt hypotheses, detection priorities, and active incident context
- **Score confidence** and document sources, limitations, and collection bias

## When NOT to Use

- Execute hypothesis-driven hunts across enterprise telemetry → `threat-hunter`
- Triage SIEM/EDR alerts, run SOAR playbooks, or close SOC queues → `soc-analyst`
- Declare incidents, lead containment, or draft regulatory/legal conclusions → `incident-responder`
- Plan or operate authorized adversary simulation campaigns → `red-team-specialist`
- Define enterprise security strategy, ISMS, or GRC roadmaps → `cybersecurity`
- Implement SIEM rules, feeds, or IAM from intel (primary) → `information-security-engineer`
- Score enterprise risk registers or board heat maps (primary) → `security-risk-analyst`
- Execute authorized pentests or exploitation → `penetration-tester`

## Related skills

| Need | Skill |
|---|---|
| Proactive hunt campaigns, query packs, detection feedback | `threat-hunter` |
| Alert triage, enrichment playbooks, SOC escalation | `soc-analyst` |
| Declared incident command, timelines, stakeholder IR | `incident-responder` |
| Adversary simulation, purple team, detection validation ops | `red-team-specialist` |
| Security program, intel function governance | `cybersecurity` |
| Feed ingestion, STIX parsers, SIEM/EDR integrations | `information-security-engineer` |
| Risk scenarios, treatment from intel-driven threats | `security-risk-analyst` |
| Pentest findings as supplemental technical context | `penetration-tester` |

## Consumer handoff chain

1. **`cti-analyst`** — vets sources, produces briefs, IOC/TTP packages, and confidence-rated assessments.
2. **`threat-hunter`** — converts tactical intel into falsifiable hunt hypotheses and query packs.
3. **`soc-analyst`** — applies IOCs and context to alert enrichment and triage (not intel production).
4. **`incident-responder`** — consumes operational intel during active incidents; CTI supports timelines and attribution hypotheses, not IR command.

CTI does **not** replace hunts, SOC queues, or CSIRT command. Escalate **active compromise** immediately to `incident-responder` with whatever intel exists—do not delay IR for “perfect” attribution.

## Core Workflows

### 1. Requirements and collection plan

1. Capture consumer ask (leadership, SOC, hunt, IR, risk, engineering)
2. Define intelligence requirements (IRs): priority questions, time horizon, sectors, regions
3. Inventory sources (OSINT, commercial, ISAC, internal telemetry summaries); note gaps and bias
4. Set handling, classification, and sharing constraints (TLP, need-to-know, export controls)

**See `references/cti_analyst_scope.md` and `references/collection_and_source_vetting.md`.**

### 2. Source vetting and fusion

1. Evaluate source reliability and information credibility (separate dimensions)
2. Correlate multiple reporting lines; flag single-source or circular citations
3. Deduplicate IOCs; normalize formats; record first-seen and context
4. Document what is **unknown** and what would change the assessment

**See `references/collection_and_source_vetting.md`.**

### 3. Actor and campaign analysis

1. Cluster infrastructure, malware families, and targeting patterns
2. Map to known groups or **uncategorized clusters** with explicit uncertainty
3. Describe campaign timeline, objectives, and likely next actions (as hypotheses)
4. Avoid over-claiming attribution; separate facts from analytic judgment

**See `references/threat_actor_and_campaign_analysis.md`.**

### 4. IOC, TTP, and ATT&CK mapping

1. Publish IOCs with type, context, expiration, and false-positive notes
2. Document TTPs at technique and procedure level where evidence supports it
3. Map to MITRE ATT&CK; note detection opportunities and data-source dependencies
4. Prioritize consumers: block lists vs hunt pivots vs strategic awareness

**See `references/ioc_ttp_and_attck_mapping.md`.**

### 5. Sharing, STIX, and confidence

1. Choose distribution tier and audience-appropriate detail
2. Apply STIX 2.x object concepts (indicator, malware, threat-actor, relationship) when sharing technically
3. Understand TAXII collections as transport—not a substitute for vetting
4. Attach **confidence** and **source** metadata to every analytic line

**See `references/sharing_stix_and_confidence.md`.**

### 6. Briefs and handoff

1. Match format to audience: strategic (risk/themes), tactical (campaign/IOCs), operational (IR/hunt actions)
2. Lead with bottom line; separate observations from judgments
3. Package handoff artifacts for `threat-hunter`, `soc-analyst`, or `incident-responder` as appropriate
4. Schedule review cadence; retract or update stale intel explicitly

**See `references/intel_briefs_and_consumer_handoff.md`.**

## When to load references

- **Role boundaries and IRs** → `references/cti_analyst_scope.md`
- **Collection and vetting** → `references/collection_and_source_vetting.md`
- **Actors and campaigns** → `references/threat_actor_and_campaign_analysis.md`
- **IOCs, TTPs, ATT&CK** → `references/ioc_ttp_and_attck_mapping.md`
- **STIX, sharing, confidence** → `references/sharing_stix_and_confidence.md`
- **Briefs and handoff** → `references/intel_briefs_and_consumer_handoff.md`

## Outputs

- **Collection plan** — IRs, sources, gaps, handling constraints
- **Source vetting notes** — reliability, credibility, circular-reference flags
- **Actor/campaign profile** — timeline, targeting, infrastructure, hypotheses, gaps
- **IOC/TTP package** — normalized indicators, ATT&CK mapping, consumer guidance
- **Intel brief** — strategic, tactical, or operational (audience-specific)
- **Sharing bundle** — STIX-oriented export where applicable; distribution record
- **Handoff memo** — prioritized actions for hunt, SOC, or IR consumers
