# Dependency & Risk Mapping

## Technique Coverage

| D3FEND Technique | Description |
|---|---|
| Operational Activity Mapping | Business process mapping |
| Access Modeling | Who can access what |
| Operational Dependency Mapping | Process dependencies |
| Operational Risk Assessment | Risk quantification |
| Organization Mapping | Org structure and roles |
| System Mapping | System relationships |
| Data Exchange Mapping | Data flow mapping |
| Service Dependency Mapping | Service relationships |
| System Dependency Mapping | System-level dependencies |

## Mapping Types

### Service Dependencies
```
Service A → depends on → Service B (API)
Service B → depends on → Database C
Database C → hosted on → Server D
```

Tools: ServiceNow, Dynatrace, Jaeger, dependency graphs

### Data Exchange Mapping
```
Source: CRM
Destination: Data warehouse
Method: ETL pipeline
Data: Customer PII
Frequency: Daily
Encryption: TLS + AES at rest
```

### Access Modeling
```
User: finance_team
Can access: erp_system, reports_share
Cannot access: prod_db, admin_panel
MFA required: yes
Approval: manager + security
```

### Risk Assessment
| Asset | Threat | Vulnerability | Impact | Likelihood | Risk |
|---|---|---|---|---|---|
| Web server | RCE exploit | Unpatched | High | Medium | High |
