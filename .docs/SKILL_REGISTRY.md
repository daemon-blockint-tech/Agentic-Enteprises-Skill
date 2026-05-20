# Agentic Enterprise OS - Skill Registry

## Overview

Complete registry of all 86 skills in the Agentic Enterprise OS. Each skill is documented with its layer, triggers, inputs, outputs, dependencies, and execution mode.

---

## Layer 5: Governance & Orchestration (7 skills)

### 1. build-validator
- **Layer**: 5 (Governance)
- **Triggers**: "validate", "quality check", "go/no-go", "architecture review", "security review", "cost review", "compliance review"
- **Inputs**: Skill output, architecture specs, security requirements, budget constraints, compliance rules
- **Outputs**: Validation report (PASS/FAIL), recommendations, next steps
- **Dependencies**: None (cross-cutting)
- **Execution Mode**: Single
- **Description**: Quality gate that validates skill outputs against architecture, security, cost, and compliance criteria.

### 2. ai-risk-governance
- **Layer**: 5 (Governance)
- **Triggers**: "ai risk assessment", "ai safety review", "ai governance", "model risk", "ai compliance"
- **Inputs**: AI model specs, training data, use case, risk criteria
- **Outputs**: Risk assessment, safety recommendations, compliance status
- **Dependencies**: None (cross-cutting)
- **Execution Mode**: Single
- **Description**: Governs AI safety, risk assessment, and ethical compliance across all AI/ML operations.

### 3. engineering-manager-agent-prompts-evals
- **Layer**: 5 (Governance)
- **Triggers**: "manage ai agents", "agent prompts", "agent evaluation", "agent performance"
- **Inputs**: Agent specs, prompt templates, evaluation criteria
- **Outputs**: Agent management plan, prompt evaluations, performance metrics
- **Dependencies**: ai-engineer, ml-systems-engineer-rl-engineering
- **Execution Mode**: Single
- **Description**: Manages AI agent development, prompt engineering, and evaluation workflows.

### 4. engineering-manager-vertical-ai-products
- **Layer**: 5 (Governance)
- **Triggers**: "manage ai products", "vertical ai strategy", "product engineering management"
- **Inputs**: Product specs, market analysis, engineering capacity
- **Outputs**: Product management plan, engineering roadmap, resource allocation
- **Dependencies**: product-designer, senior-fullstack-developer
- **Execution Mode**: Single
- **Description**: Manages vertical AI product development and engineering team coordination.

### 5. ai-skill-manager
- **Layer**: 5 (Governance)
- **Triggers**: "manage skills", "skill registry", "skill routing", "skill lifecycle"
- **Inputs**: Skill definitions, routing rules, availability status
- **Outputs**: Skill registry, routing decisions, lifecycle management
- **Dependencies**: All skills (orchestration)
- **Execution Mode**: Orchestrated
- **Description**: Central skill registry and routing manager for the entire enterprise OS.

### 6. technical-program-manager
- **Layer**: 5 (Governance)
- **Triggers**: "program management", "cross-team coordination", "technical program"
- **Inputs**: Program specs, team capacity, dependencies, timelines
- **Outputs**: Program plan, coordination strategy, status reports
- **Dependencies**: data-manager, infrastructure-engineer
- **Execution Mode**: Orchestrated
- **Description**: Coordinates technical programs across multiple teams and skill layers.

### 7. technical-program-manager-security-cvd
- **Layer**: 5 (Governance)
- **Triggers**: "security program", "coordinated vulnerability disclosure", "cvd management"
- **Inputs**: Vulnerability reports, disclosure policies, stakeholder lists
- **Outputs**: CVD plan, disclosure timeline, stakeholder communications
- **Dependencies**: cybersecurity, compliance-engineer
- **Execution Mode**: Orchestrated
- **Description**: Manages security programs and coordinated vulnerability disclosure processes.

---

## Layer 4: AI & ML Operations (12 skills)

### 8. ai-researcher
- **Layer**: 4 (AI/ML)
- **Triggers**: "ai research", "hypothesis testing", "ai feasibility study", "research experiment"
- **Inputs**: Research question, hypotheses, data availability, constraints
- **Outputs**: Research findings, feasibility assessment, experiment design
- **Dependencies**: data-scientist, ml-research-engineer-safeguards
- **Execution Mode**: Single
- **Description**: Conducts AI research, hypothesis testing, and feasibility studies.

### 9. ai-engineer
- **Layer**: 4 (AI/ML)
- **Triggers**: "build ai application", "ai development", "integrate ai model", "deploy ai"
- **Inputs**: Model specs, application requirements, integration points
- **Outputs**: AI application, integration code, deployment plan
- **Dependencies**: ml-infrastructure-engineer-safeguards, senior-fullstack-developer
- **Execution Mode**: Single
- **Description**: Develops AI applications and integrates ML models into production systems.

