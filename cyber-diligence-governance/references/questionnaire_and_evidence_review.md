# Questionnaire and evidence review

## Table of contents

1. [Questionnaire types](#questionnaire-types)
2. [Review process](#review-process)
3. [Evidence standards](#evidence-standards)
4. [Consistency and stale answers](#consistency-and-stale-answers)
5. [SME routing](#sme-routing)
6. [Outbound vs inbound](#outbound-vs-inbound)

## Questionnaire types

| Type | Notes |
|---|---|
| SIG / CAIQ | Standardized; map to internal baseline and library |
| Custom Excel / portal | Watch for ambiguous questions; document interpretations |
| Customer security review | Outbound — align with compliance library |
| Target / vendor inbound | This skill’s primary review mode |
| Lightweight attestation | Accept only for low tier with spot checks |

## Review process

1. **Triage** — due date, tier, repeating vs net-new, deal sensitivity
2. **Assign** — cyber diligence lead coordinates; SMEs own sections
3. **Answer mapping** — map each question to control theme and required evidence
4. **Verify** — attach evidence or flag “assertion only”
5. **Gap list** — partial/missing controls with severity
6. **Approval** — security delegate before external send (outbound) or internal sign-off (inbound summary)
7. **Archive** — version, date, approver, evidence links for reuse

## Evidence standards

Acceptable evidence hierarchy (strongest first):

1. **Independent third-party report** (SOC 2, ISO) — check period, scope, exceptions, bridge letter
2. **Test results** — pen test executive summary, vuln scan with remediation status
3. **Operational records** — tickets, access reviews, change records (sampled)
4. **Configuration / architecture** — diagrams, screenshots with date and system ID
5. **Policy / procedure** — necessary but insufficient alone

Reject or downgrade when:

- Report is **expired** or wrong entity (parent vs subsidiary)
- Scope excludes material services
- Marketing PDF with no auditor or test metadata
- “Planned” or “roadmap” without committed date and owner

## Consistency and stale answers

Before reusing library answers (outbound) or trusting target responses (inbound):

| Check | Action |
|---|---|
| Same question, conflicting answers | Resolve with SME; document final position |
| Post-incident | Block reuse until security lead refresh |
| Post-M&A / reorg | Update subprocessors, IdP, and data flows |
| Certification lapse | Do not cite old SOC; request updated report or bridge |

Mark answers **stale** if older than 6 months for critical tier (adjust per policy).

## SME routing

| Section theme | Typical SME |
|---|---|
| Organizational / governance | Security leadership or GRC |
| Identity / access | IAM or `iam-specialist` patterns |
| Cloud / network | Cloud security or engineering |
| App / SDLC | Appsec or engineering leadership |
| IR / BC | IR lead; BCM references for recovery claims |
| Privacy / data | Privacy office; legal for legal interpretations |
| AI / ML use of data | `ai-risk-governance` for model-specific claims |

Cyber diligence lead **integrates** SME input into one findings narrative.

## Outbound vs inbound

| Direction | Primary owner | This skill’s role |
|---|---|---|
| Outbound (you answer customer) | `compliance-specialist` + library | Support deep deals; ensure consistency with diligence findings |
| Inbound (you assess vendor/target) | Cyber diligence lead | Lead analysis and evidence review |

Never state technical controls that engineering has not validated. Route unvalidated claims to `information-security-engineer` before external submission.
