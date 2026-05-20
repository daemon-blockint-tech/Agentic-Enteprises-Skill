# Cryptography, authentication, and session security

## Table of contents

1. [Hardcoded secrets](#hardcoded-secrets)
2. [Cryptographic algorithms](#cryptographic-algorithms)
3. [Transport security (TLS)](#transport-security-tls)
4. [JWT authentication](#jwt-authentication)
5. [CSRF](#csrf)
6. [Session management](#session-management)

**CWE:** 798 (hardcoded credentials), 327 (weak crypto), 319 (cleartext), 347 (JWT), 352 (CSRF)

---

## Hardcoded secrets

**Risk:** Credentials in source, config committed to VCS, or logs—unauthorized access and difficult rotation.

**Never hardcode:** API keys, passwords, private keys, connection strings, signing secrets, webhook HMAC keys.

**Secure patterns:**

| Approach | Use when |
|---|---|
| Environment variables | Local dev, simple deploys |
| Secret manager (Vault, AWS SM, GCP SM) | Production |
| CI/CD secret stores | Pipelines (not literals in YAML) |
| Short-lived tokens | Prefer over long-lived API keys |

**Review heuristics:** High-entropy strings in code, `AKIA`, `BEGIN PRIVATE KEY`, `password =`, default credentials in samples.

**On exposure:** Rotate immediately; assume compromise if ever committed to git history.

---

## Cryptographic algorithms

**Avoid (broken or weak):**

| Category | Weak | Prefer |
|---|---|---|
| Hashing passwords | MD5, SHA1, plain SHA256 alone | Argon2id, scrypt, bcrypt (with work factor) |
| Integrity | MD5, SHA1 for security | SHA-256+ or BLAKE2 |
| Symmetric encryption | DES, 3DES, RC4, AES-ECB | AES-256-GCM or ChaCha20-Poly1305 |
| Randomness | `Math.random()`, predictable seeds | `secrets` (Python), `crypto.randomBytes` (Node), `SecureRandom` (Java) |

**Key management:** Generate keys in HSM/KMS; separate encryption keys per tenant where required; document rotation.

**Do not roll custom crypto protocols** — use established libraries and protocols (TLS, NaCl/libsodium, framework crypto).

---

## Transport security (TLS)

**Risk:** Credentials and data exposed on the wire; MITM if verification disabled.

**Requirements:**

- HTTPS for all production traffic; HSTS for browser apps.
- **Verify certificates** — never disable TLS verification in production (`rejectUnauthorized: false`, `verify=False`).
- Modern TLS versions (1.2+; prefer 1.3); disable weak ciphers.
- Certificate pinning only when justified and maintained.

**Review heuristics:** `http://` in production URLs, custom `TrustManager` that accepts all certs, curl `-k`.

---

## JWT authentication

**Risk:** Forged or altered tokens if verification is missing or weak.

**Checks:**

| Issue | Mitigation |
|---|---|
| `alg: none` or algorithm confusion | Explicitly allow only expected algs (e.g., RS256); verify signature |
| Weak HMAC secret | Long random secret from secret manager; prefer asymmetric keys |
| Missing `exp` / `nbf` | Validate time claims with clock skew tolerance |
| Sensitive data in payload | JWTs are signed, not encrypted—do not store PII/secrets in claims |
| Token in URL | Prefer `Authorization: Bearer` header; avoid query strings (logs, Referer) |

**Pattern:** Use maintained libraries; always call `verify` with issuer/audience checks.

---

## CSRF

**Risk:** Browser sends authenticated requests the user did not intend.

**Mitigate state-changing operations (POST/PUT/PATCH/DELETE):**

- Synchronizer token (CSRF token in form + cookie/header).
- `SameSite` cookies (`Strict` or `Lax` where compatible).
- Double-submit cookie pattern only with care (still prefer framework CSRF middleware).
- For APIs: avoid cookie auth without CSRF protection; use tokens with explicit client actions.

**Not required for:** Pure read-only GET with no side effects (still avoid sensitive data in GET URLs).

---

## Session management

| Practice | Detail |
|---|---|
| Session ID entropy | Cryptographically random, sufficient length |
| Cookie flags | `HttpOnly`, `Secure`, `SameSite` |
| Fixation | Regenerate session ID on login |
| Timeout | Idle and absolute timeouts |
| Logout | Invalidate server-side session |
| Storage | Server-side session store or hardened JWT strategy—not client-only trust |

Coordinate with `information-security-engineer` for enterprise IdP/SSO patterns.
