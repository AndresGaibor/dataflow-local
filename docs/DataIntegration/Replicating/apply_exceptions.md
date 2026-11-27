---
title: "Apply exceptions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Replicating/apply_exceptions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Monitoring and operating your data tasks", "Control tables"]
---

# Apply exceptions

Change Processing errors are recorded in the `attrep_apply_exceptions` table, which is described below.

The data in this table is never deleted.

Exceptions table

| Column | Type | Description |
| --- | --- | --- |
| TASK\_NAME | nvchar | The name of the Qlik data task. |
| TABLE\_OWNER | nvchar | The table owner. |
| TABLE\_NAME | nvchar | The table name. |
| ERROR\_TIME (in UTC) | timestamp | The time the exception (error) occurred. |
| STATEMENT | nvchar | The statement that was being executed when the error occurred. |
| ERROR | nvchar | The actual error message. |
