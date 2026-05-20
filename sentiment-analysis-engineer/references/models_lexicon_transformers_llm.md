# Models: lexicon, transformers, and LLMs

## Table of contents

1. [Approach ladder](#approach-ladder)
2. [Lexicon and rules](#lexicon-and-rules)
3. [Classical and neural encoders](#classical-and-neural-encoders)
4. [Fine-tuning transformers](#fine-tuning-transformers)
5. [LLM prompt classification](#llm-prompt-classification)
6. [Selection heuristics](#selection-heuristics)

## Approach ladder

Always establish baselines in order:

1. **Lexicon + rules** — fast, interpretable, domain lexicons
2. **Classical ML** — TF-IDF + linear models on labeled data
3. **Fine-tuned encoder** — DistilBERT/RoBERTa/XLM-R for accuracy and latency balance
4. **LLM prompts** — few-shot or structured output when labels are fluid or low data

Document **cost, latency, and maintainability** at each step; stop when acceptance metrics are met.

## Lexicon and rules

- Use domain lexicons (product, finance) plus negation handling (not, never, without)
- Combine **VADER-style** heuristics with custom intensifiers and emoticons
- Rules excel for **compliance keywords**, **banned phrases**, and **bootstrap labels**
- Weakness: sarcasm, domain shift, multilingual code-switching

## Classical and neural encoders

- TF-IDF + logistic regression / linear SVM: strong baseline on ≥1k labeled docs
- Character n-grams help short social text
- FastText-style embeddings for multilingual baselines with modest data

## Fine-tuning transformers

- Prefer **encoder-only** models for classification and token-level ABSA heads
- Use class weights or focal loss for **imbalanced** negative/neutral skew
- Early stopping on **macro-F1** on dev; avoid optimizing accuracy alone
- Export ONNX/TorchScript when latency matters; quantize after accuracy check

Hyperparameters (starting points): lr 2e-5–5e-5, batch 16–32, 2–4 epochs with early stop.

## LLM prompt classification

- Fixed **JSON schema** outputs: `{"polarity":"positive","confidence":0.82}`
- Few-shot examples from adjudicated gold; keep prompts versioned
- Use for **label schema changes**, **long-tail aspects**, or **<500 labels**
- Mitigate: temperature 0, self-consistency only for research, cache by hash
- Cost and latency usually exceed encoders at scale — reserve for tier-2 or audit

## Selection heuristics

| Signal | Favor |
|---|---|
| <500 labeled examples | Lexicon + LLM few-shot; data collection first |
| 1k–100k labels, stable schema | Fine-tuned encoder |
| Strict latency (<50ms p99) | Small encoder or linear + embeddings |
| Multilingual, one model | XLM-R, mBERT, or language-specific heads |
| Open-vocabulary aspects | ABSA span models or LLM extraction + validation |
| Frequent schema churn | LLM prompts with eval regression suite |

Pair with `ai-engineer` when sentiment is one tool inside a larger agent; own the **classification eval and labels** here.
