# Incident tooling

## Table of contents

1. [Integration checklist](#integration-checklist)
2. [Timeline hygiene](#timeline-hygiene)

## Integration checklist

- [ ] Monitoring alert → paging service (dedupe, enrichment)
- [ ] Page ack → auto-create incident + Slack channel
- [ ] Ticket linked (Jira/Linear) with SEV field
- [ ] Status page integration for SEV1–2
- [ ] Postmortem doc template linked on close
- [ ] Metrics export for MTTD/MTTR dashboards

## Timeline hygiene

Log with timestamps:

- SEV declared and roles assigned
- Customer comms sent
- Mitigation applied
- Resolution confirmed
- Postmortem scheduled

Avoid editing past entries; add corrections as new lines.
