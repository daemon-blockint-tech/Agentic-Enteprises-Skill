# Inference and serving platform

## Table of contents

1. [Topology](#topology)
2. [Model servers](#model-servers)
3. [Gateway responsibilities](#gateway-responsibilities)
4. [Scaling and health](#scaling-and-health)

## Topology

Typical production stack:

```
Client → API gateway → Inference gateway → [safeguard stages] → Model server(s) → [post-safeguards] → Client
```

Separate **control plane** (config, routing tables) from **data plane** (request handling).

Document ownership per box: team, on-call, SLO.

## Model servers

| Pattern | When |
|---|---|
| Dedicated GPU pods per model | Large LLM, strict isolation |
| Shared GPU with batching | High QPS, similar SLAs |
| CPU classifiers | Small models, fast pre-filter |
| External API passthrough | Vendor LLM with local safeguards only |

Requirements:

- Health: readiness when model loaded; liveness under load
- **Graceful drain** on deploy; in-flight request timeout
- Token/context limits enforced at gateway and server
- Secrets for weights/API keys via vault, not env in images

Hand off cluster bootstrap to `cluster-deployment-engineer`; own serving manifests and HPA rules here.

## Gateway responsibilities

- Authentication, tenancy, rate limits (coordinate with `product-infrastructure-security-engineer`)
- Request ID propagation for tracing
- Routing by model ID, region, experiment flag
- Timeout and payload size limits
- Circuit breakers to downstream safety and model services

Keep gateway **stateless**; store session policy in external store if needed.

## Scaling and health

- HPA on GPU utilization, queue depth, or custom metric (tokens/s)
- **Cold start** budget for scale-from-zero — often unacceptable for prod LLM
- Pre-warm replicas before traffic shift
- Load test **full path** including safeguards (`performance-engineer`)

Capacity signals: GPU memory headroom, batch queue length, OOM kills, throttle rate from vendor APIs.
