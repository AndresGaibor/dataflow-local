---
title: "Managing scripts for tenant and analytics administrators"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-scripts.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing resources"]
---

# Managing scripts for tenant and analytics administrators

If you are a tenant admin or analytics admin, you can move scripts between [managed spaces](#glossary-0 "Glossary term") or between self-managed (personal or shared) spaces, change owner of scripts, delete scripts, and manage reload schedules.

## Administrator access levels for managing scripts

Tenant and analytics administrators have different levels of access to scripts:

- Tenant administrators: Can manage all scripts in managed, shared, and personal spaces.
- Analytics administrators: Can manage scripts in managed and shared spaces. Cannot manage scripts in other users' personal spaces.

Information noteScript owners and developers can also manage script properties. For more information, see [*Managing scripts*](../ScriptEditor/managing-scripts.htm).

## Scripts overview

To manage scripts, go to the Content page in the Administration activity center and open the Scripts tab.
The tab displays a table with information about the owner of the script and the space where it is located. You can also see when the script was last updated and find details about scheduled data reloads.
You can sort by the columns Name or Last updated, and filter by Name, ID, Owner or Space.

Select Source or Published in the dropdown list above the table:

- Source shows scripts that are in personal or shared spaces. As a tenant admin or analytics admin, you can perform the following actions on these scripts:

  - Manage the script reload schedule
  - Change the owner of the script
  - Move the script to another space
  - Delete the script
- Published shows scripts that are in managed spaces. As a tenant admin or analytics admin, you can perform the following actions on these scripts:

  - Manage the script reload schedule
  - Move the script to another space
  - Delete the script

## Changing owner of scripts

As a tenant or analytics admin, you can change owner of a script.

Do the following:

1. In the Administration activity center, go to Content > Scripts.
2. Select Source.
3. Select one or more scripts and click Change owner.
4. In the Change owner dialog, select the user you want to make the new owner, and then click Apply.

## Changing space of scripts

As a tenant or analytics admin, you can move a script to another space.

Do the following:

1. In the Administration activity center, go to Content > Scripts.
2. Select Source or Published.
3. Select one or more scripts and click Move.
4. In the Move dialog, select the space where you'd like to move the scripts, and then click Confirm.

   Information note

   When changing the space of a script, you might need higher permissions. If required, select the Get elevated privileges checkbox before confirming.

   Elevated privileges are required if you're not the owner of the script or don’t have Can manage permission for either the current or new space. These privileges are temporary and will be reverted after the space change is complete.

## Managing scheduled reloads of script data

Reloading a script updates it with the latest data from the script data sources and then exports it. Scripts can be reloaded manually from [activity centers](#glossary-1 "Glossary term") or on a schedule. Scheduled reloads can be configured by creating tasks with time-based or event-based triggers.

As a tenant admin or analytics admin, you can view and delete tasks that have been created for scheduled reloads. This is done in the Administration activity center.
You can see the time of the last reload and the next planned reload. With proper permissions in the spaces where the scripts and data sources are stored, you can also create and edit these tasks.

For detailed information about tasks for scheduled reloads of scripts, including limitations and considerations, see [*Running scripts*](../ScriptEditor/reloading-scripts.htm). For information about the permissions required to reload data, see [*Managing permissions in shared spaces*](../Spaces/managing-shared-spaces.htm) and [*Managing permissions in managed spaces*](../Spaces/managing-managed-spaces.htm).

### Viewing status of script reload schedules

The Scheduling column in the scripts table displays the status of a script's tasks for scheduled reloads. An empty column means the script has no tasks. The statuses are:

- Scheduled: The script has at least one activated task.
- Schedule disabled: All tasks for the script are currently deactivated. For information about how tasks can be deactivated, see [*Reasons for task deactivation*](../Refresh/refresh-manage-tasks.htm#Reasons).

### Creating or editing reload schedules

To configure reload schedules, [tenant admins](#glossary-2 "Glossary term") and analytics admins with the appropriate space permissions for a script and its data content can create a new task or edit an existing one. The task can be configured to run on a time-based or event-based schedule.

Information noteEditing a task changes the owner of the task. See [*Ownership of tasks for scheduled reloads*](#Ownershi).

Do the following:

1. In the Administration activity center, go to Content > Scripts.
2. Select Source or Published and locate the script for which you want to add or edit a task.
3. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), and then select Schedule.
4. If you are adding a new task, click Create new task in the scheduling dialog. To edit an existing task, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to the task and select Edit.
5. Configure the task with your desired scheduling settings.

   For detailed information on how to configure tasks for scripts, see [*Reloading application data*](../Apps/reloading-apps-cloud-hub.htm).
6. Click Save.

#### Ownership of tasks for scheduled reloads

A task for data refreshes runs on behalf of the user who owns the task rather than the script owner. For the task to run successfully, the task owner must still have the correct access to the script and its data sources. Certain actions result in changes to who owns the task. The task owner is determined by the following rules:

- When you create a task to schedule refreshes of a script, you become the owner of that task.
- If another user edits or saves an existing task, they become the new owner of that task.
- If another user modifies the script, they become the new owner of all tasks for refreshes of that script.
- Publishing or republishing a script to a managed space does not change the owner of any existing tasks within the published copy.

### Deleting reload schedules

Tenant admins and analytics admins can delete existing tasks for scheduled reloads from the Administration activity center.

Do the following:

1. In the Administration activity center, go to Content > Scripts.
2. Find the script that you want to delete a task from.
3. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), and then select Schedule.
4. In the scheduling dialog, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to the task, and select Delete.

## Deleting scripts

As a tenant or analytics admin, you can delete scripts.

Do the following:

1. In the Administration activity center, go to Content > Scripts.
2. Select Source or Published.
3. Select one or more scripts and click Delete.
4. In the Delete scripts dialog, select the checkbox to confirm the deletion, and then click Delete.
