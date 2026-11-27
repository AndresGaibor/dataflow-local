---
title: "Creating task chains for data refreshes"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Refresh/task-chains-for-refresh.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Refreshing analytics data", "Scheduling data refreshes with tasks"]
---

# Creating task chains for data refreshes

In the context of analytics data refreshes, a task chain is a set of tasks configured with event-based schedules that depend on one another. You can create task chains that refresh applications, scripts, data flows, and table recipes in a specific order. For example, you could run three data flows, one after the other, and after these events, reload an application to collect and analyze the data from these data flows.

## Starting a task chain

To start a task chain, you need to create a dependency between the current task and an existing task.

Do the following:

1. Create a task (for an application, script, data flow, or table recipe) that refreshes data on a time-based schedule.

   [*Creating a task*](refresh-work-with-tasks.htm#Creating)
2. Create another task. When configuring the task, under Based on, select one of the following:

   - Another task succeeded: Start the refresh when a selected task successfully runs.
   - Another task failed: Start the refresh when a selected task fails.
   - Another task finished: Start the refresh when a selected task finishes running, regardless of whether it ended successfully or unsuccessfully.
   - When data is refreshed: Start the refresh when a data update is detected in a Qlik Talend Data Integration pipeline that is used downstream in an application. Available for applications only.

     Tip noteThe option is only available if the application is connected to a Qlik Talend Data Integration pipeline.
3. Select the Space, Asset, and Task that you want to link to your current task.
4. Click Save.

In this way, you can chain together many different tasks.

To create a task chain, create a task with an event-based schedule.

![Task creation dialog with dropdown in use, to select an event-based trigger under 'Based on' property](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui-gen_reload-task-chain.png "Click to view full size")

## Task chaining example

For example, you could configure the following chain:

1. Task 1 reloads an application at a specific time.
2. When task 1 completes—regardless of success or failed status—task 2 runs a script to export QVD data.
3. When task 2 runs successfully, task 3 runs a data flow to export additional QVD data.
4. When task 3 runs successfully, task 4 reloads a second application. This application combines the data loaded by each of these assets.

## Visualizing task chains

You can visualize and manage task chains in the Tasks section of the Analytics activity center. See [*Viewing and managing task chains*](refresh-monitor-tasks.htm#ManageChains).

## Permissions

A task chain is simply a set of multiple tasks that have dependencies between them. You need to have the required permissions in each resource's space to be able to establish a task chain and run the chain successfully.

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

## Learn more

- [*Scheduling data refreshes with tasks*](refresh-work-with-tasks.htm)
