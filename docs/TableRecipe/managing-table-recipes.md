---
title: "Managing table recipes"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/TableRecipe/managing-table-recipes.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Table recipe"]
---

# Managing table recipes

What you can do with a table recipe depends on the type of space where the table recipe is located. In your personal space, you can manage your own table recipes. In a shared space, depending on your permissions in that space, you can manage both your own table recipes and those of other users. In managed spaces, there are fewer options for managing table recipes as access is more governed. For more information about what you can do, see [*Table recipe actions*](../Spaces/permissions-managed-space-prof-full.htm#Table) and [*Table recipe actions*](../Spaces/permissions-shared-space-prof-full.htm#Table).

From your catalog, and depending on the space, the available actions are:

- [*Copying the link to a table recipe*](#Copying).
- [*Adding table recipes to collections*](#Adding).
- [*Sharing table recipes*](#Sharing)
- [*Moving table recipes*](#Moving).
- [*Editing table recipe details*](#Editing).
- [*Duplicating table recipes*](#Duplicat).
- [*Running table recipes*](#Running).
- [*Scheduling table recipes runs*](#Scheduli).
- [*Configuring table recipes notifications*](#Configur).
- [*Seeing table recipe details*](#Seeing).
- [*Viewing a table recipe lineage*](#Viewing).
- [*Viewing a table recipe impact analysis*](#Viewing2).
- [*Exporting table recipes*](#Exportin).
- [*Converting table recipes to script*](#Converti).
- [*Converting table recipes to a data flow*](#Converti2).
- [*Opening a table recipe in a new tab*](#Opening).
- [*Deleting table recipes*](#Deleting).

## Copying the link to a table recipe

You can copy the link to a specific table recipe and use it as bookmark or share it with collaborators with access to the table recipe.

Do the following:

- Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the table recipe and select Share > Copy link.

## Adding table recipes to collections

Collections enable you to group content such as table recipes, data flows, applications, charts, notes and links. To add a table recipe to a collection, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Manage > Add to collection.

By default, collections are private. Tenant admins and analytic admins can make collections public to share them with all other members of the tenant. Public collections do not change members' access to content in spaces. Members will only be able to see content in public collections to which they already have access. To make a collection public, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the collection, select Make public, and click Make public. To make a public collection private again, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), select Make private, and click Make private.

## Sharing table recipes

You can share a table recipe by inviting a user, group, or everyone in your tenant to the space where it is stored.

Do the following:

1. In the catalog, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the item to be shared and select Share > Invite.
2. Search for users or groups by name or email address.
3. Select space permissions for the users or groups.
4. Or, select permissions for Anyone at <your tenant name> from the dropdown list.
5. Click Done.

The users receive access to the shared item and all other content in the space.

## Moving table recipes

You can move table recipes between shared spaces as well as between a shared space and a personal space.

If you move a table recipe with a run schedule between spaces, the run schedule is deleted. Recreate the schedule in the new space if required.

Do the following:

1. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the table recipe and select Manage > Move to space.
2. Select the new space from Space.
3. To open the new space, select Navigate to space.
4. Click Move.

## Editing table recipe details

You can change the titles and descriptions of your table recipes. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the table recipe that you want to edit and then select Manage > Edit details. You can also change the tags used with the table recipe. Tags are used to group table recipes with related content. When adding new tags to a table recipe, users can view all tags that exist in the tenant.

## Duplicating table recipes

You can duplicate any table recipe you have access to by clicking ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the table recipe and then selecting Manage > Duplicate. The duplicate can be modified.

Duplicating table recipes has several uses. For example, you can duplicate a table recipe as a form of version control, and store older ones a space created for archival purposes.

Duplicated table recipes keep the original data source. If you did not create the original data source used in the table recipe or if they are not available in the space, you will have to reconfigure the data source in the table recipe.

## Running table recipes

You can manually run your recipe from the catalog, without having to go to the Editor view. The latest configuration of the recipe will be used, along with the latest data from the data source. A new output will be generated if the run is successful.

Do the following:

- Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the table recipe and select Run > Run now.

## Scheduling table recipes runs

Create tasks to schedule runs for your table recipe. The schedule can use time-based or event-based triggers.

To create a task:

1. Do one of the following:

   - In your [activity center](#glossary-0 "Glossary term"), click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the table recipe and select Run > Schedule.
   - In your table recipe, open the Overview section and click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > Schedule.
2. Click Create new task.
3. For Task name, enter a name for the task.
4. Optionally add a Description.
5. Under Based on, select the trigger for the task. You have the following options:

   - Time-based: Schedule the refresh to occur at a specific point in time. Then, configure the task with the associated settings for that trigger.

     The following time-based triggers are available:

     - Daily
     - Weekly
     - Monthly
     - Yearly
   - Event-based: Schedule the refresh to start when a specific event takes place.

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

   - In your [activity center](#glossary-1 "Glossary term"), click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the table recipe and select Run > Schedule.
   - In your table recipe, open the Overview section and click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > Schedule.
2. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to a task, and select any of the available options. Alternatively, switch to the History tab to view a detailed history for when the task was run.

For more information, see [*Managing tasks for data refreshes*](../Refresh/refresh-manage-tasks.htm).

### Limitations and considerations

- A task for refreshing data is deactivated if it fails to run five times in a row. If you own the task, you will receive [notifications](#glossary-2 "Glossary term") when this happens. Notification settings can be customized for a single application, all applications in a space, or all applications in a tenant. For more information, see [*Ownership of tasks*](#Ownershi).
- If the task owner leaves or is deleted from the tenant, another user has to take ownership of the task, or delete and recreate it. Otherwise, its scheduled refreshes will fail. For information about how to change this ownership, see [*Ownership of tasks*](#Ownershi).
- If you have a high number of queued and running data refresh processes (and additional concurrent CPU and memory intensive processes), you might notice that some refresh processes run, in some cases, noticeably after their scheduled start time.
- Tasks for refreshing data are not included for the published copy of a table recipe. Published table recipes must have their tasks reconfigured on the version in the managed space.
- If your table recipe has tasks for refreshing data, and you move it between spaces (personal or shared spaces), these tasks are deactivated. You can reactivate them when ready to resume the scheduled refreshes. See [*Activating and deactivating a task*](../Refresh/refresh-manage-tasks.htm#Activating).

### Ownership of tasks

A task for data refreshes runs on behalf of the user who owns the task rather than the owner of the application, script, data flow, or table recipe. For the task to run successfully, the task owner must still have the correct access to the application, script, data flow, or table recipe and its data sources. Certain actions result in changes to who owns the task. The task owner is determined by the following rules:

- When you create a task for running a table recipe, you become the owner of that task.
- If another user edits or saves an existing task, they become the new owner of that task.
- If another user modifies the table recipe in Editor, they become the new owner of all tasks for scheduled runs of that table recipe.
- Publishing or republishing a tale recipe to a managed space does not change the owner of any existing tasks within the published copy.

### Administering tasks for refreshing data

Tenant admins and analytics admins can edit and delete tasks for scheduled data refreshes. This is done in the Administration activity center.
For more information, see:

- [*Managing applications for tenant and analytics administrators*](../Admin/mc-administer-apps.htm)
- [*Managing scripts for tenant and analytics administrators*](../Admin/mc-administer-scripts.htm)

## Configuring table recipes notifications

You can access the notifications configuration panel of a table recipe to set or modify which event will trigger a notification, and on which support to receive it.

Do the following:

- Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the table recipe and select Manage > Notifications settings.

## Seeing table recipe details

Using this option will lead you to the Overview page of the table recipe, where you can see all the general information of your table recipe. See [*Overview*](navigating-table-recipes.htm#Overview).

Do the following:

- Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the table recipe and select Details.

## Viewing a table recipe lineage

Lineage tracks data and data transformation backwards from the table recipe to its original source. This provides an interactive representation of the origins of the data that this table recipe processes. For more information on lineage, see [*Analyzing lineage in Analytics*](../Catalog/lineage.htm).

Do the following:

- Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the table recipe and select Tools > Lineage.

## Viewing a table recipe impact analysis

Impact analysis shows the downstream dependencies of table recipe output. It answers questions about what other applications, scripts, or other resources would be directly or indirectly impacted by changes to the table recipe. For more information on impact analysis, see [*Analyzing impact analysis in Analytics*](../Catalog/impact-analysis2.htm).

Do the following:

- Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the table recipe and select Tools > Impact analysis.

## Exporting table recipes

You can export table recipes from the Analytics activity center as .trp files. These can be uploaded into other Qlik Cloud Analytics tenants or Qlik Sense versions.

The exported table recipe is saved in the default download folder of your web browser.

Do the following:

- Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the table recipe you want to export and select Download > Export.

## Converting table recipes to script

You can convert table recipes into scripts. Converting duplicates the table recipe and then converts it into a script.

Do the following:

- Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the table recipe you want to convert and select Manage > Duplicate as script.

## Converting table recipes to a data flow

You can convert table recipes into data flows. Converting duplicates the table recipe and then converts it into a data flow.

Do the following:

- Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the table recipe you want to convert and select Manage > Duplicate as data flow.

## Opening a table recipe in a new tab

You can open a specific table recipe in a new browser tab to avoid interrupting your current work.

Do the following:

- Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the table recipe you want to open and select Open in new tab.

## Deleting table recipes

You can completely remove unnecessary table recipes from your catalog.

Do the following:

1. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the table recipe you want to delete and select Delete.
2. Click Delete.
