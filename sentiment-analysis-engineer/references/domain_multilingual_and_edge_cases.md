# Domain, multilingual, and edge cases

## Table of contents

1. [Domain adaptation](#domain-adaptation)
2. [Multilingual strategies](#multilingual-strategies)
3. [Sarcasm and negation](#sarcasm-and-negation)
4. [Bias and fairness](#bias-and-fairness)
5. [Entity-level sentiment](#entity-level-sentiment)

## Domain adaptation

| Domain | Challenges | Mitigations |
|---|---|---|
| Product reviews | Long text, aspects, rating skew | ABSA, align stars vs text slice |
| Social media | Slang, hashtags, short text | Emoji rules, character models, dedupe |
| Support tickets | PII, procedural tone | Redact entities; separate urgency vs sentiment |
| News | Neutral wire copy, multiple entities | Target-aware models; headline vs body |
| Finance | Market vs opinion, tickers | Entity linking; domain lexicon; disclaimers |

Techniques: **in-domain fine-tune**, **continued pretrain** on unlabeled domain corpus, **adapter layers**, **self-training** with confidence filtering (audit high-impact paths).

Always evaluate on **in-domain test**; cross-domain F1 is optimistic for deployment.

## Multilingual strategies

| Strategy | Pros | Cons |
|---|---|---|
| Translate-then-analyze | One English model | Translation errors, idiom loss |
| Multilingual encoder (XLM-R) | Single pipeline | Weaker on low-resource pairs |
| Per-language models | Best per locale | Ops overhead, routing |
| Language ID + route | Right tool per lang | Mis-ID errors |

For **code-switching**: train on mixed examples; evaluate dedicated code-switch slice; avoid translating away language signal.

Document **primary languages**, **script**, and **locale** (en-US vs en-GB) in model card.

## Sarcasm and negation

- Sarcasm: often needs **context** (thread, user history); document-level models beat bag-of-words
- Negation: dependency-aware features, NLI-style models, or LLM with explicit negation examples in prompt
- Do not rely on lexicon **antonym flip** alone ("not good" ≠ "good")
- Report **sarcasm slice** separately; do not merge into generic "hard examples"

## Bias and fairness

- Audit slices by **demographic proxies** only when ethical and legal review allows
- Check **dialect and identity terms** for systematic score shifts
- Avoid using sentiment for **high-stakes** decisions without policy and human review
- Log **disparate impact** on routing rates if scores trigger workflows

Partner with governance when scores affect customers or employees.

## Entity-level sentiment

- **Target extraction** then polarity (pipeline) vs joint ABSA models
- Finance: link **ticker/company** mentions; disambiguate homographs
- News: coreference and headline-body alignment
- Evaluate **target F1** and **polarity F1** separately

When entities are ambiguous, prefer **abstain** or human review over forced labels.
