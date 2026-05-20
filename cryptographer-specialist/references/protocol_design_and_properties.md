# Protocol design and security properties

## Table of contents

1. [Security properties glossary](#security-properties-glossary)
2. [Protocol review method](#protocol-review-method)
3. [Handshakes and key derivation](#handshakes-and-key-derivation)
4. [Downgrade and replay](#downgrade-and-replay)
5. [Transcript binding and channel binding](#transcript-binding-and-channel-binding)
6. [Session management](#session-management)
7. [Common protocol patterns](#common-protocol-patterns)
8. [Formal verification fit](#formal-verification-fit)

## Security properties glossary

| Property | Meaning | Typical mechanism |
|---|---|---|
| **Secrecy** (confidentiality) | Adversary cannot learn plaintext | AEAD, forward-secret key agreement |
| **Authentication** | Peer is who they claim | Signatures, MACs, certs, pre-shared keys |
| **Integrity** | Adversary cannot alter undetected | AEAD tag, signatures |
| **Forward secrecy (PFS)** | Past sessions safe if long-term key leaks | Ephemeral DH per session |
| **Agreement** | Both parties derive same keys | Explicit key confirmation, signed transcript |
| **Replay resistance** | Old messages cannot be replayed | Nonces, counters, session IDs, timestamps |
| **Ordering** | Messages processed in intended order | Sequence numbers within session |

Clarify **which property applies to which layer** (transport vs application message).

## Protocol review method

1. **Diagram** participants, messages, and trust boundaries
2. List **cryptographic inputs** per message (keys, nonces, AD, identities)
3. For each message, state what **breaks** if an attacker modifies, drops, or replays it
4. Trace **key derivation tree** from long-term secrets to session keys
5. Check **composition** with TLS (what is protected below vs at app layer)
6. Record **assumptions** (clock sync, trusted CA, secure enrollment)
7. Compare to **known attacks** (MITM, version rollback, key compromise impersonation)

Deliver a **residual risk** table with severity and mitigations.

## Handshakes and key derivation

**Good practice:**

- Use **authenticated key exchange** (signed server params, certs, or mutual auth)
- Derive keys with **HKDF** or protocol-standard KDF (TLS 1.3 key schedule)
- Bind keys to **context**: protocol version, ciphersuite, client/server identities
- Separate keys by **direction** and **purpose** (encrypt vs MAC vs IV generation)

**Anti-patterns:**

- Shared static symmetric key for all clients
- Encrypting under long-term RSA without freshness
- Custom hash chains without analysis
- Ignoring **identity** in KDF input (wrong peer key)

## Downgrade and replay

**Downgrade resistance:**

- Include **version** and **ciphersuite** in signed or MAC'd transcript (TLS 1.3 does via Finished)
- Reject unknown versions explicitly; no silent fallback to weak crypto
- Log and alert on **fallback** events in clients

**Replay:**

- Use **session identifiers** + monotonic counters or sliding windows
- For stateless APIs, **signed timestamps** with short skew + nonce store
- Distinguish **at-least-once delivery** (idempotent handlers) from crypto replay

## Transcript binding and channel binding

**Transcript binding:** signatures or MACs cover the **full negotiation** so MITM cannot splice parameters.

**Channel binding (tls-unique, tls-exporter):**

- Tie application auth to the underlying TLS channel
- Prevents **credential forwarding** to different TLS sessions
- Specify which exporter label and length per RFC 5705 / 8446

Document if application crypto is **independent of TLS** (double encryption) and why.

## Session management

| Topic | Guidance |
|---|---|
| Session ID | Unpredictable, rotated on privilege change |
| Resumption | TLS tickets / session IDs—understand PFS implications of 0-RTT |
| Rekey | After volume limit (bytes) or time; align with AEAD limits |
| Logout | Invalidate server-side session and ticket store |

**TLS 1.3 0-RTT:** replay of early data possible—never use for non-idempotent operations without anti-replay at app layer.

## Common protocol patterns

| Pattern | Notes |
|---|---|
| Signal / Noise | Use established frameworks; specify pattern name (e.g., XX, IK) |
| JWT / JOSE | Prefer **EdDSA/ECDSA**; avoid `none` alg; validate `aud`, `iss`, `exp`; key rotation via JWKS |
| OAuth/OIDC | TLS for transport; validate state/nonce; separate signing keys for ID tokens |
| Custom RPC | mTLS or token + TLS; do not roll custom handshake without review |
| E2E messaging | Double ratchet concepts; clarify device trust and key transparency |

## Formal verification fit

When stakeholders need **machine-checked arguments**:

| Tool | Strength | Typical input |
|---|---|---|
| **ProVerif** | Symbolic; infinite sessions; secrecy/auth | Pi calculus model, queries |
| **Tamarin** | Symbolic; equational theories; state | Multiset rewriting rules |

**Properties to state:** `confidentiality(sk, attacker)`, `event(accept) ==> event(run)`, `executable`

**Scope limits:** models abstract crypto; implementation bugs (timing, memory) need separate review.

Pair with `crypto-protocol-diagram` and `mermaid-to-proverif` (agent catalog) for diagram-to-model workflows.
