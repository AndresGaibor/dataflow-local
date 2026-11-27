---
title: "Creating dynamic views and charts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DynamicViews/creating-dynamic-views.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Managing your data", "Managing data with dynamic views"]
---

# Creating dynamic views and charts

[Dynamic views](#glossary-0 "Glossary term") can be added from the Assets panel in sheet edit mode. You can add dynamic [charts](#glossary-1 "Glossary term") from your dynamic views to your [sheets](#glossary-2 "Glossary term").

Dynamic views in the Assets panel when editing a new sheet

![Dynamic views in the Assets panel of a new sheet](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_dynamic_view_assets_panel-saas-rev.png "Click to view full size")

## Creating dynamic views

When you create a dynamic view, you can limit how many rows are brought in as a part of the dynamic view. This can help prevent returning too many rows if your dynamic views are connecting to a very large data set.

Do the following:

1. In the Edit mode of a sheet, click Dynamic views.
2. Click Create new.
3. After Name, enter a name for the view.
4. After Template app, select a template application.
5. After Row limit, optionally select to use a Row limit expression and optionally set a Maximum row count.
6. Click Create.

## Adding dynamic charts to sheets

Dynamic charts can be added to sheets from the Assets panel.

If you have editing [permissions](#glossary-3 "Glossary term") in the template application, you can edit the master chart upon which the dynamic chart is based.

To edit a dynamic chart, select a dynamic chart while the sheet is in Edit mode and select Edit source app.

## Editing dynamic views

You can edit your dynamic views and change your row limits. You cannot change the template application used by a dynamic view.

Do the following:

1. Select a dynamic view from the dynamic views drop-down.
2. Click ![More information](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg).
