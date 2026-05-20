# Jurisdiction formats and filing

## Table of contents

1. [Disclaimer](#disclaimer)
2. [Jurisdiction-agnostic core](#jurisdiction-agnostic-core)
3. [United States — FinCEN SAR](#united-states--fincen-sar)
4. [European Union — STR concepts](#european-union--str-concepts)
5. [United Kingdom — SAR to NCA](#united-kingdom--sar-to-nca)
6. [goAML and FIU platforms](#goaml-and-fiu-platforms)
7. [Continuing activity and amendments](#continuing-activity-and-amendments)
8. [Cross-border and group filing](#cross-border-and-group-filing)
9. [Mapping narrative to form fields](#mapping-narrative-to-form-fields)

## Disclaimer

This reference provides **high-level structural orientation** only. **Filing obligations, deadlines, thresholds, and legal interpretations** are for **MLRO and counsel**—see **`commercial-counsel`** and local counsel. Do not treat this document as legal advice.

## Jurisdiction-agnostic core

Most STR/SAR regimes expect:

| Element | Narrative block |
|---|---|
| Reporting entity identity | Who files |
| Subject identification | Who is reported |
| Financial institution role | Relationship to activity |
| Account / product details | Where activity occurred |
| Transaction details | What moved, when, how much |
| Suspicion description | Why it is unusual |
| Action taken | Restrictions, closures, SAR filed on prior date |
| Law enforcement contact | If already referred (factual) |

Draft in **modular sections** so compliance can paste into national XML/PDF portals.

## United States — FinCEN SAR

**Form**: FinCEN SAR (e-file via BSA E-Filing). Commonly called **SAR**, not STR.

| Concept | Drafting note |
|---|---|
| **Part IV — Suspicious activity information** | Types of activity—select categories supported by facts |
| **Narrative** | Often constrained by length—lead with summary; use continuation if allowed |
| **Subjects** | Individuals, entities, branches; include TIN/SSN/EIN when known |
| **Amount involved** | Total suspicious amount in USD; explain calculation |
| **Instrument types** | Check, wire, money order, crypto as applicable |
| **Prior SAR** | Indicate continuing activity |

**US-specific reminders** (non-exhaustive):

- Distinguish **BSA AML SAR** from other reports (e.g., fraud-only channels) per policy
- **314(b)** information sharing is separate from SAR narrative—follow legal process
- Do not include **Grand Jury** or sealed LE material without counsel

## European Union — STR concepts

EU framework (AMLD) generally requires reporting **suspicious transactions** to **FIU** without tipping off. Member states implement via national law.

| Theme | Drafting implication |
|---|---|
| **Objective indicators** | Describe facts; suspicion can be subjective but must be explained |
| **Attempted transactions** | Include prevented/incomplete if suspicious |
| **Tipping-off** | Strict internal distribution |
| **GDPR** | Lawful basis for processing; minimize data in non-essential copies |

Field names vary by member state portal—maintain **master narrative** plus country-specific field mapping table maintained by compliance.

## United Kingdom — SAR to NCA

UK uses **SAR** to **NCA** (not FinCEN form). Consider:

| Theme | Note |
|---|---|
| **Consent regime (DAML)** | Moratorium requests are **legal/process** topics—MLRO/counsel |
| **Defence against money laundering** | Not covered in this skill |
| **Terrorism** | May use separate pathway—coordinate with `aml-cft` |

Narrative should still follow who/what/when/where/why with UK terminology (e.g., sort code, account number).

## goAML and FIU platforms

Many FIUs use **goAML** or compatible XML schemas.

| goAML-oriented block | Content |
|---|---|
| Report code / reason | Institution selects per policy |
| Location | Branch where activity observed |
| Indicators | Map internal red flags to national indicator codes |
| Transactions | Structured tx list with parties and accounts |
| Attachments | PDF narrative, statements |

Build **structured data first** (transactions), then **attach narrative PDF** if workflow requires both.

## Continuing activity and amendments

| Situation | Typical handling (policy-dependent) |
|---|---|
| New facts on same subject | Continuing SAR/STR or amendment |
| Same pattern, new period | Reference prior report ID and date |
| Customer exited | Note closure date; final activity |
| False positive overturned | Do not file; document closure in case system only |

Narrative must state **relationship to prior report**: “Institution filed SAR ID [internal ref] on [date] regarding [summary]; activity continued as follows…”

## Cross-border and group filing

| Scenario | Consideration |
|---|---|
| Parent / subsidiary | Which entity has account relationship |
| Correspondent | Respondent vs originator obligations |
| Multiple countries touched | List jurisdictions of legs; avoid duplicate filings without coordination |

Group compliance often maintains **filing matrix**—reference it before finalizing narrative voice (“on behalf of [Entity X]”).

## Mapping narrative to form fields

Use a two-column worksheet for MLRO:

| Form field (example) | Narrative section / exhibit |
|---|---|
| Subject name | Who — primary subject |
| Total amount | Aggregation summary + Exhibit A |
| Suspicion description | Why — synthesis |
| Date range | When — first/last transaction |
| Product type | Account appendix |

Keeps **e-filing** accurate when narrative is drafted in Word/Markdown first.
