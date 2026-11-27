---
title: "Adding data manually"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/adding-data-manually.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and managing data with Data Manager", "Adding data to the application from connections and new files"]
---

# Adding data manually

Manual entry in Add data enables you to enter data into an editor in Qlik Sense, and then add it as a table in Data manager.

Manually entering data is useful if you want to use a limited set of data from another source. For example, if you only wanted a selection of rows from an Excel spreadsheet or from a table on a webpage to be loaded as a table into Data manager, you could copy and paste the selected data into Manual entry and then add it as a table in Data manager. It is also useful if you have a small amount of data that might be faster to add manually than importing from another data source.

To add data manually, you open Add data, select Manual entry, enter your data into the table, and then add the table to Data manager. The table editor starts with one row and two columns, but as you add data to the table, additional empty rows and columns are automatically added to the table.

Warning note

Manual entry does not automatically save as data is entered. Data entered may be lost if the screen is refreshed, if the session times out, or if the [connection](#glossary-0 "Glossary term") is lost before the data is added to Data manager.

In addition to typing data, you can copy and paste it from other sources. Manual entry preserves the columns and rows of data copied from Excel tables.

There are a number of keyboard shortcuts you can use to work effectively and easily in Manual entry. Shortcuts behavior varies depending if you are selecting cells, rows, or columns, or if you are editing cells in the table. The following table contains the selecting shortcuts:

Keyboard shortcuts for selecting

| Shortcut | Description |
| --- | --- |
| Arrow keys | Navigates between cell selection |
| Tab | Moves the cell selection right. If no cell exists to the right, it moves to the first cell in the next row. |
| Shift+Tab | Moves the cell selection left. If no cell exists to the left, it moves to the first cell in the previous row. |
| Enter | Toggles to editing mode |
| Delete | Deletes the current selection |

The following table contains the editing shortcuts:

Keyboard shortcuts for editing

| Shortcut | Description |
| --- | --- |
| Arrow keys | Moves the cursors in the cell. |
| Tab | Commits the edit and moves to the next cell to the right |
| Shift+Tab | Commits the edit and moves to the previous cell to the left |
| Enter | Commits the edit and moves to the next cell below |
| Shift+Enter | Commits the edit and moves to the previous cell above |
| Esc | Cancels the edit and toggles to selecting mode |

Tables created using Manual entry can be edited later to add or remove content. For more information, see [*Updating a table from the data source*](editing-table.htm#Updating).

## Adding data manually

Do the following:

1. Open an application.
2. Open Data manager and then click ![Add](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) Add data > Files and other sources.

   You can also click Files and other sources in the ![Navigation ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) menu.
3. Under In-App, click Manual entry.
4. Type a name for the table.
5. In the table editor, enter your data.

   Double-click a cell to start entering data in the cell.

   While editing a cell, clicking any other cell in the table commits your edit and selects the other cell.
6. When your data is complete, click Add data.

The table is added to Data manager.

Information note

If your data includes city or country geographic information, the following QVD files might automatically be added to the current space:

- countryAliases.qvd
- countryGeo.qvd
- cityAliases.qvd
- cityGeo.qvd

These files are used to provide additional geographic data for the locations included in your added data. Qlik Sense manages and updates these files as necessary. If they are deleted, they are automatically added back after the next reload.
