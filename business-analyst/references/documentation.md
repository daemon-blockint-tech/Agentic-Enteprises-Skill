# Documentation & Communication

## Business Requirements Document (BRD)

### Template Structure

```markdown
# [Project Name] — Business Requirements Document

## 1. Executive Summary
- Business problem and opportunity
- Proposed solution at a high level
- Expected benefits and success criteria

## 2. Business Objectives
| Objective | Metric | Target | Timeline |
|---|---|---|---|
| Reduce order processing time | Avg minutes per order | <5 min | 6 months |

## 3. Scope
### In Scope
- [Requirement area 1]
- [Requirement area 2]

### Out of Scope
- [Explicitly excluded item 1]

## 4. Stakeholders
| Role | Name | Responsibility |
|---|---|---|
| Project Sponsor | [Name] | Budget approval, escalation |
| Business Owner | [Name] | Requirements sign-off |
| End Users | [Group] | Validation, training |

## 5. Current State
[Process description, pain points, supporting data]

## 6. Future State
[Desired outcomes, process changes, user experience]

## 7. Functional Requirements
| ID | Requirement | Priority | Acceptance Criteria |
|---|---|---|---|
| FR-001 | [Description] | Must | [Measurable criteria] |

## 8. Non-Functional Requirements
- Performance: [e.g., page load <2s]
- Security: [e.g., SSO, role-based access]
- Availability: [e.g., 99.5% uptime]
- Compliance: [e.g., GDPR, SOX]

## 9. Constraints & Assumptions
- Budget limit: $XXX
- Timeline: Must launch by [date]
- Assumption: User volume will not exceed X

## 10. Risks
| Risk | Impact | Probability | Mitigation |
|---|---|---|---|
| Data migration delays | High | Medium | Start migration early, plan rollback |

## 11. Appendix
- Glossary
- Reference documents
- Approval signatures
```

## Functional Requirements Document (FRD)

### Template Structure

```markdown
# [Project Name] — Functional Requirements Document

## 1. Introduction
- Purpose and audience (developers, QA, architects)
- Relationship to BRD

## 2. System Context
[Diagram showing system boundaries and interfaces]

## 3. Functional Requirements
### 3.1 [Feature Area]
#### FR-001: [Requirement name]
**Description:** [Detailed description]
**User stories:** [As a... I want... so that...]
**Acceptance criteria:**
- [Criterion 1]
- [Criterion 2]
**Business rules:**
- [Rule 1]
- [Rule 2]
**Data requirements:**
- Inputs: [Fields, sources]
- Outputs: [Fields, destinations]
**UI/UX notes:** [Wireframe references, interaction patterns]
**Error handling:** [Invalid input, system failure]

## 4. Data Dictionary
| Field | Type | Description | Source | Valid Values |
|---|---|---|---|---|
| customer_id | UUID | Unique customer identifier | CRM | Valid UUID format |

## 5. Interface Requirements
- API contracts
- File formats
- Integration touchpoints

## 6. Business Rules Engine
| Rule ID | Condition | Action | Priority |
|---|---|---|---|
| BR-001 | Order value > $10K | Require manager approval | High |
```

## Presentation Framework

### Pyramid Principle (Barbara Minto)
1. **Start with the answer** (main recommendation)
2. **Group supporting arguments** (3-5 key reasons)
3. **Provide evidence** (data, examples, logic)

### SCQA for Business Presentations
- **Situation**: Context everyone agrees on
- **Complication**: The problem or change
- **Question**: What should we do?
- **Answer**: The recommendation with supporting data

### Slide Structure

```
Slide 1: Title + Main Recommendation
Slide 2: The Problem (data + impact)
Slide 3: Options Considered
Slide 4: Recommended Approach + Why
Slide 5: Implementation Plan
Slide 6: Risks & Mitigation
Slide 7: Ask (decision, resources, next steps)
```

## Business-Technical Translation

### Common Translation Gaps

| Business Says | Technical Interpretation | Clarifying Question |
|---|---|---|
| "Real-time" | Sub-second? 5 minutes? Daily? | "What decision depends on this speed?" |
| "All users" | Internal only? Customers? Partners? | "Who needs access and from where?" |
| "Easy to use" | Few clicks? No training? Mobile? | "Can you walk me through a typical use case?" |
| "Flexible reporting" | Self-serve? Custom SQL? Export? | "What does the end user do with the data?" |
| "Secure" | Encryption? Access control? Audit? | "What compliance requirements apply?" |

### Glossaries

Maintain a shared glossary:
| Term | Business Definition | Technical Mapping |
|---|---|---|
| Active customer | Made a purchase in last 90 days | `last_order_date >= NOW() - 90 days` |
| Revenue | Gross merchandise value, net of returns | `SUM(order_total) WHERE status != 'returned'` |

## Communication Templates

### Requirement Change Request
```markdown
## Change Request

**Date:** [Date]
**Requested by:** [Name]
**Priority:** Low / Medium / High / Critical

**Current requirement:** [What exists]
**Proposed change:** [What should change]
**Business justification:** [Why]
**Impact on scope:** [Add / Remove / Modify]
**Impact on timeline:** [Days added/removed]
**Impact on cost:** [Additional budget needed]

**Approved by:** __________ **Date:** __________
```

### Weekly Status Update
```markdown
## [Project] Status — Week of [Date]

### Overall Health: 🟢 On Track / 🟡 At Risk / 🔴 Off Track

### This Week
- [Accomplishment 1]
- [Accomplishment 2]

### Next Week
- [Planned activity 1]

### Blockers
- [Blocker] — Owner: [Name]

### Decisions Needed
- [Decision] — From: [Stakeholder] — By: [Date]
```
