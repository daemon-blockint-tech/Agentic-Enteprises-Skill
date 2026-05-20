# Classified boundaries and operations

## Table of contents

1. [Documentation-level boundaries](#documentation-level-boundaries)
2. [Classified processing rules (high level)](#classified-processing-rules-high-level)
3. [Cross-domain and interconnections](#cross-domain-and-interconnections)
4. [Physical and personnel interfaces](#physical-and-personnel-interfaces)

## Documentation-level boundaries

ISSO maintains **authorization boundary** documentation suitable for SSP and assessors:

- Logical boundary — applications, databases, services in scope
- Data flows — direction, classification, encryption at summary level
- User communities — cleared populations, roles (no PII lists in open channels)
- Out-of-scope components — explicitly excluded with rationale

**Appropriate:** "Subsystem A processes SECRET data within Enclave X; connection to Enterprise Service B is read-only via approved interface Z."

**Avoid:** Detailed firewall rule sets, crypto parameters, or operational security details that belong in controlled technical repositories.

Update diagrams when interconnections or data categories change. Version and date all figures.

## Classified processing rules (high level)

Align SSP statements with program policy without reproducing classified guides:

| Topic | ISSO documentation approach |
|---|---|
| Marking | Reference marking guide; list media types in scope |
| Storage | Media types allowed; reference secure storage standard |
| Transmission | Approved methods summary; cite standard ID |
| Printing / removable media | Allowed or prohibited per program |
| Wireless | In-scope wireless policy reference or N/A |
| Mobile / portable | If allowed, cite mobility standard |

When uncertain, route to ISSM or security manager — do not invent requirements.

## Cross-domain and interconnections

For connections spanning classification levels or security domains:

1. Identify interface owner and approving authority (program-specific)
2. Document data type, direction, and security services (filter, guard, manual review)
3. Record authorization or agreement identifier and expiration
4. Trigger significant-change process before production cutover
5. Update POA&M if interface deficiencies are known

Do not specify guard product configurations in unclassified skill outputs; reference approved interface records.

## Physical and personnel interfaces

Cross-reference (do not duplicate) in SSP:

- Facility accreditation or container approval status
- Personnel clearance and access rules (role-based summary)
- Visitor and escort requirements at high level
- Media destruction and sanitization references

Coordinate with facility security and HR security points of contact; ISSO ensures SSP **mentions** dependencies and **does not contradict** authoritative physical/personnel programs.
