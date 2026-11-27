---
title: "Monitoring and operating your data tasks"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Introduction/Monitoring-your-data-tasks.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data"]
---

# Monitoring and operating your data tasks

You can monitor and operate the status and progress of your data tasks with monitor views. A monitor view lets you view the status of a subset of the data tasks that you have access to monitor in the tenant, based on a filter. You can create several views to monitor different aspects of your data pipelines.

- Navigate to Data Integration > Monitor views to display monitor views.

Besides creating customized monitor views you can also use the prepared All tasks view to shows all runnable data tasks in all projects.

Information noteWith a Qlik Talend Cloud Starter subscription, customized monitor views are not supported. You can monitor and operate your data tasks as described in [*Using a monitor view*](#Using)with a single monitor view. You can filter which tasks to display, and which columns to display, but the settings will not be saved.

## [*Monitoring an individual data task*](Monitoring-data-tasks.htm)

You can monitor the status and progress of individual data tasks by selecting Monitor from the drop-down menu in the top left of the data task window.

## [*Monitoring a Qlik Open Lakehouse storage task*](Monitoring-qol-storage-tasks.htm)

The storage task in Qlik Open Lakehouse projects runs continuously rather than in batches. As a result, the associated monitoring metrics differ accordingly.

## [*Setting notifications for changes in operation*](Notifications.htm)

You can set notifications to be alerted at changes in the operation of your data pipeline. You can get a notification in your browser, by email, or a push message to the Qlik Analytics mobile app.

## [*Troubleshooting data tasks*](../Deploying/Troubleshooting-data-assets.htm)

This section describes problems that can occur when working with data tasks and how to troubleshoot.

## Creating a new monitor view

Create a customized monitor view to get started monitoring your data tasks.

1. Click Create new and select Monitor view.
2. Type a name and description of the monitor view, select which space to create it in, and click Create when you are ready.

   The monitor view is displayed.
3. The monitor view shows all data tasks from all projects from the start.

   Use the filters to create a view with the tasks that you want to monitor. The filter lists will only include the resources that you have permission to list.

   The following filters are available:

   - Project

     You can select all projects in one or more spaces, select individual projects, or a combination of both.
   - Task type
   - Task lineage

     Shows the upstream task lineage of the selected tasks.

     For example, you can select data marts from different projects. This will monitor all upstream data tasks that affect the selected data marts.
   - Task impact

     Shows all downstream tasks impacted by the selected tasks.

     For example, you can select a landing data task that is in error. This will monitor all downstream data tasks that are affected by the selected landing data task.

     Tip noteYou can combine the Task lineage and Task impact filters. For example, you can monitor all data tasks that are in the lineage of a selected data mart of your interest, and are impacted by a selected landing task that is in error.
   - Data gateway

     Shows all data tasks that perform operations via one of the selected Data Movement gateways. Such tasks can be:

     - Tasks that move data, such as landing tasks or replication tasks
     - Tasks that extract, load, and transform data and that are running on a data platform that is not directly accessible from Qlik Cloud. Such tasks can be storage tasks, transform tasks, registration tasks, and data mart tasks.

     Select Not using data gateway to view tasks that are not using a data gateway. This would be any ELT task running on a data platform which is directly accessible from Qlik Cloud.

     Information noteTasks that are associated with a deleted gateway will no longer match the Data gateway filter. In order to see such tasks you should clear the Data gateway filter selection.
   - Data platform/target

     Shows tasks with the selected data platforms (data pipeline tasks) or targets (replication tasks).
   - Source

     Shows data movement tasks with the selected data sources. Data movement tasks can be any the following, according to use case:

     - Data pipeline use case: Landing tasks
     - Replication use case: "Replicate data" tasks or "Land data in data lake" tasks
   - Lakehouse clusters

     Show data movement tasks running on selected lakehouse clusters.

     Information noteThe lakehouse clusters filter only applies to Qlik Open Lakehouse projects.
   - Owner

   For example, select a space in Project under All projects in spaces:, and select Landing in Task type. This creates a view where you can see all landing data tasks for all projects in the selected space.
4. When you are ready, click Save.

The monitor view is now created and displays all tasks that match the filter, and are in a state where they can be run. This means that tasks in status New or Ready to prepare are not displayed in the monitor view. If a task that has been prepared successfully is changed and prepared with errors, the monitor view will display the previous version that can be run.

Information noteIf more than 300 tasks match the filter, only the first 300 tasks are displayed, with a warning at the top. In this case, use the filters to reduce the number of matching tasks.

## Cloning a monitor view

You can also create a monitor view by cloning an existing monitor view.

- Click Save as and save the view with a new name. You can also select which space to save the view in.

You can use this, for example, to:

- Create a monitor view based on another view.

  Open a monitor view, change the filters, and save it with a different name.
- Move a monitor view to another space

  Save the monitor view with the same name to another space, and then delete the original view.

## Managing monitor views

To display monitor views, navigate to Data Integration > Monitor views.

You can filter the monitor views on Spaces and Owner of the monitor view. Click on a monitor view to open it.

- To edit a monitor view, click ... and then Edit.
- To delete a monitor view, click ... and then Delete.

## Using a monitor view

The monitor view shows the following properties for all data tasks that are displayed with the filter that is used.

- Task name
- Project
- Source

  Shows data movement tasks with the selected data sources.
- Data platform/target

  Shows tasks with the selected data platforms (data pipeline tasks) or targets (replication tasks).
- Space
- State
- Message
- Data is updated to

  Source changes for at least one of the task sources are applied up to this time.
- Datasets
- Datasets with error
- Next schedule
- Lakehouse cluster

  Information noteThe lakehouse clusters filter only applies to Qlik Open Lakehouse projects.
- Last run: Start time
- Last run: Durations
- Last run: Datasets
- Owner
- Processed datasets
- Processed records
- Created
- Modified
- Actions

  This column contains a menu where you can perform an action, such as Run or Stop, depending on the status of the task. You can also access the schedule, and go directly to the project or the task design.

### Selecting which columns to display

You can customize which columns to display by clicking ![More button](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_vertical.svg) on a column and selecting Displayed columns. Then you can select which columns to display or hide.

You can hide a single column by clicking ![More button](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_vertical.svg) on a column and selecting Hide column.

### Sorting the data tasks in the monitor view

You can sort the data tasks by clicking on a column header. Click on the header again to change between ascending and descending sort order. You can also click ![More button](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_vertical.svg) on a column and select Sort by ascending or Sort by descending.

To sort on multiple columns, press Shift or Ctrl while selecting columns. On a macOS device, use the command button (⌘).

### Pinning columns

You can pin columns to the left or the right side of the column to keep them visible when you scroll horizontally.

- Click ![More button](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_vertical.svg) on a column and select Pin to the left or Pin to the right.

To unpin a pinned column, click ![More button](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_vertical.svg) on a column and select Unpin.

### Filtering tasks in the monitor view

You can also click KPIs to get a quick overview of the status of tasks. The KPI items can be used as a quick filter. The following KPIs are available:

- Ready to run

  This includes all tasks that have not been run, and tasks that were stopped before execution was completed.
- Running
- Completed

  This includes all tasks where the last run was successful.
- Attention required!

  This displays all tasks in error, and tasks where the gateway agent is disconnected.

Transitional states, such as Starting, are included in the closest KPI item.

### Viewing details for a data task

You can view details for a data task.

1. Select a data task.
2. Click Details.

You can view:

- Pipeline, to see a pipeline view of the project where the data task belongs.

You can also go to the individual monitor view of the selected data task by clicking Open task monitor.

- For more information about monitoring individual Landing tasks, see [*Landing data from data sources*](../Landing/Landing-data-data-sources.htm#Monitori).
- For more information about monitoring other data tasks, see [*Monitoring an individual data task*](Monitoring-data-tasks.htm).

### Operating data tasks

You can operate data tasks in the monitor view.

1. Select one or more tasks in the monitor view.

   - Click Run to run the selected tasks.
   - Click Stop to stop the selected tasks.

Tip noteYou can also perform Run and Stop for a task from the ... menu in the Actions column. If you do not see the Actions column it is probably hidden, use the column picker (![column picker](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_columns.svg)) to display it.

For more information about operating data tasks, see:

- [*Operations on the landing data task*](../Landing/Landing-data-data-sources.htm#Operatio)
- [*Operations on the storage data task*](../Storage/generating-datasets.htm#Operatio)[*Operations on the storage data task*](../Storage/generating-datasets.htm#Operatio)

## Viewing run history

You can view the run history of a task to identify root causes and understand patterns over time.

- Click Run history in Monitor view of a task.
- Click Run history in the ... menu of a task in Monitor views.

Up to 100 executions are displayed in the run history based on your filter selections. Refine your filter criteria to see other executions. You can filter on execution end date and task status. Run information is retained for 13 months. Dataset metadata in runs is retained for 30 days.
