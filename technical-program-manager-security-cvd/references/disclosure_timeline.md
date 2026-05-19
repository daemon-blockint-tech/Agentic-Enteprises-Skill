# Coordinated disclosure timeline

## Table of contents

1. [Default timeline](#default-timeline)
2. [Embargo management](#embargo-management)
3. [Extensions](#extensions)
4. [Early disclosure triggers](#early-disclosure-triggers)
5. [Multi-party coordination](#multi-party-coordination)

## Default timeline

1. **Agreement** — reporter accepts coordinated disclosure (implicit via policy or explicit)
2. **Fix window** — engineering delivers validated fix
3. **Embargo end** — publication date (often 0–14 days after fix deploy)
4. **Publication** — advisory, CVE, comms, bounty payout

Record all dates in **disclosure tracker** visible to legal and comms.

## Embargo management

Embargo means: no public details until agreed date.

| Party | Obligation |
|---|---|
| Company | No premature blog, support leaks, or commit messages with exploit detail |
| Reporter | No public disclosure without agreement |
| Internal | Need-to-know; mark tickets confidential |

**Pre-release builds** — restrict access; no public issue titles with exploit strings.

## Extensions

Request extension when:

- Fix complexity underestimated
- Holiday / release freeze
- Retest failed; additional work needed

Communicate to reporter:

- New target date
- Brief reason (not internal blame)
- What changed since last update

Document extension approval (TPM + security lead; legal if near prior public commitment).

## Early disclosure triggers

May accelerate publication without full fix when:

- **Active exploitation** in the wild
- **Leak** or partial public disclosure
- **Regulatory** or customer notification duty (coordinate with legal)

Run parallel **incident response** track; CVD TPM syncs advisory timing with IR comms.

## Multi-party coordination

When issue spans vendors or open source:

- Identify **CVE assignment** owner (CNA vs upstream)
- Align **credit** lines and advisory wording
- Single **coordinated release time** (UTC); use shared calendar invite
- Avoid staggered leaks between parties

TPM owns calendar and checklist — not technical content of upstream patches.
