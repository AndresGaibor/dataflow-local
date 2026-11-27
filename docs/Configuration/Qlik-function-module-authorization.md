---
title: "Qlik Function Module authorization"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Connectors_SAP/Configuration/Qlik-function-module-authorization.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "SAP NetWeaver", "SAP Connector configuration"]
---

# Qlik Function Module authorization

Expand/Collapse all

# Qlik Function Module authorization

You can restrict which Qlik Function Modules can be used. There is an authorization object where the allowed Qlik Function Modules can be listed: /QTQVC/CAL.

You can list the allowed Function Modules under /QTQVC/FM:

![File tree showing where Function modules can be listed](../_images/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Resources/Images/ui_SAP-Function-Modules.png)

A ‘\*’ in /QTQVC/FM means that all Qlik Function Modules can be used.

Use a role where the authorization object /QTQVC/CAL is present, for example QTQVCACCESS. When the authorization object in the role has been updated, assign the role to the SAP connector user. If users should have different assignments, it is possible to create different copies of a role and assign the appropriate role to a specific user.

## Function Modules used for SAP connectors that can be used in all SAP systems

SQL Function Modules

Function Modules for SQL connector

| Function Module | Function Module description | Function group |
| --- | --- | --- |
| /QTQVC/ANALYZE\_SQL | Analyze SQL-Statement | /QTQVC/QSQL |
| /QTQVC/DELETE\_MEMORY | Deletes Shared Buffer memory after usage | /QTQVC/CONNECTOR |
| /QTQVC/EXPAND\_STATEMENT | Expands SQL statement if Row Based Security is used | /QTQVC/QSQL |
| /QTQVC/FETCH\_STREAM | Fetch data produced by READ\_DATA job | /QTQVC/CONNECTOR |
| /QTQVC/GET\_BUSINESSGROUP | Get Business Groups | /QTQVC/BUSGROUP |
| /QTQVC/GET\_BUSINESSGROUP\_TBLS | Get Business Group Definition | /QTQVC/BUSGROUP |
| /QTQVC/GET\_CDS\_INFO | Get information about CDS view | /QTQVC/CONNECTOR |
| /QTQVC/GET\_LANGUAGE | Get available language codes | /QTQVC/CONNECTOR |
| /QTQVC/GET\_TABLES | Get table information | /QTQVC/CONNECTOR |
| /QTQVC/OPEN\_STREAM | Opens the Stream for Downloading Data | /QTQVC/CONNECTOR |
| /QTQVC/PROCESS\_STATUS | Check or update process chain status | /QTQVC/QSQL |
| /QTQVC/READ\_FIELDS | Get tables and fields and check SQL statement structure | /QTQVC/QSQL |
| /QTQVC/READ\_MEMORY | Read Shared Buffer memory filled by READ\_DATA | /QTQVC/CONNECTOR |
| /QTQVC/SCHEDULE\_JOB | Schedules the READ\_DATA Background Job | /QTQVC/CONNECTOR |
| /QTQVC/SELECT\_WIDE\_FIELD | Select a wide field | /QTQVC/CONNECTOR |
| /QTQVC/TIMESTAMP\_ADD\_TIME | Add seconds to timestamp | /QTQVC/CONNECTOR |
| /QTQVC/WRITE\_TRACE | Write record in Trace table | /QTQVC/CONNECTOR |

General Function Modules

Function modules that can be used by most SAP connectors

| Function Module | Function Module description | Function group |
| --- | --- | --- |
| /QTQVC/ADMIN | Qlik administration module | /QTQVC/CONNECTOR |
| /QTQVC/CHECK\_RELEASE | SAP Connectors release information | /QTQVC/CONNECTOR |
| /QTQVC/UPDATE\_CONTROL | Update database table /QTQVC/CONTROL | /QTQVC/CONNECTOR |
| /QTQVC/UPDATE\_STATUS | Update database table /QTQVC/STATUS | /QTQVC/CONNECTOR |

## Function Modules used for SAP connectors for SAP BW

These Function Modules can only be used in SAP BW systems.

BW Function Modules

Function Modules for BW (BEx, InfoProvider) connector

| Function Module | Function Module description | Function group |
| --- | --- | --- |
| /QTQVC/ADDITIONAL\_METADATA | Get additional metadata | /QTQVC/MULTIPROVIDER |
| /QTQVC/CALL\_BEXQUERY | Execute a BEx Query | /QTQVC/BEX\_QUERY |
| /QTQVC/CHECK\_CHAR\_VALUE | Check characteristic value | /QTQVC/BEX\_QUERY |
| /QTQVC/CHECK\_RELEASE\_BW | SAP BW Connectors release information | /QTQVC/BEX\_QUERY |
| /QTQVC/DELETE\_MEMORY | Deletes Shared Buffer memory after usage | /QTQVC/CONNECTOR |
| /QTQVC/FETCH\_MPSTREAM | Fetch data produced by READ\_DATA job | /QTQVC/MULTIPROVIDER |
| /QTQVC/GET\_BEXQUERIES | Get available BEx Queries | /QTQVC/BEX\_QUERY |
| /QTQVC/GET\_BWOBJECTS | Get BW objects | /QTQVC/MULTIPROVIDER |
| /QTQVC/GET\_INFOPROVIDERS | Get InfoProviders | /QTQVC/MULTIPROVIDER |
| /QTQVC/GET\_METADATA | Get Metadata for InfoProvider | /QTQVC/MULTIPROVIDER |
| /QTQVC/GET\_MPROWCOUNT | Get number of expected rows from an InfoProvider execution | /QTQVC/MULTIPROVIDER |
| /QTQVC/GET\_VARNAMES | Get Variable names for a BEx Query | /QTQVC/BEX\_QUERY |
| /QTQVC/IOBJ\_GETDETAIL | Get Details About an InfoObject | /QTQVC/BEX\_QUERY |
| /QTQVC/MDPROV\_GET\_VARIABLES | Delivers a List of VARIABLES | /QTQVC/RSOB |
| /QTQVC/MDPROVIDER\_GET\_HIER | Delivers a list of HIERARCHIES | /QTQVC/BEX\_QUERY |
| /QTQVC/MDPROVIDER\_GET\_MEMBERS | Delivers a List of MEMBERS | /QTQVC/BEX\_QUERY |
| /QTQVC/OPEN\_MPSTREAM | Opens the Stream for Downloading Data | /QTQVC/MULTIPROVIDER |
| /QTQVC/READ\_MEMORY | Read Shared Buffer memory filled by READ\_DATA | /QTQVC/CONNECTOR |
| /QTQVC/RRT\_GET\_DIM\_CARDINALITY | Number of members in the dimension | /QTQVC/CARDINALITIES |
| /QTQVC/SCHEDULE\_MPJOB | Schedules the READ\_MPDATA Background Job | /QTQVC/MULTIPROVIDER |
| /QTQVC/UPDATE\_CONTROL | Update database table /QTQVC/CONTROL | /QTQVC/CONNECTOR |
| /QTQVC/UPDATE\_STATUS | Update database table /QTQVC/STATUS | /QTQVC/CONNECTOR |
| /QTQVC/WRITE\_TRACE | Write record in Trace table | /QTQVC/CONNECTOR |
