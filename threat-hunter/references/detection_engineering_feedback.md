# Detection engineering feedback

## Table of contents

1. [When to file feedback](#when-to-file-feedback)
2. [Candidate detection template](#candidate-detection-template)
3. [Tuning and false positives](#tuning-and-false-positives)
4. [Data and parser gaps](#data-and-parser-gaps)
5. [Purple team loop](#purple-team-loop)

## When to file feedback

Create detection engineering tickets when hunts find:

- **Repeatable true positives** without a production rule
- **High-value behaviors** seen once but likely to recur (living-off-the-land, cloud API abuse)
- **Systematic false negatives** due to missing fields, wrong index, or short retention
- **Alert noise** that caused SOC to miss related activity (tuning opportunity)

Do not file rules for one-off misconfigurations fixed by IT change management alone.

## Candidate detection template

| Section | Guidance |
|---|---|
| Title | Behavior + data source (e.g., “Rare cloud API CreateAccessKey from new country”) |
| Hunt ID | Link to hunt record |
| Logic summary | Plain language + pseudocode or SPL/KQL snippet |
| Data sources | Index/table, required fields |
| Expected volume | Events/day in prod (estimate from hunt stats) |
| False positive risk | Known benign cases; exclusion ideas |
| Priority | Based on impact and prevalence |
| ATT&CK | Technique IDs |
| Test plan | Historical replay window; known true/false samples |

Attach **example events** (redacted) or saved search links—not full PII dumps.

### Rule design principles

1. Prefer **behavior + context** over single IOC where possible
2. Add **rate limits** and **allowlists** for noisy admin tools
3. Stage: **dev → limited prod → full prod** with SOC review
4. Document **owner** and **review cadence** (quarterly for high-FP rules)

## Tuning and false positives

When hunts explain **why SOC missed** activity:

- List alerts that fired but were **closed incorrectly**
- Recommend **correlation** (e.g., combine IdP + EDR signals)
- Suggest **severity** or **queue** changes with evidence counts
- Propose **suppressions** with explicit expiry and approver

Never tune global rules to silence a hunt finding without root-cause review.

## Data and parser gaps

File infrastructure tickets when hunts are blocked by:

| Gap type | Example ask |
|---|---|
| Missing log source | Enable CloudTrail data events on sensitive buckets |
| Retention | Extend EDR network connection history to 90 days |
| Parser | Map `userAgent` from app logs into UDM/ECS |
| Enrichment | Add asset owner tags to IP→host mapping |
| Collection | Deploy Sysmon config update for script block logging |

Quantify impact: “Hunt H-2024-017 could not evaluate T1053 without scheduled task events on servers X–Y.”

## Purple team loop

After `red-team-specialist` or pentest exercises:

1. Import **techniques attempted** and **detection results**
2. Prioritize hunts on **undetected** techniques with realistic exposure
3. Close loop in hunt report: “Detection D-1234 added; retest on [date]”

Coordinate with purple team so hunt queries do not disrupt live operations or violate ROE.
