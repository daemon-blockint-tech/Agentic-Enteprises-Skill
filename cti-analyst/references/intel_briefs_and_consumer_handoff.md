# Intel briefs and consumer handoff

## Table of contents

1. [Brief types](#brief-types)
2. [Writing standards](#writing-standards)
3. [Handoff to threat hunter](#handoff-to-threat-hunter)
4. [Handoff to SOC](#handoff-to-soc)
5. [Handoff to incident responder](#handoff-to-incident-responder)
6. [Maintenance and retraction](#maintenance-and-retraction)

## Brief types

| Type | Audience | Horizon | Content emphasis |
|---|---|---|---|
| **Strategic** | Executives, risk, board | Months–quarters | Themes, actor trends, geopolitical drivers, investment implications |
| **Tactical** | SOC leads, hunt leads, IR managers | Weeks | Active campaigns, sector targeting, prioritized TTPs/IOCs |
| **Operational** | IR, hunt, tier-2 SOC | Hours–days | Immediate actions, evolving IOCs, incident-specific hypotheses |
| **Flash** | Mixed | Breaking | 1-page: what happened, so what, what to do now |

Match length to urgency: operational flashes are short; strategic assessments may be longer with appendices.

## Writing standards

1. **BLUF** — bottom line up front in the first paragraph
2. **Separate** observations (sourced facts) from judgments (analysis)
3. **Confidence** on every major judgment
4. **Actionable recommendations** per consumer role
5. **Handling banner** — TLP/classification on every page
6. **Glossary** — actor cluster IDs, internal codenames
7. **No hype** — avoid sensational attribution or certainty theater

## Handoff to threat hunter

Package for `threat-hunter`:

1. **Falsifiable hypotheses** — “If campaign X active, expect Y in Z logs”
2. **ATT&CK focus** — techniques to hunt this week
3. **Seed IOCs and entities** — with confidence and FP notes
4. **Data source hints** — which telemetry should show activity
5. **Time window** — UTC bounds aligned to campaign reporting
6. **Out of scope** — systems or hypotheses deferred

Do not assign hunt execution to CTI; hunters own queries and findings.

## Handoff to SOC

Package for `soc-analyst`:

1. **Tiered IOC list** — block vs enrich-only
2. **Alert correlation context** — lure themes, subject lines, tool names
3. **Expected false positives** — updaters, security scanners, CDNs
4. **Playbook tweaks** — not full playbook rewrites unless agreed with SOC lead
5. **Watch items** — emerging TTPs without solid IOCs yet

SOC owns triage outcomes; CTI does not close alerts.

## Handoff to incident responder

Package for `incident-responder` during active incidents:

1. **Operational brief** tied to incident ID and scope
2. **Timeline hypotheses** — reporting dates vs possible intrusion dates (labeled)
3. **Actor/campaign context** with attribution uncertainty
4. **Evolving IOCs** — versioned; highlight deltas since last send
5. **Questions for IR** — what evidence would confirm or refute lines of analysis

Escalate immediately if intel suggests **active C2, ransomware prep, or data staging**—do not wait for polished prose.

IR owns declaration, containment, and comms; CTI supports with intel only.

## Maintenance and retraction

1. Set **review date** on every IOC and major judgment
2. Publish **updates** with change log (added/removed/changed confidence)
3. **Retract** incorrect IOCs explicitly; notify consumers who received them
4. Archive superseded briefs; point to current version ID
5. Post-incident: capture **lessons for collection** (what sources helped or failed)