### 10. ai-lead-ops
- **Layer**: 4 (AI/ML)
- **Triggers**: "ai operations", "ai orchestration", "manage ai workflow", "ai production"
- **Inputs**: AI workflow specs, production requirements, monitoring criteria
- **Outputs**: Operations plan, orchestration strategy, monitoring setup
- **Dependencies**: ai-engineer, devops, data-system-ops-lead
- **Execution Mode**: Orchestrated
- **Description**: Leads AI operations, orchestration, and production workflow management.

### 11. ai-redteam
- **Layer**: 4 (AI/ML)
- **Triggers**: "ai red team", "adversarial testing", "ai security test", "prompt injection test"
- **Inputs**: AI model, attack vectors, security criteria
- **Outputs**: Vulnerability report, attack simulations, mitigation recommendations
- **Dependencies**: offensive-security-analyst, ai-risk-governance
- **Execution Mode**: Single
- **Description**: Conducts adversarial testing and red team operations against AI systems.

### 12. ai-token-improvement-plan-engineer
- **Layer**: 4 (AI/ML)
- **Triggers**: "token optimization", "token improvement", "context window optimization"
- **Inputs**: Token usage data, context requirements, optimization goals
- **Outputs**: Token optimization plan, improvement recommendations, efficiency metrics
- **Dependencies**: ai-context-engineer, ai-memory-developer
- **Execution Mode**: Single
- **Description**: Optimizes token usage and context window efficiency for AI systems.

### 13. ai-context-engineer
- **Layer**: 4 (AI/ML)
- **Triggers**: "context management", "context engineering", "prompt context", "context optimization"
- **Inputs**: Context requirements, prompt specs, model constraints
- **Outputs**: Context design, optimization strategy, prompt templates
- **Dependencies**: prompt-engineer, ai-memory-developer
- **Execution Mode**: Single
- **Description**: Engineers context management and prompt context optimization for AI systems.

### 14. ai-memory-developer
- **Layer**: 4 (AI/ML)
- **Triggers**: "ai memory", "persistent context", "session memory", "cross-session context"
- **Inputs**: Session data, context requirements, persistence criteria
- **Outputs**: Memory architecture, persistence strategy, context retrieval system
- **Dependencies**: data-architect, infrastructure-engineer
- **Execution Mode**: Single
- **Description**: Develops persistent memory and cross-session context management for AI systems.

### 15. ai-skill-manager (ops)
- **Layer**: 4 (AI/ML)
- **Triggers**: "skill lifecycle", "skill versioning", "skill deployment", "skill monitoring"
- **Inputs**: Skill specs, version requirements, deployment criteria
- **Outputs**: Lifecycle management plan, versioning strategy, monitoring setup
- **Dependencies**: ai-skill-manager (governance), devops
- **Execution Mode**: Single
- **Description**: Manages skill lifecycle, versioning, and deployment operations.

### 16. prompt-engineer
- **Layer**: 4 (AI/ML)
- **Triggers**: "design prompt", "prompt engineering", "optimize prompt", "prompt template"
- **Inputs**: Task requirements, model specs, output criteria
- **Outputs**: Prompt designs, templates, optimization recommendations
- **Dependencies**: ai-context-engineer, ai-researcher
- **Execution Mode**: Single
- **Description**: Designs and optimizes prompts for AI models and applications.

### 17. prompt-engineer-agent-prompts-evals
- **Layer**: 4 (AI/ML)
- **Triggers**: "agent prompt", "prompt evaluation", "agent prompt testing"
- **Inputs**: Agent specs, prompt templates, evaluation criteria
- **Outputs**: Agent prompt designs, evaluation results, optimization recommendations
- **Dependencies**: prompt-engineer, engineering-manager-agent-prompts-evals
- **Execution Mode**: Single
- **Description**: Specializes in agent prompt design and evaluation workflows.

### 18. ml-research-engineer-safeguards
- **Layer**: 4 (AI/ML)
- **Triggers**: "safe ml research", "ml safeguards", "responsible ml", "ml safety testing"
- **Inputs**: Research specs, safety criteria, risk assessments
- **Outputs**: Safe research plan, safeguards implementation, testing results
- **Dependencies**: ai-researcher, ai-risk-governance
- **Execution Mode**: Single
- **Description**: Conducts ML research with safety safeguards and responsible AI practices.

### 19. ml-systems-engineer-rl-engineering
- **Layer**: 4 (AI/ML)
- **Triggers**: "rl engineering", "reinforcement learning", "rl training", "reward design"
- **Inputs**: RL requirements, environment specs, reward criteria
- **Outputs**: RL system design, training plan, reward functions
- **Dependencies**: ml-research-engineer-safeguards, ml-infrastructure-engineer-safeguards
- **Execution Mode**: Single
- **Description**: Engineers reinforcement learning systems and reward optimization.

