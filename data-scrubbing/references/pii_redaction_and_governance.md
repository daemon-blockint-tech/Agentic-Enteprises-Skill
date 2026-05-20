# PII Redaction and Governance (Technical)

> **Not legal advice.** This reference covers technical patterns for minimizing sensitive data in scrub pipelines. Legal basis, retention, DPA terms, and regulatory filings require `compliance-engineer` and qualified counsel.

## Goals

- Reduce exposure of personally identifiable information (PII) and sensitive categories in datasets used for analytics, modeling, or sharing
- Maintain usefulness where possible via aggregation, tokenization, or separation of keys
- Leave audit trail of what was redacted and how

## PII inventory (minimum)

For each column, record:

| Field | Value |
|---|---|
| Column name | `member_email` |
| Category | direct identifier / quasi-identifier / sensitive |
| Regulatory tag | e.g., GDPR personal data (org taxonomy) |
| Required for use case? | yes / no |
| Approved treatment | mask / hash / drop / aggregate |

Use organizational data catalog when available; do not invent legal categories.

## Common PII categories (technical)

| Category | Examples | Typical treatment |
|---|---|---|
| Direct identifiers | name, email, phone, government ID | drop or tokenize |
| Quasi-identifiers | ZIP, DOB, gender, rare job title | generalize or suppress |
| Financial account | bank account, card PAN | drop; never log |
| Health (PHI) | diagnosis codes in some contexts | strict minimization; legal review |
| Online identifiers | cookie ID, device ID | hash with salt if needed |

## Treatment patterns

### Removal

Drop column from derivative datasets when not needed. Simplest and lowest risk.

### Masking

Partial display for operational support only:

- Email: `j***@domain.com`
- Phone: show last 4 digits

Not sufficient for open analytics datasets.

### Hashing / tokenization

```
token = HMAC-SHA256(pepper, normalized_value)
```

Requirements:

- Use organization-approved pepper/secret store (env var, KMS)—never commit pepper
- Normalize before hash (lower email, strip phone formatting)
- Same input → same token enables joins within environment
- Salting per environment prevents cross-env linkage

### Generalization

| Field | Generalization |
|---|---|
| DOB | birth year or age band |
| ZIP | 3-digit prefix (US) where policy allows |
| Date | month-start only |

### Aggregation

Publish cohort-level stats only; suppress small cells (n < k).

## Pseudonymization vs anonymization

| Term (technical) | Meaning |
|---|---|
| Pseudonymized | Reversible with key; still often regulated |
| Anonymized | No reasonable re-identification; expert determination required |

Do not label output "anonymized" without organizational sign-off.

## Pipeline controls

1. **Separate environments**: scrub in non-prod; restrict prod exports
2. **Least privilege**: pipeline service account reads only required columns
3. **Logging**: log rule IDs and counts, not raw PII values
4. **Output scanning**: run pattern detectors on sample exports (email regex, SSN patterns)
5. **Secure quarantine**: encrypted store for rows held for investigation

## Sharing externally

Before third-party transfer:

- Confirm contract and purpose limitation with legal/compliance
- Strip or tokenize per data sharing agreement
- Document schema and transformation version sent

Route SOC 2 / ISO evidence of controls to `compliance-engineer`.

## Coordination table

| Question | Route to |
|---|---|
| Lawful basis, DPIA, DSR delete workflows | `compliance-engineer`, counsel |
| Enterprise retention schedule | `data-architect`, compliance |
| Catalog and classification taxonomy | `data-architect` |
| Technical scrub implementation | this skill |

## Detection helpers (non-exhaustive)

Pattern-based scans (tune per locale):

- Email: RFC-like regex on sample
- Phone: E.164 length checks
- SSN (US): `###-##-####` with invalid area filters
- Credit card: Luhn check on digit runs

Flag columns for review; do not auto-delete without rule approval.

## Documentation for audit

Include in scrub package:

- PII column list and treatment per column
- Hash algorithm and key management reference (not the secret)
- Sample of masked output
- Count of rows in quarantine for failed redaction

## Anti-patterns

- Committing production extracts to git or public buckets
- Logging full row on parse errors
- Using reversible encoding (base64) and calling it encrypted
- Sharing dedupe keys across partners without agreement
- Assuming k-anonymity without formal analysis
