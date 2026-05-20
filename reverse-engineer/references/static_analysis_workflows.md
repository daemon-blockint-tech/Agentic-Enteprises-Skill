# Static analysis workflows

## Table of contents

1. [Triage and identification](#triage-and-identification)
2. [Disassembly workflow](#disassembly-workflow)
3. [Decompilation and structures](#decompilation-and-structures)
4. [Cross-references and data flow](#cross-references-and-data-flow)
5. [Automation and scripting](#automation-and-scripting)
6. [Quality bar for notes](#quality-bar-for-notes)

## Triage and identification

1. Record **SHA-256**, file size, and source (ticket, URL, attachment policy)
2. Identify format: `file`, magics, `binwalk` for firmware containers
3. Note architecture, bitness, endianness, OS ABI (PE/ELF/Mach-O)
4. Run **strings** (ASCII/UTF-16) and entropy scan; flag packed/obfuscated regions
5. Check signatures (AV, YARA, imphash) for known families—do not trust labels alone

Document packer/compiler hints; plan unpacking only in lab with authorization.

## Disassembly workflow

```
load → auto-analyze → define entry → rename symbols → annotate calls → export IDB/project
```

- Prefer **one primary tool** per engagement (Ghidra, IDA, Binary Ninja, radare2)
- Set correct **processor module** and calling convention
- Resolve **imports/exports**; mark thunk and PLT/GOT where relevant
- Rename functions by **behavior** once understood (`parse_config`, `send_beacon`)
- Add **comments** at decision points with evidence (string xref, API name)

For firmware: locate vector table, identify bootloader vs application segments.

## Decompilation and structures

- Validate decompiler output against **disassembly** at hot paths
- Define **structs** and enums from sizeof checks, field access patterns, and known formats
- Recover **vtable** layouts for C++ when object lifecycle matters
- Map **crypto** calls to libraries (OpenSSL, mbedTLS, custom)—do not claim weakness without proof
- Track **global state** and singletons that affect exploitability narratives

## Cross-references and data flow

- Start from **interesting strings**, imports (`CreateRemoteThread`, `VirtualProtect`, `socket`), and exports
- Build **xref graphs** for credential parsing, network send, file write, registry keys
- Trace **user input** to dangerous sinks (copy, format, command execution) for vuln reports
- Use **graph views** for complex state machines (protocol parsers, dispatch tables)
- Mark **dead code** and anti-analysis tricks separately from core logic

## Automation and scripting

- Export **function lists**, strings, and call graphs for diff baselines
- Use headless Ghidra (`ghidra-headless` skill if installed) for batch on many builds
- Script **signature generation** at stable byte sequences; avoid overfitting relocations
- Version-control **project files** or export scripts—not necessarily the binary itself

## Quality bar for notes

Every finding should include:

- **Location** — function name/address/offset, module version
- **Evidence** — xref, API, decompiler snippet reference
- **Confidence** — confirmed vs likely vs speculative
- **Impact hook** — what an attacker or defender should care about
- **Next step** — dynamic validation, patch diff, or detection idea
