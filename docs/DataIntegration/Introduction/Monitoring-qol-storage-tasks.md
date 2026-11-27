---
title: "Monitoring a Qlik Open Lakehouse storage task"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Introduction/Monitoring-qol-storage-tasks.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Monitoring and operating your data tasks"]
---

# Monitoring a Qlik Open Lakehouse storage task

The storage task in Qlik Open Lakehouse projects differs from other projects as it runs continuously, rather than in batch mode. As a result, monitoring metrics are different.

## General monitoring overview

The monitoring view lets you track task status and metrics:

- Tabs

  Switch between Info, Full load, and Change processing to view the relevant metrics for each phase of the task.
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

## Info monitoring details

The Info section provides a summary of the overall task status:

- Run

  Displays the Run ID of the current run.
- Data

  Data task is updated to displays the time to which the oldest view is updated. It represents the latest point in time where all source changes committed up to that moment are already available in the target tables.

  If no new source changes are detected, this value is set to the current time.
- Task

  Displays the name and status of the cluster on which this task is running, and general task information and status.

## Full load monitoring details

You can view the following statistics for the data task in Full load:

- Total datasets

  The number of datasets loaded.
- Datasets in error

  The number of datasets in error.
- Incoming changest

  The number of incoming changes.
- Total latency

  Current latency of the task (hh:mm:ss). This duration represents the time from when the change is available in the source until the change is applied and available in the target.

You can view the following details for each table in the data task:

- Name

  The name of the target table.
- State

  Table state will be either: Queued, Loading, Completed, or Error.
- Started

  The time that loading started.
- Ended

  The time that loading ended.
- Duration

  Duration of the load in format hh:mm:ss.
- Records

  The number of records that were replicated during the load.
- Message

  Displays error message if the load was not processed successfully.

## Change processing monitoring details

You can view the following details for the data task to monitor change processing in Change processing:

- Total datasets

  The number of datasets loaded.
- Datasets in error

  The number of datasets in error.
- Incoming changest

  The number of incoming changes.
- Processed changest

  The number of processed changes.
- Total latency

  Current latency of the task (hh:mm:ss). This duration represents the time from when the change is available in the source until the change is applied and available in the target.

You can view the following details for each table in the data task:

- Name

  The name of the target table in the landing asset.
- State

  Table state will be either: Accumulating changes or Error.
- Incoming changes

  The number of changes processed by the landing task which are waiting to be applied by the storage task.
- Processed changes

  The total number of changes which was applied to the target since the dataset was last fully loaded (by the initial full load or by reload action).
- Last processed

  The last source data time that was inserted to the target dataset, translated to local time.
- Unoptimized changes

  Number of records that are queryable via the view, but not yet merged into optimized Iceberg partitions. High counts may affect performance until background optimizations finish.

  This reflects the number of records currently in the changes partition that have not yet been applied to the current or history partitions.

  If this number is consistently high, consider increasing cluster compute capacity to accelerate optimization.

  Information note

  A persistently high or continuously climbing value usually means the rate of incoming changes is outpacing the optimization cycle — the next batch of changes keeps arriving before the previous one finishes optimizing. This does not indicate failed or stopped optimization, and does not affect data correctness.

  If this persists, possible things to check include:

  - Increasing cluster compute capacity to accelerate optimization.
  - Reviewing the primary key — a key that concentrates updates on a small set of rows increases churn.
- Message

  Displays error message if changes to the table fail and are not processed.

## Viewing run history

You can view the run history of a task to identify root causes and understand patterns over time.

- Click Run history in Monitor view of a task.
- Click Run history in the ... menu of a task in Monitor views.

Up to 100 executions are displayed in the run history based on your filter selections. Refine your filter criteria to see other executions. You can filter on execution end date and task status. Run information is retained for 13 months. Dataset metadata in runs is retained for 30 days.
