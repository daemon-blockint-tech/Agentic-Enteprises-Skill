# Logistics and fulfillment

## Table of contents

1. [Network design](#network-design)
2. [Incoterms](#incoterms)
3. [3PL management](#3pl-management)
4. [Lead time and buffers](#lead-time-and-buffers)

## Network design

Options:

- **Central DC** — scale, longer last mile
- **Regional DCs** — faster delivery, more inventory
- **Cross-dock** — high velocity, low storage
- **Drop-ship** — no inventory; supplier ships to customer

Model **lane cost**, handling, and inventory carrying cost together.

## Incoterms

Common choices (legal defines contract; SCM owns operational impact):

| Term | Seller responsibility snapshot |
|---|---|
| EXW | Buyer picks up at seller site |
| FOB | Seller delivers to port; buyer ocean/air |
| DDP | Seller delivers duty-paid to destination |

Clarify **risk transfer** and who books freight/customs.

## 3PL management

SLA elements:

- Receiving and put-away time
- Pick/pack accuracy and cut-off times
- Inventory accuracy (cycle count agreement)
- Returns processing
- Chargeback model (storage, picks, labels)

Run **operational reviews** monthly; annual commercial review with `commercial-counsel`.

## Lead time and buffers

Document **total lead time**:

```
Supplier LT + inbound transit + receiving + internal processing + outbound transit
```

Buffer in **days of supply** at each leg for critical SKUs.

Customer promise dates must exceed **cumulative P95** lead time unless expedite budget exists.
