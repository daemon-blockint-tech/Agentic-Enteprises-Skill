# Network Traffic Analysis

## Technique Coverage

| D3FEND Technique | Description |
|---|---|
| Network Traffic Analysis | General traffic inspection |
| Administrative Network Activity Analysis | Admin traffic monitoring |
| Application Protocol Command Analysis | Protocol-specific |
| Remote Firmware Update Monitoring | FW update tracking |
| Byte Sequence Emulation | Payload emulation |
| Certificate Analysis | TLS cert inspection |
| Active Certificate Analysis | Active probing |
| Passive Certificate Analysis | Passive observation |
| Client-server Payload Profiling | Payload analysis |
| Connection Attempt Analysis | Connection tracking |
| DNS Traffic Analysis | DNS monitoring |
| File Carving | Extract files from traffic |
| Inbound Session Volume Analysis | Volume anomalies |
| IPC Traffic Analysis | Inter-process communication |
| Network Traffic Community Deviation | Peer comparison |
| Network Traffic Signature Analysis | Signature matching |
| Per Host Download-Upload Ratio Analysis | Ratio analysis |
| Protocol Metadata Anomaly Detection | Metadata anomalies |
| Relay Pattern Analysis | Proxy/Relay detection |
| Remote Terminal Session Detection | RDP/SSH detection |
| RPC Traffic Analysis | Remote procedure call |

## Detection Methods

### Signature-based
```
SNORT/Suricata rules for known threats
YARA over network payloads
Custom IDS rules for IOCs
```

### Anomaly-based
```
Baseline: normal traffic patterns per host/subnet
Deviation: unusual volume, protocols, destinations
Machine learning: auto-encoder, clustering
```

### Protocol Analysis
```
DNS: DGA detection, tunneling, unusual queries
HTTP: C2 beaconing, data exfiltration
TLS: JA3 fingerprinting, SNI analysis
SMB: lateral movement, suspicious shares
```

## Tools
- Zeek, Suricata, Snort
- Wireshark, tshark
- Arkime (Moloch), Corelight
- Vectra, Darktrace
