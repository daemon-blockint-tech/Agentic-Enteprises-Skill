# Threat intel and ATT&CK mapping

## Table of contents

1. [Intel sources](#intel-sources)
2. [Fusion workflow](#fusion-workflow)
3. [ATT&CK mapping](#attck-mapping)
4. [Coverage gaps](#coverage-gaps)
5. [Confidence and attribution](#confidence-and-attribution)

## Intel sources

Use **authorized** feeds and internal context:

- Commercial TI platforms, ISAC/ISAO sharing, government advisories (sector-specific)
- Vendor reports (campaign names, IOC bundles, TTP summaries)
- Internal: prior incidents, pentest/red team reports, purple-team results
- OSINT only when policy permits; cite URLs and retrieval date

Record **provenance** for every IOC and TTP claim in the hunt report.

## Fusion workflow

1. **Extract** IOCs (hash, domain, IP, email, cert thumbprint) and TTPs from intel
2. **Normalize** — de-duplicate, expire stale IOCs, note false-positive history
3. **Map** IOCs to enterprise telemetry (proxy, DNS, EDR, email, cloud)
4. **Expand** — pivot on hits to related entities (same ASN, parent domain, tooling family)
5. **Contrast** — compare findings to intel narrative; note mismatches
6. **Update** detection backlog and SOC runbooks when sustained true positives appear

Do not block production solely on low-confidence IOCs without corroboration.

## ATT&CK mapping

For each observed behavior, document:

| Field | Content |
|---|---|
| Technique ID | e.g., T1059.001 |
| Tactic | e.g., Execution |
| Procedure | How it manifested in your environment |
| Data source | Log type that proved it |
| Detection | Existing rule ID or “none” |

Use ATT&CK to structure hunts, not to inflate technique counts. Prefer **procedure-level** detail your defenders can action.

### Hunt framing by tactic

| Tactic | Example hunt questions |
|---|---|
| Initial Access | Unusual external auth, exploit-facing apps, new OAuth grants |
| Execution | Rare scripts, LOLBins, office child processes |
| Persistence | New services, scheduled tasks, cloud IAM keys |
| Privilege Escalation | Admin role grants, token theft indicators |
| Defense Evasion | Log clearing, disabled controls, timestomp patterns |
| Credential Access | LSASS-adjacent, Kerberos anomalies, password spray |
| Discovery | Recon commands, cloud enumeration APIs |
| Lateral Movement | RDP/WinRM/SMB spikes, new service accounts |
| Collection | Archive staging, large mailbox exports |
| C2 | Beaconing, DNS tunnels, rare JA3/JA4 |
| Exfiltration | Upload volume, cloud sync abuse |

## Coverage gaps

Maintain a simple matrix for the hunt:

- **Detected** — alert fired and investigated
- **Hunted only** — found manually; no reliable rule
- **No visibility** — required log missing or retention too short

Feed gaps to `detection_engineering_feedback.md` and program owners (`cybersecurity` for prioritization).

## Confidence and attribution

Use graded confidence on findings:

- **High** — multiple independent sources, strong temporal correlation
- **Medium** — single strong source or weak multi-source
- **Low** — circumstantial; needs more collection

**Attribution** to named actors is optional and often **not required** for defensive action. State “consistent with [campaign/actor]” only when intel supports it. Never claim legal attribution.

When intel conflicts with observations, trust **local evidence** and document the delta.