### 20. ml-infrastructure-engineer-safeguards
- **Layer**: 4 (AI/ML)
- **Triggers**: "ml infrastructure", "ml deployment", "ml pipeline", "ml safety infra"
- **Inputs**: Infrastructure requirements, safety criteria, deployment specs
- **Outputs**: ML infrastructure design, deployment plan, safety safeguards
- **Dependencies**: infrastructure-engineer, ml-systems-engineer-rl-engineering
- **Execution Mode**: Single
- **Description**: Builds ML infrastructure with safety safeguards and deployment pipelines.

---

## Layer 3: Data & Analytics (9 skills)

### 21. data-architect
- **Layer**: 3 (Data)
- **Triggers**: "design data architecture", "create data model", "plan data warehouse", "data pipeline architecture", "schema design", "data governance framework"
- **Inputs**: Business requirements, data sources, compliance needs, scalability goals
- **Outputs**: Data architecture design, schema definitions, governance framework
- **Dependencies**: business-model-researcher, infrastructure-engineer
- **Execution Mode**: Single
- **Description**: Designs enterprise data architecture, schemas, and governance frameworks.

### 22. data-warehouse-engineer
- **Layer**: 3 (Data)
- **Triggers**: "build data warehouse", "create etl pipeline", "data warehouse design", "warehouse optimization"
- **Inputs**: Data architecture, source systems, transformation rules, performance requirements
- **Outputs**: Warehouse schema, ETL pipelines, optimization recommendations
- **Dependencies**: data-architect, analytics-data-engineer
- **Execution Mode**: Single
- **Description**: Builds and optimizes data warehouses and ETL pipelines.

### 23. analytics-data-engineer
- **Layer**: 3 (Data)
- **Triggers**: "build data pipeline", "create analytics pipeline", "data engineering", "analytics infrastructure"
- **Inputs**: Warehouse specs, analytics requirements, data sources, transformation rules
- **Outputs**: Data pipelines, analytics infrastructure, monitoring setup
- **Dependencies**: data-warehouse-engineer, data-scientist
- **Execution Mode**: Single
- **Description**: Builds data pipelines and analytics infrastructure for data science teams.

### 24. analytics-data-engineering-manager-product
- **Layer**: 3 (Data)
- **Triggers**: "manage analytics product", "analytics engineering management", "data product strategy"
- **Inputs**: Product requirements, team capacity, analytics goals, stakeholder needs
- **Outputs**: Product management plan, team coordination strategy, roadmap
- **Dependencies**: analytics-data-engineer, data-manager
- **Execution Mode**: Single
- **Description**: Manages analytics data engineering as a product with stakeholder alignment.

### 25. data-scientist
- **Layer**: 3 (Data)
- **Triggers**: "build ml model", "statistical analysis", "data science", "predictive modeling", "machine learning"
- **Inputs**: Data pipelines, business questions, feature requirements, model criteria
- **Outputs**: ML models, statistical analyses, predictions, insights
- **Dependencies**: analytics-data-engineer, bi-analyst
- **Execution Mode**: Single
- **Description**: Builds ML models, conducts statistical analysis, and generates data insights.

### 26. bi-analyst
- **Layer**: 3 (Data)
- **Triggers**: "create dashboard", "bi analysis", "business intelligence", "data visualization", "report building"
- **Inputs**: Data models, business metrics, visualization requirements, stakeholder needs
- **Outputs**: Dashboards, reports, visualizations, business insights
- **Dependencies**: data-scientist, data-system-ops-lead
- **Execution Mode**: Single
- **Description**: Creates BI dashboards, reports, and data visualizations for business stakeholders.

### 27. ontology-engineer
- **Layer**: 3 (Data)
- **Triggers**: "build knowledge graph", "ontology design", "semantic modeling", "knowledge management"
- **Inputs**: Data sources, domain knowledge, relationship requirements, use cases
- **Outputs**: Knowledge graphs, ontologies, semantic models, relationship mappings
- **Dependencies**: data-architect, data-scientist
- **Execution Mode**: Single
- **Description**: Designs knowledge graphs, ontologies, and semantic data models.

### 28. data-system-ops-lead
- **Layer**: 3 (Data)
- **Triggers**: "data operations", "data system monitoring", "data ops", "data pipeline monitoring"
- **Inputs**: Pipeline specs, monitoring criteria, SLA requirements, incident reports
- **Outputs**: Operations plan, monitoring setup, incident response, SLA reports
- **Dependencies**: bi-analyst, data-manager, devops
- **Execution Mode**: Single
- **Description**: Leads data operations, monitoring, and incident response for data systems.

