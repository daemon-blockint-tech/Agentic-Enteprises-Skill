# State and data fetching

## Table of contents

1. [Waterfalls](#waterfalls)
2. [Mutations](#mutations)
3. [Cache invalidation](#cache-invalidation)

## Waterfalls

Bad: layout fetches → page fetches → child fetches serially on client.

Better: parallel `Promise.all` on server; pass data as props; or single query with includes.

## Mutations

- Prefer Server Actions for simple forms on Next.js
- Use API route + client mutation when complex client logic required
- Optimistic updates: snapshot previous state; rollback on error

## Cache invalidation

After mutation:

- Invalidate query keys affected
- Or `revalidatePath` / `revalidateTag` for RSC caches
- Document which paths must refresh
