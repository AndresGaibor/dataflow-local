---
title: "Working with applications"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/create-apps-visualizations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data"]
---

# Working with applications

Qlik Sense applications are purpose-built applications created with data. Application users explore the data through [visualizations](#glossary-1 "Glossary term") selected and enhanced by application developers.

Applications are created by three primary methods depending on skill level and how much data manipulation is required upon dataload. Options from basic to advanced include:

1. Uploaded once and never modified.
2. Modified manually through Data manager.
3. Replaced or refreshed with net new changes.

When you create an application, you add it to a space. There are two kinds of spaces in which you can create new applications: Personal spaces are private to individual users. Applications and data sources added there cannot be shared with other users. Shared spaces are collaborative. You can create applications and other members of a shared space can access them. You can also work with other space members to develop applications. Data sources in shared spaces are shared with other members. When your application is complete, you can invite your application audience to your shared space or publish the application to a managed space. For more information about working with shared and managed spaces, see [*Working in spaces*](../Spaces/Spaces.htm).

The foundation of an application is the data model and [load script](#glossary-2 "Glossary term"). Measures and [dimensions](#glossary-3 "Glossary term") are reusable data items used to build [charts](#glossary-4 "Glossary term"). Sheets and [stories](#glossary-5 "Glossary term") display and organize your visualizations. Discoveries can be made by applying filters and [selections](#glossary-6 "Glossary term").

A Qlik Sense application with selections applied

![Make discoveries by applying selections](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_CreatingAppsExample-saas.png "Click to view full size")

[Permissions](#glossary-7 "Glossary term") are required to create and interact with applications. If application functionality is not available to you, contact your administrator for appropriate permissions.

## Foundations

### Data manager, Data load editor, and the data catalog

The [Data manager](#glossary-8 "Glossary term") lets you quickly add and transform data. You can also associate data tables. The [Data load editor](#glossary-9 "Glossary term") uses scripts to connect to a data source and retrieve the data. The [data catalog](#glossary-10 "Glossary term") allows you to quickly see all datasets to which you have access. You can add data from multiple files at once. See [*Loading and managing data with Data Manager*](../LoadData/managing-data.htm), and [*Using Data load editor*](../LoadData/use-data-load-editor.htm).

### Measures

Measures are calculations used in visualizations. Measures are created from an expression composed of aggregation functions, such as Sum or Max, combined with one or several fields. See [*Measures*](../Measures/measures.htm) and [*Using expressions in visualizations*](../ChartFunctions/use-expressions-in-visualizations.htm).

### Dimensions

Dimensions are fields used in visualizations. Dimensions determine how the data in a visualization is grouped. For example: total sales per country or number of products per supplier. See [*Data grouping with dimensions*](../Dimensions/dimensions.htm) and [*Fields*](../DataSource/fields.htm).

## Structure and visuals

### Sheets

Sheets contain data visualizations, such as charts and tables. You create structure in your application by grouping visualizations on sheets. For example, you could have a sheet for North American sales, and a different sheet for Europe. For more information, see [*Working with sheets*](../Sheets/working-with-sheets.htm) and [*Choosing the right visualization*](creating-visualization.htm).

### Bookmarks

Bookmarks are shortcuts to a certain set of selections and chart expansions.  See [*Bookmarking selections*](../Bookmarks/keep-track-of-important-data.htm).

### Stories

Stories are based on snapshots of visualizations. You present your data by creating a story that guides you to new insights by combining snapshots of data at specific times and selection states. See [*Sharing insights with data storytelling*](../StoryTelling/use-data-storytelling.htm).

Related learning:

- [How do I create an application?](/lnk/How_create_app)
- [Getting started with Qlik Sense](/lnk/Getting_started_QS)
