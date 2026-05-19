# Authentication Hardening

## Technique Coverage

| D3FEND Technique | Description |
|---|---|
| Agent Authentication | Service-to-service auth |
| Biometric Authentication | Fingerprint, face, etc |
| Certificate-based Authentication | mTLS, client certs |
| Multi-factor Authentication | 2FA/MFA |
| Password Authentication | Password policies |
| Token-based Authentication | JWT, OAuth, session tokens |

## Implementation Guide

### Multi-factor Authentication

| Factor Type | Examples | Strength |
|---|---|---|
| Knowledge | Password, PIN | Low |
| Possession | TOTP app, SMS, hardware key | Medium |
| Inherence | Fingerprint, face, iris | High |
| Context | Location, device, behavior | Medium |

Deployment:
- Enforce MFA for all privileged accounts
- Prefer TOTP/WebAuthn over SMS
- Require hardware keys for admin/root

### Certificate-based Authentication

```
Client → presents client cert → Server verifies against CA
Server → presents server cert → Client verifies (mTLS)
```

- Maintain private CA or use public PKI
- Short certificate lifetimes (90 days)
- Automated rotation
- CRL or OCSP for revocation

### Password Policy

```
Minimum length: 16 characters
Complexity: not required (length > complexity)
Breach check: against HaveIBeenPwned
Rotation: only on compromise, not periodic
Storage: Argon2id, bcrypt, or scrypt
```

### Token Security

| Token Type | Lifetime | Storage |
|---|---|---|
| Access token | 5-15 minutes | Memory |
| Refresh token | 7-30 days | Secure cookie + httpOnly |
| Session cookie | Session + sliding | Secure + SameSite |
