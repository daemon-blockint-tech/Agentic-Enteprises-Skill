# Review checklist and OWASP mapping

## Table of contents

1. [Security review checklist](#security-review-checklist)
2. [OWASP Top 10:2021 quick map](#owasp-top-102021-quick-map)
3. [CWE quick reference](#cwe-quick-reference)
4. [Medium and low impact](#medium-and-low-impact)
5. [Finding template](#finding-template)

---

## Security review checklist

Use for reactive reviews. Check **Critical** before **High**.

### Critical

- [ ] **SQL injection** — no dynamic SQL from user input; parameterized queries only  
- [ ] **Command injection** — no shell with user data; argument arrays  
- [ ] **XSS** — encoded output; no unsafe `innerHTML` / unescaped templates  
- [ ] **XXE** — XML parsers hardened on untrusted XML  
- [ ] **Path traversal** — canonical paths under allowlisted base  
- [ ] **Insecure deserialization** — no pickle/Marshal/Java serialization on untrusted data  
- [ ] **Code injection** — no `eval`/dynamic code on user input  
- [ ] **Hardcoded secrets** — no keys/passwords in repo  
- [ ] **Memory safety (C/C++)** — bounds checks; avoid unsafe string APIs  

### High

- [ ] **Weak crypto** — modern algorithms; no MD5/SHA1/DES/ECB for security  
- [ ] **TLS** — verify certs; HTTPS in production  
- [ ] **SSRF** — URL allowlists; no user-controlled hosts  
- [ ] **JWT** — verify signature/alg/exp; no secrets in payload  
- [ ] **CSRF** — tokens or SameSite on state-changing cookie auth  
- [ ] **Prototype pollution (JS)** — safe object merge  
- [ ] **Unsafe functions** — no `gets`, `strcpy`, reckless `eval`  
- [ ] **Terraform** — encryption, least IAM, no public data stores  
- [ ] **Kubernetes** — non-root, non-privileged, drop caps  
- [ ] **Docker** — non-root user, no socket mount, pinned images  
- [ ] **GitHub Actions** — no script injection; careful `pull_request_target`  

### Medium / Low (when time permits)

- [ ] **ReDoS** — catastrophic backtracking in user-supplied regex  
- [ ] **Race / TOCTOU** — temp files, check-then-act  
- [ ] **Correctness** — null derefs, error handling hiding failures  

---

## OWASP Top 10:2021 quick map

| OWASP 2021 | Representative issues in this skill | Primary references |
|---|---|---|
| **A01 Broken Access Control** | IDOR patterns (validate object ownership), path traversal | injection reference, scope workflow |
| **A02 Cryptographic Failures** | Weak hash/cipher, hardcoded keys, TLS off | crypto_auth reference |
| **A03 Injection** | SQLi, command, XSS, code injection | injection reference |
| **A04 Insecure Design** | Missing rate limits, unsafe architecture (out of code-only scope) | escalate to design review |
| **A05 Security Misconfiguration** | XXE defaults, K8s/Docker/Terraform misconfig | deserialization_ssrf_xxe, infrastructure reference |
| **A06 Vulnerable Components** | Unpinned deps, old base images | note for `devsecops` / dependency scan |
| **A07 Identification & Auth Failures** | JWT, session, CSRF | crypto_auth reference |
| **A08 Software & Data Integrity** | Unsigned updates, unsafe deserialization | deserialization reference |
| **A09 Security Logging & Monitoring** | Missing audit on auth failures (brief) | log without secrets |
| **A10 SSRF** | User-controlled outbound requests | deserialization_ssrf_xxe reference |

---

## CWE quick reference

| CWE | Name | Category file |
|---|---|---|
| CWE-22 | Path traversal | injection_and_input_validation |
| CWE-78 | OS command injection | injection_and_input_validation |
| CWE-79 | XSS | injection_and_input_validation |
| CWE-89 | SQL injection | injection_and_input_validation |
| CWE-94 | Code injection | injection_and_input_validation |
| CWE-119 | Memory buffer issues | injection (C/C++); scope workflow |
| CWE-327 | Broken crypto | crypto_auth_and_session |
| CWE-347 | JWT issues | crypto_auth_and_session |
| CWE-352 | CSRF | crypto_auth_and_session |
| CWE-502 | Deserialization | deserialization_ssrf_xxe |
| CWE-611 | XXE | deserialization_ssrf_xxe |
| CWE-798 | Hardcoded credentials | crypto_auth_and_session |
| CWE-918 | SSRF | deserialization_ssrf_xxe |
| CWE-1333 | ReDoS | this file (medium) |
| CWE-1321 | Prototype pollution | injection_and_input_validation |

Full upstream index: 28 rule categories in source `rules/_sections.md` (not duplicated in this repo).

---

## Medium and low impact

### Regular expression DoS (ReDoS) — CWE-1333

**Risk:** User-supplied or attacker-influenced regex with catastrophic backtracking → CPU exhaustion.

**Mitigations:**

- Avoid nested quantifiers on overlapping alternations (`(a+)+`).
- Use regex timeouts (language-dependent) or RE2-style engines where appropriate.
- Prefer simple string operations or precompiled allowlists over complex regex on untrusted input.

### Race conditions — CWE-367

**Risk:** TOCTOU between check and use (temp files, privilege checks).

**Mitigations:**

- Use atomic create (`O_EXCL`), secure temp APIs.
- File locks where appropriate; avoid predictable temp paths in shared `/tmp`.

### Correctness with security impact

Logic bugs (off-by-one bounds, null checks, swallowed exceptions) can become vulnerabilities when they bypass auth or leak data. Flag when they affect security controls.

### Low-priority categories (source rules)

**Best practice, performance, maintainability** — address when they directly weaken security (e.g., deprecated crypto API usage). Do not expand scope into general style review; defer to `senior-software-engineer`.

---

## Finding template

```markdown
### [Critical|High|Medium|Low] Title (CWE-XXX, OWASP A0X)

**Location:** `path:line` or resource name  
**Issue:** One sentence describing abuse scenario.  
**Evidence:** Code snippet or config excerpt (minimal).  
**Fix:** Specific secure pattern or config change.  
**References:** OWASP cheat sheet or internal reference file name.
```

**Severity guidance:**

| Level | Typical examples |
|---|---|
| Critical | RCE, full DB read, secret in public repo, auth bypass |
| High | SSRF to metadata, weak crypto on passwords, open SG to world |
| Medium | ReDoS, race on non-critical resource |
| Low | Defense-in-depth improvements, style-adjacent hardening |
