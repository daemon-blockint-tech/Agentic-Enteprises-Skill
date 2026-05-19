# Credential & Message Hardening

## Technique Coverage

| D3FEND Technique | Description |
|---|---|
| Credential Hardening | Protect credentials |
| Certificate Pinning | Pin known certs |
| Credential Rotation | Periodic rotation |
| Certificate Rotation | Auto cert renewal |
| Password Rotation | Password changes |
| One-time Password | OTP/TOTP |
| Strong Password Policy | Complexity rules |
| Change Default Password | Eliminate defaults |
| Token Binding | Bind token to device |
| Message Hardening | Protect messages |
| Message Authentication | HMAC/MAC |
| Bus Message Authentication | ICS bus auth |
| Message Encryption | Encrypt in transit |
| Transfer Agent Authentication | Secure transfer |

## Credential Lifecycle

### Rotation Schedule

| Credential Type | Rotation Frequency | Method |
|---|---|---|
| API keys | 90 days | Automated reissue |
| Service accounts | 90 days | Vault rotation |
| Certificates | 1 year max | Auto-renewal |
| Passwords | On suspicion | Forced reset |
| Secrets (DB, etc) | 90 days | Vault dynamic |

### Certificate Pinning

```
Mobile app → embed expected cert hash
If server presents different cert → reject connection
Fallback: allow user override with warning
```

### Message Integrity

| Protection | Mechanism | Use Case |
|---|---|---|
| Authentication | HMAC-SHA256 | API requests |
| Encryption | TLS 1.3 | All network traffic |
| Signing | ECDSA/RSA | Software updates, emails |
| Sealing | Envelope encryption | Data at rest |

### Token Binding

```
Token issued to specific device/browser
Bound via Channel ID or TLS channel
Stolen token cannot be used on different device
```
