---
name: tech-writer-researcher
description: |
  Guides technical writing, documentation, and research synthesis.
  Covers API docs, user guides, runbooks, READMEs, style guides, information architecture,
  literature reviews, competitive analysis, evidence synthesis, and content strategy.
  Use when writing technical documentation, creating developer content, structuring information,
  conducting research, synthesizing findings, or building documentation systems.
---

# Technical Writer / Researcher

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

**See `references/technical_writing.md` for templates, style guidance, and doc system architecture.**

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

**See `references/research_methods.md` for frameworks, synthesis techniques, and citation standards.**

### 3. Content Strategy & Planning

**Content inventory template:**

| Document | Audience | Type | Owner | Last Updated | Review Cycle | Status |
|---|---|---|---|---|---|---|
| API Guide | Developers | Reference | @tech-writer | 2024-01 | Quarterly | Current |

**See `references/content_strategy.md` for planning frameworks, lifecycle management, and content metrics.**

### 4. Editing & Review

**Self-editing checklist:**
- [ ] One idea per paragraph
- [ ] Active voice (where appropriate)
- [ ] Defined acronyms on first use
- [ ] Consistent terminology
- [ ] Scannable headings and lists
- [ ] Working links and code examples
- [ ] Accessibility (alt text, color independence)

**See `references/technical_writing.md` for review rubrics and style guide frameworks.**

## When to Load References

- **Technical writing** → `references/technical_writing.md`
- **Research methods** → `references/research_methods.md`
- **Content strategy** → `references/content_strategy.md`
- **Tools & frameworks** → `references/tools_frameworks.md`
