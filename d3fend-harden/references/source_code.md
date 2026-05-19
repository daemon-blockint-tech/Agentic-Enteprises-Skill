# Source Code Hardening

## Technique Coverage

| D3FEND Technique | Description |
|---|---|
| Source Code Hardening | Secure coding practices |
| Credential Scrubbing | Remove secrets from code |
| Domain Logic Validation | Validate business rules |
| Operational Logic Validation | Validate ops rules |
| Integer Range Validation | Check integer bounds |
| Pointer Validation | Safe pointer use |
| Memory Block Start Validation | Buffer start checks |
| Null Pointer Checking | Null checks |
| Reference Nullification | Clear refs after free |
| Trusted Library | Use vetted libraries |
| Variable Initialization | Init before use |
| Variable Type Validation | Type checking |

## Secure Coding Checklist

### Input Validation

```python
# Good: validate range, type, and format
def process_age(age_str):
    try:
        age = int(age_str)
        if not (0 <= age <= 150):
            raise ValueError("Invalid age range")
        return age
    except ValueError:
        raise ValueError("Age must be a valid integer")

# Bad: trust input
def process_age_bad(age_str):
    return int(age_str)  # May crash or accept invalid
```

### Memory Safety

| Language | Safe Practices |
|---|---|
| C/C++ | Use smart pointers, bounds-checking APIs, ASan |
| Rust | Ownership model prevents most issues |
| Java/Go | Bounds-checked arrays, GC manages memory |
| Python | No raw pointers, but watch C extensions |

### Secrets Management

```
❌ Hardcoded: API_KEY = "sk-abc123"
✅ Environment: API_KEY = os.environ["API_KEY"]
✅ Secret vault: API_KEY = vault.get("api_key")
```

### Static Analysis Integration

| Tool | Language | Focus |
|---|---|---|
| Semgrep | Multi | Pattern matching, custom rules |
| SonarQube | Multi | Code quality + security |
| CodeQL | Multi | Deep semantic analysis |
| Bandit | Python | Python-specific issues |
| ESLint Security | JS/TS | Node.js security |

### Pre-commit Checks
```bash
# Block commits with secrets
gitleaks protect --staged

# Block commits with high-severity issues
semgrep --error --config=auto
```
