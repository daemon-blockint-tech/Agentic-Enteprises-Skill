---
name: support-engineer
description: |
  Guides technical support engineering—customer ticket investigation, reproduction, log and API
  analysis, root-cause isolation, workaround communication, engineering escalation with evidence,
  and knowledge-base fixes for product bugs and integration issues.
  Use when debugging a customer-reported issue, writing a repro for engineering, analyzing API
  errors, drafting technical replies, or improving support runbooks—not for CS program design,
  renewals, or billing ops (customer-ops-specialist), production incident command
  (incident-management-engineer), building product features (fullstack-software-engineer), or
  company-wide crisis statements and launch announcements (communication-lead), or
  exec/VIP and community escalation program design (community-executive-escalations-program-manager).
  Product how-to, macros, and ticket triage without deep debugging: product-support-specialist.
---

# Support Engineer

## When to Use

- Investigate a customer bug or "it doesn't work" report
- Reproduce issues across environments (browser, API, mobile)
- Analyze logs, request IDs, and HTTP/API error payloads
- Draft technical response with steps, workaround, or ETA
- Escalate to engineering with minimal repro and impact
- Author or update KB articles after resolved issues

## When NOT to Use

- Support queue SLAs, CS metrics, renewals, dunning → `customer-ops-specialist`
- Company-wide outage incident commander role → `incident-management-engineer`
- Implement product code fixes in repo → `fullstack-software-engineer`
- Public API reference documentation → `tech-writer-researcher`
- Security incident or SOC alert investigation → `defensive-security-analyst`

## Related skills

| Need | Skill |
|---|---|
| Support ops, health scores, billing tickets | `customer-ops-specialist` |
| App code fixes and PRs | `fullstack-software-engineer` |
| Browser auth, CORS, session issues | `web-application-developer` |
| Production outage process | `incident-management-engineer` |
| Customer-facing docs and API guides | `tech-writer-researcher` |
| Infra/logs on platform side | `devops` |
| Company-wide incident or launch messaging | `communication-lead` |
| Exec/VIP and public community escalation program | `community-executive-escalations-program-manager` |
| How-to replies, KB gaps, feature-request capture | `product-support-specialist` |

## Core Workflows

### 1. Intake and triage

Capture before deep dive:

- Customer ID, environment (prod/sandbox), region
- Timestamp with timezone
- User role and exact URL or API endpoint
- Error message verbatim; request/correlation ID
- Recent changes (release, config, integration)
- Severity: blocked vs degraded vs question

Route billing/access-only issues to `customer-ops-specialist` if non-technical.

**See `references/ticket_triage.md`.**

### 2. Reproduce

1. Follow customer steps on comparable environment
2. Reduce to minimal repro (fewest steps, clean account if possible)
3. Note deterministic vs intermittent
4. Capture HAR, server logs, or curl with redacted secrets

**See `references/reproduction_debugging.md`.**

### 3. Isolate root cause

| Layer | Checks |
|---|---|
| Client | Browser, cache, extensions, version |
| API | Status code, body, rate limits, auth token |
| Config | Feature flags, tenant settings, quotas |
| Data | Specific record IDs, permissions |
| Platform | Status page, known incidents |

Document hypothesis and evidence; avoid guessing in customer reply.

### 4. Resolve or escalate

**If known issue:** link KB, workaround, linked engineering ticket + ETA.

**If new bug:** file engineering ticket with:

- Title: `[component] short failure description`
- Impact: customer count, blocked workflows
- Repro steps, expected vs actual
- Logs/IDs attached

**See `references/escalation_engineering.md`.**

### 5. Customer communication

- Acknowledge impact; no blame
- State what is known, unknown, and next update time
- Provide workaround before permanent fix when possible
- After fix: confirm with customer; close loop

**See `references/customer_comms.md`.**

### 6. Knowledge base

After fix verified:

- Symptom → cause → resolution → prevention
- Searchable title; tags for product area
- Link to public API doc if applicable

**See `references/kb_article.md`.**

## When to load references

- **Priority and intake** → `references/ticket_triage.md`
- **Repro and logs** → `references/reproduction_debugging.md`
- **Engineering handoff** → `references/escalation_engineering.md`
- **Customer updates** → `references/customer_comms.md`
- **KB template** → `references/kb_article.md`
