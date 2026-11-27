---
title: "Monitoring an individual data task"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Introduction/Monitoring-data-tasks.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Monitoring and operating your data tasks"]
---

# Monitoring an individual data task

You can monitor the status and progress of your data tasks by selecting Monitor from the drop-down menu in the top left of the data task window.

You can also create monitor views to monitor several data tasks. For more information, see [*Monitoring and operating your data tasks*](Monitoring-your-data-tasks.htm).

## General monitoring overview

The monitoring view is available for all task types and lets you track task status and metrics:

- Tabs

  Switch between the available tabs — such as Info, Full load, and Change processing, Batch, or Streaming — depending on the task type. For details on each tab, see the relevant task section below.
- Dataset status filter

  A bar chart above the datasets table shows how many datasets are in each status: Queued, Loading, Completed, and Error. The chart is updated dynamically as dataset statuses change. Click a status segment to filter the datasets table to show only datasets in that status.
- Hide widgets

  Click Hide widgets to collapse the metrics widgets. This provides more space to view the datasets table below.
- Start date

  The date and time when the current task run started.
- End date

  The date and time when the task run ended. This is only displayed for finished task runs.
- Run history

  Click Run history to view a list of previous task runs and their outcomes.

## Monitoring data movement tasks

The available monitoring options are determined by both the task type and the connector type. As some connectors do not support CDC (for example, [Epicor](../WebApplications/Connecting-Epicor.htm)), monitoring options that are relevant for CDC will not be shown for those connectors. Similarly as some connectors do not support Full Load, monitoring options that are relevant for Full Load will not be shown for those connectors.

### Data pipeline use case: Landing tasks

All landing tasks must start with a full load of the source data to the target. Once the initial full load completes, the target data is updated with changes to the source data. This can either be done using Reload and compare or Change data capture (CDC) according to the task definition.

For more information, on landing tasks, see [*Landing data from data sources*](../Landing/Landing-data-data-sources.htm).

### Replication use case: "Replicate data" tasks

"Replicate data" tasks usually start with a full load of the source data to the target. The following table summarizes the full load use cases.

| Use case | Full load |
| --- | --- |
| Replicating from SaaS applications. | Required |
| Replicating from other data source types such as databases | Optional |

When replicating from non-SaaS application sources, if the source data already exists on the target and you only want to apply the source changes to the target (or store them for applying later), then the replication mode can be Apply changes, Store changes or both. Both of these replication modes are shown in CDC monitoring.

For more information, on "Replicate data" tasks, see the following topics:

[*Replicating data with a Standard, Premium, or Enterprise subscription*](../Replicating/replicating-other-subscriptions.htm)

[*Replicating data with a Qlik Talend Cloud Starter subscription*](../Replicating/replicating-starter-subscription.htm)

### Replication use case: "Land data in data lake" tasks

"Land data in data lake" tasks are similar to landing tasks in that they must start with a full load. Once the initial full load completes, the target data is updated with changes to the source data. This can either be done using Reload or Change data capture (CDC). Despite their similarity to landing tasks, "Land data in data lake" tasks are considered replication tasks as they consist of source-to-target replication only. They do not offer the possibility of manipulating the data further downstream (for example, using transformations and data marts), which is available in a data pipeline.

Information noteThe steps for creating a separate "Land data in data lake" task are not relevant with a Qlik Talend Cloud Starter subscription. With a Qlik Talend Cloud Starter subscription, replication to cloud storage targets is done via a standard "Replicate data" task.

For more information on "Land data in data lake" tasks, see [*Landing data in a data lake with a Standard, Premium, or Enterprise subscription*](../Replicating/landing-datalakes.htm).

### Refreshing the metadata after new columns are added to a SaaS application source

When new columns are added to a SaaS application source after a task is already running, you need to refresh the metadata to prevent data loss.

To do this:

1. Open and re-save the connection.
2. Prepare the task as described in [*Creating and managing data pipeline projects*](Data-projects.htm).

### Monitoring details

The following monitoring details are available:

- Info
- Full load
- Change processing
- Streaming

  Available for streaming landing tasks only.

#### Info monitoring details

You can view general information about the task, the Run ID, and when data was updated. For CDC tasks, scheduling information is also available in this tab.

#### Full load monitoring details

You can view the following statistics for the data task in Full load:

- Total datasets

  The number of datasets loaded.
- Datasets in error

  The number of datasets in error.
- Total latency

  Current latency of the task (hh:mm:ss). This duration represents the time from when the change is available in the source until the change is applied and available in the target or landing.
- Total throughput

  Target throughput in Kilobytes/second. This indicates how fast the change records are loaded to the target endpoint.

You can view the following details for each dataset in the data task:

- Name

  The name of the target dataset .
