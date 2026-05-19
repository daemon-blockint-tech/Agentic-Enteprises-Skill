# Power and cooling

## Table of contents

1. [Power chain](#power-chain)
2. [Rack density](#rack-density)
3. [Cooling and PUE](#cooling-and-pue)

## Power chain

```
Utility → (gen optional) → ATS/STS → UPS → PDU (rack/row) → C13/C19 → IT load
```

| Element | Design notes |
|---|---|
| UPS | Runtime at full load; battery refresh schedule |
| PDU | Metered, switched where needed; A+B feeds for dual-cord servers |
| STS | Transfer time within equipment tolerance |

**Margin:** Plan facility at **80%** of nameplate for sustained IT load; burst for GPU per vendor guidance.

## Rack density

| Profile | kW/rack (indicative) | Cooling |
|---|---|---|
| General compute | 5–8 | Air, hot aisle containment |
| Dense compute | 10–15 | Enhanced air or rear-door HX |
| GPU/HPC | 20–70+ | Direct liquid, immersion, or specialty |

Mismatch (high kW in low-density hall) causes thermal trips and stranded space.

## Cooling and PUE

- **PUE** = total facility power / IT equipment power; measure at defined points consistently
- Setpoints: ASHRAE A1–A4 classes; wider bands save energy if hardware allows
- **Containment** reduces bypass air; blanking panels mandatory
- Humidity and filtration per equipment specs

Commissioning: heat load bank or staged IT rollout; trend inlet/outlet temps per rack row.
