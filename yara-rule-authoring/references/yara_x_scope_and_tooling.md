# YARA-X Scope and Tooling

## Table of contents

1. [Why YARA-X](#why-yara-x)
2. [Install and CLI](#install-and-cli)
3. [Development cycle](#development-cycle)
4. [yr dump for exploration](#yr-dump-for-exploration)
5. [Legacy migration](#legacy-migration)
6. [YARA-X features](#yara-x-features)
7. [External resources](#external-resources)

## Why YARA-X

YARA-X is the Rust-based successor to legacy YARA. It powers VirusTotal production scanning and is the recommended runtime for new rules.

| Capability | Benefit |
|---|---|
| Regex engine | 5–10× faster on regex-heavy rules |
| Validation | Stricter errors with precise source locations |
| Formatter | `yr fmt` for consistent style |
| Modules | `crx`, `dex` (new); improved PE/ELF/Mach-O |
| Compatibility | ~99% legacy rule compatibility after fixes |

**Scope of this skill:** rule authoring, review, optimization, FP debugging, and deployment—not malware RE, network IDS, or memory forensics.

## Install and CLI

```bash
# macOS
brew install yara-x

# From source
cargo install yara-x

# Verify
yr --version
```

| Command | Purpose |
|---|---|
| `yr check rule.yar` | Syntax and semantic validation |
| `yr check rules/` | Validate directory |
| `yr fmt -w rule.yar` | Format in place |
| `yr scan rule.yar /path/to/files` | Scan corpus |
| `yr scan -s rule.yar file` | Show matching strings |
| `yr scan -c rule.yar corpus/` | Count matches only |
| `yr dump -m pe sample.exe` | Inspect module fields (YAML/JSON) |

## Development cycle

```
Write rule → yr check → yr fmt → yr dump (if using modules)
    → scan malware set (must match) → scan goodware (must be zero)
    → peer review → deploy
```

**Timing:** `time yr scan -s rule.yar corpus/` to spot slow rules before production.

**Diagnostic advantage:** When `yr check` reports line 15, the issue is on line 15—unlike legacy YARA's imprecise regex errors.

## yr dump for exploration

Use before writing module-heavy conditions:

```bash
yr dump -m pe sample.exe --output-format yaml
yr dump -m math sample.exe --output-format yaml | grep entropy
yr dump -m crx extension.crx --output-format yaml
yr dump -m dex classes.dex --output-format yaml
```

Shows exactly what modules expose—imports, sections, permissions, DEX classes—without writing throwaway rules.

## Legacy migration

```bash
# Step 1: find issues (diagnostic only)
yr check --relaxed-re-syntax rules/

# Step 2: fix each issue
# Step 3: strict validation
yr check rules/
```

| Issue | Legacy behavior | YARA-X fix |
|---|---|---|
| Literal `{` in regex | Often accepted | Escape: `/config\{key\}/` |
| Invalid escapes | Silent literal | Fix escape or use valid class |
| Base64 modifier | Any length | String must be 3+ characters |
| Negative string index | `@a[-1]` | `@a[#a - 1]` |
| Duplicate modifiers | Allowed | Remove duplicate |

**Do not** ship rules that only pass under `--relaxed-re-syntax`.

## YARA-X features

| Feature | Version | Usage |
|---|---|---|
| Private patterns | 1.3.0+ | `private $helper = "x"` — matches, hidden from output |
| Warning suppression | 1.4.0+ | `// suppress: slow_pattern` inline |
| Numeric underscores | 1.5.0+ | `filesize < 10_000_000` |
| NDJSON output | — | `yr scan --output-format ndjson` for pipelines |
| `crx` module | 1.5.0+ | Chrome extensions |
| `dex` module | 1.11.0+ | Android DEX (new API, not legacy-compatible) |

## External resources

| Resource | Purpose |
|---|---|
| [Neo23x0/signature-base](https://github.com/Neo23x0/signature-base) | Production rule examples |
| [Elastic/protections-artifacts](https://github.com/elastic/protections-artifacts) | Endpoint-tested rules |
| [YARA Style Guide](https://github.com/Neo23x0/YARA-Style-Guide) | Naming and metadata |
| [YARA Performance Guidelines](https://github.com/Neo23x0/YARA-Performance-Guidelines) | Atoms and regex |
| [yarGen](https://github.com/Neo23x0/yarGen) | String extraction |
| [FLOSS](https://github.com/mandiant/flare-floss) | Obfuscated strings |
| [YARA-CI](https://yara-ci.cloud.virustotal.com/) | Automated goodware testing |
