# Revenue Recognition (ASC 606 / IFRS 15)

## Contract Review Checklist

### Initial Assessment
- [ ] Contract is signed and enforceable
- [ ] Payment terms are defined
- [ ] Collectibility is probable (>80% likelihood)
- [ ] Commercial substance exists (exchange is meaningful)
- [ ] Both parties are committed (penalties for cancellation)
- [ ] Rights and payment terms are identifiable

### SaaS-Specific Considerations
- [ ] Subscription term clearly stated (start/end dates)
- [ ] Auto-renewal provisions and cancellation terms
- [ ] Usage-based vs fixed fee structure
- [ ] Ramp pricing (increasing over contract life)
- [ ] Professional services included (implementation, training)
- [ ] Support tier and SLA obligations
- [ ] Material right identified (options, renewals at discount)

### Combination / Modification Assessment
- [ ] Same customer, same time → combine contracts?
- [ ] Subsequent amendment → prospective or cumulative catch-up?
- [ ] Termination and replacement vs modification?

## Performance Obligation Identification

### Distinct Criteria
A good/service is distinct if:
1. **Capable of being distinct**: Customer can benefit from it on its own or with readily available resources
2. **Distinct within context**: Promise to transfer is separately identifiable from other promises

### Common SaaS POBs

| Component | Distinct? | Treatment |
|---|---|---|
| Software subscription | Yes | Over time (ratably) |
| Implementation / setup | Often yes | Over time or point in time |
| Training | Yes | Over time or point in time |
| Support | Yes | Over time (ratably) |
| Custom development | Yes | Over time (input method) |
| Hardware | Yes | Point in time (delivery) |
| Material right (discount renewal) | Yes | Deferred, recognize when exercised |

### Series Guidance
Treat as a single POB if:
- Same pattern of transfer (daily/weekly/monthly)
- Same method for measuring progress
- Same underlying service

**Example**: 12-month SaaS subscription with monthly billing → single POB recognized ratably

## Standalone Selling Price (SSP)

### SSP Hierarchy

| Method | When to Use | Example |
|---|---|---|
| Adjusted market assessment | Observable competitor pricing | Benchmark against similar products |
| Expected cost plus margin | No direct comparable | Cost + 30% target margin |
| Residual approach | Only when other methods not available | Total price - known SSPs |

### Practical Approaches for SaaS
1. **List price**: Published pricing as SSP (with discount analysis)
2. **Historical selling price**: Median price for standalone sales
3. **Discount allocation**: Allocate discount proportionally unless evidence suggests otherwise

### Discount Allocation
```
Contract: $100K for Subscription ($120K list) + Implementation ($30K list)
Total SSP: $150K
Discount: $50K (33%)

Allocated:
- Subscription: $120K × (1 - 33%) = $80K
- Implementation: $30K × (1 - 33%) = $20K

If discount belongs only to subscription:
- Subscription: $70K (specific evidence)
- Implementation: $30K (full SSP)
```

## Revenue Timing

### Over-Time Criteria (SaaS)
Revenue recognized over time if any of:
1. Customer simultaneously receives and consumes benefits
2. Entity's performance creates/enhances asset customer controls
3. Entity's performance creates asset with no alternative use + enforceable right to payment

**SaaS subscriptions**: Typically criterion 1 (continuous access)
**Implementation**: Typically criterion 2 or 3

### Input vs Output Methods

| Method | Measure | Best For |
|---|---|---|
| Time elapsed | Days passed | Fixed-term subscriptions |
| Effort/expense | Costs incurred | Professional services |
| Milestones | Deliverables completed | Project-based work |
| Units produced | Transactions processed | Usage-based pricing |

### Point-in-Time Indicators
- Delivery of license (on-premise software)
- Acceptance criteria met
- Customer obtains control (title, risk, physical possession)

## Modification Accounting

### Prospective Method
Use when:
- New POBs added at SSP
- Remaining goods/services are distinct from delivered
- Price change reflects standalone selling price

**Accounting**: Treat as new contract for undelivered items

### Cumulative Catch-Up
Use when:
- Existing POBs change (price, scope)
- Goods/services not distinct from delivered

**Accounting**: Recalculate total revenue, adjust through catch-up

### Example: Price Change Mid-Contract
```
Original: 12 months × $10K = $120K
Month 6: Price increases to $12K/month

Prospective:
- Months 1-6: $60K recognized
- Months 7-12: $72K recognized (new price)

If not distinct (cumulative catch-up):
- Total expected: $60K + $72K = $132K
- Recognized through month 6: $60K
- Monthly rate going forward: $132K / 12 = $11K
- Catch-up in month 7: $6K ($66K cumulative - $60K recognized)
```

## Variable Consideration

### Constraint
Recognize variable consideration only to extent it's highly probable no significant reversal will occur.

### Common SaaS Variable Consideration
- Usage overages
- Success fees
- SLA credits / penalties
- Price protection clauses
- Volume tier pricing

### Estimation Methods
- Most likely amount
- Expected value (probability-weighted)
- Apply constraint based on historical experience

## Practical Expedients

### ASC 606 Practical Expedients
1. **Portfolio approach**: Group similar contracts if effects are not materially different
2. **Significant financing component**: Don't adjust if payment period < 1 year
3. **Sales tax**: Exclude from transaction price (presented net)
4. **Shipping/handling**: Can treat as fulfillment cost if policy elected
5. **Disaggregation**: Disclose revenue by geography, product, timing

## Journal Entry Examples

### Standard SaaS Subscription
```
At booking (contract signed):
No entry (only disclosures if material)

At billing (monthly):
Dr Accounts Receivable      $10,000
    Cr Deferred Revenue                  $10,000

Monthly recognition:
Dr Deferred Revenue         $10,000
    Cr Subscription Revenue              $10,000
```

### Upfront Payment (Annual)
```
At receipt:
Dr Cash                     $120,000
    Cr Deferred Revenue                  $120,000

Monthly recognition:
Dr Deferred Revenue         $10,000
    Cr Subscription Revenue              $10,000
```

### Professional Services Bundled
```
At contract (total $140K: $120K sub + $20K implementation):
Dr Accounts Receivable      $140,000
    Cr Deferred Revenue - Subscription   $120,000
    Cr Deferred Revenue - Services       $20,000

Monthly subscription:
Dr Deferred Revenue - Sub   $10,000
    Cr Subscription Revenue              $10,000

As implementation delivered (assuming 2 months):
Dr Deferred Revenue - Svc   $10,000
    Cr Professional Services Revenue   $10,000
```

## Common Issues & Judgments

| Issue | Judgment | Documentation |
|---|---|---|
| Contract commencement | When enforceable rights begin | Legal review memo |
| Renewal option as material right | Discount vs market price | SSP analysis |
| Customer-facilitated costs | Capitalize or expense? | Policy memo |
| Set-up fees | Separate POB or cost? | Historical analysis |
| Usage-based pricing | Estimation method | Historical usage pattern |
| Churn/early termination | Revenue reversal? | Contract terms review |
