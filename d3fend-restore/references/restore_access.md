# Restore Access

## Technique Coverage

| D3FEND Technique | Description |
|---|---|
| Restore Access | General access recovery |
| Reissue Credential | New credentials |
| Restore Network Access | Re-enable network |
| Restore User Account Access | Restore account |
| Unlock Account | Enable locked account |

## Access Restoration

### Credential Reissuance

```
Verify identity: Out-of-band confirmation
Generate new: Strong random, appropriate type
Distribute securely: Password manager, secure email
Monitor: Watch for use of old credentials
Notify: User and security team
```

### Account Unlock

| Step | Action |
|---|---|
| 1 | Verify compromise contained |
| 2 | Confirm user identity |
| 3 | Reset password + MFA |
| 4 | Review account permissions |
| 5 | Re-enable account |
| 6 | Monitor for 48 hours |

### Network Access Restoration

- Remove firewall blocks (if temporary)
- Re-enable VPN access
- Verify no persistence remains
- Confirm clean security scan
- Document restoration in incident timeline

## Validation Before Restore

- [ ] Threat fully contained
- [ ] No persistent access remains
- [ ] User identity verified
- [ ] New credentials issued
- [ ] Systems scanned clean
- [ ] Monitoring in place
