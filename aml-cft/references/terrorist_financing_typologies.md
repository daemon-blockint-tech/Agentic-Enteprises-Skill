# Terrorist financing typologies

## Table of contents

1. [TF vs money laundering](#tf-vs-money-laundering)
2. [Core typologies](#core-typologies)
3. [Red flags by typology](#red-flags-by-typology)
4. [Investigation prompts](#investigation-prompts)
5. [Scenario mapping](#scenario-mapping)
6. [Limitations](#limitations)

## TF vs money laundering

| Dimension | Money laundering (ML) | Terrorist financing (TF) |
|---|---|---|
| Primary aim | Disguise illicit **proceeds** of crime | Fund **terrorist acts** or support networks |
| Source of funds | Often criminal proceeds | May be **legitimate**, self-funded, or mixed |
| Transaction size | Often larger, layering focus | May be **small**, high frequency, purpose-driven |
| Lifecycle stage | Placement, layering, integration | Any stage; **reverse** flow (funds out for ops) |
| Detection bias | Amount, velocity, jurisdiction risk | **Purpose**, associates, channels, NPO/trade abuse |

Do not dismiss low-value activity when TF purpose indicators exist.

## Core typologies

### Self-funding

Individuals or cells use **salaries, savings, benefits, or small businesses** to fund operations. Funds may appear clean; suspicion rests on **behavior**, travel, associates, and open-source context.

### Charitable and nonprofit fronts

Legitimate or sham **NPOs** collect donations and divert a portion to designated groups. Typology combines social trust, cross-border transfers, and weak governance.

### MVTS and remittance abuse

Licensed or **unlicensed** money/value transfer services move funds across corridors with limited transparency. Structuring may mirror ML but **beneficiary patterns** and corridor risk dominate.

### Trade-based terrorist financing

Mis-invoicing, over/under-shipment, and commodity trades move value alongside or instead of wire transfers. Overlaps with TBML; add **end-user** and **dual-use** concerns for PF overlap.

### Cash couriers and stored value

Physical movement of cash, prepaid cards, vouchers, and crypto ATMs—often below thresholds. Document **route**, **handlers**, and **counterparties**.

### Crowdfunding and social media solicitation

Online platforms, crypto wallets, and P2P appeals for "humanitarian" causes with opaque ultimate use. Monitor **wallet clustering** only as decision support with limitations.

### State or organized sponsor flows

Large-scale flows from sponsor entities (sanctions-sensitive). Route to **TFS** and PF references; escalate immediately on designation matches.

## Red flags by typology

| Typology | Example red flags |
|---|---|
| Self-funding | Dormant account activation before travel; purchases inconsistent with profile; donations to high-risk causes |
| Charitable front | NPO with no program spend; transfers to unrelated commercial entities; high-risk geography concentration |
| MVTS | Agent without license; split transactions; sender/beneficiary incoherence; weak KYC at agents |
| Trade-based TF | Invoice mismatch; round-dollar shipping; goods inconsistent with stated business |
| Cash / stored value | Repeated sub-threshold deposits; multiple branches same day; voucher churn |
| Crowdfunding | New platform + immediate cross-border outflows; mixer exposure (heuristic only) |

## Investigation prompts

When reviewing alerts or cases, document answers where known:

1. **Who** benefits—individuals, NPO, MVTS agent, shell company?
2. **What** is the stated purpose—donation, remittance, trade, payroll?
3. **Where** are corridors and countries—sanctions, conflict, FATF high-risk?
4. **When** did pattern change—event-linked spikes (conflict, designation)?
5. **Why** is TF suspected vs ML—purpose indicators, OSINT, law enforcement inquiries?
6. **How** did funds move—wire, MVTS, cash, trade, crypto (with analytics limits)?

Maintain **need-to-know**; do not tip off subjects during investigation.

## Scenario mapping

Map internal scenarios to typologies for coverage reviews:

| Internal scenario (examples) | Primary typology |
|---|---|
| NPO account → high-risk wire | Charitable front / cross-border |
| Remittance aggregator burst | MVTS |
| Invoice value >> market | Trade-based TF |
| Customer small donations, unknown NGO out | Charitable / crowdfunding |
| Sanctions hit + prior benign history | TFS (see targeted sanctions reference) |

Review **false negative** feedback from law enforcement typology advisories annually.

## Limitations

- Red flags are **not proof** of TF; combine transaction, KYC, and vetted intelligence
- Open-source and blockchain labels are **heuristic**; document confidence
- Do not advise law enforcement tactics or covert operations
- Legal filing decisions belong to MLRO/counsel—not this skill
