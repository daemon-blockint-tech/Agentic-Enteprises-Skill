---
name: edi-engineer
description: |
  Guides design, implementation, and operation of B2B electronic data interchange—X12 and EDIFACT,
  transaction mapping (850/855/856/810/997, ORDERS/DESADV/INVOIC/APERAK), canonical-to-segment
  translation, partner implementation guides, syntax and SNIP validation, functional acks and
  exceptions, transport (AS2, SFTP, VAN), healthcare variants (834/835/837) without PHI in outputs,
  certification testing, production monitoring, idempotency and reconciliation.
  Use when the user mentions EDI engineer, electronic data interchange, X12, EDIFACT, 850 purchase
  order, 856 ASN, 810 invoice, 997 acknowledgment, EDI mapping, AS2, partner onboarding,
  implementation guide, EDI validation, or VAN—not generic API integration without EDI
  (senior-software-engineer), WMS warehouse workflows (wms-developer), supply chain strategy without
  EDI build (supply-chain-manager), healthcare compliance program only (compliance-engineer), or
  OR routing and solver math (operations-research-algorithm-developer).
---

# EDI Engineer

## When to Use

- Design or operate **B2B EDI integrations**—inbound/outbound pipelines, partner profiles, replay
- Map **canonical business objects** (order, shipment, invoice, inventory) to X12 or EDIFACT segments and loops
- Implement **partner-specific** rules from implementation guides, companion guides, and trading partner agreements
- Configure **validation**—syntax (X12 envelope/segment rules, EDIFACT UNB/UNH), implementation conventions, SNIP/business edits
- Build **acknowledgment and exception** flows—997/999, CONTRL, APERAK, negative acks, operator queues
- Onboard **trading partners**—certification, test environments, cutover, production monitoring
- Choose and operate **transport**—AS2 (sign/encrypt, MDN), SFTP/FTP, VAN mailbox patterns at integration level
- Handle **healthcare EDI** variants (834 enrollment, 835 remittance, 837 claims) as structured messaging—never embed PHI in docs or logs
- Implement **idempotency, deduplication, and reconciliation** between EDI documents and ERP/WMS/OMS state

## When NOT to Use

- Generic REST/GraphQL or event-bus integration with no EDI standards or segment mapping → `senior-software-engineer`
- WMS waves, pick paths, RF scanning, slotting, or warehouse operational logic → `wms-developer`
- Supply chain strategy, sourcing, forecast policy, or supplier QBRs without EDI implementation → `supply-chain-manager`
- SOC/ISO/HIPAA **compliance program**, audit evidence, and control attestation without EDI engineering → `compliance-engineer`
- VRP, MIP, scheduling, or solver-based routing optimization → `operations-research-algorithm-developer`
- Penetration testing or offensive security of partner endpoints → `penetration-tester`
- Legal review of trading partner contracts → `commercial-counsel`

## Related skills

| Need | Skill |
|---|---|
| WMS/ERP message consumption after canonical translation | `wms-developer` |
| Supply chain process design and inventory policy | `supply-chain-manager` |
| Application services, APIs, and integration code quality | `senior-software-engineer` |
| Audit controls, HIPAA/SOC evidence pipelines | `compliance-engineer` |
| Optimization models for routing or allocation | `operations-research-algorithm-developer` |
| Enterprise integration architecture across systems | `senior-system-architecture` |
| CI/CD and production deploy for integration services | `devops` |
| Cloud messaging and object storage for payloads | `cloud-engineer` |

## Core Workflows

### 1. Scope and boundaries

Define standards in scope (X12 version, EDIFACT release), transaction sets, direction, systems of record, and PHI handling.

**See `references/edi_engineer_scope.md`.**

### 2. Standards and message families

Select transaction sets, envelopes, and version/agency identifiers.

**See `references/standards_x12_edifact.md`.**

### 3. Mapping and translation

Build canonical models, segment/loop maps, code lists, and transformation rules.

**See `references/mapping_and_translation.md`.**

### 4. Validation and acknowledgments

Layer syntax, partner, and business validation; define ack and exception paths.

**See `references/validation_and_acknowledgments.md`.**

### 5. Transport and partner onboarding

Configure connectivity, certificates, mailboxes, certification, and cutover.

**See `references/transport_and_partner_onboarding.md`.**

### 6. Testing, monitoring, and reconciliation

Certification suites, observability, replay, and financial/operational tie-out.

**See `references/testing_monitoring_and_reconciliation.md`.**

## Outputs

- **Partner profile** — IDs, qualifiers, versions, allowed transaction sets, test vs prod endpoints
- **Canonical data model** — entities, keys, UOM, dates, references, allowance/charge patterns
- **Mapping specification** — segment/loop map, conditions, code conversions, sample in/out pairs
- **Validation matrix** — syntax, IG, SNIP/business rules, severity, remediation owner
- **Acknowledgment design** — 997/999 or CONTRL/APERAK triggers, negative ack content, SLA
- **Runbook** — stuck interchange, MDN failures, duplicate control numbers, reconciliation breaks
- **Test pack** — positive/negative cases, volume samples, certification sign-off checklist

## Principles

- Map **EDI → canonical → domain systems**; avoid EDI-shaped tables in core business schemas
- Treat every interchange as **idempotent**—control numbers, message refs, payload hash, dedupe store
- **Fail closed** on validation; route exceptions to quarantine with actionable codes—not silent drops
- Separate **test and production** profiles; never cross-wire ISA/GS or UNB interchange IDs
- Log **metadata only** for healthcare payloads—no member names, diagnoses, or claim detail in tickets
- Plan **reconciliation** jobs comparing document totals to ERP/WMS open items and payments
- Document **partner drift**—IG revisions, segment usage changes, and coordinated version upgrades
