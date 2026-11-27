---
title: "Adding links in the Analytics activity center"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Hub/links.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing resources", "Creating and managing generic links"]
---

# Adding links in the Analytics activity center

Links provide easy access to useful content, making valuable resources readily available in relevant spaces.

## Who can create links

- Tenant admins can add links to all spaces, including their personal space.
- Analytics admins can add links to all spaces except personal spaces.
- Users with the Owner or Can manage role in a space, along with permissions assigned by an administrator (see [*The Manage links permission*](../Admin/mc-administer-generic-links.htm#ManageLinks)), can add links to those specific spaces. They cannot add links to their personal space.

## Access control for linked content

Access to linked content is controlled by the permissions at the destination of the link. If a member has access to the space where the link is added but lacks permission for the linked content, they cannot view it.

## Bulk management of links

Administrators can manage multiple links in the Administration activity center.
For more information, see [*Creating and managing generic links*](../Admin/mc-administer-generic-links.htm).

## Creating links

This section describes how to add generic links in the Analytics activity center.
For instructions on adding links to application sheets, see [*Sharing links to sheets*](../Sheets/link-sheet-to-hub.htm).

Do the following:

1. Go to the Create page of the Analytics activity center and select Link.
2. To add an image, drag and drop an image file or click Browse to select the file.
3. Enter the following link details:

   - Name: Enter a name for the link.
   - Link URL: Enter the URL in the format https://domain.com.

     - Only HTTPS URLs are allowed.
     - Domain names can contain letters (a-z), numbers (0-9), and hyphens (-), but not underscores (\_) or the '@' symbol. For example, https://my-domain.com/ is valid, while https://my\_domain.com/ is not.
   - Space: Select the space where the link will be added.
   - Description (optional): Enter a description for the link.
   - Tags (optional): Add tags to help categorize the link.
4. Click Create.

A generic link added in a shared space.

![A generic link with the name Community added in a shared space.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_generic_link.png "Click to view full size")

## Sharing links

You can share a link by inviting a user, group, or everyone in your tenant to the space where it is stored.

Do the following:

1. In the catalog, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the item to be shared and select Share > Invite.
2. Search for users or groups by name or email address.
3. Select space permissions for the users or groups.
4. Or, select permissions for Anyone at <your tenant name> from the dropdown list.
5. Click Done.

The users receive access to the shared item and all other content in the space.

## Moving links

You can move links to a different space.

Do the following:

1. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the link and select Manage > Move to space.
2. Choose a new space.
3. Click Move.

## Editing links

Do the following:

1. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the link and select Manage > Edit details.
2. Modify the details as needed.
3. Click Save.

## Deleting links

Do the following:

1. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the link and select Delete.
2. Confirm the deletion.
