---
title: "Activating chart exploration in a straight table"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/StraightTable/sn-straight-table-chart-exploration.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations", "Creating straight tables", "Configuring straight table properties"]
---

# Activating chart exploration in a straight table

Chart exploration allows application consumers and other users that do not have edit rights to customize the original straight table when they are in analysis mode.

Chart exploration mode is a great way to quickly remove or add data, and then share it, download it, or bookmark the new table state. It is very helpful in applications that have many viewers with different needs.

Users with Can edit rights can make changes to the table using chart exploration, click Edit sheet, and save those changes to the original table.

## Turning on chart exploration

Application developers can turn on Chart exploration in the properties panel.

Do the following:

1. In the properties panel, expand the Chart exploration section.
2. Toggle on Enable chart exploration.
3. Choose between the following under Visibility option:

   - Auto: Chart exploration panel is visible when users open the sheet.
   - Minimized: Chart exploration is turned on, but not visible when users open the sheet. Users can open it in the hover menu by clicking ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and then ![Controls](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_control_outline.svg) Chart exploration.

## Preparing the table for chart exploration

For a table item to be available in chart exploration mode, the table creator (or a user with Can edit rights) must have added those fields, master items, or expressions to the table as columns or alternative columns. For more information, see [*Creating straight tables*](create-sn-straight-tables.htm).

## Using chart exploration as a consumer

When analyzing a sheet, chart exploration is either visible by default, or it can be activated in the ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) menu under ![Controls](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_control_outline.svg) Chart exploration.

For more information, see [*Using chart exploration*](sn-straight-table.htm#Chart).
