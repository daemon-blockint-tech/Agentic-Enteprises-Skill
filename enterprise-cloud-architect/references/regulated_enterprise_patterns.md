# Regulated enterprise patterns

## Table of contents

1. [Data classification](#data-classification)
2. [Residency and sovereign](#residency-and-sovereign)
3. [Control patterns](#control-patterns)
4. [Audit and evidence](#audit-and-evidence)

## Data classification

Map workloads to tiers (example):

| Tier | Cloud placement | Examples |
|---|---|---|
| Public | Standard regions | Marketing sites |
| Internal | Private networking, standard logging | Internal apps |
| Confidential | Restricted regions, CMK, enhanced logging | HR, finance |
| Regulated | Sovereign or approved regions, dedicated controls | PHI, certain financial |

**Architecture** selects region, encryption, and connectivity; **legal/compliance** confirms adequacy.

## Residency and sovereign

Decisions:

- In-region processing and storage
- **Sovereign cloud** or dedicated regions when required
- Cross-border replication prohibited or encrypted with approval
- Subprocessor list for SaaS components

Do not provide legal opinions — flag for compliance and counsel.

## Control patterns

| Control area | Pattern |
|---|---|
| Encryption | CMK per tier; key hierarchy and rotation |
| Network | No public endpoints; PrivateLink; egress allowlist |
| Identity | SSO federation; no local IAM users; PIM for admin |
| Logging | Immutable central store; retention per tier |
| Backup | Encrypted, cross-region only if permitted |
| AI/LLM | No training on customer data; private endpoints — `applied-ai-architect-commercial-enterprise` |

## Audit and evidence

Architecture delivers:

- **Control mapping** — which cloud config satisfies which control intent
- **Diagrams** — data flows for assessors
- **Config baselines** — policy-as-code references

Evidence collection automation → `compliance-engineer`.

Security sign-off → `information-security-engineer`.
