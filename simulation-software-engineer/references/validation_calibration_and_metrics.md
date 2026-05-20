# Validation, calibration, and metrics

## Table of contents

1. [Purpose](#purpose)
2. [V&V vocabulary](#vv-vocabulary)
3. [Validation workflow](#validation-workflow)
4. [Calibration workflow](#calibration-workflow)
5. [Metric families](#metric-families)
6. [Monte Carlo and parameter sweeps](#monte-carlo-and-parameter-sweeps)
7. [Uncertainty and sensitivity](#uncertainty-and-sensitivity)
8. [Regression governance](#regression-governance)
9. [Reporting template](#reporting-template)
10. [Checklist](#checklist)

## Purpose

Guide **evidence that simulation is fit for purpose**—comparing to measured data, tuning parameters responsibly, and structuring sweeps without over-claiming predictive power.

## V&V vocabulary

| Term | Meaning in this skill |
|---|---|
| Verification | Sim implemented correctly vs its spec (code/units/tests) |
| Validation | Sim represents reality within stated metrics for a use case |
| Calibration | Adjusting model parameters to reduce error vs measurements |
| Accreditation | Organizational sign-off—out of scope; no certification claims |

**Fit-for-purpose statement (required):** “This model is adequate for \<decision\> when metric \<M\> is within \<threshold\> on dataset \<D\>.”

## Validation workflow

1. **Define use case** — what decision the sim supports (controller gain, training coverage, HIL fault test)
2. **Select fidelity tier** per subsystem (see scope reference)
3. **Choose datasets** — holdout reserved; no tuning on test set
4. **Define metrics** — per domain (pose, velocity, range error, detection counts)
5. **Run baseline** — document sim version, seeds, assets
6. **Compare and report** — residuals, time alignment, failure cases
7. **Gate** — pass/fail thresholds for CI or release

### Time alignment

- Synchronize logs with **interpolation policy** (linear, SLERP for attitudes)
- Account for **sensor latency** in sim vs truth in field logs
- Flag **clock jumps** and drop segments that invalidate comparison

## Calibration workflow

| Step | Action |
|---|---|
| Identify parameters | List tunable params with physical bounds |
| Prior | Document source (datasheet, guess, literature) |
| Objective | Scalar or vector error (RMSE, NLL, weighted multi-metric) |
| Method | Manual, grid, Bayesian, optimizer—justify identifiability |
| Validate | Evaluate on holdout; report overfit risk |
| Freeze | Version parameter set with sim release |

**Avoid:** tuning until metrics look good on the same data used to fit (report train vs holdout).

## Metric families

| Domain | Example metrics |
|---|---|
| Pose / track | RMSE position, yaw error, NEES (if estimator present) |
| Vehicle dynamics | Lateral accel error, sideslip, steering response time |
| IMU | Allan deviation bands, bias stability |
| Camera / LiDAR | Reprojection error, range RMSE, false positive rate on fixtures |
| Radar | Range/range-rate error distributions |
| Scenario outcomes | Success rate, collision rate, time-to-goal |
| Real-time | Overrun count, max latency, dropped frames |

Publish **units** and **frames** with every metric table.

## Monte Carlo and parameter sweeps

### Design

| Approach | When |
|---|---|
| Full factorial | Small discrete sets |
| Latin hypercube | Continuous params, coverage |
| Random sampling | Quick exploration with seeds |
| Importance sampling | Rare events (document bias correction) |

### Execution contract

- Fixed **seed ladder** for reproducibility (`base_seed + run_index`)
- Cap **parallelism** with isolated output dirs
- Aggregate with **percentiles**, not only means

### Failure taxonomy

Classify failures: `collision`, `timeout`, `controller_saturation`, `sensor_fault`, `numerical_instability`—avoid undifferentiated “failed.”

## Uncertainty and sensitivity

- **Sensitivity:** vary one parameter at a time or Sobol indices when budget allows
- **Uncertainty:** report output spread across Monte Carlo; separate **epistemic** (model gap) vs **aleatory** (noise)
- Do not present **single-run** results as reliability without distribution

## Regression governance

| Artifact | Owner |
|---|---|
| Baseline metrics JSON | Sim team |
| Tolerance changelog | Reviewed in PR with scenario ID |
| Dataset manifest | Versioned; PII/export scrubbed |

When baselines move, require **hypothesis** (model fix vs intentional behavior change).

## Reporting template

```markdown
## Validation summary
- Use case:
- Sim version / scenario pack:
- Datasets (train/holdout):

## Results
| Metric | Threshold | Train | Holdout |
|--------|-----------|-------|---------|

## Residual analysis
- Largest errors (with timestamps):

## Calibration
- Parameters changed since last release:
- Identifiability / overfit notes:

## Limitations
- Known non-validated regimes:
```

## Checklist

- [ ] Fit-for-purpose statement written
- [ ] Holdout dataset reserved before tuning
- [ ] Metrics include units, frames, time sync method
- [ ] Monte Carlo seeds and aggregation documented
- [ ] Failure taxonomy applied
- [ ] Limitations section lists known bad regimes
