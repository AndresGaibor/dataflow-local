---
title: "Using the selections tool"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Selections/use-selection-tool.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Using analytics to explore data", "Exploring with selections"]
---

# Using the selections tool

The selections tool gives an overview of every dimension and field in an application. It also gives a more detailed view of selected data, so that you can explore associations in dimensions that have not been used.

During analysis, click ![Selections tool](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_selections_tool.svg) to open selections view.

The selections tool is divided into two sections: Selections and App dimensions. The Selections section displays the fields that have active selections. The App dimensions section displays all dimensions and fields. Both sections are sorted alphabetically. By default, application dimensions only displays master items. Select Show fields to show all the fields that have been loaded into the application.

Selections tool displaying the two sections Selections and App dimensions.

![Selections tool view.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_SelectionTool.png "Click to view full size")

## Making and clearing selections

You can make several selections consecutively. Click ![Confirm ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_tick.svg) or click outside the list, but within the selections tool area, to confirm your selections. These dimensions will move up to Selections. Click the toolbar to close the selections tool.

In Selections, you can clear a selection in a field by clicking ![Cancel](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_remove.svg). The field is then moved down to App dimensions.

When you are in the selections tool, you can still use the options in the selections bar: step back, step forward, and clear all selections. In each dimension you have the usual list options: selection menu, clear selection, cancel selection, confirm selection, and search.

## Searching in the App dimensions section

App dimensions has a search box that is useful when you have many dimensions and fields. You can search by field or dimension title. Your search string can consist of one or more words, or only a part of word. The search is not case sensitive, but only exact string matches are displayed. A search for "numbers" will not display fields with the string "number", but a search for "mbe" will.

## Scrolling in the selections tool

You can drag the scroll bar to scroll horizontally through a section. When you scroll in one section the other section is unaffected.

The dimension lists also have scroll bars, for vertical scrolling.

## Generating insights

Associative insights reveals relationships in your data. The Qlik cognitive engine searches your data model for excluded values in a subset of fields. It then highlights those values, so you can explore them.

Once you have made a selection, click Generate insights. Cards are shown in the right hand panel. The cards show the effect of your selection on dimensions and measures in your data. See: [*Discovering your data with associative insights*](associative-insights.htm)

## Calculated dimensions

You can show a calculated dimension in the selections tool by adding it as a master dimension. See [*Reusing dimensions with master dimensions*](../Dimensions/create-master-dimension.htm).

When a selection is made in a calculated master dimension, it is still shown in the App dimensions section, with selections shown in green. Dimensions that correspond exactly to selected fields are hidden from the App dimensions section.

## Learn more

- [*Searching within selections or visualizations*](SelectionsToolbar/search-selections.htm)
- [*Locking and unlocking selections*](SelectionsToolbar/lock-unlock-selections.htm)
- [*Exploring with selections*](SelectionsToolbar/work-with-selections.htm)
- [Searching and Selecting data](/lnk/Searching_selecting_data)

Related learning:

- [Searching and Selecting data](/lnk/Searching_selecting_data)
