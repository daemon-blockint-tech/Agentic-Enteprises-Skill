# Context, tokenization, and long-context

## Table of contents

1. [Tokenization effects](#tokenization-effects)
2. [Context assembly](#context-assembly)
3. [Long-context phenomena](#long-context-phenomena)
4. [Study designs](#study-designs)

## Tokenization effects

Research angles:

- **Cross-model token inflation** — same Unicode, different token counts
- **Delimiter and markup** — JSON vs XML vs markdown overhead
- **Code vs prose** — compression ratios by language
- **Rare characters and emoji** — fragmentation spikes
- **Tool schema size** — function-calling token tax

Report **bytes → tokens** curves for representative corpora.

## Context assembly

Decompose input budget:

| Block | Typical share | Research lever |
|---|---|---|
| System prompt | Fixed | Shorter policy variants |
| Tool definitions | Fixed per turn | Tool pruning, lazy tools |
| Retrieved chunks | Variable | k, chunk size, rerank |
| Chat history | Growing | compaction, window |
| User message | Variable | clarification cost |

Measure **marginal value** — ablate one block at a time.

## Long-context phenomena

Standard probes (adapt to product domain):

- **Needle-in-haystack** — fact at depth d
- **Multi-hop** — requires two distant facts
- **Lost in the middle** — U-shaped accuracy vs position
- **Instruction at top vs bottom** — constraint following

Plot accuracy vs **insertion depth** and vs **total tokens**.

## Study designs

- Fixed total window; sweep needle depth
- Fixed task; sweep window size with constant density
- Compare **yarn/extended** models only with matched eval — avoid conflating model upgrade with context strategy

Link findings to `ai-context-engineer` implementation choices, not as production spec by themselves.
