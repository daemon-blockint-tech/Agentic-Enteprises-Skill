# Timeline correlation and reporting

## Table of contents

1. [Super-timeline construction](#super-timeline-construction)
2. [Timeline row fields](#timeline-row-fields)
3. [Report structure](#report-structure)
4. [Expert witness preparation outline](#expert-witness-preparation-outline)
5. [Quality checks](#quality-checks)

## Super-timeline construction

1. **Ingest** exports from host, network, cloud, identity, email
2. **Normalize** timestamps to UTC; document original timezone in appendix
3. **Deduplicate** same event from multiple sensors (prefer authoritative source)
4. **Phase** events: initial access → execution → persistence → lateral → exfil → impact
5. **Annotate** confidence and open questions

Use a single master sheet or database; version control the file used for the report.

## Timeline row fields

Minimum columns:

| Column | Content |
|---|---|
| UTC time | ISO-8601 Z |
| Source | e.g., CloudTrail, Security.evtx, EDR |
| Host / account | Entity affected |
| Event type | Login, process start, API call, file write |
| Detail | Factual description (no speculation in this column) |
| Artifact ref | Evidence ID or log query |
| Confidence | Confirmed / Likely / Speculative |
| Analyst note | Optional inference, clearly labeled |

## Report structure

### Executive summary (1–2 pages)

- **What happened** (high level, factual)
- **Scope** (systems, users, dates UTC)
- **Key findings** (bullet, cited)
- **Impact** (data accessed, systems affected—factual)
- **Open questions** and recommended **next steps** (technical)

### Technical appendix

- Methodology (tools, versions, limitations)
- Evidence inventory and hashes
- Super-timeline excerpt or full attachment
- IOC table (type, value, first/last seen UTC, sources)
- Malware triage summary (if applicable)
- **Gaps** (missing logs, remediated hosts, retention limits)

### Legal/IR coordination

- Not legal advice; no criminal conclusions
- Flag items requiring **privilege review** before sharing externally
- Provide **raw exports** or counsel-approved redactions only

## Expert witness preparation outline

For counsel review only—do not draft testimony or legal strategy.

Suggested outline sections:

1. **Qualifications summary** (analyst provides résumé/CV to counsel)
2. **Engagement scope** — what was asked, what was not analyzed
3. **Methodology** — industry-accepted tools and validation steps
4. **Exhibit list** — evidence IDs mapped to trial exhibits (counsel assigns numbers)
5. **Foundation topics** — chain of custody, hashing, tool reliability (factual)
6. **Anticipated technical questions** — timeline, attribution limits, alternative explanations
7. **Limitations** — what artifacts cannot prove

## Quality checks

Before delivery:

- [ ] Every material claim has **artifact or log citation**
- [ ] UTC used consistently; timezone footnotes where needed
- [ ] Facts separated from **inference**
- [ ] Chain of custody complete for cited evidence
- [ ] IOCs validated against false-positive sources where possible
- [ ] Peer review by second analyst for SEV1 / litigation matters when policy requires
