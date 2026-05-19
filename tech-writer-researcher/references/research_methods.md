# Research Methods

## Research Design Frameworks

### PICO (Evidence-Based Practice)
Used for clinical/technical literature reviews:
- **P**opulation: Who or what is being studied?
- **I**ntervention: What action or exposure?
- **C**omparison: What is the alternative?
- **O**utcome: What is measured?

**Example:** "In distributed systems (P), does chaos engineering (I) vs traditional testing (C) reduce production incidents (O)?"

### SPIDER (Qualitative Research)
- **S**ample: Who was studied?
- **P**henomenon: What was explored?
- **D**esign: How was it studied?
- **E**valuation: What were the outcomes?
- **R**esearch type: Qualitative/quantitative/mixed

## Source Evaluation (CRAAP Test)

| Criterion | Questions |
|---|---|
| **C**urrency | When was it published? Is it still relevant? |
| **R**elevance | Does it answer your question? Is the level appropriate? |
| **A**uthority | Who wrote it? What are their credentials? |
| **A**ccuracy | Is it supported by evidence? Has it been reviewed? |
| **P**urpose | Why was it written? Is there bias? |

## Research Types & When to Use

| Type | When | Output |
|---|---|---|
| Literature review | Understanding a field | Synthesized overview, gap map |
| Systematic review | Rigorous evidence synthesis | PRISMA-compliant analysis |
| Meta-analysis | Quantitative evidence pooling | Effect size estimates |
| Scoping review | Mapping breadth of research | Conceptual framework |
| Rapid review | Time-constrained decision | Abbreviated synthesis |
| Competitive analysis | Market positioning | Feature matrix, SWOT |
| User research | Understanding user needs | Personas, journey maps |

## Synthesis Techniques

### Thematic Analysis
1. Familiarize: read all sources thoroughly
2. Code: label interesting features systematically
3. Theme: collate codes into potential themes
4. Review: check themes against data
5. Define: name and define each theme
6. Write: produce coherent narrative

### Evidence Matrix

| Study | Method | Sample | Key Finding | Quality | Relevance |
|---|---|---|---|---|---|
| Smith 2023 | RCT | n=500 | 20% improvement | High | Direct |
| Jones 2022 | Case study | n=1 | Novel approach | Medium | Indirect |

### Synthesis by Argument
Group findings by:
- **Agreement**: Multiple sources converge
- **Disagreement**: Contradictory findings (explore why)
- **Gap**: No research on specific sub-question
- **Methodological issues**: Limitations affecting interpretation

## Citation & Reference Management

### APA Style (Common for Research)
```
Book: Author, A. A. (Year). Title. Publisher.
Journal: Author, A. A. (Year). Title. Journal, vol(issue), pages.
Web: Author. (Year, Month Day). Title. Site. URL
```

### IEEE Style (Technical/Engineering)
```
[1] A. Author, "Title of paper," in Title of Book, City, State, Country: Publisher, year, pp. xx-xx.
```

### Chicago Style (Humanities/Business)
```
Author, Title (Place: Publisher, Year), page.
```

### Reference Management Tools
| Tool | Best For | Cost |
|---|---|---|
| Zotero | General research | Free |
| Mendeley | Collaboration | Free/Paid |
| EndNote | Institutional | Paid |
| Paperpile | Google Workspace | Paid |
| Citavi | Windows, knowledge management | Paid |

## Interview Techniques

### SME Interview Structure
1. **Context**: What are we documenting and why?
2. **Walkthrough**: Show me how you do X
3. **Edge cases**: What can go wrong?
4. **Audience**: Who needs this and what do they know?
5. **Validation**: Can I follow up with a draft?

### Active Listening for Writers
- Paraphrase to confirm understanding
- Ask "Why?" to get rationale, not just steps
- Capture exact terminology (don't translate yet)
- Record with permission, take verbatim notes

## Competitive Analysis

### Feature Comparison Matrix

| Feature | Us | Competitor A | Competitor B | Notes |
|---|---|---|---|---|
| SSO | Yes | Yes | No | Okta, Azure AD |
| Audit logs | 90 days | 1 year | 30 days | Enterprise need |
| Pricing | $10/user | $15/user | Freemium | We are mid-market |

### Analysis Dimensions
- Product features and UX
- Pricing and packaging
- Market positioning and messaging
- Strengths, weaknesses, opportunities, threats
- Customer reviews and sentiment
- Technical architecture (if relevant)

## Evidence Hierarchy

| Rank | Source Type | Reliability |
|---|---|---|
| 1 | Systematic reviews, meta-analyses | Highest |
| 2 | Randomized controlled trials | High |
| 3 | Cohort studies | Medium-High |
| 4 | Case-control, case series | Medium |
| 5 | Expert opinion, editorials | Lowest |

**For technical research:**
- Primary: RFCs, official documentation, source code
- Secondary: Books, peer-reviewed papers, conference talks
- Tertiary: Blog posts, tutorials, Stack Overflow

## Bias Detection

| Bias Type | How to Detect | Mitigation |
|---|---|---|
| Publication bias | Positive results overrepresented | Search grey literature |
| Confirmation bias | Seeking sources that agree | Actively search for contradictory evidence |
| Recency bias | Only recent sources | Include seminal older works |
| Authority bias | Assuming expert is always right | Check methodology independently |
| Selection bias | Non-representative sample | Document inclusion/exclusion criteria |
