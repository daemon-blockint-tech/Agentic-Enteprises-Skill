# Asset Security and Security Architecture (Domains 2–3)

## Table of contents

1. [Asset Security (Domain 2)](#asset-security-domain-2)
2. [Security Architecture and Engineering (Domain 3)](#security-architecture-and-engineering-domain-3)
3. [Cryptography themes](#cryptography-themes)
4. [Physical security themes](#physical-security-themes)
5. [Integration across domains](#integration-across-domains)

## Asset Security (Domain 2)

**Information lifecycle**: Create → use → store → share → archive → destroy.

| Activity | Security considerations |
|---|---|
| Classification | Labels drive handling rules |
| Ownership | Data owner approves access and sharing |
| Handling | Marking, encryption, clean desk, printing |
| Retention | Legal hold vs policy schedules |
| Disposal | Secure wipe, destruction certificates |

**Data states**: Data at rest, in transit, in use—controls differ (encryption, DLP, access, monitoring).

**Privacy-enhancing techniques** (concepts): minimization, pseudonymization, tokenization—implement with engineering and legal alignment.

**Asset inventory**: Hardware, software, data, people, services—feeds risk assessment and CMDB; automation is `information-security-engineer` / GRC evidence work.

## Security Architecture and Engineering (Domain 3)

**Secure design principles** (representative):

- Least privilege, separation of duties, defense in depth
- Fail secure, privacy by design, simplicity
- Zero trust (verify explicitly, least privilege, assume breach) as architectural direction

**Security models** (know conceptually):

| Model | Idea |
|---|---|
| Bell-LaPadula | Confidentiality-focused (no read up, no write down) |
| Biba | Integrity-focused |
| Clark-Wilson | Well-formed transactions, separation of duty |
| Brewer-Nash (Chinese Wall) | Conflict-of-interest separation |

**Evaluation criteria**: TCSEC, ITSEC, Common Criteria (EAL)—understand **assurance** and **target of evaluation** for procurement, not memorization of obsolete levels alone.

**Vulnerability categories** (architecture lens): design flaws, implementation bugs, operational misconfigurations—pair with Domain 6 testing programs.

## Cryptography themes

| Topic | CISSP-level understanding |
|---|---|
| Symmetric | Shared key; speed; key distribution challenge |
| Asymmetric | Key pairs; digital signatures, key exchange |
| Hash | Integrity; not encryption |
| Digital signature | Authenticity + integrity + non-repudiation (context-dependent) |
| PKI | CAs, certificates, revocation (CRL/OCSP) |
| Key management | Generation, storage, rotation, destruction |

**Common applications**: TLS, IPsec, S/MIME, disk encryption, code signing. Select algorithms and key lengths per organizational crypto standards and current guidance—implementation detail belongs with engineers.

## Physical security themes

- Site selection, facility design, perimeter controls
- Access badges, mantraps, CCTV, guards
- Environmental controls (HVAC, fire, power)
- Media handling and secure destruction in datacenters

Coordinate with facilities and datacenter teams; CBK framing sets requirements, operations executes.

## Integration across domains

| Topic | Domains |
|---|---|
| Data classification policy | 1, 2 |
| Encryption standard | 2, 3, 4 |
| Secure SDLC data handling | 2, 8 |
| Cloud shared responsibility | 2, 3, 4 |

When designing systems, produce **data flow diagrams** and **trust boundaries**—hand detailed patterns to `enterprise-security-architect`.
