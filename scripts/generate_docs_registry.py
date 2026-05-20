#!/usr/bin/env python3
"""Generate .docs/SKILL_REGISTRY.md from SKILL.md frontmatter."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

LAYER_NAMES = {
    5: "Governance & Orchestration",
    4: "AI & ML Operations",
    3: "Data & Analytics",
    2: "Infrastructure, Cloud & Security",
    1: "Software Engineering",
    0: "Business, Actuarial & Operations",
    -1: "Physical Infrastructure",
}

# Explicit layer assignment (folder name -> layer). Unlisted skills use heuristics below.
EXPLICIT: dict[str, int] = {}

def _load_explicit():
    groups: dict[int, list[str]] = {
        5: [
            "build-validator", "ai-risk-governance", "ai-skill-manager",
            "engineering-manager-agent-prompts-evals", "engineering-manager-vertical-ai-products",
            "technical-program-manager", "technical-program-manager-security-cvd",
            "communication-lead", "enterprise-strategist", "cross-department-translation",
            "zero-tolerance-for-failure", "cyber-diligence-governance",
            "community-executive-escalations-program-manager", "country-manager",
            "deployment-strategist",
        ],
        4: [
            "ai-researcher", "ai-engineer", "ai-lead-ops", "ai-redteam",
            "ai-token-improvement-plan-engineer", "ai-context-engineer", "ai-memory-developer",
            "ml-research-engineer-safeguards", "ml-systems-engineer-rl-engineering",
            "ml-infrastructure-engineer-safeguards", "privacy-research-engineer-safeguards",
            "prompt-engineer", "prompt-engineer-agent-prompts-evals", "agentic-ai-developer",
            "multi-agent-system-engineer", "ai-adversarial-robustness-engineer",
            "applied-ai-architect-commercial-enterprise", "research-engineer-scientist-tokens",
            "tactical-ai-autonomy-developer", "markup-detection",
            "sentiment-analysis-engineer", "sentiment-forecasting-engineer",
        ],
        3: [
            "data-architect", "data-warehouse-engineer", "analytics-data-engineer",
            "analytics-data-engineering-manager-product", "data-scientist", "bi-analyst",
            "ontology-engineer", "data-system-ops-lead", "data-manager", "data-scrubbing",
            "data-visualization", "predictive-analytics", "predictive-logistics-developer",
            "quantitative-researcher", "ab-testing-engineer",
            "operations-research-algorithm-developer", "geospatial-telematics-developer",
            "edi-engineer", "business-analyst",
        ],
        2: [
            "infrastructure-engineer", "platform-engineer", "cluster-deployment-engineer",
            "devops", "devsecops", "cicd-engineer", "ci-cd-engineer", "cybersecurity",
            "information-security-engineer", "incident-management-engineer", "incident-responder",
            "offensive-security-analyst", "defensive-security-analyst", "compliance-engineer",
            "compliance-specialist", "cloud-architect", "cloud-engineer", "cloud-security-engineer",
            "cloud-system-administrator", "cloud-compliance-specialist", "cloud-economist",
            "enterprise-cloud-architect", "finops-analyst", "site-reliability-engineer",
            "sla-slo-engineer", "performance-engineer", "bcm-disaster-recovery-specialist",
            "vp-of-cloud", "vp-of-infrastructure", "iam-specialist",
            "advanced-persistent-threat", "cti-analyst", "threat-hunter", "soc-analyst",
            "penetration-tester", "red-team-specialist", "web-pentester", "network-pentester",
            "digital-forensics-analyst", "cyber-resilience-engineer", "enterprise-security-architect",
            "vendor-cyber-risk-analyst", "scada-ics-cyber-security-specialist",
            "yara-rule-authoring", "cryptographer-specialist", "reverse-engineer",
            "software-assurance-formal-methods-specialist", "chief-information-security-officer",
            "certified-information-systems-security-professional",
            "classified-cyber-security-senior-manager", "classified-software-devsecops-engineer",
            "information-systems-security-officer-classified-specialist",
            "hardware-in-the-loop-security-tester", "security-risk-analyst", "code-security",
            "product-infrastructure-security-engineer",
            "cisco-certified-network-professional", "sd-wan-engineer", "network-backbone-architect",
            "wireless-wifi-mobility-specialist", "iot-network-edge-engineer",
            "d3fend-deceive", "d3fend-detect", "d3fend-evict", "d3fend-harden",
            "d3fend-isolate", "d3fend-model", "d3fend-restore",
        ],
        1: [
            "senior-system-architecture", "senior-fullstack-developer", "senior-software-engineer",
            "senior-frontend-software-engineer", "fullstack-software-engineer", "web-application-developer",
            "ui-software-engineer", "ux-software-engineer", "support-engineer",
            "microservice-researcher", "microservices-analyst", "microservices-developer",
            "embedded-real-time-software-engineer", "control-software-developer",
            "simulation-software-engineer", "sensor-fusion-engineer", "sdk-engineer",
            "enterprise-integration-api-developer", "event-driven-architecture",
            "high-concurrency-scalability", "extreme-lifecycle", "mission-critical",
            "matrix-environment", "solutions-architect",
        ],
        0: [
            "business-model-researcher", "business-consultant", "commercial-counsel",
            "corporate-counsel", "senior-revenue-accountant", "deal-operations-administrator",
            "transaction-manager", "transaction-principal", "product-management-monetization",
            "product-management-human-data-platform", "product-designer", "customer-ops-specialist",
            "product-support-specialist", "developer-education-lead", "people-operations-specialist",
            "talent-acquisition", "talent-sourcer", "tech-writer-researcher", "storytelling",
            "compute-accounting-manager", "auditor",
            "actuary", "actuarial-analyst", "actuarial-consulting", "appointed-chief-actuary",
            "associate-actuary", "assumption-setting", "asset-liability-management",
            "advanced-long-term-actuarial-mathematics", "advanced-short-term-actuarial-mathematics",
            "pre-actuarial-foundations", "validation-by-educational-experience",
            "property-casualty-insurance", "life-health-insurance", "pension-retirement-funds", "ifrs",
            "aml-cft", "aml-compliance", "financial-intelligence-unit", "str-report",
            "anti-false-positive-decision-making",
            "supply-chain-manager", "wms-developer", "robotics-automation-integration-engineer",
            "predictive-logistics-developer",
        ],
        -1: [
            "data-center-design-execution-lead", "data-center-portfolio-planning-execution-lead",
            "data-center-compute-supply-efficiency", "director-infrastructure-capex-accounting",
            "senior-data-center-capacity-delivery-manager", "field-services-engineer",
        ],
    }
    for layer, folders in groups.items():
        for f in folders:
            EXPLICIT[f] = layer


_load_explicit()


def assign_layer(folder: str) -> int:
    if folder in EXPLICIT:
        return EXPLICIT[folder]
  # Heuristics for any new skills
    if folder.startswith("d3fend-"):
        return 2
    if folder.startswith(("ai-", "ml-", "prompt-engineer")):
        return 4
    if folder.startswith(("data-", "analytics-")) or folder in ("bi-analyst", "ontology-engineer"):
        return 3
    if folder.startswith(("cloud-", "devops", "devsecops", "cyber", "security", "soc-", "sre")):
        return 2
    if folder.startswith(("actuarial", "actuary", "aml-", "appointed-", "associate-actuary")):
        return 0
    if folder.startswith("senior-") or folder.endswith("-engineer"):
        return 1
    if folder.startswith("data-center-"):
        return -1
    return 0


def parse_skill(path: Path) -> tuple[str, str, str]:
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", text, re.DOTALL)
    name = folder = path.parent.name
    desc = ""
    if m:
        fm = m.group(1)
        nm = re.search(r"^name:\s*(.+)$", fm, re.MULTILINE)
        if nm:
            name = nm.group(1).strip().strip('"').strip("'")
        dm = re.search(r"^description:\s*\|\s*\n((?:  .+\n?)+)", fm, re.MULTILINE)
        if dm:
            desc = re.sub(r"^  ", "", dm.group(1), flags=re.MULTILINE).replace("\n", " ").strip()
        else:
            dm2 = re.search(
                r"^description:\s*(.+)$", fm, re.MULTILINE | re.DOTALL
            )
            if dm2:
                desc = dm2.group(1).strip()
            else:
                dm3 = re.search(
                    r"^description:\s*\|\s*\n(.*?)(?=\n\S|\Z)", fm, re.DOTALL | re.MULTILINE
                )
                if dm3:
                    desc = re.sub(r"^  ", "", dm3.group(1), flags=re.MULTILINE).replace(
                        "\n", " "
                    ).strip()
    return folder, name, desc[:280] + ("…" if len(desc) > 280 else "")


def main() -> None:
    skills = []
    for skill_md in sorted(ROOT.glob("*/SKILL.md")):
        if skill_md.parent.name.startswith("."):
            continue
        folder, name, desc = parse_skill(skill_md)
        layer = assign_layer(folder)
        skills.append((layer, folder, name, desc))

    by_layer: dict[int, list] = {k: [] for k in LAYER_NAMES}
    for s in skills:
        by_layer[s[0]].append(s)

    lines = [
        "# Agentic Enterprise OS — Skill Registry",
        "",
        "## Overview",
        "",
        f"Catalog of **{len(skills)}** skills in the Agentic Enterprise OS. Each entry maps a folder",
        "(`<skill-name>/SKILL.md`) to its display name, routing layer, and `description` triggers.",
        "",
        "**Distribution:** Install via [skills.sh](https://skills.sh) / [skills CLI](https://www.skills.sh/docs/cli):",
        "",
        "```bash",
        "npx skills add daemon-blockint-tech/Agentic-Enteprises-Skill --list",
        "npx skills add daemon-blockint-tech/Agentic-Enteprises-Skill --skill <folder-name> --agent cursor -y",
        "```",
        "",
        "**Source repo:** [github.com/daemon-blockint-tech/Agentic-Enteprises-Skill](https://github.com/daemon-blockint-tech/Agentic-Enteprises-Skill)",
        "",
        "**Authoritative triggers:** `description` in each skill's YAML frontmatter (not this file).",
        "",
        "---",
        "",
    ]

    idx = 1
    for layer in sorted(by_layer.keys(), reverse=True):
        items = by_layer[layer]
        lname = LAYER_NAMES[layer]
        sign = f"L{layer}" if layer >= 0 else f"L{layer}"
        lines.append(f"## Layer {layer}: {lname} ({len(items)} skills)")
        lines.append("")
        lines.append("| # | Folder | Display name | Summary |")
        lines.append("|---|--------|--------------|---------|")
        for _layer, folder, name, desc in sorted(items, key=lambda x: x[1]):
            esc = desc.replace("|", "\\|")
            lines.append(f"| {idx} | `{folder}` | {name} | {esc} |")
            idx += 1
        lines.append("")
        lines.append("---")
        lines.append("")

    # Summary stats
    lines.append("## Summary statistics")
    lines.append("")
    lines.append("| Layer | Skills | % of total |")
    lines.append("|-------|--------|------------|")
    total = len(skills)
    for layer in sorted(by_layer.keys(), reverse=True):
        n = len(by_layer[layer])
        pct = 100.0 * n / total
        sign = f"L{layer}" if layer >= 0 else f"L{layer}"
        lines.append(f"| {sign}: {LAYER_NAMES[layer]} | {n} | {pct:.1f}% |")
    lines.append(f"| **Total** | **{total}** | **100%** |")
    lines.append("")
    lines.append("## skills.sh index")
    lines.append("")
    lines.append("| Field | Value |")
    lines.append("|-------|-------|")
    lines.append("| Package | `daemon-blockint-tech/Agentic-Enteprises-Skill` |")
    lines.append(f"| Skill count | {total} |")
    lines.append("| Cursor install | [skills.sh/agent/cursor](https://www.skills.sh/agent/cursor) |")
    lines.append("| Badge | `https://skills.sh/b/daemon-blockint-tech/Agentic-Enteprises-Skill` |")
    lines.append("")
    lines.append("### Folder index (alphabetical)")
    lines.append("")
    for layer, folder, name, _ in sorted(skills, key=lambda x: x[1]):
        lines.append(f"- `{folder}` — {name}")
    lines.append("")

    out = ROOT / ".docs" / "SKILL_REGISTRY.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {out} ({len(skills)} skills)")


if __name__ == "__main__":
    main()
