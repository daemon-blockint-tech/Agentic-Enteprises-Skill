# Coordinates, projections, and formats

## Table of contents

1. [CRS policy](#crs-policy)
2. [Common CRS choices](#common-crs-choices)
3. [Reprojection rules](#reprojection-rules)
4. [Vector formats](#vector-formats)
5. [Raster formats](#raster-formats)
6. [Validation checklist](#validation-checklist)

## CRS policy

| Layer | Typical choice | Notes |
|---|---|---|
| Ingest / API exchange | EPSG:4326 (WGS84 lat/lon) | Interop default; document axis order (lon, lat) for GeoJSON |
| Storage (global fleet) | 4326 or 3857 | 4326 for degrees; 3857 only if web-map native queries dominate |
| Local metric work | UTM zone, state plane, national grid | Pick zone from asset home region; avoid mixing zones in one table |
| Distance / buffer in SQL | Geography type or projected CRS | `ST_Distance` on geography (meters) or project then measure |

**Never** mix SRIDs in one geometry column. **Always** set `ST_SetSRID` on insert and validate bounds.

## Common CRS choices

| Use case | EPSG examples |
|---|---|
| Worldwide lat/lon | 4326 |
| Web map display meters | 3857 (Web Mercator)—display only; poor for high-latitude area metrics |
| US state plane | 22xx–29xx (zone-specific) |
| UTM northern hemisphere | 326xx (zone = 326 + zone number) |

## Reprojection rules

- Reproject **once** at a defined boundary (ingest, API response, or export)—not repeatedly in hot paths
- Use `ST_Transform(geom, target_srid)` in PostGIS; pin PROJ versions in production images
- For bbox queries across zones, prefer **geography** predicates or precomputed grid cells (H3/S2)
- Log **source SRID** on ingest when devices report local grids

## Vector formats

| Format | When to use | Pitfalls |
|---|---|---|
| GeoJSON | APIs, small/medium extracts | Large payloads; ring orientation; validate with `ST_IsValid` |
| Shapefile | Legacy GIS exchange | 2 GB limits; .prj required; field name length |
| FlatGeobuf / GeoParquet | Analytics interchange | Schema evolution; partition by region/time |
| MVT | Basemap overlay tiles | Simplify appropriately per zoom; attribute thinning |

**GeoJSON conventions:** RFC 7946, coordinates `[longitude, latitude]`, right-hand rule for polygons.

## Raster formats

| Format | When to use | Pitfalls |
|---|---|---|
| GeoTIFF | Elevation, imagery, heatmaps | CRS in geokeys; overviews; COG for cloud range reads |
| Cloud Optimized GeoTIFF (COG) | Object-store serving | HTTP range requests; internal tiling |
| PNG/WebP tiles | Cached basemaps | Not georeferenced without companion metadata |

## Validation checklist

- [ ] SRID set on every geometry inserted
- [ ] `ST_IsValid` / `ST_MakeValid` policy documented for bad polygons
- [ ] Antimeridian and pole crossings handled for global fleets
- [ ] Precision documented (decimal places vs true GNSS accuracy)
- [ ] File imports include `.prj` or explicit CRS metadata
- [ ] Simplification tolerance scales with zoom level for tiles
