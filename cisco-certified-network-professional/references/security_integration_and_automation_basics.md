# Security integration and automation basics

## Table of contents

1. [Scope at the network layer](#scope-at-the-network-layer)
2. [802.1X and port-based access](#8021x-and-port-based-access)
3. [ACL design and placement](#acl-design-and-placement)
4. [Control plane protection](#control-plane-protection)
5. [Device hardening checklist](#device-hardening-checklist)
6. [Management plane security](#management-plane-security)
7. [Automation and programmability basics](#automation-and-programmability-basics)
8. [Handoffs to security peers](#handoffs-to-security-peers)

## Scope at the network layer

This reference covers **integration** of security controls on campus and WAN devices — not enterprise GRC, pentest programs, or cloud CSPM.

**In scope:**

- 802.1X / MAB on access ports
- Infrastructure ACLs and **zone-based** filtering at distribution
- **Control Plane Policing (CPP)** and management ACLs
- Cisco **IOS-XE hardening** baselines (conceptual)
- Awareness of **NETCONF/RESTCONF** and Git-backed config

**Out of scope:**

| Topic | Skill |
|---|---|
| SOC 2 / ISO evidence pipelines | `information-security-engineer` |
| Full zero-trust product architecture | Security architecture peers |
| Firewall rule lifecycle (Palo Alto, FTD) | Security engineering / vendor runbooks |

## 802.1X and port-based access

**Components:**

| Component | Role |
|---|---|
| Supplicant | Client (802.1X on NIC) |
| Authenticator | Access switch port |
| Authentication server | RADIUS (ISE, NPS, etc.) |

**Deployment modes:**

- **Single-host** access mode on user ports
- **MAB** for printers/IoT without supplicant — **limited** VLAN only
- **Guest** via separate SSID or VLAN after portal (wireless peer for portal depth)

**Design checklist:**

- [ ] **RADIUS redundancy** (primary/secondary)
- [ ] **Dynamic VLAN** assignment documented per authorization profile
- [ ] **Guest** cannot reach RFC1918 corporate without firewall
- [ ] **Critical auth** vs **open auth** policy for RADIUS outage (document risk)
- [ ] **Reauth** timers for wireless roaming coordination

**Meraki:** 802.1X and RADIUS in dashboard; align authorization VLANs with IOS-XE campuses.

## ACL design and placement

**Principles:**

- **Deny by exception** at trust boundaries; **permit** established/related on stateful firewalls
- **Infrastructure ACLs** on SVIs facing servers or management zones
- Avoid **mega-ACLs** on core — aggregate rules; log sparingly

| Placement | Typical purpose |
|---|---|
| Access port | Not common; prefer 802.1X |
| Distribution SVI | Inter-VLAN segmentation |
| WAN edge | Bogon filter, anti-spoofing |
| Management | SSH/HTTPS source restriction |

**IPv6:** separate ACLs; remember **ICMPv6** essentials for ND (do not over-filter on internal segments).

**Object groups** and **named ACLs** improve readability; comment with ticket IDs.

## Control plane protection

Protect **CPU-bound** processes from flooding:

- **Control Plane Policing (CPP)** — classify ARP, BGP, SNMP, SSH
- **CoPP policy maps** — police or drop excess classes
- **rate-limit** routing protocol neighbors on untrusted interfaces
- Disable **unused services** (finger, pad, etc. on legacy images)

**BGP/OSPF authentication** on all external and WAN adjacencies per policy.

## Device hardening checklist

Apply per platform baseline (CIS or vendor guide):

- [ ] **SSH v2** only; disable Telnet
- [ ] **Strong passwords** or **certificate-based** admin auth
- [ ] **Enable secret** type 8/9 where supported
- [ ] **Login banner** (legal notice)
- [ ] **AAA** (TACACS+/RADIUS) for admin with local fallback documented
- [ ] **Privilege levels** — least privilege for operators
- [ ] **SNMPv3** only; no default communities
- [ ] **NTP authentication** where required
- [ ] **Unused ports** shutdown in default template
- [ ] **BOOTP/IP source routing** disabled per hardening guide
- [ ] **Image integrity** — signed images, secure boot where available

**Meraki:** dashboard RBAC, MFA on admin accounts, API key rotation.

## Management plane security

| Control | Implementation |
|---|---|
| Out-of-band management | Dedicated Mgmt VRF or OOB network |
| Jump hosts | SSH only via bastion; no direct internet SSH to devices |
| Segmentation | ACL: NMS subnets only to SNMP/SSH |
| Config backup | Encrypted Git; no secrets in repo |
| Certificate lifecycle | HTTPS for NETCONF/gRPC |

**ZTP/PNP:** validate **chain of trust** for bootstrap; staging VLAN isolated.

## Automation and programmability basics

**Goals at CCNP depth:** consistency and auditability, not full NetDevOps program.

| Mechanism | Use |
|---|---|
| **Git** | Versioned configs, PR review for network changes |
| **NETCONF/RESTCONF** | Structured config push on IOS-XE |
| **Ansible** | Idempotent playbooks for repeatable baselines |
| **Meraki API** | Dashboard automation for branch templates |
| **DNA Center** (if deployed) | Intent templates; document drift handling |

**Guardrails:**

- Dry-run and **rollback** snippet per change
- **Secrets** in vault, not variables in plain Git
- Test in **lab** or maintenance window for routing policy changes

Defer **Terraform cloud networking** primary design to `cloud-engineer`.

## Handoffs to security peers

| Scenario | Escalate to |
|---|---|
| Enterprise security architecture, SASE, ZTNA | Security architecture / `information-security-engineer` |
| Pentest findings on network devices | Remediation with security engineering |
| SIEM correlation rules for NetFlow/syslog | SOC / detection engineering |
| Identity policy (AD groups, cert templates) | Identity team with 802.1X data from network |

Network engineering delivers **reachability, segmentation hooks, and telemetry** — security peers own **control frameworks and attestation**.
