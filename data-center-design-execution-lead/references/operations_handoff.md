# Operations handoff

## Table of contents

1. [DCIM and monitoring](#dcim-and-monitoring)
2. [Runbooks](#runbooks)
3. [Maintenance](#maintenance)

## DCIM and monitoring

Minimum DCIM records per rack:

- Asset ID, U positions, kW nameplate, weight
- Power feed (A/B), PDU circuit
- Network ports (switch, port, VLAN intent link)

Monitor and alert:

- Inlet temperature, humidity per row
- PDU branch current vs threshold
- UPS battery health, fuel level (if gen)
- Leak detection (liquid cooling)

Integrate to NOC; severity aligned with `incident-management-engineer` if shared ops model.

## Runbooks

| Scenario | Outline |
|---|---|
| Smart hands | Escort, media ship, visual inspection |
| Emergency power-down | Order of shutdown; customer notification |
| Carrier outage | Failover WAN; colo ticket template |
| Thermal event | Row isolation, load shed policy |

## Maintenance

- Quarterly: torque checks, filter replacement, alarm test
- Annual: UPS battery test, thermal imaging, failover drill
- Vendor SLAs: response time, parts depot, escalation

Facilities owns MEP; IT owns racks and cabling above PDU—RACI in handoff doc.

After handoff, K8s and app deploy → `cluster-deployment-engineer`.
