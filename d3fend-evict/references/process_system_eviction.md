# Process & System Eviction

## Technique Coverage

| D3FEND Technique | Description |
|---|---|
| Process Eviction | Remove malicious processes |
| Host Shutdown | Emergency shutdown |
| Host Reboot | Restart system |
| Process Suspension | Pause process |
| Process Termination | Kill process |
| Session Termination | End user session |

## Process Eviction

### Suspension vs Termination

| Action | Use Case | Benefit |
|---|---|---|
| Suspend | Need to analyze process | Preserve memory for forensics |
| Terminate | Confirmed malicious | Immediate containment |

### Termination Methods

```
Graceful: SIGTERM, service stop
Forceful: SIGKILL, taskkill /F
Kernel: Delete process object
Remote: EDR kill command
```

## Session Termination

| Session Type | Termination Method |
|---|---|
| RDP | Log off user, disconnect session |
| SSH | Kill PTY, revoke authorized_keys |
| Web | Invalidate cookie/token |
| VPN | Disconnect from concentrator |
| Application | Revoke app-specific token |

## System Eviction

### Shutdown
- Immediate: Cut power (last resort)
- Graceful: `shutdown /s /t 0`
- Network: Isolate first, then shutdown

### Reboot
- Use for: Clearing memory-resident malware
- Risk: Persistent malware restarts
- Combine with: Boot from clean media

## Coordination

1. Identify all malicious processes
2. Document parent-child relationships
3. Terminate in dependency order (children first)
4. Verify termination (process not respawning)
5. Check for persistence mechanisms
6. Verify system stability after eviction
