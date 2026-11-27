---
title: "Suspended Tables"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Replicating/suspended_tables.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Monitoring and operating your data tasks", "Control tables"]
---

# Suspended Tables

When a table is suspended, information about the table including the reason for its suspension is recorded in the `attrep_suspended_tables` table. If a table is suspended and then unsuspended while the task is running, the entries for that table will be deleted from the `attrep_suspended_tables` table.

When a task with suspended tables stops, records for that task will remain in the `attrep_suspended_tables` table. In the event that the tables are still suspended when the task is restarted, the data is deleted and then recorded again.

Column descriptions

| Column | Type | Description |
| --- | --- | --- |
| SERVER\_NAME | nvchar | The name of the machine on which the Qlik replication server is installed. |
| TASK\_NAME | nvchar | The name of the data task. |
| TABLE\_OWNER | nvchar | The owner of the suspended table. |
| TABLE\_NAME | nvchar | The name of the suspended table. |
| SUSPEND\_REASON | varchar | The reason why the table was suspended. |
| SUSPEND\_TIMESTAMP | timestamp | The date and time the table was suspended. |
