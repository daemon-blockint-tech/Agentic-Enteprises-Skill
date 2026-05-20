---
name: YARA Rule Authoring
description: |
  Guides authoring, review, optimization, and false-positive debugging of YARA-X detection rules for
  malware identification across PE, script, npm, Office, Chrome extensions (crx module), and Android
  DEX (dex module). Covers string and atom quality, condition short-circuiting, legacy YARA migration,
  yarGen/FLOSS workflows, goodware validation, and production deployment—not full malware reverse
  engineering, network IDS (Suricata/Snort), or memory forensics (Volatility).
  Use when the user asks to write YARA rule, YARA-X, yr check, yr scan, false positive YARA, yarGen,
  malware detection rule, crx module, dex module, optimize YARA performance, or migrate legacy YARA.
---

# YARA Rule Authoring

Write YARA-X rules that catch the intended family without drowning analysts in false positives.

> **Target runtime:** YARA-X (Rust successor to legacy YARA). Install: `brew install yara-x` or `cargo install yara-x`. Essential CLI: `yr check`, `yr scan`, `yr fmt`, `yr dump`.

## When to Use

- Write, review, or optimize YARA-X rules for malware, hacktools, webshells, or supply-chain artifacts
- Convert IOCs or threat intel into maintainable signatures
- Debug false positives or tune `any of` / `all of` logic
- Migrate legacy YARA rules to YARA-X stricter validation
- Author Chrome extension (`crx`) or Android DEX (`dex`) module rules
- Prepare rulesets for production, YARA-CI, or VirusTotal retrohunt

## When NOT to Use

- Full malware reverse engineering, disassembly, or unpacker development → `reverse-engineer`
- Network intrusion detection (Suricata, Snort, Zeek) → network security / SOC tooling skills
- Memory forensics with Volatility or live RAM analysis → `digital-forensics-analyst`
- Hash-only blocklists with no pattern logic → use IOC lists or EDR hash feeds
- Enterprise security strategy, GRC, or audit evidence → `cybersecurity`, `compliance-engineer`
- Embedding YARA in CI/CD pipelines as the primary task → `devsecops`
- Adversarial LLM or application red team → `ai-redteam`

## Related skills

| Need | Skill |
|---|---|
| Security program, IR strategy, detection philosophy | `cybersecurity` |
| SIEM/EDR rules, logging, control implementation | `information-security-engineer` |
| Audit evidence, control mapping, CCM | `compliance-engineer` |
| Pipeline gates, artifact scanning, SBOM | `devsecops` |
| Binary RE, unpacking, patch diff | `reverse-engineer` |
| SOC alert triage and detection tuning (non-YARA) | `defensive-security-analyst`, `soc-analyst` |
| Proactive threat hunts and ATT&CK campaigns | `threat-hunter` |
| CTI briefs, IOC/TTP production | `cti-analyst` |
| Adversarial AI / prompt injection testing | `ai-redteam` |
| Disk imaging and forensic reports | `digital-forensics-analyst` |

## Core principles

1. **Atoms matter** — YARA extracts 4-byte subsequences for Aho-Corasick prefilter. Strings with repeated bytes, common sequences, or under 4 bytes force expensive bytecode verification on too many files.
2. **Family-specific, not category-generic** — "Detects ransomware" matches everything and nothing. Target identifiable mutexes, PDB paths, C2 paths, or structural markers for one family or campaign.
3. **Goodware before production** — Validate against ecosystem-appropriate clean corpus (VT goodware for PE; top npm packages for JS; marketplace extensions for CRX).
4. **Short-circuit cheap checks first** — `filesize` → magic bytes → strings → modules.
5. **Metadata is documentation** — Name, description, author, reference, and date survive personnel changes.

## Essential toolkit

| Tool | Purpose |
|---|---|
| **yarGen** | Candidate strings from samples (`--excludegood`); always `yr check` output |
| **FLOSS** | Obfuscated/stack strings when yarGen fails |
| **yr** | `yr check`, `yr scan -s`, `yr fmt`, `yr dump -m pe\|crx\|dex` |
| **YARA-CI / VT retrohunt** | Goodware corpus testing before deploy |

## Core workflows

### 1. Scope samples and file type

1. Collect **3+ variants** when possible (single-sample rules are brittle)
2. Check packing: entropy > 7.0 or few strings → unpack or target packer/structure, not encrypted layer
3. Choose platform path: PE magic / JS / Office ZIP / `import "crx"` / `import "dex"`

**See `references/yara_x_scope_and_tooling.md` for install, CLI workflow, and migration.**

### 2. Extract and filter strings

