# Access Mediation

## Technique Coverage

| D3FEND Technique | Description |
|---|---|
| Access Mediation | General access control |
| Credential Transmission Scoping | Limit credential flow |
| IO Port Restriction | Hardware port control |
| Network Access Mediation | Network access control |
| LAN Access Mediation | LAN segmentation |
| Routing Access Mediation | Routing control |
| Network Resource Access Mediation | Resource access |
| Remote File Access Mediation | Remote file control |
| Web Session Access Mediation | Web session control |
| Endpoint-based Web Server Access Mediation | Endpoint mediation |
| Proxy-based Web Server Access Mediation | Proxy mediation |
| Operating Mode Restriction | Mode-based access |
| OT Variable Access Restriction | OT/ICS access |
| Physical Access Mediation | Physical access |
| Physical Locking | Physical locks |
| System Call Filtering | Syscall filtering |
| Local File Access Mediation | Local file control |
| Access Policy Administration | Policy management |
| Domain Trust Policy | Trust boundaries |
| Local File Permissions | File ACLs |
| User Account Permissions | User ACLs |
| User Group Permissions | Group ACLs |

## Implementation

### Network Access Control

```
802.1X: Port-based auth (device + user)
NAC: Posture checking before access
Zero Trust: Verify every request, assume breach
```

### System Call Filtering

```
Linux: seccomp, seccomp-bpf
Containers: Docker default seccomp profile
Custom: Allowlist only required syscalls
```

### Access Policy Administration

| Element | Best Practice |
|---|---|
| Least privilege | Minimum required access |
| Separation of duties | No single point of control |
| Regular review | Quarterly access recertification |
| Emergency access | Break-glass with audit |
| Role-based | RBAC/ABAC models |

### Physical Controls

| Control | Implementation |
|---|---|
| Electronic locks | Badge + PIN |
| Mantraps | One person at a time |
| Biometric | Fingerprint + badge |
| Visitor escort | Signed in, escorted, logged |
