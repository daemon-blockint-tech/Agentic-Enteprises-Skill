# Golden paths

## Table of contents

1. [Template requirements](#template-requirements)
2. [Standard pipeline bundle](#standard-pipeline-bundle)
3. [Exception process](#exception-process)

## Template requirements

Every golden-path scaffold includes:

- [ ] CI workflow (test, build, scan)
- [ ] Container or runtime manifest with resource defaults
- [ ] Observability (metrics, logs, traces hooks)
- [ ] Health/readiness endpoints
- [ ] Secret injection pattern (no hardcoded creds)
- [ ] README with deploy and rollback commands

## Standard pipeline bundle

| Stage | Owned by platform |
|---|---|
| Lint/test | Shared action/workflow |
| Build/publish | Standard registry and tagging |
| Deploy dev/stage | GitOps or promoted artifact |
| Prod gate | Approval + deployment-strategist patterns |

## Exception process

1. Team documents why golden path insufficient
2. Platform + security review
3. Time-bound exception with compensating controls
4. Backlog item to absorb into path or retire exception
