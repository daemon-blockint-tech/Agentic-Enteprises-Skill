# Code security scope and workflow

## Table of contents

1. [Purpose and boundaries](#purpose-and-boundaries)
2. [Proactive vs reactive modes](#proactive-vs-reactive-modes)
3. [Review workflow](#review-workflow)
4. [Language priority table](#language-priority-table)
5. [Impact tiers](#impact-tiers)
6. [Evidence and reporting](#evidence-and-reporting)

## Purpose and boundaries

This skill covers **secure coding guidance and security-focused code review** for application and infrastructure-as-code artifacts. It distills OWASP-oriented patterns across 15+ languages and common IaC formats.

**In scope:** identifying vulnerable patterns, recommending secure replacements, mapping to CWE/OWASP, prioritizing fixes by impact.

**Out of scope:** running authorized offensive engagements, compliance attestation, operating enterprise security tools, or replacing language-specific exploit development.

## Proactive vs reactive modes

### Proactive

Apply when the agent writes or edits code that:

- Accepts HTTP/query/body/header/cookie input
- Builds SQL, shell commands, file paths, or dynamic code
- Parses XML, deserializes objects, or fetches user-supplied URLs
- Handles passwords, tokens, API keys, or session state
- Defines Terraform, Kubernetes, Docker, or GitHub Actions resources

Check **Critical** categories first, then **High**, without waiting for the user to mention security.

### Reactive

When the user asks for a security review, audit, or “is this safe?”:

1. Confirm scope (paths, languages, threat assumptions).
2. Follow `review_checklist_and_owasp_mapping.md`.
3. Return findings ordered by severity with CWE/OWASP tags and fix snippets.

## Review workflow

```
scope → language/stack → data flows (sources/sinks) → category checklist → findings → fixes
```

| Step | Action |
|---|---|
| 1 | List files and languages in scope |
| 2 | Identify trust boundaries (user input, webhooks, CI events, admin APIs) |
| 3 | Trace sources to sinks (DB, shell, filesystem, HTTP client, eval, deserialize) |
| 4 | Run Critical checklist (injection, secrets, deserialization, XXE, memory) |
| 5 | Run High checklist (crypto, transport, SSRF, JWT, CSRF, IaC) |
| 6 | Note Medium/Low (ReDoS, races, correctness) when time permits |
| 7 | Summarize with severity, CWE, OWASP category, and remediation |

## Language priority table

When multiple issues exist, start with the rows that match the stack under review.

| Language / stack | Check first (references) |
|---|---|
| **Python** | SQL/command injection, path traversal, `eval`/template injection, SSRF, pickle/YAML unsafe load, weak crypto |
| **JavaScript/TypeScript** | XSS, prototype pollution, `eval`/VM, CSRF on state-changing routes, TLS verification, JWT verify |
| **Java** | SQL injection, XXE on XML parsers, Java deserialization, SSRF, weak crypto algorithms |
| **Go** | SQL injection, `exec` with user strings, path traversal, SSRF, TLS config |
| **C/C++** | Buffer overflows, unsafe libc (`strcpy`, `gets`), format strings, command injection |
| **Ruby** | SQL/command injection, `YAML.load`, `Marshal.load`, ERB injection |
| **PHP** | SQL injection, XSS, `shell_exec`, `include` path issues, deserialization |
| **Rust** | Unsafe blocks, command APIs, SQL via string concat, TLS |
| **HCL (Terraform)** | Public S3/storage, wildcard IAM, unencrypted disks, open security groups |
| **Kubernetes YAML** | Privileged pods, root user, host namespaces, secrets in manifests, excessive RBAC |
| **Dockerfile** | `USER root`, `privileged`, unpinned base images, secrets in build args |
| **GitHub Actions** | Script injection in `run:`, `pull_request_target` + checkout, unpinned actions |

## Impact tiers

Aligned with upstream rule categories (28 total, grouped here):

| Tier | Categories |
|---|---|
| **Critical** | SQL injection, command injection, XSS, XXE, path traversal, insecure deserialization, code injection, hardcoded secrets, memory safety (C/C++) |
| **High** | Insecure crypto, insecure transport, SSRF, JWT issues, CSRF, prototype pollution, unsafe functions, Terraform (AWS/Azure/GCP), Kubernetes, Docker, GitHub Actions |
| **Medium** | Regex DoS, race conditions / TOCTOU, correctness bugs with security impact |
| **Low** | General best practices, performance, maintainability (only when tied to security) |

## Evidence and reporting

Each finding should include:

- **Location** — file and line (or resource block in IaC)
- **Issue** — what can go wrong (one sentence)
- **Severity** — Critical / High / Medium / Low
- **CWE** — when applicable (e.g., CWE-89, CWE-79)
- **OWASP** — map to Top 10:2021 category (see review reference)
- **Fix** — concrete pattern (parameterize query, encode output, allowlist URL, etc.)

Avoid claiming exploitability without evidence; state assumptions (e.g., “if `host` is attacker-controlled”).
