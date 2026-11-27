---
title: "Sharing embed codes for anonymous access"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Share/anonymous-access-embed-code.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Using analytics to explore data", "Sharing and downloading application content", "Sharing application content with anonymous access"]
---

# Sharing embed codes for anonymous access

After anonymous access has been turned on for an application, an embed code is made available in Qlik Cloud. This embed code contains an access code that automatically authenticates external users against the Qlik Cloud tenant, allowing them to consume application content without logging in.

For more information about anonymous access, including requirements and [permissions](#glossary-0 "Glossary term"), see [*Sharing application content with anonymous access*](share-anonymous-access.htm).

Information note
This functionality is only available with a Qlik Anonymous Access subscription. For more information, see [*Qlik Anonymous Access subscriptions*](../Admin/subscription-options-anonymous.htm).

## Using embed codes

The integration of Qlik Sense application content into an external web site or application is known as a mashup. You use qlik-embed to integrate the application content from an anonymous access tenant into your mashup. The embed code that you generate in Qlik Cloud is used to provide authentication for consumers of the mashup.

Application content from an anonymous access tenant can be embedded as any of the following:

- An entire application (that is, all sheets in the application)
- One or more sheets
- One or more individual visualizations

The following references on the Qlik Cloud developer portal can help you with using qlik-embed for anonymous access:

- [Anonymous Access with](https://qlik.dev/embed/qlik-embed/quickstart/qlik-embed-anonymous-tutorial/)
  [qlik-embed](https://qlik.dev/embed/qlik-embed/quickstart/qlik-embed-anonymous-tutorial/)
  : Quick start tutorial that guides you through the process of sharing content on public websites with Qlik Anonymous Access.
- [Create an anonymous OAuth2 client](https://qlik.dev/authenticate/oauth/create/create-oauth-client-anonymous/): Tutorial guiding you the process of creating an OAuth client to use to provide anonymous access to content. For further information, see [*Creating an OAuth client for anonymous embedding of application content*](#CreateOAuth).
- [qlik-embed](https://qlik.dev/embed/qlik-embed/): Home page for qlik-embed.
- [Auth overview](https://qlik.dev/embed/qlik-embed/authenticate/connect-qlik-embed/): Overview of how authentication works with qlik-embed.

## Structure of embed codes

The embed code contains an access code that provides authentication for anonymous users. This access code is shared between the application link and the embed code.

## Creating an OAuth client for anonymous embedding of application content

To embed application content for anonymous access using qlik-embed, you need to create an OAuth client with a type specifically designed for this use case.

Do the following:

1. In the Administration [activity center](#glossary-1 "Glossary term"), go to the OAuth section.
2. Click Create new.
3. In the Client type dropdown menu, select Anonymous embed.
4. Enter a Name and optionally a Description for the OAuth client.
5. Under Allowed origins, enter each origin that you need to authorize. These are the domains that will be accessing the Qlik Cloud tenant to retrieve the information for the embedded analytics.

   Click Add after inserting each URL.
6. When you are done, click Create.
7. Click Copy to clipboard to save the client ID  for later use. It will be needed when the application content is embedded with qlik-embed.
8. Click Done.

## Copying an embed code for an application

After anonymous access is turned on for an application, you can copy the embed code from the sharing dialog for the application. To do this, you need the Owner or Can manage role in the application's space, as well as a value of Allowed for Anonymous access link.

Do the following:

1. Activate anonymous access for the application. See [*Turning anonymous access on and off*](share-anonymous-access.htm#Activate).
2. Click Share > Invite. The sharing dialog opens.
3. In the section Anyone with the link, click ![Cogwheel](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) to open the settings.
4. Under Embed code, click ![Copy](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_copy.svg) to copy the code.

   You can now use the embed code in your web content to allow anonymous access to the analytics.

## Resetting the access code

You can reset the access code if needed. For more information, see [*Resetting the access code*](share-anonymous-access.htm#AccessReset).
