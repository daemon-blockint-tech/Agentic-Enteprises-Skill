---
name: infrastructure-engineer
description: |
  Design and implement cloud infrastructure.
  Cover cloud architecture, IaC (Terraform, Pulumi), CI/CD pipelines, container orchestration (Kubernetes),
  networking, observability, and security hardening.
  Triggers on "design cloud infrastructure", "set up Terraform", "configure Kubernetes",
  "build CI/CD pipeline", "infrastructure monitoring", "network architecture",
  "security hardening", "infrastructure cost optimization", or "platform engineering". For day-2 Kubernetes cluster
  operations—Helm rollouts, add-ons, RBAC, GitOps sync, workload troubleshooting,
  use cluster-deployment-engineer. For data center facility design, power/cooling, rack layout,
  and build commissioning, use data-center-design-execution-lead. For on-prem compute utilization,
  GPU/CPU supply planning, stranded kW, and hardware refresh efficiency, use
  data-center-compute-supply-efficiency. For on-site colo smart-hands, rack-and-stack, cabling,
  and physical acceptance, use field-services-engineer. Compute accounting:
  compute-accounting-manager.
---

# Infrastructure Engineer

## Overview

Design and implement cloud infrastructure. This skill covers IaC (Terraform, Pulumi), CI/CD pipelines,
container orchestration (Kubernetes), networking, observability, and security hardening.

## Features

- Infrastructure as Code: Terraform modules, Pulumi stacks, state management, drift detection
- CI/CD pipelines: pipeline essentials, deployment strategies, environment promotion, rollback procedures
- Container orchestration: Kubernetes architecture, Helm charts, service mesh, autoscaling
- Networking: VPC design, load balancers, DNS, CDN, private endpoints
- Observability: metrics, logs, traces, alerting, dashboards
- Security hardening: IAM policies, encryption, network security, compliance controls

## Usage

1. Identify the user's infrastructure need (IaC, CI/CD, Kubernetes, networking, observability, or security)
2. Follow the corresponding workflow below
3. Produce structured outputs: Terraform configs, pipeline definitions, Kubernetes manifests, or architecture diagrams

## Examples

- **User**: "Set up Terraform for AWS"
  **Agent**: Runs IaC workflow, creates module structure, configures state backend, produces VPC, EC2, and RDS resources

- **User**: "Build a CI/CD pipeline"
  **Agent**: Runs CI/CD workflow, designs pipeline with build/test/deploy stages, adds environment promotion and rollback

- **User**: "Configure Kubernetes autoscaling"
  **Agent**: Runs Kubernetes workflow, sets up HPA based on CPU/memory, configures cluster autoscaler, tests scaling behavior

## When to Use

- Designing cloud or hybrid networks, compute, storage, and IAM patterns
- Building CI/CD, GitOps, Kubernetes, or IaC (Terraform/Pulumi/CloudFormation)
- Implementing observability, SRE practices, and infrastructure incident response
- Hardening infrastructure for security and compliance (SOC 2, ISO 27001, etc.)

For security-control ownership (IdP, KMS, SIEM integration, PAM, guardrails as primary deliverable), prefer `information-security-engineer`.

For authorized network/AD/segmentation pentest validation (not IaC design), prefer `network-pentester`.

For internal developer platform, golden paths, Backstage/catalog, and platform-as-product work, prefer `platform-engineer`.

## When NOT to Use

- Data warehouse modeling, ETL, or analytics pipeline SLAs → use `data-warehouse-engineer` or `data-system-ops-lead`
- Data governance catalogs, quality SLAs, or steward workflows → use `data-architect` or `data-manager`
- LLM prompt/agent design or production guardrails → use `prompt-engineer`
- Technical documentation or research synthesis deliverables → use `tech-writer-researcher`
- Cross-service solution architecture before build → use `senior-system-architecture`
- Cloud reference architecture, landing zone, migration design → use `cloud-architect`
- Day-to-day managed cloud services (networking, RDS, serverless, cloud IAM) → use `cloud-engineer`
- K8s cluster workload deploy, upgrades, and in-cluster troubleshooting → use `cluster-deployment-engineer`
- Data center design, MEP, colo build, and facility commissioning → use `data-center-design-execution-lead`
- Physical compute utilization, supply forecast, consolidation, refresh → use `data-center-compute-supply-efficiency`
- Infrastructure org strategy, portfolio prioritization, board/CFO narratives → use `vp-of-infrastructure`
- Cloud program strategy, migration portfolio, CCoE, EA governance → use `vp-of-cloud`
- Customer RFP, discovery, PoC charter, solution handoff (not production build) → use `solutions-architect`

## Core Workflows

### 1. Infrastructure Design & Provisioning

**Design checklist:**

1. **Define requirements**
   - Traffic patterns (steady, bursty, batch)
   - Compliance needs (data residency, encryption)
   - RTO/RPO targets
   - Budget constraints

2. **Choose compute model**
   | Model | When | Trade-off |
   |---|---|---|
   | VMs (EC2/GCE/VM) | Predictable workloads | Management overhead |
   | Containers (EKS/GKE/AKS) | Microservices, portability | Orchestration complexity |
   | Serverless (Lambda/Cloud Functions) | Event-driven, variable load | Cold start, limits |
   | Bare metal | High performance, licensing | Full management burden |

3. **Design network**
   - VPC/VNet with public/private subnets
   - NAT Gateway for outbound-only workloads
   - Transit Gateway for multi-VPC/VNet
   - PrivateLink/Private Service Connect for SaaS

4. **Provision with IaC**
   - Terraform for multi-cloud
   - CloudFormation for AWS-only
   - Pulumi for programmatic (Python/TS)
   - Ansible for configuration management

### 2. CI/CD & Platform Automation

**Pipeline essentials:**
- Build → Test → Security scan → Deploy → Verify
- GitOps with ArgoCD/Flux for K8s
- Feature flags for progressive rollout
- Automated rollback on failure

### 3. Monitoring & Reliability

**Observability stack:**
- Metrics: Prometheus + Grafana, Datadog, CloudWatch
- Logs: ELK, Loki, Splunk
- Traces: Jaeger, Zipkin, AWS X-Ray
- Alerts: PagerDuty, Opsgenie, Alertmanager

**Reliability patterns:**
- Health checks: liveness, readiness, startup probes
- Circuit breakers: fail fast, degrade gracefully
- Rate limiting: token bucket, leaky bucket
- Bulkheads: isolate failure domains

### 4. Security & Compliance

**Security by layer:**
- Network: Security groups, NACLs, WAF, DDoS protection
- Identity: RBAC, least privilege, MFA, service accounts
- Data: Encryption at rest (KMS) and in transit (TLS 1.3)
- Application: Secrets management, vulnerability scanning
- Compliance: SOC 2, ISO 27001, GDPR, HIPAA controls
