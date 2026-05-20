---
name: geospatial-telematics-developer
description: |
  Builds location-aware systems—CRS/projections; GeoJSON, Shapefile, GeoTIFF, MVT; PostGIS spatial SQL;
  indexes and tiling; OGC WMS/WFS/WMTS integration; map matching, trajectories, geofencing; fleet
  telematics (GPS/GNSS, NMEA, timestamps, CAN metadata); streams and batch ETL; location privacy/accuracy.
  Use for geospatial developer, telematics, PostGIS, GeoJSON, geofencing, fleet tracking, GPS trajectory,
  map matching, NMEA, spatial query, tile server, OGC, coordinate projection, vehicle telematics—not pure
  OR routing without geo (operations-research-algorithm-developer), autonomy fusion (sensor-fusion-engineer),
  WMS workflows (wms-developer), warehouse marts without geo (data-warehouse-engineer), generic backend
  (senior-software-engineer), simulation platforms (simulation-software-engineer), robotics without fleet geo
  (robotics-automation-integration-engineer).
---

# Geospatial and Telematics Developer

## When to Use

- Design **location-aware services**—ingest, store, query, and serve positions, trajectories, and regions
- Implement **CRS and projections**—WGS84, local projected CRS, reprojection policy, bounds checks
- Work with **vector and raster** formats—GeoJSON, Shapefile, GeoTIFF, MVT; validation and simplification
- Build **PostGIS / spatial SQL**—geometry types, predicates, indexes, aggregates, and performance tuning
- Plan **spatial indexing and tiling**—GiST/BRIN, H3/S2 grids, vector tile pyramids, cache keys
- Integrate **OGC map services**—WMS, WFS, WMTS clients; layer metadata, bbox, and auth at integration level
- Process **trajectories**—dedupe, gap-fill policy, map matching hooks, stop detection, trip segmentation
- Implement **geofencing**—enter/exit/dwell, buffered predicates, timezone and schedule rules
- Ingest **fleet telematics**—GPS/GNSS fixes, NMEA parsing, device vs server timestamps, CAN-linked metadata
- Operate **streams and batch ETL**—Kafka/Kinesis-style pipelines, late data, idempotency, replay
- Address **privacy and accuracy**—precision reduction, retention, consent, jitter, and audit needs

## When NOT to Use

- **Pure OR routing / VRP / MIP** without geospatial implementation (tiles, CRS, spatial DB, ingestion) → `operations-research-algorithm-developer`
- **Multi-sensor perception fusion** (LiDAR, radar, EKF/MOT, calibration) for autonomy → `sensor-fusion-engineer`
- **WMS warehouse workflows**—waves, pick paths, RF scanning, inventory allocation → `wms-developer`
- **Snowflake/BigQuery marts**, dbt, dimensional modeling without operational geo store → `data-warehouse-engineer`
- **Generic backend**, CRUD APIs, or cloud microservices without location domain → `senior-software-engineer`
- **Simulation platform software**—physics engines, SIL/HIL rigs, deterministic replay frameworks → `simulation-software-engineer`
- **Robotics cell integration**—PLC/AMR orchestration without fleet/geo pipeline ownership → `robotics-automation-integration-engineer`
- **Legal privacy counsel** or regulatory filings—route to legal/compliance; implement technical controls only

## Related skills

| Need | Skill |
|---|---|
| VRP, scheduling, MIP, solver-based routing optimization | `operations-research-algorithm-developer` |
| LiDAR/camera/radar/IMU fusion, tracking, calibration | `sensor-fusion-engineer` |
| Warehouse operational workflows and WMS logic | `wms-developer` |
| Analytics warehouse, dbt, BI semantic layers | `data-warehouse-engineer` |
| Enterprise application and API engineering | `senior-software-engineer` |
| DES/physics sim platforms, digital twins | `simulation-software-engineer` |
| AMR/PLC integration, material-handling automation | `robotics-automation-integration-engineer` |
| Stream/batch data platform patterns (non-geo-specific) | `analytics-data-engineer` |
| Production SLOs, on-call, incident response | `site-reliability-engineer` |

## Core Workflows

### 1. Scope and boundaries

Define geo/telematics footprint, consumers, retention, and handoffs.

**See `references/geospatial_telematics_scope.md`.**

### 2. Coordinates, projections, and formats

Pick CRS, validate geometries, and standardize exchange formats.

**See `references/coordinates_projections_and_formats.md`.**

### 3. Spatial databases and queries

Model schemas, indexes, predicates, and query plans in PostGIS or equivalent.

**See `references/spatial_databases_and_queries.md`.**

### 4. Telematics ingestion and quality

Parse device feeds, timestamp policy, quality flags, and batch/stream contracts.

**See `references/telematics_ingestion_and_quality.md`.**

### 5. Geofencing, tracking, and map matching

Rules engines, trajectory logic, and map-matching integration boundaries.

**See `references/geofencing_tracking_and_map_matching.md`.**

### 6. Serving APIs and operations

Tile/map APIs, OGC integration, monitoring, privacy controls, and runbooks.

**See `references/serving_apis_and_operations.md`.**

## Outputs

- **Location data model** — entities, geometry columns, SRID, time columns, partition keys
- **Ingestion contract** — schema, idempotency keys, late-data policy, quality dimensions
- **Spatial index and tiling plan** — indexes, grid choice, zoom levels, cache invalidation
- **Query and API spec** — predicates, bbox rules, pagination, rate limits, error codes
- **Geofence catalog** — regions, triggers, debounce, timezone rules, audit trail
- **Trajectory processing note** — segmentation, map-matching vendor boundary, stop detection
- **Privacy and retention matrix** — precision, TTL, export controls, deletion hooks
- **Operations runbook** — lag alarms, replay procedure, CRS migration checklist

## Principles

- **Fix CRS and time first** — wrong SRID or clock skew dominates downstream “algorithm” bugs
- **Store raw plus derived** — keep device fixes; derive matched/snapped layers with version pins
- **Index for real queries** — design GiST/grid indexes around bbox + time filters actually used
- **Treat ingestion as idempotent** — device sequence, dedupe keys, and replay-safe upserts
- **Separate operational geo from analytics** — OLTP/track store vs warehouse marts (`data-warehouse-engineer`)
- **Document accuracy and privacy** — horizontal accuracy, sampling rate, reduction, and lawful basis
- **Integrate OGC; do not re-spec the standards** — client patterns and failure modes, not full spec rewrite

## When to load references

| Topic | Reference |
|---|---|
| Role scope, RACI, boundaries | `references/geospatial_telematics_scope.md` |
| CRS, projections, file formats | `references/coordinates_projections_and_formats.md` |
| PostGIS, indexes, spatial SQL | `references/spatial_databases_and_queries.md` |
| GPS/NMEA, streams, data quality | `references/telematics_ingestion_and_quality.md` |
| Geofences, trips, map matching | `references/geofencing_tracking_and_map_matching.md` |
| Tiles, OGC, APIs, ops, privacy | `references/serving_apis_and_operations.md` |
