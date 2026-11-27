---
title: "Sharing application links for anonymous access"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Share/anonymous-access-app-link.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Using analytics to explore data", "Sharing and downloading application content", "Sharing application content with anonymous access"]
---

# Sharing application links for anonymous access

After anonymous access has been turned on for a Qlik Sense application, a link to the application becomes available. This link can be opened by anyone and requires no authentication. This makes it easy to share analytics with users who are not members of the Qlik Cloud tenant.

When an external (anonymous) user opens the link to the application, they can explore the analytics with a limited version of the application. For information about what features and actions anonymous users have access to, see [*Qlik Anonymous Access specifications and capacity limits*](../Introduction/qcs-specs-capacity-anonymous-access.htm) and [*Managed space permissions for anonymous users*](../Spaces/permissions-managed-space-anonymous.htm).

For more information about anonymous access, including requirements and [permissions](#glossary-0 "Glossary term"), see [*Sharing application content with anonymous access*](share-anonymous-access.htm).

Information note
This functionality is only available with a Qlik Anonymous Access subscription. For more information, see [*Qlik Anonymous Access subscriptions*](../Admin/subscription-options-anonymous.htm).

## Structure of anonymous access links

The anonymous access link for an application is similar to a regular link to an application, except that it also contains an access code. This access code is what provides authentication for anonymous users.

In the application link, the access code is defined in the eac parameter. For example, you might see the following format:

https://<tenant and application address>?eac=<access code>

## Copying an anonymous access link to an application

Before anyone else can copy the anonymous access link, the apps needs to have anonymous access turned on. See [*Turning anonymous access on and off*](share-anonymous-access.htm#Activate).

After copying the anonymous access link to your clipboard, you can now distribute it to others and they can use it to open the application without needing to log in.

### Option 1: Using the Copy link action

Users can copy the link directly from the ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) menu in their activity center.

To copy the link, you need one of the following space roles in the application's space:

- Owner (of space)
- Can manage
- Can contribute
- Can view
- Has restricted view
- Can operate

Do the following:

1. In Qlik Cloud Analytics, open the Insights or Analytics [activity center](#glossary-1 "Glossary term").
2. Right-click the application, or click the ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) icon next to it.
3. Click Copy link.

If you do not have one of the required space roles, the application link does not contain the access code. Therefore, it can only be used by Qlik Cloud users who can access the application.

### Option 2: Copying from the sharing dialog

After anonymous access is turned on, you can also copy the link from the sharing dialog for the application. To do this, you need the Owner or Can manage role in the application's space, as well as a value of Allowed for Anonymous access link.

1. In Qlik Cloud Analytics, open the Insights or Analytics [activity center](#glossary-2 "Glossary term").
2. Right-click the application, or click the ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) icon next to it.
3. Click Share > Invite. The sharing dialog opens.
4. In the section Anyone with the link, click ![Cogwheel](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) to open the settings.
5. Under Link, click ![Copy](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_copy.svg) to copy the anonymous access link.
6. You can now distribute the link to others and they can use it to open the application without needing to log in.

## Resetting the access code

You can reset the access code if needed. For more information, see [*Resetting the access code*](share-anonymous-access.htm#AccessReset).

## Learn more

- [*Analyzing data without being added to a Qlik Cloud tenant*](analyze-anonymous-content.htm)
