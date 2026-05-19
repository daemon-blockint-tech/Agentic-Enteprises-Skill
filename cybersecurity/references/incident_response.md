# Incident response

## Table of contents

1. [Preparation](#preparation)
2. [Containment actions](#containment-actions)
3. [Evidence](#evidence)

## Preparation

- Runbooks per scenario (ransomware, credential leak, DDoS)
- Contact tree and legal/comms roles
- Tabletop exercise annually

## Containment actions

| Scenario | Action |
|---|---|
| Compromised account | Disable sessions, rotate creds |
| Malware host | Isolate network, image disk |
| Data exfil suspicion | Block egress, preserve logs |

## Evidence

Chain of custody for disk images and log exports; coordinate with legal before broad notification.
