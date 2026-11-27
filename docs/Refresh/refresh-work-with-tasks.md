---
title: "Scheduling data refreshes with tasks"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Refresh/refresh-work-with-tasks.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Refreshing analytics data"]
---

# Scheduling data refreshes with tasks

You can create tasks with custom schedules for an application, script, [data flow](#glossary-2 "Glossary term"), or table recipe to be updated with the latest data. Tasks can be created in your activity center, or when you open the application, script, data flow, or table recipe.

Scheduling dialog showing the tasks for scheduled reloads of an application

![Scheduling dialog showing tasks for an app](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-gen_reload-tasks-dialog.png "Click to view full size")

This help topic is a general overview of working with tasks. For specific instructions about each type of asset, see:

- Applications: [*Reloading application data*](../Apps/reloading-apps-cloud-hub.htm)
- Scripts: [*Running scripts*](../ScriptEditor/reloading-scripts.htm)
- Data flows: [*Managing data flows*](../DataFlow/managing-data-flows.htm)
- Table recipes: [*Managing table recipes*](../TableRecipe/managing-table-recipes.htm)

## Terminology

Different terminology is used for the process of refreshing data in your analytics assets:

### Applications

The action of refreshing the data loaded by your application is known as reloading the application. This is because data is updated and reflected across all analytics objects in the application, such as visualizations and sheets.

### Scripts

A script does not contain any analytics objects, such as visualizations or sheets. Scripts are used to export data into separate files or external storage locations, which then may be loaded into applications for analysis. For this reason, the action of refreshing a script is known as running the script.

### Data flows and table recipes

Similar to scripts, data flows and table recipes are used to prepare and export data to files or storage locations. For this reason, the action of refreshing a data flow or table recipe is referenced as running it.

## Creating a task

To create a task:

1. In the Analytics or Insights activity center, click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on an application, script, data flow, or table recipe.
2. Click Schedule.

   The scheduling dialog opens.
3. Click Create new task.
4. For Task name, enter a name for the task.
5. Optionally add a Description.
6. Under Based on, select the trigger for the task. You have the following options:

   - Time-based: Schedule the refresh to occur at a specific point in time. Then, configure the task with the associated settings for that trigger. For details, see [*Time-based schedules*](#TimeBased).

     The following time-based triggers are available:

     - Daily
     - Weekly
     - Monthly
     - Yearly
   - Event-based: Schedule the refresh to start when a specific event takes place. For details, see [*Event-based schedules*](#EventBased).

     The following event-based triggers are available:

     - Another task succeeded: Start the refresh when a selected task successfully runs.
     - Another task failed: Start the refresh when a selected task fails.
     - Another task finished: Start the refresh when a selected task finishes running, regardless of whether it ended successfully or unsuccessfully.
     - When data is refreshed: Start the refresh when a data update is detected in a Qlik Talend Data Integration pipeline that is used downstream in an application. Available for applications only.

       Tip noteThe option is only available if the application is connected to a Qlik Talend Data Integration pipeline.

     Information noteUse event-based triggers to create task chains for refreshing data. For further instructions, see [*Creating task chains for data refreshes*](task-chains-for-refresh.htm).
7. When done, click Save.

### Time-based schedules

When you create a time-based schedule, you can choose:

- The frequency and interval of the refresh
- The timezone and time of day
- How long the schedule will be in effect

Repeating refreshes can be set at the following intervals:

- Daily: Set the times per day, timezone, and the time of day.
- Weekly: Set the days of the week, times per day, timezone, and time of day.
- Monthly: Set the days of the month, times per day, timezone, and time of day.
- Yearly: Set the months, days of the month, times per day, timezone, and time of day.

For schedules running multiple times per day at any interval, you can also define the hours of the day at which the schedule runs. Specify a specific time for the schedule to start that day.

By default, schedules will run continuously, with no end date. You can choose to set a start date, an end date, or to only run the schedule between two dates.

### Event-based schedules

Event-based schedules allow you to chain together tasks for different applications, scripts, data flows, and table recipes. This is useful for sequential refreshes of these assets.

For more information, see [*Creating task chains for data refreshes*](task-chains-for-refresh.htm).

### Limitations and considerations

- A task for refreshing data is deactivated if it fails to run five times in a row. If you own the task, you will receive [notifications](#glossary-3 "Glossary term") when this happens. Notification settings can be customized for a single application, all applications in a space, or all applications in a tenant. For more information, see [*Ownership of tasks*](#Ownership).
- If the task owner leaves or is deleted from the tenant, another user has to take ownership of the task, or delete and recreate it. Otherwise, its scheduled refreshes will fail. For information about how to change this ownership, see [*Ownership of tasks*](#Ownership).
- If you have a high number of queued and running data refresh processes (and additional concurrent CPU and memory intensive processes), you might notice that some refresh processes run, in some cases, noticeably after their scheduled start time.
- Tasks for refreshing data are not included for the published copy of an application, script, data flow, or table recipe. These published copies must have their tasks reconfigured on the version in the managed space.
- Tasks for refreshing data are not included for the published copy of a table recipe. Published table recipes must have their tasks reconfigured on the version in the managed space.
- If your application, script, data flow, or table recipe has tasks for refreshing data, and you move it between spaces (personal or shared spaces), these tasks are deactivated. You can reactivate them when ready to resume the scheduled refreshes.

  See [*Activating and deactivating a task*](refresh-manage-tasks.htm#Activating).
- If your table recipe has tasks for refreshing data, and you move it between spaces (personal or shared spaces), these tasks are deactivated. You can reactivate them when ready to resume the scheduled refreshes. See [*Activating and deactivating a task*](refresh-manage-tasks.htm#Activating).

## Manually running a task

Although tasks are meant to run on time-based or event-based schedules, you can still manually run a task for immediate updates.

Do one of the following:

1. Run any task from a single view.

   1. In the Analytics activity center, open the Tasks section from the side panel.
   2. Click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on a task and select Run now.
2. Run the task from the single item.

   1. In the Analytics or Insights activity center, click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on an application, script, data flow, or table recipe.
   2. Click Reload > Schedule or Run > Schedule.

      The scheduling dialog opens.
   3. Click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on a task, and select Run now.

## Managing tasks

From the scheduling dialog, you can manage existing tasks. Actions include:

- Viewing all tasks
- Running
- Editing
- Activating and deactivating
- Viewing run history, including logs
- Deleting

For information, see [*Managing tasks for data refreshes*](refresh-manage-tasks.htm).

## Guardrails

A maximum of 10 tasks for scheduled data refreshes can be added within each application, script, data flow, or table recipe. This limit applies to all Qlik Cloud subscriptions.

## Ownership of tasks

A task for data refreshes runs on behalf of the user who owns the task rather than the owner of the application, script, data flow, or table recipe. For the task to run successfully, the task owner must still have the correct access to the application, script, data flow, or table recipe and its data sources. Certain actions result in changes to who owns the task. The task owner is determined by the following rules:

- When you create a task to schedule refreshes of an application, script, data flow, or table recipe, you become the owner of that task.
- If another user edits or saves an existing task, they become the new owner of that task.
- If another user modifies the load script (application or script) or preparation configuration (data flow or table recipe), they become the new owner of all tasks for refreshes of that application, script, data flow, or table recipe.
- Publishing or republishing to a managed space does not change the owner of any existing tasks within the published copy.
- Creating or modifying an application's [distribution list](#glossary-4 "Glossary term"), whether by uploading a source file in the Reporting section or by manually editing the load script, makes you the new owner of all tasks that have been created for scheduled reloads of that application.

## Permissions for tasks

To create and manage tasks for analytics data refreshes, you need the following permissions:

- Professional user entitlement (applies only to user-based subscriptions)
- For an application, script, data flow, or table recipe in a shared space, you need one of the following space roles in the shared space:

  - Owner (of the space)
  - Can manage
  - Can edit data in applications
  - Can edit
- For an application, script, data flow, or table recipe in a managed space, you need one of the following space roles in the managed space:

  - Owner (of the space)
  - Can manage
  - Can operate

You can also create and manage tasks as a tenant or analytics administrator. However, you also need the required space roles in the space (see above) if the resource is in a shared or managed space.

For more information about permissions in shared and managed spaces, see:

- [*Shared space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-shared-space-prof-full.htm)
- [*Managed space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-managed-space-prof-full.htm)

## Administrators and tasks for refreshing data

In the Administration activity center, tenant and analytics administrators can manage tasks for refreshes of applications, scripts, data flows, and table recipes.

For more information, see [*Managing resources*](../Introduction/managing-user-resources.htm).

## Learn more

- [*Managing tasks for data refreshes*](refresh-manage-tasks.htm)
