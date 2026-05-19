---
name: customer-ops-specialist
description: |
  Guides customer operations across customer success, support, and revenue operations.
  Covers customer onboarding, health scoring, renewal management, ticket triage, SLA management,
  knowledge base development, billing operations, dunning, refunds, and customer metrics.
  Use when managing customer relationships, resolving support issues, processing billing inquiries,
  designing onboarding flows, or optimizing customer-facing operational processes.
---

# Customer Operation Specialist

## Core Workflows

### 1. Customer Onboarding & Success

**Onboarding checklist:**

1. **Pre-engagement**
   - Welcome email with next steps
   - Account setup and provisioning
   - Introductory call scheduled
   - Technical requirements confirmed

2. **Activation (first 30 days)**
   - Core feature walkthrough
   - Data migration/import completed
   - Integrations configured
   - First value milestone achieved

3. **Adoption (30-90 days)**
   - Advanced feature training
   - Use case expansion
   - Regular check-in cadence established
   - Success metrics baseline set

**Health scoring:**

| Dimension | Weight | Green | Yellow | Red |
|---|---|---|---|---|
| Product usage | 30% | Daily active | Weekly | <Monthly |
| Feature adoption | 25% | >80% core features | 50-80% | <50% |
| Support tickets | 15% | <2/month | 2-5/month | >5/month |
| NPS/CSAT | 15% | >50 | 30-50 | <30 |
| Engagement | 15% | Responsive | Delayed | Ghosted |

**See `references/customer_success.md` for onboarding playbooks, health scoring frameworks, and renewal/expansion strategies.**

### 2. Support & Issue Resolution

**Ticket triage:**

| Priority | Response | Resolution | Examples |
|---|---|---|---|
| P1 (Critical) | 15 min | 4 hours | System down, data loss, security |
| P2 (High) | 1 hour | 24 hours | Major feature broken, workaround exists |
| P3 (Normal) | 4 hours | 72 hours | Minor bug, feature question |
| P4 (Low) | 24 hours | 7 days | Cosmetic, enhancement request |

**Resolution workflow:**
1. Acknowledge and set expectations
2. Gather context (logs, screenshots, reproduction steps)
3. Reproduce internally
4. Resolve or escalate to engineering
5. Verify fix with customer
6. Document in knowledge base
7. Close with CSAT survey

**See `references/support_operations.md` for SLA frameworks, escalation paths, and knowledge base management.**

### 3. Revenue Operations

**Billing workflow:**
- Invoice generation and delivery
- Payment processing and reconciliation
- Dunning (failed payment recovery)
- Refund and credit processing
- Subscription changes (upgrade/downgrade/cancel)

**See `references/revenue_operations.md` for billing procedures, dunning strategies, and subscription management.**

### 4. Metrics & Continuous Improvement

**Weekly review:**
- Ticket volume and trend
- First response time vs SLA
- Resolution time vs SLA
- CSAT score
- Top categories and emerging issues

**Monthly review:**
- Churn rate and reasons
- Expansion revenue
- NRR (Net Revenue Retention)
- Health score distribution
- Knowledge base article effectiveness

**See `references/tools_metrics.md` for CRM/helpdesk setup, analytics dashboards, and operational KPIs.**

## When to Load References

- **Customer success** → `references/customer_success.md`
- **Support operations** → `references/support_operations.md`
- **Revenue operations** → `references/revenue_operations.md`
- **Tools & metrics** → `references/tools_metrics.md`
