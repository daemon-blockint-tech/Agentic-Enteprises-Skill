# Launch and Governance

## Monetization launch tiers

| Tier | Examples | Gates |
|------|----------|-------|
| **Tier 0** | Copy, CTA, in-app banner | PM + analytics |
| **Tier 1** | New fence, add-on SKU | PM + finance + eng |
| **Tier 2** | List price change | Exec + finance + comms |
| **Tier 3** | Model change (seat→usage) | Cross-functional program |

## Launch checklist (Tier 1+)

- [ ] PRD approved; entitlements documented
- [ ] Finance SKU and recognition notes
- [ ] Legal: terms, tax, region availability
- [ ] Analytics events live in staging
- [ ] Support macro and KB (`customer-ops-specialist`)
- [ ] Sales enablement (battlecard, FAQ)
- [ ] Rollback plan (feature flag, price revert)
- [ ] Customer comms if existing users affected

## Price change governance

| Step | Owner |
|------|-------|
| Impact model (churn, expansion) | PM + finance |
| Segment mapping (who changes when) | PM |
| Approval | Per discount/price policy |
| Comms plan | PM + marketing/comms |
| In-product notices | PM + design |
| Post-launch monitor | PM + analytics (2–4 weeks) |

## Grandfathering policy template

```markdown
**Existing customers:** [keep legacy / migrate on renewal / opt-in migrate]
**New customers:** [new price effective DATE]
**Enterprise contracts:** [honor MSA through term]
```

## Conflict resolution

| Conflict | Forum |
|----------|-------|
| Sales custom vs product packaging | Deal desk + PM + finance |
| Free user abuse | Trust + monetization PM |
| Recognition vs desired packaging | Finance + PM + legal |

## Documentation deliverables

- Internal pricing playbook (plans, fences, objections)
- Public pricing page brief (not legal terms)
- Changelog entry for transparency

## Retrospective

After major monetization launch:

- Conversion vs forecast
- Support ticket themes
- Unintended downgrade/churn
- Playbook updates for `references/pricing_packaging.md`

## Related programs

- Large cross-team price migrations → `technical-program-manager`
- Company-wide customer messaging → `communication-lead`
