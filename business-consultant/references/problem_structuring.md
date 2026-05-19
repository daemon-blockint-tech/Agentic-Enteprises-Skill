# Problem structuring

## Table of contents

1. [Issue tree](#issue-tree)
2. [MECE rules](#mece-rules)
3. [Prioritization](#prioritization)
4. [Root cause vs symptom](#root-cause-vs-symptom)

## Issue tree

Start from the **key question** (answerable yes/no or numeric):

```
How can we improve [metric] by [amount] in [timeframe]?
├── Grow revenue
│   ├── New customers
│   ├── Expansion
│   └── Reduce churn
├── Reduce cost
│   ├── COGS
│   └── OpEx
└── Improve capital efficiency
```

Each leaf needs a **fact base** (data, benchmark, interview).

## MECE rules

**Mutually Exclusive** — no overlap between siblings at the same level.

**Collectively Exhaustive** — branches cover all material drivers; add "Other" only if truly residual.

Common splits:

| Dimension | Use when |
|---|---|
| Revenue / cost / capital | P&L improvement |
| Customer / product / channel | GTM problems |
| People / process / technology | Operating failures |
| Internal / external | Risk and market |

## Prioritization

Score branches (1–5) on:

- **Impact** on success metric
- **Confidence** evidence exists
- **Effort** to analyze

Work high impact × high confidence first; spike uncertain high-impact branches.

## Root cause vs symptom

| Symptom | Often root cause |
|---|---|
| Missed deadlines | Unclear ownership, WIP limits, bad estimates |
| High support volume | Product quality, docs, onboarding |
| Low win rate | ICP mismatch, pricing, competitive positioning |
| Manual rework | Process design, integration gaps |

Use **5 Whys** only after structuring—avoid jumping to a single narrative too early.

Hand detailed process documentation to `business-analyst` once root cause is agreed.
