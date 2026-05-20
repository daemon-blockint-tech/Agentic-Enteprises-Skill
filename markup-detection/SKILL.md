---
name: Markup Detection
description: |
  This skill should be used when the user asks for markup detection, detect manipulation, image tampering,
  deepfake detection, document integrity, hidden markup, metadata forensics, EXIF analysis, content
  authenticity, synthetic media, altered image, C2PA, or provenance verification across documents,
  images, and video. Guides workflow-level assessment of visual tampering indicators (splicing, cloning,
  inconsistent lighting or shadows, compression artifacts), metadata and provenance checks (EXIF, hashes,
  source chain), document revision and hidden markup (tracked changes, comments, invisible text),
  synthetic-media and deepfake red flags, watermarking and content-credentials concepts, and structured
  reporting with confidence levels and explicit limitations—not training detection models
  (ml-research-engineer-safeguards), cryptographic watermark design (cryptographer-specialist), full
  digital forensics lab attribution or legal conclusions, or blockchain-only tracing unless the user
  scopes on-chain context.
---

# Markup Detection

## When to Use

- Assess whether **images or video** show signs of tampering, compositing, or inconsistent capture metadata
- Review **documents** (Office, PDF) for hidden markup, revision layers, comments, or undisclosed edits
- Run **metadata and provenance** checks—EXIF/XMP, file hashes, embedded timestamps, export vs capture mismatches
- Triage **synthetic media** and **deepfake** concerns using observable workflow indicators (not model training)
- Interpret **watermarks**, **C2PA / content credentials**, and publisher attestation claims at a high level
- Produce **investigation memos** with confidence tiers, evidence tables, and stated limitations
- Compare **source chain** (original upload, reposts, screenshots) when authenticity is disputed

## When NOT to Use

- Train, fine-tune, or benchmark **detection ML models** → `ml-research-engineer-safeguards`
- Design **cryptographic watermarks**, steganography, or signing schemes → `cryptographer-specialist`
- Perform **full digital forensics** with chain-of-custody, disk imaging, or courtroom expert testimony → specialized forensics vendor / `digital-forensics-analyst` (when installed)
- Conduct **authorized offensive security** or adversarial AI red teaming → `ai-redteam`, `penetration-tester`
- Map findings to **audit attestations**, SOC 2 opinions, or control effectiveness → `auditor`, `compliance-engineer`
- **Blockchain-only** address tracing, sanctions, or on-chain attribution → blockint / investigation skills unless user adds document/media context
- Issue **legal conclusions** on fraud, defamation, or admissibility → counsel; state facts and uncertainty only

## Related skills

| Need | Skill |
|---|---|
| IAM, logging, DLP, and control implementation | `information-security-engineer` |
| Adversarial testing of LLM apps and copilots | `ai-redteam` |
| Crypto signing, PKI, and watermark protocol design | `cryptographer-specialist` |
| Internal audit, evidence standards, deficiency write-ups | `auditor` |
| Technical control evidence and CCM pipelines | `compliance-engineer` |
| Production LLM features and RAG (not media forensics) | `ai-engineer` |
| AI governance and risk tiers for synthetic content policy | `ai-risk-governance` |
| Disk/memory/log forensics and chain of custody | `digital-forensics-analyst` (when installed) |

## Core Workflows

### 1. Intake and scope

1. Identify **asset type** (image, video, audio, PDF, Office, email archive, web capture)
2. Record **claimed provenance** (author, date, device, platform, original URL)
3. List **decision needed** (internal triage, incident response, press review, litigation support prep—not legal advice)
4. Note **constraints** (only copies available, re-encoded social video, missing originals)
5. Select reference files from the table below

| Topic | Reference |
|---|---|
| Scope and boundaries | `references/markup_detection_scope.md` |
| Visual tampering heuristics | `references/visual_media_tampering_indicators.md` |
| Documents, EXIF, hashes | `references/document_integrity_and_metadata.md` |
| Synthetic media / deepfakes | `references/synthetic_media_and_deepfakes.md` |
| Watermarks, C2PA, credentials | `references/watermarks_provenance_c2pa.md` |
| Reporting and limits | `references/investigation_reporting_and_limits.md` |

### 2. Preserve and catalog evidence

1. Obtain **best available originals**; avoid unnecessary re-saving that strips metadata
2. Compute **cryptographic hashes** (SHA-256) per file; record filename, size, received time
3. Capture **context screenshots** (platform UI, URLs, conversation thread) separately from the asset
4. Document **tool versions** used for extraction or enhancement
5. If chain of custody matters, route to formal forensics—do not improvise custody from this skill alone

### 3. Layered analysis

Run checks in parallel where possible; **corroborate** across layers before strong conclusions.

1. **Structural / visual** — lighting, shadows, edges, noise, perspective, duplicate regions (see visual reference)
2. **Metadata** — EXIF/XMP, container timestamps, software strings, GPS/device fields (see document integrity reference)
3. **Document markup** — tracked changes, comments, hidden text, embedded objects (see document integrity reference)
4. **Synthetic-media signals** — face boundary, blink cadence, audio-visual sync at workflow level (see synthetic reference)
5. **Attestation** — C2PA manifest, publisher credentials, visible watermarks (see watermarks reference)

### 4. Score and report

1. Classify each finding: **observed fact** vs **inference** vs **hypothesis**
2. Assign **confidence** (High / Medium / Low) per finding with rationale
3. State **alternative explanations** (heavy compression, beauty filters, legitimate edits)
4. Deliver memo using templates in `references/investigation_reporting_and_limits.md`
5. Recommend **next steps** (obtain original, specialist lab, legal review) when confidence is insufficient

## Quality bar

- Never present **heuristic suspicion** as definitive proof of manipulation
- Separate **undisclosed editorial markup** from **malicious tampering** when intent is unknown
- Call out **re-encoding**, **screenshots**, and **platform transcoding** as common false-positive drivers
- Cite **which checks were not run** when tooling or access was missing
