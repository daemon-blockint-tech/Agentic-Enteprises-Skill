# Validation and acknowledgments

## Table of contents

1. [Validation layers](#validation-layers)
2. [Syntax validation](#syntax-validation)
3. [Implementation guide rules](#implementation-guide-rules)
4. [SNIP and business edits](#snip-and-business-edits)
5. [Functional acknowledgments](#functional-acknowledgments)
6. [Application advice and exceptions](#application-advice-and-exceptions)
7. [Quarantine workflow](#quarantine-workflow)
8. [Severity model](#severity-model)

## Validation layers

Apply in order; short-circuit only when partner requires early ack:

| Layer | Catches | Typical action |
|---|---|---|
| **Transport** | MDN failure, signature, size limits | Retry / alert |
| **Syntax** | Bad envelopes, segment counts, missing terminators | Reject + 997/CONTRL |
| **IG / partner** | Wrong qualifiers, forbidden segments | Reject or quarantine |
| **Business / SNIP** | Invalid combos, totals mismatch | Quarantine + partner notify |
| **Posting** | ERP reject (unknown SKU) | Application exception queue |

## Syntax validation

**X12**

- ISA length and fixed fields; GS/ST nesting; SE segment count match
- Valid segment IDs; element length per dictionary; mandatory elements present
- Composite elements and repetition separators respected

**EDIFACT**

- UNB/UNH/UNT/UNZ consistency; message reference uniqueness within interchange
- Service string advice; release character handling

Return **machine-readable error lists** (segment, position, element, code) for ack generation and ops UI.

## Implementation guide rules

Partner **implementation guides (IGs)** override general standards:

- Which segments are **mandatory vs optional**
- Allowed code values and qualifiers
- Maximum loop iterations and trailer requirements
- Usage notes (e.g. single GS per ISA vs multiple)

Version IGs in partner profile; run validation against **IG version + effective date**.

## SNIP and business edits

**SNIP** (retail grocery/supply chain) profiles add cross-segment business rules—e.g. PO line totals, allowance consistency, 856 HL structure.

Implement as **rule packs** separate from syntax:

- Configurable per partner/industry
- Each rule: ID, description, severity, remediation hint
- Support **waivers** with expiry for cert periods only

## Functional acknowledgments

**X12 997 / 999**

- **997** — functional accept/reject at group or transaction level (AK1/AK2/AK5)
- **999** — implementation-level errors with IK segments (5010+)

Generate promptly when partner SLA requires; include **accurate AK5/IK5** codes.

**EDIFACT CONTRL**

- Report syntax and service-level acceptance for UNH/UNG/UNB
- Link to original control references for partner correlation

**Timing**

- Define SLA (e.g. ack within 15 minutes of receipt)
- Async generation acceptable if interchange already persisted with status `received`

## Application advice and exceptions

When syntax passes but **business posting fails**:

- X12 **824/864** or partner-specific **APERAK** (EDIFACT) for application-level errors
- Include canonical document ID, error code, field path, partner reference numbers

Distinguish:

- **Reject** — do not process; partner must resend
- **Accept with errors** — partial line accept; document remaining exceptions
- **Hold** — await master data fix then replay from canonical store

## Quarantine workflow

```
Receive → Syntax OK? → Map → Business OK? → Post
                ↓ no          ↓ no
            997/CONTRL    Quarantine queue
                              ↓
                    Ops: fix map / master data / contact partner
                              ↓
                         Replay (idempotent)
```

Quarantine record must store: raw payload hash, parsed tree, validation report, partner ID, timestamps, assignee, resolution code.

## Severity model

| Severity | Meaning | Example |
|---|---|---|
| **Fatal** | Do not ack accept; reject interchange | Invalid ISA |
| **Error** | Reject transaction set | Missing mandatory PO1 |
| **Warning** | Accept with note | Optional date defaulted |
| **Info** | Log only | Non-standard but allowed by waiver |

Document partner-specific overrides—some retailers treat warnings as fatal.
