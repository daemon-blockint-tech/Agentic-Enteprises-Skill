# Serving APIs and operations

## Table of contents

1. [API surfaces](#api-surfaces)
2. [Tile and map serving](#tile-and-map-serving)
3. [OGC integration](#ogc-integration)
4. [Caching and CDN](#caching-and-cdn)
5. [Privacy and retention](#privacy-and-retention)
6. [Monitoring and runbooks](#monitoring-and-runbooks)

## API surfaces

| API | Typical operations |
|---|---|
| REST/JSON | Last position, history bbox+time, geofence CRUD, event webhooks |
| WebSocket / SSE | Live asset positions (throttled) |
| gRPC | High-volume internal consumers |

**Contract essentials:**

- Required `time_start` / `time_end` on history endpoints
- Max points per response; pagination cursors
- Explicit `srid` on geometry fields
- Rate limits per tenant and per asset subscription tier

## Tile and map serving

| Layer | Pattern |
|---|---|
| Vector tiles (MVT) | Tippecanoe or pg_tileserv; simplify per zoom |
| Raster tiles | GeoTIFF/COG or pre-rendered PNG pyramid |
| Dynamic features | Short TTL cache; bbox-aligned requests |

Tile URL template example pattern: `/{z}/{x}/{y}.mvt?layer=fences&tenant=`

Invalidate caches on **geofence publish** and **style version** bump.

## OGC integration

Integration-level guidance (not full spec):

| Service | Client responsibilities |
|---|---|
| WMS | GetMap with CRS, bbox, layers, format; handle exceptions XML |
| WFS | GetFeature with bbox/filter; GML/GeoJSON output negotiation |
| WMTS | Tile matrix set alignment; cache templates |

Pin **supported CRS list** from GetCapabilities; fail fast on unsupported combinations.

## Caching and CDN

| Content | Cache key inputs |
|---|---|
| Static basemap tiles | z/x/y + style version |
| MVT fences/assets | z/x/y + tenant + data version |
| Last position API | Do not CDN-cache; short in-memory only |

Use **ETag** or version query params for cache busting after data migrations.

## Privacy and retention

| Control | Implementation hint |
|---|---|
| Precision reduction | Truncate coords at storage or API by role |
| Retention TTL | Partition drops; legal hold flags |
| Access audit | Log who queried which asset history |
| Export | Minimum fields; approval workflow for bulk export |
| Public sharing | Avoid exact home locations; use geohash coarsening |

Coordinate with legal/compliance on **lawful basis**—implement technical controls only.

## Monitoring and runbooks

| Metric | Alert when |
|---|---|
| Ingest lag p99 | Above SLA (e.g. > 60s) |
| Reject rate | Spike vs 7-day baseline |
| PostGIS query p95 | Bbox history > budget |
| Tile error rate | 5xx on tile endpoint |
| Geofence evaluator backlog | Queue depth sustained |

**Runbook snippets:**

- **CRS migration:** add column → backfill → dual-write → cutover → drop old
- **Replay day:** pause derived jobs → replay Kafka topic with keys → rebuild trips
- **Map vendor outage:** serve raw tracks; flag `matched=false` in API

Hand off production incidents to `site-reliability-engineer` when SLOs and infra are involved.
