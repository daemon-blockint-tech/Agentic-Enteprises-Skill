# Data Program & Product Management

## Roadmap Framework

### Horizon Planning

| Horizon | Timeframe | Focus | Example |
|---|---|---|---|
| H1 (Now) | 0-3 months | Bugs, tech debt, quick wins | Fix stale data, add monitoring |
| H2 (Next) | 3-6 months | Committed features | New mart, self-serve tool |
| H3 (Later) | 6-12 months | Strategic bets | Data mesh, ML platform |

### Prioritization Frameworks

**RICE (for product features):**
```
Score = (Reach × Impact × Confidence) / Effort
```

**WSJF (Weighted Shortest Job First):**
```
WSJF = (Business value + Time criticality + Risk reduction) / Job size
```

**MoSCoW (for stakeholder alignment):**
- Must have: Non-negotiable for release
- Should have: Important but not blocking
- Could have: Nice to have if capacity allows
- Won't have: Explicitly deferred

## Stakeholder Management

### Stakeholder Matrix

| Stakeholder | Interest | Influence | Engagement Strategy |
|---|---|---|---|
| CDO / VP Data | High | High | Weekly 1:1, strategic input |
| Business analysts | High | Medium | Bi-weekly demo, requirements sessions |
| Data engineers | High | Medium | Sprint ceremonies, technical RFCs |
| Legal / Compliance | Medium | High | Monthly governance review |
| Finance / Procurement | Low | High | Quarterly budget review |
| End users (analysts) | High | Low | Office hours, documentation |

### Communication Templates

**Weekly status email:**
```
1. This week: What shipped (with links)
2. Next week: What's committed
3. Blockers: What needs leadership help
4. Metrics: Pipeline health, quality scores
5. Shoutouts: Recognize team wins
```

**Quarterly business review:**
```
1. Goals vs outcomes
2. Key deliverables (demos)
3. Metrics trend (6 months)
4. Challenges & learnings
5. Next quarter priorities
6. Ask for feedback/decisions
```

## Data Product Management

### Product Lifecycle

1. **Discovery**: Interview stakeholders, define the question
2. **Definition**: Write PRD with acceptance criteria
3. **Design**: Data model, pipeline architecture, UX (dashboards)
4. **Build**: Iterative delivery with demos
5. **Launch**: Staged rollout (alpha → beta → GA)
6. **Operate**: Monitor, support, iterate
7. **Sunset**: Deprecate when obsolete (see EOL communication)

### PRD Template (Data Product)

```markdown
# [Product Name] PRD

## Problem
What business question are we answering?

## Success Criteria
- Metric: __________
- Baseline: __________
- Target: __________
- Timeline: __________

## Data Requirements
- Sources: __________
- Granularity: __________
- History needed: __________
- Refresh frequency: __________

## Dependencies
- Upstream: __________
- Downstream: __________
- Blockers: __________

## Acceptance Criteria
- [ ] Data passes quality tests
- [ ] Dashboard loads in <5 seconds
- [ ] Documentation complete
- [ ] Stakeholder sign-off received
```

## Team Coordination

### RACI for Data Work

| Activity | Data PM | Data Engineer | Analyst | Steward | Consumer |
|---|---|---|---|---|---|
| Requirements | A/R | C | C | I | R |
| Pipeline build | C | R | C | I | I |
| Data model design | A | R | C | C | I |
| Quality tests | A | R | C | C | I |
| Documentation | A | C | R | C | I |
| Release comms | R | C | C | I | C |

### Meeting Guidelines

**Effective data standup (15 min):**
- What did I complete yesterday?
- What am I working on today?
- What's blocking me?
- No problem-solving in standup (schedule breakout)

**Sprint demo (30 min):**
- Demo working data, not slides
- Show the business impact
- Record for async stakeholders
