# Engagement scope

## Table of contents

1. [Authorization checklist](#authorization-checklist)
2. [ROE elements](#roe-elements)
3. [Severity rubric](#severity-rubric)

## Authorization checklist

- [ ] Signed contract or letter of authorization on file
- [ ] Named technical and business contacts
- [ ] In-scope IP/domains/apps listed explicitly
- [ ] Out-of-scope documented (third parties, prod PII, physical, DoS)
- [ ] Testing window and timezone confirmed
- [ ] Emergency stop procedure agreed

## ROE elements

| Topic | Decision |
|---|---|
| Social engineering | Allowed / not allowed |
| Credential spraying | Allowed / throttled / not allowed |
| Production vs staging | Which environments |
| Data handling | No real customer data; synthetic only |
| Destructive tests | Forbidden unless explicit approval |

## Severity rubric

| Level | Typical criteria |
|---|---|
| Critical | Unauthenticated RCE, full tenant takeover, mass data access |
| High | Authenticated RCE, privilege escalation to admin, sensitive data read |
| Medium | Limited impact, difficult preconditions, defense in depth bypass |
| Low | Information disclosure with minimal impact |
| Info | Hardening, missing headers, version disclosure |

Align rubric with customer risk appetite before testing starts.
