# Threat hunting

## Table of contents

1. [Hunt cycle](#hunt-cycle)
2. [Pivot table](#pivot-table)
3. [Hunt ideas](#hunt-ideas)

## Hunt cycle

1. Hypothesis
2. Data collection plan
3. Execute queries
4. Analyze and pivot
5. Document findings (positive or negative)
6. Create detections or close gap ticket

## Pivot table

| Start entity | Pivot to |
|---|---|
| User | Hosts, IPs, apps consented |
| Hash | Hosts, first seen, prevalence |
| Domain | DNS requests, TLS SNI, proxy |
| IP | Connections, geo, ASN |

## Hunt ideas

- Rare parent-child process pairs
- New service binaries in user-writable paths
- OAuth apps with mail.read + low user count
- Cloud API keys created then immediate data list
