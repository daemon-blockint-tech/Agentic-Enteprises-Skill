# Auth and sessions

## Table of contents

1. [Cookie session flow](#cookie-session-flow)
2. [Token flow](#token-flow)

## Cookie session flow

```
login POST → server sets HttpOnly session cookie → subsequent requests include cookie → logout clears cookie
```

- `SameSite=Lax` (or `Strict` if no cross-site needs)
- `Secure` in production
- CSRF token on POST/PUT/PATCH/DELETE when using cookies

## Token flow

```
login → access token (short TTL) + refresh token (HttpOnly cookie or rotation endpoint)
```

- Store access token in memory, not localStorage, when XSS risk is material
- Refresh before expiry; single-flight refresh to avoid storms
