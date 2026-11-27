---
title: "Navigating scripts in catalog"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ScriptEditor/navigating-scripts.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Working with scripts in the catalog"]
---

# Navigating scripts in catalog

When you open a script, it opens in Script. Script provides both information on the script and its dependencies as well as an editor for authoring the script. Script contains two sections:

- Overview: Provides a summary of information about the script, including information on dependencies, run history, and published copies.
- Editor: Provides the text editor for creating and editing the script, previewing the script, and running the script in full.

## Overview

Overview provides general information about a script, its data sources, and its exported files. Overview has the following sections:

- Summary
- Notifications
- Reload history
- Published copies

Script overview

![Script editor overiew, open to the Summary tab. There are two outputs displayed in the Outputs section and two inputs listed in the Inputs section.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_script-editor-overview-rev.png "Click to view full size")

### Summary

Summary provides an overview of details about the script. You can see the following information:

- Owner: Owner of the script
- Creator: Creator of the script
- Contributors: Number of contributors to the script. Click ![Users](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_info_outline.svg) to view the names of contributors.
- History: Number of entries in the history. Click ![Last 5 entries](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_info_outline.svg) to view the names of contributors for the last five entries. Click View to open History.
- Space: Space the script where the script is located
- Created date: Date the script was created
- Modified date Date the script was last modified
- Last modified by: User who last modified the script
- Last reload date: Date of the last reload
- Last reload duration: Duration of the last reload
- Last reload date: Date of the last reload

Information note

Previewing the data (without Use Store statement turned on) does not count as a reload for reload information.

Summary also has two additional sections, Output and Input. Output shows the files exported by the script. View the full impact analysis for your script by clicking Open Impact Analysis. For more information on impact analysis, see [*Analyzing impact analysis in Analytics*](../Catalog/impact-analysis2.htm).

Input lists all tables and their source used by the script. View the full lineage of your script by clicking Open Lineage. For more information on lineage, see [*Analyzing lineage in Analytics*](../Catalog/lineage.htm).

For items listed in Output and Input, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) to view additional options. You can view the impact analysis or lineage for each item. You can also open items in a new tab.

### Notifications

Notifications lists the notifications you can receive for the script. You can turn them on or off, and select how you receive the notifications.

### Reload history

Reload history lists the history of manual and scheduled runs for your script. Click View to open a log for the run. You can download a detailed copy of the log as a LOG file.

Information note

Previews and exports in Editor are not included in Reload history.

Script reload history.

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_script-editor-reload-history-rev.png "Click to view full size")

### Published copies

Published copies displays all copies of the script created during publishing to managed spaces. It displays each copy and the following information:

- Name
- Owner
- Last modified
- Space
- Viewed by

Script published copies

![Script editor opened to published copies. A single copy published to a managed space is displayed.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_script-editor-published-copies-rev.png "Click to view full size")

Click on the copy to open it in Script. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) to view additional options. You can:

- Add it to a collection.
- Rename it.
- View lineage information.
- View impact analysis.
- View the copy reload schedule.
- Open it in a new tab.
- Delete the copy.

## Editor

In Editor, you can create and run your data load script for your script. You can add new data sources or use existing data sources.

Editor open in Script

![Editor open in Script editor. The text editor contains a load script loading two tables. It stores them in two separate QVD files. Data sources is open showing available data and Preview is open at the bottom, showing a preview of loaded data.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Scripting/ui_script-editor-editor.png "Click to view full size")

The Editor toolbar provides easy access to scripting tools.

Editor toolbar

| Option | Description |
| --- | --- |
| Show/Hide Selections panel Sections | Show or hide Sections in Editor. Sections allow you to organize your load script. |
| Search | Search and replace text in the script. |
| Comment / Uncomment | Comment/uncomment. |
| Indent | Indent code. |
| Undent | Outdent code. |
| Help | Activate syntax help mode. In help mode you can click on a syntax keyword (marked in blue) in the editor to access detailed syntax help. |
| Autocomplete hints on | Autocomplete script hints turned on. Click to turn off. |
| Autocomplete hints off | Autocomplete script hints turned off. Click to turn on. |
| Next-gen editor | Turn on an enhanced script editor with new features such as code folding, dark mode, Command Palette, and a refreshed look and feel.  [*Working with the next-gen script editor*](next-gen-editor.htm) |
| Undo | Undo the latest change (multiple step undo is possible). |
| Redo | Redo the latest undo. |
| Show/Hide script history History | Open History to view the history of changes to the script. |
| Show/Hide data sources Data sources | Open Data sources to view the available data sources to add to the load script |
| Turn on debug mode Debug | Open Debug to troubleshoot your load script. |
| Run script without exporting data using store statements Preview data | Run a limited load of the load script, with a limited number of rows returned per table and ignoring Store statements. Click Settings to view additional preview settings. |
| load data Export data | Run the load script. |

### Customizing the interface

#### Resizing and collapsing panes

You can resize and collapse panes in the Editor for flexible navigation. Your adjustments are used in all other scripts and analytics applications.

#### Dark mode

With Dark mode, the script editor switches to a different color scheme with a dark background. Text and other elements appear in light colors, maintaining high contrast and readability.

Information note

You need to turn on the following in Next-gen editor:

- Enable new code editor experience
- Dark mode

See [*Working with the next-gen script editor*](next-gen-editor.htm).

Information note

