# Memorization and extraction

## Table of contents

1. [Attack surfaces](#attack-surfaces)
2. [Study designs](#study-designs)
3. [Mitigations research](#mitigations-research)
4. [Ethics](#ethics)

## Attack surfaces

| Surface | Question |
|---|---|
| Generative model | Can it repeat rare training strings? |
| Safety fine-tune | Did safety data introduce user snippets? |
| RAG / retrieval | Cross-user chunk retrieval |
| Logs used for retraining | Accidental inclusion of prod prompts |
| Eval notebooks | Copied datasets without access controls |

## Study designs

- **Canary strings** — unique tokens inserted in train; probe generation frequency
- **Membership inference** — research-only; document limitations and ethics
- **Prompt repetition** — ask model to continue known prefixes from suspected leaks
- **Log replay** — verify redaction before indexing for analytics

Use **synthetic canaries** when possible; prod canaries only with governance approval.

## Mitigations research

Evaluate:

- Differential privacy training (utility cost curve)
- Data deduplication and **near-duplicate** removal before train
- Train only on **redacted** corpora
- Output filters blocking high-entropy repeated n-grams
- Tenant isolation in retrieval and fine-tune pipelines

Report measurable **utility delta** on primary safety metrics.

## Ethics

- No publishing raw leaked strings externally
- Aggregate findings in memos
- Stop study if unintended real PII discovered — incident path via `ai-lead-ops`

Pair offensive testing of extraction with `ai-redteam` scope clarity — research measures, red team attacks prod.
