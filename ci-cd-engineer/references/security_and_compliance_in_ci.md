# Security and compliance in CI

## Table of contents

1. [Shared responsibility](#shared-responsibility)
2. [Credentials and secrets](#credentials-and-secrets)
3. [OIDC federation](#oidc-federation)
4. [Runner and supply-chain hardening](#runner-and-supply-chain-hardening)
5. [Security scanning gates](#security-scanning-gates)
6. [Fork and untrusted code](#fork-and-untrusted-code)
7. [Compliance evidence hooks](#compliance-evidence-hooks)
8. [Agentic and AI workflows in CI](#agentic-and-ai-workflows-in-ci)

## Shared responsibility

| Role | Owns |
|---|---|
| CI/CD engineer | Where scans run, gate placement, credential wiring, artifact retention |
| DevSecOps | Tool selection, severity SLAs, signing, threat models for delivery |
| Information security engineer | IdP, KMS, org policies, SIEM integration |
| Compliance engineer | Control mapping and audit evidence requirements |

CI/CD implements **hooks**; security teams define **policy**.

## Credentials and secrets

**Do:**

- Store secrets in vault/GitHub encrypted secrets/GitLab masked variables with environment scope
- Rotate credentials on schedule; break glass documented
- Use separate credentials per environment (dev ≠ prod)
- Mask secrets in logs; prevent `set -x` leaking values

**Do not:**

- Commit secrets or long-lived cloud keys to git
- Share one prod deploy key across all repos
- Pass secrets to fork workflows without controls

**Rotation runbook:** update secret → verify pipeline → revoke old → audit last use.

## OIDC federation

Prefer **OIDC** over static cloud keys in CI:

1. IdP trusts CI platform (GitHub/GitLab issuer URL)
2. Role trust policy scoped to `repo:org/name:ref:refs/heads/main` or environment
3. Short-lived tokens per job
4. Least privilege IAM role per repo or environment

Validate: job cannot assume prod role from unprotected branch.

## Runner and supply-chain hardening

| Control | Notes |
|---|---|
| Pinned action versions | SHA pin for third-party actions |
| Allowed actions org policy | Deny unverified marketplace actions |
| Immutable action mirrors | For high assurance |
| Hardened images | CIS-aligned runner AMIs or containers |
| Network egress | Restrict runners that touch prod |
| Dependency review | Block known CVEs on PR |

Container builds: use digest-pinned base images; scan images before prod gate.

## Security scanning gates

Typical stages (configure with `devsecops`):

| Scan | When | Merge block? | Deploy block? |
|---|---|---|---|
| Secret detection | PR | Yes | Yes |
| SAST | PR | Critical/high | Critical |
| SCA / dependency | PR | Policy-based | Policy-based |
| IaC scan | PR touching infra | Yes | Yes |
| Container scan | After image build | — | Yes |
| DAST | Staging | — | Optional |

**Triage workflow:** finding ID → owner → SLA → exception with expiry → re-scan.

Export SARIF or vendor JSON to artifact store for dashboards and audits.

## Fork and untrusted code

- `pull_request_target` only when absolutely necessary; prefer `pull_request` with limited permissions
- Require maintainer approval before running workflows on external forks
- No access to org secrets on fork PRs unless label-gated and reviewed
- Sanitize branch names in shell scripts (injection risk)

## Compliance evidence hooks

Pipeline outputs for auditors (coordinate with `compliance-engineer`):

| Control theme | Evidence from CI |
|---|---|
| Change management | Deploy logs, approvers, tickets |
| SDLC testing | Test reports, required checks |
| Vulnerability management | Scan results, remediation tickets |
| Access control | OIDC role assumptions, environment protections |
| Configuration management | IaC scan, drift detection job results |

Schedule **monthly export** of failed gates and mean time to remediate for leadership review.

## Agentic and AI workflows in CI

When pipelines invoke AI coding agents (Copilot Actions, Claude Code, Codex):

- Treat PR comments and workflow inputs as untrusted
- Sandbox with minimal permissions; no prod secrets
- Pin action versions; review workflow diffs like application code
- Use `agentic-actions-auditor` patterns when available for injection review

CI/CD engineer ensures workflow structure is safe; `devsecops` defines security bar for tools.
