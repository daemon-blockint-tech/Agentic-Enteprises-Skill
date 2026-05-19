---
name: ai-redteam
description: |
  Guides adversarial testing of AI systems—prompt injection, jailbreaks, tool abuse, data exfiltration,
  bias and harmful output probes, multi-turn attacks, and automated red-team harnesses for LLM applications.
  Use when red-teaming chatbots, agents, RAG systems, or copilots before launch, designing safety eval
  suites, reproducing reported vulnerabilities, or validating mitigations after incidents—not for writing
  corporate AI policy (ai-risk-governance), building production features (ai-engineer), or general
  network penetration testing (cybersecurity).
---

# AI Red Team

## When to Use

- Red-teaming chatbots, agents, RAG systems, or copilots before launch
- Designing safety evaluation suites and adversarial test harnesses
- Reproducing reported prompt injection or jailbreak vulnerabilities
- Validating mitigations after incidents (retesting filters, hardening)
- Running multi-turn coercion, encoding, or indirect injection campaigns
- Assessing bias, harmful output, or data exfiltration risks in LLM applications
- Scoping rules of engagement and severity rubrics for AI security testing

## When NOT to Use

- Writing corporate AI policy or risk governance frameworks → `ai-risk-governance`
- Building production LLM features or RAG pipelines → `ai-engineer`
- General network penetration testing or app/API security → `cybersecurity` / `offensive-security-analyst`
- CI/CD pipeline security → `devsecops`

## Related skills

| Need | Skill |
|---|---|
| Production architecture and mitigations | `ai-engineer` |
| Governance sign-off and risk tiers | `ai-risk-governance` |
| Prompt design baselines | `prompt-engineer` |
| CI pipeline security | `devsecops` |
| App/API security testing | `cybersecurity` |
| Network/app pentest and red team (non-LLM) | `offensive-security-analyst` |

## Core Workflows

### 1. Scope and rules of engagement

1. Define target: model, app surface, tools, data stores
2. Obtain written authorization and time window
3. Agree out-of-scope (e.g., no social engineering of employees unless approved)
4. Define success criteria: critical findings, reproduction steps, severity rubric
5. Plan safe test environment (no prod customer data)

**See `references/engagement_scope.md` for ROE template and severity definitions.**

### 2. Threat model for LLM applications

| Class | Examples |
|---|---|
| Prompt injection | Instructions in user/doc content override system policy |
| Jailbreak | Role-play, encoding, multi-turn coercion |
| Tool abuse | Unauthorized API calls, parameter injection |
| Data exfiltration | RAG leaks other tenants' chunks, PII in logs |
| Supply chain | Malicious tool definitions, compromised plugins |
| Denial of service | Token burn, recursive agent loops |

**See `references/attack_catalog.md` for technique families and test prompts (use ethically).**

### 3. Test execution

**Phases:**

1. **Baseline** — document intended refusals and allowed behaviors
2. **Automated sweep** — harness with curated attack set + fuzz mutations
3. **Manual creativity** — domain-specific abuse scenarios
4. **Tool/RAG focus** — indirect injection via retrieved documents
5. **Regression** — re-run after mitigations

Log: input, output, tool calls, latency, whether guardrail fired.

**See `references/testing_harness.md` for harness design and datasets.**

### 4. Reporting

Each finding includes:

- Title and severity (impact × likelihood)
- Steps to reproduce (minimal)
- Evidence (redacted transcripts)
- Affected component
- Recommended mitigation
- Retest criteria

**See `references/reporting.md` for report template and remediation tracking.**

### 5. Mitigation validation

| Mitigation | Retest |
|---|---|
| Input/output filters | Bypass attempts with paraphrases |
| System prompt hardening | Injection via RAG context |
| Tool allowlists | Confused deputy and scope creep |
| Human approval gate | Automated agent bypass paths |

**See `references/mitigations.md` for defense depth and known weak controls.**

## When to load references

- **ROE and scope** → `references/engagement_scope.md`
- **Attack types** → `references/attack_catalog.md`
- **Harness and automation** → `references/testing_harness.md`
- **Reports** → `references/reporting.md`
- **Defenses** → `references/mitigations.md`
