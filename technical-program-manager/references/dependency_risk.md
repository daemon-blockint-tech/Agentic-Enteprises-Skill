# Dependencies and RAID

## Table of contents

1. [Dependency types](#dependency-types)
2. [RAID log](#raid-log)

## Dependency types

| Type | Example |
|---|---|
| Technical | Service B API must ship before UI integration |
| Team | Security review blocks prod deploy |
| External | Vendor API GA date |
| Environment | Staging parity with prod for load test |

Document: predecessor, successor, lead time, fallback if slip.

## RAID log

| Column | Use |
|---|---|
| **R**isk | Potential problem; likelihood/impact; mitigation |
| **A**ction | Task to reduce risk or advance program |
| **I**ssue | Active blocker; owner; target resolution |
| **D**ecision | What was decided; who; when |

Review weekly; close items with evidence, not optimism.
