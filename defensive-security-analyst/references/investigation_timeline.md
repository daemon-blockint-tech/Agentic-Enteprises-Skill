# Investigation and timeline

## Table of contents

1. [Log sources](#log-sources)
2. [Query tips](#query-tips)
3. [Timeline template](#timeline-template)
4. [Report outline](#report-outline)

## Log sources

| Source | Typical questions |
|---|---|
| IdP / SSO | Logins, MFA failures, impossible travel |
| EDR | Process, parent chain, network connections |
| Proxy/DNS | External domains, DGA patterns |
| Cloud audit | API calls, IAM changes, data access |
| Email | Phishing delivery, rule forwards |

## Query tips

- Normalize all times to UTC
- Start narrow (user + 24h window) then widen
- Correlate on `session_id`, `device_id`, `src_ip` when available
- Watch for `runas`, service account abuse, new OAuth grants

## Timeline template

| UTC time | Entity | Event | Source | Analyst note |
|----------|--------|-------|--------|--------------|

## Report outline

1. Summary (impact, current status)
2. Timeline (table)
3. IOCs (hashes, domains, IPs with context)
4. ATT&CK mapping
5. Hypothesis and confidence
6. Recommendations (contain, eradicate, recover)
7. Evidence appendix (log query IDs, screenshots hash)
