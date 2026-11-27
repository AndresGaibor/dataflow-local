---
title: "Analyzing data without being added to a Qlik Cloud tenant"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Share/analyze-anonymous-content.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Using analytics to explore data"]
---

# Analyzing data without being added to a Qlik Cloud tenant

With Qlik Anonymous Access, users outside of a Qlik Cloud tenant can explore analytics from Qlik Sense apps. This help topic outlines how you can interact with this analytics content when it is shared with you.

When you access content through anonymous access, no login is required. Your session lasts for 15 minutes. To continue using the application, you can refresh your browser to start another 15-minute session.

For more information about anonymous access, see [*Sharing application content with anonymous access*](share-anonymous-access.htm).

Qlik Cloud Government note

Qlik Anonymous Access subscriptions are not available in Qlik Cloud Government.

Information note

This help topic refers to other help topics that focus on using Qlik Sense. Some functionality documented in these help topics is not available unless you are a member of a Qlik Cloud tenant.

## Methods of accessing analytics from a Qlik Anonymous Access subscription

If you do not have access to Qlik Cloud, there are two possible ways in which Qlik Anonymous Access content has been shared with you: via an anonymous access link to an application, or as content embedded directly into another web page or application.

### Exploring apps from anonymous access links

An application could have been shared with you as a link. When you open this link, you are not required to log in or provide any credentials, and you immediately have access to the analytics content within it.

### Analyzing data from embedded analytics

You might be interacting with Qlik analytics content that is embedded directly into an external web page or application. In this case, the analytics could take the form of one or more embedded [sheets](#glossary-0 "Glossary term"), or it could consist of individual [visualizations](#glossary-1 "Glossary term").

## User interface

The user interface you see depends on whether you are viewing a series of sheets or a single visualization. For example, if you have been given a link to an application, all sections below will be relevant. For analytics that are embedded into external locations, you might notice differences between the sections below and your own options.

### Navigating the application

#### Using the navigation bar

The navigation bar at the top of the interface lets you switch between different views in the application. Use the drop down menu in the navigation bar to the switch between:

- Overview: Get a high-level overview of application content that is available to you. The Sheets and Bookmarks tabs are available. Click a sheet to open it, and click bookmarks to apply pre-defined data filters across the application. Search for content using the search bar.

  [*Application overview*](../Apps/app-overview-cloud-hub.htm)
- Sheet: This is where you can explore analytics in the form of [sheets](#glossary-2 "Glossary term"). Click ![Left arrow](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_left.svg) and ![Right arrow](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_right.svg) to switch between sheets, or use the expandable Assets panel.

  [Analysis mode in sheet view](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Sheets/sheet-view.htm#Analysis)

#### Application details area

Details is not available to anonymous users.

#### Touch screen mode

You can toggle touch support on and off. Click ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) in the navigation bar at the top of the interface, then use the toggle switch for ![Touch screen mode](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_touch_outline.svg) Touch screen mode.

### Exploring sheets

A [sheet](#glossary-3 "Glossary term") is a collection of visualizations that have been arranged to help you analyze and explore data. Selections are global across all application sheets. This means that when you make a selection and switch sheets, the selection remains applied for all other sheets.

#### Assets panel

Click Assets to expand a condensed assets panel, where you can select:

- Sheets: Navigate to other sheets and access more options for each sheet.
- Bookmarks: View all [bookmarks](#glossary-4 "Glossary term") , and apply them to explore the analytics with the pre-configured [selections](#glossary-5 "Glossary term"). For more information about bookmarks, see [*Bookmarking selections*](../Bookmarks/keep-track-of-important-data.htm).

[*Assets panel in analysis mode*](../Sheets/sheet-view.htm#AssetsAnalyze)

#### Downloading sheets

You can download sheets as PDF by doing any of the following:

- Click ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) in the navigation bar at the top of the interface, and then click Download sheet as PDF.
- Expand Assets, go to Sheets, and then click ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to a sheet. Then, click Download sheet as PDF.

### Exploring the analytics with selections

[Selections](#glossary-6 "Glossary term") are a foundation of interactive analysis in Qlik Sense. Apply selections to filter the data across the analytics content. By making selections, you can uncover insights about specific subsets of the data, and perform comparative analysis.

For full details, see [*Exploring with selections*](../Selections/SelectionsToolbar/work-with-selections.htm) and associated topics.

The selections bar shows you the current selections that you have currently made, and allows you to manage them.

![Selections bar with three selections, one is locked.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_SelectionsBarLock.png "Click to view full size")

You can make selections by:

- Interacting with visualizations in various ways.

  [*Types of selections in visualizations*](../Selections/selection-in-visualization.htm)
- Searching within charts or in the selection bar.

  [*Searching within selections or visualizations*](../Selections/SelectionsToolbar/search-selections.htm)
- Using the selections tool. During analysis, click ![Selections tool](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_selections_tool.svg) to open selections view. The selections tool provides a standalone view of the analytics content that can be filtered, and allows you to apply selections.

  [*Using the selections tool*](../Selections/use-selection-tool.htm)
- Using smart search, the global search tool for the analytics content.

  [*Using smart search*](../Search/use-smart-search-tool.htm)

Other actions on selections include:

- Click a selected field in the selection bar. This allows you to search in existing selections, lock or unlock them, and further modify them.
- In the selection bar, click ![Remove](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_remove.svg) to remove a selection. Clear all selections by clicking the ![Clear selections](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_clear_selections2.svg) icon.
- Step forward and backward in your selections by clicking ![Step backward in selections](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_selections_back.svg) and ![Step forward in selections](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_selections_forward.svg).

### Interacting with visualizations

Visualizations are interactive and allow you to make selections to filter their data. See [*Exploring the analytics with selections*](#Selections).

Additionally, you might be able to right-click the visualization or use the context menu ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) to perform other actions, including:

- ![Expand](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expand_3_outline.svg) Full screen: Download the visualization in different formats, such as an image, PDF, or data file.
- ![Info icon](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_info_outline.svg) Show details: See the fields and master items that make up the visualization. You can view their dependencies to see the fields that comprise them and their sources.

  [*Viewing details for visualizations*](../UserInterface/show-details.htm)
- ![Controls](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_control_outline.svg) Exploration menu: Change certain visualization properties, without making selections or editing the sheet. See: [*Visual exploration*](../UserInterface/visual-exploration-menu.htm)
- ![Table](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_outline.svg) View data: View the data for a visualization in a table.
- ![Download](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_download.svg) Download: Download the visualization in different formats, such as an image, PDF, or data file.

  [*Downloading visualizations*](../Download/downloading-visualization.htm#DownloadChart)

## Additional resources

For more help with using Qlik Sense, there are many additional resources available:

- There are many other help topics available in the [Qlik online help](http://help.qlik.com/) to help you learn.
- Training, including free online courses, is available on [Qlik Learning](https://learning.qlik.com/).
- Discussion forums, blogs, and more can be found in [Qlik Community](http://community.qlik.com/).
