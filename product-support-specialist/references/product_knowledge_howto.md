# Product Knowledge and How-Tos

## Verify before answering

| Source | Use for |
|--------|---------|
| Help center / KB | Customer-facing steps |
| Internal playbook | Edge cases, plan matrix |
| Release notes | Recent changes |
| `product-management-monetization` fences | Limits by plan |
| PM or designer | Ambiguous behavior |

If sources conflict, **do not guess**—confirm with product or file doc bug.

## How-to answer template

```markdown
**Goal:** [what user wants to accomplish]

**Prerequisites:** Role, plan, integration enabled

**Steps:**
1. …
2. …

**Result:** What they should see

**If different:** [what to check / escalate]
```

## Common how-to themes

| Theme | Often confused with |
|-------|---------------------|
| Permissions | Bug ("button missing") |
| Integration setup | API bug |
| Export limits | Data loss bug |
| Trial expiry | Billing bug |
| SSO | Login outage |

## Plan and entitlement checks

Before deep troubleshooting:

- Plan tier and add-ons
- Seat role (admin vs member)
- Feature flags for beta
- Region / data residency restrictions

Reference `product-management-monetization` for packaging language.

## "Works as designed" conversations

1. Restate user goal
2. Explain designed behavior in neutral terms
3. Offer path to goal (workflow, upgrade, integration)
4. Capture feedback if gap is real

Avoid arguing; offer to log enhancement request.

## Onboarding support

| Friction | Support move |
|----------|--------------|
| Can't complete setup wizard | Screen-share checklist |
| Invites not received | Spam/whitelist KB |
| Empty state confusion | Point to first-value guide |
| Import failed | Route to eng if error code |

## Staying current

- Weekly release skim (support digest)
- Flag macros that reference old UI
- Contribute corrections to `tech-writer-researcher` for doc fixes

## Anti-patterns

- Sharing admin-only URLs with non-admins
- Recommending unsupported third-party workarounds as official
- Teaching circumvention of security controls
