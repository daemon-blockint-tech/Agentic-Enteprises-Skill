# Third-party and supply-chain risk

## Table of contents

1. [Tiering model](#tiering-model)
2. [Inherent risk factors](#inherent-risk-factors)
3. [Assessment depth](#assessment-depth)
4. [Supply-chain extensions](#supply-chain-extensions)
5. [Concentration and fourth parties](#concentration-and-fourth-parties)
6. [Lifecycle events](#lifecycle-events)

## Tiering model

Tier vendors before deep assessment:

| Tier | Typical criteria | Review cadence |
|---|---|---|
| T1 Critical | Production data, admin access, single-source, regulated | Annual + continuous monitoring |
| T2 Important | Internal data, integration, moderate spend | Annual |
| T3 Standard | Limited data, replaceable, low spend | Every 2–3 years or on change |
| T4 Low | No sensitive data, no integration | Lightweight attestation |

Align tier with **inherent risk** in the enterprise register; one vendor may map to multiple scenarios.

## Inherent risk factors

Score or tag vendors on:

- **Data**: PII, PHI, PCI, credentials, source code, AI training data
- **Access**: Production, network, IdP federation, break-glass
- **Criticality**: Outage duration if vendor fails
- **Substitutability**: Switching cost and time
- **Geography**: Residency, sanctions, political exposure
- **Concentration**: % of revenue or workloads on one provider

Do not conflate **vendor financial health** with security tier without separate finance input.

## Assessment depth

| Tier | Minimum evidence |
|---|---|
| T1 | Security questionnaire (SIG/CAIQ/custom), SOC 2 Type II or ISO 27001, pen test summary if available, subprocessors, incident history |
| T2 | Questionnaire + certification or detailed security doc |
| T3 | Short questionnaire or public trust center |
| T4 | Terms review for data handling only |

Gap findings become **register rows** or feed existing rows; assign remediation owner (vendor manager + `information-security-engineer` for technical gaps).

## Supply-chain extensions

Beyond SaaS vendors:

- **Software dependencies**: SBOM risk themes (unmaintained libs, typosquat)—coordinate with `devsecops` for pipeline controls
- **Hardware / OEM**: firmware, support EOL—coordinate with procurement
- **Managed service providers**: shared tenancy, staffing access
- **Open source**: license and maintainer risk for embedded components

Risk analyst frames **scenario and residual**; does not run SCA tools.

## Concentration and fourth parties

Flag **concentration risk** explicitly:

- Single hyperscaler region for all production
- One IdP, one email security vendor, one backup provider
- Subprocessors not disclosed for T1 vendors

Require **fourth-party** list for T1 contracts where possible; inherit subprocessors into scenario library (e.g., "primary vendor breach via unknown subprocessor").

## Lifecycle events

Re-tier or reassess on:

- New data type or production integration
- Acquisition, merger, or hosting change
- Public breach or sustained outage
- Contract renewal (use as forcing function)
- Offboarding: confirm data return/deletion risks until exit complete

Hand legal and privacy questions to counsel; provide **risk tier and required clauses list** only.
