# Formal methods, agility, and governance

## Table of contents

1. [Crypto governance](#crypto-governance)
2. [Approved algorithms and exceptions](#approved-algorithms-and-exceptions)
3. [Crypto agility](#crypto-agility)
4. [Deprecation program](#deprecation-program)
5. [Formal methods workflow](#formal-methods-workflow)
6. [ProVerif and Tamarin concepts](#proverif-and-tamarin-concepts)
7. [Change control and evidence](#change-control-and-evidence)
8. [Legal and export boundaries](#legal-and-export-boundaries)

## Crypto governance

Establish organizational control without blocking delivery:

| Artifact | Owner | Purpose |
|---|---|---|
| **Crypto standards** | Security architecture | Approved algorithms, minimum TLS, key sizes |
| **Crypto review gate** | Cryptographer / security architect | Mandatory for new protocols, PKI changes, custom schemes |
| **Exception register** | GRC + engineering | Time-bound waivers with compensating controls |
| **Inventory** | Platform teams | Where keys live, algorithms in use, PQ exposure |

**Review triggers:** new protocol, custom KDF, change to root CA, new HSM policy, customer crypto addendum, post-incident crypto failure.

## Approved algorithms and exceptions

Maintain a living **approved list** synced with `primitives_and_algorithm_selection.md`:

- Symmetric, hash, signature, KEM, password, KDF columns
- **Sunset date** per deprecated entry
- **FIPS / regional** columns (e.g., EU, federal)

**Exception process:**

1. Business justification and risk owner
2. Compensating controls (network isolation, shortened lifetime, monitoring)
3. Expiry date and remediation ticket
4. Executive or CISO delegate approval for high risk

## Crypto agility

Design systems to **swap algorithms** without rewriting applications:

| Layer | Agility mechanism |
|---|---|
| Protocol | Version field, cipher suite negotiation, extensible TLV |
| Data at rest | **Algorithm ID** in ciphertext header (e.g., `v1-aes256-gcm`) |
| Keys | Key IDs in KMS; support multiple active wrapping keys |
| Certificates | Parallel trust anchors during CA migration |

**Inventory fields:** algorithm, key ID, location, owner, last rotation, PQ sensitivity (HNDL).

Test **rollback** of agility changes in staging before production.

## Deprecation program

| Phase | Actions |
|---|---|
| Discover | Scan configs, code, certs, HSM policies, partner integrations |
| Notify | Owners, timelines, breaking change windows |
| Dual-run | Support old + new during overlap |
| Enforce | Fail closed on deprecated algorithms in prod |
| Verify | Scanners, CI gates, external probes |

**Priority deprecations:** SHA-1 signatures, RSA-1024, TLS 1.0/1.1, weak DH (<2048), RC4/3DES, CBC without MAC discipline.

## Formal methods workflow

When to invest:

- High-impact protocol (auth, payments, key enrollment)
- Prior incidents or subtle race/replay bugs
- Regulatory or customer demand for assurance evidence

**Steps:**

1. Freeze **protocol narrative** and assumptions
2. Build **abstract model** (roles, channels, crypto as equations)
3. State **queries** (secrecy, authentication, equivalence)
4. Run tool; analyze **counterexamples** → fix spec or design
5. Map model elements to **implementation** (gap analysis)
6. Archive model + scripts in version control

**Limitation:** symbolic models ≠ timing, memory, or implementation bugs—pair with code review and testing.

## ProVerif and Tamarin concepts

**ProVerif:**

- Processes, channels, cryptography as **perfect or symbolic**
- Queries: `query attacker(s)` for secrecy; `event()` implications for authentication
- Good for **large protocol** skeletons and standard primitives

**Tamarin:**

- **Multiset rewriting** rules; support for equational theories (Diffie-Hellman)
- Strong for **stateful** protocols, compromise models, complex induction

**Shared vocabulary:**

- **Dolev-Yao** attacker controls network
- **Corruption** queries (reveal long-term key) test forward secrecy
- **Observational equivalence** for privacy (vote, anonymity)

Integrate with `mermaid-to-proverif` and `crypto-protocol-diagram` (agent catalog) for diagram-driven workflows.

## Change control and evidence

For each crypto change, retain:

- Design doc and threat model delta
- Review sign-off (cryptographer + implementer)
- Test results (unit, Wycheproof, TLS scan)
- Config diffs (cipher suites, cert templates)
- Rollback plan

Link to **assurance cases** when `software-assurance-formal-methods-specialist` applies (safety-critical or certified products).

## Legal and export boundaries

- **Do not** provide export classification, deemed export, or sanctions determinations
- Flag designs involving **dual-use** crypto, classified environments, or cross-border key escrow to **legal/compliance**
- Route contract clauses on crypto obligations to `commercial-counsel` (legal review—not legal advice from the agent)

Document **customer contractual** crypto requirements separately from engineering standards.
