# Credential Eviction

## Technique Coverage

| D3FEND Technique | Description |
|---|---|
| Credential Eviction | Remove compromised credentials |
| Account Locking | Disable account access |
| Authentication Cache Invalidation | Clear auth caches |
| Credential Revocation | Revoke certificates/tokens |

## Eviction Procedures

### Account Locking

```
Trigger: Confirmed compromise or suspicious activity
Action: Disable account in AD/IdP
Notification: User + security team
Unlock: After verification + credential reset
Consideration: May disrupt business - plan for emergency access
```

### Authentication Cache Invalidation

| System | Method |
|---|---|
| Active Directory | Clear Kerberos tickets (klist purge) |
| OAuth/OIDC | Revoke refresh tokens |
| SAML | Force re-authentication |
| API Keys | Rotate or revoke in key vault |
| Cached Credentials | Clear local credential cache |

### Credential Revocation

| Type | Revocation Method |
|---|---|
| Certificates | Publish to CRL, OCSP |
| API Keys | Disable in key management |
| Tokens | Blacklist or rotate signing key |
| Passwords | Force reset on next login |
| Service Accounts | Rotate via secret vault |

## Coordination Checklist

- [ ] Identify all systems using the credential
- [ ] Revoke/rotate in identity provider first
- [ ] Clear all cached sessions
- [ ] Verify no active sessions remain
- [ ] Issue new credentials through secure channel
- [ ] Monitor for attempts to use old credentials
