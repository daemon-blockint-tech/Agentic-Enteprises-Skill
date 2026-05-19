# Detection engineering

## Table of contents

1. [Rule template](#rule-template)
2. [Tuning loop](#tuning-loop)
3. [ATT&CK mapping](#attack-mapping)

## Rule template

```yaml
title: [Short behavior name]
description: [What adversary action this catches]
status: experimental | test | production
logsource:
  product: [EDR | windows | aws.cloudtrail]
detection:
  selection: ...
  condition: selection
falsepositives:
  - [Known benign case]
level: medium | high | critical
tags:
  - attack.credential_access
  - attack.t1003
```

## Tuning loop

1. Deploy in alert-only mode
2. Measure FP rate over 14 days
3. Add enrichment (asset criticality, user role)
4. Promote to production with playbook link
5. Review quarterly

## ATT&CK mapping

Map each detection to at least one technique ID; identify coverage gaps in ATT&CK matrix for hunt backlog.
