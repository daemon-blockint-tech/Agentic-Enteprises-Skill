# Intake and triage

## Table of contents

1. [Intake channels](#intake-channels)
2. [Triage workflow](#triage-workflow)
3. [Severity assignment](#severity-assignment)
4. [Researcher communication](#researcher-communication)

## Intake channels

- **Dedicated email** — alias with ticketing integration
- **Web form / portal** — structured fields (asset, steps, impact)
- **Bug bounty platform** — HackerOne, Bugcrowd, Intigriti, etc.
- **Internal** — red team, employees via internal channel (separate queue if needed)

Log every report with: received time, channel, reporter identity (if known), duplicate-of link.

## Triage workflow

1. **Ack** — auto-reply with ticket ID and policy link; human ack within SLA for critical
2. **Dedupe** — same root cause, same component; merge tickets
3. **Reproduce** — security engineering or delegated product team; document result
4. **Severity** — apply rubric; record CVSS vector if used
5. **Assign DRI** — engineering owner for fix; TPM tracks dates
6. **Disclosure track** — open embargo record if external reporter

**Out of scope** — respond with policy pointer; do not debate at length.

**Spam / noise** — close with template; no bounty.

## Severity assignment

Balance **technical severity** and **exploitability in context**:

| Factor | Raises severity |
|---|---|
| Unauthenticated remote code execution | Critical |
| Auth bypass on admin functions | Critical / High |
| Stored XSS on high-traffic surface | High |
| IDOR on sensitive customer data | High |
| Information disclosure of non-sensitive metadata | Low |

Disputes: security lead decides; document decision in ticket.

## Researcher communication

Templates should cover:

- Acknowledgment and expected next steps
- Request for clarification or retest steps
- Severity notification (without promising bounty amount in email)
- Extension request for disclosure date (rationale, new date)
- Fix deployed — invite retest
- Publication notice and credit line (if offered)
- Closure — duplicate, not applicable, or resolved

**Do not** share customer data, internal URLs, or other researchers’ reports.
