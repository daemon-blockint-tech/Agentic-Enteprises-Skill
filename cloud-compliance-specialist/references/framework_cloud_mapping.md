# Framework mapping in cloud

## Table of contents

1. [SOC 2 and ISO on cloud](#soc-2-and-iso-on-cloud)
2. [HIPAA](#hipaa)
3. [PCI DSS](#pci-dss)
4. [FedRAMP and government cloud](#fedramp-and-government-cloud)
5. [CIS and Well-Architected](#cis-and-well-architected)

## SOC 2 and ISO on cloud

Common Trust Services Criteria → cloud evidence:

| TSC theme | Cloud evidence examples |
|---|---|
| CC6 Logical access | IdP federation, IAM Access Analyzer export, access reviews |
| CC7 System ops | CloudTrail/Activity Log, change tickets linked to deploy |
| CC8 Change mgmt | PR approvals + pipeline logs (`devsecops`) |
| CC6.1 Encryption | KMS policies, default encryption Config rules |
| A1 Availability | Multi-AZ config, backup jobs (reliability narrative with `site-reliability-engineer`) |

ISO 27001 Annex A: map same technical checks; add **supplier** evidence for cloud provider SOC.

## HIPAA

Technical safeguards (customer responsibility on cloud):

- **BAA** executed with provider for in-scope services
- **Encryption** at rest and in transit for PHI stores
- **Access controls** — least privilege, MFA, audit logs
- **Backup and DR** — encrypted, access-controlled
- **No PHI** in unapproved regions or public resources

Evidence: Config rules for public exposure, KMS usage, log retention ≥ org policy.

Legal BAA scope → `commercial-counsel`; technical proof → this skill.

## PCI DSS

Cloud scoping pitfalls:

- **CHD environment** boundary — network segmentation proof (SG/NSG, private subnets)
- **No CHD** on shared multi-tenant without compensating controls
- **Logging** and time sync for in-scope components
- **Scanning** — ASV for external; internal for in-scope CDE

Map each PCI requirement to **specific account/VNet** and service; exclude out-of-scope accounts from assessment boundary diagram.

## FedRAMP and government cloud

- Use **authorized** services only (FedRAMP marketplace / GovCloud boundaries)
- **Impact level** (Low/Moderate/High) drives control baseline
- Leverage provider **FedRAMP package** for inherited controls; document **customer configuration** for remainder
- Change management and continuous monitoring align with ConMon expectations

Implementation of technical controls → `cloud-security-engineer` + `enterprise-cloud-architect`.

## CIS and Well-Architected

Use as **operational baselines** mapped to audit controls:

- CIS AWS/GCP/Azure Benchmarks → Config conformance packs / SCC
- AWS Well-Architected **Security** pillar — gap input for remediation backlog

CIS pass ≠ SOC pass; use as continuous hygiene feeding CCM.
