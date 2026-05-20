# Automotive and industrial patterns

## Table of contents

1. [Automotive reference architecture](#automotive-reference-architecture)
2. [Common automotive test themes](#common-automotive-test-themes)
3. [Industrial ICS patterns](#industrial-ics-patterns)
4. [Supply chain and lifecycle](#supply-chain-and-lifecycle)
5. [Anti-patterns](#anti-patterns)

## Automotive reference architecture

Typical bench targets (names vary by OEM):

| Domain | Examples | Security relevance |
|---|---|---|
| **Powertrain / chassis** | ECM, TCU, brake/abs mock | High safety sensitivity — strict ROE |
| **Body / comfort** | BCM, door modules | Gateway paths, keyless entry surfaces |
| **Infotainment / connectivity** | IVI, T-box, telematics | Rich attack surface; often isolated VLAN on bench |
| **ADAS / perception** | Radar/camera ECU (mocked) | Sensor spoof via HIL; calibration integrity |
| **Gateway / zonal** | Central gateway, zone controllers | Cross-domain routing policy |
| **Diagnostics** | OBD-II, DoIP edge | Session and authentication flows |

Use OEM-provided **threat models** when available; otherwise derive from interface inventory.

## Common automotive test themes

| Theme | Bench approach | Evidence |
|---|---|---|
| **UDS securityAccess** | Scripted seed-key attempts within ROE | Session logs, negative response codes |
| **Programming session** | Signed vs unsigned image handling | Flash tool logs, version registers |
| **Gateway filtering** | Cross-domain frame from tap | Trace showing pass/block |
| **Key storage** | No extraction guidance — observe behavior only | Lockout, tamper flags |
| **OTA (mocked)** | Local update server on isolated VLAN | Manifest signature checks |
| **Wireless entry** | Cabled RF or shielded chamber | Pairing/downgrade observations |

Coordinate with `reverse-engineer` when analysis requires firmware images or cryptographic review beyond bus behavior.

## Industrial ICS patterns

| Pattern | Security focus on HIL bench |
|---|---|
| **PLC + HMI shadow** | Engineering station authentication, logic integrity |
| **SCADA gateway (mock)** | Segmentation from IT; protocol translation abuse |
| **Safety PLC** | Often **out of scope** for active injection — document-only review |
| **Fieldbus bridge** | Modbus ↔ proprietary mapping errors |
| **Historian / OPC** | Read-only exfil paths when historian is in scope |

Never test **live production** assets; use shadow logic, digital twin, or vendor training rigs.

## Supply chain and lifecycle

| Phase | HIL security angle |
|---|---|
| **Sample ECU receipt** | Baseline capture; compare to golden reference |
| **Integration** | Gateway rules before full vehicle HIL |
| **Field campaign** | Retest same test cases on post-patch firmware |
| **End of life** | Residual diagnostic exposure on refurbished units |

Document **hardware and firmware revision matrix** in the report appendix.

## Anti-patterns

| Anti-pattern | Why it fails |
|---|---|
| Treating HIL work as **network pentest only** | Misses bus-level and diagnostic trust boundaries |
| **Unbounded fuzz** on safety buses | Safety incident; non-reproducible results |
| **No baseline restore** | Contaminated retest and fleet risk |
| Findings without **trace correlation** | Not actionable for firmware teams |
| Skipping **safety sign-off** | Regulatory and personnel risk |
| Publishing **exploit chains** without redaction | Supplier and customer harm |
