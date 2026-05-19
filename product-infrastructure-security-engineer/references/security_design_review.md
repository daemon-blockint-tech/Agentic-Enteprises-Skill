# Security design review

## Table of contents

1. [When required](#when-required)
2. [Review template](#review-template)

## When required

Mandatory before prod for:

- New customer data store or replication path
- Change to authentication or authorization model
- New external integration or webhook surface
- Material change to encryption or key management
- New privileged operator capability

## Review template

```markdown
# Security design review — [feature]
**Author:** **Reviewers:** **Status:** draft | approved | blocked

## Summary
## Threat model link
## Data classification
## Tenancy impact
## AuthN/AuthZ design
## Crypto and secrets
## Logging and audit
## Abuse/rate limits
## Rollout (flags, migration)
## Open risks
## Test plan (security)
## Sign-off
```

Block launch on unresolved critical/high without explicit risk acceptance.
