# Conditions and Performance

## Table of contents

1. [How scanning works](#how-scanning-works)
2. [Condition ordering](#condition-ordering)
3. [Slow pattern killers](#slow-pattern-killers)
4. [Regex and loops](#regex-and-loops)
5. [Modules vs raw bytes](#modules-vs-raw-bytes)
6. [Platform short-circuits](#platform-short-circuits)
7. [Optimization checklist](#optimization-checklist)

## How scanning works

Three phases:

1. **Atom extraction** — 4-byte subsequences from strings/hex
2. **Aho-Corasick** — fast multi-pattern atom search
3. **Bytecode verification** — full string/condition evaluation per hit

**Goal:** maximize Phase 2 selectivity so Phase 3 runs rarely.

### Good atoms

- Rare in target file types
- No wildcards in the 4-byte window
- Not common PE/JS noise (`MZ`, `This program`, `http`)

```
String: "MalwareConfig"  → atom "Malw"
String: { 4D 5A ?? ?? 50 45 } → limited atom options due to wildcards
```

## Condition ordering

Always order from cheapest to most expensive:

```yara
condition:
    filesize < 10MB and                    // 1. Instant
    uint16(0) == 0x5A4D and                // 2. Magic bytes
    all of ($core_*) and                   // 3. Strings (if good atoms)
    pe.imports("kernel32.dll", "Sleep") and // 4. Module (moderate)
    pe.imphash() == "abc123..."            // 5. Expensive hashes
```

Failed cheap checks skip expensive work.

**Rule of thumb:** If the condition block exceeds ~5 lines of logic, consider splitting into focused rules.

## Slow pattern killers

| Anti-pattern | Why | Fix |
|---|---|---|
| Strings < 4 bytes | No useful atoms | Lengthen or use hex with context |
| `{ 90 90 90 90 }` NOP sleds | Atom `9090` everywhere | Add surrounding opcode context |
| `/https?:\/\/.*/` | Unbounded regex | Bound length and charset |
| Leading wildcards `{ ?? ?? 4D 5A }` | Unstable atoms | Put fixed bytes first |
| `nocase` on common strings | Doubles atoms | Remove or narrow string |
| Module call without file filter | Parses non-target files | Magic bytes + `filesize` first |

## Regex and loops

### Regex rules

- Bound repetitions: `.{0,30}` not `.*`
- Anchor to distinctive literals
- Validate with `yr check` (YARA-X strict escapes)

### Loops

```yara
// GOOD: bound by filesize and index range
filesize < 100KB and
for all i in (1..#a) : ( @a[i] < 1000 )

// BAD: unbounded #a on large files
for all i in (1..#a) : ( ... )
```

## Modules vs raw bytes

```
Need imphash, authenticode, rich header?
  → PE module (too complex to hand-parse)

Only magic bytes or simple offsets?
  → uint16/uint32 — faster, no module load

Chrome extension permissions?
  → crx module — fragile to parse manifest as strings

LNK target paths?
  → lnk module
```

**Principle (Neo23x0):** If `uint32()` suffices, do not load a module.

## Platform short-circuits

| Platform | Pattern |
|---|---|
| Windows PE | `filesize < 10MB and uint16(0) == 0x5A4D` |
| Mach-O 64 | `uint32(0) == 0xFEEDFACF` |
| Universal binary | `uint32(0) == 0xCAFEBABE or uint32(0) == 0xBEBAFECA` |
| OOXML | `uint32(0) == 0x504B0304` |
| JavaScript | `filesize < 1MB` (no magic) |
| Chrome CRX | `crx.is_crx` |
| Android DEX | `dex.is_dex` |

## Optimization checklist

- [ ] `filesize` limit appropriate for file type
- [ ] Magic bytes or `crx.is_crx` / `dex.is_dex` before modules
- [ ] All strings ≥ 4 bytes with non-trivial atoms
- [ ] No unbounded regex; braces escaped for YARA-X
- [ ] `nocase` / `wide` only with sample evidence
- [ ] Loops bounded by `filesize` and index range
- [ ] `time yr scan` acceptable on representative corpus
- [ ] Split mega-rules into family-specific rules if still slow
