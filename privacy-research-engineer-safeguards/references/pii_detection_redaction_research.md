# PII detection and redaction research

## Table of contents

1. [Entity taxonomy](#entity-taxonomy)
2. [Detection approaches](#detection-approaches)
3. [Redaction strategies](#redaction-strategies)
4. [Evaluation protocol](#evaluation-protocol)

## Entity taxonomy

Align types with policy and **locale**:

- Direct identifiers: email, phone, government ID, payment card
- Quasi-identifiers: name, address, employer, rare combinations
- Special categories (jurisdiction-dependent): health, biometric references in text
- Contextual: username, session token, internal employee ID

Document **overlap** with harm categories (e.g. self-harm content is not PII).

## Detection approaches {#detection-approaches}

| Approach | Research notes |
|---|---|
| Rules/regex | Strong on structured IDs; brittle on unicode |
| Token classification (NER) | Per-type metrics; train on balanced slices |
| LLM span labeling | Flexible; watch cost and consistency |
| Ensemble | Often best; ablate contribution |

## Redaction strategies

| Strategy | Trade-off |
|---|---|
| Mask (`***`) | Simple; may break downstream parsing |
| Replace with type token (`[EMAIL]`) | Good for ML pipelines |
| Synthetic fill | Higher utility risk if plausible fake PII |
| Drop span | May break grammar; measure downstream task |

Measure **downstream harm classifier** change after redaction — privacy must not silently break safety.

## Evaluation protocol

1. Frozen **benchmark version** with human-adjudicated spans
2. Report per-type P/R and **macro** averages
3. **Hard negative** set (benign numbers, product IDs)
4. **Adversarial** formats: obfuscated email, split across messages, homoglyphs
5. Error analysis clusters for next labeling round

Hand promotion thresholds to `ml-research-engineer-safeguards` when shared classifier stack.
