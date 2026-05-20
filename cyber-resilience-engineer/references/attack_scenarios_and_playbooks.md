# Attack scenarios and playbooks

## Table of contents

1. [Playbook structure](#playbook-structure)
2. [Ransomware and extortion](#ransomware-and-extortion)
3. [Destructive malware / wiper](#destructive-malware--wiper)
4. [Identity platform compromise](#identity-platform-compromise)
5. [Logging and detection loss](#logging-and-detection-loss)
6. [Cloud control-plane and SaaS loss](#cloud-control-plane-and-saas-loss)
7. [Supply chain and golden image](#supply-chain-and-golden-image)
8. [Decision gates](#decision-gates)

## Playbook structure

Each engineering playbook includes:

| Section | Content |
|---|---|
| **Triggers** | Technical and business signals to activate |
| **Immediate actions** | Isolation, preserve evidence, stop spread |
| **Resilience mode** | What to defer vs accelerate (recovery vs investigation) |
| **Recovery sequence** | Ordered steps with owners |
| **MVC targets** | Minimum viable per phase |
| **Validation** | Integrity checks before prod traffic |
| **IR handoffs** | When `incident-responder` owns vs resilience leads restore |
| **Comms inputs** | Facts for BCM/crisis comms—not draft external messages |
| **Evidence** | Logs and tickets to retain |

Keep playbooks **executable**—commands, console paths, automation job names, not policy prose.

## Ransomware and extortion

**Triggers:** encryption notices, mass file renames, backup encryption, BEC + deployment anomaly.

**Engineering sequence:**

1. Activate bridge; IR leads containment (`incident-responder`)
2. **Isolate** segments; disable risky automation and remote tools
3. Assess **backup plane**—last clean immutable copy; assume prod untrusted
4. **Decision gate:** decrypt vs rebuild (default **rebuild** unless IR/legal approves pay/decrypt)
5. Provision **greenfield** environment from gold IaC/images
6. Restore data from immutable copy **after** malware-free verification
7. Rotate **all** secrets, API keys, certs; force password reset if IdP touched
8. Re-enable logging and EDR **before** broad user access
9. MVC cutover; phased user return; monitor for re-entry

Document **RTO impact** if rebuild path chosen—set expectations early.

## Destructive malware / wiper

**Triggers:** boot failures, MBR/GPT damage, mass deletes, firmware alerts.

**Differences from ransomware:**

- Often **no** negotiation; backups targeted first
- Faster priority on **offline/immutable** copies and gold images
- Hardware reimage may dominate RTA

Sequence emphasizes **spare capacity** (hardware pool, cloud quota), **IaC rebuild**, and **tape/air-gap** restore paths.

## Identity platform compromise

**Triggers:** impossible travel admin actions, MFA bypass reports, rogue federation apps, golden SAML cert.

**Resilience actions:**

1. Enable **break-glass** local accounts (pre-staged, tested quarterly)
2. Revoke sessions and refresh tokens globally
3. Disable compromised federation apps and OAuth grants
4. Restore IdP config from **immutable** config backup or vendor export
5. Re-issue MFA enrollment; prioritize tier-0 admins
6. Validate **conditional access** and PAM before restoring SaaS SSO

Coordinate with `information-security-engineer` for hardening; IR for attribution.

## Logging and detection loss

**Triggers:** SIEM ingest drop, log forwarder silence, EDR cloud disconnect.

**Impact:** Extended blind spot—recovery priority **after** IdP, parallel with network isolation.

**Actions:**

1. Queue/buffer on endpoints where possible
2. Failover to **secondary region** or warm SIEM
3. Restore parsers from versioned config backup
4. Backfill from archives after ingest restored (watch RPO)
5. Document **detection gap window** for IR and compliance consumers

## Cloud control-plane and SaaS loss

**Triggers:** regional API outage, identity provider API failure, mistaken org-wide deny policy.

**Actions:**

1. Execute **alternate admin path** (break-glass account, support ticket, secondary region)
2. Run DNS and traffic failover per `cloud-engineer` architecture
3. Activate **manual runbooks** for critical security SaaS (export APIs if available)
4. Track vendor status; record RTA against RTO
5. Post-incident: add **synthetic canaries** for control-plane dependencies

Maintain **offline copies** of runbooks and contact trees—assume IdP unavailable.

## Supply chain and golden image

**Triggers:** compromised CI/CD, malicious package, trojaned AMI/container base.

**Actions:**

1. Halt deployments; freeze artifact registry
2. Identify **last known-good** image digest and IaC commit
3. Rebuild pipelines from clean runners
4. Redeploy from signed gold images only
5. Expand scanning and provenance (SBOM) in backlog

Link to IR for scope; resilience owns **rebuild path** and image promotion gates.

## Decision gates

| Gate | Question | Default |
|---|---|---|
| **G1 Restore-in-place** | Forensic need vs speed? | No in-place without IR sign-off |
| **G2 Pay ransom** | Legal/regulatory/business? | Out of engineering scope—escalate |
| **G3 Prod cutover** | MVC and monitoring green? | Hold until logging + IdP OK |
| **G4 User access** | Re-infection risk? | Phased by tier |
| **G5 Test in prod** | Exercise vs incident? | Stop exercise if real attack suspected |

Record gate decisions with timestamp and approver in incident ticket.
