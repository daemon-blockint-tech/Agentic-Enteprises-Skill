# Style, Metadata, and Deployment

## Table of contents

1. [Naming convention](#naming-convention)
2. [Category prefixes](#category-prefixes)
3. [Required metadata](#required-metadata)
4. [Optional metadata](#optional-metadata)
5. [Rule structure](#rule-structure)
6. [Deployment practices](#deployment-practices)
7. [Common mistakes](#common-mistakes)

## Naming convention

```
{CATEGORY}_{PLATFORM}_{FAMILY}_{VARIANT}_{DATE}
```

| Component | Examples |
|---|---|
| CATEGORY | `MAL`, `HKTL`, `WEBSHELL`, `EXPL`, `SUSP`, `GEN` |
| PLATFORM | `Win`, `Lnx`, `Mac`, `Android`, `CRX`, `Multi` |
| FAMILY | `Emotet`, `CobaltStrike`, `LockBit` |
| VARIANT | `Loader`, `Beacon`, `Config` |
| DATE | `Jan26`, `May25` (MonthYear) |

**Good:** `MAL_Win_Emotet_Loader_Jan26`, `SUSP_CRX_HighRiskPerms_Jan26`

**Bad:** `malware_detector`, `rule1`, `EMOTET_RULE` (missing category/platform/date)

### Optional classifiers

Append when relevant: `APT_`, `CRIME_`, `RANSOM_`, `RAT_`, `MINER_`, `STEALER_`, `LOADER_`, `C2_`

## Category prefixes

| Prefix | Meaning | When |
|---|---|---|
| `MAL_` | Confirmed malware | Verified malicious |
| `HKTL_` | Hacking tool | Dual-use (Mimikatz, CS) |
| `WEBSHELL_` | Web shell | PHP/ASP/JSP backdoors |
| `EXPL_` | Exploit | Exploit code/shellcode |
| `SUSP_` | Suspicious | Lower confidence; expect tuning |
| `PUA_` | Potentially unwanted | Adware, bundleware |
| `GEN_` | Generic | Broad category; high FP risk |

Use `SUSP_` when description would say "might be" — confidence belongs in the prefix, not vague metadata.

## Required metadata

```yara
meta:
    description = "Detects Emotet loader via unique mutex and C2 path"
    author = "Team Name <team@example.com>"
    reference = "https://example.com/analysis-report"
    date = "2026-01-15"
```

### Description rules

- Start with **"Detects"**
- 60–400 characters
- State **what** and **how** (distinguishing feature)

```yara
// Good
description = "Detects CobaltStrike beacon via watermark bytes in PE overlay"

// Bad
description = "Malware"
description = "This rule detects..."
description = "Might be malware"   // use SUSP_ prefix instead
```

## Optional metadata

```yara
meta:
    hash = "sha256:abc123..."
    hash = "sha256:def456..."    // repeatable field
    score = 75
    malware_type = "trojan"
    tlp = "white"
    comment = "FP fix 2026-02: excluded VendorX updater path"
```

Use `comment` for FP history and tuning notes.

## Rule structure

```yara
rule MAL_Win_Example_Loader_Jan26
{
    meta:
        description = "Detects Example loader via mutex and config path"
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

**String prefixes:** group related strings (`$a*`, `$b*`, `$network_*`) for readable conditions.

**Private helpers (YARA-X 1.3.0+):**

```yara
private $helper = "internal_marker"
```

## Deployment practices

1. **Repository layout** — group by platform or campaign; avoid monolithic unnamed files
2. **Pre-merge gates** — `yr check`, goodware scan, peer review
3. **Versioning** — Git tags for ruleset releases; changelog for FP fixes
4. **Monitoring** — track match rate and analyst dismissals per rule ID
5. **Retirement** — deprecate rules that FP persistently; document in commit message

### Production quality bar

| Check | Requirement |
|---|---|
| Naming | Full convention with date |
| Metadata | All required fields |
| Testing | 100% malware set, 0 goodware |
| Performance | `filesize` + magic before modules |
| Documentation | Reference URL to analysis |

## Common mistakes

| Mistake | Bad | Good |
|---|---|---|
| API as indicator | `"VirtualAlloc"` | Hex at call site + unique mutex |
| Unbounded regex | `/https?:\/\/.*/` | Bounded charset and length |
| No file filter | `pe.imports(...)` first | `uint16(0)==0x5A4D and filesize...` |
| Short strings | `"abc"` | 4+ bytes |
| Unescaped braces (YARA-X) | `/config{key}/` | `/config\{key\}/` |
| Generic description | `"Malware"` | "Detects X via Y" |
