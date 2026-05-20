# Geofencing, tracking, and map matching

## Table of contents

1. [Geofencing models](#geofencing-models)
2. [Spatial predicates for fences](#spatial-predicates-for-fences)
3. [Event semantics](#event-semantics)
4. [Trajectory processing](#trajectory-processing)
5. [Map matching integration](#map-matching-integration)
6. [Stop and trip detection](#stop-and-trip-detection)

## Geofencing models

| Shape | Pros | Cons |
|---|---|---|
| Polygon | Precise sites, yards, campuses | Requires valid topology; maintenance |
| Circle (center + radius) | Simple yards | Poor fit for irregular sites |
| Corridor buffer | Routes, highways | Needs centerline geometry |
| Grid cell (H3) | Fast prefilter | Coarse; combine with precise polygon |

Store fences in **PostGIS** with SRID documented; prefilter candidates with bbox or H3 before precise predicate.

## Spatial predicates for fences

| Rule | Predicate notes |
|---|---|
| Inside | `ST_Contains(fence, point)` — boundary behavior explicit |
| Enter | Transition outside → inside between consecutive fixes |
| Exit | Inside → outside |
| Dwell | Inside for ≥ T seconds without exit |
| Buffered fence | `ST_DWithin(point::geography, fence::geography, buffer_m)` |

**Debounce:** require N consecutive inside samples or minimum dwell before ENTER to reduce GPS jitter false triggers.

## Event semantics

Emit events with:

- `asset_id`, `fence_id`, `event_type` (ENTER/EXIT/DWELL)
- `ts_event`, `position`, `confidence`
- `rule_version` for reproducibility

Downstream consumers (billing, alerts, workflow) must tolerate **at-least-once** delivery—dedupe on natural keys.

## Trajectory processing

Pipeline stages (conceptual):

1. **Normalize** — CRS, units, canonical fix schema
2. **Filter** — quality flags, impossible speed
3. **Segment** — trips on ignition/gap/stop rules
4. **Enrich** — geofence hits, timezone, jurisdiction
5. **Match** (optional) — snap to network; store vendor + graph version
6. **Publish** — API and warehouse export interfaces

Keep **raw** and **derived** layers; never overwrite raw fixes with snapped coordinates.

## Map matching integration

| Approach | When |
|---|---|
| External API (OSRM-like, commercial MM) | Production fleets; graph maintained by vendor |
| Self-hosted routing graph | High scale, licensed road data, dedicated team |
| Simple snap | Low stakes yard maps only—not public road inference |

Contract boundaries:

- Input: ordered fixes + timestamps + optional heading
- Output: matched polyline, edge IDs, confidence, distance on network
- Failure: return unmatched with reason; do not block raw ingest

**Do not** implement full routing graph maintenance inside generic app services—coordinate with `operations-research-algorithm-developer` for optimization on top of matched networks.

## Stop and trip detection

| Signal | Heuristic |
|---|---|
| Speed < threshold for T seconds | Stop |
| Ignition off | End trip (if available) |
| Gap > T minutes | Split trip |
| Geofence depot enter | Start/end shift events |

Tune thresholds per **asset class** (truck vs trailer vs handheld). Document in configuration, not hard-coded constants.
