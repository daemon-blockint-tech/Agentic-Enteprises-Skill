# DevOps & Platform Engineering

## CI/CD Pipeline Design

### Pipeline Stages
```
Code Commit → Build → Unit Test → Integration Test → Security Scan → Deploy Staging → E2E Test → Deploy Prod → Verify
```

### Git Branching Strategies

| Strategy | Best For | Complexity |
|---|---|---|
| Trunk-based | Fast iterations, small teams | Low |
| GitHub Flow | Simple web apps | Low |
| GitLab Flow | Environment per branch | Medium |
| GitFlow | Released software with versions | High |

### Pipeline as Code Examples

**GitHub Actions:**
```yaml
name: CI/CD
on:
  push:
    branches: [main]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
      - run: npm ci
      - run: npm test
      - run: npm run build
  deploy:
    needs: build
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to AWS
        uses: aws-actions/configure-aws-credentials@v4
        with:
          role-to-assume: ${{ secrets.DEPLOY_ROLE_ARN }}
      - run: aws ecs update-service --cluster prod --service app --force-new-deployment
```

**GitLab CI:**
```yaml
stages: [build, test, deploy]

build:
  stage: build
  script: docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .

test:
  stage: test
  script: pytest
  coverage: '/TOTAL.+?([0-9]{1,3}%)/'

deploy_prod:
  stage: deploy
  script: helm upgrade --install app ./chart
  environment:
    name: production
  when: manual
```

## Containerization

### Dockerfile Best Practices
```dockerfile
# Multi-stage build
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production
COPY . .
RUN npm run build

FROM node:20-alpine
RUN apk add --no-cache dumb-init
USER node
WORKDIR /app
COPY --from=builder --chown=node:node /app/dist ./dist
COPY --from=builder --chown=node:node /app/node_modules ./node_modules
EXPOSE 3000
ENTRYPOINT ["dumb-init", "node", "dist/main.js"]
```

### Kubernetes Patterns

**Deployment with HPA:**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: app
  template:
    metadata:
      labels:
        app: app
    spec:
      containers:
        - name: app
          image: app:v1.2.0
          resources:
            requests:
              memory: "256Mi"
              cpu: "250m"
            limits:
              memory: "512Mi"
              cpu: "500m"
          livenessProbe:
            httpGet:
              path: /health
              port: 8080
            initialDelaySeconds: 10
            periodSeconds: 5
          readinessProbe:
            httpGet:
              path: /ready
              port: 8080
            initialDelaySeconds: 5
---
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: app-hpa
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: app
  minReplicas: 3
  maxReplicas: 10
  metrics:
    - type: Resource
      resource:
        name: cpu
        target:
          type: Utilization
          averageUtilization: 70
```

**ConfigMap + Secret:**
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  DB_HOST: "postgres"
  LOG_LEVEL: "info"
---
apiVersion: v1
kind: Secret
metadata:
  name: app-secrets
type: Opaque
stringData:
  DB_PASSWORD: "<encrypted>"
  API_KEY: "<encrypted>"
```

## Infrastructure as Code

### Terraform Patterns

**Module structure:**
```
modules/
├── vpc/
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
├── ecs/
├── rds/
└── s3/
```

**State management:**
- Use remote backend (S3 + DynamoDB, GCS, Azure Storage)
- Enable state locking
- Separate state per environment

**Workspace strategy:**
```bash
terraform workspace new prod
terraform workspace select prod
terraform apply -var-file=prod.tfvars
```

### Pulumi Example
```python
import pulumi
from pulumi_aws import s3

bucket = s3.Bucket("my-bucket",
    versioning=s3.BucketVersioningArgs(
        enabled=True
    ))

pulumi.export("bucket_name", bucket.id)
```

## GitOps

### ArgoCD Setup
```yaml
# Application manifest
apiVersion: argoproj.io/v1alpha1
kind: Application
metadata:
  name: my-app
  namespace: argocd
spec:
  project: default
  source:
    repoURL: https://github.com/org/gitops-repo
    targetRevision: HEAD
    path: overlays/production
  destination:
    server: https://kubernetes.default.svc
    namespace: production
  syncPolicy:
    automated:
      prune: true
      selfHeal: true
    syncOptions:
      - CreateNamespace=true
```

### Flux Setup
```yaml
apiVersion: source.toolkit.fluxcd.io/v1
kind: GitRepository
metadata:
  name: my-app
  namespace: flux-system
spec:
  interval: 1m
  url: https://github.com/org/gitops-repo
  ref:
    branch: main
---
apiVersion: kustomize.toolkit.fluxcd.io/v1
kind: Kustomization
metadata:
  name: my-app
  namespace: flux-system
spec:
  interval: 10m
  path: ./overlays/production
  prune: true
  sourceRef:
    kind: GitRepository
    name: my-app
```

## SRE Practices

### SLI / SLO / SLA

| Term | Definition | Example |
|---|---|---|
| SLI | Service Level Indicator | "Request latency < 200ms" |
| SLO | Service Level Objective | "99.9% of requests < 200ms" |
| SLA | Service Level Agreement | "< 0.1% downtime or credit" |

### Error Budget
```
Error Budget = 100% - SLO

Example: SLO = 99.9% → Error Budget = 0.1% = 43.8 min/month

Policy: If error budget is consumed, freeze feature launches until recovered.
```

### Toil Reduction
- Automate repeated manual tasks
- Self-service platforms for developers
- Standardized templates and modules
- Target: <50% of time on toil

## Monitoring & Alerting

### Metrics Stack

| Component | Open Source | Commercial |
|---|---|---|
| Collection | Prometheus, Telegraf | Datadog Agent, Splunk UF |
| Storage | Prometheus TSDB, Thanos, Cortex | Datadog, New Relic |
| Visualization | Grafana | Datadog, New Relic |
| Alerting | Alertmanager | PagerDuty, Opsgenie |

### Key Metrics

| Category | Metric | Alert |
|---|---|---|
| Latency | p50, p95, p99 response time | p95 > 500ms |
| Traffic | Requests per second | Drop > 50% |
| Errors | Error rate | > 0.1% for 5 min |
| Saturation | CPU, memory, disk, connections | > 80% |

### Alerting Rules
```yaml
# Prometheus alert rule
groups:
  - name: app_alerts
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m]) / rate(http_requests_total[5m]) > 0.01
        for: 5m
        labels:
          severity: critical
        annotations:
          summary: "High error rate detected"
```

## Incident Response

### On-Call Setup
- Primary + secondary rotation
- Escalation: 15 min → 30 min → manager
- Runbook required for every alert
- Blameless post-mortems within 48 hours

### Post-Mortem Template
```markdown
## Incident [ID] — [Date]

### Summary
What happened in 2 sentences.

### Timeline
| Time | Event |
|---|---|
| 10:00 | Alert fired |
| 10:15 | On-call acknowledged |
| 10:30 | Mitigation applied |
| 11:00 | Service restored |

### Root Cause
5 Whys analysis.

### Impact
- Duration: 1 hour
- Affected users: ~500
- Data loss: None

### Action Items
| Action | Owner | Due |
|---|---|---|
| Fix X | @alice | Friday |
| Add monitoring for Y | @bob | Next week |
```
