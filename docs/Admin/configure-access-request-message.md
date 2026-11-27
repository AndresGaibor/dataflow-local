---
title: "Customizing the access request process"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/configure-access-request-message.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Configuring features and integrations"]
---

# Customizing the access request process

You can use your own process for requesting access instead of the default Qlik process. To do this, turn off the permission to request access and customize the access request message to guide users to your organization's process.

## Overview

By default, users can request access when they try to open a content through a shared link but don’t have permission. Space owners and members with the Can manage role receive a notification and can grant access.

If your organization uses a different access request flow, such as a helpdesk or service portal, you can replace the default behavior. To do this:

1. Turn off the Request access to content permission for users.
2. Customize the message shown to users when they try to access content.

The message can include instructions and a link to your organization's process.

For details on the default access request flow, see [*Approving access requests*](../Share/approving-access-requests.htm) and [*Requesting application access*](../Share/requesting-access.htm).

## Turning off default access requests

Tenant administrators can turn off the Request access to content permission in the default permissions.

Do the following:

1. In the Administration activity center, go to Manage users > Permissions.
2. Click Manage default permissions above the table.
3. Click Features and actions and select Space management.
4. Set Request access to content to Not allowed.
5. Click Confirm.

Optionally, you can create a custom role to grant this permission only to specific users. For more information, see [*Managing custom roles*](permissions-custom-roles-capacity-model.htm).

## Customizing the access request message

A pre-defined message is shown until you customize it.

Default access request message shown to users before customization.

![Pre-defined access request message.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_access-request-message.png "Click to view full size")

Changes are saved automatically and shown to all users who don't have the Request access to content permission. Only one message can exist at a time—updating it replaces the previous text.

Do the following:

1. In the Administration activity center, go to Settings > Tenant.
2. Enter the message text (maximum 255 characters).
3. (Optional) Add a link:

   1. Turn on the Link toggle.
   2. Enter the link text.
   3. Enter the link URL.

Changes are saved automatically.

Settings for access request message.

![Access request message settings.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_access-request-message-settings.png "Click to view full size")

### Example message for users

Here’s an example of a customized message, including a link, that guides users to your organization’s access request process:

- Text: "To request access to this content, please submit a ticket through our IT service portal."
- Link text: "Submit a request"
- Link URL: Link to the service portal page

Settings showing example message text and link.

![Example of access request message settings.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_access-request-message-settings-example.png "Click to view full size")

This is how the example message appears to users who try to access content they don’t have permission for:

Customized access request message shown to users.

![Example of a customized access request message.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_access-request-message-example.png "Click to view full size")
