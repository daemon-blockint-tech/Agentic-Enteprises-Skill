---
name: web-application-developer
description: |
  Guides web application development—browser-based products spanning UI, HTTP APIs, sessions and
  cookies, routing (SPA and SSR), forms, file uploads, and web-specific security (CSRF, CORS, CSP,
  XSS prevention) on stacks such as React/Next.js, Vue, or similar with Node/Python/Ruby backends.
  Use when building or maintaining a web app, implementing login flows, server-rendered or hybrid
  pages, REST/GraphQL consumption, or debugging browser–server issues—not for mobile native apps,
  CLI tools, or data pipelines. For generic full-stack feature delivery use fullstack-software-engineer;
  for front-end-only work use senior-frontend-software-engineer; for deploy/CI use devops.
  For design-to-code UI implementation (tokens, states, Storybook) without auth/CORS focus, use
  ui-software-engineer.
---

# Web Application Developer

## When to Use

- Build or extend a browser-based web application (not native mobile)
- Implement auth flows, sessions, or token handling in a web context
- Connect UI to HTTP APIs with correct error and loading handling
- Address CORS, cookies, CSRF, or caching behavior between browser and server
- Ship SSR, SPA, or hybrid (e.g., Next.js) routing and data loading

## When NOT to Use

- Native iOS/Android or desktop-only clients → stack-specific mobile/desktop guidance
- Pure infrastructure or pipelines → `devops`, `infrastructure-engineer`
- UX discovery and wireframes only → `product-designer`
- Org-wide security program → `cybersecurity`
- Senior cross-service RFCs → `senior-software-engineer`

## Related skills

| Need | Skill |
|---|---|
| Full-stack IC features (general) | `fullstack-software-engineer` |
| Senior full-stack delivery | `senior-fullstack-developer` |
| Front-end architecture only | `senior-frontend-software-engineer` |
| UI screens from design specs | `ui-software-engineer` |
| UX specs and flows | `product-designer` |
| Pipeline and hosting | `devops` |
| Pipeline security scans | `devsecops` |

## Core Workflows

### 1. Web app structure

Choose rendering model explicitly:

| Model | When |
|---|---|
| SSR / hybrid | SEO, fast first paint, authenticated dashboards |
| SPA | Heavy client interactivity, app behind login |
| Static + API | Marketing site + separate app subdomain |

Document: routes, auth gates, global layout, error boundaries.

**See `references/web_app_architecture.md` for routing and env patterns.**

### 2. HTTP API integration

- Use typed client or OpenAPI-generated types
- Handle 401 → refresh or redirect to login
- Timeouts and retry only for idempotent GETs
- Paginate list endpoints; avoid loading unbounded data in browser

**See `references/api_integration.md` for client patterns.**

### 3. Auth in the browser

- Prefer HttpOnly, Secure, SameSite cookies for session cookies
- Or short-lived access token in memory + refresh rotation
- Never store secrets in localStorage for high-risk apps
- Protect state-changing routes with CSRF tokens when using cookies

**See `references/auth_sessions.md` for flow diagrams.**

### 4. Forms and uploads

- Client validation for UX; server validation required
- `multipart/form-data` for files; progress and size limits
- Sanitize filenames; scan server-side if policy requires

### 5. Web security baseline

- Escape output; avoid `dangerouslySetInnerHTML` without sanitizer
- Set CSP headers; restrict script sources
- CORS allowlist explicit origins—not `*` with credentials
- Security headers: HSTS, X-Frame-Options or frame-ancestors

**See `references/web_security.md` for checklist.**

### 6. Test and release

- Unit: validators, hooks, API mappers
- Integration: API routes with test DB
- E2E: login and one critical journey (Playwright/Cypress)
- Smoke test after deploy on staging URL

**See `references/web_app_architecture.md` for env and config.**

## When to load references

- **Architecture and env** → `references/web_app_architecture.md`
- **API clients** → `references/api_integration.md`
- **Login and sessions** → `references/auth_sessions.md`
- **CSRF, CSP, CORS** → `references/web_security.md`
