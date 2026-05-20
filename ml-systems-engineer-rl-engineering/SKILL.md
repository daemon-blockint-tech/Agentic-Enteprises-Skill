---
name: ml-systems-engineer-rl-engineering
description: |
  Guides ML systems engineering for reinforcement learning—distributed training platforms, rollout
  workers and vectorized environments, replay buffers, policy/critic serving for train loops,
  checkpointing and experiment tracking, sim-to-real hooks, and RL training reliability.
  Use when building RL training infrastructure, scaling PPO/SAC-style jobs, debugging unstable
  distributed rollouts, designing env APIs, or exporting policies for inference—not for supervised
  ML product modeling (data-scientist), LLM RAG/agents (ai-engineer), safeguard classifiers
  (ml-research-engineer-safeguards, ml-infrastructure-engineer-safeguards), general GPU serving
  without RL (ml-infrastructure-engineer-safeguards), or app latency profiling (performance-engineer).
---

# Machine Learning Systems Engineer, RL Engineering

## When to Use

- Design **RL training platform** — controllers, workers, resource scheduling
- Implement **rollout collection** — vectorized envs, async actors, trajectory buffers
- Operate **distributed training** — data parallel, parameter servers, gradient sync patterns
- Manage **replay buffers** — prioritization, storage, sampling at scale
- Wire **checkpointing** — policy/value nets, optimizer state, resume after preemption
- Integrate **experiment tracking** — seeds, configs, metric schemas, artifact lineage
- Connect **simulators** — Gymnasium-style APIs, custom env servers, batch stepping
- **Export policies** for batch eval or downstream inference path
- Debug **training instability** — NaNs, reward scale, worker desync, straggler GPUs
- Plan **GPU/memory** layout for actor vs learner processes

## When NOT to Use

- Churn models, A/B tests, classical supervised pipelines → `data-scientist`
- Production LLM features, agents, RAG → `ai-engineer`
- Safeguard/moderation inference gateways → `ml-infrastructure-engineer-safeguards`
- Safety classifier research → `ml-research-engineer-safeguards`
- CI/CD and generic K8s ops → `devops`, `cluster-deployment-engineer`
- DC-wide GPU supply programs → `data-center-compute-supply-efficiency`
- HTTP API p99 without RL training context → `performance-engineer`
- RL algorithm theory only (no systems) → `ai-researcher` for literature; stay systems-focused here

## Related skills

| Need | Skill |
|---|---|
| Supervised ML and statistical eval | `data-scientist` |
| General AI research methodology | `ai-researcher` |
| Inference gateways and model serving | `ml-infrastructure-engineer-safeguards` |
| Training cluster / K8s jobs | `cluster-deployment-engineer` |
| Pipelines and GitOps | `devops` |
| GPU capacity at facility level | `data-center-compute-supply-efficiency` |
| Serving latency and load tests | `performance-engineer` |
| Product agents using RL outcomes | `ai-engineer` |

## Core Workflows

### 1. RL systems framing

Env contract, on/off-policy, scale targets.

**See `references/rl_systems_framing.md`.**

### 2. Training platform architecture

Controllers, workers, scheduling.

**See `references/training_platform_architecture.md`.**

### 3. Environments and rollouts

Vectorization, trajectory format.

**See `references/environments_rollouts.md`.**

### 4. Replay, checkpoints, experiments

Buffers, resume, tracking.

**See `references/replay_checkpoints_experiments.md`.**

### 5. Evaluation and policy export

Eval harness, deployment handoff.

**See `references/evaluation_policy_export.md`.**

### 6. Reliability and observability

Stability, metrics, incident debug.

**See `references/reliability_observability_rl.md`.**

## Outputs

- **Architecture doc** — actor/learner topology, data flow, failure domains
- **Env API spec** — observation, action, reward, reset, seed semantics
- **Runbook** — launch, resume, preempted job recovery, scale-out
- **Config template** — hyperparameters + infra knobs versioned together
- **Metric dashboard spec** — reward, length, KL, GPU, steps/sec, queue depth
- **Policy export package** — weights, normalization stats, eval report

## Principles

- **Reproducibility** — seed envs, log config hash, pin sim versions
- **Separate rollout from learn** — scale collectors and learners independently
- **Deterministic resume** — checkpoint includes optimizer and buffer cursor when needed
- **Observe the MDP** — log reward components, not only scalar return
- **Fail fast on desync** — version mismatch between workers is a top incident class
