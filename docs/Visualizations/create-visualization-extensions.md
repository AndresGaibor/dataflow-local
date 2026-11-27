---
title: "Creating a visualization using a custom object"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/create-visualization-extensions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations"]
---

# Creating a visualization using a custom object

You can enhance your applications with custom-objects.

Custom objects are visualization extensions.

Information noteExtensions that contain resource requests to external resources must have its origins allowlisted in the Content Security Policy, else the extension will be blocked from rendering.

You can make adjustments to custom objects in the standard edit view and apply filters to them.

## Adding a custom object to the sheet

You start creating a visualization by dragging a visualization extension onto a [sheet](#glossary-0 "Glossary term").

Do the following:

1. Click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit sheet in the toolbar.
2. Click ![Extension](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_puzzle_outline.svg) in the panel on the left-hand side to expand custom objects.
3. Drag a visualization extension onto the sheet.

   You can drop it in an empty location on the sheet, split the area of an existing visualization into two, or replace an existing visualization.

   Tip noteIf you double-click a [custom object](#glossary-1 "Glossary term"), it is added to the sheet immediately.
4. Change the required settings for the custom object in the properties panel. The required settings are defined by the extension developer, this can be dimensions, measures, or other settings.

You now have a complete visualization that you can start using while exploring the data in the application.
