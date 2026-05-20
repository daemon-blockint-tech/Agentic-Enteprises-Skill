# Workload placement and service selection

## Table of contents

1. [Placement decision tree](#placement-decision-tree)
2. [Compute models](#compute-models)
3. [Data and integration](#data-and-integration)
4. [Selection matrix](#selection-matrix)

## Placement decision tree

1. **Regulatory residency** — limits regions and providers
2. **Latency** — user proximity, on-prem adjacency
3. **Team skills** — operational burden tolerance
4. **Cost horizon** — steady vs bursty, commitment appetite
5. **Exit** — contractual and technical portability

Document **why not** alternatives rejected.

## Compute models

| Model | When | Ops burden |
|---|---|---|
| Serverless functions | Event spikes, short jobs | Low |
| Managed containers (Fargate, Cloud Run) | Services without K8s ops | Medium |
| Kubernetes (managed) | Portable microservices, operators | High — `cluster-deployment-engineer` |
| VMs / instance groups | Legacy, licensed software | Medium–high |
| Bare metal / GPU nodes | ML training at scale — coordinate with `ml-systems-engineer-rl-engineering` |

## Data and integration

| Need | Cloud-native options |
|---|---|
| Relational OLTP | RDS, Cloud SQL, Azure SQL |
| Analytics | Warehouse (Snowflake, BigQuery, Redshift) — `data-architect` |
| Cache | ElastiCache, Memorystore |
| Events | EventBridge, Pub/Sub, Event Grid |
| API | API Gateway, Apigee, API Management |

Prefer **managed** unless latency, cost, or compliance blocks it.

## Selection matrix

Template columns:

| Option | NFR fit | Cost (3yr TCO) | Risk | Ops | Verdict |

Score 1–5 with weights agreed with stakeholders.

Include **pilot** scope before enterprise commit.
