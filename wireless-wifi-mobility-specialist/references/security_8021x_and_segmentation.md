# Security, 802.1X, and segmentation

## Table of contents

1. [SSID design patterns](#ssid-design-patterns)
2. [Authentication methods](#authentication-methods)
3. [802.1X and EAP architecture](#8021x-and-eap-architecture)
4. [RADIUS and NAC integration](#radius-and-nac-integration)
5. [WPA2-Enterprise vs WPA3-Enterprise](#wpa2-enterprise-vs-wpa3-enterprise)
6. [Guest and captive portal](#guest-and-captive-portal)
7. [Segmentation and policy enforcement](#segmentation-and-policy-enforcement)
8. [Operational security practices](#operational-security-practices)

## SSID design patterns

Minimize SSID sprawl—each SSID consumes airtime (beacons, probes). Typical enterprise set:

| SSID role | Auth | Segmentation |
|---|---|---|
| Corporate | 802.1X WPA3-Enterprise | user VLAN; dynamic VLAN via RADIUS |
| Voice | 802.1X or PSK (vendor voice) | dedicated voice VLAN; QoS |
| Guest | captive portal or PSK | guest VLAN; internet-only ACL |
| IoT / device | PSK, MPSK, or 802.1X | restricted VLAN; no route to corp |
| Lab / legacy | isolated | time-bounded; non-production |

Use **hidden SSID** sparingly—does not provide security; complicates operations.

## Authentication methods

| Method | Use | Notes |
|---|---|---|
| WPA3-Enterprise (SAE for personal only) | corporate users | prefer WPA3 where clients support |
| WPA2-Enterprise | legacy mix | transition plan to WPA3 |
| 802.1X EAP-TLS | managed devices | cert lifecycle critical |
| EAP-PEAP/MSCHAPv2 | legacy | weaker; phase out where possible |
| PSK | IoT, printers, simple guest | rotate; per-site or MPSK |
| MPSK (multiple PSK) | IoT scale | map PSK to VLAN without 802.1X per device |
| Open + portal | guest | terms, bandwidth, logging |

**OWE** (Enhanced Open) — encrypted open for guest in some designs; verify client support.

## 802.1X and EAP architecture

Logical components:

```
Supplicant (client) ↔ Authenticator (AP) ↔ Authentication server (RADIUS)
                              ↕
                         AS (AD/LDAP via RADIUS)
```

Key concepts:

- **Authenticator** terminates 802.1X on AP; passes EAP to RADIUS.
- **Supplicant** must be configured (GPO, MDM, or manual) with correct EAP type and trust anchors.
- **Certificate trust** — deploy enterprise root or use public CA for EAP-TLS; document rotation.
- **Machine vs user auth** — Windows often machine auth before user; affects VLAN assignment timing.

Failure modes to design for:

- RADIUS timeout → **local fallback** policy (deny vs guest VLAN) — default deny for corp SSID
- Clock skew → breaks cert validation
- Wrong outer identity → privacy and routing of inner EAP

## RADIUS and NAC integration

RADIUS responsibilities:

- Accept **Access-Request** from NAS (AP/controller)
- Return **Access-Accept/Reject** with VLAN, ACL, or filter-id attributes
- Accounting (optional) for session logging

Common attribute mappings:

| Attribute | Purpose |
|---|---|
| Tunnel-Type / Tunnel-Private-Group-Id | dynamic VLAN assignment |
| Filter-Id / ACL name | per-user policy |
| Session-Timeout | guest or contractor limits |

**NAC / posture** (conceptual):

- Redirect to remediation VLAN until patch/AV criteria met
- Integrate with **ClearPass, ISE, FortiNAC**, etc. as policy engine
- Document **MAB** (MAC auth bypass) for devices that cannot do 802.1X—tight allow lists only

High availability:

- **Multiple RADIUS** servers; AP/controller server lists with dead-time
- Geographic **RADIUS** placement for latency; cloud RADIUS requires resilient path

Handoff to `information-security-engineer` for **identity program**; this skill covers WLAN binding to that program.

## WPA2-Enterprise vs WPA3-Enterprise

| | WPA2-Enterprise | WPA3-Enterprise |
|---|---|---|
| Cipher | CCMP (AES) | GCMP-256 / CCMP transition modes |
| PMF | optional/recommended | required (802.11w) |
| Transition | widespread | mixed mode SSIDs during migration |

Migration approach:

1. Inventory **client capabilities** (WPA3 support %).
2. Pilot **WPA3-Enterprise** SSID or mixed mode on test floor.
3. Monitor **connection failures** and driver issues.
4. Deprecate WPA2-only when metrics allow.

## Guest and captive portal

Guest flows:

- **Web redirect** — DNS hijack or HTTP redirect to portal; HTTPS requires careful cert handling
- **Social/sponsor** — sponsor email approval for contractors
- **Self-registration** — SMS/email verification; logging for compliance

Security controls:

- **Guest VLAN** without RFC1918 access to corp
- **DNS filtering** and **egress firewall**
- **Bandwidth limits** and **session timeout**
- **WIPS** — detect rogue gateways on guest VLAN

Document **data retention** for guest logs (GDPR, local law).

## Segmentation and policy enforcement

Map **SSID → VLAN → VRF/firewall zone**:

| Zone | Example controls |
|---|---|
| Users | east-west microseg or ACL; internet via firewall |
| Voice | QoS end-to-end; limited internet |
| Guest | deny RFC1918; allow DNS/HTTP/S to internet |
| IoT | deny corp; allow only required destinations |

**FlexConnect / local switching** vs **central switching**:

- Local switching — VLAN terminates at access switch; lower WAN hairpin
- Central switching — traffic tunnels to controller; easier policy centralization, more WAN load

Coordinate with `network-backbone-architect` and `sd-wan-engineer` for **path** and **breakout** when guest traffic should exit locally at branch.

## Operational security practices

- Disable **legacy protocols** (WEP, WPA-TKIP) everywhere
- Enforce **PMF** where possible
- Rotate **PSKs** and MPSK keys on schedule
- Monitor **rogue APs**, **evil twin**, and **deauth** (where detectable)
- Protect **controller management** — out-of-band or dedicated mgmt VLAN, MFA for admin
- Backup **configs** and document **golden templates**
- Patch **controller/AP firmware** on supported train with rollback plan

Certificate operations:

- Track **EAP-TLS** cert expiry; automate renewal via MDM/PKI
- Use **separate certs** for admin UI vs EAP if vendor supports
