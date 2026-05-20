# Strategic briefings and stakeholders

## Table of contents

1. [Audience types](#audience-types)
2. [Briefing structure](#briefing-structure)
3. [Language discipline](#language-discipline)
4. [Recommendations and investments](#recommendations-and-investments)
5. [Coordination with executives](#coordination-with-executives)

## Audience types

| Audience | Needs | Format |
|---|---|---|
| **CISO / board** | Risk themes, sector exposure, major shifts, investment asks | 1–2 pages; BLUF; minimal jargon |
| **SOC / hunt leads** | Actionable TTPs, priorities, IOC context | Tactical annex; links to handoffs |
| **IR leadership** | Active campaign tie-in, timeline hypotheses | Operational brief; UTC timeline |
| **Risk / GRC** | Scenarios, control gaps, third-party exposure | Risk-oriented framing |
| **IT / cloud leadership** | Platform-specific gaps (identity, SaaS, edge) | Technical recommendations list |
| **Legal / comms** | Facts vs judgment; publication risk | Attribution memo without overstatement |

Route board-ready narratives through `chief-information-security-officer` when that function owns executive messaging.

## Briefing structure

**Strategic APT brief (recommended sections):**

1. **Bottom line up front** — 3 bullets: who/what risk/what changed
2. **Situation** — campaign status (active/dormant), sectors, geographies
3. **Adversary overview** — cluster or actor name with confidence; avoid sensationalism
4. **Tradecraft highlights** — ATT&CK themes in plain language
5. **Organizational exposure** — validated vs potential; gaps in visibility
6. **Recommendations** — prioritized actions (monitor, hunt, harden, escalate)
7. **Confidence and gaps** — what would change the assessment
8. **Annexes** — IOC/TTP tables for technical consumers

**Time-sensitive flash:** BLUF, change log since last brief, immediate actions, handling.

## Language discipline

- **Observations** — “We observed LDAP reconnaissance on Host-A at UTC …”
- **Judgments** — “We assess with moderate confidence that …”
- **Assumptions** — “Assuming campaign remains active …”
- Avoid **certainty inflation** — “may,” “likely,” “suggests” with confidence labels
- Avoid **vendor name soup** — one primary label plus alias footnote
- Do not state **legal guilt**, **sanctions violations**, or **breach notification** outcomes

## Recommendations and investments

Tie recommendations to **defender outcomes**, not tool brands:

- Identity hardening (phishing-resistant MFA, PAM, tiering)
- Logging and retention for high-value data sources
- Edge and VPN patch cadence for known exploited vulnerabilities
- Supply-chain monitoring for critical vendors
- Tabletop exercises for sector-relevant APT scenarios

Classify recommendations:

- **Immediate (0–7 days)** — active risk
- **Near-term (30 days)** — hunt and detection backlog
- **Strategic (quarter+)** — architecture and program investments

## Coordination with executives

Before **external attribution** or **public sector naming**:

1. Align with `chief-information-security-officer` on messaging and appetite for uncertainty
2. Involve legal/comms for state-sponsored or victim-sensitive content
3. Prepare **Q&A** — “What if wrong?” “What are we doing?” “How do we know?”
4. Schedule **refresh cadence** — monthly for watch-list actors; ad hoc for active campaigns

Strategic briefs should enable **decisions**, not demonstrate analytic volume.