1. Run yarGen or FLOSS on unpacked samples
2. Reject ~80% of yarGen output: API names, `C:\Windows\`, format strings, `require`/`fetch` alone
3. Prefer gold tier: mutex names, PDB paths, stack strings; silver: C2 paths, config markers

**See `references/string_selection_and_atoms.md` for decision trees and modifiers.**

### 3. Write rule with ordered conditions

```yara
rule MAL_Win_Example_Loader_Jan26
{
    meta:
        description = "Detects Example loader via unique mutex and config path"
        author = "Team <team@example.com>"
        reference = "https://example.com/analysis"
        date = "2026-01-15"

    strings:
        $mutex = "Global\\ExampleMutex" ascii wide
        $cfg  = "/api/beacon/check" ascii

    condition:
        filesize < 10MB and
        uint16(0) == 0x5A4D and
        all of ($mutex, $cfg)
}
```

**Condition order:** `filesize` → magic bytes → string matches → module calls (`pe`, `crx`, `dex`).

**See `references/conditions_and_performance.md` for atom theory, regex bounds, and loops.**

### 4. Validate and test

```bash
yr check rule.yar && yr fmt -w rule.yar
yr scan -s rule.yar malware_samples/    # must match all targets
yr scan -c rule.yar goodware_corpus/    # must be zero
```

**FP flow:** `yr scan -s` on false positive → identify matching string → tighten, exclude vendor, or pivot to structure.

**See `references/testing_goodware_and_fp_debugging.md` for corpus selection and investigation.**

### 5. Platform modules (when applicable)

- **Chrome extensions:** `import "crx"` — permissions, `permhash()` (v1.11.0+). Always `crx.is_crx` first.
- **Android:** `import "dex"` — `dex.contains_class()`, `contains_method()`, `contains_string()`. API differs from legacy YARA dex module.

**See `references/platform_modules_pe_crx_dex.md`.**

### 6. Deploy

1. Naming: `{CATEGORY}_{PLATFORM}_{FAMILY}_{VARIANT}_{DATE}` (e.g. `MAL_Win_Emotet_Loader_Jan26`)
2. Peer review + quality checklist
3. Monitor production FPs; version rules in Git with full metadata

**See `references/style_metadata_and_deployment.md`.**

## Decision trees (quick reference)

### Is this string good enough?

```
< 4 bytes? → reject
Repeated bytes (0000, 9090)? → reject
API name or common path? → reject
Unique to family? → use
Common across malware? → combine with family-specific marker
```

### `any of` vs `all of`

- Individually unique strings → `any of ($a*)`
- Common strings that are suspicious only together → `all of ($a*)`
- Mixed confidence → `all of ($core_*) and any of ($variant_*)`

Production lesson: `any of ($network_*)` with `fetch`, `axios`, `http` matches most web apps — require credential path **and** exfil destination **and** network call.

### When strings fail → pivot

Use `yr dump -m pe` for sections, imports, imphash, resources; `math.entropy()` on sections; packer signatures. If nothing unique remains, YARA alone may not be the right control.

## Legacy YARA migration

```bash
yr check --relaxed-re-syntax rules/   # diagnostic only
yr check rules/                       # fix until clean
```

Common fixes: escape `\{` in regex; base64 strings need 3+ chars; `@a[-1]` → `@a[#a - 1]`; remove duplicate modifiers.

## Rationalizations to reject

| Thought | Reality |
|---|---|
| "yarGen gave me these strings" | yarGen suggests; you validate each string |
| "It works on 10 samples" | Test goodware corpus before deploy |
| "I'll tighten after FPs" | FPs burn trust — write tight rules upfront |
| "This API name is malicious" | Legitimate software uses the same APIs |
| "any of them is fine" | Common strings + `any` = FP flood |

## Quality checklist

- [ ] Name follows `{CATEGORY}_{PLATFORM}_{FAMILY}_{VARIANT}_{DATE}`
- [ ] Description starts with "Detects" and states distinguishing feature
- [ ] Required meta: author, reference, date
- [ ] Strings ≥4 bytes with good atoms; no unbounded regex (`.*`)
- [ ] Condition: `filesize` and magic bytes before modules
- [ ] Matches all target samples; **zero** goodware matches
- [ ] `yr check` and `yr fmt --check` pass
- [ ] Peer review completed

## When to load references

| Topic | Reference |
|---|---|
| YARA-X install, CLI, migration, toolkit | `references/yara_x_scope_and_tooling.md` |
| String quality, types, modifiers | `references/string_selection_and_atoms.md` |
| Atoms, condition order, regex, loops | `references/conditions_and_performance.md` |
| PE, macOS, JS, crx, dex patterns | `references/platform_modules_pe_crx_dex.md` |
| Goodware testing, FP debugging | `references/testing_goodware_and_fp_debugging.md` |
| Naming, metadata, deployment | `references/style_metadata_and_deployment.md` |
