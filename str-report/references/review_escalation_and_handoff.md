# Review escalation and handoff

## Table of contents

1. [Review stages](#review-stages)
2. [Analyst self-QA](#analyst-self-qa)
3. [Second-line MLRO review](#second-line-mlro-review)
4. [Legal and tipping-off](#legal-and-tipping-off)
5. [MLRO handoff package](#mlro-handoff-package)
6. [Escalation triggers](#escalation-triggers)
7. [Post-filing actions](#post-filing-actions)
8. [Distinguishing handoff types](#distinguishing-handoff-types)

## Review stages

| Stage | Owner | Outcome |
|---|---|---|
| 1. Draft | AML analyst | Complete narrative + exhibits |
| 2. Peer review | Senior analyst / team lead | Fact-check, typology coherence |
| 3. Compliance / MLRO | MLRO delegate | Filing decision, edits |
| 4. Legal (optional) | Counsel | Privilege, LE, novel issues |
| 5. Filing | MLRO / authorized filer | Submission to FIU |
| 6. Post-filing | Compliance ops | Acknowledgment, retention, monitoring |

Document **version**, **reviewer**, and **date** on each circulation.

## Analyst self-QA

Before escalating, confirm:

- [ ] Scope and date range stated in opening
- [ ] Subject identifiers match KYC system
- [ ] Transaction totals reconcile to source export
- [ ] Chronology ordered and timezone noted
- [ ] Each red flag tied to cited facts
- [ ] Benign explanations documented
- [ ] Exhibits numbered and referenced
- [ ] No customer notification / tipping-off language in external drafts
- [ ] Prior STR/SAR checked
- [ ] Spell-check and remove alert boilerplate

## Second-line MLRO review

MLRO typically assesses:

| Question | Action if “no” |
|---|---|
| Is suspicion **reasonable** based on facts? | Return for more investigation |
| Are **identifiers** sufficient for FIU? | Request KYC update or appendix |
| Is **timing** correct for filing deadline? | Expedite or document delay reason |
| Is **continuing activity** handled? | Amend or new report per policy |
| **Group / entity** correct? | Reassign filing entity |

MLRO may **edit narrative tone**, **shorten**, or **request legal** review—analyst provides clean track-changes version.

## Legal and tipping-off

Engage **`commercial-counsel`** when:

- Filing vs **no-file** decision has legal ambiguity
- **DAML / moratorium** (UK) or similar freeze regimes
- **Subpoena** or LE request overlaps with STR
- **Privilege** concerns (audit, investigation by counsel)
- **Cross-border** sharing restrictions

**Tipping-off**: restrict distribution to need-to-know; watermark drafts “CONFIDENTIAL — AML INVESTIGATION”.

## MLRO handoff package

Deliver a single package (folder or case system bundle):

1. **Cover memo** (1 page): case ID, recommendation (file / do not file / hold), deadline, risks
2. **STR narrative** (final draft)
3. **Chronology & aggregation tables**
4. **Subject / account appendix**
5. **Exhibit index** with files attached
6. **Alert & investigation notes** (fact extracts)
7. **Prior filings** copies if continuing
8. **Open questions** list
9. **Filing form worksheet** (field mapping)

### Cover memo template (structure)

| Section | Content |
|---|---|
| Recommendation | File STR/SAR / defer / no file |
| Summary | 2–3 sentences |
| Amount in scope | Total + period |
| Key typologies | Bullets |
| Urgency | Deadline, LE interest, reputational |
| Open items | What MLRO must decide |

## Escalation triggers

Escalate immediately to MLRO (and legal if policy requires) when:

- **Sanctions true match** or blocked transaction attempted
- **TF/PF** indicators (`aml-cft` supplement)
- **Insider** or **employee** involvement suspected
- **Material customer** (PEP, government, large commercial relationship)
- **Media / regulatory** inquiry linked to case
- **Law enforcement** already engaged
- **Group-wide** or multi-entity exposure
- **Crypto** high-risk exposure beyond institution appetite
- **Data breach** affecting investigation integrity

## Post-filing actions

After MLRO files (operational—not narrative drafting):

| Action | Owner |
|---|---|
| Store acknowledgment / submission ID | Compliance ops |
| Update case system status | Analyst |
| **Continuing monitoring** plan | Analyst + TM |
| **Retention** per schedule | Records management |
| **No tipping-off** customer communications | Front-line policy |
| **Management information** | Periodic MI to board |

Do not reference STR filing in **customer-facing** messages unless counsel approves specific script.

## Distinguishing handoff types

| Handoff | Recipient | Content focus |
|---|---|---|
| **MLRO filing** | Compliance / FIU | Full STR package |
| **Internal audit** | Auditor | Process sample—not full STR unless audit scope |
| **Law enforcement** | Agency via legal | Referral facts; may differ from STR |
| **Parent company** | Group compliance | Summary per group policy |
| **Technology** | Engineering | Only if data quality issue—no STR narrative |

**Internal case notes** may contain speculative content; **strip** before MLRO package unless explicitly included and approved.

For audit of **AML process** (not STR drafting), route to **`auditor`**. For **TM governance**, route to **`aml-compliance`**.
