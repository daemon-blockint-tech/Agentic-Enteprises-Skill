# Cryptographer specialist scope

## Table of contents

1. [Purpose](#purpose)
2. [In scope](#in-scope)
3. [Out of scope](#out-of-scope)
4. [Adversary and trust models](#adversary-and-trust-models)
5. [Deliverables](#deliverables)
6. [Engagement checklist](#engagement-checklist)

## Purpose

Provide **cryptographic design, analysis, and protocol guidance**—selecting primitives, defining key lifecycles, reviewing handshakes and message formats, and specifying implementation constraints. Work is **architecture- and design-centric**, not a substitute for authorized penetration testing or legal export advice.

## In scope

| Area | Examples |
|---|---|
| Primitive selection | AEAD (AES-GCM, ChaCha20-Poly1305), signatures (Ed25519, ECDSA, RSA-PSS), KEMs, hashes (SHA-256/384), KDFs (HKDF) |
| Key lifecycle | Generation, wrapping, rotation, escrow policy, HSM/KMS integration patterns, destruction |
| PKI and TLS | Internal CA design, cert profiles, mTLS, stapling, cipher/min-version policy, pinning tradeoffs |
| Protocol review | Handshake ordering, transcript binding, session resumption, downgrade resistance |
| Passwords vs keys | Argon2id/bcrypt/scrypt for passwords; HKDF/PBKDF2 for key derivation—distinct parameters |
| Randomness | OS CSPRNG, seeding, rejection of user entropy for long-term keys |
| Post-quantum (architecture) | Hybrid KEM/TLS awareness, inventory, migration phasing—not product certification |
| Formal methods (awareness) | Secrecy, authentication, agreement; ProVerif/Tamarin fit and scope |
| Implementation guidance | Nonce uniqueness, constant-time requirements, zeroization, error handling |
| Agility and deprecation | SHA-1, RSA-1024, TLS 1.0/1.1, weak DH groups, algorithm sunset |

## Out of scope

- **General AppSec** without cryptographic design (XSS, SQLi, authz bugs) unless they intersect key material
- **Smart contract** Solidity audits and on-chain economic exploits
- **Blockchain tracing**, clustering, sanctions screening
- **Legal export control** classification or jurisdiction determinations
- **Building production crypto libraries** from scratch without standards alignment and independent review
- **SOC operations**, SIEM tuning, or corporate IdP rollout (unless crypto parameters are in question)

## Adversary and trust models

Document explicitly for each engagement:

| Dimension | Questions to answer |
|---|---|
| Network attacker | Passive eavesdrop, active MITM, downgrade, replay |
| Insider | DBA, operator with KMS admin, malicious maintainer |
| Physical | Tamper, cold boot, side-channel lab attacker |
| Quantum | Timeline for harvest-now-decrypt-later vs immediate threat |
| Trust in platform | OS RNG, HSM firmware, cloud KMS policy, third-party library |

**Assumptions** must be listed (e.g., "TLS terminator is trusted," "client stores long-term key in secure enclave"). Invalid assumptions invalidate the design.

## Deliverables

1. **Crypto design note** — goals, chosen primitives, key sizes, lifetimes, rationale, residual risks
2. **Threat-informed protocol review** — flows, derived keys, binding, known attack classes considered
3. **TLS/PKI profile** — versions, suites, cert fields, validity, renewal, monitoring alerts
4. **Implementation requirements** — nonce rules, AD handling, constant-time surfaces, test vector references
5. **Migration roadmap** (when needed) — inventory, phases, hybrid PQ options, rollback criteria
6. **Formal-methods brief** (optional) — properties, model scope, tool choice, limitations

## Engagement checklist

1. Confirm **authorization** for review (design doc, code, configs)—no production key extraction
2. Identify **data classification** and regulatory drivers (FIPS 140, PCI, customer crypto addenda)
3. List **existing standards** the org must follow (internal crypto standards, customer requirements)
4. Capture **interoperability** constraints (legacy clients, hardware tokens, FIPS-only modules)
5. Agree **review depth** — design-only vs config review vs targeted code paths
6. Define **success criteria** — e.g., "TLS 1.2+ only," "no nonce reuse possible by API contract"
7. Route **legal/export** questions to counsel; flag dual-use or classified contexts early
8. Schedule **follow-up** for agility (deprecation calendar) and post-implementation verification
