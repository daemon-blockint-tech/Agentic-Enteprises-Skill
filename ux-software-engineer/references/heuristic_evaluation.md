# Heuristic Evaluation

## When to run

- Before major release on changed flows
- After support tickets cluster on confusion
- When metrics drop (activation, completion) without clear technical cause
- Complement—not replace—usability testing with real users

## Nielsen heuristics (quick pass)

| # | Heuristic | Look for |
|---|-----------|----------|
| 1 | Visibility of system status | Loading, save, sync, progress |
| 2 | Match real world | Labels match user mental models |
| 3 | User control | Undo, cancel, back, escape |
| 4 | Consistency | Same action, same label, same place |
| 5 | Error prevention | Confirm destructive; disable invalid |
| 6 | Recognition over recall | Visible options, recent items |
| 7 | Flexibility | Shortcuts for power users |
| 8 | Minimalist design | Noise, duplicate CTAs |
| 9 | Error recovery | Clear message + next step |
| 10 | Help | Contextual help, not manual only |

## Severity scale

| Level | Definition | Example |
|-------|------------|---------|
| **0** | Cosmetic | Alignment nit |
| **1** | Minor | Inconsistent icon |
| **2** | Major | User likely hesitates or retries |
| **3** | Critical | Task blocked or data loss risk |

## Finding format

```markdown
**[S2] Checkout — Error recovery**
Heuristic: 9
Issue: Card decline shows only "Error" with no retry path.
Impact: Users abandon; support volume.
Recommendation: Show decline reason (safe subset), keep form data, primary "Try again".
Effort: S
Owner: ui-software-engineer
```

## Scope the audit

- One primary persona per pass
- One journey at a time (e.g. onboarding day 1)
- Desktop and mobile if both supported
- Keyboard-only pass for critical flows (coordinate with `senior-frontend-software-engineer` for WCAG depth)

## Output

1. Executive summary (top 5 fixes)
2. Full table sorted by severity
3. Linked tickets with acceptance criteria
4. "Won't fix" with rationale

## Avoid

- Opinion without task context ("I don't like blue")
- Replacing product strategy debates—escalate to PM/design
- Claiming WCAG compliance from heuristics alone
