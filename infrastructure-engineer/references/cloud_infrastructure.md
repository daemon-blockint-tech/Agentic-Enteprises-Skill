# Cloud Infrastructure

## VPC / VNet Design

### Multi-AZ Architecture
```
VPC (10.0.0.0/16)
├── Public Subnet A (10.0.1.0/24) — AZ-a
│   ├── ALB/NLB
│   ├── NAT Gateway A
│   └── Bastion host
├── Public Subnet B (10.0.2.0/24) — AZ-b
│   └── NAT Gateway B
├── Private Subnet A (10.0.3.0/24) — AZ-a
│   ├── App tier (ECS/EKS/EC2)
│   └── RDS read replica
├── Private Subnet B (10.0.4.0/24) — AZ-b
│   ├── App tier
│   └── RDS primary
└── Database Subnet (10.0.5.0/24) — AZ-a,b
    └── RDS, ElastiCache, MSK
```

### Traffic Flow Patterns

| Flow | Components |
|---|---|
| Internet → App | CloudFront/WAF → ALB → App in private subnet |
| App → Internet | Private subnet → NAT Gateway → Internet |
| Cross-VPC | VPC Peering or Transit Gateway |
| On-prem → Cloud | VPN or Direct Connect/ExpressRoute |
| SaaS → Private | VPC PrivateLink / Private Service Connect |

## Compute

### AWS

| Service | Use Case | When Not to Use |
|---|---|---|
| EC2 | Full control, lift-and-shift | Want serverless simplicity |
| ECS | Docker containers, AWS-native | Need K8s ecosystem |
| EKS | K8s, multi-cloud portability | Simple container needs |
| Fargate | Serverless containers | Need host access |
| Lambda | Event-driven, <15 min | Long-running, stateful |
| Batch | HPC, scheduled jobs | Real-time workloads |

### GCP

| Service | Use Case |
|---|---|
| Compute Engine | VMs, disks, GPUs |
| GKE | Managed K8s |
| Cloud Run | Serverless containers |
| Cloud Functions | Event-driven functions |
| Cloud Batch | HPC workloads |

### Azure

| Service | Use Case |
|---|---|
| VMs | IaaS workloads |
| AKS | Managed K8s |
| Container Instances | Simple containers |
| Functions | Event-driven |
| App Service | Web apps, APIs |

## Storage

### Object Storage

| Feature | AWS S3 | GCS | Azure Blob |
|---|---|---|---|
| Storage classes | Standard, IA, Glacier, Glacier Deep | Standard, Nearline, Coldline, Archive | Hot, Cool, Archive |
| Lifecycle policies | Yes | Yes | Yes |
| Versioning | Yes | Yes | Yes |
| Cross-region replication | Yes (CRR) | Yes (dual-region, multi-region) | Yes (GRS, GZRS) |
| Event notifications | S3 Events | Pub/Sub notifications | Event Grid |

### Block Storage

| Use Case | AWS | GCP | Azure |
|---|---|---|---|
| Boot volumes | EBS (gp3, io2) | Persistent Disk (pd-ssd, pd-balanced) | Managed Disks (Premium SSD) |
| Shared storage | EFS | Filestore | Azure Files |
| High performance | io2 Block Express | Hyperdisk | Ultra Disk |

## IAM & Identity

### AWS IAM Best Practices
- Use IAM roles, not long-term access keys
- Apply least privilege with conditions
- Enable MFA for console access
- Use service-linked roles where available
- Regular access review (quarterly)

### Cross-Cloud Identity
- **OIDC**: Federate identity across clouds (e.g., GitHub Actions → AWS via OIDC)
- **Azure AD / Google Workspace**: SSO across SaaS and cloud
- **HashiCorp Vault**: Dynamic secrets across clouds

### Policy Structure
```json
{
  "Version": "2012-10-17",
  "Statement": [{
    "Effect": "Allow",
    "Action": ["s3:GetObject"],
    "Resource": "arn:aws:s3:::my-bucket/*",
    "Condition": {
      "StringEquals": {"aws:RequestedRegion": "us-east-1"},
      "Bool": {"aws:MultiFactorAuthPresent": "true"}
    }
  }]
}
```

## Networking

### Load Balancers

| Type | Layer | Use Case |
|---|---|---|
| Application (ALB/GLB/Azure ALB) | L7 | HTTP/HTTPS, path-based routing |
| Network (NLB) | L4 | TCP/UDP, high throughput, static IP |
| Classic (CLB) | L4/L7 | Legacy, avoid for new |
| Global (GCLB / Azure Front Door) | L7 | Multi-region, anycast |

### DNS & Traffic Management
- Route 53: Weighted, latency-based, geo, failover routing
- Cloud DNS: Global anycast, low TTL for failover
- Azure DNS: Integrated with Traffic Manager

### CDN
- CloudFront: Edge caching, signed URLs, origin shield
- Cloud CDN: GCP-native, integrates with GCLB
- Azure CDN / Front Door: Rules engine, WAF

## Serverless Patterns

### Event-Driven Architecture
```
Event Source → Event Bus → Lambda/Function → Target
```

**Event sources:**
- S3, DynamoDB Streams, Kinesis, SNS, SQS, EventBridge
- API Gateway, ALB, CloudWatch Events
- Third-party SaaS (via EventBridge)

### Cold Start Mitigation
- Provisioned concurrency (Lambda)
- Minimum instances (Cloud Run)
- Always-ready plans (Azure Functions Premium)
- Keep-alive pings (less reliable)

## Cost Optimization

| Technique | Savings | Applies To |
|---|---|---|
| Reserved Instances / CUDs | 30-70% | Steady-state compute |
| Savings Plans | Flexible commitment | AWS compute |
| Spot / Preemptible | 60-90% | Fault-tolerant workloads |
| Storage tiering | 50-80% | Infrequently accessed data |
| Auto-shutdown | 20-40% | Dev/test environments |
| Right-sizing | 10-30% | Over-provisioned resources |

## Disaster Recovery

### RTO/RPO Targets by Tier

| Tier | RTO | RPO | Pattern |
|---|---|---|---|
| Tier 1 | <1 hour | 0 | Active-active multi-region |
| Tier 2 | <4 hours | <1 hour | Pilot light + auto-failover |
| Tier 3 | <24 hours | <24 hours | Warm standby |
| Tier 4 | <72 hours | <7 days | Backup + restore |

### Multi-Region Patterns
- **Read replica**: Async replication, promote on failover
- **Global database**: Aurora Global, Cosmos DB, Spanner
- **Active-active**: Multi-master writes, conflict resolution needed
