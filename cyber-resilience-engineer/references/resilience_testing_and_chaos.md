# Resilience testing and chaos

## Table of contents

1. [Test taxonomy](#test-taxonomy)
2. [Planning a game day](#planning-a-game-day)
3. [Restore drills](#restore-drills)
4. [Chaos and failure injection](#chaos-and-failure-injection)
5. [Safety guardrails](#safety-guardrails)
6. [Evidence and reporting](#evidence-and-reporting)
7. [Continuous improvement](#continuous-improvement)

## Test taxonomy

| Type | Primary goal | Typical frequency |
|---|---|---|
| **Component restore** | Prove backup → isolated env | Quarterly (tier-0/1) |
| **Service failover** | RTO/RPO in controlled cutover | Semi-annual |
| **Game day** | Multi-team coordination | Annual per major scenario |
| **Tabletop** | Decisions and comms | BCM calendar |
| **Chaos experiment** | Validate detection and auto-recovery | Monthly in non-prod; gated in prod |
| **Purple-team recovery** | IR + rebuild path under attack sim | Annual |

Distinguish **reliability chaos** (latency, pod kill) from **cyber resilience** tests (backup delete attempt, IdP unavailable, logging pipeline stopped).

## Planning a game day

1. **Objective** — e.g., "restore IdP and SIEM within RTO after simulated ransomware"
2. **Scope** — systems, environments, **explicit non-goals**
3. **Hypothesis** — what should work; what you expect to fail
4. **Success criteria** — RTA, RPO, MVC met; comms milestones
5. **Roles** — resilience lead, IR liaison, SRE, app owners, scribe
6. **Schedule** — inject timeline, go/no-go checkpoints
7. **Rollback** — abort criteria and technical steps
8. **Approvals** — change advisory, leadership, customer impact

Coordinate calendar with `bcm-disaster-recovery-specialist` to avoid duplicate exercises.

## Restore drills

**Minimum drill script:**

1. Select target from tier register (rotate coverage)
2. Provision **isolated** network and accounts
3. Restore from **immutable** copy where applicable
4. Run integrity and smoke tests
5. Measure **RTA** and effective **RPO**
6. Record gaps (automation, runbook, staffing, tooling)
7. File remediation; link to next quarter's drill

For **ransomware simulation**, prefer:

- Restore to greenfield VPC/subscription
- No reuse of prod AD/connectors until IR clearance
- Validate **golden image** hash and IaC revision

## Chaos and failure injection

Security-relevant experiments (examples):

| Experiment | Validates |
|---|---|
| Revoke IdP signing cert (staging) | Break-glass, session handling |
| Block SIEM ingest endpoint | Buffering, alert on blind spot |
| Simulate backup job failure | Monitoring, paging |
| Attempt delete on immutable bucket (denied) | Object lock, alerting |
| Kill secrets manager replica | App degradation, failover |
| DNS failure for control plane | Cached creds, alternate runbook |

Use **blast-radius budgets** with SRE (`site-reliability-engineer`): max error rate, max duration, automatic abort.

**Production chaos** requires:

- Feature flags or kill switches
- On-call aware and bridge optional
- Customer impact assessment
- Post-experiment stability soak

## Safety guardrails

- Never inject **destructive** malware or real encryption in prod
- No production restore **into** prod without change window and IR awareness
- Separate **test credentials** from prod; revoke after exercise
- Document **stop conditions**: customer SLA breach, data corruption signal, leadership call
- Legal/compliance review for scenarios touching **regulated data**

## Evidence and reporting

Capture per exercise:

- Date, scope, tier, scenario ID
- Participants and roles
- RTA, RPO achieved vs targets
- Pass/fail per validation check
- Screenshots/logs (redacted) in evidence repository
- Findings with severity and owners
- Retest date for failed items

**See `references/metrics_reporting_and_governance.md`** for KPI definitions.

## Continuous improvement

- Feed failures into **architecture backlog** (not only runbook edits)
- Update playbooks within **5 business days** of material gap
- Re-run failed scenarios before claiming closure
- Share **blameless** summary with IR and BCM
- After real incidents, compare RTA to last drill—update tests if drift >25%
