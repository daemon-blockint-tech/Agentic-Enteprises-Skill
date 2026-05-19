# Containment and handoff

## Table of contents

1. [Containment checklist](#containment-checklist)
2. [Evidence preservation](#evidence-preservation)
3. [IR handoff template](#ir-handoff-template)

## Containment checklist

- [ ] Incident ticket opened with severity
- [ ] Stakeholders notified per runbook
- [ ] Containment approved by IR lead
- [ ] Actions logged (who, what, when)
- [ ] Monitoring increased on related entities

## Evidence preservation

Before reimage or account reset when required:

- EDR snapshot / disk image per policy
- Export relevant log window to case storage
- Hash critical files
- Chain of custody note

## IR handoff template

```markdown
# Handoff — [INC-####]
**Severity:**
**Status:** Investigating | Contained | Eradicating

## Impact
## Timeline summary
## IOCs
## Containment taken
## Open questions
## Recommended next steps
**Analyst:**
```
