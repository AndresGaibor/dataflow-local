---
title: "QlikCloudGroupMode"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemVariables/QlikCloudGroupMode.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Working with variables in the data load editor", "System variables"]
---

# QlikCloudGroupMode

This variable controls the groups that are used in Section Access and returned with the GetUserAttr function ('userGroups' attribute).

Syntax:

QlikCloudGroupMode

Example:

SET QlikCloudGroupMode = 1 ;

QlikCloudGroupMode values

| Value | Results |
| --- | --- |
| 0 | IdP groups |
| 1 | Custom groups |
| 2 | Both IdP and custom groups |

## Learn more

- [*System variables*](system-variables.htm)
- [*Defining IdP or custom groups for GROUP*](../Security/manage-security-with-section-access.htm#Selectin)
- [*GetUserAttr Script and chart function*](../SystemFunctions/GetUserAttr.htm)
