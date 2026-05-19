---
name: business-analyst
description: |
  Guides business analysts through requirements elicitation, process analysis, data-driven insights,
  and solution documentation. Covers stakeholder interviews, process modeling, user stories, gap analysis,
  cost-benefit analysis, BRDs/FRDs, and business-technical translation.
  Use when gathering requirements, mapping processes, analyzing business problems, writing documentation,
  facilitating workshops, or translating between business stakeholders and technical teams.
---

# Business Analyst

## Core Workflows

### 1. Requirements Elicitation

**Step-by-step process:**

1. **Prepare**
   - Review existing documentation, systems, and pain points
   - Identify stakeholders (sponsors, users, implementers)
   - Define scope boundaries (in-scope, out-of-scope)

2. **Elicit**
   - Interview key stakeholders using open-ended questions
   - Observe users in their current workflow (shadowing)
   - Review existing reports, data, and system outputs
   - Run workshops for complex or cross-functional needs

3. **Analyze & consolidate**
   - Group requirements by theme (functional, non-functional, technical)
   - Resolve conflicts between stakeholders
   - Prioritize using MoSCoW or weighted scoring

4. **Validate**
   - Walk through requirements with stakeholders
   - Confirm understanding with prototypes or examples
   - Get formal sign-off before proceeding

**See `references/requirements_process.md` for interview techniques, workshop facilitation, and prioritization frameworks.**

### 2. Business Process Analysis

**Analysis workflow:**

1. **Map the current state (as-is)**
   - Identify actors, steps, decisions, and handoffs
   - Note time spent, pain points, and error rates
   - Document data inputs and outputs at each step

2. **Identify gaps and inefficiencies**
   - Redundancies, manual workarounds, bottlenecks
   - Missing integrations, duplicate data entry
   - Compliance risks or audit gaps

3. **Design the future state (to-be)**
   - Streamline or automate steps
   - Eliminate non-value-add activities
   - Define new roles, systems, and data flows

4. **Plan the transition**
   - Phased rollout vs big-bang
   - Change impact assessment
   - Training and communication plan

**See `references/requirements_process.md` for BPMN notation, process mapping templates, and gap analysis frameworks.**

### 3. Data-Driven Business Analysis

**Analytical techniques:**

| Technique | When to Use | Output |
|---|---|---|
| Cost-benefit analysis | Evaluate initiatives | ROI, payback period, NPV |
| SWOT analysis | Strategic planning | Strengths, weaknesses, opportunities, threats |
| Root cause analysis | Problem diagnosis | 5 Whys, fishbone diagram |
| Process mining | Understand actual vs documented process | Bottleneck map, variant analysis |
| Benchmarking | Compare performance | Gap vs industry leaders |

**See `references/business_analysis.md` for financial modeling, forecasting techniques, and strategic frameworks.**

### 4. Documentation & Communication

**Key documents:**

| Document | Purpose | Audience |
|---|---|---|
| Business Requirements Document (BRD) | What the business needs and why | Business stakeholders, project sponsor |
| Functional Requirements Document (FRD) | How the system should behave | Developers, QA, solution architects |
| User Stories | Feature from user perspective | Agile team, product owner |
| Process Flow | Visual step-by-step workflow | All stakeholders |
| Data Dictionary | Definitions of fields and terms | Technical team, data consumers |

**See `references/documentation.md` for document templates, writing guidelines, and presentation frameworks.**

## When to Load References

- **Requirements & process** → `references/requirements_process.md`
- **Business analysis** → `references/business_analysis.md`
- **Documentation** → `references/documentation.md`
- **Tools & frameworks** → `references/tools_frameworks.md`
