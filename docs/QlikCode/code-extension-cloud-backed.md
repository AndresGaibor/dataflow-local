---
title: "Update load scripts directly against Qlik Cloud"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikCode/code-extension-cloud-backed.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Qlik for VS Code", "Work with load scripts in Qlik for VS Code"]
---

# Update load scripts directly against Qlik Cloud

After signing in, the extension loads spaces, apps, and QVF script assets into the **Qlik Cloud** tree in the Visual Studio Code Explorer. Opening one of these entries opens a cloud-backed document. The extension fetches the current script content from Qlik Cloud when the file is read.

Information noteThis workflow is suitable for inspection and direct, limited interaction with the cloud resource. For local editing options, refer to the controlled editing instructions at [*Update load scripts with controlled editing*](code-extension-working-copy.htm).

## Locking and unlocking the script for editing

Information noteYou need to have permissions to edit the load script of the application or QVF script asset. If you only have view access, you can open the script in read-only mode but cannot edit it.

Do the following:

1. In the VS Code [Explorer](https://code.visualstudio.com/docs/editing/getting-started/userinterface#_explorer-view), expand Qlik Cloud.
2. Find an application (or QVF script asset), and right-click it.
3. Select one of the following:

   - Unlock remote editing: Unlocking remote editing allows you to directly edit the load script.
   - Lock remote editing: Locking remote editing is done on an unlocked script when you are done with making edits and want to re-lock the script to make it read-only again.

Alternatively, click the resource to open its script in read-only mode, and then select Unlock remote editing in the popup that appears.

Selecting remote editing option in opened load script

![Selecting remote editing option in opened load script](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/qlik-code-cloud-backed-edit-popup-option.png "Click to view full size")

## Saving the load script after remote editing

After you have made your desired edits, save the load script to update it in Qlik Cloud.

Do the following:

- Use the VS Code Save option, either through the menu bar, a keyboard shortcut, or the Command Palette.

After the script is updated, you are notified in a popup that appears.

Popup confirming the load script has been updated remotely in the Qlik Cloud application.

![Popup confirming the load script has been updated remotely in the analytics application](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/qlik-code-cloud-backed-edit-confirmed.png "Click to view full size")
