---
name: d3fend-harden
description: |
  Guides cybersecurity hardening controls using MITRE D3FEND—authentication, application hardening,
  credential management, message integrity, platform security, and source code defenses.
  Covers MFA, certificate pinning, control flow integrity, encryption, input validation,
  and secure configuration. Use when hardening systems, configuring auth, implementing
  encryption, or reviewing code security—not for detection rules (d3fend-detect),
  network segmentation (d3fend-isolate), or incident response (d3fend-evict).
---

# D3FEND — Harden

## When to Use

- Implementing authentication controls (MFA, certificates, biometrics, tokens)
- Hardening applications and platforms (configuration, patches, encryption)
- Managing credential lifecycle (rotation, pinning, scrubbing, policies)
- Validating input and enforcing domain/operational logic
- Securing source code (memory safety, pointer validation, dead code elimination)
- Reviewing boot integrity, driver signing, and firmware protections

## When NOT to Use

- Detection engineering or monitoring → `d3fend-detect`
- Network segmentation or access mediation → `d3fend-isolate`
- Decoy and deception operations → `d3fend-deceive`
- Incident response or eviction → `d3fend-evict`
- Secure coding deep dives → `devsecops` / `senior-software-engineer`

## Core Workflows

### 1. Authentication Hardening

| Control | Implementation |
|---|---|
| Multi-factor Authentication | TOTP, WebAuthn, hardware keys |
| Certificate-based Auth | mTLS, client certs, PKI |
| Biometric Auth | Fingerprint, face, behavioral |
| Token-based Auth | JWT with short expiry, rotation |
| Password Policy | Length, complexity, breach check |

**See `references/authentication.md`**

### 2. Application & Platform Hardening

- Application config hardening (disable unused features, remote access)
- Control flow integrity (CFI, stack canaries, ASLR, pointer auth)
- Bootloader authentication, TPM boot integrity
- Disk/file encryption, hardware write protection
- Software update management, driver load integrity

**See `references/application_platform.md`**

### 3. Credential & Message Hardening

- Credential rotation (certs, passwords, tokens)
- Certificate pinning (mobile, embedded)
- Message authentication (HMAC, MAC) and encryption
- Token binding to prevent session hijacking

**See `references/credential_message.md`**

### 4. Source Code Hardening

- Input validation (range, type, pointer, null checks)
- Memory safety (initialization, nullification, bounds)
- Use trusted libraries, eliminate dead code
- Exception handler validation, domain logic checks

**See `references/source_code.md`**

## When to load references

- **Authentication** → `references/authentication.md`
- **Application & platform** → `references/application_platform.md`
- **Credential & message** → `references/credential_message.md`
- **Source code** → `references/source_code.md`
