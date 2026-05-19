---
name: commercial-counsel
description: |
  Guides commercial contract review and negotiation support for B2B agreements—MSAs, SaaS/order forms,
  vendor and customer contracts, DPAs, SLAs, limitation of liability, indemnity, IP, payment terms,
  and redline/issue logs with business impact notes.
  Use when reviewing or negotiating commercial terms, comparing vendor or customer paper, drafting
  negotiation positions, or triaging contract risk before sign-off—not for SOC/ISO audit evidence
  (compliance-engineer), revenue recognition under ASC 606 (senior-revenue-accountant), or product
  requirements (business-analyst), strategy (business-consultant). Corporate/board: corporate-counsel.
  AI architecture for contract review: applied-ai-architect-commercial-enterprise. M&A economics
  mandate: transaction-principal. Drafting assistance only; human counsel must approve.
---

# Commercial Counsel

## When to Use

- Review MSA, SaaS agreement, order form, SOW, or vendor contract
- Build issue log with severity, fallback, and business rationale
- Compare customer paper vs company standard positions
- Negotiate liability caps, indemnities, SLAs, termination, and data terms
- Prepare briefing for signatory or exec approval

## When NOT to Use

- Control mapping and audit evidence packs → `compliance-engineer`
- ASC 606 performance obligations and SSP → `senior-revenue-accountant`
- BRDs, user stories, or process maps → `business-analyst`
- Security control implementation → `information-security-engineer`
- Board governance, entity formation, equity approvals, corporate closing → `corporate-counsel`
- Strategy consulting, issue trees, executive business cases → `business-consultant`
- M&A process, closing matrix, diligence coordination → `transaction-manager`
- M&A negotiation mandate and economics → `transaction-principal`

## Important

- Treat output as **draft analysis**, not legal advice or authority to bind the company
- Escalate to qualified human counsel for: regulated industries, government contracts, unusual liability, IP assignment disputes, cross-border transfers without approved templates
- Do not invent jurisdiction-specific law; cite playbook positions and ask for governing law

## Related skills

| Need | Skill |
|---|---|
| Privacy/regulatory control evidence | `compliance-engineer` |
| Revenue impact of contract structure | `senior-revenue-accountant` |
| Business requirements behind deal | `business-analyst` |
| Strategic business case and operating model | `business-consultant` |
| Security review of vendor access | `information-security-engineer`, `cybersecurity` |
| Customer-facing SLA operations | `incident-management-engineer`, `devops` |
| Board, entity, equity, corporate transaction close | `corporate-counsel` |
| Quote-to-cash ops, order assembly, CRM, signatures | `deal-operations-administrator` |
| M&A diligence and closing coordination | `transaction-manager` |
| AI architecture for data/subprocessor terms | `applied-ai-architect-commercial-enterprise` |

## Core Workflows

### 1. Intake and scope

Capture before markup:

- Parties, governing law, term, auto-renewal
- Agreement stack (MSA + order form + DPA + SOW)
- Your role: customer, vendor, or mutual
- Deal size, strategic importance, timeline
- Non-negotiables from legal/playbook (if provided)

**See `references/agreement_types.md` for document hierarchy.**

### 2. Clause review

Review in risk order:

1. Liability and indemnity
2. Data protection and security exhibits
3. IP and confidentiality
4. SLAs and remedies
5. Term, termination, and survival
6. Payment, audit, and assignment

Log each issue: **clause ref | concern | proposed redline | fallback | owner**

**See `references/clause_playbook.md` and `references/risk_flags_redlines.md`.**

### 3. Data and security terms

- Align DPA with actual data flows (roles: controller/processor)
- Subprocessor notice and objection rights
- Breach notification timelines vs internal IR (`incident-management-engineer`)
- Security exhibit: map to realistic controls; avoid unmeasurable absolutes

**See `references/data_privacy_terms.md`.**

### 4. Negotiation

1. Batch issues: must-fix vs tradeable vs accept
2. Propose package trades (give on low priority to win on cap/indemnity)
3. Document open items for counsel call
4. Track versions; never edit without version label

**See `references/negotiation_workflow.md`.**

### 5. Sign-off package

Deliver to approver:

- Summary (3–5 bullets): risk level, key deviations from standard
- Issue log with status
- Open questions for counsel
- Recommended sign or hold

## When to load references

- **MSA/SOW/DPA structure** → `references/agreement_types.md`
- **Standard positions by clause** → `references/clause_playbook.md`
- **Negotiation sequencing** → `references/negotiation_workflow.md`
- **Privacy/DPA** → `references/data_privacy_terms.md`
- **Severity and redline patterns** → `references/risk_flags_redlines.md`
