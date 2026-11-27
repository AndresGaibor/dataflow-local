---
title: "Visualize the data model"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikCode/code-extension-visualize-data-model.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Qlik for VS Code"]
---

# Visualize the data model

You can visualize the data model of an application directly within the Qlik for VS Code extension.

Information noteNot applicable to QVF script assets.

Do the following:

1. Use the Data Model Diagram / View Data Model option, from any of the following:

   - Right-clicking the app from the Qlik Cloud panel in the VS Code [Explorer](https://code.visualstudio.com/docs/editing/getting-started/userinterface#_explorer-view).
   - Right-clicking a bound local script in the VS Code Explorer.
   - Right-clicking in the text editor when editing a script.
   - Using the [Command Palette](https://code.visualstudio.com/docs/editing/getting-started/userinterface#_command-palette).

   This opens a visual diagram of the app's tables and the associations between them, in its own editor tab.
2. With the data model diagram opened, you have access to a number of options for customizing its appearance:

   - Switch between Auto Layout and Grid Layout, or Restore Saved Layout to return to a manually arranged layout.
   - Reset Zoom and Fit to Screen adjust the view.
   - Minimize All Tables / Maximize All Tables collapse or expand every table card.
   - Show Only Connections filters the diagram down to tables and fields that are actually linked.
   - Search Tables & Fields finds a specific table or field in a large model.

Viewing the data model of an application within Qlik for VS Code

![Data model diagram in Qlik for VS Code](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/qlik-code-view-data-model.png "Click to view full size")

## Learn more

- [*Preview data*](code-extension-preview-data.htm)
- [*Reload and preview apps*](code-extension-reload-preview-apps.htm)
- [Visual Studio Code documentation](https://code.visualstudio.com/docs)
