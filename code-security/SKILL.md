---
name: code-security
description: |
  Guides secure coding and security-focused code review across languages and infrastructure—OWASP-oriented
  vulnerability patterns (injection, XSS, auth, crypto, deserialization, SSRF, XXE), secrets handling,
  and IaC security (Terraform, Kubernetes, Docker, GitHub Actions).
  Use when writing or reviewing code that handles user input, authentication, files, databases,
  network requests, cryptography, or infrastructure config—or when the user asks to check for SQL
  injection, XSS, SSRF, hardcoded secrets, OWASP issues, Terraform security, or GitHub Actions security.
  Not for authorized penetration test engagements (ai-redteam, cybersecurity), compliance program
  mapping (compliance-engineer), YARA/malware rules (yara-rule-authoring), or CI pipeline setup only
  (devsecops).
---

# Code Security

## When to Use

- Write or review application code for common vulnerability classes (injection, XSS, auth, crypto, SSRF, XXE, deserialization)
- Review secrets handling, session/JWT patterns, and transport security in code
- Review Terraform, Kubernetes manifests, Dockerfiles, or GitHub Actions for security misconfigurations
- Proactively harden code that accepts user input, performs I/O, queries databases, or calls external URLs
- Map findings to CWE/OWASP categories and suggest concrete secure patterns

## When NOT to Use

- Plan or execute authorized penetration tests, exploit chains, or red-team campaigns → `ai-redteam`, `cybersecurity`, `penetration-tester`, `red-team-specialist`
- Map controls to SOC 2, ISO 27001, or build audit evidence packages → `compliance-engineer`, `compliance-specialist`
- Deploy SIEM, IdP, KMS, WAF, or operate security tooling → `information-security-engineer`
- Configure CI/CD scanners, SBOM, OIDC, or pipeline gates without secure-coding review → `devsecops`
- Author YARA or malware detection rules → `yara-rule-authoring`
- General feature design, RFCs, or refactoring without a security lens → `senior-software-engineer`

## Related skills

| Need | Skill |
|---|---|
| Security program strategy, policies, IR | `cybersecurity` |
| Control implementation, IdP, KMS, SIEM | `information-security-engineer` |
| CI/CD security gates, SBOM, pipeline OIDC | `devsecops` |
| Audit evidence and framework mapping | `compliance-engineer` |
| LLM/agent red team and prompt injection | `ai-redteam` |
| Code review, RFCs, reliability (non-security) | `senior-software-engineer` |
| Cloud account guardrails and CSPM | `cloud-security-engineer` |
| Cryptographic primitive/protocol design | `cryptographer-specialist` |
| Pentest findings reproduction | `penetration-tester`, `web-pentester` |

## How to work

### Modes

- **Proactive** — When writing or touching security-sensitive code (input, auth, files, DB, HTTP clients, crypto, IaC), check relevant categories without waiting for an explicit security ask.
- **Reactive** — When the user requests a security review, follow the review workflow in `references/review_checklist_and_owasp_mapping.md`.

### Workflow

1. Identify language/stack and what the code does (input? DB? shell? XML? outbound HTTP? secrets? IaC?).
2. Load the matching reference(s) below; prioritize **Critical** then **High** impact.
3. Flag vulnerable patterns with CWE/OWASP labels; propose secure alternatives from references (language-specific examples live there).
4. For reviews, produce severity-ordered findings with file/line context and fix guidance.

### Language priority (first checks)

| Language / stack | Priority topics |
|---|---|
| Python | SQL/command injection, path traversal, code injection, SSRF, insecure crypto, deserialization |
| JavaScript/TypeScript | XSS, prototype pollution, code injection, CSRF, insecure transport |
| Java | SQL injection, XXE, insecure deserialization, SSRF, insecure crypto |
| Go | SQL/command injection, path traversal, SSRF, insecure transport |
| C/C++ | Memory safety, unsafe functions, command injection, path traversal |
| Ruby / PHP | SQL/command injection, XSS, deserialization (Ruby), code injection |
| HCL / YAML | Terraform (AWS/Azure/GCP), Kubernetes, Docker, GitHub Actions |

## When to load references

Detailed vulnerable/secure patterns and multi-language examples are in `references/` (condensed from 28 upstream rule categories). Do not expect per-language copies of every rule in `SKILL.md`.

| Topic | Reference |
|---|---|
| Scope, modes, language priorities | `references/code_security_scope_and_workflow.md` |
| SQL, command, XSS, path traversal, code injection | `references/injection_and_input_validation.md` |
| Secrets, JWT, CSRF, crypto, TLS | `references/crypto_auth_and_session.md` |
| XXE, deserialization, SSRF | `references/deserialization_ssrf_xxe.md` |
| Terraform, K8s, Docker, GitHub Actions | `references/infrastructure_as_code_security.md` |
| Review checklist, CWE/OWASP map, medium/low | `references/review_checklist_and_owasp_mapping.md` |

## Quick prevention reference

| Vulnerability | Key prevention |
|---|---|
| SQL injection | Parameterized queries / prepared statements |
| XSS | Context-aware output encoding; CSP where appropriate |
| Command injection | Avoid shell; use APIs with argument lists |
| Path traversal | Canonicalize paths; allowlist base directories |
| SSRF | URL allowlists; block metadata/link-local ranges |
| Secrets | Env vars / secret managers; never commit credentials |
| Weak crypto | SHA-256+, AES-256-GCM; avoid MD5/SHA1/DES/ECB |
| XXE | Disable DTD/external entities in XML parsers |
| Deserialization | Do not deserialize untrusted data |
