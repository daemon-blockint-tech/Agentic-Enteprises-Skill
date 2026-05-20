# Compute and serverless

## Table of contents

1. [VM and instance groups](#vm-and-instance-groups)
2. [Autoscaling](#autoscaling)
3. [Serverless](#serverless)
4. [Containers without full platform](#containers-without-full-platform)

## VM and instance groups

| Workload | Pattern |
|---|---|
| Steady state | Right-sized VM, reserved capacity if 12mo+ stable |
| Bursty | Autoscaling group / MIG / VMSS |
| Batch | Spot/preemptible with checkpointing |
| Licensed software | Dedicated hosts or BYOL rules — legal review |

Harden: IMDSv2 (AWS), metadata restrictions, patch cadence, no SSH from internet.

## Autoscaling

- Scale on **CPU, memory, custom metric**, or queue depth
- **Cooldown** and min/max bounds to prevent thrash
- **Health checks** tied to load balancer or managed group
- Load test before prod promotion — `performance-engineer` for app-level tests

## Serverless

| Service class | Examples | Watch |
|---|---|---|
| Functions | Lambda, Cloud Functions, Azure Functions | Timeout, concurrency, cold start |
| Containers | Fargate, Cloud Run, Container Apps | CPU/mem limits, VPC attachment |
| Orchestration | Step Functions, Workflows | State size, idempotency |

Design:

- **Idempotent** handlers; dead-letter queues
- **Secrets** from manager, not env in plain text
- **VPC** attach only when needed (adds cold start / complexity)

## Containers without full platform

- **ECS/EKS/GKE/AKS** service definitions when not doing cluster lifecycle → cluster ops in `cluster-deployment-engineer`
- Cloud engineer owns **service account IAM**, subnets, ALB/GLB fronting, and autoscaling policies at cloud API layer
