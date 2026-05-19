---
name: customer-ops-specialist
description: |
  Manage customer operations across success, support, and revenue operations.
  Cover customer onboarding, health scoring, renewal management, ticket triage, SLA management,
  knowledge base development, billing operations, dunning, refunds, and customer metrics.
  Triggers on "customer onboarding", "support ticket triage", "billing inquiry", "churn analysis",
  "health score", "SLA management", "dunning process", "customer success playbook",
  "renewal management", "CSAT review", or "customer ops". Exec/VIP and public community
  escalation program: community-executive-escalations-program-manager. Monetization product
  (pricing, paywalls): product-management-monetization.
---

# Customer Operations Specialist

## Overview

Manage customer operations across success, support, and revenue operations. This skill covers
customer onboarding, health scoring, renewal management, ticket triage, SLA management,
knowledge base development, billing operations, dunning, refunds, and customer metrics.

## Features

- Customer onboarding playbook with milestone tracking
- Health score framework with leading indicators and risk signals
- Renewal management workflow with expansion opportunity identification
- Ticket triage and SLA management with escalation paths
- Billing operations: dunning sequences, refund processing, subscription changes
- Customer metrics: CSAT, NPS, NRR, GRR, churn rate, time-to-resolution

## Usage

1. Identify the user's customer ops need (onboarding, support, billing, or metrics)
2. Follow the corresponding workflow below
3. Produce structured outputs: onboarding checklists, health scorecards, renewal playbooks, or billing SOPs

## Examples

- **User**: "Design a customer onboarding flow"
  **Agent**: Runs Customer Onboarding workflow, produces 30-60-90 day plan with milestones, success criteria, and handoff points

- **User**: "Set up a health score"
  **Agent**: Runs Health Scoring workflow, defines leading indicators (product usage, support tickets, NPS), creates scoring model with risk thresholds

- **User**: "Handle a billing dispute"
  **Agent**: Runs Billing Operations workflow, investigates charge, applies refund policy, documents resolution, updates customer record

## When to Use

- Design or run customer onboarding, health scoring, and renewal playbooks
- Triage support tickets, SLAs, escalations, and knowledge-base updates
- Handle billing, dunning, refunds, and subscription change operations
- Review CSAT, churn, NRR, and other customer-facing operational metrics

## When NOT to Use

- ASC 606 revenue recognition, deferred revenue, or audit-ready close → use `senior-revenue-accountant`
- Data pipeline incidents or warehouse platform operations → use `data-system-ops-lead` or `data-manager`
- Product requirements or process documentation for internal systems → use `business-analyst`
- Public API or developer documentation → use `tech-writer-researcher`
- Deal desk, order forms, signature routing, CRM close process → use `deal-operations-administrator`
- Employee HR onboarding, offboarding, HRIS → use `people-operations-specialist`
- Technical debugging, repro, engineering escalation → use `support-engineer`
- Product how-to, configuration help, support macros → use `product-support-specialist`

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

### 3. Revenue Operations

**Billing workflow:**
- Invoice generation and delivery
- Payment processing and reconciliation
- Dunning (failed payment recovery)
- Refund and credit processing
- Subscription changes (upgrade/downgrade/cancel)

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
