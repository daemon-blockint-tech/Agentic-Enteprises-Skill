# Synthetic media and deepfakes

## Purpose

Support **workflow-level triage** of suspected AI-generated or face-swapped content without training detectors or claiming laboratory certainty.

## Table of contents

1. [Categories of synthetic media](#categories-of-synthetic-media)
2. [Face-swap and lip-sync indicators](#face-swap-and-lip-sync-indicators)
3. [Full synthetic imagery](#full-synthetic-imagery)
4. [Audio and voice cloning](#audio-and-voice-cloning)
5. [Multimodal LLM outputs](#multimodal-llm-outputs)
6. [Detection limitations](#detection-limitations)
7. [Escalation paths](#escalation-paths)

## Categories of synthetic media

| Category | Description | Typical user claim |
|---|---|---|
| **Face swap** | One person’s face on another’s body | “This video isn’t them” |
| **Lip sync / puppet** | Driving mouth from separate audio | “Words don’t match mouth” |
| **Text-to-image** | Fully generated still | “This photo never happened” |
| **Enhancement** | Legitimate edit vs synthetic inpaint | “Filter” vs “fake scene” |
| **Voice clone** | TTS or VC on real or fake video | “They never said that” |

## Face-swap and lip-sync indicators

- **Face boundary artifacts** — jawline shimmer, hair-edge halos, skin tone seam at cheeks
- **Eye behavior** — irregular blinks, lack of micro-saccades, mismatched gaze on turns
- **Teeth and mouth** — blurred interior, inconsistent tooth count frame-to-frame
- **Head pose vs torso** — neck stiffness, misaligned jaw when body rotates
- **Temporal consistency** — face box jitter, resolution change localized to face crop
- **Lighting on face** vs **lighting on scene** — inconsistent specular on nose vs environment

## Full synthetic imagery

- **Anatomical errors** — hands, ears, text in scene, jewelry symmetry (common in generative stills)
- **Background logic** — incoherent signage text, impossible reflections
- **Metadata** — absent camera EXIF; `Software` tags naming generative tools (when not stripped)
- **Noise uniformity** — synthetic images sometimes lack sensor noise model of claimed camera
- **Semantic impossibilities** — shadows inconsistent with multiple objects (overlap with visual tampering reference)

## Audio and voice cloning

- **Spectral flatness** or **metallic** timbre in cloned speech
- **Breath and mouth sounds** missing or misaligned with video
- **Background room tone** discontinuities at splice points
- **Phoneme timing** — rushed consonants or uniform vowel length unnatural for speaker
- Route **deepfake audio-only** claims to specialist tools; note this skill does not certify voice identity

## Multimodal LLM outputs

- When asset is **chat-exported image** from an LLM:
  - Document **provenance** (prompt, model version, policy filters)
  - Do not treat as camera capture; label **synthetic by construction**
- For **documents** mixing human and model text, use document integrity reference for revision markup
- **AI red team** skill applies to **testing apps**, not adjudicating a single disputed JPEG

## Detection limitations

- **No universal detector** — scores vary by generator version and compression
- **Adversarial recompression** on social platforms degrades both real and fake signals
- **Benign filters** trigger many face-boundary heuristics
- **P deepfakes** in adult content contexts — handle under policy; avoid redistribution
- **Scientific consensus** — report **suspicion tier**, not “100% fake” without lab consensus

## Escalation paths

| Situation | Suggested next step |
|---|---|
| High-stakes legal or HR | Specialist media forensics vendor; preserve originals |
| Ongoing harassment campaign | Safety / legal per org policy |
| Internal security incident | IR with `information-security-engineer`; evidence preservation |
| Product trust & safety | `ai-risk-governance` for policy; detector R&D to `ml-research-engineer-safeguards` |
| Press or public disinformation | Comms + verified primary sources; avoid overclaiming in public statements |

## Triage checklist

1. Classify **synthetic type** (swap, lip-sync, full gen, audio-only)
2. List **observable indicators** with timestamps for video
3. Note **platform** and **generation count** (re-uploads)
4. Assign confidence; default **Low** if only social-quality copy exists
5. Recommend **original acquisition** or **lab analysis** before irreversible actions
