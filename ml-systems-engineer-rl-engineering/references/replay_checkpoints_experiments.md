# Replay, checkpoints, and experiments

## Table of contents

1. [Replay buffer](#replay-buffer)
2. [Checkpoints](#checkpoints)
3. [Experiment tracking](#experiment-tracking)
4. [Config management](#config-management)

## Replay buffer

| Concern | Practice |
|---|---|
| Capacity | Steps vs transitions; ring buffer on disk for huge |
| Prioritized replay | Thread-safe heap; watch bias in metrics |
| Serialization | Chunked files for resume |
| Sampling | Batch builder on learner; avoid actor blocking |

Monitor **buffer fill rate** and **sample age** (staleness for off-policy).

## Checkpoints

Include for resume:

- Policy (+ target nets if applicable)
- Optimizer state
- Global step / epoch
- Observation normalizer stats
- RNG states (python, numpy, torch, cuda)
- Replay cursor or on-policy batch offset

Store in **versioned object store**; manifest JSON with git SHA and env version.

Test **resume continues learning curve** — not flat restart.

## Experiment tracking

Log at minimum:

- `episode_return`, length (mean, std, percentiles)
- `policy_loss`, `value_loss`, `entropy`, `kl` (algorithm-specific)
- `steps_per_sec`, actor count, learner GPU util
- `grad_norm`, NaN flags

Tag runs: team, algorithm, env version, config hash.

## Config management

Single source:

```yaml
algorithm: ...
env: ...
infra:
  num_actors: ...
  learner_gpus: ...
  checkpoint_every_steps: ...
```

Never split infra knobs from algorithm hparams across unlinked files.
