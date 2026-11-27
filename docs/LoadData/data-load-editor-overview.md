---
title: "Data load editor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/data-load-editor-overview.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Understanding applications", "Navigating in the application interface"]
---

# Data load editor

Create and run data load scripts from the data load editor, and create connections to data sources. When you have loaded the data it is available to the application for analysis.

Click Data load editor in the application navigation menu to open the data load editor.

Data load editor

![Data load editor, with data sources open ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Scripting/ui_gen-dle_cloud.png "Click to view full size")

Scripts can also be generated when you load data using the data manager. However, if you need to use complex script statements, you need to create the script manually in the data load editor.

See: [*Loading and transforming data with scripting*](../Scripting/introduction-data-modeling.htm)

## Adding data from existing datasets

Click Add from data catalog to open the [data catalog](#glossary-0 "Glossary term"). You can add data from multiple datasets.

See: [*Loading data from the data catalog*](adding-data-catalog.htm)

## Inserting other scripts into load scripts

Click Insert script to select an existing QVS file or another script to insert in your load script.

See: [*Inserting other scripts into load scripts*](QVS/inserting-qvs-script-editor.htm)

## Creating connections

Expand the Data sources panel to view Data connections. Click Create new connection add a connection to your script.

See: [*Loading analytics data*](connect-data-sources.htm)

## Creating and editing scripts

Write your script code in the script editor. Each script line is numbered and the script is color coded by syntax components.

Script editor tools

| UI item | Description |
| --- | --- |
| Search | Search and replace text in the script. |
| Comment / Uncomment | Comment/uncomment. |
| Indent | Indent code. |
| Undent | Outdent code. |
| Help | Activate syntax help mode. In help mode you can click on a syntax keyword (marked in blue) in the editor to access detailed syntax help. |
| Autocomplete hints on | Autocomplete script hints turned on. Click to turn off. |
| Autocomplete hints off | Autocomplete script hints turned off. Click to turn on. |
| Undo | Undo the latest change (multiple step undo is possible). |
| Redo | Redo the latest undo. |

Click ![Create new](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) to add a script section. The sections are executed from top to bottom.

Click ![Debug](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_debug_outline.svg) to debug the script.

Click History to manage script versions.

See:

- [*Editing load scripts*](edit-data-load-script.htm)
- [*Organizing load scripts*](organize-script-code.htm)
- [*Debugging the data load script*](debug-data-load-script.htm)
- [*Managing load script history*](managing-load-script-history.htm)

## Running scripts

Click the Load data button to run the script. A dialog opens to display the progress of the data load and any messages that are generated. Additionally, you can click the Output button to view the output.

[*Running load scripts to load data in applications*](run-script-load-data.htm)

You can also preview the load script. Previewing runs the load script while limiting the number of rows of source data loaded into the application and skipping any Store statements. You can set how many rows to include. To preview your data, click Preview data.

[*Previewing data in load scripts*](../ScriptEditor/previewing-scripts.htm)

Previewed or loaded data can be viewed by clicking the Preview button.

Related learning:

- [Introduction to the data load editor](/lnk/Intro_Data_Load_Editor_QS)
- [Getting started with Qlik Sense](/lnk/Getting_started_QS)
