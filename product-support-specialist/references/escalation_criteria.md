# Escalation Criteria

## To technical support (`support-engineer`)

Escalate when **any**:

- Reproducible error with request ID, stack trace, or HTTP code
- Data incorrect vs source of truth
- Performance degradation isolated to customer
- Integration fails after correct config per docs
- Regression after release (link version)
- Security-sensitive symptom (suspected breach → security path first)

**Handoff bundle:**

```markdown
- Customer impact (users, workflow blocked)
- Steps to reproduce (numbered)
- Expected vs actual
- Environment (plan, region, browser, version)
- Logs/screenshots attached
- What customer was told (avoid contradiction)
```

## To customer ops (`customer-ops-specialist`)

- Refunds, credits, invoice disputes
- Subscription change not applied
- Dunning / payment failure loops
- Contractual SLA credits

## To product / PM

- Repeated confusion (doc + 5+ tickets)
- Missing capability with no workaround
- UX defect (misleading copy, broken flow) without eng bug yet
- Feature request with clear business case

Use `feedback_feature_requests.md` format.

## To sales / account team

- Expansion, enterprise features, custom limits
- Renewal risk expressed in support thread
- Champion asking for pricing (warm handoff)

## To exec escalation program

- C-suite contact, strategic logo, public threat
- `community-executive-escalations-program-manager`

## To incident management

- Multiple customers, same symptom, same window
- Status page candidate
- `incident-management-engineer`

## Do not escalate

- Answered in KB with customer confirmation
- User error fixed with education
- Duplicate of closed eng issue with known fix version

## Escalation hygiene

- One owner on customer side (no parallel threads)
- Internal note @ mention with SLA ask
- Customer informed of handoff and new SLA
- Ping if no internal response before breach
