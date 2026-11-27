---
title: "Managing tasks for data refreshes"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Refresh/refresh-manage-tasks.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Refreshing analytics data", "Scheduling data refreshes with tasks"]
---

# Managing tasks for data refreshes

You can manage existing tasks for refreshing data in applications, scripts, data flows, and table recipes. You can view and manage tasks in two ways:

- In the Tasks section of the Analytics activity center, monitor tasks for all assets you can access. See [*Monitoring tasks for refreshing data*](refresh-monitor-tasks.htm).
- For a single asset, click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > Reload/Run > Schedule on the application, script, data flow, or table recipe from the Analytics or Insights [activity center](#glossary-0 "Glossary term").

Actions for managing and monitoring tasks include:

- Viewing all tasks
- Running
- Editing
- Activating and deactivating
- Viewing run history, including logs
- Deleting

## Viewing existing tasks

Do one of the following:

1. Monitor all tasks in a single view.

   - In the Analytics activity center, open the Tasks section from the side panel.
2. Open the item individually.

   1. Click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on an application, script, data flow, or table recipe from the Analytics or Insights [activity center](#glossary-1 "Glossary term").
   2. Select Reload > Schedule or Run > Schedule.

      The scheduling dialog opens. In the Tasks tab, you can view all tasks for the item.

## Running tasks

You can schedule and manually run tasks.

### Scheduling tasks

To learn about how you can schedule tasks for data refreshes, see [*Scheduling data refreshes with tasks*](refresh-work-with-tasks.htm).

### Manually running a task

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

## Editing a task

You can edit existing tasks.

Do the following:

1. In the Analytics or Insights activity center, click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on an application, script, data flow, or table recipe.
2. Select Reload > Schedule or Run > Schedule.

   The scheduling dialog opens.
3. Click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on a task, and select Edit.

## Activating and deactivating a task

A task can have one of two activation states: Active or Inactive.

You can activate and deactivate tasks as needed. Tasks can are also sometimes deactivated automatically (see [*Reasons for task deactivation*](#Reasons)). When a task is inactive, it will not run based on time-based or event-based triggers. The task also cannot be run manually when it is inactive.

Do one of the following:

1. Activate or deactivate any task from a single view.

   1. In the Analytics activity center, open the Tasks section from the side panel.
   2. Click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on a task and select Activate or Deactivate.
2. Activate or deactivate the task from the single item.

   1. In the Analytics or Insights activity center, click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on an application, script, data flow, or table recipe.
   2. Select Reload > Schedule or Run > Schedule.

      The scheduling dialog opens.
   3. Click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on a task, and select Activate or Deactivate.

### Identifying whether a task is active or inactive

You can tell whether a task is active or inactive by opening Tasks in the Analytics activity center. Deactivated tasks will show Next run as Inactive. They will also have a ![Restricted](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_restricted.svg) icon next to the Task name.

Alternatively, you can view the state by opening ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > Reload/Run > Schedule on the individual asset. In this view, there are two ways to find out the task state:

1. Inactive tasks have a ![Restricted](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_restricted.svg) icon next to the Task name.
2. Check the Next run column value for the task. If the task is inactive, this column shows Inactive, as well as how the task was deactivated.

### Reasons for task deactivation

Tasks can be deactivated in the following ways:

- You or another user with sufficient permissions has manually deactivated it.
- A task is automatically deactivated after failing to run five times in a row.
- If your application, script, data flow, or table recipe has tasks for refreshing data, and you move it between spaces (personal or shared spaces), these tasks are deactivated. You can reactivate them when ready to resume the scheduled refreshes.

## Viewing the refresh history of a task

You can dive deeper into task histories with History. The History view shows all runs of the tasks for the application, script, data flow, or table recipe. You can view details such as completion status, duration, the user on behalf of whom the task ran, and how the run was triggered.

Do the following:

1. In the Analytics or Insights activity center, click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on an application, script, data flow, or table recipe.
2. Select Reload > Schedule or Run > Schedule.

   The scheduling dialog opens.
3. Switch to the History tab.

Click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > View on a single run in the list for additional details. In this view, you are given a log that includes a reload ID. If needed, click Download to download a line-by-line script execution log for further analysis.

The History tab in the scheduling dialog

![Scheduling dialog with the 'History' tab open](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-gen_reload-tasks-dialog-history.png "Click to view full size")

## Deleting a task

Do one of the following:

1. Delete any task from a single view.

   1. In the Analytics activity center, open the Tasks section from the side panel.
   2. Click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on a task and select Delete.
2. Delete the task from the single item.

   1. In the Analytics or Insights activity center, click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on an application, script, data flow, or table recipe.
   2. Select Reload > Schedule or Run > Schedule.

      The scheduling dialog opens.
   3. Click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on a task, and select Delete.

## Permissions

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

## Administering tasks

[Tenant admins](#glossary-2 "Glossary term") can delete tasks for scheduled data refreshes. This is done in the Administration activity center.
For more information, see:

- [*Managing applications for tenant and analytics administrators*](../Admin/mc-administer-apps.htm)
- [*Managing scripts for tenant and analytics administrators*](../Admin/mc-administer-scripts.htm)

## Learn more

- [*Analytics activity center*](../QlikCloudNavigation/Analytics-activity-center.htm)
- [*Monitoring tasks for refreshing data*](refresh-monitor-tasks.htm)
- [*Scheduling data refreshes with tasks*](refresh-work-with-tasks.htm)
