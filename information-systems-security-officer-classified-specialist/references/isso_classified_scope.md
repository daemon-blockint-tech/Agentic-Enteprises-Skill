# ISSO classified scope

## Table of contents

1. [Role boundary](#role-boundary)
2. [System and enclave context](#system-and-enclave-context)
3. [Stakeholders and RACI](#stakeholders-and-raci)
4. [Minimum artifacts](#minimum-artifacts)

## Role boundary

| ISSO (this skill) | Partner skill |
|---|---|
| SSP stewardship, control status, POA&M, A&A package support | `classified-cyber-security-senior-manager` — multi-system classified program |
| Board strategy, risk appetite, enterprise program | `chief-information-security-officer` |
| Enterprise GRC charter, framework scope | `compliance-specialist` |
| Audit evidence automation, technical control tests | `compliance-engineer` |
| IAM, logging, EDR, remediation implementation | `information-security-engineer` |
| Reference architecture and security patterns | `enterprise-security-architect` |
| Active incident command and forensics | `incident-responder` |
| Enterprise risk register and FAIR-style scoring | `security-risk-analyst` |

**Do not** provide legal conclusions, make authorization decisions for the AO, or include export-controlled technical specifications in open outputs.

## System and enclave context

Capture at engagement start:

| Element | Notes |
|---|---|
| Authorization boundary | Hardware, software, data, personnel in scope |
| Classification | Highest level processed; caveats if applicable |
| Impact level | Confidentiality, integrity, availability per program baseline |
| Operating environment | Dedicated enclave, shared infrastructure, cloud segment |
| Interconnections | External systems, APIs, data feeds (names at unclassified summary where required) |
| Common controls | Inherited control providers and authorization dates |
| Leveraged authorizations | Other systems or services consumed |

Revalidate context after major releases, data migration, or boundary changes.

## Stakeholders and RACI

| Activity | Accountable | Responsible | Consulted | Informed |
|---|---|---|---|---|
| SSP accuracy | System owner | ISSO | Control implementers | ISSM |
| POA&M closure | System owner | ISSO track | Implementers | AO staff |
| Continuous monitoring | ISSO | Control owners | ISSM | AO |
| A&A package | System owner | ISSO assemble | Assessors | ISSM |
| Incident reporting | ISSM | ISSO notify | `incident-responder` if declared | AO, PM |
| Technical remediation | System owner | `information-security-engineer` | ISSO | ISSM |

## Minimum artifacts

Maintain current versions with version history:

1. System security plan (SSP) and appendices index
2. POA&M with risk ratings and milestone dates
3. Continuous monitoring strategy and last review record
4. Authorization decision letter (or interim) and expiration
5. Boundary and interconnection diagrams (documentation level)
6. Contingency / IR contact sheet aligned to program (not full IR playbook)
7. Significant change log since last assessment
