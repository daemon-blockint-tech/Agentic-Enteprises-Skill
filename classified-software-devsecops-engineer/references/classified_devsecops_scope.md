# Classified DevSecOps Scope

## Purpose

Define what a **classified software DevSecOps engineer** owns in secure delivery versus adjacent roles (ISSO, classified cyber senior manager, commercial DevSecOps, platform/IaC).

## In scope

| Area | DevSecOps engineer owns | Typical collaborators |
|------|-------------------------|---------------------|
| Secure software factory | Pipeline architecture, gates, runner placement | Platform, security engineering |
| Build integrity | SBOM, signing, provenance, dependency policy | Release management, ISSO (evidence) |
| Deploy hardening | Image baseline, IaC scans, admission themes | Infrastructure, cluster ops |
| Cleared dev experience | Approved tooling paths, local build constraints | Personnel security, IT |
| Pipeline audit | Build/deploy logs, retention, tamper resistance | ISSO, compliance |
| ATO/RMF **evidence** | Scan reports, change records, control **pointers** | ISSO (SSP/POA&M) |

## Out of scope

- Portfolio-level classified cyber governance, inspection leadership, government escalation
- SSP authorship, POA&M ownership, assessor negotiation as system ISSO
- Enterprise GRC charter, framework selection, commercial SOC 2-only programs
- Hands-on pentest, malware RE, or red-team exploit development
- Legal classification, export control determinations, or contract interpretation

## Environment archetypes

### Connected enclave (policy-constrained)

- Outbound internet restricted or proxied; artifact repos may be internal mirrors only
- Third-party packages ingested through approved vetting workflows
- CI may reach internal package mirrors but not arbitrary registries

### Disconnected / air-gapped build

- Build runners have no route to public internet; dependencies arrive via approved transfer
- Tooling versions pinned; offline vulnerability DBs or periodic sync windows
- Promotion of artifacts uses physical or one-way transfer mechanisms (program-specific)

### High-side delivery

- Developers and pipelines operate at higher classification; downstream consumers may be lower
- Promotion requires boundary controls, labeling themes, and verification at handoffs (see artifact promotion reference)
- Never reproduce operational transfer procedures in chat—reference program SOPs

## RACI themes (delivery-focused)

| Activity | DevSecOps | ISSO | Classified cyber Sr Mgr | Platform/Infra |
|----------|-----------|------|----------------------|----------------|
| Pipeline design | R/A | C | I | C |
| Security gate policy | R/A | C | I | C |
| SSP control narrative | C | R/A | I | C |
| Authorization decision | I | C | C | I |
| Runner/host baseline | C | C | I | R/A |
| Incident in pipeline | R (fix) | I | C | C |

*R = responsible, A = accountable, C = consulted, I = informed — adjust to program RACI.*

## Intake questions

1. What is the **authorization boundary** for systems this pipeline deploys?
2. What **connectivity** do build runners have (none, proxy, full)?
3. Who **signs releases** and who **approves promotion** across stages?
4. Which **controls** must pipeline evidence satisfy (e.g., CM, SI, SA, RA families at high level)?
5. Are **containers** in scope? Who owns base image gold standards?
6. What **retention** applies to build logs and scan artifacts?

## Deliverable quality bar

- Architecture diagrams show trust zones, not internal hostnames or tenant IDs
- Gate matrix is testable: tool, trigger, fail/warn, exception owner
- Evidence index maps artifacts to control IDs **as pointers** for ISSO—not duplicate SSP text

## Handoff to ISSO

Provide:

- Last green pipeline run ID (or internal equivalent) per release
- SBOM + signature verification record
- Aggregated scan summary (critical/high open with exceptions)
- Change ticket linking commit → deploy
- Known gaps explicitly listed for POA&M consideration

## Anti-patterns

- Treating pipeline green as authorization to operate
- Storing long-lived cloud keys in CI variables on classified programs
- Skipping image scan because builds are "internal only"
- Copying commercial `devsecops` gate thresholds without program baseline review
- Embedding classification markings or customer data in SBOMs or logs shared broadly
