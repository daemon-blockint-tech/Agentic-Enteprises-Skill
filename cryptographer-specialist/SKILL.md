---
name: cryptographer-specialist
description: |
  This skill should be used when the user asks for a cryptographer, cryptography review,
  help to choose a cipher (AES-GCM, ChaCha20-Poly1305, ECDH, RSA tradeoffs), key management,
  PKI design, TLS configuration, protocol security or handshake review, authenticated encryption,
  digital signature scheme design, post-quantum migration at architecture level, ProVerif or
  Tamarin modeling concepts, nonce reuse or IV misuse analysis, HKDF vs password hashing (Argon2),
  HSM or KMS usage patterns, secure randomness, side-channel and constant-time requirements,
  or cryptographic agility and algorithm deprecation—not general OWASP web app review only
  (information-security-engineer), secure coding checklists without crypto depth, Solidity or
  smart contract audits, blockchain wallet tracing, legal export classification, or shipping
  custom production crypto without design and review gates.
---

# Cryptographer Specialist

## When to Use

- Select and justify **cryptographic primitives** (AEAD, signatures, KEMs, hashes, KDFs)
- Design **key lifecycle** — generation, storage, rotation, escrow policy, destruction, dual control
- Architect **PKI and TLS** — internal CAs, cert profiles, mTLS, pinning, stapling, cipher policies
- Review **protocols** — handshakes, transcript binding, downgrade resistance, session keys
- Analyze **authenticated encryption misuse** — nonces, IVs, associated data, key separation
- Compare **password hashing** (Argon2, bcrypt, scrypt) vs **KDFs** (HKDF, PBKDF2) for the use case
- Plan **post-quantum awareness** — hybrid schemes, inventory, migration sequencing (architecture level)
- Frame **formal properties** — secrecy, authentication, forward secrecy, agreement (ProVerif/Tamarin concepts)
- Specify **implementation requirements** — constant-time, zeroization, entropy, crypto agility
- Produce **crypto design reviews** and threat-informed recommendations with explicit assumptions

## When NOT to Use

- General OWASP web/API pentest or app-layer vuln triage without crypto design → `information-security-engineer`, `web-pentester`, `penetration-tester`
- Broad secure-coding review across stacks (injection, authz, headers) without primitive/protocol focus → use secure-coding skills in the agent catalog (e.g. `code-security` when installed)
- Deploy SIEM, IdP, EDR, or corp guardrails without cryptographic design → `information-security-engineer`
- Solidity/EVM smart contract audit or DeFi on-chain triage → `evm-solidity-defi-triage-agent` (agent skill) or protocol-specific audit skills
- Blockchain address tracing, clustering, or compliance screening → blockint / on-chain investigation skills
- **Legal export control**, sanctions, or jurisdiction classification → `commercial-counsel` (legal boundaries only; not legal advice)
- Implement a **full production crypto library** from scratch without peer review, standards alignment, and test vectors
- ML adversarial robustness on models → `ai-adversarial-robustness-engineer`
- Assurance cases and DO-178C-style software assurance without crypto-specific claims → `software-assurance-formal-methods-specialist`

## Related skills

| Need | Skill |
|---|---|
| KMS/TLS deployment, secrets stores, corp encryption ops | `information-security-engineer` |
| Secure coding and vulnerability patterns (general) | `code-security` (agent catalog, when available) |
| Constant-time implementation review | `constant-time-analysis`, `constant-time-testing` (agent catalog) |
| Protocol sequence diagrams from specs/code | `crypto-protocol-diagram` (agent catalog) |
| Mermaid → ProVerif model translation | `mermaid-to-proverif` (agent catalog) |
| Secret zeroization audit in C/C++/Rust | `zeroize-audit` (agent catalog) |
| Contract/export and commercial legal boundaries | `commercial-counsel` |
| Formal assurance cases, GSN, DO-178C context | `software-assurance-formal-methods-specialist` |
| CI/CD and supply-chain crypto in pipelines | `devsecops` |
| Cloud KMS, cert managers, private CA in cloud | `cloud-security-engineer` |

## Core Workflows

### 1. Scope and assets

1. Identify **protected assets** (keys, plaintext, metadata, identities, logs)
2. Define **adversary model** — network, insider, physical, quantum timeline
3. List **trust boundaries** and **assumptions** (HSM, OS RNG, third-party libraries)
4. Record **compliance or policy constraints** (FIPS, regional, customer crypto profiles)

**See `references/cryptographer_specialist_scope.md`.**

### 2. Primitive and algorithm selection

Map security goals to approved primitive families; document tradeoffs and deprecation status.

**See `references/primitives_and_algorithm_selection.md`.**

### 3. Key management, PKI, and TLS

Design key hierarchy, rotation, escrow exceptions, and certificate/TLS profiles.

**See `references/key_management_pki_and_tls.md`.**

### 4. Protocol design and security properties

Specify messages, key derivation, binding, and the properties each layer must achieve.

**See `references/protocol_design_and_properties.md`.**

### 5. Implementation pitfalls and side channels

Translate design into developer requirements: AEAD usage, timing, memory, RNG, error handling.

**See `references/implementation_pitfalls_and_side_channels.md`.**

### 6. Formal methods, agility, and governance

Align with verification artifacts, algorithm sunset, and review gates for crypto changes.

**See `references/formal_methods_agility_governance.md`.**

## Outputs

- **Crypto design note** — goals, primitives, key sizes, lifetimes, assumptions, open risks
- **Protocol review** — message flow, derived keys, downgrade and replay analysis
- **TLS/PKI profile** — versions, cipher suites, cert fields, rotation, monitoring
- **Implementation checklist** — nonce rules, constant-time surfaces, zeroization, test vectors
- **Migration plan** — deprecated algorithms, PQ hybrid options, inventory and phases
- **Formal-methods brief** — intended properties, model scope, tool fit (when applicable)

## Principles

- Prefer **well-vetted libraries and standards** (RFCs, NIST, CFRG) over custom constructions
- **Never roll your own** block cipher, hash, or protocol; compose proven building blocks
- Separate **confidentiality, integrity, and identity** keys; document **nonce uniqueness** rules
- Treat **password hashing** and **key derivation** as different problems with different parameters
- Plan **crypto agility** before algorithms break; monitor deprecations (SHA-1, RSA-1024, TLS 1.0/1.1)
- Escalate **legal/export** questions to counsel; do not provide export classification advice

## When to load references

- **Scope and boundaries** → `references/cryptographer_specialist_scope.md`
- **Algorithms and primitives** → `references/primitives_and_algorithm_selection.md`
- **Keys, PKI, TLS** → `references/key_management_pki_and_tls.md`
- **Protocols and properties** → `references/protocol_design_and_properties.md`
- **Implementation and side channels** → `references/implementation_pitfalls_and_side_channels.md`
- **Formal methods and governance** → `references/formal_methods_agility_governance.md`
