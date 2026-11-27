---
title: "Target update methods"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/SourcesConnections/Change-processing.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Setting up spaces and connections", "Setting up connections to data sources"]
---

# Target update methods

You can set which update method to use, either during the initial task setup, or later in the data task Settings. It is not possible to change the update method once the data task has been prepared.

The available update methods are determined by task type and connector capabilities. The available data movement task types are landing, replication, or landing data in a data lake.

## Update methods when landing data in data pipeline projects

- Change data capture (CDC) using Change Tables

  The data task starts with a full load. The target data is then kept up-to-date using incremental loading based on date fields. CDC may not be supported by all data sources.

  Information noteWhen landing data from SaaS application sources, DELETE operations are not supported. This means that if a row is deleted in the source, it will not be deleted in the landing data.

  When working without Data Movement gateway, you set the interval using the Scheduler. For more information, see [*Scheduling tasks*](../Deploying/Scheduling-tasks.htm).
  When working with Data Movement gateway, you set the interval between reading changes from the source in Settings > Change processing tuning.
- Reload and compare

  The data task performs full loads only from the source. This is useful if your source does not support CDC, for example, or if you want DELETE operations (which are not supported by CDC) to be propagated to the target. Reload and compare can be used with any supported data source, and can be scheduled to occur periodically.

## Update methods when replicating to database or data warehouse targets

- Full load: Loads the data from the selected source tables to the target platform and creates the target tables if necessary. The full load occurs automatically when the task is started, but can also be performed manually should the need arise. Manual full load would be required, for example, if you need to replicate updates to Views (which are not captured during CDC) or if you are replicating from a data source that does not support CDC.

  Information noteWhen using a SaaS application connector, this option will always be enabled as full load is required.
- Apply changes: Keeps the target tables up-to-date with any changes made to the source tables.
- Store changes: Stores the changes to the source tables in Change Tables (one per source table).

  For more information, see [*Store changes*](../Replicating/replicating-settings.htm#Store).

When working with Data Movement gateway, except when using SaaS application sources, changes are captured from the source in near real-time. When working without Data Movement gateway (for example, with a Qlik Talend Cloud Starter subscription or when selecting None) or when using SaaS application sources, changes are captured according to the scheduler settings. For more information, see [*Scheduling tasks*](../Deploying/Scheduling-tasks.htm).

## Update methods when replicating to cloud storage (data lakes)

- Change data capture (CDC) using Change Tables: Data lake landing tasks starts with a full load (during which all of the selected tables are loaded to the target). The target data is then kept up-to-date using CDC (Change Data Capture) technology.

  Information noteCDC (Change Data Capture) of DDL operations is not supported.

  When working with Data Movement gateway, except when using a SaaS application source, changes are captured from the source in near real-time. When working without Data Movement gateway or with SaaS application sources, changes are captured according to the scheduler settings. For more information, see [*Scheduling tasks*](../Deploying/Scheduling-tasks.htm).
- Reload: Performs a full load of the data from the selected source tables to the target platform and creates the target tables if necessary. The full load occurs automatically when the task is started, but can also be performed manually or scheduled to occur periodically as needed.

  Information noteThis setting is not available when using a SaaS application connector.

Information note

The procedure for setting up replication to cloud storage differs according to your subscription tier.

- If you have a Standard, Enterprise, or Premium subscription, see [*Landing data in a data lake with a Standard, Premium, or Enterprise subscription*](../Replicating/landing-datalakes.htm)
- If you have a Starter subscription, see [*Replicating data with a Qlik Talend Cloud Starter subscription*](../Replicating/replicating-starter-subscription.htm)

## Understanding scheduled change data capture (CDC)

When working without Data Movement gateway, changes are captured according to a scheduled interval. It is important to be aware of how the scheduling works, which is best demonstrated by way of example. In the following example, a task has been scheduled to run every 30 minutes, starting at 9:00.

- The task starts at 9:00 with a full load.
- The full load ends at 9:40, meaning that the 9:30 run will be skipped.
- The next run starts at 10:00, and captures any changes committed until 10:00.
- The 10:00 run ends at 10:15.
- The next run starts at 10:30 and captures any changes that occurred between 10:00 and 10:30.

Information noteDepending on the load on the system, the number of concurrent running tasks, and how many pods are available, the next scheduled instance might not start at exactly the scheduled time.
