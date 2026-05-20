# Scoping, Rules of Engagement, and OPSEC

## Authorization (mandatory)

1. Obtain **written authorization** (SOW, letter, or signed ROE) before any activity
2. Record approver name, date, validity window, and scope identifiers
3. Confirm **emergency stop** contact and procedure with client/security operations
4. If scope is unclear, **stop** and clarify—do not probe adjacent assets

## ROE checklist

| Item | Document |
|---|---|
| In-scope assets | Hostnames, IPs, CIDRs, cloud accounts, apps, identities |
| Out-of-scope | Third parties, prod customer data, physical, social eng (unless approved) |
| Allowed methods | Phishing, C2, credential spray, exploit, data exfil simulation |
| Prohibited | DoS, ransomware deploy, destructive actions, real data theft |
| Impact limits | Max accounts compromised, max hosts, data volume for exfil test |
| Windows | UTC start/end, maintenance blackouts |
| Notification | Who is informed (SOC, CISO), blind vs purple visibility |
| Evidence handling | Storage, encryption, retention, destruction date |
| Legal | Jurisdiction, data protection, contractor constraints |

## OPSEC principles

- **Minimize attribution** to red team infrastructure when stealth is required
- Use dedicated redirectors, domains, and hosting per ROE—not personal assets
- Segregate operator accounts, keys, and logs from production admin paths
- Avoid storing client secrets on unsecured endpoints; use encrypted vaults
- Coordinate **blocklist / allowlist** with blue team to prevent accidental IR escalation
- Plan **deconfliction** identifiers (canary accounts, DNS names, file markers)

## Communication

| Mode | When |
|---|---|
| **Blind** | SOC exercises realism; limited pre-brief |
| **Purple** | Pre-agreed observers; real-time or end-of-day sync |
| **White card** | Pause for safety or scope questions |

Document cadence: kickoff, mid-campaign check-in, hotwash, final readout.

## Emergency stop

On stop signal (client or lead):

1. Cease all active operations immediately
2. Notify operators and blue team per ROE
3. Preserve logs per evidence policy; do not delete without approval
4. Document stop reason and residual access for cleanup

## Safe testing defaults

- Prefer **non-production** or designated test tenants when available
- Use synthetic data for exfil demonstrations
- Remove persistence, scheduled tasks, and test accounts before closeout
- Validate cleanup with blue team or asset owner
