# Recovery objectives and tiers

## Table of contents

1. [Definitions](#definitions)
2. [Tiering model](#tiering-model)
3. [Setting RTO and RPO](#setting-rto-and-rpo)
4. [Security-critical service targets](#security-critical-service-targets)
5. [Recovery strategies](#recovery-strategies)
6. [Activation and sequencing](#activation-and-sequencing)
7. [Exceptions and risk acceptance](#exceptions-and-risk-acceptance)

## Definitions

| Term | Meaning |
|---|---|
| **RTO** | Maximum acceptable time to restore **minimum viable function** |
| **RPO** | Maximum acceptable **data loss** (time since last recoverable point) |
| **MTPD** | Maximum tolerable period of disruption (from BIA) |
| **RTA** | **Actual** recovery time in test or incident |
| **MVC** | Minimum viable capability during degraded recovery |

RTO/RPO are **engineering contracts**—require service owner sign-off and BCM alignment (`bcm-disaster-recovery-specialist`).

## Tiering model

| Tier | Business impact | Engineering expectation |
|---|---|---|
| **0** | Existential / regulatory / safety | Active/active or warm; RPO minutes; tested quarterly |
| **1** | Major revenue or security blind spot | Warm or rapid restore; RPO ≤1 h; tested semi-annually |
| **2** | Material but workaround exists | Backup restore; RPO hours; annual test |
| **3** | Low / dev / non-prod | Best-effort; document accepted loss |

**Cyber rule:** tier-0/1 **security services** (IdP, SIEM hot, KMS, secrets) default to tier-0/1 even if business app is tier-2—logging and identity gaps extend attacker dwell time.

## Setting RTO and RPO

1. Ingest **MTPD** and process criticality from BCM BIA
2. Subtract **mobilization** (assessment, bridge stand-up, approvals)—often 30–120 min
3. Set RTO ≤ remaining budget for **restore work** (not full performance)
4. Set RPO from replication lag, backup frequency, and **legal log minimums**
5. Validate with **restore test** or game day; record RTA vs RTO
6. Automate **monitoring** of backup lag and replication drift as leading indicators

Document **MVC** per service: what "recovered" means (e.g., SIEM ingesting 80% sources, not full historical search).

## Security-critical service targets

Indicative starting points—**calibrate to your BIA**:

| Service | Tier | RTO (indicative) | RPO (indicative) | Notes |
|---|---|---|---|---|
| Production IdP / SSO | 0 | 1–4 h | 0–15 min | Break-glass outside RTO path |
| MFA / PAM | 0–1 | 4 h | 0–1 h | Emergency access procedure |
| KMS / HSM | 0–1 | 4–8 h | 0 | Ceremony may extend RTA |
| SIEM (hot) | 1 | 4–8 h | 15 min–1 h | Ingest gap = detection blind spot |
| Log archive (cold) | 2 | 24 h | 1–24 h | Investigation history |
| EDR console | 1 | 4 h | 1 h | Agents may buffer locally |
| SOAR | 2 | 24 h | 4 h | Manual playbooks interim |
| Secrets manager | 0–1 | 4 h | 0–15 min | Downstream rotation deps |
| PKI / internal CA | 1 | 8–24 h | 1 h | Cert expiry cascade |

## Recovery strategies

| Strategy | Use when | Cyber note |
|---|---|---|
| **Active/active** | Tier-0, budget | Validate split-brain and key compromise |
| **Warm standby** | Tier-0/1 regional | Drift testing; secrets rotation |
| **Pilot light** | Tier-1/2 | Faster than cold; longer RTA |
| **Backup restore** | SaaS, DBs | Bound by RPO; verify integrity |
| **Rebuild from gold** | Post-ransomware, untrusted estate | Default after confirmed compromise |
| **Manual workaround** | Short gaps | Document security weakness; time-box |

After compromise, **restore-in-place** requires IR approval (`incident-responder`) and integrity proof—otherwise rebuild.

## Activation and sequencing

**Declare resilience/DR mode** when triggers met (customize in playbooks):

- Tier-0 outage >50% of RTO without credible ETA
- Ransomware/wiper affecting production or **backup plane**
- IdP or MFA total loss
- Cloud **control-plane** or identity API widespread failure
- Loss of **central logging** beyond RPO for tier-0/1

**Security-first recovery order** (adjust per scenario):

1. Command bridge and roles (`incident-responder`)
2. Network isolation and safe paths
3. IdP / MFA / break-glass
4. KMS, secrets, PKI
5. Logging and EDR visibility
6. Critical apps and data
7. Full performance and backlog catch-up

## Exceptions and risk acceptance

Every gap needs: **risk ID**, owner, compensating control, review date.

Examples requiring explicit acceptance:

- RPO >24 h for dev SIEM with no prod dependency
- No immutable backup for tier-1 DB (document attack scenario impact)
- Single-region IdP without warm standby

Review exceptions after **every material incident** and failed test.
