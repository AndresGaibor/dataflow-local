---
title: "Reload and preview apps"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikCode/code-extension-reload-preview-apps.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Qlik for VS Code"]
---

# Reload and preview apps

You can reload analytics applications (and QVF script assets) directly from the Qlik for VS Code extension.

## Reload behavior

How Qlik for VS Code reloads an app or QVF script asset depends on whether you are working with a cloud-backed script or a local working copy.

### Reload a cloud-backed script

When you reload a cloud-backed script, Qlik for VS Code reloads the corresponding Qlik Cloud app or script directly. You can start the reload, monitor its progress, view the result, and abort a reload in progress. Reload logs and error messages are available if the reload fails.

### Reload a local working copy

When you reload a local bound file, Qlik for VS Code does not reload the origin app or QVF script asset directly. Instead, it uses a preview app.

What is a preview app?

In Qlik for VS Code, a preview app is a copy of the origin app used to validate local script changes without affecting the original.

- If no preview app exists yet, Qlik for VS Code creates one by copying the origin app or QVF script asset.
- It applies your local script to the preview app and reloads it.
- The preview app ID is stored in the binding metadata.
- You can open the preview app in your browser to review the results. It is located in your personal space and includes the original app name with a prefix [Working copy].
- The preview app remains in the Qlik Cloud tenant until the user deletes the local script, at which point a prompt appears asking "Do you want to delete the Working Copy  also?".

Local-file reload and data preview features always operate on the preview app, not on the origin app.

## Reloading applications

Do the following:

1. Use the Reload Application option, from any of the following:

   - The text editor toolbar.
   - Right-clicking the application (or QVF script asset) in the Qlik Cloud panel of the [Explorer](https://code.visualstudio.com/docs/editing/getting-started/userinterface#_explorer-view).
   - Right-clicking the bound local copy in the Explorer.
   - Using the [Command Palette](https://code.visualstudio.com/docs/editing/getting-started/userinterface#_command-palette).
2. Depending on the workflow you are using, the resource either reloads, or a preview app is created and reloaded (see [*Reload behavior*](#Behavior)).
3. After reloading, you can open the app in your browser to validate the results. See [*Open applications in the browser*](code-extension-open-in-browser.htm).

### Other options when reloading applications

The [Command Palette](https://code.visualstudio.com/docs/editing/getting-started/userinterface#_command-palette) offers more options to better control reloads and preview apps:

- Abort Reload stops a reload in progress.
- Create Preview App creates a temporary preview app so you can check the effect of script changes without touching the original.

## Learn more

- [*Work with load scripts in Qlik for VS Code*](code-extension-work-with-load-script.htm)
- [*Performing Qlik for VS Code commands*](code-extension-commands.htm)
- [Visual Studio Code documentation — Home](https://code.visualstudio.com/docs)
- [Visual Studio Code documentation — User interface](https://code.visualstudio.com/docs/editing/getting-started/userinterface)
