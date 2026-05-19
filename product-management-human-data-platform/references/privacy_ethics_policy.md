# Privacy, Ethics, and Policy

## Human data risks

| Risk | Product response |
|------|------------------|
| PII in source media | Detection, blur, block, escalate |
| Sensitive attributes | Restricted tasks, expert tier only |
| Re-identification | Aggregation limits on exports |
| Consent gaps | Customer attestation fields, block upload |
| Cross-tenant leakage | Strict project isolation, audit logs |
| Misuse of labels | Acceptable use policy, export controls |

## Privacy-by-design features

- Role-based access (customer, contributor, reviewer, admin)
- Region pinning for storage and processing
- Retention TTL per project with legal hold override
- Download logging and watermarking on exports
- Contributor view: minimum data needed for task (masking)

## Customer responsibilities (product enforces)

```markdown
Before production labeling:
- [ ] Customer confirms rights to use data for labeling
- [ ] Classification selected (public / confidential / regulated)
- [ ] Retention and deletion requirements captured
- [ ] Banned content categories acknowledged
```

## Ethics review triggers

Escalate product/legal review when:

- Biometric, medical, or children's data
- Deception studies or undisclosed recording
- Political, religious, or violence-heavy content at scale
- Surveillance or law-enforcement sensitive use cases
- Export to jurisdictions with conflicting rules

## Alignment with compliance engineering

Map features to controls with `compliance-engineer`:

- Access reviews for admin roles
- Encryption at rest/transit
- Audit logs for label changes and exports
- DPIA inputs for new modalities or regions

## Transparency

- Contributor: what data is used for (within legal bounds)
- Customer: how quality and workforce tiers work
- Document known limitations in release notes

## Incident response (product angle)

| Event | PM actions |
|-------|------------|
| PII spill in task | Pause project, purge policy, notify customer |
| Rubric causes systematic harm | Halt task type, revise instructions |
| Workforce protest / pay dispute | Coordinate with ops and legal |

Pair with `community-executive-escalations-program-manager` if public reputational escalation.

## AI training downstream

- Metadata: label provenance, spec version, workforce tier
- Avoid implying labels are "ground truth" in API docs—document error bars
- Support customer deletion requests propagating to derived exports where feasible

## Anti-patterns

- Shipping geo features without residency analysis
- Using contributor-generated content to train platform models without disclosed consent
- Hiding quality problems from customer dashboards
