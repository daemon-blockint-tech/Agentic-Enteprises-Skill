# Compliance & Audit

## SOX 404 Controls

### Revenue Process Controls

| Control ID | Activity | Control | Frequency | Evidence |
|---|---|---|---|---|
| R-01 | Contract review | Legal/finance review of non-standard terms | Per contract | Approval email / checklist |
| R-02 | Revenue recognition | System-calculated revenue vs manual verification | Monthly | Reconciliation sign-off |
| R-03 | Deferred revenue | DR rollforward agrees to GL and billing system | Monthly | Reconciliation |
| R-04 | Journal entries | All entries >$10K require manager approval | Per entry | Approval in system |
| R-05 | Month-end close | Controller review of flux and significant items | Monthly | Meeting minutes |
| R-06 | AR valuation | Aging review and reserve calculation | Monthly | Aging report + reserve memo |
| R-07 | System access | User access review for revenue systems | Quarterly | Access review log |
| R-08 | Change management | IT changes to revenue systems require approval | Per change | Change ticket |

### IT General Controls (ITGC)

| Domain | Control | Testing |
|---|---|---|
| Access | User provisioning/removal within 48 hours | Sample user tickets |
| Access | Privileged access limited + logged | Review admin logs |
| Access | Quarterly access recertification | Signed recertification |
| Change | Segregation of duties (dev/test/prod) | Environment review |
| Change | Emergency changes documented + approved post-hoc | Change tickets |
| Operations | Backups tested quarterly | Backup test logs |
| Operations | Disaster recovery tested annually | DR test report |

## Audit Preparation

### PBC (Prepared by Client) List

Typical revenue PBC items:
- [ ] Revenue summary by month (detailed GL)
- [ ] Deferred revenue rollforward
- [ ] Contract listing (new, amendments, cancellations)
- [ ] Revenue waterfall (new, expansion, contraction, churn)
- [ ] AR aging and allowance analysis
- [ ] SSP documentation and methodology
- [ ] Sample contracts (statistical sample or judgmental)
- [ ] Board minutes referencing major contracts
- [ ] Revenue recognition policy memo
- [ ] Flux analysis (income statement, balance sheet)

### Contract Sample Selection

**Statistical sampling:**
- Stratify by revenue amount (top 20 + random sample of remainder)
- Sample size based on population and confidence level
- Typically 20-50 contracts depending on volume

**Judgmental sampling:**
- Largest contracts by value
- Most complex terms (modifications, variable consideration)
- New contract types or terms
- Contracts with related parties
- Contracts near period end (cutoff testing)

### Audit Response Template

```markdown
## Audit Response — [Request ID]

**Request:** [Auditor question]

**Response:**
[Clear, factual answer]

**Supporting Documentation:**
- [Document 1] — [description]
- [Document 2] — [description]

**Prepared by:** [Name, Date]
**Reviewed by:** [Name, Date]
```

## Internal Controls Testing

### Design Effectiveness
- Does the control address the risk?
- Is the control precise enough?
- Is it automated or manual?
- Who performs it and are they qualified?

### Operating Effectiveness
- Walkthrough: Document the control from trigger to completion
- Inquiry: Ask control owner how they perform it
- Observation: Watch control being performed
- Inspection: Review evidence (sign-offs, reports)
- Re-performance: Independently verify the control output

### Deficiency Classification

| Severity | Definition | Example |
|---|---|---|
| Control deficiency | Control not designed or operating effectively | Missing approval on 1 entry |
| Significant deficiency | Material weakness, less severe | Repeated missing approvals |
| Material weakness | Reasonable possibility of material misstatement | No review of revenue entries |

## Revenue-Specific Audit Procedures

### Cutoff Testing
- Select transactions 5 days before and after period end
- Verify revenue is recognized in correct period
- Match billing date to service period

### Completeness Testing
- Trace from billing system to revenue recognition
- Ensure all billed amounts are in deferred revenue or revenue
- Test for unrecorded revenue (contract review)

### Accuracy Testing
- Recalculate revenue recognition for sample contracts
- Verify SSP allocation math
- Confirm proration calculations

### Presentation & Disclosure
- Review revenue note for completeness
- Confirm disaggregation matches internal reporting
- Verify RPO disclosure accuracy

## Documentation Standards

### Revenue Recognition Policy Memo
```markdown
# Revenue Recognition Policy

## Effective Date: [Date]
## Owner: [Name, Title]
## Review Frequency: Annual

### Scope
Applies to all revenue contracts for [Company]

### Performance Obligations
[Description of POBs]

### Standalone Selling Prices
[Methodology]

### Timing
[When revenue is recognized]

### Variable Consideration
[How estimated and constrained]

### Modifications
[Prospective vs cumulative catch-up criteria]

### Practical Expedients
[Which are elected]

### Approval
[Signatures]
```

### SSP Documentation
```markdown
# SSP Analysis — [Product/Service]

## Method Used
[Adjusted market assessment / Expected cost plus margin / Residual]

## Data Sources
[List of transactions used]

## Calculation
[Detailed calculation]

## Range
[Minimum, maximum, median]

## Conclusion
[Selected SSP and rationale]

## Review
[Name, Date]
```

## Regulatory Filings

### S-1 / F-1 Revenue Disclosures
- Revenue recognition policy (detailed)
- SaaS metrics (ARR, NRR, cohort retention)
- Customer concentration
- Contract backlog / RPO
- Seasonality

### 10-Q / 10-K Revenue Disclosures
- Revenue by type and timing
- Deferred revenue rollforward
- RPO disclosure
- Significant judgments and estimates

## PCAOB / Auditor Hot Topics
- Revenue recognition (always a significant risk)
- Management override of controls
- Related party transactions
- Cutoff and completeness
- Judgmental estimates (SSP, variable consideration)

## Quarterly Control Self-Assessment

```markdown
## Q[X] Control Self-Assessment — Revenue

### Controls Tested
| Control | Result | Exceptions | Remediation |
|---|---|---|---|
| R-01 | Effective | 0 | N/A |
| R-02 | Effective | 1 | Retraining scheduled |

### Emerging Risks
- [New product line requires SSP update]

### Recommendations
- [Automate reconciliation X]

### Sign-off
[Controller, Date]
```
