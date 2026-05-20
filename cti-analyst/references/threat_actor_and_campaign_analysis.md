# Threat actor and campaign analysis

## Table of contents

1. [Definitions](#definitions)
2. [Actor profiling](#actor-profiling)
3. [Campaign analysis](#campaign-analysis)
4. [Attribution discipline](#attribution-discipline)
5. [Product structure](#product-structure)

## Definitions

- **Threat actor** — cluster of activity with shared infrastructure, malware, TTPs, and targeting (may map to named group or uncategorized cluster)
- **Campaign** — time-bounded operation with coherent objectives, tools, and victims
- **Activity cluster** — technical grouping before confident actor naming

Use internal **cluster IDs** until attribution meets your org’s bar; avoid public naming without review.

## Actor profiling

Build profiles from **observable behavior**, not marketing names alone:

1. **Motivation hypothesis** — financial, espionage, disruption, hacktivism (label as assessment)
2. **Targeting** — sectors, geographies, org sizes, technology stacks
3. **Capabilities** — access brokering, 0-day use, living-off-the-land, cloud expertise
4. **Infrastructure** — registrars, hosting, CDNs, bulletproof patterns, fast-flux
5. **Malware and tools** — families, loaders, RATs, ransomware affiliates, commodity vs custom
6. **TTP themes** — initial access, persistence, C2, exfil patterns (ATT&CK-aligned)
7. **Relationships** — affiliates, overlap with other groups, shared developers

Maintain **alias list** (vendor names, government designations) with source for each mapping.

## Campaign analysis

1. **Scope** — start/end estimates, still-active flag, linked incidents
2. **Victimology** — who was hit, how compromises were discovered (where known)
3. **Attack chain** — staged narrative from delivery through impact (evidence-backed)
4. **Infrastructure graph** — domains, IPs, certs, hosting; note takedown/resurrection
5. **Malware trajectory** — new variants, packers, config changes
6. **Countermeasures observed** — defender actions that altered actor behavior
7. **Forecast** — likely next targets or TTP shifts (low confidence unless strong signals)

## Attribution discipline

- **Minimum evidence bar** — define internally (e.g., multiple independent technical lines + targeting consistency)
- **Separate levels** — “activity attributed to Cluster-A” vs “Cluster-A equals PublicName-B”
- **State sponsored claims** — require highest bar; expect leadership and comms review
- **Do not attribute from IOC alone** — shared hosting and commodity malware mislead
- **Document alternative explanations** — red team, insider, criminal opportunists

Never present attribution as **legal fact**; it is analytic judgment subject to revision.

## Product structure

**Actor profile (living doc):**

- Summary (3–5 bullets), key TTPs, recent campaigns, IOC/TTP pointers, confidence, gaps, last updated

**Campaign flash:**

- Bottom line, timeline, targeting, TTPs, IOC package link, recommended actions by consumer, handling

**Strategic note (leadership):**

- Themes across campaigns, risk to org, investment implications—not raw IOC tables

Route operational detail to `threat-hunter`, `soc-analyst`, and `incident-responder` via `intel_briefs_and_consumer_handoff.md`.
