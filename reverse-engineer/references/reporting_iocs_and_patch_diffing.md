# Reporting, IOCs, and patch diffing

## Table of contents

1. [Vulnerability research memo](#vulnerability-research-memo)
2. [IOC export format](#ioc-export-format)
3. [YARA authoring](#yara-authoring)
4. [Patch diff workflow](#patch-diff-workflow)
5. [Variant hunting](#variant-hunting)
6. [Review checklist](#review-checklist)

## Vulnerability research memo

Use this structure for internal or coordinated disclosure:

1. **Title** — product, component, vulnerability class
2. **Affected versions** — exact builds; test matrix
3. **Summary** — one paragraph for executives
4. **Technical details** — root cause with function/offset references
5. **Preconditions** — auth, network position, config flags
6. **Impact** — confidentiality/integrity/availability; realistic abuse scenario in lab
7. **Reproduction** — minimal steps; no live weaponized hosting
8. **Remediation** — vendor fix, workaround, detection compensating controls
9. **Timeline** — discovery, report, vendor ack, fix, disclosure
10. **References** — CVE, advisories, related diffs

Label **speculation** clearly. Do not overstate CVSS without calculator inputs.

## IOC export format

Provide machine- and human-readable bundles:

| Type | Fields |
|---|---|
| File | SHA-256, MD5 (optional), filename obs., imphash |
| Network | Domain, IP, URL, JA3/JA4 if available, User-Agent |
| Host | Registry path, mutex, service name, scheduled task, file path |
| Email | Subject patterns, attachment hashes (if email vector) |

Include **first seen**, **confidence**, and **source** (sandbox run, static string). SOC (`soc-analyst`) validates before global block.

## YARA authoring

1. Pick **stable** regions (error strings, unique opcode patterns, config magic)
2. Avoid overly broad rules that flag entire compiler runtimes
3. Test against **corpus** of benign files in lab; record false positive rate
4. Version rules in repo; tag with **sample family** and **author**
5. Mark rules **experimental** until SOC promotion

Do not publish rules that primarily match security tools or red-team frameworks unless intentional.

## Patch diff workflow

```
identify fixed version → obtain before/after binaries → bindiff or diaphora → prioritize security-relevant changes → validate in lab
```

- Align **same build channel** (debug vs release confounds diffs)
- Focus on changed functions touching **parsers, auth, crypto, IPC, file ops**
- Read **commit messages** and advisories when source is available
- Re-run **PoC** against patched build in lab only—do not ship exploits
- Document **regression tests** defenders can use (crash file, malformed packet)

Tools: BinDiff, Diaphora, Ghidra Version Tracking, `diff` on symbols export.

## Variant hunting

After identifying fix:

- Search for **shared code** across product line (same function names, strings)
- Hunt **incomplete fixes** (length checks added but not width)
- Check **alternate entry points** (CLI vs GUI, kernel vs user)
- Share **hunting ideas** with `defensive-security-analyst` if installed

Stop at documented hypotheses—confirm with authorized test or vendor.

## Review checklist

Before delivery:

- [ ] Authorization and version scope stated
- [ ] Hashes and tooling versions included
- [ ] Facts separated from inference
- [ ] No live exploit hosting or C2 interaction instructions for abuse
- [ ] IOCs reviewed for collateral damage (CDN, shared libs)
- [ ] Legal/compliance notified for third-party or export-sensitive findings
- [ ] Peer skills cited where work continues (forensics, IR, SOC, pentest)
