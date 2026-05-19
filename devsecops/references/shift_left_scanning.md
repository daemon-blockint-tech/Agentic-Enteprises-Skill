# Shift-left scanning

## Table of contents

1. [Scan types](#scan-types)
2. [Tool selection](#tool-selection)
3. [CI integration patterns](#ci-integration-patterns)
4. [Baseline rules](#baseline-rules)
5. [False positives and noise](#false-positives-and-noise)

## Scan types

| Layer | What it finds | Typical tools | Run when |
|---|---|---|---|
| Secrets | Keys, tokens, private keys in git | Gitleaks, TruffleHog, GitHub secret scanning | Every commit/PR |
| SAST | Injection, authz bugs, unsafe APIs | Semgrep, CodeQL, SonarQube | Every PR |
| SCA | Vulnerable dependencies | Dependabot, Snyk, OSV-Scanner | Every PR + daily on default branch |
| IaC | Overly open SGs, public buckets, weak K8s | Checkov, tfsec, KICS, Terrascan | On IaC/manifest changes |
| Container | OS and app CVEs in images | Trivy, Grype, Snyk Container | After image build |
| DAST | Runtime vulns, misconfig | OWASP ZAP, Burp CI (scoped) | Staging post-deploy |

## Tool selection

| Constraint | Prefer |
|---|---|
| Polyglot monorepo | Semgrep with org rulesets + CodeQL for supported langs |
| GitHub-native | CodeQL + Dependabot + secret scanning |
| GitLab-native | SAST/Dependency/Container scanning templates |
| Air-gapped / self-hosted | Semgrep OSS, Trivy, Checkov, local OSV DB |
| Low noise for startups | Semgrep `--config p/ci` + Dependabot + Gitleaks |

## CI integration patterns

**Principles:**

- Run fast scans on PR; run full scans nightly on default branch
- Upload SARIF to the platform security tab when available
- Fail builds on **new** critical issues introduced in the diff when possible (diff-aware scanning)

**Example: Semgrep in GitHub Actions**

```yaml
- name: Semgrep
  uses: semgrep/semgrep-action@v1
  with:
    config: p/ci
  env:
    SEMGREP_APP_TOKEN: ${{ secrets.SEMGREP_APP_TOKEN }}
```

**Example: Trivy image scan**

```yaml
- uses: aquasecurity/trivy-action@master
  with:
    image-ref: ${{ env.IMAGE }}
    format: sarif
    output: trivy.sarif
    severity: CRITICAL,HIGH
    exit-code: 1
```

## Baseline rules

1. No secrets in repository history—rotate if found
2. No `0.0.0.0/0` ingress on admin ports in production IaC
3. No `latest` tag for production deploy images
4. No privileged containers or `hostNetwork: true` in prod namespaces
5. TLS 1.2+ for external endpoints; prefer 1.3

## False positives and noise

| Symptom | Action |
|---|---|
| Test fixtures flagged as secrets | Allowlist path + document in security.md |
| CVE in unused transitive dep | Verify reachability; upgrade or waiver with expiry |
| SAST on generated code | Exclude `generated/` paths in config |
| IaC finding in module upstream | Fix in module version pin; don't patch locally twice |

**Waiver template:**

```markdown
## Security waiver: [ID]
- Finding: [tool + rule + CVE]
- Asset: [service/repo]
- Risk: [why accepted]
- Compensating controls: [WAF, network policy, etc.]
- Owner: @team
- Expires: YYYY-MM-DD
- Revisit trigger: [upgrade, exposure change]
```
