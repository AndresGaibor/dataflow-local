---
title: "Including variable states in bookmarks and reports"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Variables/using-variables-with-bookmarks.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Using expressions in visualizations", "Using variables in expressions"]
---

# Including variable states in bookmarks and reports

You can configure variables to have their states included in bookmarks and reports.

By default, variable states are not included when users create bookmarks or reports. Application creators and application users have different options for including variable states in bookmarks and reports.

You can configure your application's variables to have their current state included when users create a bookmark or report. By selecting Include current value of variable when creating bookmarks, application creators can have variable states automatically included in bookmarks and reports.

You can also choose to include variable states in bookmarks and reports. When creating bookmarks, you can use Save all variables states. When creating subscriptions to reports, you can select the option Use variable state to include variable states in the report. For more information, see:

- [*Creating bookmarks*](../Bookmarks/create-bookmark.htm)
- [*Creating a subscription*](../Reporting/Subscriptions/Subscription-reports.htm#Creating)

## Advantages of setting Include in bookmarks on variables

There are two advantages to setting Include current value of variable when creating bookmarks on variables over the other options. You can choose which variables to have their states included in bookmarks and reports on an individual basis. This gives you more control over what variable states are included.  Script variable states are not included when you use Save all variables states in a bookmark or Use variable state in a subscription.

## Interactions between the variable setting and bookmark and subscription settings

If Include current value of variable when creating bookmarks is selected, it will overrule the option selected for Save all variable states in bookmarks and Use variable state in subscriptions.

The table below summarizes the behavior of bookmarks and reports for including variable states when Include current value of variable when creating bookmarks and Save all variable states/Use variable state are used.

Interaction summary

| Include current value of variable when creating bookmarks | Save all variable states /Use variable state | Result |
| --- | --- | --- |
| Yes | Yes | Variable states of all variables included. |
| Yes | No | Variable states of variables with Include current value of variable when creating bookmarks selected included. |
| No | Yes | Variable states of all variables included. |
| No | No | Variable states not included. |

## Saving variable states in bookmarks

Do the following:

1. When editing a sheet, click ![Variables](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_variables_outline.svg) in the edit bar on the sheet to open the variables dialog.

   The variables dialog opens.
2. In the row of the variable you want to delete, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Edit.
3. Select Include current value of variable when creating bookmarks.
4. Click Save.

## Limitations

Include current value of variable when creating bookmarks is not available for script variables.
