# Scoping and rules of engagement

## Table of contents

1. [Authorization gate](#authorization-gate)
2. [Scope worksheet](#scope-worksheet)
3. [ROE decisions](#roe-decisions)
4. [Emergency stop](#emergency-stop)
5. [Severity rubric](#severity-rubric)

## Authorization gate

**Stop.** Do not run active scans, exploitation, or credential attacks without:

- [ ] Signed contract, SOW, or letter of authorization naming tester and customer
- [ ] Named technical and business contacts (24/7 during test window if production)
- [ ] Explicit in-scope assets (IPs, hostnames, app URLs, API bases, cloud accounts)
- [ ] Explicit out-of-scope (third parties, other tenants, physical, employees unless approved)
- [ ] Agreed testing window, timezone, and notification channel
- [ ] Emergency stop procedure and escalation path documented

If authorization is unclear, **ask the customer in writing**—do not assume implied consent.

## Scope worksheet

| Field | Example |
|---|---|
| Engagement name | Q2 external web pentest |
| Test type | Grey-box web + API |
| Environments | `staging.example.com`, `api-stg.example.com` |
| Credentials | 2 user roles + 1 admin (test tenant) |
| Network position | Internet-only / VPN jump / on-segment |
| Data rules | Synthetic data only; no bulk export |
| Tools | Burp, nmap, custom scripts (list if restricted) |

Maintain a living **asset inventory** during recon; add newly discovered hosts only after customer confirms they are in scope.

## ROE decisions

| Topic | Document allowed / forbidden |
|---|---|
| Denial of service | Usually **forbidden** unless explicit written approval |
| Social engineering | Allowed / not allowed / targeted roles only |
| Password attacks | Spraying, brute force, default creds—rate limits and lockout policy |
| Production vs non-prod | Which environments; customer monitoring expectations |
| Destructive tests | Data deletion, ransomware simulation—almost always **out of scope** |
| Third-party SaaS | Out of scope unless vendor authorization on file |
| Cloud | Which accounts/subscriptions; no org-wide changes without approval |
| Post-exploitation | Lateral movement depth, credential dumping, domain admin proof |

Record **compensating controls** that block exploitation (WAF, MFA, segmentation)—they inform severity and remediation, not excuses to skip validation.

## Emergency stop

1. Customer or tester invokes **stop word** or stop channel
2. Cease all active testing immediately
3. Preserve logs and notes; do not delete evidence
4. Notify all testers and customer contact
5. Document stop reason and resume criteria in writing before continuing

## Severity rubric

Align with customer before testing. Typical mapping:

| Level | Typical criteria |
|---|---|
| **Critical** | Unauthenticated RCE, full tenant/account takeover, mass sensitive data access |
| **High** | Authenticated RCE, admin privilege escalation, significant data read/write |
| **Medium** | Limited impact, difficult preconditions, partial control bypass |
| **Low** | Minor information disclosure, missing hardening |
| **Info** | Best-practice gaps without direct exploit path |

Score **impact × likelihood** using agreed definitions; avoid inflating scanner noise to Critical.
