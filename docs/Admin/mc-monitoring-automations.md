---
title: "Monitoring automations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-monitoring-automations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing automations"]
---

# Monitoring automations

Use the Automations, Runs, and Connections tabs in the Administration activity center to review tenant automations, run history, and connections, and filter each list.

## Viewing automation information

A tenant admin or analytics admin can see all the automations under Automations in the Administration activity center.

The Automations table lists all automations and runs for the tenant. The Automations tab displays information about each automation, like whether the automation is enabled or disabled, the status of the last automation run, and the automation run mode. The Runs tab displays information of all the runs during the last 30 days, including the run title, context and duration. Information about the inclusion of third-party blocks is available on both these tabs.

The Connections tab displays information of the configured connectors, including the status, owner, and space where they reside.

You can perform a set of actions by clicking ![Three dots to expand menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) at the end of the automation row. The menu options allows you to view the automation's runs, change owner, enable or disable the automation, and delete it.

When you select one or more automations, you can perform bulk actions view the runs for the selected automations, enable, disable, or delete them.

![Automations table from the management console with three selected automations and bulk action menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_mc_automations_table_bulk_actions.png)

## Automation monitoring filters

The Automations, Runs, and Connections tabs can be filtered to easily find a specific automation or run. All three tabs allow the use of multiple filters, allowing you to narrow down the list of automations or runs.

The Automations tab can be filtered by:

- Automation name
- Last run status
- Owner name
- Space
- Third-party blocks

The Runs tab can be filtered by:

- Automation name or run title
- Run status
- Context
- Automation by name
- Owner name
- Run start time
- Space at runtime
- Executed by
- Third-party blocks

The Connections tab can be filtered by:

- Connection name
- Connector
- Owner name
- Spaces

Information noteThe usage of third-party blocks in an automation run may incur additional costs depending on your type of subscription.
In the Automations tab you can use the Third-party blocks filter to see which automations include third-party blocks, while in the Runs tabs, you can use the Third-party blocks filter to see which runs have actually used a third-party block when executing an automation workflow.

Tip noteThe Run mode filter in the Automations tab is useful to see the upcoming automations and what kind of triggers they have. The Context filter in the Runs tab shows how previously run automations were triggered. To learn more about automation run statuses, see the [Runs section in Navigating the user interface](../../Sense_QlikAutomation/introduction/navigating-UI.htm#Runs).
