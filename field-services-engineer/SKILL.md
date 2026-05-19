---
name: field-services-engineer
description: |
  Guides field services engineering—on-site and colocation smart-hands work: site readiness,
  rack-and-stack, power and network cabling, hardware install/replace, labeling, acceptance
  tests, photo documentation, customer sign-off, and remote handoff to NOC or platform teams.
  Use when planning or executing a field visit, writing work orders, troubleshooting physical
  layer on site, or coordinating vendor/colocation access—not for K8s cluster deploy (cluster-deployment-engineer),
  DC capacity program delivery (senior-data-center-capacity-delivery-manager), hall MEP design
  (data-center-design-execution-lead), cloud IaC (infrastructure-engineer), or software support
  tickets (support-engineer). Customer escalation program: community-executive-escalations-program-manager.
---

# Field Services Engineer

## When to Use

- Plan **site visit** scope, tools, parts, and access
- Execute **rack-and-stack**, rail kits, PDUs, cable management
- **Install, replace, or decommission** servers, switches, storage
- Run **power-on and link-light** checks; basic hardware diagnostics
- Apply **labeling** and asset tags per standards
- Complete **acceptance checklist** with photos and serials
- Obtain **customer/colo sign-off** and close work order
- **Hand off** to remote teams for OS/cluster bring-up
- Write **smart-hands instructions** for colo vendors

## When NOT to Use

- Kubernetes, Helm, GitOps on clusters → `cluster-deployment-engineer`
- MW/rack capacity program RAID → `senior-data-center-capacity-delivery-manager`
- Facility design, commissioning specs → `data-center-design-execution-lead`
- Terraform, VPC, cloud networking → `infrastructure-engineer`
- Remote software debugging → `support-engineer`
- Release rollout strategy → `deployment-strategist`

## Related skills

| Need | Skill |
|---|---|
| Rack-ready capacity delivery | `senior-data-center-capacity-delivery-manager` |
| Hall design and commissioning | `data-center-design-execution-lead` |
| Post-install cluster bootstrap | `cluster-deployment-engineer` |
| DC compute inventory | `data-center-compute-supply-efficiency` |
| On-site customer exec issues | `community-executive-escalations-program-manager` |
| Infra remote troubleshooting | `infrastructure-engineer` |

## Core Workflows

### 1. Site readiness and access

Prereqs, badges, lift, window.

**See `references/site_readiness_access.md`.**

### 2. Rack-and-stack install

Mechanical, power, weight.

**See `references/rack_stack_install.md`.**

### 3. Cabling and labeling

Copper/fiber, standards, tests.

**See `references/cabling_labeling.md`.**

### 4. Acceptance and sign-off

Tests, photos, CMDB.

**See `references/acceptance_signoff.md`.**

### 5. Safety and compliance

LOTO, PPE, escorts.

**See `references/safety_compliance.md`.**

### 6. Remote handoff

Runbook, escalation, closeout.

**See `references/remote_handoff.md`.**

## Output standards

- Work order lists **serial numbers, rack U positions, port map**
- Photos: wide rack, asset labels, cable dress, link lights
- No energize work without **approved change window** and safety check
- Remote team receives **single closeout note** with blockers explicit
- Escalate design conflicts to `data-center-design-execution-lead`, not improvise

## When to load references

- **Access** → `references/site_readiness_access.md`
- **Install** → `references/rack_stack_install.md`
- **Cables** → `references/cabling_labeling.md`
- **Acceptance** → `references/acceptance_signoff.md`
- **Safety** → `references/safety_compliance.md`
- **Handoff** → `references/remote_handoff.md`
