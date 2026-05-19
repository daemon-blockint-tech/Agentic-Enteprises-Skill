---
name: d3fend-isolate
description: |
  Guides cybersecurity isolation controls using MITRE D3FEND—access mediation, content filtering,
  execution isolation, and network segmentation. Covers access policies, permissions, content
  validation, process isolation, allowlisting, and traffic filtering. Use when segmenting
  networks, restricting access, filtering content, or isolating execution—not for detection
  (d3fend-detect), hardening (d3fend-harden), or deception (d3fend-deceive).
---

# D3FEND — Isolate

## When to Use

- Implementing access mediation (network, file, web session, physical)
- Configuring content filtering and validation (format, metadata, magic bytes)
- Isolating execution (process sandboxing, allowlisting, denylisting)
- Segmenting networks (VLANs, micro-segmentation, broadcast isolation)
- Managing DNS/IP allowlists and denylists
- Setting system call filtering and I/O port restrictions

## When NOT to Use

- Building detection rules or monitoring → `d3fend-detect`
- System hardening or encryption → `d3fend-harden`
- Honeypots or deception → `d3fend-deceive`
- Network architecture design → `infrastructure-engineer`
- Zero-trust implementation → `cybersecurity`

## Core Workflows

### 1. Access Mediation

| Type | Controls |
|---|---|
| Network | VLANs, ACLs, routing mediation, remote file access |
| Web Session | Proxy-based, endpoint-based mediation |
| File | Local permissions, access policy administration |
| Physical | Locks, badges, physical access mediation |
| System | System call filtering, I/O port restrictions |

**See `references/access_mediation.md`**

### 2. Content Filtering & Validation

- Content filtering (email, web, DLP)
- Content modification, excision, rebuild, substitution
- Format verification (magic bytes, metadata, internal structure)
- Decompression checking and quarantine

**See `references/content_filtering.md`**

### 3. Execution Isolation

- Application-based process isolation (containers, app sandbox)
- Kernel-based isolation (seccomp, namespaces, cgroups)
- Hardware-based isolation (TEE, TPM, enclaves)
- Executable allowlisting and denylisting

**See `references/execution_isolation.md`**

### 4. Network Isolation

- Broadcast domain isolation (VLANs, private VLANs)
- Directional network links (one-way gateways)
- DNS/IP allowlisting and denylisting
- Encrypted tunnels (VPN, TLS, IPsec)
- Traffic filtering (inbound, outbound, email)

**See `references/network_isolation.md`**

## When to load references

- **Access mediation** → `references/access_mediation.md`
- **Content filtering** → `references/content_filtering.md`
- **Execution isolation** → `references/execution_isolation.md`
- **Network isolation** → `references/network_isolation.md`
