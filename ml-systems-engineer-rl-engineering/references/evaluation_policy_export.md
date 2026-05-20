# Evaluation and policy export

## Table of contents

1. [Eval harness](#eval-harness)
2. [Deterministic eval](#deterministic-eval)
3. [Policy export](#policy-export)
4. [Handoff to serving](#handoff-to-serving)

## Eval harness

Separate **training** from **eval** jobs:

- Fixed seed suite; frozen env version
- Deterministic policy (`eval` mode, no exploration noise)
- Report mean/std return over N episodes per seed
- Compare checkpoints on same harness — learning curves

Schedule eval on **checkpoint events**, not only end of run.

## Deterministic eval

- Fix seeds list in config
- Disable domain randomization if used in training
- Same observation normalization as training checkpoint
- Log videos/traces sparingly — storage cost

Regression gate: eval return must not drop > X% vs prior champion.

## Policy export

Artifacts:

- TorchScript / ONNX / native weights (document format)
- Normalization constants
- Action post-processing (clip, discrete mapping)
- Expected obs shape and dtype

Include **latency benchmark** on reference hardware for downstream teams.

## Handoff to serving

| Consumer | Needs |
|---|---|
| Batch offline scoring | Exported policy + batch driver |
| Real-time control | `ml-infrastructure-engineer-safeguards` or custom inference service |
| Sim validation | Env server + policy client |

Document **exploration off** in production; epsilon schedule not applied.

For HTTP/gateway deployment → coordinate with inference infra skills; this skill owns **export correctness**.