### 29. data-manager
- **Layer**: 3 (Data)
- **Triggers**: "manage data program", "data governance", "data strategy", "data program management"
- **Inputs**: Program requirements, governance policies, stakeholder needs, compliance rules
- **Outputs**: Program management plan, governance framework, strategy document
- **Dependencies**: data-system-ops-lead, technical-program-manager
- **Execution Mode**: Orchestrated
- **Description**: Manages data programs, governance, and strategic alignment across the enterprise.

---

## Layer 2: Infrastructure & Security (19 skills)

### 30. infrastructure-engineer
- **Layer**: 2 (Infra/Sec)
- **Triggers**: "design cloud infrastructure", "cloud architecture", "infrastructure setup", "cloud deployment"
- **Inputs**: Application requirements, scalability needs, budget constraints, compliance rules
- **Outputs**: Infrastructure design, deployment plan, cost estimates, compliance checklist
- **Dependencies**: senior-system-architecture, platform-engineer
- **Execution Mode**: Single
- **Description**: Designs and deploys cloud infrastructure for enterprise applications.

### 31. platform-engineer
- **Layer**: 2 (Infra/Sec)
- **Triggers**: "build platform", "platform engineering", "internal developer platform", "platform as a service"
- **Inputs**: Infrastructure specs, developer needs, platform requirements, integration points
- **Outputs**: Platform design, developer tools, integration APIs, documentation
- **Dependencies**: infrastructure-engineer, cluster-deployment-engineer
- **Execution Mode**: Single
- **Description**: Builds internal developer platforms and platform-as-a-service solutions.

### 32. cluster-deployment-engineer
- **Layer**: 2 (Infra/Sec)
- **Triggers**: "deploy kubernetes", "cluster setup", "k8s deployment", "container orchestration"
- **Inputs**: Platform specs, cluster requirements, container images, scaling policies
- **Outputs**: Cluster deployment, configuration, scaling setup, monitoring
- **Dependencies**: platform-engineer, devops
- **Execution Mode**: Single
- **Description**: Deploys and manages Kubernetes clusters and container orchestration.

### 33. devops
- **Layer**: 2 (Infra/Sec)
- **Triggers**: "setup ci/cd", "devops pipeline", "automation", "infrastructure as code", "deployment automation"
- **Inputs**: Application code, deployment requirements, testing criteria, infrastructure specs
- **Outputs**: CI/CD pipelines, automation scripts, IaC templates, deployment workflows
- **Dependencies**: cluster-deployment-engineer, devsecops
- **Execution Mode**: Single
- **Description**: Builds CI/CD pipelines, automation, and infrastructure-as-code workflows.

### 34. devsecops
- **Layer**: 2 (Infra/Sec)
- **Triggers**: "secure ci/cd", "devsecops", "security automation", "pipeline security"
- **Inputs**: CI/CD pipelines, security requirements, vulnerability scans, compliance rules
- **Outputs**: Secure pipelines, security automation, vulnerability remediation, compliance reports
- **Dependencies**: devops, cybersecurity
- **Execution Mode**: Single
- **Description**: Integrates security into CI/CD pipelines and automates security workflows.

### 35. deployment-strategist
- **Layer**: 2 (Infra/Sec)
- **Triggers**: "deployment strategy", "blue-green deployment", "canary deployment", "rolling deployment"
- **Inputs**: Application specs, deployment requirements, risk tolerance, rollback criteria
- **Outputs**: Deployment strategy, rollout plan, rollback procedures, risk assessment
- **Dependencies**: devsecops, incident-management-engineer
- **Execution Mode**: Single
- **Description**: Designs deployment strategies and rollout procedures for production systems.

### 36. cybersecurity
- **Layer**: 2 (Infra/Sec)
- **Triggers**: "security operations", "cybersecurity", "security monitoring", "threat detection"
- **Inputs**: Infrastructure specs, threat intelligence, security policies, incident reports
- **Outputs**: Security operations plan, monitoring setup, threat detection, incident response
- **Dependencies**: offensive-security-analyst, defensive-security-analyst
- **Execution Mode**: Orchestrated
- **Description**: Manages cybersecurity operations, threat detection, and incident response.

### 37. information-security-engineer
- **Layer**: 2 (Infra/Sec)
- **Triggers**: "infosec engineering", "security architecture", "security controls", "security design"
- **Inputs**: Security requirements, threat models, compliance rules, architecture specs
- **Outputs**: Security architecture, control implementations, compliance documentation
- **Dependencies**: cybersecurity, compliance-engineer
- **Execution Mode**: Single
- **Description**: Engineers security architectures and implements security controls.

