# Security & Compliance

## Security Hardening

### Compute Hardening

**Linux (CIS Benchmarks):**
- Disable root SSH login
- Enforce password complexity (PAM)
- Configure AIDE for file integrity monitoring
- Enable auditd for system call logging
- Apply security updates within 30 days
- Disable unnecessary services

**Windows (CIS/Security Baselines):**
- Enable Windows Defender + ASR rules
- Configure AppLocker / WDAC
- Disable SMBv1, LLMNR, NetBIOS
- Enforce Credential Guard
- Apply Microsoft Security Baselines via GPO

**Containers:**
- Run as non-root user
- Read-only root filesystem
- Drop unnecessary capabilities
- No privileged containers in production
- Scan images for CVEs (Trivy, Clair, Snyk)
- Distroless or minimal base images

### Network Security

**VPC Security:**
- Default deny all inbound
- Explicit allow rules by service/port
- No 0.0.0.0/0 except for public-facing LB
- VPC Flow Logs for traffic analysis
- Private subnets for workloads

**DDoS Protection:**
- AWS Shield Advanced / Cloud Armor / Azure DDoS
- CDN for absorption
- Rate limiting at edge
- Anycast for distribution

## Identity & Access Management

### RBAC Design
```yaml
# Kubernetes RBAC example
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: app-developer
  namespace: app
rules:
  - apiGroups: [""]
    resources: ["pods", "services", "configmaps"]
    verbs: ["get", "list", "watch", "create", "update", "patch"]
  - apiGroups: ["apps"]
    resources: ["deployments"]
    verbs: ["get", "list", "watch", "update", "patch"]
```

### Zero Trust Principles
1. **Verify explicitly**: Authenticate and authorize every access request
2. **Least privilege**: Minimum permissions for minimum time
3. **Assume breach**: Micro-segmentation, continuous monitoring

### Secrets Management

| Tool | Best For | Deployment |
|---|---|---|
| HashiCorp Vault | Enterprise, dynamic secrets | Self-hosted or HCP |
| AWS Secrets Manager | AWS-native | Managed |
| Azure Key Vault | Azure-native | Managed |
| Google Secret Manager | GCP-native | Managed |
| Sealed Secrets / External Secrets | K8s GitOps | Open source |

**Vault policy example:**
```hcl
path "database/creds/app" {
  capabilities = ["read"]
}

path "secret/data/app/*" {
  capabilities = ["read"]
  allowed_parameters = {
    "environment" = ["prod", "staging"]
  }
}
```

## Vulnerability Management

### Scanning Pipeline
```
Source Code → SAST (Semgrep, SonarQube)
Dependencies → SCA (Snyk, Dependabot)
Container Image → Image Scan (Trivy, Clair)
Infrastructure → IaC Scan (Checkov, tfsec)
Runtime → RASP / CSPM (Wiz, Orca)
```

### Patch Management
| Severity | SLA | Process |
|---|---|---|
| Critical (CVSS 9.0+) | 24-48 hours | Emergency change |
| High (CVSS 7.0-8.9) | 7 days | Standard change |
| Medium (CVSS 4.0-6.9) | 30 days | Scheduled maintenance |
| Low (CVSS 0.1-3.9) | 90 days | Next update cycle |

## Compliance Frameworks

### SOC 2 Type II
**Trust Services Criteria:**
- CC1: Control environment
- CC2: Communication and information
- CC3: Risk assessment
- CC4: Monitoring activities
- CC5: Control activities
- CC6: Logical and physical access controls
- CC7: System operations
- CC8: Change management
- CC9: Risk mitigation

### ISO 27001
**Key domains:**
- Information security policies
- Organization of information security
- Human resource security
- Asset management
- Access control
- Cryptography
- Physical security
- Operations security
- Communications security
- System acquisition and development
- Supplier relationships
- Incident management
- Business continuity
- Compliance

### GDPR (if applicable)
- Data inventory and classification
- Privacy by design
- Consent management
- Right to erasure
- Data portability
- Breach notification (72 hours)
- DPO appointment (if required)

## Encryption

### At Rest
- **Database**: Transparent Data Encryption (TDE)
- **Storage**: AES-256-GCM (managed keys or customer-managed)
- **Backups**: Encrypted before leaving production
- **Key rotation**: Annual or on suspected compromise

### In Transit
- **TLS 1.3** minimum for all external traffic
- **mTLS** for service-to-service in zero-trust environments
- **Certificate management**: Auto-renewal, monitoring expiry

### Key Management
- Use cloud KMS or HashiCorp Vault
- Separate keys by environment
- Envelope encryption: DEK encrypted by KEK
- Audit all key usage

## Incident Response

### Security Incident Severity

| Level | Definition | Example |
|---|---|---|
| Critical | Active data breach, ransomware | Unauthorized access to production DB |
| High | Potential breach, active attack | Failed privilege escalation attempt |
| Medium | Policy violation, malware | Unapproved software installation |
| Low | Attempted attack, reconnaissance | Port scan from unknown IP |

### Response Playbook
1. **Contain**: Isolate affected systems
2. **Eradicate**: Remove threat actor access
3. **Recover**: Restore from clean backups
4. **Post-incident**: Forensics, lessons learned

## Compliance Automation

### Policy as Code
```hcl
# Terraform Sentinel / OPA Rego
package terraform.aws.security

deny[msg] {
  resource := input.resource_changes[_]
  resource.type == "aws_security_group"
  resource.change.after.ingress[_].cidr_blocks[_] == "0.0.0.0/0"
  msg := sprintf("Security group %s allows unrestricted ingress", [resource.name])
}
```

### Continuous Compliance
- Terraform plan scanning (Checkov, tfsec, terrascan)
- K8s admission controllers (OPA Gatekeeper, Kyverno)
- Cloud posture management (Wiz, Orca, Prisma Cloud)
- Scheduled compliance audits ( ScoutSuite, Prowler, Steampipe)

### Audit Evidence
- Maintain evidence repository (S3, SharePoint)
- Automate evidence collection where possible
- Review access logs quarterly
- Document exceptions with justification
