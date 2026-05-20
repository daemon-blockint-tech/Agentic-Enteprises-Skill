# Spatial databases and queries

## Table of contents

1. [Schema patterns](#schema-patterns)
2. [Geometry vs geography](#geometry-vs-geography)
3. [Indexes](#indexes)
4. [Common predicates](#common-predicates)
5. [Query performance](#query-performance)
6. [Partitioning](#partitioning)

## Schema patterns

**Track point (hot path):**

```sql
-- asset_id, ts_utc, geom (Point, 4326), speed_mps, heading_deg,
-- accuracy_m, source_device_id, ingest_id
```

**Geofence region:**

```sql
-- fence_id, name, geom (Polygon, 4326), buffer_m, active, rules_json
```

**Trip segment (derived):**

```sql
-- trip_id, asset_id, start_ts, end_ts, geom (LineString, 4326), distance_m
```

Store **raw fixes** separately from **matched/snapped** geometries; version map-matching vendor and graph date.

## Geometry vs geography

| Type | Use when |
|---|---|
| `geometry` | Projected CRS for local editing; explicit `ST_Transform` for metrics |
| `geography` | Global fleets; distances/areas in meters with lon/lat storage |

Example bbox filter (WGS84 points):

```sql
WHERE geom && ST_MakeEnvelope($minx, $miny, $maxx, $maxy, 4326)
  AND ST_Intersects(geom, ST_MakeEnvelope($minx, $miny, $maxx, $maxy, 4326))
```

Use `&&` for index-friendly envelope prefilter before `ST_Intersects`.

## Indexes

| Index | Use when |
|---|---|
| GiST on geometry/geography | Bbox, intersects, nearest-neighbor (with care) |
| BRIN on time + coarse geo | Append-only track history, time-range scans |
| B-tree on `(asset_id, ts_utc)` | Primary trajectory lookups |
| Grid/H3 column (text/int) | Bucketed aggregates, geofence candidate filtering |

Create indexes **after** load on large migrations; `ANALYZE` after bulk ingest.

## Common predicates

| Need | PostGIS pattern |
|---|---|
| Inside geofence | `ST_Contains(fence.geom, point.geom)` or `ST_Within(point, fence)` |
| Within radius | `ST_DWithin(geog_a, geog_b, radius_m)` |
| Along corridor | `ST_DWithin(point, route_line, buffer_m)` |
| Nearest road (prep) | Precompute graph IDs via map-matching service—not ad hoc `ST_ClosestPoint` on full linework in OLTP |

## Query performance

- Avoid `ST_Transform` on every row in hot queries—materialize projected columns if needed
- Cap result counts; require **time window** + **asset filter** for track history APIs
- Use **simplified** geometries for low-zoom map responses
- Watch ** cardinality of DISTINCT spatial joins**—pre-bin by H3 where possible

## Partitioning

| Strategy | Fit |
|---|---|
| Time range (monthly) on track tables | High-volume telematics |
| List by tenant/region | Multi-tenant fleets |
| Archival to object store (Parquet/COG) | Cold history; keep metadata in catalog |

Document **retention drop** jobs per partition and legal hold exceptions.
