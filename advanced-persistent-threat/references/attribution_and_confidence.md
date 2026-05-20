# Attribution and confidence

## Table of contents

1. [Definitions](#definitions)
2. [Confidence scale](#confidence-scale)
3. [Attribution levels](#attribution-levels)
4. [Evidence standards](#evidence-standards)
5. [Alternative hypotheses](#alternative-hypotheses)
6. [Publication and naming](#publication-and-naming)

## Definitions

- **Activity cluster** — technical grouping of incidents by shared infrastructure, malware, TTPs, and targeting
- **Threat actor** — durable entity (may map to public group names) once organizational bar is met
- **Attribution** — analytic judgment linking activity to an actor or sponsor (not legal identity proof)
- **Assessment** — judgment with explicit confidence; distinct from **observation** (direct evidence)

## Confidence scale

Use a consistent scale org-wide (example—adapt to internal standards):

| Level | Meaning | Typical use |
|---|---|---|
| **High** | Multiple independent technical lines; consistent targeting; low plausible alternatives | Internal action on actor-specific playbooks |
| **Moderate** | Strong technical link; incomplete targeting or single-source reporting | Hunt prioritization, enhanced monitoring |
| **Low** | Weak or single-indicator link; significant alternatives | Watch item; further collection |
| **Unknown** | Insufficient data | Document gaps; avoid naming |

Apply confidence **per analytic line**, not only to the summary.

## Attribution levels

1. **Level 0 — Uncategorized activity** — techniques observed, no cluster
2. **Level 1 — Activity cluster** — internal ID (e.g., `CLUSTER-FOX-12`)
3. **Level 2 — Cluster matches public reporting** — “consistent with techniques used by GROUP-X per [sources]”
4. **Level 3 — Organizational attribution** — “we attribute CLUSTER-FOX-12 to GROUP-X” with documented bar
5. **Level 4 — Sponsor/state claim** — highest bar; leadership and comms review required

Never skip levels in external products; executives need to see uncertainty.

## Evidence standards

**Stronger evidence:**

- Multiple incidents with custom malware and exclusive infrastructure
- Consistent TTP ordering and tooling over time
- Targeting aligned with known actor objectives
- Independent CTI and internal IR alignment (after vetting via `cti-analyst`)

**Weaker evidence (insufficient alone):**

- Single IOC match on shared host
- Malware family used globally
- ATT&CK technique overlap without procedure detail
- Linguistic or geopolitical inference without technical corroboration

Document **circular reporting**—multiple articles citing one original source.

## Alternative hypotheses

Always list plausible alternatives:

- Different actor sharing commodity tools
- Cybercrime vs state-sponsored motivation
- Insider threat or business email compromise
- Authorized red team or third-party assessment
- False flag or deliberate infrastructure mimicry (rare; do not default to this)

Note what evidence would **confirm or eliminate** each alternative.

## Publication and naming

- Use **internal cluster IDs** in operational channels until review approves external names
- Map **vendor aliases** in a table with source—not all names refer to the same activity
- **State-sponsored attribution** — align with legal, comms, and government relations
- **Law enforcement** — coordinate before public attribution that could affect investigations
- **No attribution from IOC block alone** — pair with tradecraft and campaign context

Attribution is **revisable**; issue update notices when assessments change materially.
