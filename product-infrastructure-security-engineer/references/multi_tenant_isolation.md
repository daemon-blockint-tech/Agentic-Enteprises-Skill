# Multi-tenant isolation

## Table of contents

1. [Patterns](#patterns)
2. [Tenant context](#tenant-context)
3. [Isolation tests](#isolation-tests)

## Patterns

| Pattern | Isolation strength | Cost |
|---|---|---|
| Shared DB + tenant_id column + RLS | Good if enforced in DB and app | Low |
| Schema per tenant | Stronger | Medium |
| DB/cluster per tenant (cells) | Strongest | High |
| Shared K8s + network policy per ns | Depends on policy rigor | Medium |

Pick tiered model: standard on shared; enterprise on dedicated cell.

## Tenant context

- Resolve tenant from authenticated identity, not from unvalidated body fields
- Propagate `tenant_id` in internal RPC metadata
- Reject missing tenant context at data layer (fail closed)

## Isolation tests

Automate in CI:

- Cross-tenant read/write negative tests for every resource API
- Fuzz tenant ID in paths and headers
- Chaos: wrong tenant in async job payload must not process
