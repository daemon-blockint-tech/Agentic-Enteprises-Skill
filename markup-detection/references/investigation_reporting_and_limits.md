# Investigation reporting and limits

## Purpose

Standardize **how to report** markup and authenticity findings with explicit **confidence**, **limitations**, and **boundaries**—without legal conclusions or forensic overclaim.

## Table of contents

1. [Confidence scale](#confidence-scale)
2. [Finding structure](#finding-structure)
3. [Report template](#report-template)
4. [Evidence annex](#evidence-annex)
5. [Limitations catalog](#limitations-catalog)
6. [Disclaimers](#disclaimers)
7. [Peer handoffs](#peer-handoffs)

## Confidence scale

| Level | Definition | When to use |
|---|---|---|
| **High** | Multiple independent layers agree; originals available; tools validated | Rare for tampering claims without lab |
| **Medium** | Strong single-layer signal with plausible benign alternative ruled out partially | Internal triage proceed-with-caution |
| **Low** | Heuristic only, re-encoded copy, or single weak indicator | Default for social screenshots |
| **Inconclusive** | Insufficient data or conflicting signals | Recommend more evidence |

Rules:

- **Never** label “High” on ELA or detector score alone
- Downgrade one level if only **derivative copies** exist
- Upgrade only with **corroboration** across visual + metadata + manifest (any two)

## Finding structure

Each finding should include:

1. **ID** — FIND-001
2. **Category** — Visual / Metadata / Document markup / Synthetic / C2PA
3. **Observation** — factual description of what was measured or seen
4. **Inference** — what it might imply (clearly labeled)
5. **Confidence** — High / Medium / Low / Inconclusive
6. **Alternatives** — benign explanations considered
7. **Evidence refs** — file hash, frame timecode, tool output name

## Report template

```markdown
# Content authenticity assessment — [short title]

**Date:** YYYY-MM-DD  
**Analyst role:** Markup detection (workflow triage; not legal or lab forensics)  
**Requestor / context:** [internal team, incident ID]  
**Assets:** [list with SHA-256]

## Executive summary
[3–5 sentences: question asked, overall assessment tier, key limitation]

## Scope
- In scope: [files and checks performed]
- Out of scope: [lab forensics, legal opinions, model training, etc.]

## Findings summary
| ID | Category | Confidence | One-line summary |
|----|----------|------------|------------------|

## Detailed findings
[Repeat finding structure per item]

## Provenance timeline
| Time (UTC) | Event | Source |
|------------|-------|--------|

## Limitations
[Bullets from limitations catalog below]

## Recommendations
1. [Obtain original / C2PA-preserving export / specialist lab]
2. [Policy or legal review if needed]

## Tools and methods
| Tool | Version | Use |
|------|---------|-----|
```

## Evidence annex

Maintain:

- **Hash list** for every file analyzed
- **Metadata dumps** (raw EXIF/XMP, PDF info)
- **Screenshots** of tool outputs (label as derivative)
- **C2PA manifest** exports when present
- **Chain-of-custody note** if formal forensics will continue elsewhere

Do not include **illegal**, **highly sensitive**, or **unnecessary PII** in shared annexes.

## Limitations catalog

Copy applicable items into every report:

- Analysis performed on **copies**; originals not available
- **Re-encoding** via [platform] may have removed metadata and forensic signals
- **No hardware** acquisition of source device
- **No specialist lab** techniques (PRNU, advanced audio phonetics, etc.)
- **Detector tools** not run or not licensed for this engagement
- **C2PA** absent or failed validation; credentials not checked against custom trust store
- **Timezone / clock** accuracy not verified
- **Intent** not assessed—manipulation ≠ fraud without context
- **Language / jurisdiction** for admissibility not evaluated

## Disclaimers

Standard footer (adapt to org policy):

> This assessment is technical triage based on available files and stated methods. It is not legal advice, not a expert witness opinion, and not a guarantee of authenticity or inauthenticity. Strong conclusions may require specialist forensic examination and preserved originals.

## Peer handoffs

| Need | Skill / role |
|---|---|
| Implement monitoring, DLP, logging | `information-security-engineer` |
| Audit-ready control testing | `auditor`, `compliance-engineer` |
| Crypto signing / watermark design | `cryptographer-specialist` |
| LLM app abuse testing | `ai-redteam` |
| Formal disk / memory forensics | `digital-forensics-analyst` |
| AI governance policy for synthetic media | `ai-risk-governance` |
| Detector research / training | `ml-research-engineer-safeguards` |
