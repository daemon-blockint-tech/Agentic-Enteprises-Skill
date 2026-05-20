# Red-team campaigns on models

## Table of contents

1. [Scope vs ai-redteam](#scope-vs-ai-redteam)
2. [Campaign planning](#campaign-planning)
3. [Execution patterns](#execution-patterns)
4. [Finding format](#finding-format)

## Scope vs ai-redteam

| This skill (model robustness) | `ai-redteam` (LLM product) |
|---|---|
| ASR under perturbation budgets | Jailbreak policy, multi-turn coercion ROE |
| Poisoning and backdoor hunts | Tool abuse, data exfil from RAG apps |
| Extraction query budgets | Enterprise red-team simulation |
| Lab/staging model endpoints | Full copilot/agent surface testing |

Run **both** when shipping LLM products: robustness eval on model + product red team on app.

## Campaign planning

1. **Authorize** — scope, environment, models, stop conditions
2. **Freeze** — model hash, API version, defense config snapshot
3. **Select attacks** — aligned to threat model (evasion set, poison probes, extraction scripts)
4. **Allocate budget** — query caps, compute ceiling, calendar window
5. **Define severity** — link ASR deltas and exploit practicality to tiers

Never run destructive load or unapproved prod tests.

## Execution patterns

| Pattern | When |
|---|---|
| **Automated sweep** | Grid over ε, attack types, slices — nightly regression |
| **Guided fuzzing** | Mutate inputs toward misclassification (gradient-free APIs) |
| **Poison canary** | Inject labeled canary rows; detect label drift after retrain |
| **Extraction trial** | Bounded queries; measure agreement with surrogate |
| **Champion/challenger** | Compare new weights vs production on fixed attack seed |

Log: timestamp, seed, attack params, input hash, output, defense flags triggered.

## Finding format

```markdown
### [ID] Title
- **Class**: Evasion | Poisoning | Extraction | Inference
- **Severity**: Critical / High / Medium / Low
- **Environment**: lab | staging
- **Model**: name@version (hash)
- **Budget**: ε=..., queries=...
- **ASR / impact**: ...
- **Reproduction**: minimal script or curl sequence
- **Mitigation**: defense layer + owner
- **Residual risk**: adaptive follow-ups
```

Hand critical poisoning or supply-chain issues to `devsecops` and governance as needed.
