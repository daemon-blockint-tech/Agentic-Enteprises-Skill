# Document integrity and metadata

## Purpose

Guide **document markup discovery** and **metadata forensics** for Office files, PDFs, email containers, and raster exports—complementing visual tampering checks.

## Table of contents

1. [Document markup and hidden content](#document-markup-and-hidden-content)
2. [PDF-specific integrity](#pdf-specific-integrity)
3. [Office Open XML](#office-open-xml)
4. [Email and archives](#email-and-archives)
5. [EXIF and XMP on images](#exif-and-xmp-on-images)
6. [Hashes and file identity](#hashes-and-file-identity)
7. [Timestamp interpretation](#timestamp-interpretation)
8. [Metadata spoofing awareness](#metadata-spoofing-awareness)

## Document markup and hidden content

- **Tracked changes** — insertions/deletions not accepted; compare display vs stored revision XML
- **Comments and annotations** — author identity, unresolved threads, deleted-but-recoverable comment history
- **Hidden text** — font color matching background, hidden paragraph flag, collapsed outline levels
- **White-on-white** or **microfont** text in contracts and invoices
- **Embedded objects** — OLE packages, linked spreadsheets, external URLs in macros (route malware concerns separately)
- **Form fields** — default values changed after signing workflow claimed complete

## PDF-specific integrity

- **Incremental updates** — multiple generations in one file; prior object versions may remain recoverable
- **Revision history** — some editors embed change logs in proprietary ways
- **Redaction failures** — black boxes overlaying text still selectable or extractable underneath
- **Digital signatures** — validate certificate chain, coverage (what is signed), and post-sign modifications
- **JavaScript / actions** — unexpected launch actions (security issue distinct from markup)
- **XMP metadata** — `CreatorTool`, `CreateDate`, `ModifyDate`, custom keys

## Office Open XML

- Unzip `.docx`/`.xlsx`/`.pptx` (OOXML) and inspect:
  - `word/document.xml`, `word/comments.xml`, `word/revisions.xml` (when present)
  - `docProps/core.xml` and `app.xml` for author and timestamps
  - `customXml/` for workflow or DMS residue
- Compare **printed/PDF export** vs **editable source** when dispute is “what was shared”
- Watch **template** and **theme** paths revealing internal share locations

## Email and archives

- **EML/MBOX** — `Received` hops vs `Date` header; MIME boundaries for altered attachments
- **TNEF winmail.dat** — nested attachments with separate metadata
- **S/MIME or PGP** signatures on messages (integrity of body, not necessarily attachments)

## EXIF and XMP on images

| Field | Interpretation caveats |
|---|---|
| `DateTimeOriginal` | May be wrong if camera clock unset; absent after edit |
| `Software` | Shows export tool; not proof of malice |
| `GPS*` | May be stripped for privacy; spoofable |
| `Make` / `Model` | Missing in screenshots and AI outputs |
| `Orientation` | Mismatch vs displayed pixels suggests re-save |
| XMP `History` | Some editors append edit steps |

## Hashes and file identity

- Compute **SHA-256** on received bytes; record before any conversion
- Compare hashes across **purported duplicates** from different sources
- **Perceptual hashes** (pHash) — similarity for near-duplicates; not cryptographic proof
- Note **hash collision** risk is theoretical for SHA-256; focus on process integrity

## Timestamp interpretation

- Distinguish **filesystem** times (copy time) from **internal** metadata times
- **Timezone** offsets in EXIF vs UTC in PDF XMP
- **Container** `mtime` after cloud sync may reflect upload, not capture
- **Versioned storage** (SharePoint, Drive) — use platform audit logs when available (outside this skill’s file-only pass)

## Metadata spoofing awareness

- EXIF and PDF info dict are **editor-controlled**—treat as **claims**, not ground truth
- Correlate metadata with **visual** and **structural** evidence
- **Screenshot of metadata** is weaker than extracted tool output from original file

## Workflow

1. Inventory **file types** and versions received
2. Extract metadata with **documented tools**; save raw dumps in evidence annex
3. Run **markup extraction** (comments, revisions, hidden text)
4. Cross-check **author strings** and **timestamps** against known timeline from user
5. Flag **gaps** (stripped EXIF) as limitations, not automatic guilt
