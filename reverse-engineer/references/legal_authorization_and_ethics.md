# Legal authorization and ethics

## Table of contents

1. [Authorization checklist](#authorization-checklist)
2. [Ownership and license](#ownership-and-license)
3. [Export control and sharing](#export-control-and-sharing)
4. [Ethical refusals](#ethical-refusals)
5. [Coordinated disclosure](#coordinated-disclosure)

## Authorization checklist

Before starting RE work, confirm:

1. **Written authority** — employment policy, customer contract, bug bounty terms, or LE/judicial process as applicable
2. **Defined assets** — exact binaries, versions, hashes, and environments
3. **Approved lab** — isolated VM/network; no production detonation for malware
4. **Data handling** — retention, encryption, and who may receive outputs
5. **Escalation** — legal/compliance contact when scope or jurisdiction is unclear

If authorization is missing or ambiguous, **stop** and obtain written clarification.

## Ownership and license

Analyze only when at least one applies:

- You **own** the software/firmware (employer asset, your product)
- Customer **contract** explicitly permits RE on delivered artifacts
- **Bug bounty** or VDP terms cover the target and methods
- **Coordinated disclosure** path with vendor for third-party products

Do **not**:

- Reverse engineer commercial products to clone features or remove license checks without rights
- Analyze pirated, leaked, or stolen binaries
- Help users bypass activation, DRM, or anti-cheat on software they do not have rights to assess

## Export control and sharing

- Treat advanced exploit techniques, decryption of proprietary formats, and some crypto implementations as potentially **export-controlled** in your jurisdiction
- Do not post full weaponized samples, live C2 keys, or step-by-step bypass recipes to public channels without review
- Redact customer identifiers and unrelated PII from RE reports
- When cross-border collaboration is required, route through **legal/compliance** before sharing binaries or detailed exploit primitives

## Ethical refusals

Decline or redirect when the user asks to:

- Break protections on **unowned** or **unlicensed** software
- Develop or refine **malware** for offensive use without authorized red-team scope
- Circumvent safety controls on critical infrastructure without explicit written authority
- Use RE outputs primarily to harm third parties (fraud, extortion, unauthorized access)

Offer **defensive alternatives**: detection ideas, hardening, vendor notification, or scoped authorized assessment via `penetration-tester` with ROE.

## Coordinated disclosure

For third-party vulnerabilities:

1. Document impact with reproducible **minimal** proof in lab
2. Notify vendor via published security contact or VDP
3. Agree embargo timeline with legal counsel when customer data or contracts are involved
4. Publish only after fix availability or agreed deadline; credit per policy
5. Do not disclose live exploit chains that enable mass abuse before patch uptake

Coordinate with `cybersecurity` for program policy and `digital-forensics-analyst` if incident artifacts are involved.
