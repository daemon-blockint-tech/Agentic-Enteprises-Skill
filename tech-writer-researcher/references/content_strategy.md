# Content Strategy

## Audience Analysis

### Persona Template
```markdown
## [Persona Name]

**Role:** Senior Developer at mid-size SaaS company
**Goals:** Evaluate if our API fits their integration needs
**Pain points:** Poor examples, unclear error messages, missing edge case docs
**Technical level:** Expert in their stack, beginner with our tech
**Context:** Evaluating during sprint planning, limited time
**Preferred format:** Copy-paste code examples, decision trees

**Quote:** "I just need to see if this handles webhooks properly."
```

### Audience Matrix

| Audience | Knowledge | Need | Format | Channel |
|---|---|---|---|---|
| Evaluators | Low | Quick assessment | README, quick start | GitHub, landing page |
| New users | Medium | Get running | Tutorials, guides | Docs site |
| Power users | High | Advanced patterns | Reference, blogs | Docs, GitHub |
| Contributors | Expert | Architecture, internals | Explanations, RFCs | Wiki, repo |

## Content Planning

### Content Calendar Template

| Week | Content | Type | Owner | Status | Channel |
|---|---|---|---|---|---|
| W1 | New feature guide | How-to | @writer | Draft | Docs |
| W2 | API changelog | Reference | @eng | Ready | GitHub |
| W3 | Architecture deep dive | Explanation | @architect | Idea | Blog |

### Content Prioritization
Score each piece by:
- **Reach**: How many users affected?
- **Impact**: How critical is this information?
- **Effort**: Time to produce?
- **Urgency**: Is there a deadline or blocker?

## Documentation Lifecycle

### States

| State | Criteria | Action |
|---|---|---|
| Draft | Being written | Internal review |
| Review | SME checking accuracy | Incorporate feedback |
| Published | Live and discoverable | Monitor metrics |
| Current | Up-to-date, accurate | Schedule next review |
| Stale | Minor drift | Update in next cycle |
| Outdated | Significant drift | Priority update |
| Deprecated | Feature removed | Archive or redirect |

### Review Cadence

| Doc Type | Review Frequency | Trigger |
|---|---|---|
| API reference | Per release | API version change |
| Runbooks | Quarterly | Incident post-mortem |
| Tutorials | Bi-annually | Product UI change |
| Architecture docs | Annually | Major redesign |
| README | Per release | Dependency update |

## Content Metrics

| Metric | How to Measure | Target |
|---|---|---|
| Page views | Analytics | Trend up |
| Time on page | Analytics | 2-5 min (context-dependent) |
| Bounce rate | Analytics | <40% for landing pages |
| Search queries | Search logs | Match user vocabulary |
| Support tickets | Support system | Decline for documented issues |
| NPS/CSAT | Surveys | >7/10 |
| Contribution rate | GitHub metrics | Community PRs accepted |

## Information Scent
Help users know they're in the right place:
- Page title matches search query
- First paragraph confirms relevance
- Headings preview what's covered
- Cross-links to related content

## Content Reuse Strategy

### Single Sourcing
Write once, publish everywhere:
- Source in Markdown/DITA
- Generate docs site, PDF, help center
- Include in product (in-app help)

### Snippet Libraries
Maintain reusable content:
- Warnings and disclaimers
- Common troubleshooting steps
- Boilerplate definitions
- Code examples by language

## Governance

### RACI for Documentation

| Activity | Writer | SME | Editor | PM |
|---|---|---|---|---|
| Write first draft | R | C | I | I |
| Technical accuracy | C | R/A | I | I |
| Style review | R | I | R/A | I |
| Publish | R | I | C | A |
| Maintain | R | C | I | I |

### Style Guide Governance
- Versioned style guide in repo
- Linting with Vale or similar
- Annual review for relevance
- Contribution process for additions

## Multichannel Publishing

| Channel | Format | Update Frequency |
|---|---|---|
| Docs site | HTML/Markdown | Continuous |
| GitHub README | Markdown | Per release |
| In-app help | Embedded snippets | Per feature |
| PDF | Generated | Quarterly |
| Video tutorials | Screencast | Per major feature |
| Blog posts | Markdown | Weekly/Bi-weekly |
| API explorer | Interactive | Real-time |
| Slack/Discord | Short snippets | As needed |
