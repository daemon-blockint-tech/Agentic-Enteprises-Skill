# Stakeholder Management

## Requirements Gathering

### Discovery Interview Template

```markdown
## Stakeholder: [Name, Role]
## Date: [Date]

### Business Context
What is happening in the business that prompted this request?

### The Question
What decision are you trying to make?

### Current State
How do you answer this question today?
What data do you currently use?

### Success Criteria
What would make this analysis/dashboard a success?
What action would you take with the answer?

### Constraints
What is the deadline?
Who else needs to see this?
Any known data limitations?

### Follow-up
- [ ] Data access request
- [ ] Prototype by [date]
- [ ] Review meeting scheduled
```

### Question Refinement

When stakeholders ask for data, dig deeper:

| Surface Request | Underlying Need | Better Approach |
|---|---|---|
| "Give me a report of all users" | "I need to understand user segments" | Cohort analysis + segments |
| "Show me revenue by day" | "I need to forecast cash flow" | Add forecasting, seasonality |
| "List all churned customers" | "I need to prevent churn" | Churn risk score + drivers |
| "What is our conversion rate?" | "Which funnel step leaks?" | Step-by-step funnel + drop-off |

## Data Storytelling

### SCQA Framework
- **Situation**: What is the current state?
- **Complication**: What changed or is problematic?
- **Question**: What do we need to decide?
- **Answer**: What does the data say?

### Presentation Structure

1. **Start with the answer** (BLUF — Bottom Line Up Front)
2. **Show the evidence** (1-2 key charts)
3. **Explain the "so what"** (business impact)
4. **Recommend action** (specific, owned, time-bound)
5. **Add details as backup** (appendix for questions)

### Slide Guidelines

| Rule | Example |
|---|---|
| One insight per slide | Not 4 charts competing for attention |
| Title states the finding | "Q3 revenue up 12% driven by Enterprise" |
| Annotations over legends | Direct labels on data points |
| Use consistent scales | Same Y-axis across compared charts |
| Highlight the story | Grey out non-essential data |

## Managing Feedback

### Feedback Triage

| Type | Response | Example |
|---|---|---|
| Clarification | Ask probing questions | "When you say 'active user,' do you mean logged in or took an action?" |
| Scope expansion | Assess impact, negotiate | "We can add that in v2; it requires joining a new table" |
| Data challenge | Verify, document methodology | "Let me check the source table and get back to you" |
| Design preference | Accommodate if low cost | "I can switch to a bar chart if that's clearer" |
| Urgent ad-hoc | Prioritize vs existing work | "I can have this by Thursday; the dashboard update moves to next week" |

### Iteration Management

Limit feedback rounds:
- Round 1: Structural (metrics, dimensions, layout)
- Round 2: Refinement (formatting, labels, colors)
- Round 3: Polish only (minor tweaks)

If a round 4 is needed, revisit scope or requirements.

## Building Trust

**Proactive communication:**
- Share interesting findings without being asked
- Warn about data issues before stakeholders discover them
- Document assumptions and limitations transparently

**Demonstrating rigor:**
- Show sample sizes and confidence intervals
- Acknowledge uncertainty ("estimate with 90% CI")
- Distinguish correlation from causation explicitly

**Building data literacy:**
- Teach stakeholders to read dashboards independently
- Share metric definitions openly
- Explain methodology in accessible language

## Difficult Conversations

### When Data Contradicts Expectations
1. Verify your analysis (check for errors first)
2. Present with context ("Here's what we expected, here's what we found")
3. Propose hypotheses, not conclusions
4. Suggest next steps (deeper dive, experiment, data fix)

### When Data Quality Is Poor
1. Be transparent about limitations
2. Quantify the impact ("5% of records have missing values")
3. Propose remediation ("We can exclude these or impute with X")
4. Set expectations for when quality will improve

### When Requests Are Impossible
1. Explain the blocker clearly (data doesn't exist, privacy constraint)
2. Offer alternatives (proxy metric, partial answer, future data collection)
3. Suggest who can unblock (engineering, legal, vendor)
