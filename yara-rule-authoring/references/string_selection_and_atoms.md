# String Selection and Atoms

## Table of contents

1. [Quality checklist](#quality-checklist)
2. [Value tiers](#value-tiers)
3. [String types](#string-types)
4. [Modifiers and cost](#modifiers-and-cost)
5. [Reject list](#reject-list)
6. [Hex vs text vs regex](#hex-vs-text-vs-regex)
7. [JavaScript and supply chain](#javascript-and-supply-chain)
8. [Multi-category grouping](#multi-category-grouping)

## Quality checklist

Before adding any string:

```
Is this string good enough?
├─ At least 4 bytes?
├─ Four consecutive non-trivial bytes (not 0000, 9090, FFFF)?
├─ NOT an API name (VirtualAlloc, CreateRemoteThread)?
├─ NOT a common path (C:\Windows\, cmd.exe)?
├─ NOT a format string (%s, Error: %s)?
├─ Would match Windows system or ecosystem goodware?
│  └─ YES → reject or add exclusion
├─ Unique to this malware family?
│  └─ YES → use
└─ Shared across malware families?
   └─ MAYBE → combine with family-specific marker
```

**Expert heuristic:** If you need more than ~6 strings, you are likely over-fitting one sample.

## Value tiers

| Tier | Examples | Notes |
|---|---|---|
| **Gold** | Mutex names, stack strings, PDB paths | Almost always unique |
| **Silver** | C2 paths, config markers, custom protocol headers | Usually unique |
| **Bronze** | Campaign IDs, rare error messages | Require combination with gold/silver |

**yarGen output:** Expect to discard ~80% of suggested strings after manual review.

## String types

### Text

```yara
$s = "Hello World"              // ASCII (default)
$s = "Hello" wide               // UTF-16LE
$s = "Hello" ascii wide         // Either encoding
$s = "hello" nocase             // Doubles atoms — use only when proven necessary
$s = "token" fullword           // Word boundaries
```

### Hex

```yara
$h = { 4D 5A 90 00 }            // Exact
$w = { 4D 5A ?? ?? 50 45 }      // Single-byte wildcards
$j = { 4D 5A [2-4] 50 45 }      // Bounded jump — always bound jumps
$a = { 4D 5A ( 90 00 | 00 00 ) } // Alternatives
```

Prefer hex over regex when the pattern is fixed bytes.

### Regular expressions

```yara
// GOOD: bounded
$url = /https?:\/\/[a-z0-9]{5,50}\.onion/

// BAD: unbounded — catastrophic backtracking
$bad = /https?:\/\/.*/
```

**YARA-X:** Escape literal braces: `/config\{key\}/`. Run `yr check` on every regex.

**Anchoring:** Regex without a 4+ byte literal substring may evaluate at every offset. Anchor to a distinctive literal: `/mshta\.exe http:\/\/.../` not `/http:\/\/.../` alone.

## Modifiers and cost

| Modifier | Cost | When to use |
|---|---|---|
| `ascii` | None | Default |
| `wide` | Low | Confirmed UTF-16 in samples |
| `nocase` | **Doubles atoms** | Confirmed case variance only |
| `fullword` | Low | Avoid substring FP |
| `xor(0x00-0xFF)` | **Very high** | Almost never — find real encoding |
| `xor(0x41)` | Moderate | Known single-byte key |
| `base64` | Moderate | Payload encoding; **3+ chars in YARA-X** |
| `private` | None | Helper patterns (YARA-X 1.3.0+) |

> Kaspersky Applied YARA: do not use `nocase` or `wide` without evidence they vary in your corpus.

## Reject list

### API names (PE)

```yara
// REJECT — present in most executables
"VirtualAlloc", "CreateRemoteThread", "WriteProcessMemory", "NtCreateThreadEx"
```

Use hex at call sites plus behavioral strings, not import names alone.

### Common paths and binaries

```yara
// REJECT
"C:\\Windows\\System32", "cmd.exe", "powershell.exe", "\\AppData\\Local"
```

### Format strings

```yara
// REJECT
"%s", "%d", "Error: %s"
```

Prefer unique messages: `"Beacon initialized: %s:%d with key %08X"`.

### JavaScript (npm/browser)

```yara
// REJECT alone
"require", "fetch", "axios", "Buffer", "crypto", "process.env"
```

Require combinations: specific env var names + exfil URL + suspicious hook.

## Hex vs text vs regex

| Need | Use |
|---|---|
| Exact ASCII/Unicode | Text with `ascii` / `wide` |
| Fixed byte sequence | Hex |
| Variation in bytes | Hex with `??` or bounded jumps |
| Structured text (URL, path) | Bounded regex |
| Unknown XOR layer | Avoid broad `xor(0x00-0xFF)`; unpack or narrow key |

## JavaScript and supply chain

```
Writing a JavaScript rule?
├─ npm package? → package.json hooks, postinstall, exfil + env access
├─ Browser extension? → crx module (Chrome) or manifest strings
├─ Standalone JS? → obfuscation markers (_0x, eval+atob chains)
└─ Bundled/minified? → URLs, magic constants (not mangled identifiers)
```

**Good JS indicators:** ERC-20 selectors `{ 70 a0 82 31 }`, zero-width steganography bytes, campaign-specific domains.

## Multi-category grouping

```yara
strings:
    $lib1 = "SRWebSocket" ascii
    $lib2 = "SocketRocket" ascii
    $beh1 = "SSH tunnel" ascii
    $beh2 = "keylogger" ascii nocase

condition:
    filesize < 10MB and
    (uint32(0) == 0xFEEDFACF or uint32(0) == 0xCAFEBABE) and
    any of ($lib*) and any of ($beh*)
```

Require evidence from **multiple** indicator classes when single categories are weak alone.
