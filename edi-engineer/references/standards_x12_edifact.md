# Standards: X12 and EDIFACT

## Table of contents

1. [Envelope hierarchy](#envelope-hierarchy)
2. [Common X12 transaction sets](#common-x12-transaction-sets)
3. [Common EDIFACT messages](#common-edifact-messages)
4. [Version and agency identifiers](#version-and-agency-identifiers)
5. [Delimiters and character sets](#delimiters-and-character-sets)
6. [Control numbers and uniqueness](#control-numbers-and-uniqueness)
7. [Healthcare X12 (concept)](#healthcare-x12-concept)

## Envelope hierarchy

**X12 (ANSI)**

```
ISA (interchange) → GS (functional group) → ST (transaction set) → segments
```

- **ISA/IEA** — interchange control; sender/receiver IDs, standards ID, control number
- **GS/GE** — functional group; application sender/receiver, version/release, group control number
- **ST/SE** — transaction set; ST01 = transaction set ID (e.g. 850), control number

**EDIFACT (UN)**

```
UNB (interchange) → UNG (optional group) → UNH (message) → segments → UNT → UNZ
```

- **UNB/UNZ** — interchange header/trailer; syntax version, partners, control reference
- **UNH/UNT** — message header/trailer; message type (e.g. ORDERS), reference number
- **UNG/UNE** — optional functional grouping for batching related messages

## Common X12 transaction sets

| Set | Name | Typical use |
|---|---|---|
| **850** | Purchase Order | Inbound order to supplier/DC |
| **855** | PO Acknowledgment | Accept/reject/change lines |
| **856** | Ship Notice / ASN | Cartons, SSCC, ship-from/to |
| **810** | Invoice | Bill-to; match PO/ASN |
| **812** | Credit/Debit Adjustment | Price/qty corrections |
| **832** | Price/Sales Catalog | Item and price updates |
| **846** | Inventory Inquiry/Advice | Stock snapshots |
| **940** | Warehouse Shipping Order | To 3PL WMS |
| **945** | Warehouse Shipping Advice | Ship confirm from 3PL |
| **997** | Functional Acknowledgment | Accept/reject functional group or set |
| **999** | Implementation Acknowledgment | IG-level errors (5010+) |

Retail and grocery often add **894/895/816** and require **SNIP** validation profiles—call out in partner profile.

## Common EDIFACT messages

| Message | Name | X12 analog (loose) |
|---|---|---|
| **ORDERS** | Purchase order | 850 |
| **ORDRSP** | Order response | 855 |
| **DESADV** | Despatch advice | 856 |
| **INVOIC** | Invoice | 810 |
| **INVRPT** | Inventory report | 846 |
| **PRICAT** | Price catalog | 832 |
| **RECADV** | Receiving advice | 944 (concept) |
| **APERAK** | Application error | 824/864 (concept) |
| **CONTRL** | Syntax/control ack | 997 (concept) |

EDIFACT uses **composite data elements** and **coded lists** (e.g. ISO country, UN/ECE units)—map via explicit code tables, not ad hoc strings.

## Version and agency identifiers

Capture in partner profile:

| Standard | Fields | Example |
|---|---|---|
| X12 | ISA12 / GS08 | 005010, 004010 |
| X12 | ST version in GS08 | 005010UCS |
| EDIFACT | UNB syntax + version | UNOC:3, D:96A:UN |

Never assume one global version—partners drift on **different releases per document**.

## Delimiters and character sets

X12 uses configurable element, segment, and subelement separators in ISA (positions 104–105 and implied conventions). EDIFACT uses UNA or service-string advice defaults.

- Document chosen delimiters in partner profile
- Parser must **read ISA/UNA** before tokenizing—do not hardcode `*` and `~` without verification
- Support **UTF-8** where partners require multibyte; validate charset in UNB if EDIFACT

## Control numbers and uniqueness

| Level | X12 | EDIFACT |
|---|---|---|
| Interchange | ISA13 | UNB control reference |
| Group | GS06 | UNG reference |
| Transaction | ST02 | UNH message ref |

Implement **allocator + dedupe store**: reject or quarantine duplicates; allow partner-specific reuse rules only when documented.

## Healthcare X12 (concept)

| Set | Purpose | Notes |
|---|---|---|
| **834** | Enrollment | Eligibility maintenance; heavy companion guides |
| **835** | Payment / remittance | Claim payments; loop 2100+ claim detail—**no PHI in ops logs** |
| **837** | Claims | Professional/institutional/dental variants |

Use same envelope/mapping discipline; add **payer-specific edits** and stricter audit. Defer compliance program design to `compliance-engineer`.
