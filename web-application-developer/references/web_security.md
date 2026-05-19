# Web security

## Table of contents

1. [Checklist](#checklist)
2. [CORS](#cors)

## Checklist

- [ ] No secrets in client bundle
- [ ] CSP configured for scripts and styles
- [ ] Cookies: HttpOnly + Secure + SameSite
- [ ] CSRF protection on cookie-based mutations
- [ ] Input validated server-side
- [ ] Output encoded in HTML contexts
- [ ] File upload type and size limits
- [ ] Dependencies scanned (link `devsecops`)

## CORS

- Allow specific origins only
- `credentials: true` only with explicit origin—not wildcard
- Preflight handled for non-simple methods
