# Watermarks, provenance, and C2PA

## Purpose

Explain how to **interpret** visible watermarks, embedded marks, and **C2PA (Content Credentials)** manifests during markup detection—not how to design cryptographic watermark schemes.

## Table of contents

1. [Visible and forensic watermarks](#visible-and-forensic-watermarks)
2. [C2PA content credentials](#c2pa-content-credentials)
3. [Verification workflow](#verification-workflow)
4. [Publisher and platform claims](#publisher-and-platform-claims)
5. [Limits and attacks](#limits-and-attacks)
6. [Routing to cryptographer specialist](#routing-to-cryptographer-specialist)

## Visible and forensic watermarks

| Type | What it shows | Limits |
|---|---|---|
| **Visible logo/text** | Brand or “AI generated” label | Easy to crop; can be faked visually |
| **Steganographic / fragile** | Survives some edits; may break on re-encode | Requires proprietary detectors; not universal |
| **Broadcast watermark** | TV/streaming trace codes | Specialist decode; not in consumer files |

- Record **whether watermark is present**, **location**, and **whether cropped**
- Distinguish **platform overlay** (TikTok handle) from **creator watermark**
- Absence of watermark **does not prove** authenticity

## C2PA content credentials

**C2PA** embeds a signed manifest chain describing actions on content (capture, edit, publish).

Common manifest elements:

- **Claim generator** — software that produced the manifest
- **Actions** — `c2pa.created`, `c2pa.edited`, `c2pa.placed`, etc.
- **Ingredients** — parent assets when compositing
- **Signature** — credential bound to issuer (camera app, Adobe, etc.)

### What strong verification implies

- Manifest **signature validates** against trusted roots configured in verifier
- **Ingredient chain** is internally consistent
- **Timestamps** align with other evidence (weak alone)

### What it does not imply

- **Moral truth** of depicted events—only **processing history** attested by signer
- **Impossibility of fake**—attackers can strip manifests or attach fake ones if verifiers are naive

## Verification workflow

1. Use a **C2PA-aware viewer** or CLI (project tooling evolves—cite tool name and version in report)
2. Capture **manifest JSON** or export for evidence annex
3. Record **validation result**: valid / invalid / absent / partial
4. Map **issuer** to expected publisher (news org camera app vs unknown generator)
5. If manifest says **edited**, list claimed edits; compare to user dispute
6. Cross-link **visual** and **metadata** references when manifest claims `created` but EXIF is empty

## Publisher and platform claims

- **Newsroom** “original” badges — verify crypto where offered; otherwise organizational trust only
- **Stock sites** — license metadata ≠ capture provenance
- **Social platforms** — “labeled as altered” policies vary; screenshot labels are not C2PA
- **Blockchain NFT** pointers — do not prove image authenticity; route on-chain questions to blockint skills

## Limits and attacks

| Risk | Handling |
|---|---|
| **Strip** manifest on re-save | Report absence; do not infer innocence |
| **Fake manifest** with self-signed cert | Check trust store; invalid signature = red flag |
| **Partial manifest** | Document what is unsigned |
| **Screenshot of credentialed image** | Credentials usually lost—state limitation |
| **AI tool** emitting credentials for synthetic | Manifest truthfully reports synthetic creation—still not “camera proof” |

## Routing to cryptographer specialist

Route to `cryptographer-specialist` when the user needs:

- **Design** of watermarking, perceptual hashing at scale, or custom signing hierarchies
- **Protocol review** for content-auth APIs, key rotation, or cross-org trust fabrics
- **Threat modeling** of steganographic channels

This skill **reads** credentials; it does not **architect** them.
