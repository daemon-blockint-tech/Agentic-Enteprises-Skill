# SSP and control inheritance

## Table of contents

1. [SSP structure](#ssp-structure)
2. [Control selection and baselines](#control-selection-and-baselines)
3. [Inheritance and common controls](#inheritance-and-common-controls)
4. [Control narratives](#control-narratives)

## SSP structure

Typical SSP sections (adapt to program template):

| Section | ISSO focus |
|---|---|
| System identification | Name, identifier, owner, environment |
| System categorization | Impact level, rationale |
| Authorization boundary | Components in and out of scope |
| System environment | Architecture summary, data flows (documentation level) |
| Security requirements | Baseline controls, overlays, tailoring |
| Control implementation | Status per control, inheritance pointers |
| Continuous monitoring | Frequencies, roles, metrics |
| Appendices | Diagrams, procedures index, related plans |

Keep the SSP **accurate as-implemented** — not aspirational. Track deltas in a change log.

## Control selection and baselines

1. Confirm baseline (e.g., moderate/high) and applicable overlays for classified processing
2. Document tailoring decisions with ISSM or AO concurrence where required
3. Map compensating controls to gaps with explicit risk discussion
4. Align control selection with actual components (do not inherit controls that do not apply)

## Inheritance and common controls

| Pattern | ISSO action |
|---|---|
| Fully inherited | Reference common control provider SSP section; no duplicate narrative |
| Hybrid | Split provider vs system-specific implementation |
| Not inherited | Full narrative and evidence for system boundary |
| Leveraged authorization | Cite other system's authorization date and scope limits |

For each inherited control, record:

- Provider name and point of contact
- Authorization date (or POA&M if provider is deficient)
- Customer responsibilities (system-specific portion)
- Evidence pointer (ticket, scan, attestation location)

## Control narratives

Each implemented control narrative should answer:

1. **What** is enforced (policy, config, procedure)
2. **Who** operates it (role, team)
3. **How often** (continuous, daily, monthly, event-driven)
4. **Evidence** (repository, ticket type, log retention)
5. **Exceptions** (open POA&M or risk acceptance reference)

**Good narrative:** "Privileged access reviews occur quarterly; owner is IAM team; evidence in GRC tool ticket series PRV-YYYY-Qn; exceptions tracked in POA&M 2024-017."

**Weak narrative:** "Access reviews are performed per policy."

Refresh narratives when tooling, ownership, or frequency changes.
