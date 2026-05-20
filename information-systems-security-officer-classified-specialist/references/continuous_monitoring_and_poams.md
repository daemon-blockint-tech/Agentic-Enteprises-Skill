# Continuous monitoring and POA&Ms

## Table of contents

1. [Continuous monitoring strategy](#continuous-monitoring-strategy)
2. [Ongoing control assessment](#ongoing-control-assessment)
3. [Significant changes](#significant-changes)
4. [POA&M lifecycle](#poam-lifecycle)
5. [Vulnerability management interface](#vulnerability-management-interface)

## Continuous monitoring strategy

Define in SSP or companion plan:

| Element | Example content |
|---|---|
| Objectives | Detect control drift before reassessment |
| Scope | Controls under ongoing assessment vs annual only |
| Frequency | Monthly operational reviews; quarterly deep dives |
| Roles | ISSO, control owners, ISSM |
| Metrics | POA&M aging, scan SLA compliance, change volume |
| Reporting | ISSM brief, AO staff read-ahead |

## Ongoing control assessment

Monthly (or program-defined) cycle:

1. Sample high-risk controls (access, logging, change, boundary protection)
2. Verify evidence freshness — not older than policy allows
3. Record pass/fail/partial with dated notes
4. Open POA&M or deviation when effectiveness fails
5. Update SSP only when implementation materially changes

## Significant changes

Treat as security-relevant when affecting:

- Authorization boundary or data flows
- Classification or impact level
- Interconnections or cross-domain interfaces
- Privileged access model or crypto posture
- Major version upgrades of COTS or platform

For each significant change:

1. Document description, date, approver
2. Perform security impact analysis (liaise with `information-security-engineer` for technical depth)
3. Update SSP sections and diagrams as needed
4. Notify ISSM and AO staff per program thresholds
5. Trigger re-assessment if required by program rules

## POA&M lifecycle

| State | Criteria |
|---|---|
| Open | Finding accepted; milestone dates set |
| In progress | Work underway; evidence partial |
| Pending verification | Fix deployed; awaiting scan or assessor check |
| Closed | Evidence on file; ISSM or assessor concurrence if required |
| Risk accepted | AO-approved exception with expiry |

Each POA&M row should include:

- Control ID and weakness description
- Risk rating (program scale)
- Scheduled completion date and responsible owner
- Milestones (interim dates)
- Source (assessment, scan, incident, self-identified)
- Evidence location upon closure

Escalate when: past due > 30 days (adjust per program), risk rating high without mitigation plan, or duplicate recurring findings.

## Vulnerability management interface

ISSO does not own the scanner but **owns traceability**:

1. Map scan findings to controls and POA&M entries
2. Track SLA by severity (critical/high/medium)
3. Distinguish false positives with documented rationale
4. Coordinate emergency patches through change and significant-change process
5. Summarize open critical counts for ISSM and authorization risk discussions

Hand technical remediation to `information-security-engineer`; retain POA&M and SSP alignment.
