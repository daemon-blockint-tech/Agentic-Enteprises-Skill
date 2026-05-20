# SDK Testing and Documentation

## Testing pyramid for SDKs

| Layer | Purpose | Tools / patterns |
|---|---|---|
| Unit | Parsing, pagination logic, error mapping, signing | mocks, fixtures |
| Contract | Request/response match spec examples | OpenAPI examples, Dredd, Prism, schemathesis |
| Integration | Live or sandbox API | ephemeral creds, VCR cassettes |
| E2E (optional) | Published package smoke test | install from registry tarball |

## Contract tests

### Goals

- Prove SDK builds requests the server expects (paths, headers, bodies)
- Prove SDK parses documented success and error responses

### Practices

1. Pull **official examples** from OpenAPI `examples` or docs site
2. For each operation: golden file → expected HTTP wire dump
3. Run without network using mock transport recording exact bytes
4. Fail CI when spec revision changes without updating fixtures

### OpenAPI tooling

- Validate spec with spectral or openapi-diff on PR
- Optional: generate tests from spec (`openapi-generator` test templates)
- Keep generated tests in `contract/` directory separate from hand unit tests

## Integration tests

- Use **sandbox** base URL and scoped API keys in CI secrets
- Rate-limit aware: serialize tests or use dedicated tenant
- Clean up created resources or use idempotent test names (`test-{uuid}`)
- Skip integration job on fork PRs without secrets (document in CONTRIBUTING)

### VCR / fixtures

- Record once; redact tokens and PII
- Pin cassette to spec version
- Re-record script documented in `scripts/refresh-cassettes.sh` only if team allows scripts

## Mock server

- Prism or WireMock from OpenAPI for local dev
- Document `make mock` for contributors
- Do not rely on mock for behaviors undocumented in spec

## Documentation alignment

SDK docs must **mirror** API reference sections:

| API reference section | SDK doc |
|---|---|
| Authentication | `## Authentication` + code sample |
| Rate limits | Defaults + `RateLimitError` |
| Pagination | Iterator example per list resource |
| Errors | Table of codes → exception types |
| Changelog / deprecations | SDK CHANGELOG links to API changelog |

### Quickstart structure

1. Install package (copy-paste command per registry)
2. Obtain credentials (link to dashboard; env var names)
3. Minimal working call (list or get)
4. Next steps: pagination, error handling, webhooks (if applicable)

### Examples directory

- `examples/` runnable in CI (`npm test` runs example compile)
- One file per common task: create, list, delete, webhook verify
- No secrets in repo; use env vars

## Reference documentation

- Auto-generate API reference from docstrings (JSDoc, Sphinx, godoc, javadoc)
- Publish to docs site with version selector matching SDK tags
- Cross-link to canonical HTTP API docs for field semantics

## Style and consistency

- Align terminology with `tech-writer-researcher` style guides when org has one
- Use same error code strings as server (`invalid_request`, not `InvalidRequest`)
- Code samples tested in CI (markdown-exec or dedicated test runner)

## Security in docs

- Never print live keys in README
- Document least-privilege scopes
- Warn against committing `.env` files; provide `.env.example`

## Release documentation

Each release includes:

- Version number and date
- Added / changed / deprecated / removed (public API)
- Spec version or git SHA supported
- Migration notes for majors

## Quality gates (pre-publish)

- [ ] Unit + contract tests green
- [ ] Linter + formatter applied per language
- [ ] CHANGELOG entry
- [ ] README quickstart verified manually or via smoke job
- [ ] No known CVEs in dependencies (audit job)
- [ ] Package size within budget (optional alert for JS bundles)

## Handoff to `build-validator`

Before large SDK rewrites, optional review packet:

- Public API diff (semver impact)
- Breaking changes list
- Test coverage on contract fixtures
- Rollback plan (yank package version policy)

## Metrics

Track:

- Time-to-first-successful-call (sandbox)
- Support tickets tagged `sdk`
- Download/version adoption curve
- Contract test failure rate on spec updates

Use metrics to prioritize ergonomic fixes over new surface area.
