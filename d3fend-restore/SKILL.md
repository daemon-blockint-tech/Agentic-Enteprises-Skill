---
name: d3fend-restore
description: |
  Guides cybersecurity restoration using MITRE D3FEND—recovering access, objects, configurations,
  and systems after incidents. Covers credential reissuance, account unlocking, file restoration,
  database recovery, configuration rebuild, and software reinstallation. Use after incident
  containment for business continuity, disaster recovery, and return to normal operations—not
  for incident containment (d3fend-evict), detection (d3fend-detect), or hardening (d3fend-harden).
---

# D3FEND — Restore

## When to Use

- Restoring user access after incident containment (reissue credentials, unlock accounts)
- Recovering files, databases, and configurations from backup
- Rebuilding systems from disk images or clean baselines
- Restoring email and software after malware removal
- Validating restored systems before returning to production
- Documenting recovery actions for post-incident review

## When NOT to Use

- Active incident containment or eviction → `d3fend-evict`
- Detection engineering or monitoring → `d3fend-detect`
- Hardening to prevent future incidents → `d3fend-harden`
- Backup strategy design → `infrastructure-engineer`
- Business continuity planning → `cybersecurity`

## Core Workflows

### 1. Restore Access

| Action | Steps |
|---|---|
| Reissue credential | Generate new token/cert/password; distribute securely |
| Unlock account | Verify identity; reset MFA if compromised |
| Restore network access | Re-enable firewall rules; verify no persistence |
| Restore user account access | Validate AD/Azure AD; check group memberships |

**See `references/restore_access.md`**

### 2. Restore Objects

- Restore file (from backup, shadow copy, or clean source)
- Restore email (from archive or backup)
- Restore database (point-in-time recovery, transaction log replay)
- Restore disk image (bare metal restore, VM snapshot)
- Restore configuration (from version control or backup)

**See `references/restore_objects.md`**

### 3. Restore Software & Systems

- Reinstall software from trusted source
- Rebuild system from hardened gold image
- Verify integrity (hash check, signature validation)
- Re-apply patches and updates
- Re-run vulnerability scan before rejoining network

**See `references/restore_systems.md`**

## When to load references

- **Restore access** → `references/restore_access.md`
- **Restore objects** → `references/restore_objects.md`
- **Restore systems** → `references/restore_systems.md`
