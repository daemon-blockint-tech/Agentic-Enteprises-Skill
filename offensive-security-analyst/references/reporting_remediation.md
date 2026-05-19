# Reporting and remediation

## Table of contents

1. [Report structure](#report-structure)
2. [Executive summary](#executive-summary)
3. [Retest checklist](#retest-checklist)

## Report structure

1. Executive summary
2. Scope and methodology
3. Risk rating methodology
4. Findings summary table
5. Detailed findings (one section per issue)
6. Attack narrative (optional, for red team)
7. Appendices (tools, raw scan configs redacted)

## Executive summary

Include:

- Overall risk posture (sentence)
- Count by severity
- Top 3 themes (e.g., auth, injection, cloud IAM)
- Remediation priority order
- Positive observations (controls that worked)

## Retest checklist

For each fixed critical/high finding:

- [ ] Customer states fix deployed and version/build ID
- [ ] Analyst reproduces original steps
- [ ] Confirm exploit no longer succeeds
- [ ] Update status: Open → Remediated → Verified
- [ ] Note partial fixes explicitly
