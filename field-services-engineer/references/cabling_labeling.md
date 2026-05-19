# Cabling and Labeling

## Labeling standard (both ends)

| Element | Label content |
|---------|----------------|
| Device | hostname or asset tag |
| Port | port ID / interface name |
| Cable | unique cable ID optional for long runs |
| Patch panel | panel, port, destination |

Labels readable from aisle; facing out; heat-shrink or laser per site standard.

## Copper vs fiber

| Media | Field checks |
|-------|--------------|
| Cat6/AOC DAC | Correct length; no kink; latch click |
| SM/MM fiber | Correct OM/OS; no dust caps left off |
| MTP/MPO | Polarity per diagram; use scope if available |

## Cable dress

- Separate power and data bundles
- Maintain bend radius on fiber
- Use velcro; no zip ties on fiber
- Leave service loop for top-of-rack moves

## Link verification (physical layer)

| Test | Tool | Record |
|------|------|--------|
| Link light | Visual | Photo |
| Copper cert | Fluke (if SOW) | PDF attach |
| Fiber loss | OLTS/OTDR (if SOW) | Values |
| Port map | Tone/trace (rare) | Note |

Logical config (VLAN, BGP) is **remote**—field confirms physical continuity only.

## Port map closeout

```markdown
| Local device | Local port | Remote device | Remote port | Cable ID |
```

Mismatch with design → stop and escalate.

## Common faults

| Symptom | Likely cause |
|---------|--------------|
| No link one side | Wrong port, bad module, VLAN N/A at L1 |
| Intermittent | Loose SFP, dirty fiber, damaged patch |
| All links down | PDU off, wrong breaker |

## Spares on belt

- SFPs (speed/type approved list)
- Patch cords (lengths)
- Fiber cleaners
- Console cable / crash cart access

## Anti-patterns

- Home-run cables without change record
- Mixing A/B power on same PDU branch against design
- Unlabeled "temporary" cables left permanent
