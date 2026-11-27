---
title: "Managing IdP configurations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-changing-idp.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Deploying Qlik Cloud", "Identity providers in Qlik Cloud"]
---

# Managing IdP configurations

Manage identity provider (IdP) configurations to control how users authenticate in your tenant. This includes activating, deactivating, validating, editing, or deleting IdPs as needed.

Do the following:

1. In the Administration activity center, open the section Identity provider.
2. In the table, to the far right, click ... for the IdP that you want to edit.

   A sub menu is displayed with options for activating/deactivating, validating, editing, and deleting IdPs.

## Activating and deactivating the IdP

You can have several different interactive IdPs configured in parallel, but only one active at a time. The others need to be deactivated or deleted. When you deactivate an interactive IdP, you automatically revert back to the Qlik Account configuration. For more information, see [*Deleting the IdP*](#Deleting).

## Validating the IdP

To validate an IdP configuration, select Validate during creation or editing. This action initiates the validation process, which includes logging in to the identity provider and completing additional steps to ensure the configuration is correct.

## Editing the IdP

You can edit IdPs of all types. After editing, validate your changes to ensure that the IdP is working properly.

Information noteChanges to the IdP configuration are not applied immediately. The previous settings remain active until the new ones have been validated successfully. To activate the updated configuration, you must complete the validation process.

## Deleting the IdP

The default IdP is Qlik Account. You can change to a corporate IdP of your choice. If you later decide to delete the corporate IdP, you need to be aware of the consequences.

Warning noteDeleting an identity provider can make the [tenant](#glossary-0 "Glossary term") inaccessible for users.

When you delete a corporate IdP, the tenant reverts back to Qlik Account. Users who access the tenant via the deleted corporate IdP can no longer log in, nor can they can access content that they created. However, their content is visible by Qlik Account tenant administrators who could adjust ownership.

Also, if those users previously used Qlik Account, with the same email address as for the corporate IdP, any content created during the period with the Qlik Account is preserved.

Information noteInstead of deleting the IdP, you can deactivate the IdP. The tenant then reverts back to Qlik Account.

Related learning:

- [Integrating an external identity provider with Qlik Cloud](/lnk/Integrating_external_identity_provider_Cloud)
