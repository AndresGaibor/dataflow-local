---
title: "Usage example"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Replicating/change_tables_useExample.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating a replication project", "Using Change Tables"]
---

# Usage example

The following SQL statement returns a range of changes from the last handled event (of change sequence "20240723144522110000000000000901203") until the event committed on 23-Jul-2024 at 23:00:00.00. For update operations, the before image value (in this example, the salary before and after) is also returned.

SELECT CHANGE.[header\_\_change\_seq],

CHANGE.[header\_\_stream\_position],

CHANGE.[header\_\_operation],

CHANGE.[header\_\_transaction\_id],

CHANGE.[header\_\_timestamp],

CHANGE.[EMPLOYEE\_ID],

CHANGE.[FIRST\_NAME],

CHANGE.[LAST\_NAME],

CHANGE.[SALARY],

BI.[SALARY],

FROM [Replication].[HR].[EMPLOYEES\_ct] CHANGE LEFT OUTER JOIN

[Replication].[HR].[EMPLOYEES\_ct] BI  ON

BI.[header\_\_change\_seq] = CHANGE.[header$\_\_change\_seq] AND

BI.[header\_\_change\_oper] = 'B'

WHERE CHANGE.header\_\_oper <> 'B' AND

CHANGE.[header\_\_stream\_position] > '20120723144522110000000000000901203' AND

CHANGE.[header\_\_stream\_position] <= '2012072323000000Z' AND

ORDER BY

CHANGE.[header\_\_stream\_position], CHANGE.[header$\_\_stream\_oper]