### 38. incident-management-engineer
- **Layer**: 2 (Infra/Sec)
- **Triggers**: "incident response", "incident management", "security incident", "production incident"
- **Inputs**: Incident reports, severity criteria, response procedures, stakeholder lists
- **Outputs**: Incident response plan, resolution steps, post-mortem, stakeholder communications
- **Dependencies**: deployment-strategist, cybersecurity
- **Execution Mode**: Single
- **Description**: Manages incident response and resolution for security and production incidents.

### 39. offensive-security-analyst
- **Layer**: 2 (Infra/Sec)
- **Triggers**: "penetration test", "vulnerability assessment", "red team", "security audit", "exploit development", "attack surface analysis"
- **Inputs**: Target systems, scope, attack vectors, testing criteria
- **Outputs**: Vulnerability report, exploit demonstrations, remediation recommendations
- **Dependencies**: defensive-security-analyst, ai-redteam
- **Execution Mode**: Single
- **Description**: Conducts penetration testing, vulnerability assessments, and red team operations.

### 40. defensive-security-analyst
- **Layer**: 2 (Infra/Sec)
- **Triggers**: "blue team", "defensive security", "threat hunting", "security monitoring", "incident detection"
- **Inputs**: Threat intelligence, monitoring data, incident reports, security policies
- **Outputs**: Threat detection, monitoring setup, incident analysis, defensive recommendations
- **Dependencies**: offensive-security-analyst, d3fend-harden
- **Execution Mode**: Single
- **Description**: Conducts defensive security operations, threat hunting, and incident detection.

### 41. compliance-engineer
- **Layer**: 2 (Infra/Sec)
- **Triggers**: "compliance audit", "regulatory compliance", "compliance engineering", "compliance automation"
- **Inputs**: Compliance requirements, regulatory rules, audit criteria, system specs
- **Outputs**: Compliance report, audit results, automation scripts, remediation plan
- **Dependencies**: information-security-engineer, commercial-counsel
- **Execution Mode**: Single
- **Description**: Engineers compliance automation and conducts regulatory compliance audits.

### 42-48. D3FEND Framework (7 skills)
- **Layer**: 2 (Infra/Sec)
- **Triggers**: "d3fend", "cyber defense framework", "defense operations"
- **Skills**:
  - d3fend-harden: "harden systems", "security hardening"
  - d3fend-detect: "detect threats", "threat detection"
  - d3fend-evict: "evict threats", "threat removal"
  - d3fend-isolate: "isolate systems", "network isolation"
  - d3fend-restore: "restore systems", "system recovery"
  - d3fend-model: "model threats", "threat modeling"
  - d3fend-deceive: "deceive attackers", "deception technology"
- **Dependencies**: defensive-security-analyst, compliance-engineer
- **Execution Mode**: Chain
- **Description**: Implements D3FEND cyber defense framework for comprehensive threat response.

---

## Layer 1: Software Engineering (9 skills)

### 49. senior-system-architecture
- **Layer**: 1 (Software)
- **Triggers**: "system architecture", "architecture design", "system design", "technical architecture"
- **Inputs**: Business requirements, scalability needs, integration points, technology constraints
- **Outputs**: Architecture design, technology stack, integration plan, scalability analysis
- **Dependencies**: business-consultant, senior-fullstack-developer
- **Execution Mode**: Single
- **Description**: Designs enterprise system architecture and technology stack selection.

### 50. senior-fullstack-developer
- **Layer**: 1 (Software)
- **Triggers**: "fullstack development", "build application", "web development", "api development"
- **Inputs**: Architecture specs, feature requirements, design mockups, integration APIs
- **Outputs**: Application code, API implementations, integration code, documentation
- **Dependencies**: senior-system-architecture, senior-frontend-software-engineer
- **Execution Mode**: Single
- **Description**: Develops fullstack applications with frontend and backend expertise.

### 51. fullstack-software-engineer
- **Layer**: 1 (Software)
- **Triggers**: "software engineering", "application development", "code development", "feature implementation"
- **Inputs**: Feature specs, design requirements, API contracts, testing criteria
- **Outputs**: Feature implementations, code, tests, documentation
- **Dependencies**: senior-fullstack-developer, ui-software-engineer
- **Execution Mode**: Single
- **Description**: Implements software features and application functionality.

### 52. senior-software-engineer
- **Layer**: 1 (Software)
- **Triggers**: "senior engineering", "code review", "technical leadership", "engineering best practices"
- **Inputs**: Codebase, review criteria, performance requirements, quality standards
- **Outputs**: Code reviews, technical guidance, best practices, mentoring
- **Dependencies**: fullstack-software-engineer, senior-frontend-software-engineer
- **Execution Mode**: Single
- **Description**: Provides senior engineering leadership, code review, and technical guidance.

