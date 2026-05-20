# Testing, Goodware, and FP Debugging

## Table of contents

1. [Testing philosophy](#testing-philosophy)
2. [Validation workflow](#validation-workflow)
3. [Goodware corpora](#goodware-corpora)
4. [Interpreting matches](#interpreting-matches)
5. [False positive investigation](#false-positive-investigation)
6. [Sample coverage](#sample-coverage)
7. [CI and retrohunt](#ci-and-retrohunt)

## Testing philosophy

Every production rule requires three validations:

| Stage | Pass criteria |
|---|---|
| **Positive** | Matches all intended malware samples / variants |
| **Negative** | Zero matches on ecosystem goodware |
| **Edge** | Handles packing, older variants, related families without broad FPs |

Untested rules cause alert fatigue (FP) or missed detections (FN).

## Validation workflow

```
Write rule
  → yr check (fix until clean)
  → yr fmt --check
  → scan malware set (widen if misses)
  → scan goodware (tighten if hits)
  → peer review
  → deploy + monitor FPs
```

```bash
yr check rule.yar
yr fmt -w rule.yar
yr scan -s rule.yar malware_samples/
yr scan -c rule.yar goodware_corpus/   # expect 0
```

**Migration:** `yr check --relaxed-re-syntax` is diagnostic only—fix issues, do not depend on relaxed mode in production.

## Goodware corpora

VT goodware is PE-heavy. Supplement for your target:

| Rule target | Minimum goodware |
|---|---|
| PE | VT goodware; Chrome, Firefox, Office, Python installer |
| JavaScript | lodash, react, express, webpack, electron |
| npm | Top 100 weekly downloads + packages with postinstall scripts |
| Chrome CRX | Top marketplace extensions by installs |
| Android DEX | Popular benign APKs from trusted vendors |

**Expert baseline (Kaspersky Applied YARA):** include Chrome, Firefox, and Adobe Reader for PE rules.

## Interpreting matches

```
Goodware matches?
├─ 1–2 files → investigate; exclusion or tighten string
├─ 3–5 files → pattern too common; new indicators
├─ 6+ files → rule fundamentally broken; restart
└─ Single vendor only → not $fp_vendor or replace string
```

### VirusTotal retrohunt

1. Upload rule to VT Intelligence hunting
2. Run against **Goodware** corpus
3. Treat every match as potential FP until explained

| VT goodware matches | Action |
|---|---|
| 0 | Proceed toward deploy |
| 1–2 | Review, exclude or tighten |
| 3–5 | Replace indicators |
| 6+ | Rewrite approach |

### yarGen goodware DB

```bash
python db-lookup.py -f strings.txt   # yarGen install path
```

Query candidate strings before committing to a rule.

## False positive investigation

```
FP reported
  │
  ├─ 1. yr scan -s rule.yar false_positive.file
  │      Which string(s) matched?
  │
  ├─ 2. Legitimate library/vendor?
  │      → not $fp_vendor_string
  │
  ├─ 3. Common dev pattern?
  │      → replace with more specific indicator
  │
  ├─ 4. Multiple weak strings via any of?
  │      → switch to all of + unique marker
  │
  └─ 5. Technique-level only (e.g. "uses VirtualAlloc")?
         → target family-specific implementation detail
```

**Document FP fixes** in rule changelog or meta `comment` field—future maintainers need context.

## Sample coverage

| Samples | Confidence | Use case |
|---|---|---|
| 1 | Low (fragile) | Emergency hunt; refine quickly |
| 3–5 | Medium | Standard family rule |
| 10+ | High | Long-lived production rule |

**Gather variants:** imphash/ssdeep pivot on VT, C2/mutex pivot, campaign time window, unpack siblings.

**Packed check:**

```bash
yr dump -m math sample.exe --output-format yaml | grep entropy
strings sample.exe | wc -l
```

| Signal | Action |
|---|---|
| Entropy > 7.0 | Unpack or detect packer |
| < 50 strings | Unpack first |
| UPX/MPRESS sig | `upx -d` or packer rule |

## CI and retrohunt

- **YARA-CI:** automated goodware testing on PR
- **Git:** version rules with mandatory meta fields
- **Production:** monitor FP rate per rule; disable or fork hot rules quickly

**Hunting rules:** same quality bar as detection—hunting rules become production rules without rework.
