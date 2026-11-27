---
title: "Exploring analytics with the Qlik Analytics mobile app"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Mobile/qsmsaas-work-with-apps.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Analytics mobile app"]
---

# Exploring analytics with the Qlik Analytics mobile app

Use the Qlik Analytics mobile app to access and consume Qlik Sense applications that are available to you on a Qlik Cloud [tenant](#glossary-1 "Glossary term").

Information noteThe Qlik Analytics mobile app will use Wi-Fi when it is available. If Wi-Fi is not available, the app will attempt to use cellular data. If you do not want the app to use cellular data, disable cellular data on your device.

When you have opened an app in the Qlik Analytics mobile app, the [sheets](#glossary-2 "Glossary term") are presented at the top. Swipe the sheet title to navigate to the next or previous sheet. Tap the sheet title to get a list of sheets organized by public and private sheets.

You can use the Qlik Analytics mobile app in both portrait mode or landscape mode.

You can make [selections](#glossary-3 "Glossary term"), and on Apple devices you can share [visualizations](#glossary-4 "Glossary term") with others.

At the bottom you have a toolbar for selections and [bookmarks](#glossary-5 "Glossary term"). The selections tool can be expanded and you can then search for [dimensions](#glossary-6 "Glossary term") and fields, view the current selections and make selections in fields. Tap ![bookmarks](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bookmark.svg) to open the bookmark module.

[The associative selection model](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Selections/associative-selection-model.htm)

[Selection options](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Selections/SelectionsToolbar/work-with-selections.htm)

## Interacting with visualizations

There are two different ways to interact with visualizations in the Qlik Analytics mobile app.

- Tap the visualization to open it in full screen mode. When a visualization is in full screen mode, you can make selections.
- Charts with a gesture icon ![gesture](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_gesture.svg) indicates that you can make selections directly in the [chart](#glossary-7 "Glossary term"), without going into full screen mode.

On all charts, you can tap ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) to show a menu where you can select to view data as a table, and monitor the visualization in the [hub](#glossary-8 "Glossary term").

Select View data to see the data as a table

![Data in table format](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_MobileViewData.png "Click to view full size")

### Interacting in full screen mode

Tap the visualization to open it in full screen mode. When a visualization is in full screen mode, you can make selections. On Apple devices, tap ![bookmarks](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_share_2.svg) to share visualizations with others.

Make selections by tapping and drawing in the different visualizations.

When you make a selection, all associated visualizations are updated immediately to reflect the selection. Confirm the selection by tapping ![ ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_tick.svg). Cancel a selection by tapping ![Cancel](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_remove.svg).

By default, new selections in a visualization are added to the previous ones. Deselect an item by tapping it. You can also move back and forward in your selections.

### Interacting directly in the chart

Charts with a gesture icon ![gesture](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_gesture.svg) indicates that you can make selections directly in the chart, without going into full screen mode. Tap on the chart's title bar to open it in full screen mode.

The following charts have a gesture icon, meaning you can interact directly in them:

- Treemaps
- Tables, including View data tables
- Text & image objects

In treemaps, tooltips can be activated by long pressing on a leaf node.

In tables, including view data tables, you can sort on [measures](#glossary-9 "Glossary term") and dimensions, resize columns, bring the table into full screen mode, and make selections.

If you touch and hold on a cell value you can select to copy the value or to expand the row. Copying the cell value also includes any image or mini chart present in the cell. Expanding the row means you see all of the row data in full screen mode transposed into a vertical scroll list.

### Interacting with filter panes

If the Small screen layout for a sheet is set to List view, filter panes are not rendered on the sheet but are available from the Sheet filters section in the Selection panel.

If the Small screen layout for a sheet is set to Grid view, filter panes are rendered on the sheet.

Information noteThe small screen layout can be set in the sheet properties in Qlik Cloud, see [Changing sheet layouts](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Sheets/changing-sheet-layout.htm).

## Using the selections tool

The selections tool in the Qlik Analytics mobile app gives an overview of every dimension and [field](#glossary-10 "Glossary term") in an app. It also gives a more detailed view of selected data, so that you can explore associations in dimensions that have not been used.

During analysis, expand Applied selections to open selections view.

The selections tool is divided into three sections: Current selections, Master items, and Available selections. The Current selections section displays the fields that have active selections. The Master items sections displays all master items contained in the application. The Available selections section displays all dimensions without an active selection. All sections are sorted alphabetically.

Selections tool

![Qlik Sense Mobile SaaS selections tool](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/qsmsaas-global-filter.png "Click to view full size")

The selections tool has a search box that is useful when you have many dimensions and fields. You can search by field or dimension title. Your search string can consist of one or more words, or only a part of word. The search is not case sensitive, but only exact string matches are displayed.

You can make several selections consecutively. Tap ![ ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_tick.svg) to confirm your selection. These dimensions will move up to Current selections.

You can clear a selection in a field by tapping ![Cancel](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_remove.svg). The field is then moved down to Available selections.

## Bookmark selections

Use bookmarks when you analyze data, and find something interesting that you want to return to or share with others.

Bookmarks save your selections and a particular sheet location. Bookmarks can later be opened to restore the selections to a former state. Apply bookmarked selections to any sheet that has the same data as the sheet used to create the bookmark.

Bookmarks are usually created in applications in your [activity center](#glossary-11 "Glossary term"), see [Bookmarking selections](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Bookmarks/keep-track-of-important-data.htm).

You can also create basic bookmarks in the Qlik Analytics mobile app.

### Creating a bookmark in the Qlik Analytics mobile app

Do the following:

1. Make the selections on the sheet that you want to save as a bookmark.
2. Tap ![Bookmark](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bookmark.svg) in the toolbar.
3. Tap Create bookmark.
4. Title: Enter a bookmark title.

   Warning noteDo not use a name already used by an alternate state.
5. Description: Enter a description of the bookmark.
6. Click Create.

### Editing a bookmark in the Qlik Analytics mobile app

You can edit the title and the description of the bookmark in the Qlik Analytics mobile app.

Do the following:

1. Tap ![Bookmark](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bookmark.svg) in the toolbar.
2. Tap ![Bookmark](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_dropdown_arrow.svg) on the bookmark you want to edit.
3. Tap Edit.

### Deleting a bookmark in the Qlik Analytics mobile app

You can delete a bookmark in the Qlik Analytics mobile app.

Do the following:

1. Tap ![Bookmark](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bookmark.svg) in the toolbar.
2. Tap ![Bookmark](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_dropdown_arrow.svg) on the bookmark you want to delete.
3. Tap Delete.

## Limitations

- Horizontal layout is not supported in Multi KPI charts. The chart is displayed in vertical layout.
- Third party visualization extensions may behave differently in the Qlik Analytics mobile app compared to Qlik Cloud. Use native Qlik extensions instead.
- The Qlik Analytics mobile app has the following limitations with cyclic dimensions:

  - Buttons with the action Step cyclic dimension will only cycle dimension if the button is in a container.
  - In offline mode, buttons with the action Step cyclic dimension do not cycle the dimension.
  - In offline mode, any visualization with a cyclic dimension will only display the first dimension in the cycle. The cyclic dimension cannot be cycled.
- The Qlik Analytics mobile app has the following limitations with the [write table](#glossary-12 "Glossary term"):

  - In the Qlik Analytics mobile app, write tables are displayed in read-only mode.
  - Write tables are not available when you open an application offline in the Qlik Analytics mobile app.
- For filter panes that show field values as images, the Qlik Analytics mobile app displays the image URLs only, rather than the images themselves.
