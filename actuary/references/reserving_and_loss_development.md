# Reserving and loss development

## Table of contents

1. [Triangle fundamentals](#triangle-fundamentals)
2. [Development methods](#development-methods)
3. [IBNR components](#ibnr-components)
4. [Diagnostics](#diagnostics)
5. [Large losses and catastrophes](#large-losses-and-catastrophes)
6. [Reserve reconciliation](#reserve-reconciliation)
7. [Workpaper exhibits](#workpaper-exhibits)

## Triangle fundamentals

Standard **loss development triangle** axes:

- **Origin period** (accident year, policy year, underwriting year)
- **Development age** (months or years since origin)
- **Values** — paid losses, incurred losses, case reserves, claim counts

| Basis | Use |
|---|---|
| Paid | Cash development; stable for long-tail when case weak |
| Incurred | Case + paid; reflects case reserve changes |
| Reported counts | Frequency development for BF methods |

Align **valuation date** and **cutoff** procedures across periods.

## Development methods

| Method | Idea | Strengths | Weaknesses |
|---|---|---|---|
| Chain ladder | Age-to-age factors to ultimate | Simple, credible for stable patterns | Fails on shifting case adequacy |
| Bornhuetter-Ferguson | Expected loss ratio × % reported | Good for immature years | Sensitive to expected LR pick |
| Cape Cod | Iterative BF using overall LR | Blends experience and prior | Opaque without documentation |
| Frequency-severity | Separate models | Interpretable for GL | Needs stable count definitions |

**Tail factor** selection: fit exponential/inverse power, industry benchmarks, or judgment for oldest age.

Document **factor selections** vs alternative picks with dollar impact.

## IBNR components

```
total reserve ≈ case outstanding + IBNR (+ IBNER if split)
ultimate = reported to date + IBNR (incurred basis)
```

| Component | Description |
|---|---|
| Case | Known claims — case reserves |
| Pure IBNR | Incurred but not reported |
| IBNER | Development on known cases (if split) |
| Bulk | Extra contractual obligations, pooling |

Explain **prior-year development** (PYD) drivers in bridge:

```
opening reserve + incurred losses − paid − closing reserve = PYD
```

## Diagnostics

Run before finalizing:

- **Calendar-year** vs accident-year implied ultimates
- **Factor stability** across recent ages
- **Paid/incurred** divergence
- **Claim count** vs severity reconciliation
- **Outlier** accident years (cat, large loss, one-time events)

Use **bootstrap** or Mack-style uncertainty (overview) when stakeholders need range, not point only.

## Large losses and catastrophes

| Approach | When |
|---|---|
| Cap per claim | Stable large loss pool |
| Separate layer | Excess or cat module |
| Cat load in pricing | Event year distortion in triangle |

Remove or **cap** catastrophe years from factor selection with explicit add-back for cat reserve.

## Reserve reconciliation

Reconcile to:

- Prior quarter/year reserve
- Pricing expected loss ratio (if linked)
- Reinsurance statements
- Statutory or GAAP reporting lines (coordinate with accounting)

Material changes (> threshold) require **narrative**: methodology, data, large losses, assumption.

## Workpaper exhibits

Minimum exhibits:

1. Paid and incurred triangles (last N origin years)
2. Selected age-to-age factors and tail
3. Ultimate loss table by origin year
4. IBNR summary and roll-forward
5. PYD bridge to prior evaluation
6. Sensitivity: ± one factor or ± tail

Store **data cut** hash, model version, and preparer/reviewer sign-off.
