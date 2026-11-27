---
title: "Insert data and catalog content into a script"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikCode/code-extension-insert-content-script.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Qlik for VS Code", "Work with load scripts in Qlik for VS Code"]
---

# Insert data and catalog content into a script

The Qlik for VS Code extension offers a number of options to help you reference data sources in the load scripts you write.

## Adding data from data connections and data files

You can add script content to load data from [data connections](#glossary-0 "Glossary term") and data files you can access in the Qlik Cloud tenant.

Do the following:

1. Open a script, either as an unlocked remote script or a bound local copy.
2. In the editor, move your focus point to an empty script line.
3. Click the ![Select data](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_VS_code_data_sources.png) Select data button that appears.

   Viewing the data model of an application within Qlik for VS Code

   ![Clicking the 'Show data' button on an empty script line](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/qlik-code-select-data-editor.png "Click to view full size")
4. Choose from the provided options, which include:

   - Select a space and its DataFiles connection to insert data from files added to the space. You can also add data files directly to the space from this view.

     Using the graphical interface to add data from data files in a Qlik Cloud space.

     ![Using the graphical interface to add data from data files in a space.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/qlik-code-select-data-datafiles-space.png "Click to view full size")
   - Select an existing data connection in the Qlik Cloud tenant to insert data from that connection.

     Information noteYou cannot create a data connection from Qlik for VS Code. The data connection must already exist in Qlik Cloud before you can use it in script content.

     Selecting a data connection from the list.

     ![Selecting a data connection from the list.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/qlik-code-select-data-connections.png "Click to view full size")
5. When done, confirm the selection to insert the script.

## Adding data from the data catalog

The Add from data catalog option can also be used to choose from data files you can access in the Qlik Cloud tenant.

Do the following:

1. Open a script, either as an unlocked remote script or a bound local copy.
2. Navigate to the place in the script where you want to insert the data.
3. Use the Add from data catalog option, from any of the following:

   - Right-clicking the app from the Qlik Cloud panel in the VS Code [Explorer](https://code.visualstudio.com/docs/editing/getting-started/userinterface#_explorer-view).
   - Right-clicking a bound local script in the VS Code Explorer.
   - Right-clicking in the text editor when editing a script.
   - Using the [Command Palette](https://code.visualstudio.com/docs/editing/getting-started/userinterface#_command-palette).
4. Choose the dataset and the fields you want to load, and confirm.

## Inserting other Qlik Cloud scripts

You can reuse other existing scripts (QVF and QVS) in the Qlik Cloud tenant without leaving your current file.

When you insert another script into a load script, a Must\_Include statement is added to the script at your current location in the editor. For more information about these statements, see [*Include*](../Scripting/SystemVariables/Include.htm).

Do the following:

1. Open a script, either as an unlocked remote script or a bound local copy.
2. Navigate to the place in the script where you want to insert the included script.
3. Use the Include scripts option, from any of the following:

   - Right-clicking the app from the Qlik Cloud panel in the VS Code [Explorer](https://code.visualstudio.com/docs/editing/getting-started/userinterface#_explorer-view).
   - Right-clicking a bound local script in the VS Code Explorer.
   - Right-clicking in the text editor when editing a script.
   - Using the [Command Palette](https://code.visualstudio.com/docs/editing/getting-started/userinterface#_command-palette).

## Learn more

- [*Work with load scripts in Qlik for VS Code*](code-extension-work-with-load-script.htm)
- [*Performing Qlik for VS Code commands*](code-extension-commands.htm)
- [Visual Studio Code documentation — Home](https://code.visualstudio.com/docs)
- [Visual Studio Code documentation — User interface](https://code.visualstudio.com/docs/editing/getting-started/userinterface)
