# Retrieval packing

## Table of contents

1. [Deduplication](#deduplication)
2. [Ordering](#ordering)
3. [Citations](#citations)

## Deduplication

Merge chunks with >85% overlap; keep highest score passage.

## Ordering

Sort by relevance score descending; group by source document for readability.

## Citations

Each chunk: `[doc_id:chunk_id]` in header line.

Instruct: answer only from cited chunks; say insufficient context otherwise.
