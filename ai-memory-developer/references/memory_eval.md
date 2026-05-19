# Memory evaluation

## Table of contents

1. [Scenario tests](#scenario-tests)
2. [Regression harness](#regression-harness)

## Scenario tests

| ID | Setup | Assert |
|---|---|---|
| M1 | User states fact in session 1 | Retrieved in session 2 |
| M2 | User contradicts fact | New fact wins |
| M3 | Tenant A fact | Never in tenant B retrieval |
| M4 | User delete | Zero hits |

## Regression harness

Version memory extraction prompt and embedding model; run harness on CI with frozen transcripts.

Report: precision@k, recall@k, isolation failures.
