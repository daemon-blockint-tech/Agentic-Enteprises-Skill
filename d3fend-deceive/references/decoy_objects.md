# Decoy Objects

## Technique Coverage

| D3FEND Technique | Description |
|---|---|
| Decoy Object | General decoy items |
| Decoy File | Fake document files |
| Decoy Network Resource | Fake network shares/services |
| Decoy Persona | Fake user accounts |
| Decoy Public Release | Fake leaked credentials |
| Decoy Session Token | Bait cookies/tokens |
| Decoy User Credential | Fake login credentials |

## Decoy Types

### Decoy Files
- Fake documents with tracking (canary tokens)
- Planted in likely attacker targets
- Alert on open/access
- Example: `salaries_2025.xlsx` with embedded tracker

### Decoy Network Resources
- Fake SMB shares: `\\fileserver\finance$
- Fake database with fake PII
- Fake admin panels with logging
- Alert on any interaction

### Decoy Personas
- Fake Active Directory accounts
- Fake email mailboxes
- Appear as high-value targets
- Monitor login attempts and email access

### Decoy Credentials
- Honey passwords for password spraying detection
- Fake API keys planted in code repositories
- Fake session tokens in browser storage
- Alert on usage attempt

### Decoy Public Releases
- Fake credentials posted to dark web/pastebin
- Track if attackers attempt to use them
- Identify compromised infrastructure

## Implementation

| Decoy Type | Deployment | Alert Trigger |
|---|---|---|
| Files | User directories, file shares | File open, hash read |
| Credentials | Code repos, config files | Login attempt |
| Tokens | Cookies, localStorage | API call with token |
| Personas | AD, email | Login, email access |
| Resources | Network shares, DBs | Connection attempt |

## Tools
- Thinkst Canary: Physical and virtual canaries
- Canarytokens.org: Free token generation
- Custom: Honey accounts, fake databases
