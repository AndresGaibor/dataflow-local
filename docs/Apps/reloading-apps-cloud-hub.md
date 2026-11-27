---
title: "Reloading application data"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/reloading-apps-cloud-hub.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with applications"]
---

# Reloading application data

Ensure your applications always reflect the latest data by reloading them. Unlike automatic updates, applications don't refresh automatically when their data sources change. Manually reload applications to sync them with the latest data, or create tasks to schedule reloads for convenience. Reloads can be initiated through various methods, ensuring your insights stay up-to-date.

For information about which users can reload data, see:

- [*Managing permissions in shared spaces*](../Spaces/managing-shared-spaces.htm)
- [*Managing permissions in managed spaces*](../Spaces/managing-managed-spaces.htm)

Information noteThe maximum reload time for an application is three hours. If an application takes longer than this to reload, it will fail and you will receive a message.

Information note
You cannot reload data for applications published to Qlik Cloud from a Qlik Sense Enterprise on Windows deployment.
Applications published from Qlik Sense Enterprise on Windows can be reloaded using the QMC in Qlik Sense Enterprise on Windows.

## Scheduling reloading application data

Create tasks to schedule reloads for your application. The schedule can use time-based or event-based triggers.

Information noteCertain actions cause the ownership of the task to change. For more information, see [*Ownership of tasks*](#Ownershi).

To create a task:

1. Do one of the following:

   - In your [activity center](#glossary-1 "Glossary term"), click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the application and select Reload > Schedule.
   - In your application, do one of the following:

     - Click the application name to open the application details area and click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > Schedule.
     - Click the application name to open the application details area and click No schedule in the ![Schedule](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_schedule.svg) schedule section. If the application already has active tasks, this section might show different text.
2. Click Create new task.
3. For Task name, enter a name for the task.
4. Optionally add a Description.
5. Under Action, select one of the following:

   - Full reload: Refresh all data in the application.
   - Partial reload: Refresh only the Load and Select statements that are preceded by an Add, Merge, or Replace prefix, leaving the other remaining data in the application untouched. For more information, see [*Partial reload*](../Scripting/ScriptPrefixes/PartialReload.htm).
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

     Information noteUse event-based triggers to create task chains for refreshing data. For further instructions, see [*Creating task chains for data refreshes*](../Refresh/task-chains-for-refresh.htm).
7. When done, click Save.

### Time-based schedules

When you create a time-based schedule, you can choose:

- The frequency and interval of the refresh
- The timezone and time of day
- How long the schedule will be in effect
- Full or [*Partial reload*](#Partial)

Repeating refreshes can be set at the following intervals:

- Daily: Set the times per day, timezone, and the time of day.
- Weekly: Set the days of the week, times per day, timezone, and time of day.
- Monthly: Set the days of the month, times per day, timezone, and time of day.
- Yearly: Set the months, days of the month, times per day, timezone, and time of day.

For schedules running multiple times per day at any interval, you can also define the hours of the day at which the schedule runs. Specify a specific time for the schedule to start that day.

By default, schedules will run continuously, with no end date. You can choose to set a start date, an end date, or to only run the schedule between two dates.

### Event-based schedules

Event-based schedules allow you to chain together tasks for different applications, scripts, data flows, and table recipes. This is useful for sequential refreshes of these assets.

For more information, see [*Creating task chains for data refreshes*](../Refresh/task-chains-for-refresh.htm).

### Managing tasks

You can manage existing tasks if you have the permissions to do so.

To view and manage tasks:

1. Do one of the following:

   - In your [activity center](#glossary-2 "Glossary term"), click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the application and select Reload > Schedule.
   - In your application, do one of the following:

     - Click the application name to open the application details area and click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > Schedule.
     - Click the application name to open the application details area and click No schedule > Add schedule.
2. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to a task, and select any of the available options. Alternatively, switch to the History tab to view a detailed history for when the task was run.

For more information, see [*Managing tasks for data refreshes*](../Refresh/refresh-manage-tasks.htm).

### Limitations and considerations

- A task for refreshing data is deactivated if it fails to run five times in a row. If you own the task, you will receive [notifications](#glossary-3 "Glossary term") when this happens. Notification settings can be customized for a single application, all applications in a space, or all applications in a tenant. For more information, see [*Ownership of tasks*](#Ownershi).
- If the task owner leaves or is deleted from the tenant, another user has to take ownership of the task, or delete and recreate it. Otherwise, its scheduled refreshes will fail. For information about how to change this ownership, see [*Ownership of tasks*](#Ownershi).
- If you have a high number of queued and running data refresh processes (and additional concurrent CPU and memory intensive processes), you might notice that some refresh processes run, in some cases, noticeably after their scheduled start time.
- Tasks for refreshing data are not included for the published copy of an application. Published applications must have their tasks reconfigured on the version in the managed space.
- If your application has tasks for refreshing data, and you move it between spaces (personal or shared spaces), these tasks are deactivated. You can reactivate them when ready to resume the scheduled refreshes. See [*Activating and deactivating a task*](../Refresh/refresh-manage-tasks.htm#Activating).

### Ownership of tasks

A task for data refreshes runs on behalf of the user who owns the task rather than the owner of the application, script, data flow, or table recipe. For the task to run successfully, the task owner must still have the correct access to the application, script, data flow, or table recipe and its data sources. Certain actions result in changes to who owns the task. The task owner is determined by the following rules:

- When you create a task for scheduling application reloads, you become the owner of that task.
- If another user edits or saves an existing task, they become the new owner of that task.
- If another user modifies the load script by making edits in Data load editor (or by loading data in Data manager), they become the new owner of all tasks for scheduled reloads of that application.
- Creating or modifying an application's [distribution list](#glossary-4 "Glossary term"), whether by uploading a source file in the Reporting section or by manually editing the load script, makes you the new owner of all tasks that have been created for scheduled reloads of that application.
- Publishing or republishing an application to a managed space does not change the owner of any existing tasks within the published copy.

Information noteIt is not recommended to use Data manager for collaboratively developing the application's data model. For more information, see [*Collaborative development and Data manager*](../LoadData/script-codevelopment.htm#Co-devel).

For more information about co-developing application data models, see [*Collaboratively developing data load scripts in shared spaces*](../LoadData/script-codevelopment.htm).

### Administering tasks for refreshing data

Tenant admins and analytics admins can edit and delete tasks for scheduled data refreshes. This is done in the Administration activity center.
For more information, see:

- [*Managing applications for tenant and analytics administrators*](../Admin/mc-administer-apps.htm)
- [*Managing scripts for tenant and analytics administrators*](../Admin/mc-administer-scripts.htm)

## Partial reload

Turn on Partial reload to run a pre-defined part of the [load script](#glossary-5 "Glossary term") and update the corresponding tables. A full reload always starts by deleting all tables in the existing data model, and then runs the load script. A partial reload will not do this. Instead it keeps all tables in the data model and then executes only Load and Select statements preceded by an Add, Merge, or Replace prefix.

Partial reload must first be configured in the load script in the Data load editor. For information, see [*Partial reload*](../Scripting/ScriptPrefixes/PartialReload.htm).

## Manually reloading application data

Information noteIn this topic, a manual reload is one you start yourself from Qlik Cloud, for example with Reload now. An interactive reload is one you start from inside the application: in the Data load editor, in Data manager, or with a button in a sheet.

You can reload an application manually, adding a reload event to the queue.

Do the following:

- Do one of the following:

  - In your [activity center](#glossary-6 "Glossary term"), click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the application and select Reload > Reload now.
  - In your application, click the application name to open the application details area and click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > Reload now.

## Checking reload status

You can check the reload status of an application. There are different statuses shown depending on your location in the interface.

### From the Reload history view

When you open Reload history, you can see the status of the reloads listed there. Interactive reloads are not included. For details, see [*Scope of Reload history*](#ReloadHistoryScope).

In Reload history, the status can be Success, Reloading, or Failed.

For more information, see [*Viewing reload history for an application*](#Viewing).

### From the application list view

You can check the reload status when browsing applications in the catalog. Switch to list view, find an application, and click the date in the Last modified column. The Reload information popover shows the status and end time of the last reload. The status is Reload successful or Reload failed. If no status is available, it shows Not available.

Information noteThe status and end time shown in Reload information may not match the latest entry in Reload history. Interactive reloads, such as reloads run from the Data load editor, Data manager, or a button in a sheet, are not listed in Reload history. A failed interactive reload is not shown as failed in the list view.

To view the full reload history, click View reload history in the popover. This requires permission to reload the application.

Reload information popover

![Reload information popover](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reload-information.png "Click to view full size")

### From the History view in the scheduling dialog

When you open the scheduling dialog for creating tasks, switch to the History tab. This view shows you the reload status for any reloads triggered by a task.

In this view, the status can be Succeeded, Running, or Failed.

For more information, see [*Viewing the refresh history of a task*](../Refresh/refresh-manage-tasks.htm#TaskHistory).

## Viewing reload history for an application

Reload history allows you to view when the application has recently been reloaded from activity centers or by scheduled Qlik Cloud reload tasks. You can view the status, start and end times, and duration of past and current reloads. You can also view and download a corresponding log file.

There are several ways to view the reload history for an application:

- In the list view of applications, click the date in the Last modified column and select View reload history.
- Open the application's menu and select Reload > History.
- Select Details for the application, and click the Data refreshed row.

Reload history of an application

![Screenshot of the Reload History menu in Qlik Cloud. The Reload History menu displays the status, start time, end time, and duration of reloads in an app. The cancel button is also shown in the screenshot. ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ReloadHistory.png "Click to view full size")

On the Reload history page, click the View button to view the reload summary. Optionally, you can also download a detailed log file. Detailed logs are kept only for a limited number of recent reloads per application. When the limit is reached, new logs replace the oldest ones. For older reloads, Download detailed log is not available.

You might want to cancel a reload of your application if the reload is taking too long or the application has been updated with new data and you want to start a new reload. To cancel a reload, go to Reload history, and click Cancel.

You can see the canceled reload in your Reload history.

### Scope of Reload history

Reload history lists reloads that were started from Qlik Cloud, such as Reload now, scheduled reload tasks, reloads started from Qlik Automate, and reloads started through the Qlik Cloud API.

Reload history does not list reloads that are run from inside the app:

- Reloads run from the Data load editor.
- Reloads run from Data manager.
- Reloads triggered by a button that uses the Reload data action.

Because of this, the status and end time shown as part of the details information can differ from the latest entry in Reload history.

To trace reloads that are not listed here, [tenant administrators](#glossary-7 "Glossary term") can check reload finished events in the Events tab of the Administration activity center. For more information about monitoring system events, administrators can refer to [*Monitoring system events*](../Admin/mc-administer-events.htm).

### Viewing history for tasks

In addition to the Reload history view, you can also view an execution history focused on the tasks created for scheduled reloads of an application. For more information, see [*Viewing the refresh history of a task*](../Refresh/refresh-manage-tasks.htm#TaskHistory).

## Understanding timestamps: Updated, Modified date, and Last reload date

The Updated timestamp is displayed towards the bottom of each application tile in activity centers.
It can also be viewed by selecting ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the application, then selecting Details. The same timestamp is listed in Details as Modified date. The format of the date may differ; for example, if the application was recently updated, the Updated value on the application tile may appear like:  Updated 15 minutes ago.

Last reload date is viewed by selecting ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the application, then selecting Details. This value is only refreshed when the application's data is reloaded. A reload also changes the Updated and Modified date timestamp.

Modified date and Last reload date fields in application Details

![Details view displays Last reload datea and Modified date timestamps](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_AppsUpdatedModifiedLastReload.png "Click to view full size")

The following table lists the operations that refresh Updated (same as Modified date) and Last reload date timestamps:

Operations that refresh Updated and Last reload date values

| Operation | Updated, Modified date | Last reload date |
| --- | --- | --- |
| Reload | Yes | Yes |
| Change name | Yes | No |
| Change description | Yes | No |
| Change thumbnail | Yes | No |
| Publish application | Yes | No |
| Change owner | Yes | No |
| Change script | Yes | No |
| New [sheet](#glossary-8 "Glossary term") | No | No |
| Change sheet | No | No |

## Other ways of reloading an application

This help topic focuses primarily on reloading from your activity centers.
You can reload applications in other ways, such as from:

- Data load editor or Data manager in an application
- Button object in an application
- Qlik Automate

The method you use to trigger your application reloads can impact the capacity limit of your Qlik Cloud subscription. Reloads triggered outside of Data load editor or Data manager, such as those from application buttons, activity centers, or automations, count towards the maximum number of scheduled reloads per application per day. For more information, see:

- [*Qlik Cloud Analytics capacity limits*](../Introduction/qcs-specs-capacity.htm)
- [*Platform guardrails*](../Admin/subscription-options-analytics-user-based.htm#guardra)

Information note

Not all reloads appear in Reload history. Reloads from the Data load editor, Data manager, and buttons in sheets are not listed. For details, see [*Scope of Reload history*](#ReloadHistoryScope).
