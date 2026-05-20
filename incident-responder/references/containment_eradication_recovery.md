# Containment, eradication, and recovery

## Table of contents

1. [Phase overview](#phase-overview)
2. [Containment](#containment)
3. [Eradication](#eradication)
4. [Recovery](#recovery)
5. [Approval gates](#approval-gates)
6. [Coordination by incident type](#coordination-by-incident-type)

## Phase overview

Follow **contain → eradicate → recover** (NIST-style). Parallelize only when actions do not destroy evidence or increase blast radius.

| Phase | Goal | Exit criteria |
|---|---|---|
| Containment | Stop spread and attacker access | No new IOCs; C2 blocked; risky sessions closed |
| Eradication | Remove persistence and root cause | Malware gone; backdoors closed; vulns patched |
| Recovery | Restore normal operations safely | Services validated; enhanced monitoring in place |

## Containment

**Identity**

- Disable compromised accounts; revoke refresh tokens and API keys
- Force password reset or step-up re-auth for affected populations (scoped, not org-wide unless approved)
- Review IdP rules, forwarding, OAuth grants, and admin roles

**Endpoint / server**

- Network isolate host (EDR network containment preferred over abrupt power-off when forensics needed)
- Block IOCs at proxy, firewall, EDR policy—document TTL and owner

**Cloud**

- Suspend compromised keys; rotate access keys; restrict security group rules
- Snapshot volumes before terminate; preserve audit logs (`cloud-security-engineer`)

**Application**

- Disable compromised integrations, webhooks, or service accounts
- Feature-flag or drain traffic from affected service if needed

Record every containment action: **who approved**, **UTC time**, **expected side effect**, **rollback**.

## Eradication

- Remove malware, scheduled tasks, webshells, and unauthorized accounts
- Close ingress paths (patch CVE, fix misconfiguration, remove public exposure)
- Rotate secrets: DB passwords, signing keys, CI tokens, encryption keys per key-management policy
- Rebuild from **gold image** when integrity uncertain
- Validate no persistence via fresh EDR scan and hunt queries

Engage `devsecops` if pipeline or artifact compromise suspected; `ai-redteam` if LLM tool abuse or prompt-injection persistence in agents.

## Recovery

1. Restore services from known-good backup or rebuild
2. Re-enable users and integrations in waves; monitor for recurrence
3. Increase detection sensitivity temporarily (higher-fidelity alerts to `soc-analyst`)
4. Confirm business functions and security controls (MFA, logging, backups)
5. Document **recovery time** and residual risk for post-incident review

## Approval gates

Require explicit approver for:

- Org-wide password reset or MFA reset
- Production data deletion or mass customer notification
- Law enforcement coordination
- Paying ransom (policy usually prohibits—legal + exec only)

## Coordination by incident type

| Type | Containment emphasis | Eradication emphasis |
|---|---|---|
| Account compromise | Session revoke, MFA review | Remove persistence in mailbox/rules |
| Ransomware | Isolate segments; stop lateral movement | Rebuild; verify backups offline |
| Data exfil | Block egress; preserve logs | Close exfil path; assess data sets |
| Supply chain | Disable compromised package/version | Rotate build secrets; redeploy clean artifacts |
| Cloud key leak | Disable key; SCP deny if needed | Audit API activity; least-privilege fix |
