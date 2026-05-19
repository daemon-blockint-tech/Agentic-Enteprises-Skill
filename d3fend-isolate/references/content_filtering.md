# Content Filtering & Validation

## Technique Coverage

| D3FEND Technique | Description |
|---|---|
| Content Filtering | Block/allow content |
| Content Modification | Sanitize content |
| Content Excision | Remove bad parts |
| Content Format Conversion | Transform format |
| Content Rebuild | Reconstruct safely |
| Content Substitution | Replace dangerous |
| Content Quarantine | Isolate suspicious |
| Content Validation | Validate structure |
| File Format Verification | Check file type |
| File Content Decompression Checking | Validate archives |
| File Internal Structure Verification | Validate internals |
| File Metadata Consistency Validation | Check metadata |
| File Metadata Value Verification | Verify values |
| File Magic Byte Verification | Check magic bytes |

## Filtering Layers

| Layer | Scope | Example |
|---|---|---|
| Email | Attachments, URLs, content | Block .exe, sandbox Office |
| Web | URLs, downloads, uploads | Block categories, scan uploads |
| Network | Protocol commands, payloads | DPI, protocol validation |
| Application | Input validation | Whitelist input, parameterized queries |
| File | Magic bytes, structure, metadata | Verify before processing |

## File Validation

```python
def validate_file(upload):
    # Magic bytes
    if not magic_bytes_match(upload, declared_type):
        reject("Magic bytes mismatch")
    
    # Metadata consistency
    if metadata_inconsistent(upload):
        reject("Metadata inconsistency")
    
    # Decompression check
    if is_archive(upload) and not valid_archive(upload):
        reject("Invalid archive")
    
    # Quarantine for deep inspection
    return quarantine(upload)
```

## Content Modification

| Input | Sanitization | Output |
|---|---|---|
| HTML | DOMPurify | Clean HTML |
| File | Rebuild from safe components | Safe document |
| Email | Remove scripts, validate links | Safe email |
| JSON/XML | Schema validation | Validated data |
