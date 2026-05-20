# Sharing, STIX, and confidence

## Table of contents

1. [Handling and distribution](#handling-and-distribution)
2. [STIX 2.x essentials](#stix-2x-essentials)
3. [TAXII concepts](#taxii-concepts)
4. [Confidence expressions](#confidence-expressions)
5. [Analytic standards](#analytic-standards)

## Handling and distribution

1. Apply **TLP** or org equivalent to every product (CLEAR, GREEN, AMBER, RED)
2. Record **audience** — SOC, hunt, IR, exec, partner, ISAC
3. Respect **license and contract** limits on commercial feed redistribution
4. **Sanitize** internal data before ISAC or partner share (IPs, victim names, employee PII)
5. Maintain **distribution list** and version history when intel is updated or retracted

Do not share beyond authorized channels because “it helps defenders.”

## STIX 2.x essentials

STIX is a **structured language** for cyber threat intel objects and relationships. Common objects:

| Object | Purpose |
|---|---|
| **indicator** | Observable pattern (hash, domain, etc.) |
| **malware** | Malware family or instance |
| **threat-actor** | Actor or group representation |
| **campaign** | Coordinated activity over time |
| **attack-pattern** | TTP aligned to ATT&CK |
| **relationship** | Links objects (`uses`, `attributed-to`, `indicates`) |
| **report** | Wrapper for human-readable intel |

**Bundle** — container exporting objects for sharing. **Sightings** — observed indicator matches (when consumers feed back).

CTI should understand STIX enough to **spec requirements** for engineers and **validate** exports; implementation belongs primarily with `information-security-engineer`.

## TAXII concepts

**TAXII** is an **application protocol** to exchange STIX content over HTTPS:

- **API roots** and **collections** — subscribed feeds (commercial, ISAC, government)
- **Poll vs push** — batch pull vs automated ingestion
- Authentication (API keys, mTLS) per server

TAXII does not replace **vetting**—automated ingestion still requires scoring, dedup, and expiration in the SOC pipeline.

## Confidence expressions

Use a **defined scale** consistently (example):

| Level | Meaning |
|---|---|
| **High** | Multiple independent sources; strong technical corroboration |
| **Moderate** | Credible single source or weak corroboration |
| **Low** | Plausible but unverified; single weak source |
| **Unknown** | Insufficient data |

Apply confidence to:

- **Analytic judgments** (actor attribution, intent, forecast)
- **Individual IOCs** (malicious in stated context)
- **TTP claims** (observed vs inferred)

Use **likelihood language** carefully: “likely” must map to your scale definition.

## Analytic standards

1. **Key judgments** upfront with confidence
2. **Sources described** — not necessarily named publicly if handling restricts
3. **Assumptions and gaps** explicit
4. **Change conditions** — what would invalidate the assessment
5. **Dissent** — alternate hypotheses when team disagrees
6. **No legal conclusions** — intel supports counsel; does not replace it

For STIX, embed confidence in `confidence` fields and human-readable `report` objects when publishing technically.
