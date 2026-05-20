# Geospatial and telematics scope

## Table of contents

1. [Purpose](#purpose)
2. [Terminology](#terminology)
3. [In scope](#in-scope)
4. [Out of scope](#out-of-scope)
5. [Roles and RACI](#roles-and-raci)
6. [Handoffs](#handoffs)

## Purpose

Define boundaries for **building and integrating location-aware systems**—from device/fix ingestion through spatial storage, processing, and map-facing APIs.

This skill covers **implementation patterns, data contracts, and operations**—not legal privacy advice, autonomy perception fusion, or warehouse operational workflows.

## Terminology

| Term | Meaning |
|---|---|
| CRS | Coordinate reference system—defines how coordinates relate to the Earth |
| SRID | Spatial reference ID—numeric CRS identifier (e.g. 4326 for WGS84 geographic) |
| Fix | Single GNSS position sample with lat/lon and optional accuracy metadata |
| Trajectory | Time-ordered sequence of fixes for one asset |
| Map matching | Snapping raw GPS to road/path network (often vendor or graph service) |
| Geofence | Region boundary with enter/exit/dwell semantics |
| MVT | Mapbox Vector Tiles—protobuf tiles for vector map layers |
| OGC | Open Geospatial Consortium—WMS, WFS, WMTS service standards |
| PostGIS | PostgreSQL extension for spatial types and functions |
| Telematics | Fleet/vehicle location and related device metadata |

## In scope

| Area | Examples |
|---|---|
| CRS and projections | WGS84 storage, local UTM/state plane for distance, reprojection on read/write |
| Data formats | GeoJSON, Shapefile, GeoTIFF, MVT generation/consumption |
| Spatial databases | PostGIS schemas, spatial SQL, indexes, partitioning by time/region |
| Tiling and indexes | Vector/raster pyramids, H3/S2 bins, GiST/BRIN, tile cache keys |
| OGC integration | WMS/WFS/WMTS clients, GetCapabilities, bbox/layer params, auth |
| Trajectories | Dedupe, gap policy, trip segmentation, stop detection hooks |
| Geofencing | Polygon/circle fences, predicates, debounce, event emission |
| Telematics ingest | NMEA, proprietary JSON, MQTT/Kafka streams, batch files |
| Streams and ETL | Late data, watermarking, idempotent upserts, replay |
| Privacy and accuracy | Precision reduction, retention TTL, audit logs |

## Out of scope

| Topic | Route to |
|---|---|
| VRP/MIP/scheduling without geo stack | `operations-research-algorithm-developer` |
| LiDAR/camera/radar fusion, EKF, MOT | `sensor-fusion-engineer` |
| WMS pick/wave/inventory workflows | `wms-developer` |
| dbt marts, dimensional models, BI layers | `data-warehouse-engineer` |
| Generic CRUD/cloud without location domain | `senior-software-engineer` |
| Physics/DES simulation platforms | `simulation-software-engineer` |
| PLC/AMR cell integration without fleet geo | `robotics-automation-integration-engineer` |
| Legal GDPR/CCPA program interpretation | Legal / compliance |
| Turn-by-turn navigation UX product ownership | Product / mobile teams |

## Roles and RACI

| Activity | Geo/telematics dev | Fleet ops | Data platform | Security/privacy | Map vendor |
|---|---|---|---|---|---|
| Ingestion schema and quality rules | A | C | C | I | I |
| PostGIS schema and spatial indexes | A | I | C | I | I |
| Geofence catalog and rules | A | C | I | C | I |
| Map matching vendor integration | A | C | I | I | C |
| Tile/map API SLOs | A | I | C | I | C |
| Retention and precision policy | C | C | C | A | I |
| OR-based dispatch optimization | C | A | I | I | I |

## Handoffs

| To skill | When |
|---|---|
| `operations-research-algorithm-developer` | Optimization model needs distance matrices or VRP—provide clean OD inputs, not duplicate routing math in app layer |
| `sensor-fusion-engineer` | Autonomy stack needs world-frame poses—agree on frame conventions and timestamps; do not merge perception fusion into fleet ingest |
| `data-warehouse-engineer` | Analytics on trips, utilization, heatmaps—replicate or export with documented grain; keep OLTP track store authoritative |
| `senior-software-engineer` | Shared auth, billing, non-geo microservices—expose stable location APIs |
| `site-reliability-engineer` | Lag, cardinality, and incident playbooks for ingest and tile services |
