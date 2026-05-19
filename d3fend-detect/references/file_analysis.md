# File Analysis

## Technique Coverage

| D3FEND Technique | Description |
|---|---|
| File Analysis | General file inspection |
| Dynamic Analysis | Runtime behavior analysis |
| Emulated File Analysis | Sandboxed execution |
| File Content Analysis | Deep content inspection |
| File Content Rules | Signature matching |
| File Hashing | Hash generation/comparison |

## Analysis Stack

### Static Analysis

| Check | Tool | Output |
|---|---|---|
| Hash (MD5/SHA256) | sha256sum | Integrity reference |
| Strings | strings, floss | Readable text |
| Imports/Exports | pestudio, objdump | Dependency map |
| Entropy | ent, binwalk | Packing/encryption detection |
| File type | file, libmagic | Format verification |
| YARA rules | yara | Malware family identification |

### Dynamic Analysis

```
Sandbox: Cuckoo, ANY.RUN, Hybrid Analysis
Monitor: API calls, registry, files, network
Duration: 2-5 minutes typical
Report: Behavior summary, IOC extraction
```

### Emulated Analysis

```
Engine: Speakeasy, Unicorn, Binee
Advantage: No full VM overhead
Use: Quick triage, API log extraction
Limitation: Anti-emulation evasion
```

## Integration

```python
# Automated pipeline
file_received → hash_lookup → yara_scan → 
    if suspicious → sandbox → report
    if clean → release
```
