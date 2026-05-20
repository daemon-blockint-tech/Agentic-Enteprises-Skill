# Cyber incident and ransomware recovery

## Table of contents

1. [Recovery vs IR boundaries](#recovery-vs-ir-boundaries)
2. [Decision tree](#decision-tree)
3. [Ransomware playbook](#ransomware-playbook)
4. [Wiper and destructive attacks](#wiper-and-destructive-attacks)
5. [Identity compromise recovery](#identity-compromise-recovery)
6. [Logging and evidence preservation](#logging-and-evidence-preservation)
7. [Crisis comms coordination](#crisis-comms-coordination)
8. [Return to normal](#return-to-normal)

## Recovery vs IR boundaries

| Phase | IR (`incident-responder`) | BCM/DR (this skill) |
|---|---|---|
| Detect & declare | **Lead** | Consult on BCP triggers |
| Contain & eradicate | **Lead** | Advise recovery order, rebuild vs restore |
| Recover services | Support | **Lead** on sequencing, RTO tracking |
| Comms | Facts to stakeholders | Prolonged outage **cadence** templates |
| Post-incident | PIR, lessons | Update RTO/RPO, playbooks, tests |

Never pay ransom or negotiate without **legal and executive** decision—document options only.

## Decision tree

```
Confirmed encryption or destructive malware?
├─ NO → Follow standard DR/BCP for outage; IR may still run parallel
└─ YES →
    ├─ Backups verified clean + immutable? (test hash/sample restore)
    │   ├─ YES → Prefer RESTORE to isolated env → validate → cutover
    │   └─ NO → REBUILD from gold images / new tenants; assume compromise
    ├─ Domain-wide admin compromised?
    │   └─ YES → Identity recovery BEFORE broad restore
    └─ Exfiltration suspected?
        └─ Coordinate legal/regulatory prep; preserve logs per hold
```

**Restore-in-place** only when IR and forensics confirm **no attacker persistence** in restored images.

## Ransomware playbook

### Phase 0 — Preparation (before event)

- Maintain **offline/immutable** backups; separate admin for backup plane
- Document **gold images**, IaC baselines, and SaaS tenant rebuild steps
- Pre-approve **isolation** actions (VLAN, disable sync, disable GPO scripts)
- Store **critical runbooks** outside primary domain (out-of-band access)

### Phase 1 — Mobilize (0–2 h)

1. IR declares incident; activate cyber recovery annex
2. Freeze **backup deletion** and **replication** jobs; snapshot backup catalog metadata
3. Identify **patient zero** timeline; map encrypted scope
4. Preserve **logs** off affected systems (forwarders, cloud audit)—see logging section
5. Establish **recovery bridge** separate from potentially compromised chat/IdP if needed

### Phase 2 — Assess backups (2–8 h)

1. Identify last **clean** backup per system (before dwell time)
2. Test restore to **isolated network**; scan restored images
3. Record **achievable RPO** per system; compare to register
4. If backups encrypted or poisoned, switch to **rebuild track**

### Phase 3 — Recover (hours–days)

1. Recover **identity** and **network controls** first
2. Restore or rebuild **tier-0 security stack** (SIEM, EDR management)
3. Restore workloads in **waves**; validate each wave before next
4. **Rotate all secrets** post-cutover (API keys, service principals, DB passwords)
5. Enhanced monitoring for **30+ days**; document RTA vs RTO

### Phase 4 — Close

- Executive sign-off on restoration completeness
- Feed gaps to PIR; schedule **restore test** and tabletop within 90 days

## Wiper and destructive attacks

- Assume **no reliable decrypt**; focus on rebuild and data loss acceptance
- Prioritize **business-critical data** recreation paths (not only IT restore)
- Coordinate with `digital-forensics-analyst` if attribution or legal hold required
- Document **permanent loss** items for leadership and legal (not legal advice)

## Identity compromise recovery

1. Disable compromised accounts and **federation** paths if needed
2. Revoke **refresh tokens**, app passwords, API keys tied to IdP
3. Reset **KRBTGT** / tier-0 recovery per AD best practice if domain affected
4. Rebuild or restore IdP from **known-good** backup to isolated environment
5. Re-enroll MFA devices; treat prior MFA as untrusted
6. Validate **conditional access** and admin roles before general user login

Handoff to `information-security-engineer` for control hardening post-recovery.

## Logging and evidence preservation

During recovery:

- **Do not** delete logs for "cleanup" without legal/IR approval
- Redirect ingest to **clean SIEM** or cold storage; note gap in investigation timeline
- Export **cloud audit**, IdP, EDR, and email logs to immutable store early
- Document **detection gap** period if SIEM down (for PIR and regulatory prep)

Forensic depth → `digital-forensics-analyst`; war-room timeline → `incident-responder`.

## Crisis comms coordination

BCM provides **prolonged recovery** messaging support:

| Audience | Content focus | Approval |
|---|---|---|
| Internal staff | What works, workarounds, ETA bands | Comms + IR |
| Leadership | RTO status, decisions, resource needs | Exec sponsor |
| Customers | Facts only, no speculation | `communication-lead`, legal |
| Regulators | Via legal/compliance; fact packs | Legal |

Use **separate fact and hypothesis** sections; update on cadence tied to severity.

## Return to normal

Criteria to exit DR mode:

- Tier-0/1 services at or above agreed **minimum function**
- No active uncontained encryption spread
- Monitoring and identity trust **validated**
- Action register for hardening owned and dated

Conduct **hot wash** within 5 business days; update cyber recovery annex and restore tests.
