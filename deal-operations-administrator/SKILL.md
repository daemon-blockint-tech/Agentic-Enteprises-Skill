---
name: deal-operations-administrator
description: |
  Guides deal operations administration—quote-to-cash coordination, deal desk intake and routing,
  CRM opportunity hygiene, order form and SOW assembly, approval workflows, signature tracking,
  and handoffs to legal, finance, and provisioning after customer signature.
  Use when processing a sales deal, preparing order paperwork, running deal desk checklist,
  fixing CRM stage/fields, coordinating signatures, or closing the loop post-signature—not for
  contract legal redlines (commercial-counsel), board or equity approvals (corporate-counsel),
  ASC 606 accounting (senior-revenue-accountant), support tickets after go-live (customer-ops-specialist),
  or M&A/financing closing (transaction-manager).
---

# Deal Operations Administrator

## When to Use

- Intake a closed-won or late-stage opportunity for operational processing
- Validate quote, SKU, term, and discount against approval policy
- Assemble order form, SOW, and exhibit package for signature
- Route deal for legal, security, and finance review with complete metadata
- Track signature status and trigger provisioning or billing setup
- Audit CRM fields and fix broken quote-to-cash handoffs

## When NOT to Use

- Legal negotiation of liability, indemnity, or DPA terms → `commercial-counsel`
- Board resolutions, entity, or cap table → `corporate-counsel`
- Revenue recognition, journal entries, or close → `senior-revenue-accountant`
- Customer support, dunning, or renewal CS playbooks → `customer-ops-specialist`
- Multi-quarter engineering program tracking → `technical-program-manager`

## Related skills

| Need | Skill |
|---|---|
| Compute capex, cloud COGS, chargeback | `compute-accounting-manager` |
| Commercial term review | `commercial-counsel` |
| Corporate approvals for financing/M&A | `corporate-counsel` |
| Revenue accounting and ASC 606 | `senior-revenue-accountant` |
| Post-sale customer success and billing disputes | `customer-ops-specialist` |
| Business case or requirements | `business-analyst`, `business-consultant` |
| Large cross-team launch coordination | `technical-program-manager` |
| Corporate M&A, closing matrix, funds flow | `transaction-manager` |

## Core Workflows

### 1. Deal desk intake

Required fields before processing:

- Account, opportunity ID, owner, segment
- Products/SKUs, quantity, term, start date
- List price, discount %, net ACV/TCV
- Billing frequency and payment terms
- MSA status (signed / dates / link)
- Special terms flag (custom SLA, security exhibit, professional services)

Reject incomplete packages back to sales with a single checklist email.

**See `references/deal_desk_review.md` for validation rules.**

### 2. Approvals

Route in parallel where possible:

| Gate | Typical owner |
|---|---|
| Discount / non-standard pricing | Sales leadership |
| Payment terms | Finance |
| Legal paper | `commercial-counsel` |
| Security questionnaire | `information-security-engineer` or security queue |
| Professional services scope | Services lead |

Document approval IDs and dates in CRM or deal folder.

**See `references/approval_routing.md`.**

### 3. Document assembly

Stack order:

1. MSA (existing or new)
2. Order form / subscription agreement
3. SOW (if services)
4. DPA (if personal data)
5. Exhibits (SLA, security)

Version control: `CustomerName_OrderForm_v3_2025-05-20`

**See `references/quote_to_order.md` for field mapping.**

### 4. Signature and close

- Confirm signatories per delegation of authority (`corporate-counsel` / internal policy)
- Send e-signature envelope; track status daily
- On fully executed: store PDFs in deal folder; update CRM to closed-won booked
- Notify: finance (billing), provisioning, CS onboarding

**See `references/signature_closeout.md`.**

### 5. Post-signature handoff

Handoff package to downstream teams:

- Executed PDFs + redlines summary
- SKU and term table
- Billing contact and PO if any
- Implementation dates and CS owner

**See `references/handoff_revops.md`.**

### 6. CRM hygiene

Weekly hygiene pass:

- Stages match reality (no stuck “negotiation” after signature)
- ACV/TCV matches signed order form
- Primary quote attached; competitor and loss reason populated on lost deals

**See `references/crm_hygiene.md`.**

## When to load references

- **Intake validation** → `references/deal_desk_review.md`
- **Approval matrix** → `references/approval_routing.md`
- **Quote → order form fields** → `references/quote_to_order.md`
- **E-sign and close** → `references/signature_closeout.md`
- **Finance / CS / provisioning** → `references/handoff_revops.md`
- **CRM cleanup** → `references/crm_hygiene.md`