### 53. senior-frontend-software-engineer
- **Layer**: 1 (Software)
- **Triggers**: "frontend development", "ui implementation", "frontend architecture", "responsive design"
- **Inputs**: Design mockups, component specs, performance requirements, accessibility criteria
- **Outputs**: Frontend code, component implementations, responsive designs, accessibility compliance
- **Dependencies**: senior-fullstack-developer, ui-software-engineer
- **Execution Mode**: Single
- **Description**: Develops frontend applications with architecture and performance expertise.

### 54. ui-software-engineer
- **Layer**: 1 (Software)
- **Triggers**: "ui development", "component development", "ui implementation", "design system"
- **Inputs**: Design specs, component requirements, design system, interaction patterns
- **Outputs**: UI components, design system implementations, interaction code
- **Dependencies**: senior-frontend-software-engineer, ux-software-engineer
- **Execution Mode**: Single
- **Description**: Implements UI components and design system elements.

### 55. ux-software-engineer
- **Layer**: 1 (Software)
- **Triggers**: "ux development", "user experience", "ux implementation", "interaction design"
- **Inputs**: UX research, user flows, interaction specs, accessibility requirements
- **Outputs**: UX implementations, interaction code, accessibility features, user testing results
- **Dependencies**: ui-software-engineer, support-engineer
- **Execution Mode**: Single
- **Description**: Implements UX patterns and interaction designs with accessibility focus.

### 56. web-application-developer
- **Layer**: 1 (Software)
- **Triggers**: "web app development", "web application", "web development", "browser application"
- **Inputs**: Feature specs, design requirements, browser compatibility, performance criteria
- **Outputs**: Web application code, browser-compatible implementations, performance optimizations
- **Dependencies**: senior-frontend-software-engineer, ux-software-engineer
- **Execution Mode**: Single
- **Description**: Develops web applications with browser compatibility and performance optimization.

### 57. support-engineer
- **Layer**: 1 (Software)
- **Triggers**: "support engineering", "customer support", "technical support", "user assistance"
- **Inputs**: User reports, bug reports, feature requests, documentation needs
- **Outputs**: Support responses, bug fixes, documentation, user guidance
- **Dependencies**: ux-software-engineer, product-support-specialist
- **Execution Mode**: Single
- **Description**: Provides technical support and user assistance for applications.

---

## Layer 0: Business & Operations (17 skills)

### 58. business-model-researcher
- **Layer**: 0 (Business)
- **Triggers**: "business model research", "market analysis", "business strategy", "competitive analysis"
- **Inputs**: Market data, competitor info, industry trends, business goals
- **Outputs**: Business model analysis, market research, competitive landscape, strategy recommendations
- **Dependencies**: None
- **Execution Mode**: Single
- **Description**: Researches business models, markets, and competitive landscapes.

### 59. business-consultant
- **Layer**: 0 (Business)
- **Triggers**: "business consulting", "strategy consulting", "business advice", "organizational design"
- **Inputs**: Business challenges, organizational data, market context, stakeholder needs
- **Outputs**: Consulting recommendations, strategy documents, organizational designs
- **Dependencies**: business-model-researcher, senior-system-architecture
- **Execution Mode**: Single
- **Description**: Provides business consulting and strategic advisory services.

### 60. commercial-counsel
- **Layer**: 0 (Business)
- **Triggers**: "commercial legal", "contract review", "legal advice", "commercial agreements"
- **Inputs**: Contract drafts, legal requirements, business terms, compliance rules
- **Outputs**: Legal review, contract recommendations, compliance assessment, risk analysis
- **Dependencies**: corporate-counsel, deal-operations-administrator
- **Execution Mode**: Single
- **Description**: Provides commercial legal counsel and contract review services.

### 61. corporate-counsel
- **Layer**: 0 (Business)
- **Triggers**: "corporate legal", "corporate governance", "corporate compliance", "legal entity"
- **Inputs**: Corporate structure, governance requirements, compliance rules, entity data
- **Outputs**: Governance framework, compliance documentation, entity management, legal advice
- **Dependencies**: commercial-counsel, compliance-engineer
- **Execution Mode**: Single
- **Description**: Manages corporate legal affairs, governance, and compliance.

### 62. senior-revenue-accountant
- **Layer**: 0 (Business)
- **Triggers**: "revenue accounting", "revenue recognition", "financial reporting", "accounting standards"
- **Inputs**: Transaction data, revenue contracts, accounting standards, reporting requirements
- **Outputs**: Revenue recognition, financial reports, compliance documentation, audit support
- **Dependencies**: deal-operations-administrator, product-management-monetization
- **Execution Mode**: Single
- **Description**: Manages revenue accounting, recognition, and financial reporting.

