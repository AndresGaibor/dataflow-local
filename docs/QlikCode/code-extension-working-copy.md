---
title: "Update load scripts with controlled editing"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikCode/code-extension-working-copy.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Qlik for VS Code", "Work with load scripts in Qlik for VS Code"]
---

# Update load scripts with controlled editing

With Qlik for VS Code's controlled editing feature, you can download working copies of an application's load script to your machine for local editing. These local copies are connected to the source application via [bindings](#Binding). You can synchronize your local script with the remote Qlik Cloud version by pulling and pushing incoming and outgoing changes. Local QVS files can also be edited and bound to Qlik Cloud applications in Qlik for VS Code, allowing you to build local scripts without first creating an application.

Information noteThis workflow allows saving, updating, and synchronizing local copies of scripts against Qlik Cloud applications. For simple inspection and quick editing workflows, refer to [*Update load scripts directly against Qlik Cloud*](code-extension-cloud-backed.htm).

## What is a binding?

In Qlik for VS Code, a binding is a connection between a local working copy of a load script (or another local QVS file) and an analytics application in Qlik Cloud.

Bindings are created whenever:

- You download a working copy of a script for local editing (see [*Downloading a working copy of a script*](#WorkingCopy)).
- You manually bind a separate QVS file to an existing application (see [*Binding an existing local file*](#BindOther)).

After a binding is created, the extension stores the relationship between the local file and the Qlik Cloud application in a resource-map.json file at the [workspace](https://code.visualstudio.com/docs/editing/workspaces/workspaces) root.

## Downloading a working copy of a script

You can download a working copy of your application's load script to your local machine. When you do this, a copy of the load script is downloaded to your [workspace](https://code.visualstudio.com/docs/editing/workspaces/workspaces) in QVS format, and a [binding](#Binding) is automatically created between the locally created file and the source application.

The local working copy is saved into the folder set by the Default Working Copy Folder setting (see [*Settings reference*](code-extension-settings-reference.htm)), or the [workspace](https://code.visualstudio.com/docs/editing/workspaces/workspaces) root if that setting is empty.

Do the following:

1. In the VS Code [Explorer](https://code.visualstudio.com/docs/editing/getting-started/userinterface#_explorer-view), expand Qlik Cloud.
2. Find an application, and right-click it.
3. Click Download working copy.

   If one or more local copies of the script already exist in your workspace, a different option appears: Downloaded resources.... This option allows you to navigate to the existing local file.

After downloading and binding the local copy, you can edit it, update it with incoming changes from the remote Qlik Cloud version, and push your own local changes to the remote Qlik Cloud version. See [*Synchronizing changes between local and remote versions*](#Synchronizing).

## Binding an existing local file

You can also bind an existing local QVS file—a file not currently connected to an application—to a Qlik Cloud application without overwriting your local content. [Binding](#Binding) links the file to the app and its current script version.

Do the following:

1. In the VS Code [Explorer](https://code.visualstudio.com/docs/editing/getting-started/userinterface#_explorer-view), right-click the local file that you want to bind.
2. Click Bind to Qlik Cloud script.
3. Select the Qlik Cloud application to bind to.

After manually binding the file, you can edit it, update it with incoming changes from the remote Qlik Cloud version, and push your own local changes to the remote Qlik Cloud version. See [*Synchronizing changes between local and remote versions*](#Synchronizing).

## Unbinding scripts

Use the Qlik: Unbind from QCS Resource command (available via [Command Palette](https://code.visualstudio.com/docs/editing/getting-started/userinterface#_command-palette)) to remove the link between the local file and the remote version without deleting either copy.

## Synchronizing changes between local and remote versions

Information noteYou need to have permissions to edit the load script of the application. If you only have view access, you can open the script in read-only mode but cannot edit it.

After you download or manually bind a script, you can edit it using the VS Code text editor.

Qlik for VS Code provides options for:

- Updating local scripts with changes made to the remote Qlik Cloud version. For example, another user edits the load script, either in Qlik Cloud or using their own installation of Qlik for VS Code.
- Pushing your own changes to the remoteQlik Cloud version.

### Syncing individual scripts

You can sync scripts individually.

Do the following:

1. In the VS Code [Explorer](https://code.visualstudio.com/docs/editing/getting-started/userinterface#_explorer-view), find your local working copy of the script.
2. Right-click the file and select one of the following:

   - Pull from Qlik Cloud: Update your local copy with any changes that have been made to the script since you last downloaded or updated it.
   - Push changes to Qlik Cloud: Push your local changes to the remote Qlik Cloud version. You are prompted to confirm the replacement of the existing script.

### Batch syncing scripts

You can also synchronize your scripts in bulk. When you perform these actions, you push and pull changes for all applications and working copies you have access to.

Do the following:

1. In the VS Code [Explorer](https://code.visualstudio.com/docs/editing/getting-started/userinterface#_explorer-view), expand Qlik Cloud.
2. In the panel toolbar, select one of the following:

   - ![Update all from Qlik Cloud](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_VS_code_cloud_download.png) (Update all from Qlik Cloud): Update all local copies with any changes that have been made to the scripts since you last downloaded or updated them.
   - ![Push all change to Qlik Cloud](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_VS_code_cloud_upload.png) (Push all changes to Qlik Cloud): Push all your local changes to the remote Qlik Cloud versions.

### Managing conflicts

If a script changed in Qlik Cloud since your last sync and you also have local changes, Qlik for VS Code detects the conflict and offers options for resolving it when possible. These options are displayed within the VS Code text editor.

- Confirm merge: Proceed with the proposed merge of the changes.
- Cancel merge: Reject the proposed merge and revert to the local copy.

Tip noteVS Code offers native options for detecting and resolving conflicts. For more information, refer to the official VS Code documentation at [Resolve merge conflicts in VS Code](https://code.visualstudio.com/docs/sourcecontrol/merge-conflicts).

## Learn more

- [*Editing load scripts in Qlik for VS Code*](code-extension-edit-load-script.htm)
- [*Performing Qlik for VS Code commands*](code-extension-commands.htm)
