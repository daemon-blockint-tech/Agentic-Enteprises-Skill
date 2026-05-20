# Bus and interface security

## Table of contents

1. [Interface inventory](#interface-inventory)
2. [CAN and CAN-FD](#can-and-can-fd)
3. [LIN](#lin)
4. [Automotive Ethernet](#automotive-ethernet)
5. [Modbus (industrial, high level)](#modbus-industrial-high-level)
6. [Cross-cutting tests](#cross-cutting-tests)

## Interface inventory

For each interface on the bench, capture:

| Field | Notes |
|---|---|
| Physical layer | Connector, baud, termination, isolation |
| Protocol / stack | CAN matrix row, DoIP, SOME/IP service, Modbus function codes |
| Authentication | Seed-key, TLS, MAC, signed frames (if any) |
| Trust boundary | Who can send; gateway filtering rules |
| Safety class | ASIL/SIL hint; whether stimulus is prohibited |

## CAN and CAN-FD

**Security angles (lab only, within ROE):**

- **ID and DLC abuse** — unexpected IDs, length violations, error-frame storms (rate-limited)
- **Diagnostic services** — UDS session transitions (default/extended/programming), securityAccess sequencing
- **Gateway policy** — cross-domain frames blocked or forwarded; replay across segments
- **Timing** — bus-off recovery, priority inversion, flood at bounded rate
- **SecOC / MAC** (if present) — replay, counter rollback, acceptance of unsigned frames on trusted buses

Capture **DBC-aligned** interpretations in reports; attach raw `.blf`/`.asc` or vendor-native captures.

## LIN

- Schedule table violations and unauthorized frame injection on isolated networks
- NAD spoofing and duplicate master scenarios (only with safety-approved benches)
- Correlation with upstream CAN gateway when LIN is a satellite bus

## Automotive Ethernet

At high level (delegate deep IT pentest to `network-pentester` when scope is enterprise-wide):

- **Switch ACLs** and VLAN separation between domains (infotainment vs powertrain mock)
- **DoIP** routing and activation types; TLS where specified
- **SOME/IP** service discovery exposure on bench VLAN
- **Time sync** (gPTP) manipulation impact on time-sensitive functions
- Mirror/port capture points documented for evidence

## Modbus (industrial, high level)

- Unauthorized **read/write holding coils** from bench segment
- **Unit ID** scanning on isolated Modbus TCP/RTU
- Engineering workstation paths (logic download) when PLC is target—coordinate with vendor safety
- No guidance on disrupting live production PLCs; bench or shadow logic only

## Cross-cutting tests

| Test theme | Objective |
|---|---|
| **Replay** | Resend captured legitimate frames; observe acceptance |
| **Spoofing** | Impersonate ECU/node ID or source address |
| **Downgrade** | Force legacy diagnostic or unsigned mode if design allows fallback |
| **Denial of service** | Bounded bus load; measure recovery and watchdog behavior |
| **Firmware update path** | Unsigned image rejection, rollback, secure boot indicators (coordinate with RE) |

Map notable behaviors to **MITRE Embedded** / **ATT&CK ICS** where helpful for reader context—not as a substitute for reproduction steps.
