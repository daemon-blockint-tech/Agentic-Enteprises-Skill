---
name: d3fend-deceive
description: |
  Guides cybersecurity deception operations using MITRE D3FEND—honeynets, decoy objects,
  decoy personas, and decoy credentials. Covers honeypot deployment, decoy file planting,
  credential baiting, and deception environment design. Use when deploying honeypots,
  planting decoy data, baiting credentials, or designing deception programs—not for
  detection (d3fend-detect), hardening (d3fend-harden), or isolation (d3fend-isolate).
---

# D3FEND — Deceive

## When to Use

- Deploying honeynets (connected, integrated, standalone)
- Planting decoy objects (files, network resources, personas)
- Distributing decoy credentials and session tokens
- Publishing decoy information (fake releases, personas)
- Designing deception programs and adversary engagement
- Monitoring deception environment for adversary interaction

## When NOT to Use

- Building detection rules or SIEM content → `d3fend-detect`
- System hardening or secure config → `d3fend-harden`
- Network segmentation → `d3fend-isolate`
- Active defense / threat intel → `cybersecurity`
- Adversarial testing (red team) → `ai-redteam` / `offensive-security-analyst`

## Core Workflows

### 1. Decoy Environments (Honeynets)

| Type | Deployment | Use Case |
|---|---|---|
| Standalone | Isolated network segment | Research, early warning |
| Integrated | Blended with production | Insider threat, lateral movement |
| Connected | Linked to real systems | APT detection, TTP collection |

**See `references/honeynets.md`**

### 2. Decoy Objects

- **Decoy files**: Fake documents with tracking (canary tokens)
- **Decoy network resources**: Fake shares, databases, services
- **Decoy personas**: Fake user accounts with believable data
- **Decoy public releases**: Fake credentials on dark web/pastebin
- **Decoy session tokens**: Bait cookies/API keys with monitoring

**See `references/decoy_objects.md`**

### 3. Deception Program Design

1. Define objectives (detection, delay, intelligence)
2. Select deception layers (environment, object, persona)
3. Ensure believability and consistency
4. Monitor and collect adversary TTPs
5. Analyze and feed into threat intelligence

**See `references/deception_program.md`**

## When to load references

- **Honeynets** → `references/honeynets.md`
- **Decoy objects** → `references/decoy_objects.md`
- **Deception program** → `references/deception_program.md`
