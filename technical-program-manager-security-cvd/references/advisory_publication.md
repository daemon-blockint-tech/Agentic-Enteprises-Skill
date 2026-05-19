# Advisory and publication

## Table of contents

1. [Publication checklist](#publication-checklist)
2. [Advisory content](#advisory-content)
3. [CVE coordination](#cve-coordination)
4. [Customer and support](#customer-and-support)

## Publication checklist

Gate before public release:

- [ ] Fix validated in production (or supported releases listed)
- [ ] Security advisory draft — technical accuracy reviewed by engineering
- [ ] Legal approval — wording, liability, credit
- [ ] Comms approval — blog, social, press hold release if needed
- [ ] CVE ID reserved or published per CNA process
- [ ] Support / KB article for customer-facing impact
- [ ] Bounty reward processed (if applicable)
- [ ] Reporter notified **before** public post (embargo lift)
- [ ] Internal distribution — sales, CS, exec briefing if customer impact

**Go/no-go** — CVD DRI + security lead + legal; comms for external-facing.

## Advisory content

Typical sections (counsel may edit):

| Section | Purpose |
|---|---|
| Summary | What is affected; severity |
| Impact | Confidentiality, integrity, availability |
| Affected versions | Builds, regions, SKUs |
| Mitigation | Upgrade path, config workaround |
| Credit | Researcher name/handle if permitted |
| Timeline | Optional: reported, fixed, published dates |

Avoid: exploit recipes, unnecessary attack detail, customer-identifying data.

## CVE coordination

| Step | Owner |
|---|---|
| Determine CNA path | CVE coordinator |
| Request CVE | Metadata: product, version, CWE |
| Sync CVE text | Match advisory; avoid contradictory scores |
| Publish | MITRE / vendor feed per CNA rules |

Track **CVE state** in disclosure tracker (reserved → published).

## Customer and support

- **Severity to customers** may differ from internal severity (communicate impact, not CVSS alone)
- Prepare **FAQ** for support: symptoms, detection, upgrade steps
- **Notification** — email, in-app, status page per policy and contracts
- Log **customer comms sent** time relative to advisory URL live

For regulated or contractual disclosure windows, legal owns interpretation — TPM tracks deadlines.
