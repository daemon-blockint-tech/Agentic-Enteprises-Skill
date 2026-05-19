# Team Leadership

## On-Call Rotation Design

### Rotation Models

| Model | Coverage | Best For | Trade-off |
|---|---|---|---|
| Follow-the-sun | 24/7 with regional teams | Global companies | Requires 3+ regions |
| Single-region | Business hours + on-call nights/weekends | Single-region teams | Night/weekend burden |
| Hybrid | Core hours + escalation on-call | Small teams | Balanced coverage |

### Schedule Design Principles
- Minimum 1 week per rotation (daily switches are too disruptive)
- Avoid back-to-back rotations (recovery time)
- Include holidays in planning (no surprise coverage)
- Publish schedule 1 month ahead
- Allow swap requests with 48-hour notice

### Escalation Path
```
L1: On-call engineer (first responder)
  → L2: On-call lead (after 15 min unresolved)
    → L3: Manager (after 30 min, P1-P2 only)
      → L4: Director (business-critical, P1 only)
```

## Shift Handoff

### Handoff Meeting (10 min)
1. Active incidents and status
2. Alerts requiring attention
3. Changes deployed and their impact
4. Planned work for next shift
5. Issues needing lead attention

### Handoff Document Template
```markdown
## Shift Handoff — [Date] [Outgoing → Incoming]

### Incidents
| ID | Severity | Status | Notes |
|---|---|---|---|
| INC-001 | P2 | Monitoring | Awaiting vendor response |

### Alerts
- Storage forecast: will hit 90% in 3 days

### Changes
- Pipeline X v2.1 deployed, stable

### Planned Work
- Security patches (approved, ready to apply)

### Lead Attention
- Recurring alert on pipeline Y — threshold may need tuning
```

## Burnout Prevention

### Warning Signs
- Increased incident response time
- Declining quality of runbook updates
- Reluctance to take on-call rotations
- Increased sick days after on-call weeks
- Escalation of previously handled incidents

### Mitigation Strategies
- Limit consecutive on-call weeks to 1
- Provide comp time after weekend/holiday coverage
- Rotate difficult shifts (nights, holidays) fairly
- Ensure uninterrupted sleep (no pages 00:00-06:00 except P1)
- Regular 1:1 check-ins focused on well-being

## Team Development

### Skills Matrix

| Skill | Engineer A | Engineer B | Engineer C | Gap? |
|---|---|---|---|---|
| Pipeline debugging | Expert | Intermediate | Beginner | Yes |
| Incident command | Intermediate | Beginner | Beginner | Yes |
| Cost optimization | Beginner | Expert | Intermediate | No |
| Runbook writing | Expert | Intermediate | Intermediate | No |

### Development Plan
- Cross-training: Pair junior with senior on incidents
- Shadowing: New team member shadows on-call for 2 weeks before solo
- Rotation: Rotate incident commander role to build skills
- Training budget: Conferences, certifications (AWS, data platforms)

## Hiring & Staffing

### Team Size Formula
```
Minimum team size = (24/7 coverage needs) / (shift hours) + (buffer for PTO/training)

Example:
- Need 24/7 coverage = 168 hours/week
- Shift = 40 hours/week
- Minimum = 168/40 = 4.2 → 5 engineers
- Buffer (PTO, training, sick) = +2
- Total recommended = 7 engineers
```

### Role Progression

| Level | Focus | Responsibilities |
|---|---|---|
| L1 (Junior) | Learning | Monitor dashboards, handle P4, update runbooks |
| L2 (Mid) | Execution | Handle P2-P3, lead incident response, optimize queries |
| L3 (Senior) | Ownership | Own Tier 1 systems, mentor juniors, design DR plans |
| Lead | Strategy | SLA ownership, vendor management, team development |

## Communication

### Team Cadence

| Meeting | Frequency | Duration | Attendees | Purpose |
|---|---|---|---|---|
| Standup | Daily | 15 min | On-shift team | Blockers, handoffs |
| Incident review | Weekly | 30 min | Full team | Learn from incidents |
| Capacity review | Monthly | 1 hour | Full team + manager | Planning, forecasts |
| Retrospective | Monthly | 1 hour | Full team | Process improvement |
| 1:1 | Weekly | 30 min | Lead + each member | Career, well-being |

### Stakeholder Reporting

**Weekly status to leadership:**
```markdown
## Data Ops Status — Week of [Date]

### Health: 🟢 On Track / 🟡 At Risk / 🔴 Degraded

### Incidents
| Severity | Count | Notes |
|---|---|---|
| P1 | 0 | — |
| P2 | 1 | Storage lag, resolved |

### SLA Performance
| Tier | Target | Actual | Status |
|---|---|---|---|
| Tier 1 | 99.9% | 99.95% | ✅ |

### Cost
| Actual | Budget | Variance |
|---|---|---|
| $12K | $11K | +9% |

### Coming Up
- Security patch window: Thursday 02:00 UTC
- Q2 capacity review: next week
```
