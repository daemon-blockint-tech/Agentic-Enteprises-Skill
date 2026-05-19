# Attack catalog

## Table of contents

1. [Prompt injection](#prompt-injection)
2. [Jailbreak families](#jailbreak-families)
3. [RAG attacks](#rag-attacks)
4. [Ethics](#ethics)

## Prompt injection

- Direct: user overrides system in same turn
- Indirect: malicious content in retrieved doc or email parsed by agent
- Payload in metadata fields (titles, alt text)

## Jailbreak families

- Role-play and fictional framing
- Encoding (base64, other languages)
- Multi-turn gradual compliance
- Refusal suppression ("ignore previous")

Test only on authorized systems; do not publish working exploits against third parties without permission.

## RAG attacks

- Plant document in index with hidden instructions
- Poison chunk boundaries to split defenses

## Ethics

Authorized testing only; minimize harm; redact PII in reports.
