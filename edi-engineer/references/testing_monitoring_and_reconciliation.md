# Testing, monitoring, and reconciliation

## Table of contents

1. [Test pyramid](#test-pyramid)
2. [Golden files and fixtures](#golden-files-and-fixtures)
3. [Certification testing](#certification-testing)
4. [Production monitoring](#production-monitoring)
5. [Replay and idempotency](#replay-and-idempotency)
6. [Reconciliation](#reconciliation)
7. [Incident response](#incident-response)
8. [Metrics and SLAs](#metrics-and-slas)

## Test pyramid

| Level | Scope | Tools |
|---|---|---|
| **Unit** | Segment parsers, single-field maps, code conversions | JUnit/pytest + fixtures |
| **Map integration** | Full transaction ↔ canonical | Golden file diff |
| **Validation** | Rule packs, SNIP cases | Tagged scenario catalog |
| **End-to-end** | Transport → post → ack | Staging AS2/SFTP + mock ERP |
| **Certification** | Partner-provided scripts | Partner test environment |

Fail builds on **any golden diff** unless explicit snapshot update reviewed.

## Golden files and fixtures

Organize:

```
tests/
  inbound/x12/850/partner_acme/happy_path.x12
  expected/canonical/po_acme_001.json
  inbound/x12/850/partner_acme/missing_po1.x12
  expected/errors/syntax_missing_po1.json
```

- Strip **dynamic timestamps** in comparators or normalize in test harness
- Include **edge cases**: empty optional loops, max repetitions, unicode, leading zeros
- For healthcare samples, use **synthetic** data only—no real PHI

## Certification testing

Track partner case matrix:

| Case ID | Description | In/Out | Status | Sign-off date |
|---|---|---|---|---|
| C-850-01 | New PO single line | In | Pass | |
| C-856-03 | ASN partial ship | Out | Fail | open defect |

Record **environment** (test ISA IDs), **software version**, and **map version** on sign-off PDF.

## Production monitoring

**Alerts (examples)**

- Interchange received but no ack within SLA
- MDN failure rate spike
- Quarantine depth > threshold
- Map exception rate by partner
- Reconciliation break count

**Dashboards**

- Volume by partner / document type / hour
- Latency: receive → post → ack
- Error taxonomy: syntax vs business vs posting

Log **interchange control numbers** and canonical IDs—never full PHI payloads in healthcare.

## Replay and idempotency

Persist:

- Raw payload (encrypted object store)
- Parsed representation
- Canonical document
- Posting result and external ERP keys

**Replay rules**

- Same control number + partner + direction → **dedupe** unless flagged `forceReplay` by ops
- Replay from canonical when ERP was down—skip transport re-fetch
- Re-generate outbound only if partner accepts **new** control numbers

## Reconciliation

| Check | Frequency | Action |
|---|---|---|
| PO open qty vs cum ASN | Daily | Exception report |
| ASN vs invoice lines | Daily | Deduction queue |
| 810 totals vs ERP AR | Daily | Hold payment file |
| Interchange count vs VAN bill | Monthly | Finance review |
| Inventory 846 vs WMS | Hourly | Resync snapshot |

Define **tolerance** (qty, amount, timing) per partner; escalate breaks above threshold.

**Three-way match (concept)**

PO (850) → ASN (856) → Invoice (810): align line refs, shipped qty, price, allowances before auto-approve.

## Incident response

| Symptom | Likely cause | First steps |
|---|---|---|
| Partner sees no files | Transport, cert, firewall | Check MDN, AS2 logs, SFTP disk |
| Mass 997 rejects | Deployed map/IG mismatch | Roll back map version; compare sample |
| Duplicate POs | Dedupe store cleared | Pause inbound; replay with dedupe on |
| Partial posts | ERP timeout | Replay from canonical; verify idempotency |

Document **runbooks** per partner for hypercare weeks after cutover.

## Metrics and SLAs

Partner-facing SLAs often include:

- Ack within N minutes
- Document processing within N hours
- Uptime of AS2 endpoint

Internal SLOs:

- 99.9% successful syntax processing
- < 0.1% unrecoverable quarantine without owner
- Mean time to replay < 30 minutes for sev-2

Review metrics in **monthly partner QBRs** with operations and account teams.
