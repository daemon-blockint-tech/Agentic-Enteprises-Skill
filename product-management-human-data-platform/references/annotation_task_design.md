# Annotation Task Design

## Task design deliverables

| Artifact | Purpose |
|----------|---------|
| **Taxonomy** | Labels, hierarchies, mutually exclusive rules |
| **Instructions** | Step-by-step for contributors |
| **Rubric** | Borderline examples and decision rules |
| **UI spec** | Controls, required fields, media handling |
| **Edge-case catalog** | Ambiguous items with gold answer |
| **Calibration set** | Items for onboarding and drift checks |

## Instruction quality checklist

- [ ] Objective defined in one sentence
- [ ] Definitions for every label with **positive and negative** examples
- [ ] Order of operations (e.g. "check safety before sentiment")
- [ ] What to do when **unsure** (skip, flag, best guess policy)
- [ ] Media-specific rules (audio clipping, occlusion, PII blur)
- [ ] Change log when taxonomy updates

## Taxonomy rules

| Rule type | Example |
|-----------|---------|
| Mutually exclusive | Single primary intent per utterance |
| Hierarchical | Vehicle → car → sedan |
| Multi-label | Tags where independent |
| Conditional | If "toxic" then severity required |

Pair with `ontology-engineer` when enterprise customers need shared ontologies across programs.

## Modality considerations

| Modality | PM must specify |
|----------|-----------------|
| Text | Language, encoding, span vs document level |
| Image | Bounding box vs polygon vs keypoint |
| Audio | Transcription vs diarization vs emotion |
| Video | Frame sampling rate, temporal segments |
| Multi-modal | Which field is source of truth |

## Pre-labeling and automation

| Strategy | When |
|----------|------|
| Model pre-label + human edit | High volume, stable taxonomy |
| Active learning queue | Edge cases for next batch |
| Rules engine | Hard constraints (regex, blocklists) |

Document **expected edit rate** so ops can staff reviewers.

## Versioning

- Task spec version tied to exported dataset metadata
- Breaking taxonomy changes require **relabel or migrate** plan
- Customer notification for downstream training impact

## Review with design and eng

- `product-designer`: task UI affordances, error prevention
- Eng: latency, autosave, conflict on concurrent edit
- Ops: estimated handle time per item for pricing/SLA
