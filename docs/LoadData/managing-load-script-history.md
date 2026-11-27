---
title: "Managing load script history"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/managing-load-script-history.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Scripting to load or export data"]
---

# Managing load script history

View and manage your application [load script](#glossary-1 "Glossary term") history in History.

In the script editors Data load editor and Script, you can view your load script history in History. The current version in History updates as you make changes to your load script. You can save versions from the current version to keep specific points in your load script history. You can view and restore these versions.

When multiple users are co-developing the load script, a new version is created whenever a new user begins editing the load script. For more information on co-development, see [*Collaboratively developing data load scripts in shared spaces*](script-codevelopment.htm).

History in Data load editor

![Data load editor with History open, displaying 4 different versions.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_DLE_History_panel-rev.png "Click to view full size")

In History, you can:

- Create new versions
- Rename versions.
- Restore versions
- Download the load script from this point in history.
- Delete versions.

Information note

For applications existing before December 13, 2022, their history begins when this feature was released.

For scripts, space permissions may give you view-only access to the script history. You can view and download the load script versions, but cannot restore versions. For more information on History permissions with scripts, see:

- [*Managing permissions in shared spaces*](../Spaces/managing-shared-spaces.htm)
- [*Managing permissions in managed spaces*](../Spaces/managing-managed-spaces.htm)

## Creating a new version

You can create a new version from the current state of the load script. This allows you to save versions for key points in history.

Do the following:

1. Click History.
2. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the current version and select Name this version.
3. Enter the new name for the version.
4. Click OK.

## Renaming version

You can rename the versions to be more meaningful to the changes made or the state of the load script.

Do the following:

1. Click History.
2. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on a version and select Rename version.
3. Enter the new name for the version.
4. Click OK.

## Restoring versions

You can restore the load script to a previous version. When you restore, a new version is added to the history that contains the load script from your selected restore version. This ensures you do not lose any history when you restore a version.

Do the following:

1. Click History.
2. Select a version and select Restore this version.

   Alternatively, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the version to restore and select Restore

## Downloading versions

You can download version of the load script as a QVS file. QVS files can be edited locally in text editors and uploaded to Qlik Cloud. For more information about QVS files, see [*Creating reusable load script with QVS files*](QVS/create-common-scripting-qvs.htm).

Do the following:

1. Click History.
2. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on a version and select Download.

## Deleting versions

You can delete versions from your history.

Do the following:

1. Click History.
2. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the version and select Delete.

## Load script history and Data manager auto-generated scripts

History only saves scripting created in Data load editor. It does not include auto-generated scripting sections created by Data manager. For example, if you restore a load script that contains auto-generated scripts in a locked section, the script outside of the auto-generated sections is restored to the old version while the script inside the auto-generated sections remains the same.
