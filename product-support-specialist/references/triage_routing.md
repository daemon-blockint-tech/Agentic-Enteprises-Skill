# Triage and Routing

## Ticket categories

| Category | Signals | Route |
|----------|---------|-------|
| **How-to / education** | "How do I…", "Where is…" | Product support (resolve) |
| **Configuration** | Roles, settings, integrations UI | Product support → eng if broken |
| **Bug** | Reproducible wrong behavior | `support-engineer` |
| **Billing** | Charge, invoice, plan change | `customer-ops-specialist` |
| **Sales** | New purchase, enterprise quote | Sales / deal desk |
| **Account access** | Login, SSO, invite | Product support → IT/eng if systemic |
| **Outage** | Widespread failure | `incident-management-engineer` + macro |
| **Abuse / legal** | Threats, GDPR delete | Policy queue + legal |
| **Exec / VIP** | Strategic account flag | `community-executive-escalations-program-manager` |

## Severity (product support lens)

| Level | Definition | Target response |
|-------|------------|-----------------|
| **P1** | Blocked on critical workflow, no workaround | Same day |
| **P2** | Major feature impaired, workaround exists | 1 business day |
| **P3** | Minor issue or question | 2–3 business days |
| **P4** | Feedback, cosmetic, docs typo | Best effort |

Align P1/P2 with org-wide incident definitions when outage-related.

## Intake checklist

- [ ] Product area and environment (prod, region, browser)
- [ ] User role and plan (limits may apply)
- [ ] Expected vs actual behavior stated
- [ ] Screenshots or screen recording if UI
- [ ] Already tried steps (avoid duplicate work)
- [ ] Account ID / org ID (never share in public channels)

## Routing decision tree

```
Can answer from help center or known behavior?
  Yes → Reply + link KB
  No → Is it billing?
    Yes → customer-ops-specialist
    No → Can you reproduce or need logs?
      Yes → support-engineer
      No → Is it product gap / feature request?
        Yes → feedback_feature_requests.md + close loop
        No → Research with PM/docs; set follow-up
```

## Duplicate and related tickets

- Link parent issue for known bugs
- Merge duplicates; one owner
- Add "+1" to eng ticket without spamming customer

## SLA hygiene

- First response ≠ resolved; set both clocks
- Bump only with new information
- Snooze with reason and next action date
