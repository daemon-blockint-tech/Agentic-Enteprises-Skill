# Compliance and evidence

## Table of contents

1. [Remediation SLAs](#remediation-slas)
2. [SOC 2 mapping (delivery)](#soc-2-mapping-delivery)
3. [ISO 27001 touchpoints](#iso-27001-touchpoints)
4. [SSDF / secure development](#ssdf--secure-development)
5. [Audit artifact checklist](#audit-artifact-checklist)
6. [Security incident severity](#security-incident-severity)

## Remediation SLAs

| Severity | CVSS (guide) | Target fix | Change type |
|---|---|---|---|
| Critical | 9.0–10.0 | 24–48 hours | Emergency |
| High | 7.0–8.9 | 7 days | Standard |
| Medium | 4.0–6.9 | 30 days | Scheduled |
| Low | 0.1–3.9 | 90 days | Backlog |

Adjust for exploitability, exposure (internet-facing), and compensating controls. Document extensions in waiver register.

## SOC 2 mapping (delivery)

| TSC | DevSecOps evidence |
|---|---|
| CC6 | Access reviews for CI/CD and cloud; branch protection |
| CC7 | Monitoring, vuln scanning, incident runbooks |
| CC8 | Change tickets linked to commits; peer review; pipeline logs |
| CC9 | Risk register entries for accepted vulns |

## ISO 27001 touchpoints

| Domain | Evidence from delivery |
|---|---|
| A.8 Asset management | SBOM, service inventory from IaC |
| A.9 Access control | IAM policies, RBAC manifests, OIDC config |
| A.12 Operations security | Scan reports, patch records |
| A.14 System acquisition/development | Threat models, secure SDLC policy, test results |
| A.16 Incident management | Incident tickets, postmortems |

## SSDF / secure development

Map practices to NIST SSDF practices (PO, PS, PW, RV):

- **Prepare:** security training, tool standards, threat modeling policy
- **Protect:** branch protection, secrets management, least privilege
- **Produce:** SAST/SCA/IaC in CI, code review, signed artifacts
- **Respond:** vuln triage, incident response, postmortems

## Audit artifact checklist

Collect automatically where possible:

- [ ] Branch protection and required check configuration export
- [ ] Sample PR showing security checks passed
- [ ] SAST/SCA scan reports for release tag
- [ ] Container scan report for deployed image digest
- [ ] SBOM for release
- [ ] Sign/provenance verification log
- [ ] Access review for CI and production roles (quarterly)
- [ ] Waiver register with approvals and expiry
- [ ] Threat model for critical service (current version)
- [ ] Penetration test summary and remediation tracker (annual or per major change)

Store in immutable bucket or GRC tool with retention matching audit period.

## Security incident severity

| Level | Definition | Example |
|---|---|---|
| Critical | Active breach or ransomware | Production DB exfiltration |
| High | Likely compromise or active attack | Successful privilege escalation |
| Medium | Policy violation, contained malware | Unapproved binary on host |
| Low | Reconnaissance, blocked attempt | Port scan |

**Response phases:** contain → eradicate → recover → post-incident review (blameless). Link to `infrastructure-engineer` runbooks for platform-specific steps.
