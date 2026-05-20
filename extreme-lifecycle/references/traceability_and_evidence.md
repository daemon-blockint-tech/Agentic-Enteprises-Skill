# Traceability and evidence

## Table of contents

1. [Purpose](#purpose)
2. [Traceability dimensions](#traceability-dimensions)
3. [Traceability matrix structure](#traceability-matrix-structure)
4. [Evidence types](#evidence-types)
5. [Independence and integrity](#independence-and-integrity)
6. [Retention and audit trail](#retention-and-audit-trail)
7. [Gap management](#gap-management)
8. [Interfaces to assurance and ATO](#interfaces-to-assurance-and-ato)

## Purpose

**Traceability** proves that what runs in production **implements approved intent** and was **verified** before promotion.

**Evidence** is the durable record that gates were satisfied—usable by operations, assurance, and auditors without re-deriving history from chat logs.

## Traceability dimensions

Maintain links across (minimum):

| From | To |
|---|---|
| Mission / capability need | Requirement or epic |
| Requirement | Design element / interface spec |
| Design | Implementation unit (module, service, IaC module) |
| Implementation | Test case / assessment |
| Test | Gate / release record |
| Release | Production baseline manifest |
| Baseline | Operations config and monitoring |
| System | Disposition record at retire |

**Bidirectional:** support impact analysis when any downstream artifact changes.

## Traceability matrix structure

Example columns (tool-agnostic):

| ID | Requirement | Design ref | Build ref | Test ref | Gate | Baseline ver | Status |
|---|---|---|---|---|---|---|---|
| REQ-001 | … | DES-12 | commit/IaC tag | TC-44, ASMT-3 | G4 | BL-2026.03.1 | Closed |

**Status values:** Proposed, Implemented, Verified, Deployed, Retired, Waived (with waiver ID).

**Freeze snapshots:** at each gate, export matrix version aligned to baseline tag.

## Evidence types

| Type | Examples | Typical phase |
|---|---|---|
| **Decision** | Gate minutes, risk acceptance, waiver | All gates |
| **Design** | ADR, ICD, data flow, control narrative | Design |
| **Build** | SBOM, build logs, signed artifacts | Build |
| **Verify** | Test reports, scan results, pen test summary (interface) | Verify |
| **Deploy** | Change record, deployment log, rollback test | Deploy |
| **Operate** | Runbook version, drill results, incident postmortems | Operate |
| **Sustain** | Patch compliance, EOL notices, refresh completion | Sustain |
| **Dispose** | Data disposition log, destruction certificate | Dispose |

Pair **compliance-engineer** when evidence must feed **automated control monitoring**.

## Independence and integrity

| Control | Practice |
|---|---|
| **Separation of duties** | Distinct roles for build, test, approve where policy requires |
| **Immutable artifacts** | Signed images, locked IaC tags, content hashes in manifest |
| **Tamper-evident storage** | WORM, versioning, access logging on evidence repository |
| **Human-readable index** | Manifest lists artifact ID, hash, location, custodian |

Do not rely on ticket comments alone as authoritative evidence.

## Retention and audit trail

Define per assurance level:

| Level | Retention guidance (adapt to policy) |
|---|---|
| **High** | Life of system + statutory period; gate packets immutable |
| **Moderate** | Multiple years; major baselines retained |
| **Low** | Org minimum; still retain production baseline history |

**Audit trail** includes: who approved, when, which baseline, which environment, superseded versions.

## Gap management

| Gap type | Action |
|---|---|
| **Missing link** | Block gate or conditional pass with dated remediation |
| **Orphan test** | Map to requirement or retire test |
| **Undocumented production drift** | Emergency change process; reconcile baseline |
| **Stale evidence** | Re-verify or re-baseline before next gate |

Track gaps in a **living register**; gate reviews summarize open count and trend.

## Interfaces to assurance and ATO

This skill **does not** own ISSO/ATO packages. It **supplies**:

- Traceability matrix exports
- Gate decision records
- Baseline manifests
- Verification summaries mapped to control **interfaces** (generic)

**Assurance consumers** map artifacts to control frameworks; use `stakeholders_and_assurance_interfaces.md` for RACI.

**DevSecOps** supplies pipeline evidence (scans, approvals); lifecycle ties pipeline runs to **baseline promotion** events.
