---
name: tech-writer-researcher
description: |
  Write and research technical documentation.
  Cover information architecture, style guides, API documentation, user research, content strategy,
  and documentation operations.
  Triggers on "write technical documentation", "create API docs", "developer tutorial",
  "information architecture", "style guide", "content strategy", "documentation audit",
  "user research", or "technical writing".
---

# Technical Writer / Researcher

## Overview

Write and research technical documentation. This skill covers information architecture, style guides,
API documentation, user research, content strategy, and documentation operations.

## Features

- Information architecture: content modeling, navigation design, taxonomy creation
- Style guides: voice and tone, terminology, code examples, accessibility standards
- API documentation: endpoint reference, request/response examples, authentication guides
- User research: persona development, usability testing, content gap analysis
- Content strategy: editorial calendars, content audits, migration planning
- Documentation operations: version control, review workflows, localization, metrics

## Usage

1. Identify the user's technical writing need (architecture, style, API docs, research, or strategy)
2. Follow the corresponding workflow below
3. Produce structured outputs: content models, style guides, API reference docs, research reports, or content strategies

## Examples

- **User**: "Write API documentation"
  **Agent**: Runs API Documentation workflow, creates endpoint reference with request/response examples, authentication guide, and error codes

- **User**: "Create a style guide"
  **Agent**: Runs Style Guide workflow, defines voice and tone, establishes terminology, produces code example standards

- **User**: "Audit our documentation"
  **Agent**: Runs Content Strategy workflow, analyzes content gaps, identifies outdated pages, produces improvement roadmap

## When to Use

- Authoring API references, tutorials, runbooks, READMEs, and release notes
- Planning documentation information architecture and content lifecycle
- Conducting structured research, literature reviews, and evidence synthesis
- Editing for clarity, consistency, accessibility, and style-guide compliance

## When NOT to Use

- Prompt/LLM agent design, eval harnesses, or guardrails → use `prompt-engineer`
- Business requirements, BRDs, or process modeling for delivery projects → use `business-analyst`
- Warehouse SQL optimization or dimensional modeling → use `data-warehouse-engineer`
- Revenue accounting, close calendars, or ASC 606 judgments → use `senior-revenue-accountant`
- Customer ticket repro, escalation, support KB fixes → use `support-engineer`
- Product support how-tos, macros, ticket triage → use `product-support-specialist`
- Strategy consulting, executive recommendations, operating model → use `business-consultant`
- Business model and competitive monetization research → use `business-model-researcher`
- All-hands, crisis statements, launch messaging → use `communication-lead`

## Core Workflows

### 1. Technical Documentation Workflow

**Phase checklist:**

1. **Audience analysis**
   - Who reads this? (role, skill level, context)
   - What do they need to do after reading?
   - What do they already know vs. need to learn?

2. **Information gathering**
   - Interview SMEs (subject matter experts)
   - Review existing docs, code, and specs
   - Test the product/feature yourself

3. **Structure & outline**
   - Choose document type (see table below)
   - Create heading hierarchy
   - Identify prerequisites and next steps

4. **Draft**
   - Write for clarity first, polish later
   - Include code examples, screenshots, diagrams
   - Use consistent terminology

5. **Review**
   - Technical accuracy review (SME)
   - Editorial review (style, grammar, clarity)
   - User testing (if possible)

6. **Publish & maintain**
   - Version control and changelog
   - Feedback mechanism
   - Scheduled review cadence

**Document type selection:**

| Type | Purpose | Audience | Length |
|---|---|---|---|
| README | Quick start, install, overview | Developers | 1-2 pages |
| API reference | Endpoint details, parameters | Developers | Per endpoint |
| Tutorial | Step-by-step learning | New users | Medium |
| How-to guide | Specific task completion | Users with context | Short |
| Explanation | Conceptual understanding | All levels | Medium |
| Runbook | Incident response, operations | On-call engineers | Short |
| Release notes | What changed, why | Users, stakeholders | Short |
| FAQ | Common questions | Support reduction | Varies |

### 2. Research & Synthesis Workflow

**Structured research process:**

1. **Define the question**
   - Convert vague request into specific research question
   - Identify scope (time period, geography, sources)
   - Define success criteria (decision support, background, deep dive)

2. **Source & collect**
   - Primary: interviews, surveys, observations
   - Secondary: papers, reports, databases, news
   - Tertiary: summaries, reviews, meta-analyses

3. **Evaluate sources**
   - Currency, relevance, authority, accuracy, purpose (CRAAP test)
   - Bias detection (funding, affiliation, methodology)

4. **Synthesize**
   - Group findings by theme
   - Identify agreements, contradictions, gaps
   - Extract evidence-backed conclusions

5. **Communicate**
   - Match format to audience (executive summary, full report, memo)
   - Cite sources properly
   - Include confidence levels and limitations

### 3. Content Strategy & Planning

**Content inventory template:**

| Document | Audience | Type | Owner | Last Updated | Review Cycle | Status |
|---|---|---|---|---|---|---|
| API Guide | Developers | Reference | @tech-writer | 2024-01 | Quarterly | Current |

### 4. Editing & Review

**Self-editing checklist:**
- [ ] One idea per paragraph
- [ ] Active voice (where appropriate)
- [ ] Defined acronyms on first use
- [ ] Consistent terminology
- [ ] Scannable headings and lists
- [ ] Working links and code examples
- [ ] Accessibility (alt text, color independence)
