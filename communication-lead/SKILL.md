---
name: communication-lead
description: |
  Guides communications leadership—messaging strategy, narrative and key-message development,
  stakeholder and executive comms cadence, internal announcements (all-hands, change, crisis),
  external customer and partner messaging, launch and incident communication plans, channel
  selection, approval workflows, and spokesperson/Q&A prep.
  Use when planning org-wide comms, drafting executive or company-wide messages, aligning
  narratives across teams, designing change or crisis communications, or preparing launch
  announcements—not for management consulting deliverables (business-consultant), API/docs/runbooks
  (tech-writer-researcher), on-call/paging/SEV program design (incident-management-engineer),
  single-ticket customer replies (support-engineer), exec/community escalation program
  (community-executive-escalations-program-manager), or legal contract language (commercial-counsel).
---

# Communication Lead

## When to Use

- Define messaging hierarchy: narrative, pillars, proof points, audience variants
- Plan comms for a launch, reorg, policy change, or transformation
- Draft executive updates, all-hands scripts, company-wide email/Slack posts
- Build crisis or incident **message** packs (holding lines, customer statements) with approval path
- Align product, sales, and support on what to say (and not say) externally
- Design comms cadence: weekly exec brief, monthly all-hands, incident updates
- Prepare spokesperson talking points and anticipated Q&A

## When NOT to Use

- Issue trees, business cases, steerCo slide **analysis** → `business-consultant`
- Technical documentation, runbooks, API reference → `tech-writer-researcher`
- Severity model, paging, on-call, postmortem **process** → `incident-management-engineer`
- Outage rollback and deploy tactics → `deployment-strategist`, `devops`
- Individual support ticket responses → `support-engineer`
- Marketing campaign creative, paid media, SEO → route to marketing skills if present; stay factual/product-truth aligned here
- Contract, DPA, or legal risk language → `commercial-counsel`
- Security control design → `cybersecurity`

## Related skills

| Need | Skill |
|---|---|
| Executive deck storyline and business case | `business-consultant` |
| Long-form docs and research synthesis | `tech-writer-researcher` |
| Incident program, status page workflow | `incident-management-engineer` |
| Release rollout and stakeholder brief | `deployment-strategist` |
| Cross-team program coordination | `technical-program-manager` |
| Customer escalation and ticket comms | `support-engineer` |
| Exec/VIP and community escalation program | `community-executive-escalations-program-manager` |
| Security incident policy and enterprise IR | `cybersecurity` |
| Security advisory and CVD publication | `technical-program-manager-security-cvd` |
| Product positioning and UX copy | `product-designer` |
| Commercial terms in customer comms | `commercial-counsel` |

## Core Workflows

### 1. Messaging framework

For any initiative, define:

1. **Audience** — who must hear, believe, and act
2. **Objective** — one outcome (e.g., adopt, reassure, comply)
3. **Narrative** — 2–3 sentence through-line (problem → direction → ask)
4. **Key messages** — 3–5 bullets, MECE, evidence-backed
5. **Proof points** — metrics, quotes, dates (no unverified claims)
6. **Guardrails** — what not to say; sensitive topics; legal review triggers

**See `references/messaging_framework.md`.**

### 2. Stakeholder and executive comms

| Artifact | Typical cadence | Lead with |
|---|---|---|
| Exec brief | Weekly | Decision or risk needing attention |
| SteerCo / leadership update | Per milestone | Status vs plan, blockers, asks |
| Board-style summary | Quarterly | Outcomes, risks, strategic choices |

Use pyramid structure: recommendation first, then support. Pair with `business-consultant` when the pack is primarily analytical.

**See `references/stakeholder_comms.md`.**

### 3. Internal communications

- **All-hands** — 30–45 min arc: context, wins, priorities, Q&A
- **Change** — why, what changes for whom, timeline, support channels
- **Manager cascade** — toolkit: email template, FAQ, office hours

Sequence: leaders briefed first → company announcement → team Q&A.

**See `references/internal_comms.md`.**

### 4. External communications

Align with product truth and legal review for:

- Customer email, in-app banners, changelog
- Partner or investor-facing notes (when approved)
- Blog or press statement (factual, attributable quotes only)

Never promise dates or features not shipped; coordinate with `deployment-strategist` for launch timing.

**See `references/external_comms.md`.**

### 5. Crisis and incident messaging

Separate **process** (`incident-management-engineer`) from **words**:

1. Confirm facts with incident commander; no speculation
2. Draft internal holding line → customer status → follow-up cadence
3. Route legal/comms/security approval per severity
4. Single source of truth doc; version messages

**See `references/crisis_comms.md`.**

### 6. Launch communications

| Phase | Comms focus |
|---|---|
| T-4 weeks | Internal preview, enablement, FAQ |
| T-1 week | Sales/support talk tracks |
| Launch | Coordinated send: email, blog, in-app, social (if approved) |
| T+1 week | Metrics, feedback loop, correction if needed |

**See `references/launch_comms.md`.**

## Output standards

- One **primary CTA** per message
- Plain language; define acronyms once
- Accessible formatting (headings, short paragraphs)
- Version and timestamp on crisis or incident drafts
- Flag `[LEGAL REVIEW]`, `[EXEC APPROVAL]` where required

## When to load references

- **Messaging hierarchy** → `references/messaging_framework.md`
- **Exec and leadership updates** → `references/stakeholder_comms.md`
- **All-hands and change** → `references/internal_comms.md`
- **Customer and public** → `references/external_comms.md`
- **Incident statements** → `references/crisis_comms.md`
- **Feature or initiative launch** → `references/launch_comms.md`
