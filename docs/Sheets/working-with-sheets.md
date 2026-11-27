---
title: "Working with sheets"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Sheets/working-with-sheets.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data"]
---

# Working with sheets

Organize data [visualizations](#glossary-0 "Glossary term") for your application consumers in [sheets](#glossary-1 "Glossary term"). Make it easier for them to analyze data by structuring your ideas and defining the purpose of your application.

Sheets are components of Qlik Sense applications that group and present visualizations of your application data. Visualizations are [charts](#glossary-2 "Glossary term") or other representations of application data, such as bar charts and pie charts. Application consumers can use your sheets and visualizations to explore data to find insights and make discoveries.

Information noteYour user interface may look different from the interface shown in the screenshots below. For example, the application creator may have hidden the toolbar or sheet header. For more information, see [*Hiding toolbar, sheet header, and application navigation bar options*](../Apps/style-app.htm#Hiding).

Sheets are developed in edit mode and viewed in analysis mode. Analysis mode is the standard view of a sheet most of your application users will see. In it, users can make [selections](#glossary-3 "Glossary term") in the data that is displayed in visualizations. Selections are applied to all visualizations in the application, enabling users to explore your application's data in depth.

To learn more about selections and exploring data in visualizations, see [*Exploring with selections*](../Selections/SelectionsToolbar/work-with-selections.htm) and [*Exploring data with visualizations*](../Selections/make-selection.htm).

Sheet in analysis mode with filter panes on the left to select and filter data

![Sheet in analysis mode with filter pane so that users can select and filter data easily.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Sheets/ui-gen-sheet-analysis-dev.png "Click to view full size")

Build sheets for your application in edit mode. When you create a new application, it is good practice to first build a structure of empty sheets, where each sheet represents an idea or a goal. This gives a good overview of the application. For example, you are creating an overview of your company's key metrics, sales, and margins by state, region, and product. Instead of having all this information in one place, you could structure it by having one sheet for each purpose.

Each sheet has a purpose and an idea of its own

![Three different sheets.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_AppOverviewSheets.png "Click to view full size")

Click Edit sheet in an open sheet to start building a sheet. The edit mode interface helps you quickly create visualizations and lay them out in a sheet. With edit mode's smart grid, you can quickly place new visualizations beside or below a chart and drag them into their final positions. You can easily create filters in your visualizations, limiting the data that displays in the charts.

Sheet in edit mode

![Sheet view in edit mode.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Sheets/ui_gen_sheet_edit-saas-rev2.png "Click to view full size")

You can continue to make selections in visualizations while editing a sheet. This helps you test out your visualizations as you develop your sheets.

In edit mode, you can do the following:

- Add new charts.
- Change the sheet title.
- Edit sheet layouts and properties.
- Add filters to your charts.
- Reload application data (if you have permission in the space).
- Add data to your application (if you have permission in the space).
- Add new sheets.

You can organize your sheets in groups. This allows you to collect related sheets together into collapsible groups in both the application overview and assets panel for easier navigation. For more information, see [*Grouping sheets*](grouping-sheets.htm).

## Permissions

Editing sheets requires the appropriate permissions in the space the application is in. In user-based subscriptions, you also need a Professional user entitlement.

In [shared spaces](#glossary-4 "Glossary term"), you can create and edit sheets with the following permissions:

- Owner
- Can manage
- Can edit data in applications
- Can edit

In [managed spaces](#glossary-5 "Glossary term"), you can create and edit sheets with the following permissions:

- Owner
- Can manage
- Can contribute

## Limitations for application content that will be shared or exported

Applications, sheets, and charts are shared and exported in several ways. Technical limitations can affect whether these capabilities function as intended. If your application exceeds these technical limitations, the sharing or exporting capabilities will not work.

For specific lists of these limitations for each capability, see:

- [*Qlik Reporting Service specifications and limitations*](../Reporting/Reporting-service-specifications-limitations.htm)
- [*Capturing and sharing insights using Notes*](../Notes/notes-overview.htm)
- [*Downloading application content*](../Download/downloading-visualization.htm)
- [*Monitoring visualizations*](../Hub/monitor-charts-hub.htm)
- [*Scheduling reports with subscriptions*](../Reporting/Subscriptions/Subscription-reports.htm)
- [*Sharing visualizations*](../Share/sharing-visualizations.htm)
