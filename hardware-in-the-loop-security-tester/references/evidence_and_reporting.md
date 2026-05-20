# Evidence and reporting

## Table of contents

1. [Evidence package](#evidence-package)
2. [Finding format](#finding-format)
3. [Severity and safety notes](#severity-and-safety-notes)
4. [Coordination and retest](#coordination-and-retest)
5. [Data handling](#data-handling)

## Evidence package

For each test case or finding, assemble:

| Artifact | Content |
|---|---|
| **Test case record** | ID, hypothesis, preconditions, stimulus version |
| **Target identity** | Part number, serial (if allowed), firmware/hash, calibration ID |
| **Bus / network captures** | Raw trace + exported decode (DBC/LDF referenced) |
| **Target logs** | UDS DTC readout, application logs, crash dumps (redacted) |
| **Photos / wiring** | Bench tap points (no customer facility identifiers unless approved) |
| **Tool manifest** | Logger, injector, HIL software versions |
| **Timeline** | UTC-synchronized sequence of stimulus and response |

Store hashes (SHA-256) of large binaries in the report index.

## Finding format

```markdown
### [SEVERITY] Title

**Safety note:** (none | caution | hazard — required field)
**Impact:** (confidentiality / integrity / availability / safety-adjacent)
**Preconditions:** bench mode, keys, firmware hash
**Reproduction:** numbered steps on HIL bench
**Evidence:** file refs and offsets / frame IDs
**Root cause hypothesis:** design vs implementation vs configuration
**Remediation:** owner team (firmware, gateway, supplier)
**Retest:** pass criteria on bench
```

Deliver **executive summary** (risk themes, safety events) and **technical appendix** (full test case list).

## Severity and safety notes

| Severity | Guidance |
|---|---|
| **Critical** | Safety-adjacent or unauthorized control of safety-related function on bench |
| **High** | Reliable integrity break, persistent unlock, or cross-domain bypass |
| **Medium** | Conditional abuse requiring specific mode or key material |
| **Low** | Information disclosure or hardening gap without practical abuse on bench |
| **Informational** | Defense-in-depth recommendations |

Always separate **safety-adjacent** observations from classic CIA impact; escalate safety notes to product safety regardless of CVE-style severity.

## Coordination and retest

| Activity | Owner |
|---|---|
| Exploitability review | Firmware / vehicle security |
| Fix implementation | Engineering or supplier |
| Bench retest | HIL security tester with frozen test case IDs |
| Customer communication | Program management / `cybersecurity` as appropriate |

Retest only when firmware hash or config version is recorded; attach before/after traces.

## Data handling

- Minimize PII and geolocation from telematics captures
- Redact VIN, license plates, and facility identifiers in external reports
- Follow ROE for data residency and export controls on automotive/ICS artifacts
- Do not upload raw traces to public issue trackers without scrubbing
