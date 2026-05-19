# NFR and quality attributes

## Table of contents

1. [NFR worksheet](#nfr-worksheet)
2. [Availability and reliability](#availability-and-reliability)
3. [Performance and scale](#performance-and-scale)
4. [Security and compliance](#security-and-compliance)
5. [Cost and sustainability](#cost-and-sustainability)

## NFR worksheet

Copy per capability:

```markdown
| NFR | Target | Measurement | Owner |
|---|---|---|---|
| Availability | e.g. 99.95% / 30d | SLO dashboard | Platform |
| Latency (p99) | e.g. 500ms | APM | Service team |
| Throughput | e.g. 2k RPS | Load test + prod | Service team |
| Durability | RPO 15m, RTO 2h | DR test annual | Infra |
| Data retention | 7y audit logs | Policy + job | Compliance |
| Cost | $X / month at peak | FinOps tag | Eng + Finance |
```

If target is unknown, schedule a spike—do not ship "TBD" to production.

## Availability and reliability

**Error budget mindset:**

- Pick SLO below 100%; budget funds velocity vs reliability debates
- Multi-AZ is baseline for stateless; stateful needs explicit failover design
- Dependencies inherit your SLO—map critical path vendors

**Failure design:**

- Graceful degradation (read-only mode, cached responses)
- Health checks: liveness vs readiness
- Chaos or game days for tier-1 paths annually

## Performance and scale

**Capacity sketch:**

```
peak_RPS × payload_bytes × fan_out = egress_pressure
active_users × writes_per_day = storage_growth_per_year
```

Load test the **critical path** at 2× expected peak before launch.

Watch: connection pools, thread pools, GC pauses, cold starts (serverless).

## Security and compliance

Align with `cybersecurity` / `information-security-engineer` for control mapping.

Architecture must state:

- Data classification per store
- Encryption in transit and at rest
- Identity: human vs machine, least privilege, break-glass
- Audit logging for sensitive actions

## Cost and sustainability

- Tag resources by service/team for chargeback
- Right-size before multi-region expansion
- Prefer managed services when operational cost > license delta
- Document **cost of scale** (egress, index size, per-seat SaaS)

For FinOps implementation detail, pair with `infrastructure-engineer` / `devops`.
