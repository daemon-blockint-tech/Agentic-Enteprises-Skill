# Implementation pitfalls and side channels

## Table of contents

1. [AEAD and nonce discipline](#aead-and-nonce-discipline)
2. [API design mistakes](#api-design-mistakes)
3. [Randomness and entropy](#randomness-and-entropy)
4. [Constant-time and side channels](#constant-time-and-side-channels)
5. [Memory and zeroization](#memory-and-zeroization)
6. [Error handling and oracle attacks](#error-handling-and-oracle-attacks)
7. [Library and dependency hygiene](#library-and-dependency-hygiene)
8. [Verification checklist](#verification-checklist)

## AEAD and nonce discipline

**AES-GCM / ChaCha20-Poly1305:**

- **Never reuse** `(key, nonce)` — disclosure of plaintext and forgery keys possible (GCM)
- Prefer **random 96-bit nonce** per message under a random key, or **counter** with partition per sender
- Document max messages per key before rotation (GCM volume limits ~2^32 blocks with same key in some policies)

**Associated data (AAD):**

- Authenticate **version, type, length, context** in AAD when not inside ciphertext
- Keep AAD **canonical** (stable encoding) to avoid ambiguity attacks

**Key separation:**

- Distinct keys for **encrypt vs MAC** vs **IV generation** when not using integrated AEAD
- Do not derive all keys from one hash output without HKDF labels

## API design mistakes

| Mistake | Safer approach |
|---|---|
| Exposing **encrypt** without authentication | Always AEAD or encrypt-then-MAC |
| **Deterministic IV** from plaintext hash | Random nonce or SIV modes |
| User-selectable **"NULL" cipher** | Compile-time or policy deny |
| Parsing **unauthenticated** fields before verify | Verify-then-decrypt; constant-time compare |
| **Compare** secrets with `==` on strings | `crypto/subtle.ConstantTimeCompare` or libs |
| Storing keys in **env vars** visible to all processes | KMS, HSM, restricted mounts |

## Randomness and entropy

- Use OS CSPRNG (`getrandom`, `BCryptGenRandom`, `crypto/rand`)
- Seed **userspace DRBG** from OS only; do not seed from time/PID alone
- **Tokens:** at least 128 bits entropy; use URL-safe encoding without shortening
- **Key generation:** in HSM/KMS when policy requires; log generation events

**Failures:** VM clone without fresh seed, embedded devices without hardware RNG—require health checks.

## Constant-time and side channels

**Threat:** attacker measures time, cache, or power to infer secrets.

**High-risk operations:**

- Private key operations (RSA, ECDSA)
- AES key schedule on secret keys (less issue with AES-NI bulk)
- Comparison of MACs/passwords
- Branching on secret-dependent memory indices

**Mitigations:**

- Use libraries with **constant-time** implementations (libsodium, BearSSL patterns, verified builds)
- Avoid secret-dependent branches in custom code
- Prefer **Ed25519/X25519** over RSA where possible for performance and timing
- Isolate crypto in **separate process/HSM** for high-value keys

Use `constant-time-analysis` and `constant-time-testing` (agent catalog) for targeted audits.

## Memory and zeroization

- Zero **stack buffers** holding keys/passwords after use where language allows
- Avoid **swapping** sensitive pages where possible (`mlock`—platform specific, operational tradeoff)
- Prevent keys in **core dumps** and crash reports
- Clear **String** objects that held passwords (language-dependent; prefer byte arrays)

Use `zeroize-audit` (agent catalog) for C/C++/Rust secret lifecycle reviews.

## Error handling and oracle attacks

| Oracle | Example | Mitigation |
|---|---|---|
| Padding oracle | CBC padding errors differ | Use AEAD; uniform errors |
| Bleichenbacher | RSA PKCS#1 v1.5 decrypt errors | RSA-OAEP; constant-time handling |
| MAC verify | Different error messages/timing | Single generic failure; constant-time MAC compare |
| Certificate parse | Detailed TLS alert differences | Uniform policy; logging server-side only |

**Rule:** return **one** client-visible error for auth/decrypt failures; log details server-side with correlation ID.

## Library and dependency hygiene

- Pin **versions** of crypto libraries; monitor CVEs (OpenSSL, BoringSSL, mbedTLS, etc.)
- Enable **FIPS mode** only when required—understand algorithm restrictions
- Disable **legacy providers** in OpenSSL 3.x where possible
- Do not fork **boring crypto** snippets from Stack Overflow
- Run **known-answer tests** and Wycheproof vectors where available

## Verification checklist

Before release of crypto-touching code:

- [ ] Nonce/uniqueness rules documented and enforced in API
- [ ] No secret branches or early returns on failed MAC compare
- [ ] Keys only in KMS/HSM or sealed config—not repos
- [ ] TLS config scanned; certs monitored
- [ ] Test vectors from RFCs or Wycheproof for parsers and edge cases
- [ ] Threat model updated if protocol fields changed
- [ ] Peer review by second engineer with crypto literacy
- [ ] Fuzzing on decoders (length fields, ASN.1) where applicable
