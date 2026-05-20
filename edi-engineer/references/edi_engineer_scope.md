# EDI engineer scope

## Table of contents

1. [Role boundaries](#role-boundaries)
2. [In scope](#in-scope)
3. [Out of scope](#out-of-scope)
4. [Systems of record](#systems-of-record)
5. [Lifecycle phases](#lifecycle-phases)
6. [Healthcare variant](#healthcare-variant)
7. [Deliverables checklist](#deliverables-checklist)

## Role boundaries

The EDI engineer owns **how structured B2B messages move, validate, transform, and reconcile** between trading partners and internal applications. Own the **integration layer**: parsers, mappers, validators, routers, ack generators, transport adapters, and operational tooling—not corporate supply chain strategy, warehouse UI workflows, or generic API design unless EDI is the payload contract.

Coordinate with:

- **ERP/OMS/WMS teams** for canonical object definitions and posting rules
- **Infrastructure/security** for certificates, AS2 endpoints, SFTP keys, secrets rotation
- **Partner managers** for trading partner agreements, SLAs, and certification windows

## In scope

| Area | Examples |
|---|---|
| **Standards** | ANSI X12 (4010/5010+), UN/EDIFACT (D96A+), TRADACOMS (legacy, as needed) |
| **Documents** | 850/855/856/810/812/832/846/940/945; ORDERS/DESADV/INVOIC/APERAK/CONTRL |
| **Mapping** | Segment/loop ↔ canonical PO, ASN, invoice, inventory, remittance |
| **Validation** | Syntax, envelope, IG rules, SNIP (retail), partner-specific edits |
| **Acks** | 997/999, 824/864 application advice; CONTRL, APERAK |
| **Transport** | AS2, SFTP, FTP, VAN handoff patterns, MDN handling |
| **Operations** | Monitoring, replay, quarantine, reconciliation, partner cutover |

## Out of scope

- Building WMS pick/wave logic or RF screens → `wms-developer`
- Defining supplier scorecards or network design without EDI → `supply-chain-manager`
- Writing microservices with no EDI contract → `senior-software-engineer`
- HIPAA security risk assessment program → `compliance-engineer`
- Mixed-integer routing models → `operations-research-algorithm-developer`

## Systems of record

Assign explicitly per entity:

| Entity | Typical SOR | EDI role |
|---|---|---|
| **Purchase order** | ERP or OMS | Inbound 850 / ORDERS → canonical PO |
| **Order ack** | ERP | Outbound 855 / ORDRSP |
| **Shipment / ASN** | WMS or TMS | Outbound 856 / DESADV |
| **Invoice** | ERP AR | Outbound 810 / INVOIC |
| **Inventory** | ERP or WMS | 846 / INVRPT snapshots |
| **Remittance** | ERP AP / bank | Inbound 820/835 (concept) |

EDI layer must not become SOR for business truth—persist **canonical documents** and **interchange audit**, then post to domain systems with idempotent keys.

## Lifecycle phases

1. **Discover** — IG, sample files, transaction frequency, direction, code lists
2. **Model** — canonical schema, keys, UOM, dates, references, taxes/charges
3. **Map** — segment rules, loops, conditions, defaults, code conversions
4. **Validate** — syntax + partner + business matrices
5. **Connect** — transport, certs, test mailbox, certification
6. **Test** — unit maps, partner cert, negative cases, volume soak
7. **Cutover** — parallel run, reconciliation, rollback triggers
8. **Operate** — monitor, replay, IG change management, periodic recon

## Healthcare variant

834 (enrollment), 835 (payment/remittance), 837 (claims) share X12 mechanics but impose **stricter privacy and companion-guide complexity**.

- Treat PHI as **classified data**: redact in logs, tickets, and skill outputs
- Reference **companion guides** and payer-specific edits without copying member or clinical content
- Coordinate HIPAA technical safeguards with `compliance-engineer`; do not substitute legal attestation

## Deliverables checklist

- [ ] Partner profile (ISA/GS or UNB IDs, versions, charset, test/prod)
- [ ] Transaction set inventory with direction and frequency
- [ ] Canonical model and mapping spec with samples
- [ ] Validation rule catalog with severity and owner
- [ ] Ack and exception workflow diagram
- [ ] Transport runbook (cert rotation, MDN failures)
- [ ] Certification sign-off and cutover plan
- [ ] Reconciliation job definitions and tolerance thresholds