Dark mode does not cover the entire user interface when activated. For example, the Qlik Cloud navigation bar and left panels, as well as some dialogs for data load and connections, do not appear in dark mode.

Dark mode

![Script editor in dark mode](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen-dle_dark-mode.png "Click to view full size")

### Sections

Sections allow you to group sections of your script. Sections are run in order when the script is run. Click ![Create new section](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) to add a new section. You can reorder sections by clicking and dragging ![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/LUIicons_draggable.svg) on a section.

For more information, see [*Organizing load scripts*](../LoadData/organize-script-code.htm)

### Included scripts

QVS and scripts inserted into your load script are visible in Included scripts. This section is only visible after running Export data or Preview after the scripts have been inserted.

Click on the scripts to preview or open them. You can also click </> where a script has been inserted in the load script.

Previewing an inserted script

![Previw of an inserted QVS script under Included scripts. The preview is Read Only.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Scripting/ui_script-preview-qvs.png "Click to view full size")

Information note

Included scripts displays the first 50 scripts included in the load scripts. If there are more included scripts, they will be executed when the load script runs, but will not be listed in Included scripts.

For more information, see:

- [*Inserting other scripts into load scripts*](../LoadData/QVS/inserting-qvs-script-editor.htm)
- [*Creating reusable load script with QVS files*](../LoadData/QVS/create-common-scripting-qvs.htm)

### Text editor

You can write and edit the script code in the text editor. Each script line is numbered and the script is color coded by syntax components. The initial script contains some pre-defined regional variable settings, for example SET ThousandSep=, that you can optionally edit. For more information, see [*Modifying regional settings for applications and scripts*](../Apps/regional-settings-in-apps.htm).

To learn more about scripting, see:

- [*Editing load scripts*](../LoadData/edit-data-load-script.htm)
- [*Understanding script syntax and data structures*](../LoadData/understand-data-structures.htm)
- [*Script syntax overview*](../Scripting/script-syntax.htm)

### History

In History, you can view and manage previous versions of your load script.

[*Managing load script history*](../LoadData/managing-load-script-history.htm)

### Debug

You can use the debugging utilities to step through the execution of your script by using breakpoints, which enable you to inspect variable values and output from the script execution.

[*Debugging the data load script*](../LoadData/debug-data-load-script.htm)

### Data sources

Add data to your load script from Data sources.

#### Add data

Under Add data, you can access the data catalog. The data catalog allows you to load data from all the existing datasets to which you have access. You can load data from multiple datasets at the same time using data catalog.

[[*Loading data from the data catalog*](../LoadData/adding-data-catalog.htm)](../LoadData/adding-data-catalog.htm)

In addition to datasets, you can select QVS files and other scripts to insert into the load script. The data catalog allows you to select any uploaded QVS file or other script to which you have access.

[*Inserting other scripts into load scripts*](../LoadData/QVS/inserting-qvs-script-editor.htm)

#### Data connections

Under Data connections you can save shortcuts to the data sources (databases or remote files) you commonly use. This is also where you initiate selection of which data to load. Data connections are sorted by the spaces to which you have access.

For more information, see [*Loading analytics data*](../LoadData/connect-data-sources.htm) and
[*Selecting data in load scripts*](../LoadData/select-data-to-load.htm).

### Preview

Once the script has been run either with Preview data or Export data, you can view a preview of the loaded tables under Preview. Click Preview data to regenerate a preview of the data using a limited load.

Preview offers three different views of table data:

- Table view
- List view
- Tile view

#### Table view

The data view displays data in a table format.

#### List view

The list view shows a summary of information about the fields and their values.

You can control what columns display by clicking ![Column picker](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_columns.svg) and selecting the desired columns. Selections do not carry over between sessions. The following columns are available:

- Name: Field name.
- Data type: Type of data in the field
- Distinct values: Count of distinct values in the field
- Null values: Count of null values in the field
- Sample values: Selection of sample values from the field
- Sum: If the field is numeric, a sum of the field values
- Min: If the field is numeric, the lowest value
- Max: If the field is numeric, the greatest value
- Average: If the field is numeric, the average value
- Median: If the field is numeric, the median value
- System Tags: Tags added to the data by the Data Profiling Service
- Standard deviation: If the field is numeric, the standard deviation of the values
- Positives: If the field is numeric, the number of positive values
- Negatives: If the field is numeric, the number of negative values
- Zero values: If the field is numeric, the number of zero values
- Empty strings: If the field is textual, the number of empty strings
- Min length: If the field is textual, the number of characters in the shortest string
- Average length: If the field is textual, the average number of characters per string
- Max length: If the field is textual, the number of characters in the longest string
- First sorted value: First value, alphabetically or numerically, in a field
- Last sorted value: Final value, alphabetically or numerically, in a field
- Numeric values: Number of numeric values in a field
- Text values: Number of text values in a field
- Most frequent values: Three most repeated values from the field
- Frequency distribution: If the field is numeric, the frequency distributions of the values

#### Tile view

The tile view displays available fields with a graphical profile of the data. Depending on the values in the field, each tile displays one of the following visualizations:

- A list of the top three distinct values from the field with a count of each value's instances.
- An area chart showing the range of values, with the average value highlighted.

### Output

Output displays the autosave status and all messages that are generated during script execution.

### Running scripts

Click Export data to run the script. A dialog opens to display the progress of the data load and any messages that are generated. Additionally, you can click the Output button to view the output.

See: [*Running load scripts to export data in scripts*](run-script-export-data.htm)
