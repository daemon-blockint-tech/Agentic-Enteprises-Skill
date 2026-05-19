# Identifier Reputation Analysis

## Technique Coverage

| D3FEND Technique | Description |
|---|---|
| Identifier Analysis | General ID inspection |
| Homoglyph Detection | Unicode spoofing detection |
| Identifier Activity Analysis | Behavioral tracking |
| Identifier Reputation Analysis | Score reputation |
| Domain Name Reputation Analysis | Domain risk scoring |
| File Hash Reputation Analysis | Hash lookup |
| IP Reputation Analysis | IP risk scoring |
| URL Reputation Analysis | URL risk scoring |
| URL Analysis | Deep URL inspection |

## Reputation Sources

| Type | Sources | Query Method |
|---|---|---|
| IP | VirusTotal, AbuseIPDB, Tor lists | API lookup |
| Domain | VirusTotal, URLVoid, Google Safe Browsing | API + DNS |
| File Hash | VirusTotal, NSRL, local DB | Hash lookup |
| URL | URLScan, PhishTank, OpenPhish | Full URL analysis |
| Sender | SPF, DKIM, DMARC, SenderBase | Email headers |

## Homoglyph Detection

```python
# Detect unicode spoofing
def detect_homoglyphs(domain):
    confusables = {
        'а': 'a',  # Cyrillic а vs Latin a
        'е': 'e',
        'о': 'o',
    }
    # Normalize and compare
```

## Scoring

| Score | Action |
|---|---|
| 0-30 | Clean, allow |
| 31-70 | Suspicious, flag for review |
| 71-100 | Malicious, block |

## Integration

- DNS firewalls: block known malicious domains
- Email gateways: reject known bad senders
- Web proxies: block malicious URLs
- EDR: alert on known bad file hashes
