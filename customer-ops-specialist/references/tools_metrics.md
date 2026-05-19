# Tools & Metrics

## CRM Setup

### Customer 360 View

| Section | Data | Source |
|---|---|---|
| Profile | Name, email, company, plan | CRM |
| Contract | Start date, renewal date, MRR | Billing system |
| Health | Score, trend, risk flags | Customer success platform |
| Usage | Active users, features, logins | Product analytics |
| Support | Open tickets, CSAT, history | Helpdesk |
| Communication | Last touch, next scheduled | CRM + email |
| Notes | Strategic context, relationships | CSM notes |

### CRM Data Hygiene
- Duplicate check on creation
- Enrich with Clearbit / ZoomInfo
- Validate email domain matches company
- Quarterly data audit (bounce rate, stale contacts)
- Standardize industry, company size fields

## Helpdesk Tools

| Tool | Best For | Cost |
|---|---|---|
| Zendesk | Enterprise, scalability | Medium-High |
| Intercom | Messenger-first, modern SaaS | Medium |
| Freshdesk | Budget-friendly, SMB | Low-Medium |
| HubSpot Service Hub | CRM integration | Medium |
| Salesforce Service Cloud | Enterprise, Salesforce shops | High |
| Help Scout | Simple, email-focused | Low |

### Helpdesk Configuration
- Custom fields: priority, category, product area, customer tier
- Automations: auto-assign by category, SLA alerts
- Macros: common responses, troubleshooting steps
- Views: my tickets, unassigned, escalated, P1
- Reports: volume, resolution time, CSAT, backlog

## Customer Success Platforms

| Tool | Focus | Best For |
|---|---|---|
| Gainsight | Comprehensive CS | Enterprise |
| ChurnZero | Onboarding + health | Mid-market |
| Catalyst | Workflow + collaboration | Scaling teams |
| Vitally | Product-led CS | PLG companies |
| Totango | Modular, flexible | Custom needs |
| Planhat | Modern, intuitive | Fast-growing |

### CSM Workflow in Platform
1. Health score automatically calculated
2. Alerts trigger playbook (risk, expansion)
3. Tasks generated (QBR prep, renewal call)
4. Usage data informs conversation
5. Outcomes logged for reporting

## Billing & Subscription Management

| Tool | Best For | Cost |
|---|---|---|
| Stripe Billing | Developer-friendly, API-first | Usage-based |
| Chargebee | SaaS subscription management | Medium |
| Recurly | Subscription + dunning | Medium |
| Zuora | Enterprise complexity | High |
| Paddle | SaaS + tax handling | Medium |
| Maxio (SaaSOptics) | B2B SaaS metrics | Medium |

## Analytics & Reporting

### Key Customer Metrics

| Metric | Formula | Target |
|---|---|---|
| Net Revenue Retention (NRR) | (Starting MRR + Expansion - Churn) / Starting | >100% |
| Gross Revenue Retention (GRR) | (Starting MRR - Churn) / Starting | >85% |
| Logo Churn | Customers lost / Total customers | <5%/month |
| CSAT | Satisfied responses / Total responses | >90% |
| NPS | % Promoters - % Detractors | >30 |
| First Response Time | Avg time to first reply | Per SLA |
| Resolution Time | Avg time to resolve | Per SLA |
| First Contact Resolution | % resolved in first reply | >70% |
| Expansion Revenue | Upsell + Cross-sell MRR | >10% of MRR |
| Customer Lifetime Value (LTV) | Avg MRR × Gross Margin / Logo Churn | >3× CAC |

### Dashboard Layout

```
Executive Summary (Weekly)
├── NRR, GRR, ARR
├── Logo churn, net new
└── Top risks and wins

Operations (Daily)
├── Ticket volume and backlog
├── SLA compliance
├── P1/P2 status
└── Agent workload

Customer Success (Weekly)
├── Health score distribution
├── Renewal pipeline
├── Expansion opportunities
└── Onboarding progress

Revenue (Monthly)
├── MRR movement
├── Dunning effectiveness
├── Refund/credit volume
└── Revenue recognition
```

## Automation & Workflows

### Common Automations

| Trigger | Action | Tool |
|---|---|---|
| Health score drops to red | Create CSM task + alert | CS platform |
| Payment fails | Start dunning sequence | Billing system |
| Ticket created (P1) | Page on-call + Slack alert | Helpdesk |
| 90 days before renewal | Create renewal opportunity | CRM |
| NPS submitted (detractor) | Create escalation task | Survey tool |
| Usage drops 50% | Create at-risk task | Product analytics |
| New feature released | Email to relevant customers | Marketing automation |

### Integration Architecture
```
CRM (HubSpot/Salesforce)
  ↔ Helpdesk (Zendesk/Intercom)
  ↔ Billing (Stripe/Chargebee)
  ↔ Product Analytics (Mixpanel/Amplitude)
  ↔ CS Platform (Gainsight/ChurnZero)
  ↔ Email (Customer.io/Iterable)
  ↔ BI (Looker/Tableau)
```

## Voice of Customer (VoC)

### Feedback Channels
- In-app surveys (micro-surveys after key actions)
- Post-support CSAT
- Quarterly NPS
- Product feedback portal (Canny, ProductBoard)
- Customer advisory board
- Support ticket theme analysis

### Feedback Loop
1. Collect feedback from all channels
2. Categorize by product area and sentiment
3. Prioritize by frequency and business impact
4. Share with product team monthly
5. Close loop with customers ("You asked, we built")

## Reporting Cadence

| Report | Audience | Frequency | Content |
|---|---|---|---|
| Support summary | Support team | Daily | Volume, SLA, top issues |
| CS pipeline | CS leadership | Weekly | Renewals, health, risks |
| Revenue report | Finance + leadership | Monthly | MRR, churn, NRR, ARR |
| Customer metrics | Executive team | Monthly | NPS, CSAT, LTV/CAC |
| Operational review | All customer ops | Monthly | Cross-functional review |
| Board metrics | Board | Quarterly | NRR, logo churn, CAC, LTV |
