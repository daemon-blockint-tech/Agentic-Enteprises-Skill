# Restore Software & Systems

## System Rebuild Process

### From Gold Image

```
1. Select verified, hardened gold image
2. Verify image signature and integrity
3. Deploy to clean infrastructure
4. Join domain / configure identity
5. Apply latest OS and app patches
6. Install required software from approved sources
7. Restore data from clean backup
8. Run security scan (vulnerability + malware)
9. Verify functionality
10. Document and re-authorize for production
```

### Software Reinstallation

| Step | Action | Verification |
|---|---|---|
| Source | Approved repository only | Signature check |
| Version | Latest stable | CVE check |
| Config | Apply hardened baseline | Policy compliance |
| Dependencies | Review and update | SBOM comparison |

## Rejoining Production

### Pre-return Checklist

- [ ] Malware scan: Clean
- [ ] Vulnerability scan: Acceptable risk
- [ ] Configuration: Matches hardened baseline
- [ ] Patching: Current as of rejoin date
- [ ] Monitoring: Agent installed and reporting
- [ ] Logging: Forwarding to SIEM
- [ ] Backup: New backup taken post-restore
- [ ] Documentation: Recovery actions logged

### Phased Return

```
Phase 1: Isolated test environment
Phase 2: Limited user pilot
Phase 3: Full production access
Phase 4: Remove temporary restrictions
```

## Lessons Learned

Document after every restoration:
- Root cause of compromise
- Time to detect, contain, and restore
- What worked well
- What needs improvement
- Updates to playbooks and procedures
