# Environments and rollouts

## Table of contents

1. [Env API contract](#env-api-contract)
2. [Vectorization](#vectorization)
3. [Trajectory schema](#trajectory-schema)
4. [Common failures](#common-failures)

## Env API contract

Standardize:

- `reset(seed) → obs, info`
- `step(action) → obs, reward, terminated, truncated, info`
- `action_space` / `observation_space` metadata exposed to controller
- **Determinism** — which ops are stochastic; how seeds propagate

Version **env binary** alongside training config — mismatch causes silent metric drift.

## Vectorization

| Approach | When |
|---|---|
| Subprocess vector env | CPU-bound sim |
| Shared-memory vector | Low-latency local |
| Remote env servers | Heavy sim (games, physics) |
| Batched GPU sim | Homogeneous parallel worlds |

Target **steps/sec per core** in benchmarks before full training run.

## Trajectory schema

Store per step (minimum):

- `obs`, `action`, `reward`, `done`, `log_prob` (if on-policy)
- `value`, `advantage` (if computed on actor)
- `env_id`, `episode_id`, `global_step`
- Optional: `info` keys for reward decomposition

Fixed schema enables **replay ingestion** and debugging tools.

## Common failures

| Symptom | Cause |
|---|---|
| Reward flatlines | Wrong normalization; env bug |
| Actor lag | Slow sim; too few workers |
| Diverging KL | Policy update too aggressive; desynced weights |
| OOM on actor | Batched obs too large |
| Non-reproducible eval | Unseeded env or floating order |

Log **episode statistics** — length, terminal reason, reward histogram.
