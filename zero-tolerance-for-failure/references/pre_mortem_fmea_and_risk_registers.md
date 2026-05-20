# Pre-mortem, FMEA, and risk registers

## Table of contents

1. [When to run structured risk work](#when-to-run-structured-risk-work)
2. [Pre-mortem workflow](#pre-mortem-workflow)
3. [FMEA basics](#fmea-basics)
4. [Risk register pattern](#risk-register-pattern)
5. [Linking to gates and metrics](#linking-to-gates-and-metrics)
6. [Facilitation tips](#facilitation-tips)

## When to run structured risk work

| Trigger | Recommended method |
|---|---|
| New tier-0/1 service or major architecture pivot | Pre-mortem + FMEA lite |
| Large migration, cutover, or flag flip at scale | Pre-mortem + rollback drill |
| Repeat incident or serious near-miss | FMEA on affected subsystem |
| Classified or safety-critical change | Formal risk register + change board |
| “We’ve always done it this way” without recent test | Norms audit + pre-mortem |

Skip heavyweight FMEA for low-tier experiments—still document **residual risk** and owner.

## Pre-mortem workflow

**Goal:** Imagine future failure, then prevent it before launch.

1. **Frame** — objective, scope, success criteria, irreversible steps
2. **Assume failure** — “It is 6 months later; we failed badly. Why?”
3. **Silent brainstorm** — causes, blind spots, org failures (5–10 min)
4. **Share and cluster** — themes: technical, process, people, external
5. **Mitigate** — controls, gates, tests, owners, dates
6. **Residual risk** — accept, defer with date, or stop launch
7. **Record** — store in risk register; link to change ticket

**Outputs:** mitigation backlog, new gates, test additions, stop-the-line triggers.

## FMEA basics

**Failure Mode and Effects Analysis** scores:

| Field | Description |
|---|---|
| **Function** | What the component must do |
| **Failure mode** | How it can fail |
| **Effect** | Local and system impact |
| **Cause** | Root mechanisms |
| **Current controls** | Detection/prevention already in place |
| **Severity (S)** | 1–10 impact if unmitigated |
| **Occurrence (O)** | 1–10 likelihood |
| **Detection (D)** | 1–10 chance current controls catch it |
| **RPN** | S × O × D (or use S×O with separate detection plan) |
| **Action** | Design/test/process change |
| **Re-score** | After action implemented |

Prioritize rows with **high S** even if RPN moderate—catastrophic rare events matter in HRO contexts.

## Risk register pattern

Maintain a **living register** (spreadsheet or ticket epic):

| Column | Purpose |
|---|---|
| Risk ID | Stable reference |
| Description | Clear failure scenario |
| Tier / system | Scope |
| Owner | Accountable mitigator |
| Controls | Existing + planned |
| Residual level | Low/Med/High or qualitative |
| Review date | Expiry for accepted risk |
| Linked changes | Tickets, ADRs, gates |

**Accepted high residual risk** requires **named executive or delegated authority** and expiry—no permanent “accepted” without review.

## Linking to gates and metrics

| Risk work output | Downstream hook |
|---|---|
| New test requirement | CI gate or release checklist (`build-validator`) |
| Architecture change | ADR + design review (`senior-system-architecture`) |
| Ops readiness gap | Ops gate evidence |
| Monitoring gap | SLI/alert work (`site-reliability-engineer`) |
| Recovery gap | Resilience test (`cyber-resilience-engineer`) |

After launch, track **did any pre-mortem scenario occur?** — calibrate facilitation quality.

## Facilitation tips

- Invite **skeptics and operators**, not only builders
- Use **premortem.google** style anonymity if hierarchy suppresses speech
- Separate **learning** from **go/no-go** decision in the meeting record
- Time-box; assign owners before adjourn
- Re-run when **scope changes materially**—do not shelf the doc

Do not use pre-mortem output for **performance punishment**—undermines HRO reporting culture.
