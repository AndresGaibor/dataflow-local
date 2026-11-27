---
title: "Managing data flows"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataFlow/managing-data-flows.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Data flow"]
---

# Managing data flows

What you can do with a data flow depends on the type of space where the data flow is located. In your personal space, you can manage your own data flows. In a shared space, depending on your permissions in that space, you can manage both your own data flows and those of other users. In managed spaces, there are fewer options for managing data flows as access is more governed. For more information about what you can do, see [*Data flow actions*](../Spaces/permissions-managed-space-prof-full.htm#Data)and [*Data flow actions*](../Spaces/permissions-shared-space-prof-full.htm#Data).

From your catalog, and depending on the space, you can:

- [*Adding data flows to collections*](#Adding).
- [*Sharing data flows*](#Sharing)
- [*Moving data flows*](#Moving).
- [*Editing data flow details*](#Editing).
- [*Publishing data flows*](#Publishi).
- [*Duplicating data flows*](#Duplicat).
- [*Running data flows*](#Reloadin).
- [*Scheduling data flows runs*](#Scheduli).
- [*Configuring data flows notifications*](#Configur).
- [*Seeing data flow details*](#Seeing).
- [*Viewing lineage*](#Viewing).
- [*Viewing impact analysis*](#Viewing2).
- [*Exporting data flows*](#Exportin).
- [*Converting data flows to script*](#Converti).
- [*Deleting data flows*](#Deleting).

## Adding data flows to collections

Collections enable you to group content such as data flows, applications, charts, notes and links. To add a data flow to a collection, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > Manage > Add to collection.

By default, collections are private. Tenant admins and analytic admins can make collections public to share them with all other members of the tenant. Public collections do not change members' access to content in spaces. Members will only be able to see content in public collections to which they already have access. To make a collection public, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the collection, select Make public, and click Make public. To make a public collection private again, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), select Make private, and click Make private.

## Sharing data flows

You can share a data flow by inviting a user, group, or everyone in your tenant to the space where it is stored.

Do the following:

1. In the catalog, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the item to be shared and select Share > Invite.
2. Search for users or groups by name or email address.
3. Select space permissions for the users or groups.
4. Or, select permissions for Anyone at <your tenant name> from the dropdown list.
5. Click Done.

The users receive access to the shared item and all other content in the space.

## Moving data flows

You can move data flows between shared spaces as well as between a shared space and a personal space.

If you move a data flow with a run schedule between spaces, the run schedule is deleted. Recreate the schedule in the new space if required.

Do the following:

1. Click ![Move](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the data flow and select Manage > Move to space.
2. Select the new space from Space.
3. To open the new space, select Navigate to space.
4. Click Move.

## Editing data flow details

You can change the titles and descriptions of your data flows. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the data flow that you want to edit and then select Manage > Edit details. You can also change the tags used with the data flow. Tags are used to group data flows with related content. When adding new tags to a data flow, users can view all tags that exist in the tenant.

## Publishing data flows

You can publish data flows from a personal space to a managed space, or share space to a managed space. Publishing creates a copy of the data flow in the managed space. You must have the Owner or Can publish permission in the managed space to which you are publishing the data flow.

You can view the spaces that a data flow has been published to in Details.

Data flows indicate when they were last published to a managed space in the publish dialog.

Do the following:

1. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the data flow and select Manage > Publish to space.
2. Select a managed space.
3. Optionally, change the Published data flow name, Description, and Tags of the data flow.
4. Click Publish.

## Duplicating data flows

You can duplicate any data flow you have access to by clicking ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the data flow and then selecting Manage > Duplicate. The duplicate can be modified.

Duplicating data flows has several uses. For example, you can duplicate a data flow as a form of version control, and store older ones a space created for archival purposes.

Duplicated data flows keep the original data sources. If you did not create the original data sources used in the data flow or if they are not available in the space, you will have to recreate data sources in the data flow.

## Running data flows

You can manually run your flow from the catalog, without having to go to the Editor view. The latest configuration of the flow will be used, along with the latest data from the data source. A new output will be generated if the run is successful.

Do the following:

- Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the data flow and select Run > Run now.

## Scheduling data flows runs

Create tasks to schedule runs for your data flow. The schedule can use time-based or event-based triggers.

To create a task:

1. Do one of the following:

   - In your [activity center](#glossary-0 "Glossary term"), click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the data flow and select Run > Schedule.
   - In your data flow, open the Overview section and click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > Schedule.
2. Click Create new task.
3. For Task name, enter a name for the task.
4. Optionally add a Description.
5. Under Based on, select the trigger for the task. You have the following options:

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

     Information noteUse event-based triggers to create task chains for refreshing data. For further instructions, see [*Creating task chains for data refreshes*](../Refresh/task-chains-for-refresh.htm).
6. When done, click Save.

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

For more information, see [*Creating task chains for data refreshes*](../Refresh/task-chains-for-refresh.htm).

### Managing tasks

You can manage existing tasks if you have the permissions to do so.

To view and manage tasks:

1. Do one of the following:

   - In your [activity center](#glossary-1 "Glossary term"), click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the data flow and select Run > Schedule.
   - In your data flow, open the Overview section and click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > Schedule.
2. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to a task, and select any of the available options. Alternatively, switch to the History tab to view a detailed history for when the task was run.

For more information, see [*Managing tasks for data refreshes*](../Refresh/refresh-manage-tasks.htm).

### Limitations and considerations

- A task for refreshing data is deactivated if it fails to run five times in a row. If you own the task, you will receive [notifications](#glossary-2 "Glossary term") when this happens. Notification settings can be customized for a single application, all applications in a space, or all applications in a tenant. For more information, see [*Ownership of tasks*](#Ownershi).
- If the task owner leaves or is deleted from the tenant, another user has to take ownership of the task, or delete and recreate it. Otherwise, its scheduled refreshes will fail. For information about how to change this ownership, see [*Ownership of tasks*](#Ownershi).
- If you have a high number of queued and running data refresh processes (and additional concurrent CPU and memory intensive processes), you might notice that some refresh processes run, in some cases, noticeably after their scheduled start time.
- Tasks for refreshing data are not included for the published copy of a data flow. Published data flows must have their tasks reconfigured on the version in the managed space.
- If your data flow has tasks for refreshing data, and you move it between spaces (personal or shared spaces), these tasks are deactivated. You can reactivate them when ready to resume the scheduled refreshes. See [*Activating and deactivating a task*](../Refresh/refresh-manage-tasks.htm#Activating).

### Ownership of tasks

A task for data refreshes runs on behalf of the user who owns the task rather than the owner of the application, script, data flow, or table recipe. For the task to run successfully, the task owner must still have the correct access to the application, script, data flow, or table recipe and its data sources. Certain actions result in changes to who owns the task. The task owner is determined by the following rules:

- When you create a task for running a data flow, you become the owner of that task.
- If another user edits or saves an existing task, they become the new owner of that task.
- If another user modifies the data flow in Editor, they become the new owner of all tasks for scheduled runs of that data flow.
- Publishing or republishing a data flow to a managed space does not change the owner of any existing tasks within the published copy.

### Administering tasks for refreshing data

Tenant admins and analytics admins can edit and delete tasks for scheduled data refreshes. This is done in the Administration activity center.
For more information, see:

- [*Managing applications for tenant and analytics administrators*](../Admin/mc-administer-apps.htm)
- [*Managing scripts for tenant and analytics administrators*](../Admin/mc-administer-scripts.htm)

## Configuring data flows notifications

You can access the notifications configuration panel of a data flow to set or modify which event will trigger a notification, and on which support to receive it.

Do the following:

- Click ![Move](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the data flow and select Manage > Notification settings.

Information note

Web notifications are available for 90 days, after which they are deleted.

## Seeing data flow details

Using this option will lead you to the Overview page of the data flow, where you can see all the general information of your data flow. See [*Overview*](navigating-data-flows.htm#Overview).

Do the following:

- Click ![Move](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the data flow and select Details.

## Viewing lineage

Lineage tracks data and data transformation backwards from the data flow to its original sources. This provides an interactive representation of the origins of the data that this data flow processes. For more information on lineage, see [*Analyzing lineage in Analytics*](../Catalog/lineage.htm).

Do the following:

- Click ![Move](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the data flow and select Tools > Lineage.

## Viewing impact analysis

Impact analysis shows the downstream dependencies of data flows outputs. It answers questions about what other applications, scripts, or other resources would be directly or indirectly impacted by changes to the data flow. For more information on impact analysis, see [*Analyzing impact analysis in Analytics*](../Catalog/impact-analysis2.htm).

Do the following:

- Click ![Move](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the data flow and select Tools > Impact analysis.

## Exporting data flows

You can export data flows from the Analytics activity center as .dfw files. These can be uploaded into other Qlik Cloud Analytics tenants or Qlik Sense versions.

The exported data flow is saved in the default download folder of your web browser.

Do the following:

- Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the data flow you want to export and select Download.

## Converting data flows to script

You can convert data flows into scripts. Converting duplicates the data flow and then converts it into a script.

Do the following:

1. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the data flow you want to convert and select Manage > Duplicate as script.
2. Click Confirm.

## Deleting data flows

Do the following:

1. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the data flow you want to delete and select Delete.
2. Click Delete.
