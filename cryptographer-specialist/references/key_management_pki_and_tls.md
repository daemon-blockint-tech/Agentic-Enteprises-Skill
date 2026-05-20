# Key management, PKI, and TLS

## Table of contents

1. [Key hierarchy](#key-hierarchy)
2. [Generation and storage](#generation-and-storage)
3. [Rotation and lifecycle](#rotation-and-lifecycle)
4. [Escrow and recovery](#escrow-and-recovery)
5. [HSM and KMS patterns](#hsm-and-kms-patterns)
6. [PKI architecture](#pki-architecture)
7. [TLS configuration](#tls-configuration)
8. [Monitoring and incident response](#monitoring-and-incident-response)

## Key hierarchy

Typical layers:

```
root CA (offline) → issuing CA / intermediate → end-entity certs / workload keys
         ↓
   data encryption keys (DEK) wrapped by KEK in KMS/HSM
```

| Key type | Lifetime | Storage |
|---|---|---|
| Root CA private key | 10–20 years (with planned replacement) | Offline HSM, ceremony, dual control |
| Issuing CA | 3–7 years | HSM or cloud CA service |
| TLS server cert | 90 days–1 year (prefer short) | KMS, cert manager, vault |
| Data encryption key (DEK) | Per object or rotation policy | Wrapped; never plaintext in logs |
| Session keys | Minutes–hours | Memory only; derived via HKDF/TLS KDF |

Document **purpose binding**: a key used for TLS must not be reused for code signing or device attestation.

## Generation and storage

**Generation:**

- Use **approved libraries** or HSM/KMS `GenerateKey` APIs
- Enforce minimum sizes (AES-256, RSA ≥2048, EC P-256+)
- Record **provenance** (who/what created, which HSM slot)

**Storage:**

| Tier | Pattern |
|---|---|
| Highest | HSM, cloud HSM, secure enclave; non-exportable keys |
| Standard | KMS with IAM/policy; envelope encryption |
| Application | Sealed secrets, vault dynamic secrets; short TTL |
| Forbidden | Source code, git, tickets, chat, unencrypted disks |

**Wrapping:** DEK encrypted under KEK; rotate KEK without re-encrypting all data when using KMS native rotation, or plan re-wrap jobs.

## Rotation and lifecycle

| Asset | Rotation driver |
|---|---|
| TLS server certs | Expiry (automate ACME or internal CA) |
| API signing keys | Calendar + on compromise |
| Data keys | Policy, crypto period, or customer requirement |
| Root CA | Planned succession; cross-sign during transition |

**Rotation checklist:**

1. Issue new key/cert alongside old (overlap window)
2. Deploy consumers that trust **both** during migration
3. Revoke or disable old after cutover metrics green
4. Audit logs for stragglers using retired key IDs
5. Update **key version** metadata in ciphertext headers

## Escrow and recovery

Escrow is **high risk**—require explicit policy:

- **When allowed:** regulated environments, enterprise recovery with split knowledge
- **When forbidden:** E2E messaging keys, device-only keys, zero-knowledge designs
- **Controls:** M-of-N ceremonies, HSM policies, audit every unwrap, time-bound access

Document **recovery RTO/RPO** without weakening confidentiality for non-escrowed data.

## HSM and KMS patterns

| Pattern | Use |
|---|---|
| Envelope encryption | App generates DEK; KMS wraps DEK |
| Sign-only HSM | Private key non-exportable; API `Sign` |
| TLS termination on LB | Keys in KMS/LB; understand trust boundary |
| BYOK / HYOK | Customer key material in cloud HSM; policy sync |

**IAM:** separate roles for `encrypt`, `decrypt`, `admin`, `audit`; no human uses admin for daily ops.

**Cloud notes:** enable **KMS CloudTrail/audit**, deny `kms:Disable*`, use **grants** sparingly with expiry.

## PKI architecture

**Internal CA:**

- Offline root; online issuing CA with CRL/OCSP or short-lived certs (prefer latter)
- **Name constraints**, EKU (serverAuth, clientAuth), max path length
- **Certificate Transparency** for public TLS where applicable

**Profiles:**

| Profile | Typical fields |
|---|---|
| Public web TLS | SAN = DNS names, key usage serverAuth, 90-day validity |
| mTLS client | ClientAuth EKU, device or service identity in SAN/URI |
| Code signing | Extended validation policies, timestamping service |
| Email (S/MIME) | Declining; if used, strict key usage and distribution |

**Revocation:** prefer **short-lived certs** over long CRLs; have break-glass revocation procedure.

## TLS configuration

**Minimum bar (new deployments):**

- TLS **1.2+**; prefer **1.3** where clients support
- **ECDHE** forward secrecy; disable static RSA key transport
- AEAD suites: `TLS_AES_256_GCM_SHA384`, `TLS_CHACHA20_POLY1305_SHA256`, `TLS_AES_128_GCM_SHA256`
- Disable **TLS 1.0/1.1**, **3DES**, **RC4**, **NULL**, **EXPORT**

**Certificate validation:**

- Full chain to trusted store; **hostname verification** (SAN)
- Consider **pinning** only with update strategy (SPKI hashes, backup pins)
- **OCSP stapling** where supported to improve privacy and reliability

**Operational:**

- Automate renewal; alert at 30/14/7 days
- Document **cipher order** vs client quirks (legacy mobile, regional regulators)
- Test with **sslscan/testssl** or CI TLS probes after changes

## Monitoring and incident response

Monitor for:

- Cert **expiry** and failed renewals
- Sudden **cipher downgrade** or protocol anomalies
- KMS **Decrypt** spikes, failed authentication to HSM
- New **CA issuances** outside change windows

On compromise: rotate affected keys, revoke certs, assess **wrapped DEK** exposure, notify per incident process—not legal advice.