### 63. deal-operations-administrator
- **Layer**: 0 (Business)
- **Triggers**: "deal operations", "deal management", "contract administration", "deal execution"
- **Inputs**: Deal terms, contract requirements, execution criteria, stakeholder lists
- **Outputs**: Deal execution plan, contract administration, stakeholder coordination, status reports
- **Dependencies**: commercial-counsel, senior-revenue-accountant
- **Execution Mode**: Single
- **Description**: Manages deal operations, contract administration, and execution workflows.

### 64. transaction-manager
- **Layer**: 0 (Business)
- **Triggers**: "transaction management", "payment processing", "transaction workflow", "transaction monitoring"
- **Inputs**: Transaction requirements, payment specs, monitoring criteria, compliance rules
- **Outputs**: Transaction workflows, payment processing, monitoring setup, compliance reports
- **Dependencies**: senior-revenue-accountant, transaction-principal
- **Execution Mode**: Single
- **Description**: Manages transaction workflows, payment processing, and monitoring.

### 65. transaction-principal
- **Layer**: 0 (Business)
- **Triggers**: "transaction principal", "transaction strategy", "transaction architecture", "transaction design"
- **Inputs**: Business requirements, transaction volumes, scalability needs, compliance rules
- **Outputs**: Transaction architecture, strategy document, scalability plan, compliance framework
- **Dependencies**: transaction-manager, product-management-monetization
- **Execution Mode**: Single
- **Description**: Designs transaction architecture and strategic transaction frameworks.

### 66. product-management-monetization
- **Layer**: 0 (Business)
- **Triggers**: "product monetization", "pricing strategy", "revenue model", "monetization design"
- **Inputs**: Product specs, market data, pricing requirements, revenue goals
- **Outputs**: Monetization strategy, pricing model, revenue projections, go-to-market plan
- **Dependencies**: business-consultant, transaction-principal
- **Execution Mode**: Single
- **Description**: Designs product monetization strategies and pricing models.

### 67. product-management-human-data-platform
- **Layer**: 0 (Business)
- **Triggers**: "human data platform", "data product management", "human-centric data", "data platform strategy"
- **Inputs**: Platform requirements, user needs, data sources, privacy requirements
- **Outputs**: Platform strategy, product roadmap, user experience design, privacy framework
- **Dependencies**: product-designer, data-architect
- **Execution Mode**: Single
- **Description**: Manages human-centric data platforms and product strategy.

### 68. product-designer
- **Layer**: 0 (Business)
- **Triggers**: "product design", "design thinking", "user research", "product strategy"
- **Inputs**: User needs, market research, business goals, design constraints
- **Outputs**: Product designs, user research, design strategy, prototype specifications
- **Dependencies**: business-consultant, customer-ops-specialist
- **Execution Mode**: Single
- **Description**: Designs products with user research and design thinking methodologies.

### 69. customer-ops-specialist
- **Layer**: 0 (Business)
- **Triggers**: "customer operations", "customer success", "customer experience", "customer workflow"
- **Inputs**: Customer data, experience metrics, workflow requirements, success criteria
- **Outputs**: Operations plan, experience improvements, workflow optimizations, success metrics
- **Dependencies**: product-designer, product-support-specialist
- **Execution Mode**: Single
- **Description**: Manages customer operations, success, and experience optimization.

### 70. product-support-specialist
- **Layer**: 0 (Business)
- **Triggers**: "product support", "customer support", "support workflow", "support optimization"
- **Inputs**: Support tickets, user feedback, product data, support metrics
- **Outputs**: Support workflows, optimization recommendations, user guidance, metrics reports
- **Dependencies**: customer-ops-specialist, community-executive-escalations-program-manager
- **Execution Mode**: Single
- **Description**: Manages product support workflows and customer assistance.

### 71. community-executive-escalations-program-manager
- **Layer**: 0 (Business)
- **Triggers**: "community management", "escalation management", "program management", "community engagement"
- **Inputs**: Community data, escalation reports, program requirements, engagement metrics
- **Outputs**: Community strategy, escalation procedures, program plans, engagement reports
- **Dependencies**: product-support-specialist, communication-lead
- **Execution Mode**: Single
- **Description**: Manages community engagement, escalations, and program coordination.

### 72. communication-lead
- **Layer**: 0 (Business)
- **Triggers**: "communication strategy", "internal communication", "external communication", "messaging"
- **Inputs**: Communication requirements, stakeholder lists, messaging guidelines, channel preferences
- **Outputs**: Communication strategy, messaging frameworks, channel plans, engagement reports
- **Dependencies**: community-executive-escalations-program-manager, developer-education-lead
- **Execution Mode**: Single
- **Description**: Leads internal and external communication strategy and messaging.

