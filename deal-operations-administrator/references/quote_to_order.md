# Quote to order

## Table of contents

1. [Field mapping](#field-mapping)
2. [SKU table](#sku-table)

## Field mapping

| CRM / quote field | Order form field |
|---|---|
| Account legal name | Customer name |
| Primary contact | Notice contact |
| Contract start | Effective date |
| Contract end | Term end / renewal |
| ACV | Annual fees line |
| TCV | Total contract value |
| PO number | Customer PO (if provided) |

Reconcile currency and tax treatment with finance before send.

## SKU table

Attach to internal deal folder:

| SKU | Description | Qty | Unit price | Discount | Net |
|---|---|---|---|---|---|

Must match provisioning and billing system product codes.
