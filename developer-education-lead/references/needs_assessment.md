# Needs assessment

## Table of contents

1. [Personas](#personas)
2. [Jobs to be done](#jobs-to-be-done)
3. [Gap analysis](#gap-analysis)
4. [Prioritization](#prioritization)

## Personas

| Persona | Typical background | Goal |
|---|---|---|
| New hire (internal) | SWE generalist | Ship on platform in 30 days |
| External app developer | Web/mobile | Integrate API/SDK in prod |
| Partner / SI | Enterprise integrator | Certify and implement for clients |
| Power user | Existing customer | Advanced patterns, migration |
| Support → builder | CS/SRE curious | Reduce escalations via depth |

Document **prerequisites** per persona (language, cloud, security basics).

## Jobs to be done

Frame as verbs:

- "When I **first authenticate**, I want to **see a working call in <10 min**"
- "When I **debug a failed deploy**, I want to **find the right log and fix**"
- "When I **go to production**, I want to **know compliance and limits**"

Interview 5–8 learners per persona; synthesize themes.

## Gap analysis

| Signal source | What to extract |
|---|---|
| Support tickets | Top "how do I" clusters |
| Docs analytics | High bounce, low completion |
| Community forums | Repeated confusion |
| Sales/SE | Deal blockers from skill gaps |
| Engineering | Onboarding friction for new teams |

Map gaps to **module candidates** with severity (blocks adoption vs nice-to-have).

## Prioritization

Score modules:

| Factor | Weight |
|---|---|
| Reach (# learners affected) | High |
| Revenue or adoption impact | High |
| Effort to build (SME time, lab infra) | Medium |
| Risk if wrong (security, data) | Gate |

Publish **NOW / NEXT / LATER** roadmap for curriculum team and `tech-writer-researcher`.