- State

  Table state will be either: Queued, Loading, Completed, Full load incomplete, or Error.

  When loading data from a SaaS application source, a Full load incomplete state might sometimes be shown in the monitor due to temporary interruptions. Such interruptions might be caused by the SaaS application's data quota being exceeded, service instability, and others.

  The task will be resumed automatically at the next scheduled CDC instance. However, the full load might remain paused if the issue that causes the interruption has not been resolved yet. You can also resume the task manually instead of waiting for the next scheduled CDC instance.
- Started

  The time that loading started.
- Ended

  The time that loading ended.
- Duration

  Duration of the load in format hh:mm:ss.
- Records

  The number of records that were written to the target during the load.

  Information note

  When the source datasets are filtered, Records will be replaced with the following sections:

  - Read records: The number of records read from the source datasets before filtering.
  - Written records (after filtering): The number of records actually written to the target after filtering.

  For information on filtering datasets, see [*Filtering a dataset*](../Transformation/Filter-data.htm).
- Message

  Displays an error message if the load was not processed successfully.

#### Change processing monitoring details

Change processing displays the number of changes applied to all tables during the last CDC run, or during the current run if it has not yet completed. To see the number of changes applied to individual datasets since the task started, see the Datasets table.

You can view the following change processing statistics:

- Total datasets

  The number of datasets loaded.
- Datasets in error

  The number of datasets in error.
- Total latency

  Current latency of the task (hh:mm:ss). This duration represents the time from when the change is available in the source until the change is applied and available in the target or landing.
- Total throughput

  Target throughput in Kilobytes/second. This indicates how fast the change records are loaded to the target endpoint.
- Total incoming changes

  The number of changes present at the source and waiting to be processed. You can view how many that are accumulated in the source, and how many that are being applied.
- Total applied changes

  The number of changes applied to the target or landing. You can view the number of additions, deletes, and updates.

You can view the following details for each table in the data task:

Information noteThe Inserts, Updates, and Deletes columns are not shown for tasks defined with a SaaS application connectors, as all operations are inserts.

- Name

  The name of the target table in the landing asset.
- State

  Table state will be one of the following: Accumulating changes, Error, or Completed (for scheduled CDC tasks).
- Last processed

  The date and time when the last changes were made to the table.
- Inserts, Updates, and Deletes

  Information note

  When the source datasets are filtered, the Inserts, Updates, and Deletes columns will be grouped as follows:

  - Read: The number of changes (Inserts, Updates, and Deletes) read from the source datasets before filtering.
  - Written (after filtering): The number of changes (Inserts, Updates, and Deletes) actually written to the target after filtering.

  For information on filtering datasets, see [*Filtering a dataset*](../Transformation/Filter-data.htm).

  - Inserts

    The number of insert operations.
  - Updates

    The number of update operations.

    Information noteUpdates are handled as inserts for SaaS application sources.
  - Deletes

    The number of delete operations.
- DMLs (Inserts/Updates)

  Information noteThis column is only shown for tasks defined with a SaaS application connector.

  Information note

  When the source datasets are filtered, the Inserts, Updates, and Deletes columns will be grouped as follows:

  - Read DMLs (Inserts/Updates): The number of DMLs (Inserts and Updates) read from the source datasets before filtering.
  - Written DMLs (Inserts/Updates): The number of DMLs (Inserts and Updates) actually written to the target after filtering.

  For information on filtering datasets, see [*Filtering a dataset*](../Transformation/Filter-data.htm).
- DDL operations

  The number of DDL operations

  Information noteAvailable for "Replicate data" tasks only.
- Message

  Displays error message if changes to the table fail and are not processed.

If you are landing data from an on-premises source and chose Full load mode , the tables will be automatically reloaded when the landing asset is Run.

If you are landing data from an on-premises source and chose Full load and CDC mode, the tables will be continuously updated with new data after the initial full load.

### Reloading selected tables

You can manually reload selected tables from the source. This is useful when you want to recover single tables with error. Reloading tables will not affect the CDC timeline, which is reset if you use Recreate tables. Metadata changes are not propagated when reloading tables.

- To reload selected tables, select the tables in the lower half of Monitor and click Reload tables.

  You need the same permissions that are required to run the data task, that is, Owner or Can operate role.

Reload tables is available after the first run of the data task. If the update method is Reload and compare, Reload tables is not available when the data task is running.

Downstream storage data tasks will be synced the next time they run. If the storage task has history enabled, it will be maintained.

If it is not possible to recover by reloading tables, the next step is to repair the data task.

### Reloading all tables to the target

You can reload all tables to the target if you experience CDC issues that cannot be resolved by reloading specific tables. Examples of issues are missing events, issues caused by source database reorganization, or failure when reading source database events.

Information noteThis operation is only available for tasks with the update method Change data capture (CDC), and that have run at least once.

1. Stop the data task and all tasks that consume it.
2. Open the data task and select the Monitor tab.
3. Click ..., and then Reload target.

This will reload all tables to the target using Drop-Create, and will restart all change data capture from now.

