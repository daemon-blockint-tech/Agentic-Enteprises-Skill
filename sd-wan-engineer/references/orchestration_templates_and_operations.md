# Orchestration, templates, and operations

## Table of contents

1. [Control plane architecture](#control-plane-architecture)
2. [Template hierarchy](#template-hierarchy)
3. [Device lifecycle](#device-lifecycle)
4. [Policy promotion workflow](#policy-promotion-workflow)
5. [RBAC and tenancy](#rbac-and-tenancy)
6. [Monitoring and observability](#monitoring-and-observability)
7. [Multi-cloud and DC breakout operations](#multi-cloud-and-dc-breakout-operations)
8. [Day-two runbooks](#day-two-runbooks)

## Control plane architecture

| Component | Role | Resilience |
|---|---|---|
| **Orchestrator / vManage / Director** | Config, policy, analytics | Clustered; backup; DR site |
| **Controller / OMP / management** | Overlay control signaling | Multi-instance; geographic redundancy |
| **Certificate authority / PKI** | Device identity for overlay | HSM or enterprise CA integration |
| **Analytics / collector** | Telemetry, alarms | Scale for flow record volume |

**Control plane outage** does not always stop forwarding—document **last-known-good** behavior and stale policy risk.

## Template hierarchy

Use layered templates to scale **branch connectivity**:

| Template type | Contents |
|---|---|
| **Device / platform** | Model, interfaces, licenses, software version |
| **Feature** | BFD timers, OMP, security profile, SNMP |
| **Transport / TLOC** | Underlay colors, weights, allowed services |
| **Service / VPN / VRF** | LAN segments, DHCP, routing to LAN |
| **Policy group** | SLA classes, app routes, firewall rules |

**Golden templates** per site class; **exceptions** via attach variables (hostname, circuit IDs, hub preference).

Avoid one-off CLI on edges—drift breaks orchestration model.

## Device lifecycle

| Phase | Actions |
|---|---|
| **Staging** | Factory default; bootstrap (ZTP/PnP); assign to staging template |
| **Provisioning** | Certificates; site ID; attach production policy group |
| **Upgrade** | Canary site class; maintenance window; rollback image |
| **Decommission** | Revoke certs; remove from policy; archive config |

**Zero-touch provisioning** requires DHCP/DNS options or redirect to onboarding server—document per vendor (Viptela ZTP, VeloCloud activation, etc.).

## Policy promotion workflow

```
Dev policy group → lab edges → validation
      ↓
Staging / pilot site class (1–2 weeks)
      ↓
Production rollout by region (change ticket)
      ↓
Post-change verification (dashboards + synthetic apps)
```

- Version **templates**; export JSON/XML for audit
- Use **read-only** analyst role for NOC
- **Rollback** = reattach previous policy group version, not manual box fixes

## RBAC and tenancy

| Role | Permissions |
|---|---|
| **Architect** | Template design, policy group edit |
| **Operator** | Push approved changes, clear alarms |
| **NOC** | Read-only, run diagnostics |
| **Security** | Firewall/SWG policy sections |
| **MSP** | Scoped tenant if multi-customer |

Separate **prod vs lab** orchestrator tenants where possible.

## Monitoring and observability

Monitor **overlay and underlay** separately:

| Signal | Overlay | Underlay |
|---|---|---|
| Reachability | Tunnel up, control up | Interface up, BGP/OSPF if used |
| Performance | Loss/latency on tunnel | Circuit utilization, errors |
| Apps | App route hits, SLA violations | N/A |
| Security | IPS/SWG blocks | N/A |

Export to **SNMP, syslog, IPFIX/NetFlow, telemetry (gRPC)**—align with enterprise NMS/SIEM.

Dashboards per site class:

- Top sites by loss or jitter
- Underlay utilization vs commit
- Policy change timeline
- Certificate expiry horizon

For production SLO alignment → `site-reliability-engineer`.

## Multi-cloud and DC breakout operations

| Pattern | Operations focus |
|---|---|
| **Cloud hub in DC** | Extend SD-WAN to cloud WAN edge appliance or virtual edge |
| **Cloud-native WAN** | Partner integration (AWS TGW, Azure vWAN)—coordinate with `cloud-architect` |
| **Direct connect + SD-WAN** | Underlay handoff at Equinix; route advertisement discipline |

Avoid **asymmetric routing** between cloud and on-prem—document preferred paths for IaaS RFC1918 prefixes.

## Day-two runbooks

Minimum runbook set:

1. **Site hard down** — underlay vs overlay triage tree
2. **Degraded performance** — SLA class stats, path stickiness reset
3. **Certificate expiry** — renewal and staggered redeploy
4. **Controller upgrade** — maintenance checklist
5. **Quarantine site** — security incident isolation template
6. **Mass template push failure** — rollback and partial attach recovery

Pair with carrier escalation matrix (circuit ID, NOC number).
