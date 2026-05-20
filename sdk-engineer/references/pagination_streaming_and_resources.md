# Pagination, Streaming, and Resources

## Pagination goals

- Hide cursor/page token mechanics behind **iterators**
- Fetch next page lazily (do not buffer entire dataset by default)
- Preserve server ordering guarantees documented in API reference
- Surface `has_more` / empty page without throwing

## REST pagination patterns

| Pattern | Wire signals | Client shape |
|---|---|---|
| Offset/limit | `offset`, `limit`, `total` | `for page in paginator: ...` with guard on max offset |
| Cursor | `starting_after`, `ending_before`, `next_cursor` | `iter_all()` yielding items |
| Link header | RFC 5988 `Link: rel="next"` | follow `next` URL until absent |
| Page number | `page`, `per_page` | explicit `next_page()` |

### Iterator API (language-agnostic)

```text
pager = client.items.list(limit=100, filters={...})
for item in pager:        # auto-fetches pages
    process(item)

# or manual
while pager.has_next():
    page = pager.next_page()
```

### Parameters

- Pass through filter/query params on first request only unless API requires repeat
- Allow `max_items` safety cap for runaway jobs
- Document default page size and server max `limit`

## GraphQL pagination

- **Relay cursors**: `first`/`after`, `pageInfo.hasNextPage`, `endCursor`
- Combine with operation-specific filters
- Avoid N+1: use batch fields or dataloaders in **app** code; SDK provides cursor helper only

## gRPC streaming

| Mode | Use case | Client responsibility |
|---|---|---|
| Server streaming | Large result sets | iterate messages; handle `EOF` |
| Client streaming | bulk upload | backpressure, chunk size |
| Bidirectional | live feeds | cancel on shutdown |

Set deadlines per stream; document heartbeat/ping if server requires keepalive.

## HTTP streaming (non-gRPC)

- **SSE**: parse `event:` blocks; reconnect policy documented if API supports `Last-Event-ID`
- **Chunked JSON lines**: NDJSON parsers with buffer limits
- **File download**: stream to disk; expose progress callback optional

## Resource lifecycle helpers

Some APIs combine pagination with sub-resources:

```text
customer = client.customers.retrieve("cus_123")
for invoice in customer.invoices.list():  # nested paginator
    ...
```

Prefer flat `client.invoices.list(customer_id=...)` unless nesting is idiomatic in target language.

## Partial responses and field selection

- Support `fields`, `expand`, `include` query params when spec defines them
- Type expanded relations as optional nested objects
- Document extra round-trips when expansion unavailable

## Uploads and downloads

- Multipart upload: expose stage helpers (init, parts, complete) matching API
- Resumable uploads: persist upload id client-side
- Downloads: stream with checksum validation when server provides digest

## Memory and performance

- Default: **O(page size)** memory per iteration
- Opt-in `collect_all()` with loud warning in docs
- Parallel page prefetch: advanced; off by default to avoid rate limits

## Error handling mid-sequence

- If page 3 fails mid-iteration: raise with cursor position in error metadata when possible
- Document whether iteration is resumable from last cursor
- Do not silently skip failed pages

## Testing pagination

- Fixture files: 2–3 pages with different cursors
- Assert single HTTP call per `next_page()` when cache disabled
- Assert stop when empty or `has_more=false`
- Property test: union of all pages equals known fixture set (test harness)

## Documentation examples

Every list operation in README should show **one** iterator example:

```python
for item in client.resources.list(status="active"):
    print(item.id)
```

Avoid only showing low-level `GET /v1/resources?page=2` unless demonstrating escape hatch.
