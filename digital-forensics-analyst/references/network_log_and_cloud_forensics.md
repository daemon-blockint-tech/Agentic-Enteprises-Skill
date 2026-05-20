# Network, log, and cloud forensics

## Table of contents

1. [Log source matrix](#log-source-matrix)
2. [Network forensics](#network-forensics)
3. [Cloud forensics](#cloud-forensics)
4. [Export and retention](#export-and-retention)
5. [Correlation tips](#correlation-tips)

## Log source matrix

| Layer | Typical sources | Forensic value |
|---|---|---|
| Identity | IdP sign-in, MFA, conditional access | Account compromise, impossible travel |
| Endpoint | EDR process/network, Sysmon | Execution, C2, lateral movement |
| Network | Firewall, proxy, DNS, NDR | Ingress/egress, beaconing |
| Email | Gateway, mailbox audit | Phishing, BEC, rules |
| Application | App audit, DB audit | Fraud, data access |
| Cloud | CloudTrail, Activity/Audit, K8s audit | API abuse, IAM changes |

Normalize all events to **UTC**. Note **clock skew** if sources disagree.

## Network forensics

### PCAP and flow data

When full packets exist:

- Identify **sessions** (五元组 / 5-tuple): src/dst IP, ports, protocol, time
- Extract **DNS queries**, HTTP Host, TLS SNI, JA3 where available
- Flag **long-lived beaconing**, rare ports, Tor/VPN exit patterns

When only **NetFlow/IPFIX** exists:

- Volume and duration anomalies; periodic intervals
- Correlate flows to **host and user** via DHCP/DNS/EDR

### Proxy and DNS

- Reconstruct user browsing and downloads (policy permitting)
- Identify **newly seen domains** in incident window
- Map **DGA** or fast-flux only with enrichment—not as sole proof

## Cloud forensics

Partner with `cloud-security-engineer` for guardrail context; forensics owns **timeline and factual reconstruction**.

| Provider | Priority exports |
|---|---|
| AWS | CloudTrail (org trail), VPC Flow Logs, GuardDuty findings, S3 access logs, EBS snapshots |
| Azure | Activity Log, Entra sign-in, NSG flow logs, disk snapshots |
| GCP | Admin Activity, VPC Flow Logs, Cloud Logging sinks, disk snapshots |
| SaaS | Vendor audit API (M365, Google Workspace, Salesforce, etc.) |

Capture:

- **API caller identity** (role ARN, service principal, access key ID)
- **Resource ARNs/IDs** and region
- **Request parameters** (security group changes, public exposure)

Document **gaps** (logging not enabled, short retention, missing org trail).

## Export and retention

Before exports expire:

1. Record **retention policy** per source
2. Export **raw** formats where possible (JSON/CSV), not screenshots alone
3. Hash export files; store with evidence ID
4. Note **time range** and **filters** used (reproducibility)

## Correlation tips

- Join on **username**, **device ID**, **source IP**, **session ID**, **cloud request ID**
- Use **first-seen** / **last-seen** per IOC across sources
- Separate **north-south** vs **east-west** movement in narrative
- Hand enriched IOCs to `soc-analyst` for blocklist/playbook updates—not for queue ownership
