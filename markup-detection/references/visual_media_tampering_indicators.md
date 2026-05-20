# Visual media tampering indicators

## Purpose

Provide **workflow-level** heuristics to flag possible image or video-frame manipulation. These are **screening** aids—not standalone proof.

## Table of contents

1. [Global consistency](#global-consistency)
2. [Lighting and shadows](#lighting-and-shadows)
3. [Edges, noise, and compression](#edges-noise-and-compression)
4. [Geometry and perspective](#geometry-and-perspective)
5. [Duplicate-region and splicing](#duplicate-region-and-splicing)
6. [Video-specific cues](#video-specific-cues)
7. [Common false positives](#common-false-positives)
8. [Tooling notes](#tooling-notes)

## Global consistency

- **Color cast mismatch** between subject and background (white balance not unified after composite)
- **Resolution islands** — sharper subject on softer background without depth-of-field justification
- **Histogram discontinuities** when examining regional stats (subject vs sky vs floor)
- **Chromatic aberration** present on one layer but absent on adjacent edges that should share an optical path

## Lighting and shadows

- **Shadow direction** inconsistent across objects allegedly in the same scene
- **Shadow hardness** mismatch (hard flash on face, soft ambient shadow on ground)
- **Specular highlights** on eyes or metal that do not match stated light sources
- **Missing contact shadows** where objects appear to float above surfaces
- **Night scenes** with mixed artificial sources but uniform shadow angles

## Edges, noise, and compression

- **Halos** or bright fringes around cutouts (especially hair and foliage)
- **Noise pattern change** at boundaries (sensor noise should be spatially correlated in one capture)
- **JPEG block boundaries** aligned differently across regions after double compression
- **Over-sharpened** subject on **blurred** background from selective filtering
- **Inpainting smear** — repetitive micro-texture in filled areas (sky, pavement)

## Geometry and perspective

- **Vanishing lines** that do not converge for coplanar structures
- **Scale errors** — door height vs person height implausible
- **Reflection mismatch** in mirrors, glass, or water relative to scene geometry
- **Lens distortion** absent on background but present on foreground (or vice versa) in one alleged shot

## Duplicate-region and splicing

- **Clone-stamp patterns** — repeated texture patches (clouds, grass, bricks)
- **Seam lines** visible at stitch boundaries in panoramas or manual composites
- **Different JPEG quality** on left vs right of a horizontal splice
- **Cut-line jitter** in video where frame-to-frame alignment shifts at a fixed row

## Video-specific cues

- **Temporal flicker** at composite edges when compression varies frame to frame
- **Inconsistent motion blur** on moving objects vs static background
- **Frame interpolation artifacts** after slow-motion synthesis from few source frames
- **Audio-visual mismatch** — lip movement cadence vs phonemes (see synthetic media reference for depth)

## Common false positives

| Observation | Benign explanation |
|---|---|
| Halo on subject | Social platform beauty filter or portrait mode matting |
| EXIF stripped | Messaging app or screenshot repost |
| Shadow softness change | Multiple real light sources or fill flash |
| Blockiness at edges | Aggressive recompression on chat apps |
| Panorama seam | Legitimate stitch; verify with source app metadata |

## Tooling notes

- **ELA (error level analysis)** — useful for JPEG double-save hints; **not definitive**; document tool settings
- **Clone detection** plugins — flag candidates for human review
- **Hex / structure viewers** — confirm container type vs claimed extension
- **Avoid** presenting heatmaps as court-ready proof without expert validation

## Review checklist

1. Establish **single-capture hypothesis** vs **composite hypothesis**
2. List **≥3 independent** visual observations before Medium+ confidence on tampering
3. Attempt **benign alternative** for each observation
4. Request **original file** or **RAW** if only screenshots exist
5. Record **display conditions** (HDR, OLED, browser scaling) that affect perception