- Storage tasks that consume the landing data task will be reloaded via compare and apply at their next run to get in sync. Existing history will be kept. Type 2 history will be updated to reflect changes after the reload and compare process is executed.

  The timestamp for the from date in the type 2 history will reflect the reload date, and not necessarily the date the change occurred in the source.
- Storage live views will not be reliable during the reload target operation, and until the storage is in sync. Storage will be fully synced when:

  - All tables are reloaded using compare and apply,
  - One cycle of changes is performed for each table.

## Monitoring storage, transform, data mart, mirror, and knowledge mart tasks

You can monitor the status and progress of a Storage, Transform, Data mart, Mirror, or Knowledge mart task.

The following monitoring details are available:

- Info
- Full load
- Batch

#### Info monitoring details

You can view general information about the task, the Run ID, and when data was updated.

#### Full load monitoring details

Information noteFull load monitoring information is not relevant for tasks defined with a SaaS application connector, and therefore not shown.

You can view the following statistics for the data task in Full load:

- Total datasets

  The number of datasets loaded.
- Datasets in error

  The number of datasets in error.
- Total throughput

  Target throughput in Kilobytes/second. This indicates how fast the change records are loaded to the target endpoint.

#### Batch monitoring details

You can view statistics for batches of changes:

- Total datasets

  The number of datasets loaded.
- Datasets in error

  The number of datasets in error.
- Total latency

  Current latency of the task (hh:mm:ss). This duration represents the time from when the change is available in the source until the change is applied and available in the target or landing.
- Total throughput

  Target throughput in Kilobytes/second. This indicates how fast the change records are loaded to the target endpoint.
- Source

  Latency and throughput in the source.
- Target

  Latency and throughput in the target.
- Total incoming changes

  The number of changes present at the source and waiting to be processed. You can view how many that are accumulated in the source, and how many that are being applied.
- Total applied changes

  The number of changes applied to the target or landing. You can view the number of additions, deletes, and updates.

### Viewing status and progress

You can view the following details for each dataset or change in Datasets:

- Name

  The name of the target dataset .
- State

  Table state will be either: Queued, Loading, Completed, or Error.
- Started

  The time that loading started.
- Ended

  The time that loading ended.
- Duration

  Duration of the load in format hh:mm:ss.
- Records

  The number of records that were written to the target during the load.

  Information note

  When the source datasets are filtered, Records will be replaced with the following sections:

  - Read records: The number of records read from the source datasets before filtering.
  - Written records (after filtering): The number of records actually written to the target after filtering.

  For information on filtering datasets, see [*Filtering a dataset*](../Transformation/Filter-data.htm).
- Message

  Displays an error message if the load was not processed successfully.

Data from all source transactions up to the time shown in Data task is updated to is available for consumption from this data task. This information is available for a data task once all tables were loaded and the first set of changes applied. If you selected to generate live views, you can also view when live views are updated.

If there is a batch of changes before the initial load is completed, Data task is updated to will not be updated until the initial load is completed and the first batch of changes are applied. For example, assume that you are loading a data asset which contains an order dataset containing 1 million orders and an order details dataset containing 10 million order details. The datasets take 10 and 20 minutes to perform a full load, respectively. The order dataset is loaded first, followed by the order details dataset . While order dataset was loading, a new order was inserted. So when the order details are loaded, it may contain details of the new order, which does not yet exist in the order dataset . The order and order details datasets will only be in sync and fully updated to the same time after the first batch of changes is applied .

### Viewing detailed information

You can view detailed information on SQL statement level.

1. Select the datasets to monitor in detail.
2. Click Monitor details.

Monitor details is displayed, and you can view the commands that are executed for each step of the load or change process. You can click on a command to view the full SQL statements that were executed.

- Click Export to CSV to export a text file with full SQL statements for all listed commands.

## Data task is updated to for views

The Data task is updated to field shows the time to which the oldest view is updated.

- Standard views

  Data task is updated to shows the time to which the oldest standard view is updated.

  For example, assume a task has two tables, Orders and Order details. Orders is updated to 10:01 with records from 10:00 and 10:01, and Order details has records from 10:00 only. In this case the data task is updated to 10:00. This should not be confused with the start and end times of the data task load, which could be 10:02 to 10:03.
- Live views (Storage data tasks)

  Data task is updated to shows the time to which the oldest live view is updated.

  For example, assume a task has an Orders table. Orders in landing is updated to 10:01 with records from 10:00 and 10:01 ,but Orders in storage is updated to records from 10:00 only. In this case live views to Orders are updated to 10:01, and standard views are updated to 10:00.

## Viewing run history

You can view the run history of a task to identify root causes and understand patterns over time.

- Click Run history in Monitor view of a task.
- Click Run history in the ... menu of a task in Monitor views.

Up to 100 executions are displayed in the run history based on your filter selections. Refine your filter criteria to see other executions. You can filter on execution end date and task status. Run information is retained for 13 months. Dataset metadata in runs is retained for 30 days.
