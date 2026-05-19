# Deception Program

## Program Design

### Objectives

| Objective | Metric |
|---|---|
| Detection | Time to detect intrusion |
| Intelligence | TTPs collected per incident |
| Delay | Time attacker spends on decoys |
| Deterrence | Reduction in attack attempts |

### Deception Layers

```
Layer 1: Decoy environment (honeynet)
Layer 2: Decoy objects (files, credentials)
Layer 3: Decoy personas (fake users)
Layer 4: Decoy indicators (fake data in recon)
```

### Believability

- Match naming conventions of real assets
- Include realistic data (synthetic, not real)
- Maintain consistent backstory
- Update decoys to match environment changes

### Monitoring & Collection

| Interaction | What to Log | Retention |
|---|---|---|
| File access | User, timestamp, action | 1 year |
| Login attempt | Source IP, credentials tried | 1 year |
| Network connection | Protocol, data exchanged | 1 year |
| Command execution | Full session transcript | 1 year |

### Legal Considerations

- Employee monitoring disclosure
- Data privacy laws (GDPR, CCPA)
- No entrapment beyond scope
- Clear authorization and policy

## Integration with Incident Response

1. Deception alert triggers
2. Validate not false positive
3. Initiate incident response
4. Collect intelligence from decoy
5. Contain and evict from real systems
6. Update deception based on learnings
