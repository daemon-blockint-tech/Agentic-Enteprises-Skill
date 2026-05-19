# Revenue Operations

## Subscription Lifecycle

### Subscription States
```
Trial → Active → At Risk → Past Due → Suspended → Cancelled
              ↓
         Renewed → Active
              ↓
         Upgraded → Active (new plan)
              ↓
         Downgraded → Active (new plan)
```

### State Transitions

| From | To | Trigger | Action |
|---|---|---|---|
| Trial | Active | Payment method added | Convert to paid |
| Active | At Risk | Health score red | CSM intervention |
| Active | Past Due | Payment failed | Dunning sequence |
| Past Due | Suspended | 30 days overdue | Service restricted |
| Past Due | Active | Payment received | Restore service |
| Active | Cancelled | Customer request | Offboarding |
| Cancelled | Active | Win-back offer | Re-activation |

## Billing Operations

### Monthly Close Process
1. **Invoice generation** (1st of month)
   - Pull active subscriptions
   - Calculate prorations for mid-cycle changes
   - Apply credits/promotions
   - Generate PDF/email invoices

2. **Payment processing** (1st-5th)
   - Charge cards on file
   - Record successful payments
   - Flag failed payments for dunning

3. **Reconciliation** (5th-10th)
   - Match payments to invoices
   - Record in accounting system
   - Handle disputes/chargebacks

4. **Reporting** (10th)
   - MRR/ARR report
   - Churn report
   - Dunning effectiveness
   - Revenue recognition

### Proration Calculation
```
Daily rate = Plan price / Days in billing period
Prorated charge = Daily rate × Remaining days

Example: Upgrade from $100/mo to $200/mo on day 15 of 30-day month
- Old plan used: $100 × (15/30) = $50
- New plan due: $200 × (15/30) = $100
- Charge: $100 - $50 = $50 (or $200 - $100 = $100 for full cycle)
```

## Dunning Management

### Dunning Sequence

| Day | Channel | Message | Action |
|---|---|---|---|
| 0 | Email | Payment failed, update method | Retry in 24h |
| 1 | Email | Reminder with direct link | Retry in 48h |
| 3 | Email + In-app | Account at risk | Retry in 72h |
| 7 | Email | Final notice | Retry in 7 days |
| 14 | Email | Account suspension imminent | Manual outreach |
| 30 | Email | Account suspended | CSM escalation |

### Dunning Templates

**Day 0 — Payment Failed:**
```
Subject: Action needed: Update your payment method

Hi [Name],

We couldn't process your [Product] payment on file ending in [last4].

Update payment method: [link]

Your service continues uninterrupted. We'll retry in 24 hours.

Questions? Reply to this email.
```

**Day 7 — Final Notice:**
```
Subject: Final notice: Payment required to avoid interruption

Hi [Name],

We've attempted to charge your payment method multiple times without success.

To avoid service interruption, please update your payment method within 7 days:
[link]

If you're experiencing financial hardship, reply and we'll work with you.
```

## Refunds & Credits

### Refund Policy Framework

| Scenario | Refund Eligible? | Amount | Approval |
|---|---|---|---|
| Service outage >4 hours | Yes | Prorated | Auto |
| Customer error (wrong plan) | Yes | Full (within 7 days) | Manager |
| Dissatisfaction | Case by case | Up to 1 month | Director |
| Annual cancel (mid-term) | Yes | Remaining months | Auto |
| Feature not delivered | Yes | Negotiated | Director |

### Credit Issuance
```
Credit reason: [outage / goodwill / error]
Amount: $[X]
Applied to: Next invoice / Immediate refund
Approval: [name]
Customer communication: [sent]
```

## Subscription Changes

### Upgrade Process
1. Customer requests or triggers upgrade
2. Confirm new plan features and pricing
3. Calculate proration (if mid-cycle)
4. Process charge or invoice
5. Provision new features/access
6. Send confirmation
7. CSM notified for expansion tracking

### Downgrade Process
1. Customer requests downgrade
2. Confirm new limitations
3. Handle data/feature access (grandfather or restrict)
4. Apply at next billing cycle (or immediate if requested)
5. Send confirmation
6. CSM notified for churn risk tracking

### Cancellation Process
1. Customer initiates cancellation
2. Conduct exit interview (if possible)
3. Offer save play (discount, pause, plan change)
4. If confirmed:
   - Schedule end-of-term or immediate
   - Export data (if applicable)
   - Revoke access
   - Send confirmation
   - Mark churn reason
5. CSM notified for win-back campaign

## Revenue Recognition

### Principles
- Revenue recognized over subscription term (ratable)
- Implementation/services recognized as delivered
- Setup fees recognized over contract life or upfront (policy-dependent)
- Annual upfront payment = deferred revenue liability

### Monthly Recurring Revenue (MRR)
```
MRR = Sum of all active subscription monthly values

MRR Changes:
+ New business (new customers)
+ Expansion (upgrades, add-ons)
- Contraction (downgrades)
- Churn (cancellations)
= Net MRR
```

### Annual Recurring Revenue (ARR)
```
ARR = MRR × 12

Common ARR metrics:
- Gross ARR churn: % lost to cancellations
- Net ARR retention: % retained including expansion
- Logo churn: % of customers lost
```

## Collections

### Collections Tiers

| Tier | Days Past Due | Action | Owner |
|---|---|---|---|
| 1 | 1-30 | Automated dunning | System |
| 2 | 31-60 | Personal outreach | AR specialist |
| 3 | 61-90 | Collections notice, payment plan | AR manager |
| 4 | 90+ | Collections agency or legal | Finance director |

### Collections Communication
- Professional but firm tone
- Document all communication
- Offer payment plans when appropriate
- Escalate to legal only as last resort
- Preserve customer relationship when possible
