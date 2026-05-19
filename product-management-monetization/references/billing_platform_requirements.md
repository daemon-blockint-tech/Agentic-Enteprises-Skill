# Billing Platform Requirements

## PM vs engineering boundary

| PM specifies | Engineering implements |
|--------------|------------------------|
| Entitlement matrix | AuthZ checks, feature flags |
| Meter events | Pipelines, idempotency |
| Proration rules | Billing provider config |
| Customer-facing copy | Checkout UI |
| Edge cases | Webhooks, retries |

## Entitlements model

```markdown
| Capability | Free | Pro | Enterprise |
|------------|------|-----|------------|
| SSO | — | — | ✓ |
| API calls/mo | 1k | 50k | custom |
```

Requirements:

- Source of truth (billing provider vs internal DB)
- Propagation latency SLA
- Grace on payment failure

## Subscription lifecycle events

Product must define behavior for:

| Event | User experience |
|-------|-----------------|
| Subscribe | Immediate access |
| Upgrade mid-cycle | Proration + instant entitlements |
| Downgrade | End of period vs immediate |
| Cancel | Access until period end |
| Payment failed | Retry dunning UI states |
| Refund | Entitlement revocation rules |

Ops execution: `customer-ops-specialist`.

## Usage metering PRD fields

- Event name and payload schema
- Aggregation window (calendar month vs rolling)
- Idempotency key
- Backfill and correction policy
- Customer-visible usage dashboard
- Dispute process

## Integrations checklist

- [ ] Tax/VAT display by region
- [ ] Invoices and receipt emails
- [ ] Admin: comp accounts, credits, extensions
- [ ] Webhooks to CRM for sales alerts
- [ ] Sandbox for sales demos

## Finance alignment

Before GA provide finance:

- SKU list and list prices
- Discount types
- Performance obligation mapping flag → `senior-revenue-accountant`
- Refund and credit accounting treatment

## Security and compliance

- PCI scope minimized (hosted checkout)
- Role for viewing billing vs changing payment method
- Audit log on entitlement overrides

## Anti-patterns

- Hard-coded plan checks scattered without entitlement service
- Meter events without idempotency
- Promising invoice terms product cannot provision
