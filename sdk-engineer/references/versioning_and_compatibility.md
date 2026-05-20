# Versioning and Compatibility

## Two axes

| Axis | Examples | Who owns |
|---|---|---|
| **API version** | `/v1/`, header `Api-Version`, package `v2` | API team |
| **SDK semver** | npm `2.3.1`, PyPI `1.8.0` | SDK team |

Document mapping: “SDK 2.x supports API v1 and v2; SDK 3.x drops API v1.”

## Semantic versioning (SDK)

- **MAJOR**: breaking public API (removed method, renamed type, behavior change)
- **MINOR**: additive (new resource, optional field, new optional parameter)
- **PATCH**: bug fixes, internal retries, docs—no signature breaks

Pre-1.0 SDKs may use `0.y.z` with explicit instability note.

## API breaking change policy

Coordinate with API owners:

| API change | SDK action |
|---|---|
| New optional response field | Minor SDK release; ignore in older clients |
| New required request field | Major SDK + migration guide |
| Renamed field | Major; alias deprecated name for one minor if policy allows |
| Removed endpoint | Major; keep stub throwing `DeprecationError` one minor optional |
| Enum value added | Minor if clients tolerate unknown values |

## Deprecation in client code

1. Mark APIs `@deprecated` / docstring / annotation per language
2. Emit runtime warning on use (configurable `warnings` / logger)
3. Link replacement in warning message
4. Remove in next major with CHANGELOG entry

### HTTP deprecation signals

Honor when present:

- `Deprecation: true` header
- `Sunset` header (RFC 8594)
- OpenAPI `deprecated: true`

Surface in release notes automation when spec scanned in CI.

## Multi-language parity matrix

Maintain a table in SDK repo:

| Feature | TS | Python | Go | Java |
|---|---|---|---|---|
| OAuth refresh | ✓ | ✓ | ✓ | ✓ |
| Streaming RPC | ✓ | ✓ | ✓ | planned |
| Idempotency keys | ✓ | ✓ | ✓ | ✓ |

**Parity rule:** same semantics; release minors on staggered schedule acceptable with documented lag.

## Codegen vs hand layer versioning

- Pin codegen to spec git SHA
- Tag generated code `DO NOT EDIT`
- Hand layer semver covers public exports only
- Regenerate on spec bump in dedicated PR for reviewability

## Compatibility testing

- Test matrix: last N API versions in sandbox (or mock servers per version)
- Record **minimum** API version in SDK README
- Fail CI if spec introduces breaking change without major SDK bump label on PR

## Release process

1. Update CHANGELOG (Keep a Changelog format)
2. Bump version in all package manifests
3. Run contract + integration tests
4. Publish to registries; tag git
5. Post migration guide for majors

## Consumer migration guide template

```markdown
## Upgrading from 1.x to 2.x

### Breaking changes
- `Client.create_user` renamed to `Client.users.create`
- `amount` now integer minor units (was decimal string)

### Steps
1. Bump dependency to `^2.0.0`
2. Replace ...
3. Run integration tests against sandbox

### Timeline
- API v1 sunset: 2026-12-01
- SDK 1.x support ends: 2026-09-01
```

## Long-term support

Define policy:

- Support last **two** SDK majors with security patches
- Backport critical auth fixes to previous major when feasible
- No indefinite support for deprecated API versions

## Anti-patterns

- Coupling SDK major bump to every server deploy
- Silent behavior change in patch release
- Removing deprecated APIs without sunset period documented on server
- Divergent error codes across languages for same server response
