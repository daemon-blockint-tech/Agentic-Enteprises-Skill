# Requirements & Process Analysis

## Requirements Elicitation Techniques

| Technique | Best For | Limitations |
|---|---|---|
| Interviews | Deep understanding, sensitive topics | Time-consuming, potential bias |
| Workshops | Cross-functional alignment, complex systems | Scheduling difficulty, groupthink risk |
| Observation (shadowing) | Understanding actual vs stated behavior | Time-intensive, may alter behavior |
| Document analysis | Existing systems, regulatory requirements | May be outdated or incomplete |
| Surveys | Large user base, quantitative needs | Low response rate, shallow insights |
| Prototyping | Clarifying ambiguous requirements | May anchor users on design too early |

### Interview Guidelines

**Before the interview:**
- Send agenda and context 24 hours ahead
- Prepare 5-10 open-ended questions
- Identify the decision-maker vs. influencer vs. user

**Sample questions:**
- "Walk me through how you currently do X from start to finish."
- "What takes the most time or causes the most frustration?"
- "If you could wave a wand, what would change?"
- "What happens when this process breaks?"
- "Who else is involved, and what do they need?"

**During the interview:**
- Listen 80%, talk 20%
- Ask "why" at least 3 times (5 Whys technique)
- Capture exact quotes for later reference
- Sketch the process live if possible

**After the interview:**
- Send summary within 24 hours
- Confirm accuracy with the interviewee
- Log requirements in shared tracker

## Prioritization Frameworks

### MoSCoW

| Priority | Definition | Decision Rule |
|---|---|---|
| Must have | Critical for launch; project fails without it | "Would we cancel the project if this were excluded?" |
| Should have | Important but not critical; workarounds exist | "Painful to defer, but possible" |
| Could have | Desirable if capacity allows | "Nice to have" |
| Won't have | Explicitly excluded (this phase) | "Out of scope for now" |

### Weighted Scoring

```
Score = Σ (Criterion Weight × Rating)
```

**Example criteria:**
| Criterion | Weight |
|---|---|
| Business value | 30% |
| User impact | 25% |
| Implementation cost | 20% |
| Time to deliver | 15% |
| Strategic alignment | 10% |

## Process Modeling

### BPMN 2.0 Core Elements

```
[Start Event] → [Task] → [Gateway (decision)] → [Task] → [End Event]
     ↓                                              ↑
   [Pool: Team A]                             [Pool: Team B]
```

| Symbol | Meaning | Usage |
|---|---|---|
| Circle | Start/End event | Process boundaries |
| Rounded rectangle | Task/Activity | Work performed |
| Diamond | Gateway | Decision, parallel, or merge |
| Rectangle with + | Sub-process | Complex step detailed elsewhere |
| Swimlane | Pool/Lane | Organizational boundaries |
| Arrow | Sequence flow | Order of activities |
| Dashed arrow | Message flow | Cross-pool communication |

### As-Is vs To-Be Analysis Template

```markdown
## Process: [Name]

### As-Is State
| Step | Actor | Time | Pain Point |
|---|---|---|---|
| 1. Receive request | Support | 5 min | Email, no tracking |
| 2. Log in system | Support | 10 min | Manual data entry |

**Issues identified:**
- Manual handoffs cause delays
- No visibility into status
- Duplicate data entry

### To-Be State
| Step | Actor | Time | Improvement |
|---|---|---|---|
| 1. Auto-create ticket | System | 0 min | Integration triggers ticket |
| 2. Route automatically | System | 0 min | Rules-based routing |

**Expected benefits:**
- 50% reduction in handling time
- Real-time status visibility
- Zero duplicate entry
```

## Gap Analysis

### Current vs Future State Matrix

| Capability | Current State | Future State | Gap | Priority |
|---|---|---|---|---|
| Self-service reporting | Manual requests to BI team | Automated dashboards with filters | No self-service capability | High |
| Data integration | 3 separate Excel files | Single source of truth in warehouse | No integration layer | High |
| Mobile access | Desktop only | Responsive web + app | No mobile support | Medium |

### Gap Resolution Strategies

| Gap Type | Strategy | Example |
|---|---|---|
| People | Hire, train, or restructure | Train users on self-service tools |
| Process | Redesign workflow | Implement approval automation |
| Technology | Build, buy, or integrate | Purchase CRM, integrate with ERP |
| Data | Clean, migrate, or master | Implement MDM for customer data |

## User Story Format

### Standard Template
```
As a [type of user],
I want [some goal],
so that [some reason/benefit].
```

**Acceptance criteria (Given-When-Then):**
```
Given [precondition]
When [action]
Then [expected result]
```

**Example:**
```
As a sales manager,
I want to see pipeline by stage and rep,
so that I can forecast revenue and coach underperformers.

Acceptance criteria:
Given I am on the sales dashboard
When I select a date range and team
Then I see pipeline value broken down by stage and rep
And I can drill into individual opportunities
```

### INVEST Checklist (Good User Stories)

| Attribute | Test |
|---|---|
| Independent | Can be delivered without other stories |
| Negotiable | Details can be discussed and refined |
| Valuable | Delivers business value |
| Estimable | Team can estimate effort |
| Small | Fits in a single sprint |
| Testable | Clear pass/fail criteria |

## Workshop Facilitation

### Workshop Types

| Type | Duration | Purpose | Activities |
|---|---|---|---|
| Discovery | 2-4 hours | Understand current state | Process mapping, pain point identification |
| Design | 4-8 hours | Design future state | To-be process, role definition |
| Prioritization | 2-3 hours | Rank requirements | Dot voting, weighted scoring |
| Review | 1-2 hours | Validate deliverables | Walkthrough, feedback capture |

### Facilitation Tips

- **Set ground rules**: No devices, one conversation at a time, all ideas valid
- **Use timeboxes**: 10-15 min per activity
- **Capture visibly**: Whiteboard or shared screen
- **Balance voices**: Actively draw out quiet participants
- **Park lot**: Capture off-topic ideas for later
- **Close with actions**: Who does what by when
