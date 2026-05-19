# Object & File Eviction

## Technique Coverage

| D3FEND Technique | Description |
|---|---|
| Object Eviction | Remove malicious objects |
| Disk Formatting | Reformat storage |
| Disk Erasure | Secure wipe |
| Disk Partitioning | Repartition |
| DNS Cache Eviction | Clear DNS cache |
| Domain Registration Takedown | Take down domain |
| File Eviction | Remove malicious files |
| Email Removal | Delete malicious email |
| Registry Key Deletion | Remove persistence |

## File Eviction

### Quarantine vs Delete

| Action | When | Risk |
|---|---|---|
| Quarantine | Need forensics | Attacker may recover |
| Delete | Confirmed malicious | Evidence loss |
| Replace | Known good backup | Restore integrity |

### Registry Cleanup

```
Common persistence locations:
HKLM\Software\Microsoft\Windows\CurrentVersion\Run
HKCU\Software\Microsoft\Windows\CurrentVersion\Run
Services (legitimate names, malicious binaries)
WMI event subscriptions
Scheduled tasks
```

### Email Removal

- Delete from all mailboxes
- Purge from recoverable items
- Block sender domain
- Update email gateway rules

### DNS & Domain

| Action | Method |
|---|---|
| DNS cache eviction | `ipconfig /flushdns`, restart resolver |
| Domain takedown | Contact registrar/hosting provider |
| Sinkhole | Redirect to internal block page |

### Disk Operations

| Method | Use Case | Standard |
|---|---|---|
| Format | Quick rebuild | NIST 800-88 |
| Secure erase | Sensitive data | DoD 5220.22-M |
| Degauss | Magnetic media | Physical destruction |
| Crypto erase | Self-encrypting drives | TCG Opal |
