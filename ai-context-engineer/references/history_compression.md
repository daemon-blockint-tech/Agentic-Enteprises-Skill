# History compression

## Table of contents

1. [When to summarize](#when-to-summarize)
2. [Summary prompt](#summary-prompt)
3. [Pitfalls](#pitfalls)

## When to summarize

Trigger when history tokens > 40% of budget or message count > 30.

## Summary prompt

Preserve verbatim:

- User goals and constraints
- Decisions made
- Open questions
- Tool errors and IDs
- Numbers, dates, names

Omit: pleasantries, repeated tool retries that succeeded.

## Pitfalls

- Summarizing away safety refusals
- Losing "do not do X" constraints
- Double summarization drift—re-summarize from raw episodic store if available
