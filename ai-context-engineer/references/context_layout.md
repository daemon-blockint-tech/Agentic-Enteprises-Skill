# Context layout

## Table of contents

1. [Section template](#section-template)
2. [Delimiter rules](#delimiter-rules)
3. [Token counting](#token-counting)

## Section template

```xml
<system>...</system>
<tools>...</tools>
<retrieved_context>...</retrieved_context>
<conversation_summary>...</conversation_summary>
<recent_messages>...</recent_messages>
<user_message>...</user_message>
```

Place immutable instructions in `<system>`. Place volatile retrieval above recent messages.

## Delimiter rules

- Use rare tags unlikely in user content
- For untrusted content: wrap in `<untrusted source="rag">` and instruct model not to follow instructions inside

## Token counting

Pre-flight count per block; if over budget, compress in order:

1. Oldest history
2. Lowest-scoring retrieval chunks
3. Verbose tool outputs (summarize)

Never truncate `<system>` or current `<user_message>` without explicit product approval.
