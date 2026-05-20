# Retest and safe practices

## Table of contents

1. [Retest workflow](#retest-workflow)
2. [Retest criteria](#retest-criteria)
3. [Safe testing practices](#safe-testing-practices)
4. [Legal and ethical boundaries](#legal-and-ethical-boundaries)
5. [Tool and data hygiene](#tool-and-data-hygiene)

## Retest workflow

1. Customer notifies fixes deployed (environment, build, date)
2. Confirm **same scope** and credentials as original test (or updated list)
3. Re-run **minimal** reproduction steps per finding ID
4. Record outcome: **Pass**, **Fail**, **Partial**, **Not applicable**
5. Update report or issue retest letter; do not reopen closed SOW without amendment

| Severity | Typical retest SLA (customer-defined) |
|---|---|
| Critical | Before production release or within days |
| High | Within agreed sprint |
| Medium/Low | Batch or next assessment |

## Retest criteria

Define pass conditions **when the finding is first reported**:

| Finding type | Pass when |
|---|---|
| IDOR | User cannot access other tenants' objects; automated test added |
| XSS | Payload encoded or CSP blocks execution in browser retest |
| Missing auth | Endpoint returns 401/403 for unauthenticated caller |
| Cloud public bucket | Object ACL/block public access enforced; verified via API |

Document **partial fixes** (e.g., patched one endpoint but not others) as Fail with notes.

## Safe testing practices

- **Rate-limit** active scans and brute force per ROE
- **Prefer non-production** environments when they represent prod code paths
- **Coordinate** with SOC if production testing may trigger alerts
- **Use dedicated test accounts**; never spray passwords against real employee accounts without approval
- **Redact** secrets in logs, reports, and chat
- **Encrypt** evidence at rest; limit distribution to engagement team
- **Time-box** sessions; avoid overnight unmonitored destructive tests

## Legal and ethical boundaries

- Operate only under **valid authorization** in relevant jurisdictions
- Respect **computer fraud** and **contract** terms; unauthorized testing is out of scope for this skill
- Do not use engagement access for **personal benefit** or unrelated research
- Report **critical** issues promptly per ROE (responsible disclosure timeline)
- **Do not** disclose customer vulnerabilities publicly without written permission

This skill is **operational guidance**, not legal advice—escalate legal questions to customer counsel.

## Tool and data hygiene

- Keep tool versions and command logs for reproducibility
- Store evidence in customer-approved repository (ticket, vault, encrypted share)
- **Delete** local copies per data-retention clause when engagement ends
- Do not upload customer data to public paste sites or unapproved cloud drives
- Segregate **customer A** and **customer B** workspaces to prevent cross-contamination

When retest passes, archive workpapers with pass evidence linked to finding ID.
