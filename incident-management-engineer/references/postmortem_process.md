# Postmortem process

## Table of contents

1. [Template](#template)
2. [Metrics](#metrics)

## Template

```markdown
# Postmortem — [incident ID] — [title]
## Summary (1 paragraph)
## Impact (duration, users, revenue if known)
## Timeline (UTC)
## Root cause
## Contributing factors
## What went well
## What went poorly
## Action items
| Item | Owner | Due | Type (detect/mitigate/process) |
```

Blameless language; no individual blame.

## Metrics

| Metric | Definition |
|---|---|
| MTTD | Alert/report → incident declared |
| MTTR (mitigate) | Declare → service restored |
| MTTR (resolve) | Declare → permanent fix deployed |
| Repeat rate | Same component class within 90 days |

Review trends in monthly ops review.
