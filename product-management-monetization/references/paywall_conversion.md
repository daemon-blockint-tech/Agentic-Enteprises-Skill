# Paywalls and Conversion

## Gating strategies

| Strategy | When | Risk |
|----------|------|------|
| **Hard paywall** | Value only after pay | Low top-of-funnel |
| **Feature gate** | Core free, advanced paid | Confusing line |
| **Usage gate** | Free quota then block | Bill shock if unclear |
| **Time gate** | Trial then lock | Expiry cliff churn |
| **Seat gate** | Invite blocked | Viral friction |

Choose gate based on **where value is realized**, not where eng is easiest to block.

## Paywall moment design (PM spec)

For each gate document:

```markdown
**Trigger:** User attempts [action]
**State shown:** Modal / full page / inline banner
**Copy intent:** What they gain by upgrading (not feature list only)
**Primary CTA:** Upgrade to [plan]
**Secondary:** Compare plans / contact sales
**Escape hatch:** What still works free
**Analytics:** paywall_viewed, upgrade_clicked, plan_selected
```

`product-designer` owns visual execution.

## Trial design

| Decision | Options |
|----------|---------|
| Length | 7 / 14 / 30 days by sales cycle |
| CC upfront | Higher quality vs volume |
| Reverse trial | Full access then downgrade |
| Extension policy | One-time auto vs sales approval |

## Upgrade paths

| Path | Product requirements |
|------|---------------------|
| Self-serve upgrade | Instant entitlement + proration |
| Sales-assisted | Quote → provision without double pay |
| Usage overage | Soft warning → hard block |
| Add-on attach | Cart or in-settings purchase |

## Expansion triggers (in-product)

- Approaching limit (80% usage)
- Team size growth (invite blocked)
- Feature discovery (locked preview with tooltip)
- Success milestone ("You saved X hours—unlock reports")

## Churn prevention product hooks

- Cancel flow with save offers (policy with finance)
- Downgrade vs pause vs export data
- Win-back offers post-cancel (coordinate `customer-ops-specialist`)

## Enterprise considerations

- Same SKU in product as order form
- No self-serve downgrade below contracted minimum
- Custom entitlements flag in admin

## Ethics and trust

- Clear renewal price before annual charge
- No dark patterns on cancel
- Disclose usage metering before consumption
