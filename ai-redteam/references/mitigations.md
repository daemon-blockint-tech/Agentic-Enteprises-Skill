# Mitigations

## Table of contents

1. [Defense layers](#defense-layers)
2. [Weak controls](#weak-controls)

## Defense layers

| Layer | Control |
|---|---|
| Input | Length limits, blocklists, classifiers |
| System | Strong policy, delimiter isolation |
| RAG | Source trust tiers, chunk sanitization |
| Tools | Allowlist, authz per tool, human approval |
| Output | Policy classifier, PII redaction |

## Weak controls

- Security through obscurity in system prompt alone
- Single regex filter
- Assuming fine-tuning removes jailbreaks
- Trusting retrieved HTML without sanitization

Always validate with `ai-redteam` regression set after changes.
