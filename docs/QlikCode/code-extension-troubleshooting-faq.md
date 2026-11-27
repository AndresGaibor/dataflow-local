---
title: "Troubleshooting and FAQ"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikCode/code-extension-troubleshooting-faq.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Qlik for VS Code"]
---

# Troubleshooting and FAQ

This page provides troubleshooting guidance and frequently asked questions that can be useful when working with the Qlik for VS Code extension.

- I don't see the Qlik Cloud panel in the sidebar.

  Make sure a folder or [workspace](https://code.visualstudio.com/docs/editing/workspaces/workspaces) is open in VS Code — the Qlik Cloud apps panel only appears once you have signed in and a workspace folder is open.

  See:

  - [*Authenticate with Qlik Cloud*](code-extension-authenticate.htm)
  - [*Browse spaces and apps*](code-extension-browse-content.htm)
- A file shows as read-only when I try to edit it.

  The script is either locked for remote editing by another user, or you don't have edit permission on it in Qlik Cloud. Use Unlock or Download from the editor toolbar to either unlock it or fall back to a local working copy, depending on which applies.

  See:

  - [*Update load scripts directly against Qlik Cloud*](code-extension-cloud-backed.htm)
  - [*Update load scripts with controlled editing*](code-extension-working-copy.htm)
- My local changes and the Qlik Cloud version both changed — what happens?

  Qlik for VS Code detects the conflict and asks you to Confirm merge or Cancel merge before continuing. See [*Update load scripts with controlled editing*](code-extension-working-copy.htm).
- Where is my data actually stored while I edit?

  The answer to this question depends on your authoring workflow:

  - A bound file (see [*Update load scripts with controlled editing*](code-extension-working-copy.htm)) lives on your local disk in the folder set by Default Working Copy Folder (see [*Settings reference*](code-extension-settings-reference.htm) for configuration details).
  - Direct remote editing (opening a script without downloading it first—see [*Update load scripts directly against Qlik Cloud*](code-extension-cloud-backed.htm)) reads and writes Qlik Cloud directly and does not create a local file.
