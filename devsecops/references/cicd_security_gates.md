# CI/CD security gates

## Table of contents

1. [Protected branches and environments](#protected-branches-and-environments)
2. [OIDC federation](#oidc-federation)
3. [GitHub Actions hardening](#github-actions-hardening)
4. [GitLab CI hardening](#gitlab-ci-hardening)
5. [Deploy-time controls](#deploy-time-controls)
6. [Agentic CI risks](#agentic-ci-risks)

## Protected branches and environments

| Control | Purpose |
|---|---|
| Require PR before merge to `main` | Prevent direct push bypass |
| Require status checks (security + test) | Enforce gates |
| Require signed commits (optional) | Integrity of history |
| Environment protection on `production` | Manual approval + branch filter |
| Deployment branches only from `main` or release tags | Reduce stray deploys |

## OIDC federation

**Replace static AWS keys:**

```yaml
permissions:
  id-token: write
  contents: read

- uses: aws-actions/configure-aws-credentials@v4
  with:
    role-to-assume: arn:aws:iam::123456789012:role/github-deploy
    aws-region: us-east-1
```

**IAM trust policy essentials:**

- Restrict `sub` to `repo:ORG/REPO:ref:refs/heads/main` (or environment)
- Restrict `aud` to STS provider audience
- Least-privilege policy on the role—no `*` on `iam:*` or `s3:*` unless justified

Same pattern applies to GCP Workload Identity Federation and Azure Federated Credentials.

## GitHub Actions hardening

| Practice | Detail |
|---|---|
| Pin actions | Use commit SHA or trusted version tags |
| `permissions:` block | Default minimal; elevate per job |
| Fork PRs | Do not run untrusted workflows with secrets; use `pull_request_target` only with extreme care |
| `GITHUB_TOKEN` | `contents: read` unless write needed |
| Self-hosted runners | Isolate; treat as production trust zone |
| Caching secrets | Never echo secrets; mask in logs |

**Dangerous patterns to block in review:**

- `curl | bash` from unpinned URLs in workflows
- Passing `${{ github.event.issue.body }}` into shell without sanitization
- Wildcard `allowed-users` on workflow_dispatch from untrusted actors
- Storing cloud keys in repo/org secrets without rotation

## GitLab CI hardening

- Use protected branches and protected variables (environment-scoped)
- Separate `deploy` stage with `when: manual` for production
- Enable dependency and SAST templates from GitLab Security
- Restrict runner tags so production deploys only on hardened runners

## Deploy-time controls

1. **Immutable artifact**: image digest or signed bundle, not floating tag
2. **Verify signature** before apply (cosign verify, Notation)
3. **Policy check**: OPA/Gatekeeper/Kyverno deny non-compliant manifests
4. **Smoke test** post-deploy; automatic rollback on failed health
5. **Audit record**: commit SHA, actor, pipeline ID, artifact digest in change ticket

## Agentic CI risks

When CI runs AI coding agents (Claude Code Action, Codex, Gemini CLI):

- Treat PR comments, issue bodies, and fork content as untrusted input
- Never pass untrusted text into `run:` shell via string interpolation
- Sandbox with minimal permissions; no org-wide secrets on fork workflows
- Require human review for changes touching workflows, IAM, or auth code
- See dedicated agentic-actions-auditor skill when available for workflow-specific checks
