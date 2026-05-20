# Deserialization, SSRF, and XXE

## Table of contents

1. [XML External Entity (XXE)](#xml-external-entity-xxe)
2. [Insecure deserialization](#insecure-deserialization)
3. [Server-Side Request Forgery (SSRF)](#server-side-request-forgery-ssrf)

**CWE:** 611 (XXE), 502 (deserialization), 918 (SSRF)  
**OWASP Top 10:2021:** A05 Security Misconfiguration (XXE/parser), A10 SSRF (2021 dedicated category)

---

## XML External Entity (XXE)

**Risk:** Malicious XML references external entities—local file read, SSRF, DoS (billion laughs).

**Vulnerable:** Default XML parsers accepting DTDs/external entities (`DocumentBuilderFactory`, `xml.etree` on untrusted XML, libxml2 without hardening).

**Secure patterns:**

- **Disable DTD and external entities** on every parser that handles untrusted XML.
- Prefer **JSON** or safer formats when XML is not required.
- Use well-maintained libraries with secure defaults; validate schema size limits.

| Platform | Hardening |
|---|---|
| Java `DocumentBuilderFactory` | `setFeature("http://apache.org/xml/features/disallow-doctype-decl", true)` plus disable external general/parameter entities |
| Python | Avoid `xml.etree` for untrusted input; use `defusedxml` |
| .NET | `XmlReaderSettings` with DTD processing prohibited |

**Review heuristics:** `parse(`, `DocumentBuilder`, SAX/DOM without feature flags on user-uploaded XML.

---

## Insecure deserialization

**Risk:** Attacker supplies serialized objects that execute code or bypass auth on deserialize.

**High-risk APIs (never on untrusted input):**

| Language | Dangerous |
|---|---|
| Java | `ObjectInputStream`, unsafe JSON/XML to arbitrary types |
| Python | `pickle.loads`, unsafe `yaml.load` (use `safe_load`) |
| Ruby | `Marshal.load`, `YAML.load` |
| PHP | `unserialize()` |
| .NET | `BinaryFormatter`, unsafe `TypeNameHandling.All` in JSON.NET |

**Secure patterns:**

- Deserialize to **limited DTOs** with schema validation (JSON + strict types).
- Sign and encrypt serialized blobs if used; short TTL.
- Reject polymorphic type discriminators from untrusted sources.

**Note:** `json.loads` is not RCE by itself; risk is **object graphs** and gadget chains in native serializers.

---

## Server-Side Request Forgery (SSRF)

**Risk:** Server fetches attacker-chosen URLs—internal services, cloud metadata (`169.254.169.254`), port scan, firewall bypass.

**Common sinks:** `requests.get(url)`, `axios.get(url)`, `fetch(userUrl)`, image/PDF fetchers, webhook validators, import-from-URL features.

**Secure patterns:**

| Control | Implementation |
|---|---|
| Fixed base URL | Only allow path/query parameters on a known host |
| Allowlist | Explicit list of schemes, hosts, ports |
| Block metadata | Deny link-local, loopback, RFC1918 unless required (defense in depth) |
| No redirects to internal | Disable redirects or re-validate each hop |
| Split DNS rebinding | Resolve and connect with consistent IP checks where feasible |

**Incorrect pattern:** User supplies full URL or hostname.

```python
# Vulnerable
requests.get(f"https://{user_host}/api/...")

# Better: allowlist host
ALLOWED = {"api.example.com"}
if user_host not in ALLOWED:
    raise ValueError("host not allowed")
requests.get(f"https://{user_host}/api/...")
```

**Cloud:** Block access to instance metadata from app roles unless strictly required; use IMDSv2 on AWS.

**Review heuristics:** HTTP client first argument from request params; URL parsers that accept `file://`, `gopher://`, or redirects.
