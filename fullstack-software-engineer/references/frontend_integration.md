# Frontend integration

## Table of contents

1. [Data fetching](#data-fetching)
2. [Forms](#forms)
3. [Performance](#performance)

## Data fetching

- Server Components: fetch on server for read-heavy pages (Next.js)
- Client: `useQuery` or equivalent with stale-time for interactive views
- Invalidate cache after mutations

## Forms

- Client validation for UX; server validation for security
- Disable submit while pending; show field-level errors
- Optimistic UI only when rollback is trivial

## Performance

- Code-split large routes
- Optimize images; avoid layout shift
- Debounce search inputs
