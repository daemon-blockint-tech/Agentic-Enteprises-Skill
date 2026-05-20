# Platform Modules: PE, CRX, DEX

## Table of contents

1. [Windows PE](#windows-pe)
2. [macOS Mach-O](#macos-mach-o)
3. [JavaScript and Office](#javascript-and-office)
4. [Chrome extensions (crx)](#chrome-extensions-crx)
5. [Android DEX (dex)](#android-dex-dex)
6. [When strings fail](#when-strings-fail)

## Windows PE

**Short-circuit:**

```yara
condition:
    filesize < 10MB and
    uint16(0) == 0x5A4D and
    ...
```

**Good PE indicators:** unique mutex, PDB path, overlay watermark, rare section names combined with strings.

**Avoid:** `pe.imports()` alone on common APIs; imphash without family context unless clustered.

**Explore:**

```bash
yr dump -m pe sample.exe --output-format yaml
```

## macOS Mach-O

No dedicated Mach-O module—use magic bytes plus strings:

```yara
// Mach-O 64-bit
uint32(0) == 0xFEEDFACF
// Universal (fat) binary
uint32(0) == 0xCAFEBABE or uint32(0) == 0xBEBAFECA
```

**Useful strings:** LaunchAgents paths, `CGEventTapCreate`, `security find-generic-password`, SSH tunnel messages.

**Example pattern (multi-category):**

```yara
rule SUSP_Mac_ProtonRAT
{
    strings:
        $lib1 = "SRWebSocket" ascii
        $lib2 = "SocketRocket" ascii
        $beh1 = "SSH tunnel not launched" ascii
        $beh2 = "Keylogger" ascii
    condition:
        (uint32(0) == 0xFEEDFACF or uint32(0) == 0xCAFEBABE) and
        any of ($lib*) and any of ($beh*)
}
```

## JavaScript and Office

| Target | Filter | Notes |
|---|---|---|
| npm / Node | `filesize < 1MB`, package.json markers | Avoid lone `postinstall` |
| VS Code ext | Uncommon `activationEvents`, hidden file access | Not `vscode.workspace` alone |
| OOXML | `uint32(0) == 0x504B0304` | Macro auto-exec strings, not generic VBA keywords |

**JS decision tree:** see `string_selection_and_atoms.md`.

## Chrome extensions (crx)

**Requires:** YARA-X v1.5.0+ (`permhash()` v1.11.0+)

```yara
import "crx"

rule SUSP_CRX_Debugger
{
    condition:
        crx.is_crx and
        for any perm in crx.permissions : (perm == "debugger")
}
```

### Key fields

| Field | Use |
|---|---|
| `crx.is_crx` | **Always first** |
| `crx.permissions` | High-risk: `debugger`, `nativeMessaging`, `<all_urls>` |
| `crx.host_permissions` | MV3 host access |
| `crx.permhash()` | Permission-set clustering (v1.11.0+) |
| `crx.signatures[].verified` | Signature state |

### Red-flag combinations

- `nativeMessaging` + broad host access → local binary bridge + web reach
- `webRequest` + `webRequestBlocking` + `cookies` → interception/theft potential
- `debugger` on non-dev extensions → full traffic visibility

```bash
yr dump -m crx extension.crx --output-format yaml
```

## Android DEX (dex)

**Requires:** YARA-X v1.11.0+

**Important:** YARA-X `dex` API is **not** compatible with legacy YARA's dex module—rewrite rules.

```yara
import "dex"

rule SUSP_DEX_DynamicLoading
{
    condition:
        dex.is_dex and
        dex.contains_class("Ldalvik/system/DexClassLoader;")
}
```

### Key APIs

| API | Purpose |
|---|---|
| `dex.is_dex` | File type gate |
| `dex.contains_string(pat)` | String search |
| `dex.contains_class(pat)` | Class descriptor search |
| `dex.contains_method(pat)` | Method name search |
| `dex.header.*` | Version, checksum, signature |
| `dex.checksum()` / `dex.signature()` | Tamper detection vs header |

### Red flags

- Single-letter class names (obfuscation)
- `DexClassLoader` / reflection loaders
- Encrypted asset references combined with dynamic load
- Checksum mismatch vs header

```bash
yr dump -m dex classes.dex --output-format yaml
```

## When strings fail

```
String extraction failed?
├─ High entropy sections → math.entropy() on section
├─ Import patterns → pe.imphash() clustering
├─ PE structure → section names, sizes, characteristics
├─ CRX → crx.permissions / permhash()
├─ DEX → dex.contains_class / method patterns
└─ Nothing unique → consider other controls (hash, behavior, sandbox)
```

**Packed samples:** entropy > 7.0 or very few strings → unpack first or detect packer, not encrypted payload strings.
