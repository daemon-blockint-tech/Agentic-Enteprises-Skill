# Frontend patterns

## Table of contents

1. [Next.js App Router](#nextjs-app-router)
2. [Forms](#forms)
3. [Performance](#performance)

## Next.js App Router

- Fetch on server by default; pass serializable props to client components
- Use `loading.tsx` and `error.tsx` boundaries
- Cache with explicit `revalidate` strategy

## Forms

- Validate on client for UX; always validate on server
- Optimistic UI only when rollback is cheap

## Performance

- Measure LCP, INP; lazy-load below-fold
- Avoid waterfall client fetches; batch where possible
