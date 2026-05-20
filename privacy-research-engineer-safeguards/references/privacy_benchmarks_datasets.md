# Privacy benchmarks and datasets

## Table of contents

1. [Dataset sources](#dataset-sources)
2. [Synthetic data](#synthetic-data)
3. [Labeling](#labeling)
4. [Versioning and access](#versioning-and-access)

## Dataset sources

| Source | Controls |
|---|---|
| Public PII corpora | License, locale coverage |
| Synthetic generators | Template diversity, bias audit |
| Internal samples | Minimization, access tier, TTL |
| Red-team harvests | Separate from train; legal review |

**Never** merge prod dumps into train without de-ID pipeline sign-off.

## Synthetic data

Pros: no real subjects. Cons: unrealistic distribution, missed edge formats.

- Vary formats (international phone, unicode names)
- Inject **hard negatives** (order numbers, public figures)
- Document generator version in dataset card

## Labeling

- Span-level PII labels with guidelines per type
- **Ambiguous** bucket — do not force wrong certainty
- Inter-annotator agreement on subset
- Annotator access: VPN, no local export, DLP where required

## Versioning and access

Dataset card:

- `dataset_id`, version, languages
- Provenance and license
- Known gaps (e.g. no APAC addresses)
- Access group (research vs production)

Rotate credentials; audit downloads.

For enterprise lineage standards → `data-architect`.
