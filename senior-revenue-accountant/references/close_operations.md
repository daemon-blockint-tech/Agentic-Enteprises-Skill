# Close Operations

## Month-End Close Checklist

### Pre-Close (Day 0)
- [ ] Confirm cutoff: no entries after 11:59 PM
- [ ] Notify departments: expense cutoffs, accrual requests
- [ ] Lock subledgers: AP, AR, payroll, inventory
- [ ] Confirm bank statement availability

### Revenue Close (Days 1-3)
- [ ] Pull billing data from CRM/billing system
- [ ] Calculate revenue waterfall (new, expansion, churn)
- [ ] Review deferred revenue rollforward
- [ ] Identify unusual transactions (>$50K, non-standard terms)
- [ ] Calculate MRR/ARR by segment
- [ ] Prepare revenue journal entries

### Reconciliations (Days 2-4)
- [ ] Bank reconciliation (all accounts)
- [ ] AR aging review (follow up on >90 days)
- [ ] Deferred revenue reconciliation
- [ ] Intercompany reconciliation
- [ ] Credit card/processor reconciliation
- [ ] Payroll reconciliation

### Accruals & Adjustments (Days 3-5)
- [ ] Expense accruals (unbilled services, utilities)
- [ ] Revenue accruals (earned but not billed)
- [ ] Prepaid amortization
- [ ] Depreciation & amortization
- [ ] Stock compensation
- [ ] Bad debt reserve review

### Review (Days 5-7)
- [ ] Preliminary trial balance
- [ ] Flux analysis (MoM, YoY)
- [ ] Management review meeting
- [ ] Identify adjusting entries
- [ ] Update financial models

### Finalization (Days 7-10)
- [ ] Post adjusting entries
- [ ] Final trial balance
- [ ] Financial statements
- [ ] Board/management reports
- [ ] Close subledgers
- [ ] Document significant judgments

## Revenue Reconciliation

### Deferred Revenue Rollforward
```
Beginning deferred revenue          $XXX
+ Billings (cash collected upfront)   + XXX
- Revenue recognized                - XXX
+/- Contract modifications          +/- XX
= Ending deferred revenue           $XXX

Check: Ending DR agrees to GL and billing system
```

### Revenue Waterfall
```
Revenue by source:
  Beginning ARR                     $XXX
  + New business (new logos)        + XXX
  + Expansion (upsell/cross-sell)     + XXX
  - Contraction (downgrades)        - XXX
  - Churn (cancelled)               - XXX
  = Ending ARR                      $XXX

Revenue recognition:
  Subscription revenue              $XXX
  Professional services revenue     $XXX
  Usage/overage revenue             $XXX
  = Total revenue                   $XXX
```

### AR Reconciliation
```
Beginning AR                        $XXX
+ Billings (invoiced)               + XXX
- Cash collections                - XXX
- Credits issued                  - XXX
- Bad debt write-off              - XXX
= Ending AR                         $XXX

Aging:
  Current (0-30 days)             $XXX
  31-60 days                      $XXX
  61-90 days                      $XXX
  >90 days                        $XXX
  = Total AR                      $XXX
```

## Journal Entry Templates

### Standard Monthly Entries

**Revenue recognition (recurring):**
```
Dr Deferred Revenue — Subscription    $XXX
    Cr Subscription Revenue                 $XXX
(To recognize monthly subscription revenue)
```

**Revenue recognition (services):**
```
Dr Deferred Revenue — Services        $XXX
    Cr Professional Services Revenue          $XXX
(To recognize services revenue as delivered)
```

**Expense accrual:**
```
Dr [Expense Account]                 $XXX
    Cr Accrued Expenses                     $XXX
(To accrue for services received but not billed)
```

**Prepaid amortization:**
```
Dr [Expense Account]                 $XXX
    Cr Prepaid Expenses                     $XXX
(To amortize prepaid insurance, software, rent)
```

**Payroll accrual:**
```
Dr Salaries & Wages                  $XXX
Dr Payroll Taxes                      $XXX
Dr Benefits                         $XXX
    Cr Accrued Payroll                      $XXX
(To accrue for period-end payroll)
```

**Bad debt provision:**
```
Dr Bad Debt Expense                   $XXX
    Cr Allowance for Doubtful Accounts      $XXX
(To adjust reserve based on aging analysis)
```

## Flux Analysis

### Income Statement Flux
```
Account                 Current    Prior     $ Change   % Change   Explanation
--------------------------------------------------------------------------------
Subscription Revenue    $500K      $450K     +$50K      +11%       New logo adds + expansion
Professional Svcs         $50K       $80K      -$30K      -38%       Implementation backlog cleared
Gross Profit              $400K      $360K     +$40K      +11%       Revenue growth outpacing COGS
Sales & Marketing         $200K      $180K     +$20K      +11%       New hires + campaign spend
Net Income                $50K       $45K      +$5K       +11%       Operating leverage
```

### Balance Sheet Flux
```
Account                 Current    Prior     $ Change   % Change   Explanation
--------------------------------------------------------------------------------
Cash                      $200K      $150K     +$50K      +33%       Collections > billings
Accounts Receivable       $300K      $280K     +$20K      +7%        Seasonal billing timing
Deferred Revenue          $600K      $550K     +$50K      +9%        Annual upfront increase
```

### Key Thresholds for Investigation
- Revenue variance > 10% vs forecast
- Expense variance > 15% vs budget
- AR days > 60 (DSO)
- Deferred revenue decline > 10% (churn signal)
- Any account > $25K unexplained change

## Close Efficiency Metrics

| Metric | Target | How to Improve |
|---|---|---|
| Days to close | 5-7 | Automate reconciliations, standardize entries |
| Entries per close | <200 | Accrual automation, recurring entries |
| Reconciliation lag | 0 days | Auto-match bank, system integrations |
| Adjusting entries | <20 | Better estimates, mid-month reviews |
| Close overtime hours | Minimal | Distributed close, deadline management |

## Automation Opportunities

### High-Impact Automations
1. **Bank reconciliation**: Auto-match rules (95%+ match rate)
2. **Revenue recognition**: Scheduled entries from billing system
3. **Prepaid amortization**: Monthly auto-post from schedule
4. **Intercompany**: Auto-eliminate upon confirmation
5. **Flux commentary**: Template-based with variance thresholds

### Tools
- **ERP**: NetSuite, Sage Intacct, QuickBooks Online
- **Close management**: FloQast, Blackline, Workiva
- **Revenue**: RevPro, Zuora RevPro, Maxio
- **Analytics**: Excel, Looker, Tableau
- **RPA**: UiPath, Automation Anywhere (for legacy systems)
