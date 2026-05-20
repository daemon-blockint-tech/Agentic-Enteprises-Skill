# Primitives and algorithm selection

## Table of contents

1. [Selection framework](#selection-framework)
2. [Symmetric encryption and AEAD](#symmetric-encryption-and-aead)
3. [Hashes and MACs](#hashes-and-macs)
4. [Asymmetric encryption and key agreement](#asymmetric-encryption-and-key-agreement)
5. [Digital signatures](#digital-signatures)
6. [Password hashing vs KDFs](#password-hashing-vs-kdfs)
7. [Post-quantum awareness](#post-quantum-awareness)
8. [Deprecated and avoid](#deprecated-and-avoid)

## Selection framework

For each security goal, pick the **simplest standard construction** that meets requirements:

| Goal | Typical choice | Notes |
|---|---|---|
| Confidentiality + integrity (record) | AEAD | Never encrypt-then-MAC ad hoc without expert review |
| Integrity only | HMAC-SHA-256/384 or AEAD tag | Prefer AEAD when encrypting anyway |
| Key agreement | ECDH (X25519, P-256), optional hybrid PQ KEM | Forward secrecy via ephemeral keys |
| Digital signatures | Ed25519, ECDSA (P-256+), RSA-PSS (≥2048) | Match curve/hash to ecosystem |
| Password storage | Argon2id (preferred), bcrypt, scrypt | Tune memory/time cost to threat model |
| Key derivation | HKDF-SHA-256/384 | Salt + context string (`info`) per RFC 5869 |
| Random tokens | CSPRNG, ≥128-bit entropy | Not passwords; not timestamps alone |

Document **key size**, **expected lifetime**, **interoperability**, and **FIPS/compliance** constraints.

## Symmetric encryption and AEAD

| Algorithm | Use when | Pitfalls |
|---|---|---|
| **AES-GCM** | Broad hardware support, high throughput | **Nonce must never repeat** for a given key; prefer 96-bit nonce + counter discipline |
| **ChaCha20-Poly1305** | Software-only paths, mobile, constant-time friendly | Still requires unique nonces per key; do not reuse (key, nonce) |
| **AES-GCM-SIV** | Nonce-misuse resistance needed | Heavier; still prefer explicit nonce management |

**Rules:**

- One **256-bit key** for AES-GCM in new systems unless legacy forces 128-bit
- Define **nonce source** (random 96-bit vs deterministic counter with partition)
- Specify **associated data (AAD)** for metadata that must be authenticated but not encrypted
- Avoid **CBC mode** for new designs; if legacy CBC exists, require encrypt-then-MAC with careful padding analysis

## Hashes and MACs

| Primitive | Role |
|---|---|
| SHA-256 | General hashing, HKDF, certificate fingerprints |
| SHA-384 | Policies requiring longer hash output |
| SHA-1 | **Deprecated** for security use; legacy interop only with migration plan |
| HMAC-SHA-256 | API tokens, legacy MAC where AEAD is not used |
| Poly1305 | Integrated in ChaCha20-Poly1305 AEAD |

Do not use fast hashes (MD5, SHA-1) for **password storage** or **signatures**.

## Asymmetric encryption and key agreement

| Mechanism | Guidance |
|---|---|
| **X25519 / Curve25519 ECDH** | Preferred for new TLS and protocols |
| **P-256 ECDH** | When FIPS or ecosystem requires NIST curves |
| **RSA encryption (OAEP)** | Legacy interop; prefer ECDH + AEAD for new designs |
| **RSA key size** | Minimum **2048**; prefer **3072+** for long-lived roots; **1024 forbidden** |
| **Static DH** | Avoid; prefer ephemeral (ECDHE) for forward secrecy |

**Hybrid encryption pattern:** ephemeral ECDH → HKDF → AEAD for payload. Do not invent custom KDF chains.

## Digital signatures

| Algorithm | Guidance |
|---|---|
| **Ed25519** | Preferred for new software signing, tokens, protocols |
| **ECDSA (P-256, P-384)** | Common in TLS and hardware; require **deterministic nonce (RFC 6979)** or HSM |
| **RSA-PSS** | Legacy PKI, code signing; use PSS not PKCS#1 v1.5 for new designs |
| **RSA PKCS#1 v1.5** | Legacy only; plan migration |

Verify **hash algorithm** alignment (e.g., ECDSA with SHA-256), **curve points** validation, and **signature malleability** where relevant (Bitcoin contexts differ from TLS).

## Password hashing vs KDFs

| Problem | Tool | Parameters |
|---|---|---|
| Human password storage | **Argon2id** (1st choice), bcrypt, scrypt | Memory/time cost tuned to hardware; unique salt per user |
| Stretching password → key | Argon2/bcrypt output → optional HKDF | Separate from storing verification string |
| Protocol key derivation | **HKDF** | Extract-and-expand with domain-separated `info` labels |
| Legacy PBKDF2 | PBKDF2-HMAC-SHA-256 | High iteration count if Argon2 unavailable |

**Never:** use bare SHA-256 on passwords; reuse password hash as encryption key without domain separation.

## Post-quantum awareness

At **architecture** level (not certification):

- Inventory **long-lived confidentiality** (archived ciphertext, recorded TLS if HNDL relevant)
- Prefer **hybrid** key establishment (classical + PQ KEM) where standards and libraries support
- Track **NIST PQC** selected algorithms and TLS/experimental profiles for your stack
- Plan **agility**: algorithm identifiers, version negotiation, cipher suite extensibility

Do not deploy experimental PQ without library maturity review and rollback plan.

## Deprecated and avoid

| Item | Action |
|---|---|
| DES, 3DES, RC4 | Remove |
| MD5, SHA-1 (security) | Migrate |
| RSA-1024 | Remove |
| TLS 1.0, 1.1, SSLv3 | Disable |
| EXPORT ciphers, NULL encryption | Forbidden |
| ECB mode | Do not use for structured data |
| Custom "simple XOR" schemes | Reject |
| Nonce reuse with GCM | Catastrophic; block release |

Maintain an **internal approved-algorithms list** with sunset dates and exception process.
