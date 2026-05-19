# Execution Isolation

## Technique Coverage

| D3FEND Technique | Description |
|---|---|
| Execution Isolation | General isolation |
| Application-based Process Isolation | App containers |
| Executable Allowlisting | Permit known good |
| Executable Denylisting | Block known bad |
| Hardware-based Process Isolation | TEE, SGX |
| Kernel-based Process Isolation | Namespaces, seccomp |

## Isolation Methods

### Application-based

```
Containers: Docker, containerd
Sandbox: Chrome sandbox, Firejail
App containers: Windows AppContainer
```

### Kernel-based

| Mechanism | What It Does |
|---|---|
| Namespaces | Isolate PID, net, mount, IPC, UTS, user, cgroup |
| cgroups | Limit CPU, memory, I/O |
| seccomp | Filter syscalls |
| Capabilities | Fine-grained privilege dropping |
| AppArmor/SELinux | Mandatory access control |

### Hardware-based

| Technology | Use Case |
|---|---|
| Intel SGX | Encrypted enclaves |
| ARM TrustZone | Secure world |
| AMD SEV | Encrypted VMs |
| TPM | Secure boot, key storage |

### Allowlisting

```
Default deny: Only approved executables run
Paths: C:\Program Files\*, /opt/approved/
Validation: Hash or signature check
Update: Through managed deployment
```

### Denylisting

```
Antivirus signatures
Known malware hashes
User-reported bad files
```
