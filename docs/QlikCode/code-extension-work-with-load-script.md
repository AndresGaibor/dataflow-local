---
title: "Work with load scripts in Qlik for VS Code"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikCode/code-extension-work-with-load-script.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Qlik for VS Code"]
---

# Work with load scripts in Qlik for VS Code

After installing Qlik for VS Code and finding an application you want to work with, you can start working on the load script. Qlik for VS Code offers several editing workflows and built-in support for Qlik script editing.

## Choose a development workflow

The first step is to choose your development workflow. Choose the way in which you will be accessing, downloading, and syncing the script against the Qlik Cloud resources you work with.

### Workflow 1: Access a cloud-backed script

In this workflow, you edit the script directly without any manual download, binding, or synchronization features. When you have made your changes, you can save the script to push changes to Qlik Cloud.This workflow is better for inspection of the load script, as well as smaller script edits that do not require heavy collaboration or version control.

For more information, see [*Update load scripts directly against Qlik Cloud*](code-extension-cloud-backed.htm).

### Workflow 2: Download, bind, and synchronize working copies

This workflow is the preferred workflow for controlled editing. With controlled editing, you download and bind local working copies of Qlik Cloud load scripts, and then synchronize the changes with the Qlik Cloud version by pushing and pulling changes to and from the source application or QVF script asset.

For more information, see [*Update load scripts with controlled editing*](code-extension-working-copy.htm).

## Get started with script editing in VS Code

After choosing your development work, you can start editing the script in the VS Code text editor. To understand how to navigate the script editing interface in Qlik for VS Code, see [*Editing load scripts in Qlik for VS Code*](code-extension-edit-load-script.htm).

## Insert data into your script

As you work on your load script, you are assisted with graphical options for inserting data from the Qlik Cloud tenant into the script.

You can:

- Select data from connections.
- Choose data from the Qlik Cloud data catalog.
- Reference existing script files in Qlik Cloud files—specifically, QVS scripts and QVF script assets.

For more information, see [*Insert data and catalog content into a script*](code-extension-insert-content-script.htm).

## Next steps

You can perform other actions, such as data and script validation, in Qlik for VS Code. You can:

- Reload the application or script.

  [*Reload and preview apps*](code-extension-reload-preview-apps.htm)
- Inspect the data model.

  [*Visualize the data model*](code-extension-visualize-data-model.htm)
- Inspect the data preview.

  [*Preview data*](code-extension-preview-data.htm)
