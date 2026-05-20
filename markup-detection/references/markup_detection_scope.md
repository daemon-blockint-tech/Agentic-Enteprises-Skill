# Markup detection scope and boundaries

## Purpose

Define what **markup detection** and **content authenticity assessment** cover in this skill, how findings differ from full forensic attribution, and which deliverables are in scope.

## Definitions

| Term | Meaning in this skill |
|---|---|
| **Markup** | Visible or hidden editorial layers—tracked changes, comments, annotations, form fields, revision XML, redacted-but-recoverable text |
| **Manipulation** | Alteration of pixels, frames, or document content after capture or authoring (compositing, inpainting, splicing, metadata spoofing) |
| **Provenance** | Documented history of creation, export, and transfer—metadata, hashes, C2PA manifests, publisher claims |
| **Synthetic media** | Machine-generated or heavily AI-assisted imagery, audio, or video presented as camera-captured |

## Engagement types

| Type | Focus | Typical outputs |
|---|---|---|
| **Triage** | Quick pass on a single asset before wider distribution | Bulleted red flags, confidence tags |
| **Incident support** | Suspected fraudulent ID, invoice, or press image | Evidence table, recommended next steps |
| **Document review** | Contract or report with disputed version | Markup inventory, hidden-text findings |
| **Platform content review** | Social repost, screenshot chain | Re-encoding caveats, metadata gaps |
| **Pre-litigation prep** | Factual memo for counsel (not legal advice) | Observations vs inferences clearly separated |

## In scope

- **Visual** tampering heuristics on images and video stills
- **Metadata** extraction and consistency checks (EXIF, XMP, container times)
- **Hashing** and file-identity comparison across copies
- **Office and PDF** markup, comments, hidden text, embedded objects
- **Workflow-level** synthetic-media and deepfake indicators
- **C2PA / content credentials** and watermark **interpretation** (verify signatures when tools allow)
- **Structured reporting** with confidence, limitations, and alternative explanations

## Out of scope (route elsewhere)

| Topic | Route to |
|---|---|
| Train or evaluate ML detectors | `ml-research-engineer-safeguards` |
| Design steganographic or crypto watermarks | `cryptographer-specialist` |
| Disk imaging, memory forensics, malware reverse engineering | `digital-forensics-analyst`, `reverse-engineer` |
| Pentest, exploit development | `penetration-tester`, `ai-redteam` (for LLM abuse) |
| Audit opinions, SOC 2, control testing | `auditor`, `compliance-engineer` |
| On-chain wallet tracing only | blockint / investigation skills |
| Legal opinions on fraud or admissibility | counsel |

## Relationship to adjacent roles

- **Information security engineer** — implements DLP, logging, and integrity controls; this skill **assesses** a specific asset.
- **Auditor** — tests control **operating effectiveness** over time; this skill examines **one artifact** or a small corpus.
- **AI red team** — adversarial testing of **LLM applications**; overlap only when synthetic **text** or **multimodal model output** is the asset under review.
- **Cryptographer specialist** — designs **signing and watermark protocols**; this skill **reads** attestations when present.

## Independence and ethics

- Do not **enhance** evidence in ways that invent pixels or remove materially relevant metadata without disclosure.
- Disclose when analysis is **non-exhaustive** (no ELAs, no lab hardware, no subpoenaed originals).
- Avoid **deanonymization** beyond what the user’s authorization and policy allow.
- For **CSAM** or imminent harm content, follow jurisdictional reporting obligations; do not redistribute illegal material.

## Minimum inputs

| Input | Why it matters |
|---|---|
| Best-quality file available | Re-encoding destroys signals |
| Claimed source and date | Establishes expected metadata profile |
| Decision context | Sets bar for confidence and depth |
| List of known edits (if any) | Separates disclosed markup from suspicious change |

## Deliverable standards

- Every strong claim needs **linked observation** (what was seen) and **confidence**.
- Include a **limitations** section (tools not run, missing originals).
- Recommend **escalation** (specialist lab, legal) when conclusions would affect rights or safety.
