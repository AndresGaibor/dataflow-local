---
title: "Refreshing analytics data"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Refresh/refresh-analytics-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data"]
---

# Refreshing analytics data

Over time, you will likely need to refresh your analytics data on a regular basis. When you refresh your analytics assets—applications, scripts, [data flows](#glossary-2 "Glossary term"), and table recipes—they are updated to reflect the most current data. You reload an application to refresh its data. You run scripts, data flows, and table recipes to refresh the data that they export. You can refresh these analytics assets in several ways.

There are options available for manually refreshing analytics data. Scheduled refreshes offer many options for updating your analytics data based on time-based or event-based triggers, automation workflows, and user interaction with application content.

This help topic outlines generally how you can refresh the data in your application, script, data flow, or table recipe. For more specific instructions, refer to the following:

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

## Manually refreshing data

You can perform a manual refresh of the data loaded or exported by your application, script, data flow, or table recipe.

### From activity center

Do the following:

1. In your [activity center](#glossary-3 "Glossary term"), click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the application, script, data flow, or table recipe.
2. Select Reload > Reload now or Run > Run now.

Information noteThere is also a Schedule option available from the ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) menu. With respect to Qlik Cloud subscription capacities, manually running a task (that is, selecting Schedule and then selecting Run now on a task) is considered to be a scheduled reload, rather than a manual reload.

### Within an application, script, data flow, or table recipe

To reload your analytics asset, follow the applicable instructions below:

- Application: Do one of the following:

  - In your application, click the application name to open the application details area and click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > Reload now.
  - Open Data manager or  Data load editor and click Load data.
- Script: Open the script and click Run now from the Overview tab.
- Data flow: Open the data flow and click Run now from the Overview tab.
- Table recipe: Open the table recipe and click Run now from the Overview tab.

## Scheduling refreshes

You can set up tasks to schedule refreshes of applications, scripts, and table recipes. Scheduled refreshes can be time-based (for example, every Sunday evening at a specific time), or event-based (for example, when another resource finishes refreshing, or when a user clicks a button in an application).

You can schedule refreshes in the following ways:

- Creating tasks in the Qlik Cloud Analytics activity centers
- Buttons in charts
- Qlik Automate

Information noteWith respect to the Qlik Cloud subscription capacities, all of the methods outlined in this section (tasks, interactive objects, and automations) count as scheduled reloads.

### About tasks

Tasks offer a simple and convenient way to schedule refreshes based on time-based and event-based triggers. You can configure these tasks from your activity center, or from the application, script, data flow, or table recipe interface. Tasks can be chained together to refresh several applications, scripts, data flows, and table recipes in a specific order.

For more information, see [*Scheduling data refreshes with tasks*](refresh-work-with-tasks.htm) and [*Creating task chains for data refreshes*](task-chains-for-refresh.htm).

### Interactive application objects

You can allow application consumers to perform refresh actions by clicking a button object within an application sheet.

For more information, see [*Creating buttons*](../Visualizations/Button/create-buttons.htm).

### Automations

Scheduled refreshes can be configured with the Qlik Cloud connector block in Qlik Automate.

For more information, see [*Automation connectors*](../../Sense_QlikAutomation/connector-blocks/connectors-list.htm).

## Permissions

To refresh analytics data for an application, script, data flow, or table recipe, you need the appropriate space roles in the space containing the resource. If the asset loads data from files or [connections](#glossary-4 "Glossary term") in other spaces, you also need the required space roles in those spaces.

Information noteFor user-based subscriptions, you need Professional user entitlement in addition to the space roles.

For more information, see:

- [*Shared space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-shared-space-prof-full.htm)
- [*Managed space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-managed-space-prof-full.htm)
