# Networking and ingress

## Table of contents

1. [Services](#services)
2. [Ingress and Gateway API](#ingress-and-gateway-api)
3. [NetworkPolicy](#networkpolicy)

## Services

| Type | Use |
|---|---|
| ClusterIP | Default in-cluster |
| Headless | StatefulSets, custom discovery |
| LoadBalancer | Cloud LB when no shared ingress |

Verify: `kubectl get endpointslices -n <ns>` matches pod IPs.

## Ingress and Gateway API

- One ingress class per environment (e.g. `nginx`, `alb`)
- TLS: cert-manager Certificate + issuer; or cloud-managed certs
- Annotate timeouts and body size for long uploads

Debug path: DNS → LB → ingress controller → Service → Pod.

## NetworkPolicy

Start **default-deny** in namespace, then allow:

- Ingress from ingress controller namespace
- Egress to DNS (kube-system), APIs, databases on known ports

Label selectors must match pod templates exactly—typos cause silent drops.

Service mesh adds mTLS and traffic policy; adopt only with platform team (`platform-engineer`).
