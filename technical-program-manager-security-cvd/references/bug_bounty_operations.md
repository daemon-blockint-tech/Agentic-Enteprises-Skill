# Bug bounty operations

## Table of contents

1. [Program setup](#program-setup)
2. [Scope management](#scope-management)
3. [Reward workflow](#reward-workflow)
4. [Platform hygiene](#platform-hygiene)
5. [Researcher relations](#researcher-relations)

## Program setup

Align bounty with CVD policy:

| Element | Decision |
|---|---|
| Platform | Public, private invite, VDP-only |
| Scope | Assets in policy; wildcards documented |
| Rules | Safe harbor, testing constraints, out-of-scope |
| Severity → reward matrix | $ ranges per tier; cap per report |
| SLA | Platform ack; internal same as CVD triage |

Launch checklist: legal review of terms, security review of scope, comms for announcement, support briefed on bounty vs support tickets.

## Scope management

- Update scope when new products launch or domains retire
- Mark **out-of-scope** clearly (third-party, physical, social engineering unless allowed)
- **Rate limits** and DoS — prohibit destructive testing in rules
- Sync scope with **attack surface** owners quarterly

## Reward workflow

1. Triage validates finding (same bar as non-bounty CVD)
2. Severity set → reward tier from matrix
3. **Mediation** — platform dispute process; TPM documents decision
4. Payout — finance/tax forms per platform; timing in SLA

Do not promise reward in triage before validation. **Duplicates** — split or deny per policy.

## Platform hygiene

- Close stale submissions with reason
- Tag components for reporting analytics
- Export metrics: submissions, valid, payout, mean time to bounty
- Rotate program admins; least privilege on platform

## Researcher relations

- Thank-you for valid reports; professional tone on declines
- **Hall of fame** — opt-in credit on advisory
- **Repeat researchers** — consistent DRIs; avoid re-triage by new analysts each time
- **Conferences** — coordinate swag or invites with comms/legal

Escalate harassment, threats, or extortion to security leadership and legal immediately — outside normal bounty flow.
