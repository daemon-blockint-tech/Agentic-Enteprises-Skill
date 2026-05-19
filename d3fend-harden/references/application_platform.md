# Application & Platform Hardening

## Technique Coverage

| D3FEND Technique | Description |
|---|---|
| Application Hardening | Secure app configuration |
| Application Configuration Hardening | Remove defaults |
| Disable Remote Access | Limit remote exposure |
| Control Flow Integrity | Prevent control hijacking |
| Dead Code Elimination | Remove unused code |
| Exception Handler Pointer Validation | Secure exception handling |
| Pointer Authentication | ARM pointer signing |
| Process Segment Execution Prevention | W^X memory |
| Segment Address Offset Randomization | ASLR |
| Stack Frame Canary Validation | Stack protection |
| Platform Hardening | OS/firmware hardening |
| Bootloader Authentication | Verified boot |
| Disk Encryption | Data at rest |
| Driver Load Integrity Checking | Driver signing |
| File Encryption | File-level encryption |
| Hardware-based Write Protection | ROM write protection |
| Physical Enclosure Hardening | Tamper resistance |
| Software Update | Patch management |
| System Configuration Permissions | Least privilege config |
| TPM Boot Integrity | Measured boot |

## Implementation

### Memory Protection

| Control | What It Does | Enable |
|---|---|---|
| ASLR | Randomize memory layout | OS default |
| DEP/NX | Mark stack/heap non-executable | OS default |
| Stack Canaries | Detect stack overflow | Compiler flag |
| CFI | Validate indirect branches | Compiler + runtime |
| Pointer Auth | Sign pointers (ARM) | Hardware support |

### Boot Integrity

```
Power On → BIOS/UEFI → Bootloader → OS
     ↓          ↓           ↓         ↓
   TPM PCR   Measured    Verified  Checked
   extends   extends     boot      against
   values    values      chain     expected
```

### Patch Management

| Asset Type | Patch Source | Frequency |
|---|---|---|
| OS | Vendor (WSUS, apt, yum) | Weekly |
| Applications | Vendor/auto-update | Weekly |
| Firmware | OEM | Monthly |
| Containers | Base image refresh | Per release |
| Network devices | Vendor | Monthly |

### Encryption

| Layer | Method | Key Management |
|---|---|---|
| Disk | LUKS, BitLocker, FileVault | TPM + PIN/recovery |
| File | EFS, native encryption | User cert |
| Database | TDE | HSM-backed |
| Application | Application-layer crypto | Key vault |
