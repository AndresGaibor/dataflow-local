---
title: "P reparing Microsoft SQL Server backup and recovery"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/Content/SharedReplicateHDD/SQLServer-Source/sqlserver_backup.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources", "Connecting to databases", "Microsoft SQL Server (log based)", "Preparing the Microsoft SQL Server database for CDC"]
---

# Preparing Microsoft SQL Server backup and recovery

Changes are captured from the database transaction log (TLOG). The TLOG is maintained by Microsoft SQL Server for recovery purposes. All changes made to a database are written to the TLOG. The following happens when recovery is required:

- A backup copy of the database is made.
- Logged events are taken and used in a rolling-forward process where the recorded changes are replayed against that copy.

To prepare for backup and recovery you must make sure that the Microsoft SQL Server Recovery Model is set up. You select the Recovery Model in the Microsoft SQL Server Management Studio. This should be carried out by a Microsoft SQL Server system administrator.

The TLOG data is truncated as soon as it is no longer needed. Therefore, the TLOG is not persistent. However, persistency of the changed data can be ensured by doing the following:

- Perform a full database backup before starting the task
- Set the Recovery Model to Bulk logged or Full.

To set the recovery model:

In the database properties Options tab, set the Recovery Model to Bulk logged or Full. In these modes, the transaction log is more durable.

Information note

After setting the Recovery Model, it is strongly recommended not to change it; doing so may result in loss of data.
