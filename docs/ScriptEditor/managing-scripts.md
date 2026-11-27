---
title: "Managing scripts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ScriptEditor/managing-scripts.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Working with scripts in the catalog"]
---

# Managing scripts

Once you have created a script, you may want to fine-tune it to make it easier and more efficient to use for yourself and others.

What you can do with a script depends on the type of space where the script is located. In your personal space, you can manage your own scripts. In a shared space, depending on your permissions in that space, you can manage both your own scripts and the scripts of other users. In managed spaces, there are fewer options for managing scripts as access is more governed. For more information about spaces, see [*Working in spaces*](../Spaces/Spaces.htm).

Depending on the space, you can:

- Add scripts to collections.

  [*Collections*](../QlikCloudNavigation/Analytics-activity-center.htm#Collecti)
- Share scripts.

  [*Sharing scripts*](#Sharing)
- Move scripts.

  [*Moving scripts*](#Moving)
- Edit and rename scripts.

  [*Editing script details*](#Renaming)
- Publish scripts

  [*Publishing scripts*](publishing-scripts.htm)
- Duplicate scripts

  [*Duplicating scripts*](#Duplicat)
- Reload scripts

  [*Running scripts*](reloading-scripts.htm)
- View script lineage information

  [*Viewing lineage*](#Viewing)
- View script impact analysis information

  [*Viewing impact analysis*](#Viewing2)
- Export scripts

  [*Exporting scripts*](#Exportin)
- Duplicate and convert scripts to analytic applications

  [*Converting scripts to applications*](#Converti)
- Delete scripts

  [*Deleting scripts*](#Deleting)

## Sharing scripts

You can share a script by inviting a user, group, or everyone in your tenant to the space where it is stored.

Do the following:

1. In the catalog, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the item to be shared and select Share > Invite.
2. Search for users or groups by name or email address.
3. Select space permissions for the users or groups.
4. Or, select permissions for Anyone at <your tenant name> from the dropdown list.
5. Click Done.

The users receive access to the shared item and all other content in the space.

## Moving scripts

You can move scripts between shared spaces as well as between a shared space and a personal space.

If you create a script in a shared space, the data connections related to it will stay in that space, even if the script moves. You will either need to add connections in the new space or use space-aware connections to reference the data connections in the original space.

For example, you create a script called SalesPrep in the Data Team shared space. If you move SalesPrep to a different shared space, the data connections will remain in the Data Team shared space.

If the data needs to be edited or reloaded, it must be done by a user with Can edit or Can edit data in applications roles in the Data Team shared space. The same would apply if you created a script in a personal space and moved it to a shared space.

If you move a script with a reload schedule between spaces, the reload schedule is deleted. Recreate the schedule in the new space if required.

Do the following:

1. Click ![Move](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the script and select Manage > Move to space.
2. Select the new space from Space.
3. To open the new space, select Navigate to space.
4. Click Move.

If you are a Qlik Cloud tenant admin or analytics admin, you can move scripts between spaces in the Administration activity center.
Scripts can be moved between shared spaces, between a shared space and a personal space, or between managed spaces. For information about these administrator privileges, see [*Changing space of scripts*](../Admin/mc-administer-scripts.htm#Changing).

## Editing script details

You can change the titles and descriptions of your scripts. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the script that you want to edit and then select Edit details. You can also change the tags used with the script. Tags are used to group scripts with related content. When adding new tags to a script, users can view all tags that exist in the tenant.

## Duplicating scripts

You can duplicate any script you have access to by clicking ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the script and then selecting Manage > Duplicate. The duplicate can be modified.

Duplicating scripts has several uses. For example, you can copy a script to use it as a template. You can also duplicate script as a form of version control, and store older ones a space created for archival purposes.

Duplicated scripts keep the original data sources. If you did not create the original data sources used in the script or if they are not available in the space, you will have to recreate data sources in the script.

## Viewing lineage

Lineage tracks data and data transformation backwards from the script to its original sources. This provides an interactive representation of the history of this flow to your script. For more information on lineage, see [*Analyzing lineage in Analytics*](../Catalog/lineage.htm).

Do the following:

- Click ![Move](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the script and select Tools > Lineage.

## Viewing impact analysis

Impact analysis shows the downstream dependencies of script outputs. It answers questions about what other applications, scripts, or other resources would be directly or indirectly impacted by changes to the script. For more information on impact analysis, see [*Analyzing impact analysis in Analytics*](../Catalog/impact-analysis2.htm).

Do the following:

- Click ![Move](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the script and select Tools > Impact analysis.

## Exporting scripts

You can export scripts from the Analytics activity center as QVF files.
These can be uploaded into other Qlik Cloud Analytics tenants or Qlik Sense versions.

The exported script is saved in the default download folder of your web browser.

Information note

Exported scripts can be imported into Qlik Sense Desktop or Qlik Sense Enterprise on Windows, however they are converted into applications.

Do the following:

- Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the script you want to export and select Download > Download.

## Converting scripts to applications

You can convert scripts into applications. Converting duplicates the script and then converts it into an application. Converted applications use the script's load script as the application's load script.

Do the following:

1. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the script you want to export and select Manage > Duplicate as application.
2. Click Confirm.

## Deleting scripts

Do the following:

1. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the script you want to delete and select Delete.
2. Click Delete.
