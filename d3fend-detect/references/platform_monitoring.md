# Platform & Physical Monitoring

## Technique Coverage

| D3FEND Technique | Description |
|---|---|
| Physical Access Monitoring | Physical security |
| Electronic Lock Monitoring | Badge/lock tracking |
| Motion Sensor Monitoring | Motion detection |
| Proximity Sensor Monitoring | Proximity alerts |
| Video Surveillance | Camera monitoring |
| Platform Monitoring | System monitoring |
| Application Performance Monitoring | App health |
| Application Exception Monitoring | Error tracking |
| File Integrity Monitoring | FIM |
| Firmware Behavior Analysis | Firmware monitoring |
| Firmware Embedded Monitoring Code | Embedded monitors |
| Firmware Verification | Firmware validation |
| Operating Mode Monitoring | Mode/state tracking |
| Operating System Monitoring | OS health |
| Endpoint Health Beacon | Device heartbeat |
| Input Device Analysis | Peripheral monitoring |
| Memory Boundary Tracking | Memory monitoring |
| Scheduled Job Analysis | Job monitoring |
| System Daemon Monitoring | Service monitoring |
| System File Analysis | System file checks |

## Platform Monitoring Stack

| Layer | What | Tool Examples |
|---|---|---|
| Application | Errors, performance, logs | Datadog, New Relic, Sentry |
| OS | Processes, services, events | OSQuery, Sysmon, Auditd |
| Firmware | Integrity, behavior | TPM, vendor tools |
| File | Integrity, changes | Tripwire, AIDE, OSQuery |
| Network | Traffic, connections | Zeek, Suricata |

## File Integrity Monitoring

```
Baseline: Known-good file hashes
Frequency: Real-time or periodic
Alerts: Unexpected changes, new files, deletions
Scope: Critical system files, configs, executables
```

## Physical Security

| Control | Purpose |
|---|---|
| Badge readers | Access logging |
| Motion sensors | After-hours detection |
| Cameras | Visual verification |
| Proximity sensors | Tailgating detection |
| Mantraps | Controlled entry |

## Firmware Monitoring

- Boot integrity measurement (TPM)
- Runtime behavior analysis
- Update verification (signed updates)
- Embedded monitoring code
