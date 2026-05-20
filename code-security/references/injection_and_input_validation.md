# Injection and input validation

## Table of contents

1. [SQL injection](#sql-injection)
2. [Command injection](#command-injection)
3. [Cross-site scripting (XSS)](#cross-site-scripting-xss)
4. [Path traversal](#path-traversal)
5. [Code injection](#code-injection)
6. [General input validation](#general-input-validation)

**CWE:** 89 (SQLi), 78 (OS command), 79 (XSS), 22 (path traversal), 94 (code injection)  
**OWASP Top 10:2021:** A03 Injection, A07 Identification and Authentication Failures (XSS session impact)

---

## SQL injection

**Risk:** Attacker manipulates query logic—read, modify, or delete data; sometimes RCE via DB features.

**Vulnerable patterns:** String concatenation, `.format()`, `%` formatting, f-strings, template literals embedding user data in SQL.

**Secure patterns:**

- **Parameterized queries / prepared statements** — bind values separately from SQL text.
- **ORM query APIs** — use bound parameters; avoid raw SQL with interpolation.
- **Identifiers** (table/column names) — allowlist only; never parameterize identifiers as strings from users.

| Language | Prefer |
|---|---|
| Python (psycopg2) | `cur.execute("SELECT * FROM users WHERE id = %s", [user_id])` |
| Node (pg) | `pool.query('SELECT * FROM users WHERE id = $1', [userId])` |
| Java (JDBC) | `PreparedStatement` with `setString` / `setInt` |
| Go | `db.Query("SELECT ... WHERE id = ?", id)` |

**Review heuristics:** Search for `execute(f"..."`, `` `...${var}` ``, `"SELECT" +`, `String.format` with SQL.

---

## Command injection

**Risk:** Arbitrary OS command execution when user input reaches a shell.

**Vulnerable patterns:** `os.system`, `subprocess` with `shell=True`, `exec` of shell strings, backticks, `Runtime.exec(String)` with concatenation.

**Secure patterns:**

- Pass **argument arrays** without shell interpretation (`subprocess.run([...], shell=False)`).
- Use library APIs instead of CLI wrappers when possible.
- Strict allowlists for any unavoidable dynamic arguments.

| Language | Avoid | Prefer |
|---|---|---|
| Python | `os.system(user_input)` | `subprocess.run(["tool", arg], shell=False)` |
| Node | `exec(\`cmd ${user}\`)` | `spawn` with `args` array |
| Java | `Runtime.getRuntime().exec("cmd " + user)` | `ProcessBuilder` with separate args |

---

## Cross-site scripting (XSS)

**Risk:** Inject script into pages viewed by other users—session theft, defacement, malware.

**Types:** Reflected, stored, DOM-based.

**Secure patterns:**

- **Context-aware output encoding** (HTML, attribute, JS, URL contexts differ).
- Use framework defaults that auto-escape (`react` JSX text, template engines with escape).
- **Content-Security-Policy** as defense in depth.
- Never insert unsanitized HTML from users; if rich text is required, use a vetted sanitizer allowlist.

| Context | Guidance |
|---|---|
| HTML body | Encode `<`, `>`, `&`, quotes |
| Attribute | Encode quotes; prefer quoted attributes |
| JavaScript | Do not build JS from user strings; use JSON.parse on server-generated JSON |
| URL | Validate scheme (`https` only); encode |

**Review heuristics:** `innerHTML`, `dangerouslySetInnerHTML`, `document.write`, unescaped template insertion in server HTML.

---

## Path traversal

**Risk:** Read or write files outside intended directory via `../` or absolute paths.

**Secure patterns:**

- Resolve to **canonical path** and verify prefix under an allowed base directory.
- Reject `..`, NUL bytes, and alternate encodings in filenames.
- Use framework-safe APIs (`send_file` with safe root, `Path.resolve()` checks).

```python
# Pattern: canonicalize then prefix-check
base = Path("/var/app/uploads").resolve()
target = (base / user_filename).resolve()
if not str(target).startswith(str(base)):
    raise ValueError("invalid path")
```

---

## Code injection

**Risk:** Execute attacker-controlled code via `eval`, `Function()`, template engines, or dynamic import.

**Vulnerable patterns:** `eval(user_input)`, `new Function(user)`, server-side template injection, `pickle`/`Marshal` on untrusted bytes (see deserialization reference).

**Secure patterns:**

- Never evaluate user input as code.
- Use safe DSLs or strict JSON parsing with schema validation.
- Sandboxing is a last resort—not a substitute for avoiding dynamic execution.

---

## General input validation

Apply at trust boundaries:

| Principle | Practice |
|---|---|
| Allowlist over denylist | Accept known-good enums, formats, lengths |
| Type and range | Parse integers/dates explicitly; reject overflow |
| Normalize once | Unicode normalization before comparison |
| Fail closed | Reject invalid input; do not coerce silently |
| Log safely | Do not log secrets or full PII |

**Prototype pollution (JavaScript):** Validate object keys; avoid unsafe merge into prototypes (`__proto__`, `constructor`). Use `Object.create(null)` for maps when appropriate. **CWE-1321.**
