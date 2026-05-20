# Customization, testing, and operations

## Table of contents

1. [Customization layers](#customization-layers)
2. [Extension guidelines](#extension-guidelines)
3. [Testing strategy](#testing-strategy)
4. [Cutover and peak readiness](#cutover-and-peak-readiness)
5. [Monitoring and support](#monitoring-and-support)
6. [Multi-warehouse and 3PL](#multi-warehouse-and-3pl)

## Customization layers

| Layer | Use when |
|---|---|
| **Configuration** | Rules, parameters, workflows without code—prefer first |
| **Scripted rules** | Vendor rule engine for allocation, putaway, wave filters |
| **Extensions / plugins** | Complex logic with vendor SDK; version with product upgrades |
| **External services** | Rate shop, cartonization, address validation—isolate behind adapter |
| **Reports/labels** | ZPL, SSCC, client branding—template ownership by site |

Avoid core table hacks; use supported extension points and **feature flags** per site/client.

## Extension guidelines

- Keep business logic **deterministic** and **side-effect free** in allocation hooks where possible
- Never bypass **scan validation** in RF shortcuts
- Log **rule version** applied to each decision for debug
- Package custom code in **CI** with same rigor as `senior-software-engineer` practices
- Document **upgrade impact** for each vendor release

## Testing strategy

| Phase | Focus |
|---|---|
| **Unit** | UOM conversion, allocation comparators, date/lot rules |
| **Integration** | ERP/TMS mock messages, idempotent replay |
| **RF UAT** | Real devices, gloves, lighting, Wi-Fi dead zones |
| **Automation** | WCS message simulators; fault injection |
| **Performance** | Peak order mix; wave release burst; print spool |
| **Regression** | Golden paths after each vendor patch |

Scenario pack (minimum):

- Full inbound ASN → putaway → available
- Multi-line B2C order → batch pick → pack → ship
- Short pick, substitute, cancel mid-wave
- Cycle count adjustment with approval
- Integration duplicate message handling

## Cutover and peak readiness

**Cutover**:

- Freeze master data changes; snapshot balances
- Run **parallel reconciliation** first day
- Define **rollback**—revert DNS/integration, restore DB backup only if approved

**Peak season**:

- Pre-build **wave templates** and labor plans
- Scale **integration consumers** and DB indexes
- Throttle **non-critical jobs** (reports, archival)
- War-room **dashboards**: open waves, pick backlog, integration lag

## Monitoring and support

Alert on:

- Integration **queue depth** and **age**
- **Failed ship confirms** and **stuck allocations**
- **RF login errors** and **device version drift**
- **Automation NACK** rate from WCS

Tier-1 runbooks: restart print service, requeue message, reprint label, unlock wave. Tier-2: data fix with approval workflow.

## Multi-warehouse and 3PL

- **Site ID** on every record; no cross-site allocation without transfer document
- **Client ID** for 3PL; row-level security in UI and APIs
- **Billing capture** on handled units, storage days, VAS tasks—export to billing system
- **SLA timers** on receipt-to-putaway and order-to-ship by client contract

Separate **operational reporting** from `data-warehouse-engineer` marts—use event export or CDC with documented schema.
