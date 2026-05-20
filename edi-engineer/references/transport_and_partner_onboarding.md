# Transport and partner onboarding

## Table of contents

1. [Transport patterns](#transport-patterns)
2. [AS2 essentials](#as2-essentials)
3. [SFTP and file-based](#sftp-and-file-based)
4. [VAN and managed networks](#van-and-managed-networks)
5. [Certificates and secrets](#certificates-and-secrets)
6. [Partner onboarding phases](#partner-onboarding-phases)
7. [Certification and cutover](#certification-and-cutover)
8. [Partner profile schema](#partner-profile-schema)

## Transport patterns

| Pattern | When used | Integration notes |
|---|---|---|
| **AS2** | High-volume retail, manufacturing, healthcare | HTTPS, signing, encryption, MDN |
| **SFTP/FTP** | Batch file drop, 3PL, smaller partners | Polling, file naming conventions, ack files |
| **VAN** | Legacy hub, multi-partner mailbox | Mailbox ID, interchange routing, billing |
| **API wrapper** | Modern hubs translating to files | Still map to EDI processing pipeline |

EDI engineer owns **handoff to parser**—file or MIME body plus metadata (filename, AS2 Message-ID, received time).

## AS2 essentials

- **Endpoints** — separate URLs for test/prod; document IP allowlists if used
- **Signing / encryption** — partner cert, own cert, algorithm suite (SHA-256, AES-256)
- **MDN** — synchronous vs asynchronous; signed MDN expectations
- **Compression** — optional; verify partner support
- **Duplicate detection** — use AS2 Message-ID + payload hash

**Failure modes**

- Certificate expiry → proactive rotation calendar
- MDN timeout → retry policy; do not double-post business documents
- 413/oversize → split at functional group only when partner permits

## SFTP and file-based

Conventions to document per partner:

- **Directory layout** — `/inbound`, `/outbound`, `/archive`, `/error`
- **Naming** — `{partner}_{doctype}_{timestamp}_{control}.edi`
- **Encoding** — ASCII vs UTF-8; BOM handling
- **Completion signal** — `.done` file vs rename vs zero-byte trailer

Implement **atomic pickup** (rename to `.processing`) and virus scan hook if policy requires.

## VAN and managed networks

- **ISA IDs / UNB partners** — production vs test qualifiers
- **Mailbox / interconnect** — route tables maintained with VAN ops
- **Billing and traffic reports** — reconcile volume with internal metrics

Abstract VAN behind same **ingest service** as AS2/SFTP to reuse validation and mapping.

## Certificates and secrets

- Store private keys in **HSM or secrets manager**—not repos
- Track **expiry** 90/30/7 days; automate renewal where possible
- Maintain **trust stores** per partner; pin prod certs separately from test
- Rotate **SFTP keys** with parallel install window

Coordinate with `information-security-engineer` for cipher policy; do not weaken TLS for convenience.

## Partner onboarding phases

1. **Kickoff** — transaction sets, direction, volume, SLAs, contacts
2. **IG collection** — version, errata, sample files, code lists
3. **Profile build** — IDs, delimiters, transport, cert exchange
4. **Map development** — canonical maps + validation pack
5. **Unit test** — golden samples internal
6. **Certification** — partner test mailbox, scripted cases
7. **Parallel production** — shadow or dual-write with reconciliation
8. **Prod cutover** — freeze window, hypercare, rollback criteria

## Certification and cutover

**Certification checklist**

- [ ] All required transaction sets in/out
- [ ] Positive and negative scenarios signed by partner
- [ ] 997/CONTRL behavior verified
- [ ] Volume test (peak file size / count)
- [ ] Clock skew and timezone cases
- [ ] Duplicate interchange handling

**Cutover**

- Switch transport profile from test to prod IDs
- Run **reconciliation** on first 24–72 hours hourly
- Keep **rollback** — revert DNS/AS2 URL and replay from canonical backlog if needed

## Partner profile schema

Minimum fields:

```yaml
partnerId: ACME
standards:
  x12:
    version: "005010"
    isa:
      senderId: "SENDER"
      senderQual: "ZZ"
      receiverId: "RECEIVER"
      receiverQual: "ZZ"
transactions:
  - id: "850"
    direction: inbound
    mapVersion: "3.2.0"
transport:
  prod:
    type: as2
    url: https://...
    signingCert: ref://secrets/acme_sign
validation:
  ig: "ACME_850_IG_v4.pdf"
  snipProfile: retail_grocery_7.2
ack:
  generate997: true
  slaMinutes: 15
```

Version profile with application releases; support **per-partner feature flags** for gradual map rollout.
