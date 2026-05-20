# Reliability metrics and release coordination

## Table of contents

1. [DORA metrics](#dora-metrics)
2. [Pipeline health metrics](#pipeline-health-metrics)
3. [Release coordination](#release-coordination)
4. [Rollback](#rollback)
5. [Incident and freeze interaction](#incident-and-freeze-interaction)
6. [Partnering with SRE and platform](#partnering-with-sre-and-platform)
7. [Continuous improvement](#continuous-improvement)

## DORA metrics

Four key metrics (define measurement consistently org-wide):

| Metric | Definition (typical) | CI/CD data sources |
|---|---|---|
| Deployment frequency | How often deploy to prod | Successful prod deploy workflow events |
| Lead time for changes | Commit → prod deploy | Timestamps from VCS + deploy job |
| Change failure rate | Deploys causing incident/rollback/hotfix | Incidents tagged with release; failed smoke |
| Mean time to restore | Incident start → service restored | Incident tool; exclude unrelated outages |

**Implementation tips:**

- Use deployment events API (GitHub deployments, GitLab environments, custom webhook)
- Normalize timezone and “what counts as production”
- Exclude docs-only deploys if policy says so—document exclusion
- Review quarterly with leadership; avoid gaming metrics

DORA informs priorities; **SLOs** remain owned by `site-reliability-engineer`.

## Pipeline health metrics

| Metric | Why it matters |
|---|---|
| Median PR pipeline duration | Developer experience |
| P90 duration | Tail latency pain |
| Queue time | Runner capacity |
| Pass rate per stage | Flaky tests vs infra |
| Mean time to fix broken main | Trunk stability |
| Cache hit rate | Cost and speed |
| Deploy job failure rate | Release risk |

Dashboard per repo and aggregate platform view for template teams.

## Release coordination

**Before release:**

1. Confirm staging validation and changelog
2. Check error budget / freeze calendar with SRE
3. Verify migrations backward-compatible or expand-contract plan
4. Notify customer-facing teams per comms policy
5. Ensure on-call coverage for deployment window

**During release:**

- Use progressive exposure (canary) when tier requires
- Monitor golden signals during deploy job + 30–60 min after
- Single **release captain** coordinates pipeline and comms

**After release:**

- Mark deployment complete in tracker
- Close feature flags cleanup tickets
- Capture DORA data point
- Schedule retro if change fail

Coordinate cutover details with `deployment-strategist` when traffic switching is complex.

## Rollback

**Preferred:** redeploy **previous known-good digest** without rebuild.

Runbook steps:

1. Identify last good digest from deploy history or container registry
2. Trigger rollback workflow (same pipeline, pinned digest input)
3. Run smoke tests
4. Verify metrics return to baseline
5. File incident if customer impact occurred
6. Block forward deploy until root cause fixed

Test rollback **quarterly** for tier-1 services.

| Situation | Action |
|---|---|
| Bad image in prod | Rollback digest |
| Bad config only | Revert config commit + redeploy same digest |
| Database migration failure | Follow DBA/runbook; may not be pipeline-only |

## Incident and freeze interaction

When SRE declares incident or freeze:

- Halt optional releases; allow security hotfix path only
- Pipeline reads `FREEZE=true` variable or environment lock
- Post-incident: prioritize pipeline fixes that caused or prolonged outage

CI/CD engineer attends blameless postmortem when delivery path contributed; action items tracked in same sprint.

## Partnering with SRE and platform

| Topic | CI/CD engineer | SRE / platform |
|---|---|---|
| Canary metric thresholds | Wire gates in workflow | Define SLO queries and thresholds |
| Error budget | Respect freeze API/label | Publish budget status |
| Runners and registries | Report capacity needs | Provide pools and quotas |
| Golden paths | Maintain pipeline templates | Own portal and scaffolds (`platform-engineer`) |
| Load tests | Trigger job before major release | Interpret results (`performance-engineer`) |

Escalate production mitigation execution to on-call; provide rollback pipeline and artifact coordinates quickly.

## Continuous improvement

Monthly delivery review agenda:

1. DORA trend vs targets
2. Top pipeline failures by category
3. Flaky test debt
4. Security gate exceptions expiring soon
5. Template version drift across repos

Quarterly: game day deploying and rolling back in staging; update runbooks from findings.
