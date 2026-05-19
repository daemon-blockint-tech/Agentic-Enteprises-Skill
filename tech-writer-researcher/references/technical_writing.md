# Technical Writing

## Document Templates

### README Template
```markdown
# Project Name

One-sentence description of what this project does.

## Installation

```bash
pip install package-name
```

## Quick Start

```python
import package
result = package.do_something()
```

## Documentation

Full docs: [link]

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md)

## License

[MIT](LICENSE)
```

### API Reference Template
```markdown
## GET /resource/{id}

Retrieve a single resource by ID.

### Parameters
| Name | Type | Required | Description |
|---|---|---|---|
| id | string | Yes | Unique resource identifier |

### Response
```json
{
  "id": "abc123",
  "name": "Example",
  "created_at": "2024-01-15T10:00:00Z"
}
```

### Errors
| Status | Description |
|---|---|
| 404 | Resource not found |
| 403 | Insufficient permissions |
```

### Runbook Template
```markdown
# [Incident Name] Runbook

## Symptoms
- [ ] Alert: `error_rate > 5%`
- [ ] User reports: [specific symptom]

## Impact Assessment
1. Check dashboard: [link]
2. Identify scope: [affected regions/services]

## Resolution Steps
1. [Step 1 with command]
2. [Step 2 with command]
3. Verify: [how to confirm fix]

## Rollback
If resolution fails:
1. [Rollback command]
2. [Verification]

## Post-Incident
- [ ] Update status page
- [ ] Log in incident tracker
```

## Style Guide Principles

### Clarity
- Use simple words: "use" not "utilize"
- Short sentences (<25 words)
- One idea per paragraph
- Front-load important information

### Consistency
- Same term for same concept (don't alternate "user" and "customer")
- Same formatting for same elements (all code in backticks)
- Same voice throughout (active preferred for instructions)

### Accessibility
- Alt text for all images
- Don't rely on color alone (add labels or patterns)
- Use descriptive link text (not "click here")
- Tables with headers for screen readers

### Code Examples
- Complete, copy-paste runnable snippets
- Include expected output as comments
- Show error handling for non-trivial examples
- Update examples when API changes

## Information Architecture

### Diátaxis Framework
Structure docs by user need, not by feature:

| Type | User Need | Example |
|---|---|---|
| Tutorials | Learning by doing | "Build your first app" |
| How-to guides | Solving a problem | "Deploy to production" |
| Reference | Understanding details | API docs, CLI reference |
| Explanation | Understanding concepts | "How authentication works" |

### Doc Site Structure
```
Getting Started/
  Installation
  Quick Start
  Configuration
Tutorials/
  Tutorial 1
  Tutorial 2
How-To Guides/
  Deploy
  Migrate
  Troubleshoot
Reference/
  API
  CLI
  Configuration
Explanation/
  Architecture
  Security
  Performance
```

## Review Rubric

| Criterion | Excellent (5) | Poor (1) |
|---|---|---|
| Accuracy | Verified by SME, code tested | Contains factual errors |
| Clarity | Skimmable, jargon explained | Dense, ambiguous, undefined terms |
| Completeness | Covers all edge cases | Missing critical steps or context |
| Usability | Examples work, links valid | Broken examples, dead links |
| Findability | Properly tagged, cross-linked | Orphan page, no navigation |

## Common Anti-Patterns

| Anti-Pattern | Fix |
|---|---|
| "Simply" / "Just" / "Obviously" | Remove; implies the task is trivial |
| Future tense for instructions | Use imperative: "Click Save" not "You will click Save" |
| Wall of text | Break into lists, tables, or steps |
| Missing prerequisites | Add "Before you begin" section |
| Docs that just describe UI | Explain what to do and why |
| Screenshots without alt text | Add descriptive alt text |
| Version-specific without context | State version applicability |

## Localization Basics

- Write for translation: avoid idioms, slang, cultural references
- Leave space for text expansion (30% for some languages)
- Don't concatenate strings: "Click" + "Save" → "Click Save"
- Use ICU message format for pluralization and variables
- Provide context for translators in comments
