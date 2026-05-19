# Customer ML Team Workflows

## End-to-end journey

1. **Scope** — modality, volume, deadline, quality bar
2. **Configure** — project, taxonomy, workforce tier, instructions
3. **Pilot** — small batch, calibrate IAA and handle time
4. **Scale** — production batches, monitoring, SLA tracking
5. **Accept** — QA sign-off, export, lineage metadata
6. **Iterate** — taxonomy v2, active learning loops

## Project setup (product requirements)

| Field | Why it matters |
|-------|----------------|
| Delivery date | Drives staffing and feature flags |
| Quality tier | Gold %, consensus, adjudication depth |
| Data classification | Privacy features, region, retention |
| Export schema | JSONL, COCO, Parquet, custom |
| Versioning | Model training reproducibility |

## Self-serve vs managed

| Mode | Customer | Platform |
|------|----------|----------|
| Self-serve | Configures tasks, monitors dashboards | Templates, guardrails, billing |
| Managed | Solution engineer / PM runs project | Playbooks, dedicated QA, custom SLA |

Product should not blur modes without clear pricing.

## API and integration

- Batch create/upload, status webhooks, export download
- Idempotent job IDs for pipeline orchestration
- Rate limits and pagination documented
- Sandbox project for integration testing

## Dashboards (customer)

- Progress: completed / in review / rejected
- Quality: gold accuracy, IAA, rework trend
- Cost: spend vs estimate (if usage-based)
- Blockers: queue starvation, instruction tickets

## Delivery acceptance

```markdown
## Acceptance checklist
- [ ] Volume and format match SOW
- [ ] Quality metrics meet appendix thresholds
- [ ] Label version and task spec hash in metadata
- [ ] Known limitations documented (classes with low support)
- [ ] PII attestation if applicable
```

## Expansion and retention

- Track **time-to-first-export** for new accounts
- Instrument **repeat project** rate by vertical
- Capture **quality incident** root cause for product backlog

## Handoffs

- Technical integration issues → support/engineering paths in org
- Legal/DPA → `commercial-counsel` + `compliance-engineer`
- Custom ontology → `ontology-engineer`
