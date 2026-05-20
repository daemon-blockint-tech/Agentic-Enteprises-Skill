# Agentic Enterprise OS — Skill Registry

## Overview

Catalog of **198** skills in the Agentic Enterprise OS. Each entry maps a folder
(`<skill-name>/SKILL.md`) to its display name, routing layer, and `description` triggers.

**Distribution:** Install via [skills.sh](https://skills.sh) / [skills CLI](https://www.skills.sh/docs/cli):

```bash
npx skills add daemon-blockint-tech/Agentic-Enteprises-Skill --list
npx skills add daemon-blockint-tech/Agentic-Enteprises-Skill --skill <folder-name> --agent cursor -y
```

**Source repo:** [github.com/daemon-blockint-tech/Agentic-Enteprises-Skill](https://github.com/daemon-blockint-tech/Agentic-Enteprises-Skill)

**Authoritative triggers:** `description` in each skill's YAML frontmatter (not this file).

---

## Layer 5: Governance & Orchestration (15 skills)

| # | Folder | Display name | Summary |
|---|--------|--------------|---------|
| 1 | `ai-risk-governance` | ai-risk-governance | Guides AI risk management and governance—use-case risk assessment, model/system documentation, policies and guardrails, human oversight, third-party model/vendor review, and mapping to frameworks (NIST AI RMF, ISO 42001, EU AI Act concepts, internal AI policy). Use when classifyi… |
| 2 | `ai-skill-manager` | ai-skill-manager | Guides management of an enterprise Agent Skills portfolio—inventory and catalog hygiene, naming and structure standards, overlap and routing deduplication, cross-linking between skills, validation and packaging at scale, lifecycle (split, merge, deprecate), and quality/security r… |
| 3 | `build-validator` | build-validator | Validate plans, designs, and implementations before execution to prevent costly mistakes. Cover architecture review, security audit, scalability assessment, cost analysis, compliance check, and risk identification. Produce go/no-go decisions with specific remediation steps. Trigg… |
| 4 | `communication-lead` | communication-lead | Guides communications leadership—messaging strategy, narrative and key-message development, stakeholder and executive comms cadence, internal announcements (all-hands, change, crisis), external customer and partner messaging, launch and incident communication plans, channel selec… |
| 5 | `community-executive-escalations-program-manager` | community-executive-escalations-program-manager | Guides program management for community and executive customer escalations—intake and triage frameworks, severity matrices, cross-functional war rooms, executive briefings, SLA design, playbooks for VIP and public-facing issues, decision logs, and program metrics. Use when standi… |
| 6 | `country-manager` | country-manager | This skill should be used when the user asks about country manager, managing director, in-country GM, market entry, localize the business, country P&L, country business plan, matrix organization, local leadership team, government relations, country operations, territory plan, or … |
| 7 | `cross-department-translation` | Cross-Department Translation | Reframes messages, requirements, metrics, and decisions for organizational audiences—engineering, product, finance, legal, compliance, sales, operations, actuarial, and executive—by detecting jargon, surfacing implicit assumptions, producing dual-audience briefs, RACI-aligned han… |
| 8 | `cyber-diligence-governance` | cyber-diligence-governance | Guides cyber due diligence and governance—M&A/investment diligence, vendor and third-party assessments, questionnaire and evidence review, control maturity and gaps, integration risk, IC/board cyber briefs, and governance cadence. Use for target or vendor security diligence, SIG/… |
| 9 | `deployment-strategist` | deployment-strategist | Guides deployment and release strategy—choosing rollout patterns (rolling, blue-green, canary, feature flags), environment topology, promotion paths, blast-radius control, rollback design, change windows, and cross-team rollout plans for web, API, data, and ML workloads. Use when… |
| 10 | `engineering-manager-agent-prompts-evals` | engineering-manager-agent-prompts-evals | Guides engineering managers leading teams that own agent prompts, tool schemas, golden eval suites, judge programs, and prompt regression CI—org design, hiring, roadmap with PM/risk, release governance, and team KPIs for eval quality and prompt stability. Use when managing prompt… |
| 11 | `engineering-manager-vertical-ai-products` | engineering-manager-vertical-ai-products | Guides engineering managers leading vertical AI product teams—industry or domain-specific copilots and AI features (not horizontal platform)—org design, hiring, roadmap with PM and GTM, vertical launch governance (eval, safety, cost), squad capacity, and escalation across shared … |
| 12 | `enterprise-strategist` | enterprise-strategist | This skill should be used when the user asks about enterprise strategy, corporate strategy, business unit strategy, portfolio prioritization, strategic roadmap, growth strategy, diversification, operating model, capability map, strategic initiative, enterprise transformation, boa… |
| 13 | `technical-program-manager` | technical-program-manager | Guides technical program management—multi-team initiatives with dependencies, milestones, RAID tracking, launch readiness, stakeholder status, and cross-functional coordination across engineering, product, and infrastructure (not application code or BRDs). Use when running a tech… |
| 14 | `technical-program-manager-security-cvd` | technical-program-manager-security-cvd | Guides technical program management for security coordinated vulnerability disclosure (CVD)— disclosure policy, intake and triage SLAs, researcher coordination, fix/remediation tracking, embargo and publication timelines, CVE/advisory coordination, bug bounty program operations, … |
| 15 | `zero-tolerance-for-failure` | zero-tolerance-for-failure | Guides failure-prevention culture and operational excellence for mission-critical engineering— zero-defect aspiration vs error budgets; HRO principles; defense-in-depth; fail-safe/fail-closed; verification gates and independent checks; redundancy and graceful degradation; pre-mor… |

---

## Layer 4: AI & ML Operations (22 skills)

| # | Folder | Display name | Summary |
|---|--------|--------------|---------|
| 16 | `agentic-ai-developer` | agentic-ai-developer | Guides hands-on development of agentic AI systems—agent loops (plan → act → observe), tool and MCP schemas, multi-agent orchestration and handoffs, state/checkpointing, HITL gates, agent prompts, reliability (retries, idempotency, cancellation), observability, trajectory evaluati… |
| 17 | `ai-adversarial-robustness-engineer` | ai-adversarial-robustness-engineer | Adversarial robustness engineering for ML/AI—evasion, poisoning, extraction, membership-inference threat models; robust training, sanitization, detectors; ASR/certified evals; lab model attacks; data-pipeline integrity; production I/O guardrails (classical ML and LLM/multimodal).… |
| 18 | `ai-context-engineer` | ai-context-engineer | Guides context engineering for LLM systems—assembling prompts, budgeting tokens, prioritizing sources, compressing history, caching, structured context blocks, and debugging context-related failures (lost instructions, overflow, distraction). Use when designing what enters the mo… |
| 19 | `ai-engineer` | ai-engineer | Guides production AI engineering—LLM apps, RAG, agents, eval harnesses, observability, cost/latency, and safe deployment. Use when building chatbots, copilots, retrieval, agent workflows, model routing, or LLM API integration—not research synthesis (ai-researcher), AI policy (ai-… |
| 20 | `ai-lead-ops` | ai-lead-ops | Guides AI ops leadership—LLM SRE, model/prompt releases, eval/incidents, cost/capacity, vendors, and cross-functional cadence. Use for AI platform ops, LLM SLAs, incidents, rollout governance, unit economics, red-team/eval gates, and team rituals—not memory (ai-memory-developer),… |
| 21 | `ai-memory-developer` | ai-memory-developer | Guides design and implementation of AI agent and application memory—short-term conversation state, long-term user/tenant memory, episodic vs semantic stores, consolidation, retrieval, forgetting, privacy retention, and eval of memory quality. Use when building persistent memory f… |
| 22 | `ai-redteam` | ai-redteam | Guides adversarial testing of AI systems—prompt injection, jailbreaks, tool abuse, data exfiltration, bias and harmful output probes, multi-turn attacks, and automated red-team harnesses for LLM applications. Use when red-teaming chatbots, agents, RAG systems, or copilots before … |
| 23 | `ai-researcher` | ai-researcher | Guides AI research work—literature reviews, hypothesis formation, experiment design, benchmarking, reproducibility, and synthesis of papers and empirical results for technical decisions. Use when surveying state of the art, comparing models or methods, designing ablation studies,… |
| 24 | `ai-token-improvement-plan-engineer` | ai-token-improvement-plan-engineer | Guides creation of AI token and cost improvement plans—baseline audits, spend attribution, optimization initiative backlog (prompt, context, model routing, RAG, agents), impact estimates, quality guardrails, measurement KPIs, and phased rollout with owners. Use when building a to… |
| 25 | `applied-ai-architect-commercial-enterprise` | applied-ai-architect-commercial-enterprise | Guides applied AI solution architecture for commercial (B2B SaaS, multi-tenant product) and enterprise (internal copilots, regulated corp data) contexts—reference patterns for RAG, agents, and copilots, platform and model selection, data boundaries, identity, observability, cost … |
| 26 | `markup-detection` | Markup Detection | This skill should be used when the user asks for markup detection, detect manipulation, image tampering, deepfake detection, document integrity, hidden markup, metadata forensics, EXIF analysis, content authenticity, synthetic media, altered image, C2PA, or provenance verificatio… |
| 27 | `ml-infrastructure-engineer-safeguards` | ml-infrastructure-engineer-safeguards | Guides ML infrastructure for safeguards—inference gateways, model serving (GPU/CPU), guardrail and moderation pipelines in the request path, policy enforcement hooks, safety observability, rollout of filter/model versions, and reliability of the protected inference plane. Use whe… |
| 28 | `ml-research-engineer-safeguards` | ml-research-engineer-safeguards | Guides ML/research engineering for safeguards—safety classifier development, harm benchmarks and eval suites, labeled dataset design, fine-tuning and ablations, calibration and slice analysis, attack-surface research memos, and promotion criteria for new moderation models. Use wh… |
| 29 | `ml-systems-engineer-rl-engineering` | ml-systems-engineer-rl-engineering | Guides ML systems engineering for reinforcement learning—distributed training platforms, rollout workers and vectorized environments, replay buffers, policy/critic serving for train loops, checkpointing and experiment tracking, sim-to-real hooks, and RL training reliability. Use … |
| 30 | `multi-agent-system-engineer` | multi-agent-system-engineer | Guides engineering of multi-agent systems—agent roles and specialization, orchestration topologies (supervisor, peer-to-peer, hierarchical, blackboard), task decomposition and routing, inter-agent messaging (A2A-style patterns), shared vs partitioned state, fan-out/fan-in and DAG… |
| 31 | `privacy-research-engineer-safeguards` | privacy-research-engineer-safeguards | Guides privacy research engineering for safeguards—PII and sensitive-data detection research, redaction and de-identification evals, memorization and extraction risk studies, privacy benchmarks and labeled corpora, logging/retention minimization for safety pipelines, and research… |
| 32 | `prompt-engineer` | prompt-engineer | Design, test, and optimize prompts for LLM interactions. Cover prompt patterns (few-shot, chain-of-thought, ReAct), system prompt design, output formatting, prompt evaluation, and prompt optimization techniques. Triggers on "write prompt", "optimize prompt", "design system prompt… |
| 33 | `prompt-engineer-agent-prompts-evals` | prompt-engineer-agent-prompts-evals | Guides prompt engineering for tool-using agents—system and developer prompts, tool schemas, handoffs and subagents, golden datasets, offline eval harnesses, regression CI, LLM-as-judge rubrics, and release gates for prompt changes. Use when authoring agent prompts, building eval … |
| 34 | `research-engineer-scientist-tokens` | research-engineer-scientist-tokens | Guides research engineering and science on LLM tokens—hypotheses about context use, tokenization, compression, and inference efficiency; rigorous benchmarks (tokens per task, quality–cost Pareto); ablation design; instrumentation and reproducible logs; and research memos that inf… |
| 35 | `sentiment-analysis-engineer` | Sentiment Analysis Engineer | This skill should be used when the user asks to build or evaluate sentiment and opinion-mining systems—label schemas, lexicon/ML/transformer/LLM classifiers, annotation and IAA, F1/calibration, domain adaptation, multilingual/code-switching, sarcasm/negation/bias, and production … |
| 36 | `sentiment-forecasting-engineer` | Sentiment Forecasting Engineer | This skill should be used when the user asks to forecast aggregate sentiment and opinion dynamics over time—sentiment indices from text streams; temporal rollups; leading/lagging KPI links; time-series and sequence models (ARIMA, Prophet, state-space, ML); nowcasting; spikes, bot… |
| 37 | `tactical-ai-autonomy-developer` | tactical-ai-autonomy-developer | Guides edge and tactical autonomous systems—perception-planning-control under latency and safety constraints; behavior trees/state machines vs learned policies; human-on-the-loop; geofencing, no-strike rules, mission abort; sim and field testing; ROS2/middleware patterns; sensor … |

---

## Layer 3: Data & Analytics (18 skills)

| # | Folder | Display name | Summary |
|---|--------|--------------|---------|
| 38 | `ab-testing-engineer` | A/B Testing Engineer | Guides experimentation engineering for A/B and multivariate tests—hypothesis framing, primary/secondary/guardrail metrics, design (A/B, A/B/n, MVT), sample size and power, duration and seasonality, allocation and randomization units, SRM checks, instrumentation, analysis plans (f… |
| 39 | `analytics-data-engineer` | analytics-data-engineer | Guides analytics engineering—dbt (or equivalent) project structure, staging/intermediate/mart models, dimensional and wide-mart patterns, incremental and CDC loads, data tests and contracts, documentation and lineage, CI for analytics code, and handoff to BI semantic layers. Use … |
| 40 | `analytics-data-engineering-manager-product` | analytics-data-engineering-manager-product | Guides managers of product-embedded analytics engineering teams—org design, hiring and levels, roadmap and prioritization with product managers, analytics data product delivery, squad alignment, stakeholder forums, team KPIs, and escalation paths for metric and mart quality. Use … |
| 41 | `bi-analyst` | bi-analyst | Design dashboards, write analytical SQL, define KPIs, and manage stakeholder analytics requirements. Cover chart selection, data storytelling, cohort/funnel analysis, metric definitions, and BI tool patterns (Tableau, Looker, Power BI). Triggers on "build dashboard", "design dash… |
| 42 | `business-analyst` | business-analyst | Run a structured business analysis workflow: requirements elicitation with stakeholder interviews and MoSCoW prioritization, as-is/to-be process mapping with BPMN notation, data-driven analysis (CBA, SWOT, root cause), and production-ready documentation (BRD, FRD, user stories wi… |
| 43 | `data-architect` | data-architect | Design data architecture at enterprise and solution levels. Cover data mesh, lakehouse, governance, domain-driven design, conceptual/logical/physical data modeling, platform selection, and compliance frameworks. Produce ADRs, data model diagrams, platform comparison matrices, and… |
| 44 | `data-manager` | data-manager | Manage data programs, governance operations, and data reliability. Cover data roadmaps, stakeholder coordination, metadata stewardship, lifecycle management, monitoring, incident response, capacity planning, and SLA frameworks. Triggers on "manage data team", "data roadmap", "gov… |
| 45 | `data-scientist` | data-scientist | Execute data science workflows from exploration to production. Apply machine learning modeling, statistical analysis, A/B testing, causal inference, feature engineering, model evaluation, and MLOps patterns. Triggers on "build predictive model", "design A/B test", "feature engine… |
| 46 | `data-scrubbing` | Data Scrubbing | Guides cleaning and standardizing tabular datasets before analysis, modeling, or reporting—profiling, quality rules, missing values, duplicates, outliers, type coercion, encoding fixes, record linkage, deduplication, high-level PII handling (not legal advice), actuarial/insurance… |
| 47 | `data-system-ops-lead` | data-system-ops-lead | Run data system operations and reliability engineering. Cover pipeline monitoring, incident response, SLA management, capacity planning, on-call runbooks, data quality alerting, and operational excellence. Triggers on "data pipeline monitoring", "incident response", "SLA manageme… |
| 48 | `data-visualization` | Data Visualization | Guides data visualization design—chart type selection for message and audience, honest scales and labeling, color and accessibility, executive and operational dashboard layout, actuarial and insurance charts (loss triangles, trends, distributions), ethics and misleading-viz avoid… |
| 49 | `data-warehouse-engineer` | data-warehouse-engineer | Design and implement data warehouses. Cover star/snowflake schemas, dimensional modeling, SQL optimization, ETL/ELT patterns, partitioning strategies, and warehouse-specific features (Snowflake, BigQuery, Redshift). Triggers on "design star schema", "optimize SQL query", "build E… |
| 50 | `edi-engineer` | edi-engineer | Guides design, implementation, and operation of B2B electronic data interchange—X12 and EDIFACT, transaction mapping (850/855/856/810/997, ORDERS/DESADV/INVOIC/APERAK), canonical-to-segment translation, partner implementation guides, syntax and SNIP validation, functional acks an… |
| 51 | `geospatial-telematics-developer` | geospatial-telematics-developer | Builds location-aware systems—CRS/projections; GeoJSON, Shapefile, GeoTIFF, MVT; PostGIS spatial SQL; indexes and tiling; OGC WMS/WFS/WMTS integration; map matching, trajectories, geofencing; fleet telematics (GPS/GNSS, NMEA, timestamps, CAN metadata); streams and batch ETL; loca… |
| 52 | `ontology-engineer` | ontology-engineer | Design ontologies and build knowledge graphs. Cover OWL/RDF ontologies, SKOS taxonomies, SPARQL querying, knowledge graph construction, semantic reasoning, and linked data patterns. Triggers on "build ontology", "design knowledge graph", "create taxonomy", "SPARQL query", "semant… |
| 53 | `operations-research-algorithm-developer` | operations-research-algorithm-developer | Formulate and implement operations research optimization models—LP, MIP/QP, constraint programming, network flows, assignment, VRP, scheduling, resource allocation, inventory/production planning; heuristics and metaheuristics; sensitivity and infeasibility diagnosis; solver integ… |
| 54 | `predictive-analytics` | Predictive Analytics | Guides applied predictive analytics for business—target and leakage framing, tabular feature engineering, regression and classification models (baselines, boosting, regularized linear), validation splits and metrics, calibration and cost-sensitive thresholds, practitioner explain… |
| 55 | `quantitative-researcher` | Quantitative Researcher | Guides quantitative research for markets and finance—research question framing, data sourcing and quality checks, descriptive and inferential statistics, time series and panel methods (high level), factor and signal research, backtest design and pitfalls (lookahead, survivorship)… |

---

## Layer 2: Infrastructure, Cloud & Security (68 skills)

| # | Folder | Display name | Summary |
|---|--------|--------------|---------|
| 56 | `advanced-persistent-threat` | advanced-persistent-threat | Guides advanced persistent threat (APT) analysis—nation-state and sophisticated criminal campaigns, long-dwell intrusions, campaign lifecycle tracking, MITRE ATT&CK TTP mapping, infrastructure and malware correlation, attribution with explicit confidence levels, intel fusion for … |
| 57 | `bcm-disaster-recovery-specialist` | bcm-disaster-recovery-specialist | Guides security-focused business continuity and disaster recovery—BIA for critical security and IT services, RTO/RPO for identity and security tooling, cyber-resilient BCP/DRP, ransomware and destructive-attack recovery playbooks, backup/immutability and restore testing, crisis c… |
| 58 | `certified-information-systems-security-professional` | certified-information-systems-security-professional | Guides security leadership aligned with the (ISC)² CISSP CBK—eight domains: Security and Risk Management; Asset Security; Security Architecture and Engineering; Communication and Network Security; IAM; Security Assessment and Testing; Security Operations; Software Development Sec… |
| 59 | `chief-information-security-officer` | chief-information-security-officer | Guides executive security leadership—security program strategy and operating model, risk appetite and board or audit-committee reporting, KRIs and leadership metrics, incident escalation and crisis communications, security budget and org design, regulatory and audit relationships… |
| 60 | `ci-cd-engineer` | CI/CD Engineer | Guides CI/CD engineering—pipeline design, build/test/deploy stages, branch and environment strategy, artifact promotion, workflow-level deploy patterns (rolling, blue-green, canary), CI secrets, security gates, flaky tests, monorepo/polyrepo layout, DORA metrics, and rollback/rel… |
| 61 | `cicd-engineer` | cicd-engineer | Guides CI/CD for agent skills repositories and skill packages—pipeline design (build, test, validate, package), GitHub Actions for PR checks and release promotion, environment gates, secrets hygiene (no secrets in repo), skill-creator integration (quick_validate.py, package_skill… |
| 62 | `cisco-certified-network-professional` | Cisco Certified Network Professional | Guides CCNP-level enterprise campus and WAN networking—VLAN/STP/RSTP/MST, EtherChannel, stacking, OSPF/EIGRP/BGP fundamentals, redistribution, FHRP (HSRP/VRRP/GLBP), IPv4/IPv6, WAN/SD-WAN design adjacency, assurance (SNMP, NetFlow/IPFIX, telemetry), 802.1X/ACLs/device hardening, … |
| 63 | `classified-cyber-security-senior-manager` | classified-cyber-security-senior-manager | Guides senior management of classified and high-side cyber programs—cleared workforce/facility alignment, program security plans, RMF/ATO-style authorization interfaces (manager depth), insider risk coordination, classified ops interfaces, government incident escalation, inspecti… |
| 64 | `classified-software-devsecops-engineer` | classified-software-devsecops-engineer | Guides secure software delivery and DevSecOps for cleared/classified or high-side programs—disconnected or air-gapped CI/CD, artifact promotion across classification boundaries (conceptual), SBOM/signing/ provenance, SAST/DAST/secrets/IaC/container gates, supply-chain controls, S… |
| 65 | `cloud-architect` | cloud-architect | Guides cloud solution architecture—Well-Architected alignment, landing zone and org design, workload placement and service selection, network and security segmentation, hybrid and multi-region patterns, migration roadmaps (7Rs), cost architecture, and cloud ADRs with diagrams for… |
| 66 | `cloud-compliance-specialist` | cloud-compliance-specialist | Guides cloud compliance—mapping SOC 2, ISO 27001, HIPAA, PCI DSS, FedRAMP, and data-residency requirements to cloud controls; collecting audit evidence from AWS, GCP, and Azure APIs; shared-responsibility narratives; CSPM/Config continuous monitoring; customer assurance questionn… |
| 67 | `cloud-economist` | cloud-economist | Guides cloud economics—TCO and NPV for cloud vs on-prem or SaaS, pricing-model trade-offs (on-demand, commitments, spot), commitment portfolio economics, marginal cost and elasticity, regional and service cost comparisons, migration and architecture option business cases, and CFO… |
| 68 | `cloud-engineer` | cloud-engineer | Guides cloud engineering on AWS, GCP, and Azure—landing zones and account structure, VPC/VNet networking, compute and autoscaling, object/block storage, managed databases and caches, serverless and messaging, DNS/CDN, cloud IAM and workload identity, multi-AZ/region reliability, … |
| 69 | `cloud-security-engineer` | cloud-security-engineer | Guides cloud security engineering on AWS, GCP, and Azure—org guardrails (SCPs, org policies), cloud IAM and federation, network segmentation and private connectivity, encryption and KMS, logging and audit to SIEM, CSPM and native detective controls (Config, Security Hub, GuardDut… |
| 70 | `cloud-system-administrator` | cloud-system-administrator | Guides cloud system administration—day-2 operations on AWS, GCP, and Azure: access requests and IAM role assignment, key and certificate rotation, OS patching and maintenance windows, backup and restore execution, monitoring and alert triage, quota and limit increases, runbooks, … |
| 71 | `cluster-deployment-engineer` | cluster-deployment-engineer | Guides Kubernetes cluster deployment and operations—cluster bootstrap and upgrades, node pools, add-ons (ingress, CNI, cert-manager), workload delivery with Helm/Kustomize/operators, namespace quotas and RBAC, GitOps sync to clusters, multi-cluster patterns, and production troubl… |
| 72 | `code-security` | code-security | Guides secure coding and security-focused code review across languages and infrastructure—OWASP-oriented vulnerability patterns (injection, XSS, auth, crypto, deserialization, SSRF, XXE), secrets handling, and IaC security (Terraform, Kubernetes, Docker, GitHub Actions). Use when… |
| 73 | `compliance-engineer` | compliance-engineer | Guides compliance engineering—mapping regulatory and framework requirements to technical controls, automating audit evidence, continuous compliance monitoring, gap remediation tracking, and audit-ready documentation for security and privacy programs (SOC 2, ISO 27001, GDPR techni… |
| 74 | `compliance-specialist` | compliance-specialist | Guides cross-functional GRC and compliance programs—framework selection and scope (SOC 2, ISO 27001, HIPAA, PCI, GDPR concepts), control mapping and gap assessments, policy and procedure outlines, audit and assessor coordination prep, vendor security questionnaire support, and co… |
| 75 | `cryptographer-specialist` | Cryptographer Specialist | This skill should be used when the user asks for a cryptographer, cryptography review, help to choose a cipher (AES-GCM, ChaCha20-Poly1305, ECDH, RSA tradeoffs), key management, PKI design, TLS configuration, protocol security or handshake review, authenticated encryption, digita… |
| 76 | `cti-analyst` | cti-analyst | Guides cyber threat intelligence (CTI)—collection and vetting of intel from OSINT, commercial feeds, and ISACs; threat actor and campaign analysis; IOC/TTP production with MITRE ATT&CK mapping; STIX/TAXII and sharing concepts; strategic, tactical, and operational intel briefs; fu… |
| 77 | `cyber-resilience-engineer` | cyber-resilience-engineer | Designs and operates cyber resilience capabilities—RTO/RPO architecture, backup/restore and immutable backup patterns, dependency mapping for critical services, crisis playbooks for ransomware, destructive malware, and cloud control-plane loss, chaos and failure injection for sec… |
| 78 | `cybersecurity` | cybersecurity | Guides enterprise cybersecurity across security architecture, control design, vulnerability and threat management, incident response, identity security, and GRC alignment (SOC 2, ISO 27001, NIST CSF). Use when defining security strategy, assessing risk, designing defense-in-depth… |
| 79 | `d3fend-deceive` | d3fend-deceive | Guides cybersecurity deception operations using MITRE D3FEND—honeynets, decoy objects, decoy personas, and decoy credentials. Covers honeypot deployment, decoy file planting, credential baiting, and deception environment design. Use when deploying honeypots, planting decoy data, … |
| 80 | `d3fend-detect` | d3fend-detect | Guides cybersecurity detection engineering using MITRE D3FEND—file analysis, identifier reputation, network traffic analysis, physical access monitoring, and platform monitoring. Covers dynamic/emulated analysis, traffic signature detection, behavior analytics, and integrity moni… |
| 81 | `d3fend-evict` | d3fend-evict | Guides cybersecurity eviction and incident response using MITRE D3FEND—credential revocation, account locking, process termination, file removal, and system recovery. Covers containment actions during incidents: killing malicious processes, revoking compromised credentials, remov… |
| 82 | `d3fend-harden` | d3fend-harden | Guides cybersecurity hardening controls using MITRE D3FEND—authentication, application hardening, credential management, message integrity, platform security, and source code defenses. Covers MFA, certificate pinning, control flow integrity, encryption, input validation, and secu… |
| 83 | `d3fend-isolate` | d3fend-isolate | Guides cybersecurity isolation controls using MITRE D3FEND—access mediation, content filtering, execution isolation, and network segmentation. Covers access policies, permissions, content validation, process isolation, allowlisting, and traffic filtering. Use when segmenting netw… |
| 84 | `d3fend-model` | d3fend-model | Guides cybersecurity asset modeling, inventory, and vulnerability assessment using MITRE D3FEND. Covers asset inventory (hardware, software, network, data, containers), network mapping, vulnerability enumeration, dependency mapping, and operational risk assessment. Use when build… |
| 85 | `d3fend-restore` | d3fend-restore | Guides cybersecurity restoration using MITRE D3FEND—recovering access, objects, configurations, and systems after incidents. Covers credential reissuance, account unlocking, file restoration, database recovery, configuration rebuild, and software reinstallation. Use after inciden… |
| 86 | `defensive-security-analyst` | defensive-security-analyst | Guides defensive security analysis—alert triage, log and SIEM investigation, threat hunting, detection engineering basics, MITRE ATT&CK mapping, incident scoping, containment recommendations, and DFIR evidence handling for SOC and blue-team analysts. Use when investigating securi… |
| 87 | `devops` | devops | Guides DevOps—CI/CD pipelines, GitOps, release management, container delivery, observability, and SRE practices for build/deploy systems. Use when building or fixing pipelines, implementing GitOps, tuning alerts and SLOs, or managing on-call/incidents for delivery infrastructure—… |
| 88 | `devsecops` | devsecops | Guides DevSecOps practices that embed security into software delivery—shift-left scanning, CI/CD security gates, supply-chain integrity, cloud/container runtime controls, threat modeling, and vulnerability management with audit evidence. Use when designing or hardening delivery p… |
| 89 | `digital-forensics-analyst` | digital-forensics-analyst | Guides digital forensics for security incidents—evidence acquisition and chain of custody, disk/memory/mobile/cloud artifact analysis, log and network forensics, timeline correlation, malware artifact triage, and investigation reports for legal/IR and expert-witness preparation o… |
| 90 | `enterprise-cloud-architect` | enterprise-cloud-architect | Guides enterprise-scale cloud architecture—multi-BU landing zones and federation, cloud Center of Excellence governance, enterprise agreement and commit strategy, org-wide FinOps and chargeback, regulated-workload patterns (residency, segmentation), hybrid integration with identi… |
| 91 | `enterprise-security-architect` | enterprise-security-architect | Guides enterprise-wide security architecture—reference architectures and domains (identity, data, application, network, endpoint), zero-trust and segmentation, framework mapping (NIST CSF, ISO 27001, CIS), EA and risk alignment, architecture executive briefings, and BU/acquisitio… |
| 92 | `finops-analyst` | finops-analyst | Guides FinOps analysis on AWS, GCP, and Azure—cost visibility and allocation, tagging and showback/chargeback models, rightsizing and waste removal, RI/Savings Plan/CUD recommendations, budgets and forecasts, anomaly detection, unit economics (cost per service/customer), and FinO… |
| 93 | `hardware-in-the-loop-security-tester` | hardware-in-the-loop-security-tester | Guides security assessment of embedded and cyber-physical systems on hardware-in-the-loop (HIL) test benches—bench setup, ECU/ECM or PLC targets, bus interfaces (CAN/CAN-FD, LIN, automotive Ethernet, Modbus at high level), fault injection and stimulus design, simulated plant/envi… |
| 94 | `iam-specialist` | iam-specialist | Guides identity and access management—workforce and machine identity lifecycle, RBAC/ABAC/PBAC entitlement design, access reviews and recertification, SSO/SAML/OIDC federation, privileged access (PAM/JIT), cloud IAM least privilege (AWS/GCP/Azure concepts), service accounts and s… |
| 95 | `incident-management-engineer` | incident-management-engineer | Guides incident management engineering—severity models, escalation policies, on-call design, paging and comms tooling (PagerDuty/Opsgenie/Slack), incident lifecycle workflows, status pages, blameless postmortems, and reliability metrics (MTTD, MTTR, incident rate). Use when desig… |
| 96 | `incident-responder` | incident-responder | Guides CSIRT-style security incident response—declaring incidents, scoping and severity, timeline reconstruction, evidence preservation, containment/eradication/recovery coordination, stakeholder communication templates, post-incident review, lessons learned, and regulatory notif… |
| 97 | `information-security-engineer` | information-security-engineer | Guides information security engineering—implementing and operating security controls, identity and access systems, encryption and secrets management, security tool integrations (SIEM, EDR, SOAR), cloud guardrails, hardening baselines, and remediation engineering for vulnerabiliti… |
| 98 | `information-systems-security-officer-classified-specialist` | information-systems-security-officer-classified-specialist | Guides Information Systems Security Officer (ISSO) work for classified systems and enclaves—system security plan (SSP), control status, continuous monitoring, POA&M, assessor coordination, authorization packages, change impact, vulnerability interfaces, incident reporting to ISSM… |
| 99 | `infrastructure-engineer` | infrastructure-engineer | Design and implement cloud infrastructure. Cover cloud architecture, IaC (Terraform, Pulumi), CI/CD pipelines, container orchestration (Kubernetes), networking, observability, and security hardening. Triggers on "design cloud infrastructure", "set up Terraform", "configure Kubern… |
| 100 | `iot-network-edge-engineer` | iot-network-edge-engineer | This skill should be used when the user asks about IoT network design, edge engineer work, MQTT broker and topic design, LoRaWAN, LPWAN, IoT gateway, device provisioning, IoT edge, CoAP, Azure IoT Edge, AWS IoT Core, device shadow, OTA updates, Zigbee, protocol bridge, IoT fleet,… |
| 101 | `network-backbone-architect` | Network Backbone Architect | Design carrier- and enterprise-scale backbone networks—core/distribution/edge topology, OSPF, IS-IS, BGP and route policy, WAN/MPLS/SD-WAN, DCI, peering, transit, IX, anycast, ECMP, BFD, FRR, addressing, backbone QoS, capacity, maintenance domains, and observability (NetFlow, SNM… |
| 102 | `network-pentester` | network-pentester | Guides authorized network and infrastructure penetration testing—scoping and rules of engagement, external and internal network assessments, host and service enumeration, vulnerability validation on network services, Active Directory attack paths within scope, lateral movement do… |
| 103 | `offensive-security-analyst` | offensive-security-analyst | Guides authorized offensive security work—engagement scoping and rules of engagement, reconnaissance, vulnerability validation, exploitation proof-of-concept, attack-path chaining, MITRE ATT&CK mapping, and remediation-focused reporting for pentests and red-team exercises. Use wh… |
| 104 | `penetration-tester` | penetration-tester | Guides authorized penetration testing—scoping and rules of engagement, reconnaissance, vulnerability identification, exploitation within scope, post-exploitation documentation, evidence and remediation reporting, and retest validation. Emphasizes written authorization, RoE bounda… |
| 105 | `performance-engineer` | performance-engineer | Guides performance engineering—profiling (CPU, memory, I/O), distributed tracing, latency and throughput analysis, load/soak/stress testing, capacity models, performance budgets, database query tuning, and regression detection in CI. Use when investigating slow endpoints, p99 reg… |
| 106 | `platform-engineer` | platform-engineer | Guides platform engineering—internal developer platforms (IDP), golden paths, self-service abstractions, developer portals, paved-road templates, multi-tenant Kubernetes platforms, and platform-as-product practices (roadmap, adoption, platform SLOs). Use when designing or operati… |
| 107 | `product-infrastructure-security-engineer` | product-infrastructure-security-engineer | Guides product infrastructure security—securing the runtime, data plane, and control plane that ships with the product: multi-tenant isolation, service-to-service auth, customer data boundaries, secure defaults in APIs and workers, abuse-resistant rate limits, product-scoped secr… |
| 108 | `red-team-specialist` | red-team-specialist | Guides authorized enterprise adversary simulation and red team operations—campaign planning, threat-informed objectives, MITRE ATT&CK–framed TTP selection, OPSEC and scope, purple-team coordination, detection validation narratives, executive reporting, and blue-team lessons learn… |
| 109 | `reverse-engineer` | reverse-engineer | Guides authorized reverse engineering—static and dynamic binary analysis, disassembly and decompilation workflows, protocol and file-format reversing, defensive malware analysis (behavior, IOCs, YARA ideas), firmware RE, patch diffing, and vulnerability research documentation. Em… |
| 110 | `scada-ics-cyber-security-specialist` | scada-ics-cyber-security-specialist | Guides OT/ICS and SCADA cyber security—Purdue zones, IEC 62443 and NIST SP 800-82 (practitioner), OT asset inventory (PLCs, RTUs, HMIs, historians), secure remote access, OT patch/vuln management, ICS protocol monitoring (Modbus, DNP3, OPC, BACnet high level), safety-first IR, OT… |
| 111 | `sd-wan-engineer` | SD-WAN (Software-Defined WAN) Engineer | Design, deploy, and operate SD-WAN—overlay WAN (hub-spoke, mesh, regional hubs), underlay overlay (MPLS, broadband, LTE/5G), path selection, application-aware routing, SASE, zero trust WAN, branch connectivity, orchestration templates, NGFW/SWG/ZTNA insertion, HA, and brownfield … |
| 112 | `security-risk-analyst` | security-risk-analyst | Guides information security risk analysis—risk identification and scoring, risk registers, threat/vulnerability/control mapping, treatment recommendations (accept/mitigate/transfer/avoid), third-party and supply-chain risk framing, business impact analysis, KRIs, and risk committ… |
| 113 | `site-reliability-engineer` | site-reliability-engineer | Guides Site Reliability Engineering—SLI/SLO and error budgets, reliability dashboards and burn-rate alerting, production readiness reviews, capacity planning for availability, toil reduction, dependency and failure-mode analysis, release reliability (canaries, rollback criteria),… |
| 114 | `sla-slo-engineer` | sla-slo-engineer | Guides SLA and SLO engineering—SLI selection and measurement specs, SLO targets and error budgets, multi-window burn-rate alerting policies, customer-facing SLA vs internal SLO alignment, criticality tiering, reporting and review cadences, and capacity implications of service lev… |
| 115 | `soc-analyst` | soc-analyst | Guides SOC operations—alert triage, SIEM/EDR investigation, enrichment, playbook execution, false-positive closure, escalation decisions, and detection tuning feedback. Use when working SOC queues, investigating suspicious alerts, correlating events, documenting analyst notes, or… |
| 116 | `software-assurance-formal-methods-specialist` | software-assurance-formal-methods-specialist | Software assurance and formal methods engineering—assurance cases (GSN/CAE), safety and security claims with evidence, requirements-to-verification traceability, hazard-analysis interfaces (FMEA, FTA) at evidence level, and high-level standards context (DO-178C, DO-333, IEC 61508… |
| 117 | `threat-hunter` | threat-hunter | Guides proactive threat hunting for advanced SOC—hypothesis-driven hunt campaigns, advanced SIEM/query workflows, baseline and anomaly analysis, MITRE ATT&CK–aligned techniques, threat intel fusion, detection engineering feedback, and hunt reporting with IR handoff. Use for threa… |
| 118 | `vendor-cyber-risk-analyst` | vendor-cyber-risk-analyst | Guides third-party and vendor cyber risk—TPRM intake and tiering, security questionnaire analysis and scoring, evidence and attestation review (SOC 2, ISO 27001, pen test summaries), continuous vendor monitoring, concentration and fourth-party risk, remediation tracking, and exec… |
| 119 | `vp-of-cloud` | vp-of-cloud | Guides VP-level cloud program leadership—multi-year cloud strategy and migration/modernization portfolio, landing zone and CCoE operating model at org scale, hyperscaler enterprise agreement and commit governance, hybrid/multi-cloud posture, cloud center of excellence and talent,… |
| 120 | `vp-of-infrastructure` | vp-of-infrastructure | Guides VP-level infrastructure leadership—org strategy and operating model, multi-year cloud, data center, and platform portfolio, capex and opex governance, org-wide reliability and security posture, hyperscaler/colo/vendor and enterprise agreement strategy, build-vs-buy and mul… |
| 121 | `web-pentester` | web-pentester | Guides authorized web application and API security testing—scoping and rules of engagement, OWASP-oriented testing (injection, auth/session, access control, SSRF, XSS, CSRF, business logic), REST and GraphQL API security, Burp/ZAP-style manual methodology without requiring commer… |
| 122 | `wireless-wifi-mobility-specialist` | Wireless (Wi-Fi) Mobility Specialist | Enterprise WLAN for mobile users—RF/site surveys, AP placement, 802.11 (Wi-Fi 5/6/6E/7), channel/power planning, SSID/VLAN segmentation, WPA3/802.1X/RADIUS, guest/captive portal, roaming (802.11k/r/v, band steering), high-density and mesh/outdoor, LAN/SD-WAN edge integration, tro… |
| 123 | `yara-rule-authoring` | YARA Rule Authoring | Guides authoring, review, optimization, and false-positive debugging of YARA-X detection rules for malware identification across PE, script, npm, Office, Chrome extensions (crx module), and Android DEX (dex module). Covers string and atom quality, condition short-circuiting, lega… |

---

## Layer 1: Software Engineering (24 skills)

| # | Folder | Display name | Summary |
|---|--------|--------------|---------|
| 124 | `control-software-developer` | control-software-developer | Guides industrial control application software—real-time loops and application layers above field devices; DCS/PLC/RTU integration; OPC UA, Modbus, DNP3, MQTT/AMQP; historian and alarm/event pipelines; HMI/SCADA server-side logic (not graphics-only); soft-PLC/PC control; determin… |
| 125 | `embedded-real-time-software-engineer` | embedded-real-time-software-engineer | Guides embedded real-time firmware—MCU tradeoffs, bare-metal vs RTOS (FreeRTOS/Zephyr patterns), task priorities/deadlines/jitter, ISR deferred work, stack/heap policy, WCET/timing analysis, concurrency and priority inversion, drivers/HAL, JTAG/SWD/trace, power modes, MISRA C awa… |
| 126 | `enterprise-integration-api-developer` | enterprise-integration-api-developer | Guides enterprise integration platforms and APIs—REST/GraphQL versioning, OpenAPI/AsyncAPI, event-driven integration (pub/sub, outbox, idempotency, sagas), canonical models and anti-corruption layers, iPaaS/ESB orchestration vs choreography, API gateways, OAuth2/OIDC, mTLS, B2B p… |
| 127 | `event-driven-architecture` | event-driven-architecture | Guides event-driven systems—pub/sub, point-to-point, event sourcing, CQRS, schema versioning (Avro/JSON Schema), ordering, partitioning, delivery guarantees, idempotency, exactly-once tradeoffs, transactional outbox/inbox, choreography vs orchestration, sagas, dead-letter queues,… |
| 128 | `extreme-lifecycle` | extreme-lifecycle | Guides end-to-end lifecycle governance for mission-critical, high-assurance, or zero-failure- tolerance systems—concept through retirement: phases, gates, evidence, traceability, obsolescence, tech refresh, configuration baselines, NDA-safe regulated/classified patterns, assuranc… |
| 129 | `fullstack-software-engineer` | fullstack-software-engineer | Guides full-stack software engineering—end-to-end product features across web frontends (React/Next.js or similar), backend APIs (Node/TypeScript or Python), databases, auth, testing, and production debugging for maintainable application code. Use when building or fixing user-fac… |
| 130 | `high-concurrency-scalability` | high-concurrency-scalability | Design and optimize systems for high concurrency, throughput, scalability, and elastic scale—concurrency models (threads, async/await, actors), lock-free patterns, connection pooling, caching stampede mitigation, horizontal scaling, load balancing, backpressure, queueing, rate li… |
| 131 | `matrix-environment` | matrix-environment | Guides organizational operating models for cross-functional security and technology teams—matrix vs hierarchical structures, RACI and interaction models, chapter/pod/guild patterns, platform vs product vs security alignment, interfaces between SOC/IR/AppSec/GRC/Engineering, scali… |
| 132 | `microservice-researcher` | microservice-researcher | Guides research and analysis for microservices architecture decisions—domain decomposition, bounded contexts, service boundary options and trade-offs, sync vs async integration patterns, data ownership and consistency (eventual consistency, sagas at research level), API and contr… |
| 133 | `microservices-analyst` | microservices-analyst | Guides analysis of existing microservice estates—service and API inventory, dependency and coupling maps (sync chains, shared-database smells), observability and SLO coverage gaps, deployment and version skew, API contract drift and breaking consumers, operational toil indicators… |
| 134 | `microservices-developer` | microservices-developer | Guides microservice design and delivery—bounded contexts, service boundaries, REST/gRPC/event APIs, sync vs async tradeoffs, resilience (timeouts, retries, circuit breakers, bulkheads), per-service data ownership, saga and outbox patterns, twelve-factor containers, observability … |
| 135 | `mission-critical` | mission-critical | Guides mission-critical system framing—tiering (mission-critical vs business-critical vs important), availability/integrity/continuity objectives, dependency and blast-radius mapping, architecture patterns (active-active, geo-redundancy, deterministic behavior), change/release go… |
| 136 | `sdk-engineer` | sdk-engineer | Designs, builds, and maintains client SDKs for HTTP/REST, GraphQL, gRPC, and RPC-style APIs— OpenAPI-first contract alignment, resource modeling, authentication (API keys, OAuth, signing), retries/timeouts/idempotency, pagination and streaming, error taxonomy, versioning and depr… |
| 137 | `senior-frontend-software-engineer` | senior-frontend-software-engineer | Guides senior front-end software engineering—TypeScript/React/Next.js architecture, component design, client and server rendering, state and data fetching, styling and design systems, accessibility (WCAG), performance (Core Web Vitals), testing, and senior-level UI code review. U… |
| 138 | `senior-fullstack-developer` | senior-fullstack-developer | Guides senior full-stack delivery across TypeScript/React/Next.js frontends, Node or Python APIs, relational databases, authentication, testing, performance, and pragmatic system design for product features. Use when implementing end-to-end features, designing REST/GraphQL contra… |
| 139 | `senior-software-engineer` | senior-software-engineer | Guides senior software engineering across languages and stacks—system and service design, RFCs, code review, refactoring, reliability patterns, testing strategy, performance analysis, technical decomposition, and engineering leadership on delivery teams. Use when designing servic… |
| 140 | `senior-system-architecture` | senior-system-architecture | Guides senior system and solution architecture—cross-service boundaries, integration patterns, non-functional requirements (scale, reliability, security, cost), ADRs, C4-style modeling, architecture review, build-vs-buy, and phased migration (strangler, dual-write). Use when desi… |
| 141 | `sensor-fusion-engineer` | sensor-fusion-engineer | Guides multi-sensor perception fusion for autonomous and robotic systems—sensor models and noise; extrinsic/intrinsic calibration; time synchronization; coordinate frames and transforms; data association and gating; Kalman-family filters (EKF/UKF) and factor graphs at high level;… |
| 142 | `simulation-software-engineer` | simulation-software-engineer | Simulation systems: discrete-event and continuous-time physics/kinematics, sensor and environment models, digital twins, scenario runners, SIL/HIL interfaces, real-time and faster-than-real-time execution, deterministic replay, calibration/validation, Monte Carlo sweeps, distribu… |
| 143 | `solutions-architect` | solutions-architect | Guides customer-facing and internal technical solution design—discovery and requirements, integration and reference architecture, security/compliance fit, sizing and cost framing, RFP/RFI responses, PoC scoping, build-vs-buy, and handoff to delivery. Use when scoping a customer o… |
| 144 | `support-engineer` | support-engineer | Guides technical support engineering—customer ticket investigation, reproduction, log and API analysis, root-cause isolation, workaround communication, engineering escalation with evidence, and knowledge-base fixes for product bugs and integration issues. Use when debugging a cus… |
| 145 | `ui-software-engineer` | ui-software-engineer | Guides UI software engineering—implementing screens and components from design specs, design tokens, responsive layout, interaction states, forms, and API-boundary loading/error UI in React/Next.js or similar stacks. Covers component library usage, basic WCAG implementation, and … |
| 146 | `ux-software-engineer` | ux-software-engineer | Guides UX software engineering—translating user flows into interaction specs and coded prototypes, heuristic UX reviews, information architecture in product, micro-interactions, usability fixes in the UI layer, and design-engineering handoff. Bridges discovery output and producti… |
| 147 | `web-application-developer` | web-application-developer | Guides web application development—browser-based products spanning UI, HTTP APIs, sessions and cookies, routing (SPA and SSR), forms, file uploads, and web-specific security (CSRF, CORS, CSP, XSS prevention) on stacks such as React/Next.js, Vue, or similar with Node/Python/Ruby b… |

---

## Layer 0: Business, Actuarial & Operations (45 skills)

| # | Folder | Display name | Summary |
|---|--------|--------------|---------|
| 148 | `actuarial-analyst` | Actuarial Analyst | Guides hands-on actuarial analyst work for insurance, reinsurance, and pension—reserving and loss development (IBNR, triangles, chain-ladder diagnostics), pricing and rate indication support (experience, trend, credibility, basic GLM at spec level), data validation and model I/O … |
| 149 | `actuarial-consulting` | Actuarial Consulting | Guides actuarial consulting engagements—client scoping and SOW design, stakeholder communication (CFO, risk, boards, regulators at overview level), due diligence and M&A actuarial support, reserving/pricing/capital review programs, model validation and opinion support, regulatory… |
| 150 | `actuary` | Actuary | Guides actuarial work for insurance and reinsurance—pricing and rate adequacy, reserving and IBNR, loss development and triangles, mortality/morbidity and lapse assumptions, experience studies and credibility, capital and risk metrics at overview level, product design tradeoffs (… |
| 151 | `advanced-long-term-actuarial-mathematics` | Advanced Long-Term Actuarial Mathematics | Guides advanced long-term actuarial mathematics (SOA ALTAM)—survival models, life insurance and annuity APVs, premiums and reserves (equivalence principle, Thiele), multiple decrement and Markov states, yield-curve discounting, mortality improvement, longevity risk, profit testin… |
| 152 | `advanced-short-term-actuarial-mathematics` | Advanced Short-Term Actuarial Mathematics | Guides advanced short-term actuarial mathematics aligned with SOA ASTAM and P&C/health-adjacent modeling—severity and frequency distributions, aggregate and compound loss models, Bühlmann and Bühlmann-Straub credibility, ratemaking and experience rating, short-term reserving at t… |
| 153 | `aml-cft` | AML/CFT | This skill should be used when the user asks about AML/CFT, counter-terrorist financing, CFT, terrorist financing, proliferation financing, PF, targeted financial sanctions, asset freeze, TF typology, charitable NPO due diligence, MVTS, FATF Recommendation 6, or STR terrorist fin… |
| 154 | `aml-compliance` | AML/Compliance | This skill should be used when the user asks about AML compliance, anti-money laundering, KYC, CDD, EDD, PEP screening, sanctions screening, transaction monitoring, SAR, STR, suspicious activity, FATF, BSA, financial crime compliance, travel rule, AML risk assessment, or MLRO. Gu… |
| 155 | `anti-false-positive-decision-making` | Anti-False-Positive Decision Making | Guides decision frameworks when false positives are costly—thresholds, evidence bars, and escalation so actions are not taken on weak signals. Covers FP/FN trade-offs, base rates, corroboration, tiered response (monitor vs act), security/compliance alert tuning, screening workflo… |
| 156 | `appointed-chief-actuary` | Appointed Chief Actuary | Guides FSA/FSAI fellow-level appointed and chief actuary work—head of actuarial function, statutory reporting accountability (Solvency II, RBC, local appointed-actuary frameworks), actuarial opinion and AA report structure, board and audit committee communication, enterprise actu… |
| 157 | `asset-liability-management` | asset-liability-management | Guides asset-liability management (ALM)—matching asset and liability cash flows and risks; interest rate risk (duration, convexity, key rate duration); surplus and risk appetite; liability-driven investment (LDI), immunization, and hedging (rates, inflation, FX); insurer, pension… |
| 158 | `associate-actuary` | Associate Actuary | Guides associate-level actuarial practice for ASA (SOA, US), ASAI (IAI, India), and analogous associate credentials—role boundaries vs analyst and fellow/chief actuary; credential pathways (high-level); professional standards and confidentiality; signing limits and review chains;… |
| 159 | `assumption-setting` | Assumption Setting | Guides defining, documenting, and governing actuarial and risk assumptions for insurance and related models—mortality, morbidity, lapse, discount rates, inflation, loss development, expense, cat, credit; categories and sources; selection methodology and judgment; sensitivity and … |
| 160 | `auditor` | Auditor | This skill should be used when the user asks to plan or execute internal audit, IT audit, risk-based audit planning, control testing, audit evidence, workpaper documentation, SOC 2 audit support, SOX ITGC testing, walkthroughs, operating effectiveness, deficiency or finding write… |
| 161 | `business-consultant` | business-consultant | Guides management consulting-style work—engagement framing, hypothesis-driven problem structuring, issue trees, business cases, operating model and capability design, strategic options analysis, workshop facilitation, and executive recommendations (not legal advice). Use when dia… |
| 162 | `business-model-researcher` | business-model-researcher | Guides business model research—Business Model Canvas and Lean Canvas, value proposition and customer segments, revenue and pricing models, unit economics (CAC, LTV, payback), market sizing (TAM/SAM/SOM), competitive business-model benchmarking, and evidence-backed synthesis for s… |
| 163 | `commercial-counsel` | commercial-counsel | Guides commercial contract review and negotiation support for B2B agreements—MSAs, SaaS/order forms, vendor and customer contracts, DPAs, SLAs, limitation of liability, indemnity, IP, payment terms, and redline/issue logs with business impact notes. Use when reviewing or negotiat… |
| 164 | `compute-accounting-manager` | compute-accounting-manager | Guides accounting for compute infrastructure—cloud COGS and prepaid commitments, capex vs OpEx for servers/GPUs, depreciation and asset disposal, colo and hardware accruals, GL mapping from usage and invoices (CUR, billing exports), chargeback/showback to products, and month-end … |
| 165 | `corporate-counsel` | corporate-counsel | Guides corporate legal support—entity structure, board and stockholder governance, corporate resolutions and minutes, equity and cap table mechanics, corporate policies, intercompany arrangements, and corporate closing checklists for financings or M&A. Use when drafting board mat… |
| 166 | `customer-ops-specialist` | customer-ops-specialist | Manage customer operations across success, support, and revenue operations. Cover customer onboarding, health scoring, renewal management, ticket triage, SLA management, knowledge base development, billing operations, dunning, refunds, and customer metrics. Triggers on "customer … |
| 167 | `deal-operations-administrator` | deal-operations-administrator | Guides deal operations administration—quote-to-cash coordination, deal desk intake and routing, CRM opportunity hygiene, order form and SOW assembly, approval workflows, signature tracking, and handoffs to legal, finance, and provisioning after customer signature. Use when proces… |
| 168 | `developer-education-lead` | developer-education-lead | Guides developer education leadership—audience and skills-gap analysis, learning paths and curriculum design, workshops and cohort programs, hands-on labs, certification or badging, instructor enablement, feedback loops, and success metrics (completion, confidence, time-to-first-… |
| 169 | `financial-intelligence-unit` | FIU (Financial Intelligence Unit) | This skill should be used when the user asks about FIU, financial intelligence unit, AML FIU, case analysis, alert triage, suspicious activity analysis, escalate to MLRO, FIU reporting, transaction monitoring investigation, or FIU workflow. Operates the Financial Intelligence Uni… |
| 170 | `ifrs` | IFRS | This skill should be used when the user asks about IFRS, International Financial Reporting Standards, IFRS 15 revenue, IFRS 16 leases, IFRS 9 financial instruments, IFRS 10 consolidation, IAS 36 impairment, IFRS 13 fair value, IFRS disclosure notes, IFRS recognition, first-time a… |
| 171 | `life-health-insurance` | Life and Health Insurance | Guides life and health insurance—life (term, whole, universal, variable overview), health (individual, group, Medicare/Medicaid overview), disability and LTC, underwriting, policy provisions, claims and benefits administration, reinsurance, distribution, and metrics (lapse, persi… |
| 172 | `pension-retirement-funds` | pension-retirement-funds | Guides pension and retirement fund work—DB vs DC structures, funding policy, liability measurement (PV of benefits, discount rates, mortality), ALM overview, plan design, public and multi-employer pensions, risk transfer (buyouts, annuities, de-risking), US regulatory overview (E… |
| 173 | `people-operations-specialist` | people-operations-specialist | Guides people operations (HR ops)—employee lifecycle administration, HRIS workflows, onboarding and offboarding checklists, handbook and policy rollout, benefits and payroll coordination, performance review cycles, leave and PTO process, and people data hygiene. Use when running … |
| 174 | `pre-actuarial-foundations` | Pre-Actuarial Foundations | Guides pre-credential actuarial foundations—probability and statistics for actuaries, financial math (interest, annuities, loans, duration intro), insurance risk concepts, spreadsheet/R/Python literacy, SOA/CAS/IAI path overview, and quantitative study discipline. Use for pre-act… |
| 175 | `predictive-logistics-developer` | predictive-logistics-developer | Build and operate predictive models for logistics networks—demand forecasting at SKU/location/lane granularity; inventory positioning and safety stock optimization interfaces; ETA and lead-time prediction; capacity and congestion signals; route and network flow forecasting at mod… |
| 176 | `product-designer` | product-designer | Guides product design—problem framing, discovery synthesis, user journeys and flows, wireframes, interaction specs, usability evaluation, and engineering handoff for digital products (web and mobile). Use when designing a new feature UX, mapping flows, creating wireframe or spec … |
| 177 | `product-management-human-data-platform` | product-management-human-data-platform | Guides product management for human data platforms—annotation and labeling products, workforce workflows, task design, quality systems (gold sets, adjudication, inter-annotator agreement), customer ML-team project delivery, contributor experience, and privacy-safe handling of hum… |
| 178 | `product-management-monetization` | product-management-monetization | Guides product management for monetization—pricing and packaging, plan tiers, usage meters, paywalls and upgrade paths, free-to-paid conversion, expansion revenue features, monetization experiments, and PRDs for billing-adjacent product surfaces. Covers success metrics (conversio… |
| 179 | `product-support-specialist` | product-support-specialist | Guides product support specialist work—customer tickets about how the product works, configuration, permissions, workflows, and expected behavior; empathetic replies, triage and routing, macro and KB guidance, feature-request capture, and escalation to technical support or produc… |
| 180 | `property-casualty-insurance` | property-casualty-insurance | Guides property and casualty (P&C) insurance—commercial and personal lines, major LOBs (property, GL, workers comp, commercial auto, umbrella, specialty), underwriting and risk selection, policy triggers (occurrence vs claims-made), limits and exclusions, claims (FNOL, reserving,… |
| 181 | `robotics-automation-integration-engineer` | robotics-automation-integration-engineer | Integrates and commissions robotic and factory automation—arms, cobots, AMRs/AGVs, gantries; PLC/PC interfaces; safety (light curtains, e-stops, STO); Profinet, EtherNet/IP, EtherCAT, Modbus; robot OEM APIs and teach-pendant workflows; vision-guided pick, conveyors, sortation, pa… |
| 182 | `senior-revenue-accountant` | senior-revenue-accountant | Apply ASC 606/IFRS 15 to revenue recognition and contract analysis. Cover performance obligations, deferred revenue, commission accounting, revenue metrics (ARR, NRR, GRR), and audit preparation. Triggers on "revenue recognition", "ASC 606 compliance", "contract analysis", "defer… |
| 183 | `storytelling` | Storytelling | Guides organizational and business storytelling—narrative structure (setup, tension, resolution), audience-tailored stories for executives, customers, boards, and teams, honest data and metrics framing, product and strategy narratives, incident and postmortem storytelling, and ac… |
| 184 | `str-report` | STR Report | This skill should be used when the user asks to draft or structure STR reports, suspicious transaction reports, SAR, suspicious activity reports, draft STR, STR narrative, file suspicious activity, AML STR, goAML, FinCEN SAR, suspicion narrative, or MLRO report. Guides jurisdicti… |
| 185 | `supply-chain-manager` | supply-chain-manager | Guides supply chain management—sourcing and supplier qualification, procurement and PO governance, demand forecasting and inventory policy, logistics and fulfillment (3PL, Incoterms, lead times), supplier scorecards, cost and TCO analysis, supply risk and continuity, and SCM KPI … |
| 186 | `talent-acquisition` | talent-acquisition | Expert talent acquisition for end-to-end recruiting operations—workforce planning tie-in, requisition intake, job descriptions and leveling, interview process coordination, candidate experience, offer process coordination, ATS/CRM workflow, hiring manager partnership, recruiting … |
| 187 | `talent-sourcer` | talent-sourcer | This skill should be used when the user asks to talent sourcer, source candidates, define a sourcing strategy, run boolean search or X-ray search, conduct LinkedIn sourcing, find passive candidates, build a talent map or talent pool, build a recruiting pipeline, draft recruiting … |
| 188 | `tech-writer-researcher` | tech-writer-researcher | Write and research technical documentation. Cover information architecture, style guides, API documentation, user research, content strategy, and documentation operations. Triggers on "write technical documentation", "create API docs", "developer tutorial", "information architect… |
| 189 | `transaction-manager` | transaction-manager | Guides corporate transaction execution—M&A, divestitures, financings, and JVs: deal timeline, diligence workstreams, data room and Q&A, conditions precedent, closing matrix, signing logistics, funds flow, and post-close handoff to integration. Use when running a live deal, mainta… |
| 190 | `transaction-principal` | transaction-principal | Guides senior corporate transaction leadership—deal thesis, valuation and offer strategy, negotiation priorities, structure (cash/stock/earnout/RWI/locked box), IC and board recommendations, adviser and banker management, go/no-go and walk-away, and oversight of execution through… |
| 191 | `validation-by-educational-experience` | Validation by Educational Experience | Guides Validation by Educational Experience (VEE) for North American actuarial credential paths (SOA, CAS)—how VEE fits preliminary requirements, current topic areas (Economics, Accounting & Finance, Mathematical Statistics; subject to society updates), approved-course criteria, … |
| 192 | `wms-developer` | wms-developer | Guides design, build, customization, and integration of warehouse management systems—receiving, putaway, inventory, allocation, picking (wave/batch/zone), packing, shipping, cycle counts; slotting; lot/serial/expiry; RF/mobile and barcode; WMS–ERP–TMS–OMS integration; EDI/API; WC… |

---

## Layer -1: Physical Infrastructure (6 skills)

| # | Folder | Display name | Summary |
|---|--------|--------------|---------|
| 193 | `data-center-compute-supply-efficiency` | data-center-compute-supply-efficiency | Guides data center compute supply and resource efficiency—capacity and utilization planning, kW-per-useful-compute metrics, stranded power and rack space, hardware refresh and decommission, power-aware placement, consolidation and right-sizing of physical hosts, GPU/CPU supply al… |
| 194 | `data-center-design-execution-lead` | data-center-design-execution-lead | Guides data center design and build execution—site and tier selection, capacity and density planning (kW/rack, floor loading), power and cooling architecture, physical layout and containment, network meet-me and carrier connectivity, standards alignment (TIA-942, Uptime tiers), c… |
| 195 | `data-center-portfolio-planning-execution-lead` | data-center-portfolio-planning-execution-lead | Guides enterprise data center portfolio planning and execution—multi-site capacity roadmaps, investment prioritization (build, expand, refresh, exit, colo vs owned), portfolio RAID and dependency management across DC programs, stage-gate governance, capex/opex alignment, regional… |
| 196 | `director-infrastructure-capex-accounting` | director-infrastructure-capex-accounting | Guides director-level infrastructure capex accounting—capitalization policy and governance, WIP/CIP and project closeout, useful-life and impairment standards, capex forecast vs actual for data center and compute programs, board and audit narratives, SOX over fixed-asset and clou… |
| 197 | `field-services-engineer` | field-services-engineer | Guides field services engineering—on-site and colocation smart-hands work: site readiness, rack-and-stack, power and network cabling, hardware install/replace, labeling, acceptance tests, photo documentation, customer sign-off, and remote handoff to NOC or platform teams. Use whe… |
| 198 | `senior-data-center-capacity-delivery-manager` | senior-data-center-capacity-delivery-manager | Guides delivery of data center capacity increments—MW/kW and rack-ready halls on schedule: capacity delivery plans, critical path (power, cooling, construction, network), vendor and contractor coordination, readiness gates, handoff to operations and compute install, and program R… |

---

## Summary statistics

| Layer | Skills | % of total |
|-------|--------|------------|
| L5: Governance & Orchestration | 15 | 7.6% |
| L4: AI & ML Operations | 22 | 11.1% |
| L3: Data & Analytics | 18 | 9.1% |
| L2: Infrastructure, Cloud & Security | 68 | 34.3% |
| L1: Software Engineering | 24 | 12.1% |
| L0: Business, Actuarial & Operations | 45 | 22.7% |
| L-1: Physical Infrastructure | 6 | 3.0% |
| **Total** | **198** | **100%** |

## skills.sh index

| Field | Value |
|-------|-------|
| Package | `daemon-blockint-tech/Agentic-Enteprises-Skill` |
| Skill count | 198 |
| Cursor install | [skills.sh/agent/cursor](https://www.skills.sh/agent/cursor) |
| Badge | `https://skills.sh/b/daemon-blockint-tech/Agentic-Enteprises-Skill` |

### Folder index (alphabetical)

- `ab-testing-engineer` — A/B Testing Engineer
- `actuarial-analyst` — Actuarial Analyst
- `actuarial-consulting` — Actuarial Consulting
- `actuary` — Actuary
- `advanced-long-term-actuarial-mathematics` — Advanced Long-Term Actuarial Mathematics
- `advanced-persistent-threat` — advanced-persistent-threat
- `advanced-short-term-actuarial-mathematics` — Advanced Short-Term Actuarial Mathematics
- `agentic-ai-developer` — agentic-ai-developer
- `ai-adversarial-robustness-engineer` — ai-adversarial-robustness-engineer
- `ai-context-engineer` — ai-context-engineer
- `ai-engineer` — ai-engineer
- `ai-lead-ops` — ai-lead-ops
- `ai-memory-developer` — ai-memory-developer
- `ai-redteam` — ai-redteam
- `ai-researcher` — ai-researcher
- `ai-risk-governance` — ai-risk-governance
- `ai-skill-manager` — ai-skill-manager
- `ai-token-improvement-plan-engineer` — ai-token-improvement-plan-engineer
- `aml-cft` — AML/CFT
- `aml-compliance` — AML/Compliance
- `analytics-data-engineer` — analytics-data-engineer
- `analytics-data-engineering-manager-product` — analytics-data-engineering-manager-product
- `anti-false-positive-decision-making` — Anti-False-Positive Decision Making
- `applied-ai-architect-commercial-enterprise` — applied-ai-architect-commercial-enterprise
- `appointed-chief-actuary` — Appointed Chief Actuary
- `asset-liability-management` — asset-liability-management
- `associate-actuary` — Associate Actuary
- `assumption-setting` — Assumption Setting
- `auditor` — Auditor
- `bcm-disaster-recovery-specialist` — bcm-disaster-recovery-specialist
- `bi-analyst` — bi-analyst
- `build-validator` — build-validator
- `business-analyst` — business-analyst
- `business-consultant` — business-consultant
- `business-model-researcher` — business-model-researcher
- `certified-information-systems-security-professional` — certified-information-systems-security-professional
- `chief-information-security-officer` — chief-information-security-officer
- `ci-cd-engineer` — CI/CD Engineer
- `cicd-engineer` — cicd-engineer
- `cisco-certified-network-professional` — Cisco Certified Network Professional
- `classified-cyber-security-senior-manager` — classified-cyber-security-senior-manager
- `classified-software-devsecops-engineer` — classified-software-devsecops-engineer
- `cloud-architect` — cloud-architect
- `cloud-compliance-specialist` — cloud-compliance-specialist
- `cloud-economist` — cloud-economist
- `cloud-engineer` — cloud-engineer
- `cloud-security-engineer` — cloud-security-engineer
- `cloud-system-administrator` — cloud-system-administrator
- `cluster-deployment-engineer` — cluster-deployment-engineer
- `code-security` — code-security
- `commercial-counsel` — commercial-counsel
- `communication-lead` — communication-lead
- `community-executive-escalations-program-manager` — community-executive-escalations-program-manager
- `compliance-engineer` — compliance-engineer
- `compliance-specialist` — compliance-specialist
- `compute-accounting-manager` — compute-accounting-manager
- `control-software-developer` — control-software-developer
- `corporate-counsel` — corporate-counsel
- `country-manager` — country-manager
- `cross-department-translation` — Cross-Department Translation
- `cryptographer-specialist` — Cryptographer Specialist
- `cti-analyst` — cti-analyst
- `customer-ops-specialist` — customer-ops-specialist
- `cyber-diligence-governance` — cyber-diligence-governance
- `cyber-resilience-engineer` — cyber-resilience-engineer
- `cybersecurity` — cybersecurity
- `d3fend-deceive` — d3fend-deceive
- `d3fend-detect` — d3fend-detect
- `d3fend-evict` — d3fend-evict
- `d3fend-harden` — d3fend-harden
- `d3fend-isolate` — d3fend-isolate
- `d3fend-model` — d3fend-model
- `d3fend-restore` — d3fend-restore
- `data-architect` — data-architect
- `data-center-compute-supply-efficiency` — data-center-compute-supply-efficiency
- `data-center-design-execution-lead` — data-center-design-execution-lead
- `data-center-portfolio-planning-execution-lead` — data-center-portfolio-planning-execution-lead
- `data-manager` — data-manager
- `data-scientist` — data-scientist
- `data-scrubbing` — Data Scrubbing
- `data-system-ops-lead` — data-system-ops-lead
- `data-visualization` — Data Visualization
- `data-warehouse-engineer` — data-warehouse-engineer
- `deal-operations-administrator` — deal-operations-administrator
- `defensive-security-analyst` — defensive-security-analyst
- `deployment-strategist` — deployment-strategist
- `developer-education-lead` — developer-education-lead
- `devops` — devops
- `devsecops` — devsecops
- `digital-forensics-analyst` — digital-forensics-analyst
- `director-infrastructure-capex-accounting` — director-infrastructure-capex-accounting
- `edi-engineer` — edi-engineer
- `embedded-real-time-software-engineer` — embedded-real-time-software-engineer
- `engineering-manager-agent-prompts-evals` — engineering-manager-agent-prompts-evals
- `engineering-manager-vertical-ai-products` — engineering-manager-vertical-ai-products
- `enterprise-cloud-architect` — enterprise-cloud-architect
- `enterprise-integration-api-developer` — enterprise-integration-api-developer
- `enterprise-security-architect` — enterprise-security-architect
- `enterprise-strategist` — enterprise-strategist
- `event-driven-architecture` — event-driven-architecture
- `extreme-lifecycle` — extreme-lifecycle
- `field-services-engineer` — field-services-engineer
- `financial-intelligence-unit` — FIU (Financial Intelligence Unit)
- `finops-analyst` — finops-analyst
- `fullstack-software-engineer` — fullstack-software-engineer
- `geospatial-telematics-developer` — geospatial-telematics-developer
- `hardware-in-the-loop-security-tester` — hardware-in-the-loop-security-tester
- `high-concurrency-scalability` — high-concurrency-scalability
- `iam-specialist` — iam-specialist
- `ifrs` — IFRS
- `incident-management-engineer` — incident-management-engineer
- `incident-responder` — incident-responder
- `information-security-engineer` — information-security-engineer
- `information-systems-security-officer-classified-specialist` — information-systems-security-officer-classified-specialist
- `infrastructure-engineer` — infrastructure-engineer
- `iot-network-edge-engineer` — iot-network-edge-engineer
- `life-health-insurance` — Life and Health Insurance
- `markup-detection` — Markup Detection
- `matrix-environment` — matrix-environment
- `microservice-researcher` — microservice-researcher
- `microservices-analyst` — microservices-analyst
- `microservices-developer` — microservices-developer
- `mission-critical` — mission-critical
- `ml-infrastructure-engineer-safeguards` — ml-infrastructure-engineer-safeguards
- `ml-research-engineer-safeguards` — ml-research-engineer-safeguards
- `ml-systems-engineer-rl-engineering` — ml-systems-engineer-rl-engineering
- `multi-agent-system-engineer` — multi-agent-system-engineer
- `network-backbone-architect` — Network Backbone Architect
- `network-pentester` — network-pentester
- `offensive-security-analyst` — offensive-security-analyst
- `ontology-engineer` — ontology-engineer
- `operations-research-algorithm-developer` — operations-research-algorithm-developer
- `penetration-tester` — penetration-tester
- `pension-retirement-funds` — pension-retirement-funds
- `people-operations-specialist` — people-operations-specialist
- `performance-engineer` — performance-engineer
- `platform-engineer` — platform-engineer
- `pre-actuarial-foundations` — Pre-Actuarial Foundations
- `predictive-analytics` — Predictive Analytics
- `predictive-logistics-developer` — predictive-logistics-developer
- `privacy-research-engineer-safeguards` — privacy-research-engineer-safeguards
- `product-designer` — product-designer
- `product-infrastructure-security-engineer` — product-infrastructure-security-engineer
- `product-management-human-data-platform` — product-management-human-data-platform
- `product-management-monetization` — product-management-monetization
- `product-support-specialist` — product-support-specialist
- `prompt-engineer` — prompt-engineer
- `prompt-engineer-agent-prompts-evals` — prompt-engineer-agent-prompts-evals
- `property-casualty-insurance` — property-casualty-insurance
- `quantitative-researcher` — Quantitative Researcher
- `red-team-specialist` — red-team-specialist
- `research-engineer-scientist-tokens` — research-engineer-scientist-tokens
- `reverse-engineer` — reverse-engineer
- `robotics-automation-integration-engineer` — robotics-automation-integration-engineer
- `scada-ics-cyber-security-specialist` — scada-ics-cyber-security-specialist
- `sd-wan-engineer` — SD-WAN (Software-Defined WAN) Engineer
- `sdk-engineer` — sdk-engineer
- `security-risk-analyst` — security-risk-analyst
- `senior-data-center-capacity-delivery-manager` — senior-data-center-capacity-delivery-manager
- `senior-frontend-software-engineer` — senior-frontend-software-engineer
- `senior-fullstack-developer` — senior-fullstack-developer
- `senior-revenue-accountant` — senior-revenue-accountant
- `senior-software-engineer` — senior-software-engineer
- `senior-system-architecture` — senior-system-architecture
- `sensor-fusion-engineer` — sensor-fusion-engineer
- `sentiment-analysis-engineer` — Sentiment Analysis Engineer
- `sentiment-forecasting-engineer` — Sentiment Forecasting Engineer
- `simulation-software-engineer` — simulation-software-engineer
- `site-reliability-engineer` — site-reliability-engineer
- `sla-slo-engineer` — sla-slo-engineer
- `soc-analyst` — soc-analyst
- `software-assurance-formal-methods-specialist` — software-assurance-formal-methods-specialist
- `solutions-architect` — solutions-architect
- `storytelling` — Storytelling
- `str-report` — STR Report
- `supply-chain-manager` — supply-chain-manager
- `support-engineer` — support-engineer
- `tactical-ai-autonomy-developer` — tactical-ai-autonomy-developer
- `talent-acquisition` — talent-acquisition
- `talent-sourcer` — talent-sourcer
- `tech-writer-researcher` — tech-writer-researcher
- `technical-program-manager` — technical-program-manager
- `technical-program-manager-security-cvd` — technical-program-manager-security-cvd
- `threat-hunter` — threat-hunter
- `transaction-manager` — transaction-manager
- `transaction-principal` — transaction-principal
- `ui-software-engineer` — ui-software-engineer
- `ux-software-engineer` — ux-software-engineer
- `validation-by-educational-experience` — Validation by Educational Experience
- `vendor-cyber-risk-analyst` — vendor-cyber-risk-analyst
- `vp-of-cloud` — vp-of-cloud
- `vp-of-infrastructure` — vp-of-infrastructure
- `web-application-developer` — web-application-developer
- `web-pentester` — web-pentester
- `wireless-wifi-mobility-specialist` — Wireless (Wi-Fi) Mobility Specialist
- `wms-developer` — wms-developer
- `yara-rule-authoring` — YARA Rule Authoring
- `zero-tolerance-for-failure` — zero-tolerance-for-failure
