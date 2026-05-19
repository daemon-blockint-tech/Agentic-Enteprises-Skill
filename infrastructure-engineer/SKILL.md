---
name: infrastructure-engineer
description: |
  Guides infrastructure engineering across cloud (AWS/GCP/Azure), DevOps/platform engineering,
  and on-premise/hybrid environments. Covers VPC design, compute, storage, networking, IAM,
  serverless, CI/CD, Kubernetes, Terraform/Pulumi, monitoring, virtualization, and security hardening.
  Use when designing infrastructure, provisioning resources, building CI/CD pipelines, managing
  containers, automating platforms, or troubleshooting infrastructure issues.
---

# Infrastructure Engineer

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

**See `references/cloud_infrastructure.md` for VPC patterns, storage options, and IAM best practices.**

### 2. CI/CD & Platform Automation

**Pipeline essentials:**
- Build → Test → Security scan → Deploy → Verify
- GitOps with ArgoCD/Flux for K8s
- Feature flags for progressive rollout
- Automated rollback on failure

**See `references/devops_platform.md` for pipeline templates, K8s patterns, and GitOps workflows.**

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

**See `references/devops_platform.md` for SRE practices, SLI/SLO/SLA definitions, and incident response.**

### 4. Security & Compliance

**Security by layer:**
- Network: Security groups, NACLs, WAF, DDoS protection
- Identity: RBAC, least privilege, MFA, service accounts
- Data: Encryption at rest (KMS) and in transit (TLS 1.3)
- Application: Secrets management, vulnerability scanning
- Compliance: SOC 2, ISO 27001, GDPR, HIPAA controls

**See `references/security_compliance.md` for hardening guides, compliance frameworks, and secrets management.**

## When to Load References

- **Cloud infrastructure** → `references/cloud_infrastructure.md`
- **DevOps & platform** → `references/devops_platform.md`
- **Hybrid & on-premise** → `references/hybrid_onprem.md`
- **Security & compliance** → `references/security_compliance.md`
