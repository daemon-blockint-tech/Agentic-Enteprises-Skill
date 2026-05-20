# Evaluation, simulation, and metrics

## Table of contents

1. [Metric categories](#metric-categories)
2. [Estimation consistency](#estimation-consistency)
3. [Tracking and fusion quality](#tracking-and-fusion-quality)
4. [Simulation and SIL](#simulation-and-sil)
5. [Bag replay and regression](#bag-replay-and-regression)

## Metric categories

| Category | Examples | Ground truth needed |
|---|---|---|
| **Ego state** | Position/attitude RMSE, drift rate | RTK, survey, SLAM reference |
| **Object state** | Position/velocity error per track | Labels, radar truth, sim |
| **Association** | Purity, mismatch rate | Track IDs in labels |
| **System** | Latency p95, drop rate, CPU | Logs only |
| **Safety proxy** | Min TTC error, miss distance | Scenario-specific |

Report **confidence intervals** over scenarios, not single-number hero runs.

## Estimation consistency

**NEES** (Normalized Estimation Error Squared):

\[
\text{NEES}_k = (x_k - \hat{x}_k)^T P_k^{-1} (x_k - \hat{x}_k)
\]

For well-tuned Gaussian filter, NEES ≈ \(\chi^2\) with dof = state dimension (per update, use with care).

| Symptom | Likely cause |
|---|---|
| NEES too high | Overconfident \(P\), bad R, calibration, unmodeled bias |
| NEES too low | Inflated Q/R, redundant measurements |
| Drift in NEES over time | Temperature, vibration, sensor aging |

**Innovation tests:** whiteness, magnitude per sensor channel.

## Tracking and fusion quality

| Metric | Use |
|---|---|
| **RMSE** (position/velocity) | Per-class, per-range-bin accuracy |
| **Track continuity** | % time object tracked without break |
| **ID switch rate** | Planning-critical scenarios |
| **Fragmentation / merges** | MOT diagnostics |
| **Association purity** | Correct measurement-to-track ratio |
| **Ghost / false track rate** | Clutter environments |

Define **success criteria** per ODD (operational design domain) before tuning.

## Simulation and SIL

| Layer | Purpose |
|---|---|
| **Sensor simulation** | Noise, latency, FOV, weather models |
| **Scenario simulation** | Traffic, dynamics, scripted edge cases |
| **Software-in-the-loop** | Fusion node with synthetic or recorded inputs |

Practices:

- Seed **RNG** for reproducibility
- Model **latency and drop** not only ideal measurements
- Version **sensor models** with fusion software in regression manifest
- Cross-check sim vs **bag replay** on same scenario

Coordinate with autonomy sim (`tactical-ai-autonomy-developer`) on scenario ownership.

## Bag replay and regression

**Bag replay checklist:**

1. Fix **clock** and **TF** to recorded or recomputed calibration version
2. Pin **software commit**, config, and calibration hash in report
3. Run **deterministic** mode where middleware allows
4. Compare outputs to **baseline** and labeled ground truth

**Regression suite structure:**

| Tier | Content | Gate |
|---|---|---|
| Smoke | Short bags, core metrics | CI nightly |
| Standard | Full ODD slice | Release candidate |
| Stress | Weather, denial, sensor loss | Manual / milestone |

Artifacts: metric JSON, plots (NEES, RMSE vs time), failure case list with bag timestamps.

**Do not** claim safety certification from metrics alone—engineering evidence for internal review.
