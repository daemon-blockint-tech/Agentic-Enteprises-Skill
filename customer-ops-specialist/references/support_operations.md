# Support Operations

## Ticket Lifecycle

### Status Flow
```
New → Open → Pending (customer) → Resolved → Closed
          ↓
      Escalated → Engineering → Resolved
```

### First Response Targets

| Priority | First Response | Update Frequency | Resolution |
|---|---|---|---|
| P1 (Critical) | 15 min | Every 30 min | 4 hours |
| P2 (High) | 1 hour | Every 4 hours | 24 hours |
| P3 (Normal) | 4 hours | Daily | 72 hours |
| P4 (Low) | 24 hours | Every 2 days | 7 days |

## Ticket Triage

### Classification Framework

**Category:**
- Technical issue
- How-to question
- Feature request
- Billing inquiry
- Account access
- Bug report

**Product Area:**
- Authentication / SSO
- API / Integrations
- Reporting / Analytics
- Data Import / Export
- Billing / Subscription
- Performance

### Triage Decision Tree
```
Is system down for multiple customers?
  Yes → P1, page on-call
  No → Continue

Is a major feature broken with no workaround?
  Yes → P2
  No → Continue

Is this a how-to or minor bug?
  Yes → P3
  No → P4 or close as duplicate
```

## Issue Resolution

### Communication Templates

**Acknowledgment:**
```
Hi [Name],

Thanks for reaching out. I've received your request about [issue].

Priority: [P2 - High]
Expected first response: Within 1 hour
Expected resolution: Within 24 hours

I'll update you within [timeframe] with next steps.

Ticket: #[number]
```

**Update (Pending):**
```
Hi [Name],

Update on ticket #[number]:

[Status update]

Next step: [action + owner]
Expected by: [time]

Let me know if you have questions.
```

**Resolution:**
```
Hi [Name],

Your issue has been resolved.

Solution: [what was done]
Root cause: [brief explanation]
Prevention: [what we're doing to prevent recurrence]

Please confirm this resolves your issue.

How was your support experience? [survey link]
```

## Escalation Paths

### Internal Escalation

| Level | When | To |
|---|---|---|
| L1 | Agent needs help | Senior agent or team lead |
| L2 | Technical complexity | Solutions engineer or L3 support |
| L3 | Bug confirmed | Engineering team |
| L4 | Account risk | CSM + account executive |
| L5 | Executive involvement | VP/CSO for strategic accounts |

### Engineering Escalation Template
```markdown
## Escalation to Engineering

**Ticket:** #[number]
**Customer:** [name, plan tier]
**Priority:** P2
**Business impact:** [description]

**Issue Summary:**
[2-3 sentences]

**Reproduction Steps:**
1. [step]
2. [step]

**Expected vs Actual:**
- Expected: [result]
- Actual: [result]

**Evidence:**
- Logs: [link]
- Screenshot: [link]
- Customer environment: [details]

**Customer impact:**
- Users affected: [number]
- Workaround available: Yes/No
```

## Knowledge Base

### Article Structure
```markdown
# [Issue/Question Title]

## Symptoms
[What the user sees]

## Cause
[Why this happens]

## Resolution
### Option 1: [Primary fix]
1. Step 1
2. Step 2

### Option 2: [Alternative]
1. Step 1

## Prevention
[How to avoid in future]

## Related Articles
- [Link 1]
- [Link 2]
```

### KB Maintenance
- Review top 20 articles quarterly for accuracy
- Update screenshots when UI changes
- Archive articles for deprecated features
- Monitor "not helpful" ratings
- Link from tickets to reduce future volume

## Quality Assurance

### Ticket Review Checklist
- [ ] Customer name used (not "hey there")
- [ ] Tone is empathetic, not robotic
- [ ] Technical explanation appropriate for audience
- [ ] Next steps clearly stated
- [ ] Follow-up scheduled if needed
- [ ] Categorized and tagged correctly
- [ ] Linked to relevant KB article
- [ ] Escalation documented

### Calibration Sessions
- Weekly: Review 5 random tickets per agent
- Monthly: Score against rubric (empathy, accuracy, efficiency)
- Quarterly: Identify training needs

## Self-Service Optimization

### Deflection Strategies
- In-app contextual help
- Chatbot for common questions
- Automated password reset
- Status page for known issues
- Community forum

### Deflection Metrics
- Self-service resolution rate
- KB article hit rate from tickets
- Chatbot containment rate
- First contact resolution (FCR)