### 73. developer-education-lead
- **Layer**: 0 (Business)
- **Triggers**: "developer education", "technical training", "developer advocacy", "education program"
- **Inputs**: Developer needs, training requirements, education goals, content specs
- **Outputs**: Education programs, training materials, advocacy strategy, developer resources
- **Dependencies**: communication-lead, people-operations-specialist
- **Execution Mode**: Single
- **Description**: Leads developer education, training, and advocacy programs.

### 74. people-operations-specialist
- **Layer**: 0 (Business)
- **Triggers**: "people operations", "hr operations", "employee experience", "workforce management"
- **Inputs**: Employee data, workforce requirements, experience metrics, compliance rules
- **Outputs**: Operations plan, experience improvements, workforce strategies, compliance reports
- **Dependencies**: developer-education-lead, business-consultant
- **Execution Mode**: Single
- **Description**: Manages people operations, employee experience, and workforce strategies.

---

## Layer -1: Physical Infrastructure (6 skills)

### 75. data-center-design-execution-lead
- **Layer**: -1 (Physical)
- **Triggers**: "data center design", "dc design", "data center build", "facility design"
- **Inputs**: Facility requirements, power needs, cooling specs, space constraints
- **Outputs**: DC design, build plan, power/cooling specs, space optimization
- **Dependencies**: data-center-portfolio-planning-execution-lead, data-center-compute-supply-efficiency
- **Execution Mode**: Single
- **Description**: Designs and executes data center construction and facility optimization.

### 76. data-center-portfolio-planning-execution-lead
- **Layer**: -1 (Physical)
- **Triggers**: "dc portfolio planning", "data center strategy", "facility portfolio", "dc planning"
- **Inputs**: Portfolio requirements, capacity needs, geographic constraints, budget
- **Outputs**: Portfolio strategy, capacity planning, geographic distribution, budget allocation
- **Dependencies**: None
- **Execution Mode**: Single
- **Description**: Plans and executes data center portfolio strategy and capacity allocation.

### 77. data-center-compute-supply-efficiency
- **Layer**: -1 (Physical)
- **Triggers**: "compute supply", "dc efficiency", "compute optimization", "resource efficiency"
- **Inputs**: Compute requirements, efficiency metrics, resource allocation, optimization goals
- **Outputs**: Supply plan, efficiency improvements, resource optimization, capacity reports
- **Dependencies**: data-center-design-execution-lead, director-infrastructure-capex-accounting
- **Execution Mode**: Single
- **Description**: Manages compute supply and efficiency optimization in data centers.

### 78. director-infrastructure-capex-accounting
- **Layer**: -1 (Physical)
- **Triggers**: "capex accounting", "infrastructure accounting", "capital expenditure", "dc finance"
- **Inputs**: Capex requirements, accounting standards, budget constraints, financial reports
- **Outputs**: Capex accounting, financial reports, budget allocation, compliance documentation
- **Dependencies**: data-center-compute-supply-efficiency, senior-data-center-capacity-delivery-manager
- **Execution Mode**: Single
- **Description**: Manages infrastructure capital expenditure accounting and financial reporting.

### 79. senior-data-center-capacity-delivery-manager
- **Layer**: -1 (Physical)
- **Triggers**: "dc capacity", "capacity delivery", "data center capacity", "capacity management"
- **Inputs**: Capacity requirements, delivery timelines, resource allocation, SLA criteria
- **Outputs**: Capacity plan, delivery schedule, resource allocation, SLA reports
- **Dependencies**: director-infrastructure-capex-accounting, field-services-engineer
- **Execution Mode**: Single
- **Description**: Manages data center capacity planning and delivery execution.

### 80. field-services-engineer
- **Layer**: -1 (Physical)
- **Triggers**: "field services", "dc maintenance", "hardware repair", "on-site support"
- **Inputs**: Maintenance requests, hardware specs, repair requirements, SLA criteria
- **Outputs**: Maintenance plans, repair procedures, on-site support, SLA compliance
- **Dependencies**: senior-data-center-capacity-delivery-manager
- **Execution Mode**: Single
- **Description**: Provides field services, hardware maintenance, and on-site support for data centers.

---

## Summary Statistics

| Layer | Skills | % of Total |
|-------|--------|------------|
| L5: Governance & Orchestration | 7 | 8.1% |
| L4: AI & ML Operations | 12 | 14.0% |
| L3: Data & Analytics | 9 | 10.5% |
| L2: Infrastructure & Security | 19 | 22.1% |
| L1: Software Engineering | 9 | 10.5% |
| L0: Business & Operations | 17 | 19.8% |
| L-1: Physical Infrastructure | 6 | 7.0% |
| **Total** | **86** | **100%** |

## Execution Mode Distribution

| Mode | Skills | % of Total |
|------|--------|------------|
| Single | 72 | 83.7% |
| Chain | 7 | 8.1% |
| Orchestrated | 7 | 8.1% |
| **Total** | **86** | **100%** |
