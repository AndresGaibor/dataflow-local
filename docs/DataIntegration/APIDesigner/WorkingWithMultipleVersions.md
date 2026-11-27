---
title: "Working with multiple versions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/WorkingWithMultipleVersions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts"]
---

# Working with multiple versions

API Contracts lets you maintain multiple versions of the same API contract so you can keep a published version stable while you prepare changes in a new version.

- Maintain an existing API version in production while introducing breaking changes in a new version.
- Track and manage published versions from a single location.
- Work on API changes without affecting existing versions.

When you create a new version, all content is copied to the new version. The latest version can then be updated independently without affecting earlier versions.

Only the latest version is editable, and you can create a new version only from it. Older versions are read-only.

The API Contracts homepage displays all APIs owned by you and all API versions shared with you.![API Contracts homepage.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/api-designer-homepage.png)

## Creating a new API version

Create a new version of an existing API definition.

Information note

Note:

You can create a new version only from the latest version. Older versions are read-only and cannot be edited or used to create a new version.

You are an owner of the API or an editor of at least one version of the
API.

1. On the homepage, go to the API for which you want to create a new version.

   You can filter the list by name or owner if needed.
2. Open the latest version to view the Preview, then click Create a new version.

   ![View of the Contacts API and the Create new version button.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/publish_version.png)
3. Enter the new version.
4. Click Create.

A new version of your API is created with the same content as the latest version.
The mock and documentation are disabled by default.

## Publishing an API version to Qlik Catalog

Publish a version of an API contract to a Qlik space so collaborators can find it in Qlik Catalog.

You are an owner of the API or an editor of the API version.

When you publish a version, the contract version becomes immutable and read-only in API Contracts. To make changes, create a new version from the latest version and continue working on the new version.

1. On the homepage, click the version that you want to publish to open the Preview, then click
   Publish.

   ![View of the Contacts API and the Publish button.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/publish_version.png)
2. In the publication dialog box, select the Qlik space where you want the version to be published.
3. Review the version preview and enter a publication note.
4. Click Publish.

The selected version is published to the chosen Qlik space and becomes read-only in API Contracts. If you need to edit the contract again, create a new version first.

## Deleting an API version

You are an owner of the API.

1. On the homepage, click the ![Menu](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/apis_menu.png) button next to the version that you want to delete and click
   Delete.
2. Click Delete to confirm.

The selected version is deleted. If you want to delete an entire API, you need to
delete each version.

## Importing version content

Import content from an existing contract into an API version, replacing or merging its current content.

You are an owner of the API or an editor of the API version.

Use this feature to update a version from an external contract file without creating
a new version. The version identifier is preserved throughout the import.

This is different from [importing a
definition](ImportingDefinition.htm "Import an existing API definition into API Contracts."), which creates a new API in API Contracts.

1. Open Import version content for the version you want to
   update.

   This action is unavailable for a read-only version.

   You can access this action from the following locations:

   - On the homepage, click ![Menu](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/apis_menu.png) next to the version and click Import version content.

     ![Import version content option in the menu button.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/import-version-content-2.png)
   - On the Preview of the version, click ![Menu](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/apis_menu.png)  >
     Import version content.

     ![Version Detail View](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/import-version-content-3.png)
   - In the version editor, click Edit  > Import version content.

     ![Import version content option in the version editor.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/import-version-content.png)
2. Select a format and a source for the contract to import.

   You can import from a local file, a URL, or text you paste directly into the
   dialog box.
3. Under Behavior, select how to apply the imported
   content.

   - Replace: overwrites all current content with the
     imported contract. The API name, version identifier, and specification
     version are preserved.
   - Merge: combines the imported content with the
     existing version content. The API name and version identifier are preserved.
     If an imported element has the same name as an existing element, the
     imported element is renamed with a \_merge suffix (for
     example, User\_merge). Duplicate base URLs and media types
     are skipped.

   ![Import version content dialog box.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/import-version-content-dialobox.png)
4. Click Import.

The version editor opens with the updated content applied.
