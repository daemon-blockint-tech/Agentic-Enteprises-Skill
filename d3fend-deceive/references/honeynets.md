# Honeynets

## Technique Coverage

| D3FEND Technique | Description |
|---|---|
| Decoy Environment | General decoy infrastructure |
| Connected Honeynet | Linked to production |
| Integrated Honeynet | Blended with real systems |
| Standalone Honeynet | Isolated research network |

## Honeynet Types

### Standalone
- Completely isolated network
- No connection to production
- Purpose: Research, threat intelligence
- Risk: None to production
- Tools: Honeyd, Modern Honey Network (MHN)

### Integrated
- Decoy systems mixed with production
- Appears as legitimate infrastructure
- Purpose: Detect lateral movement
- Risk: Low (properly isolated)
- Tools: Canary tokens, Thinkst

### Connected
- Bridge between honeynet and production
- Monitored path for attacker observation
- Purpose: TTP collection, early warning
- Risk: Managed through strict controls

## Deployment Checklist

- [ ] Define objectives (detection, intelligence, delay)
- [ ] Select honeynet type based on risk tolerance
- [ ] Ensure no production data on decoy systems
- [ ] Monitor all honeynet traffic and interactions
- [ ] Establish alerting for any honeynet access
- [ ] Plan legal/HR coordination if employee accesses
- [ ] Document and review findings regularly

## Tools
- T-Pot: Multi-honeypot platform
- Cowrie: SSH/Telnet honeypot
- Dionaea: Malware capture honeypot
- Conpot: Industrial control honeypot
- Canary tokens: File and credential bait
