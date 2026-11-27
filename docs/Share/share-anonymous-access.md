---
title: "Sharing application content with anonymous access"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Share/share-anonymous-access.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Using analytics to explore data", "Sharing and downloading application content"]
---

# Sharing application content with anonymous access

With [anonymous access](#glossary-0 "Glossary term"), you can allow people outside of the Qlik Cloud tenant to access Qlik Sense application content. You can share apps as links that can be opened by anyone, or you can use qlik-embed to embed application content directly into other web pages and applications.

Anonymous access is controlled at the application level. Users with the correct permissions can turn anonymous access on and off as needed. These users can also configure access code settings, as well as view and copy links and codes that provide anonymous access.

Information note
This functionality is only available with a Qlik Anonymous Access subscription. For more information, see [*Qlik Anonymous Access subscriptions*](../Admin/subscription-options-anonymous.htm).

Qlik Cloud Government note

Qlik Anonymous Access subscriptions are not available in Qlik Cloud Government.

## Terminology on this page

The following terminology is used in content about anonymous access:

- Anonymous users: Users who are accessing application content without signing in, either through anonymous access links to an application or by consuming embedded analytics anonymously. These users are not members of the Qlik Cloud tenant, and also do not require Qlik accounts.
- Tenant users: Users who are members of the tenant and manage the tenant or develop analytics for consumption by anonymous users. Tenant users may have administrator privileges in the tenant.

## Use cases

Anonymous access allows public consumption of analytics without authentication. You can use anonymous access to share application content in the following ways:

- Create links to apps that can be opened to explore their sheets. Anyone with an internet connection can open these links.
- Generate embed codes that can be used to integrate application content directly into web sites and applications. The end result can be consumed without authentication to Qlik Cloud.

Anonymous access allows you to securely build and share Qlik analytics on a global scale. There are many possible use cases, including:

- An organization wants to provide a link within their website to a Qlik Sense application where anyone can access statistics about market trends or the organization's community impact.
- An organization wants to embed insights for a limited set of data into their public-facing website. For example, they could embed a visualization where users can view and interact with real-time data that is in the public domain.

## Workflow

1. Build your application

   Create a Qlik Sense application with a data model and visualizations reflecting the data you want to show to external audiences.

   [*Creating analytics with Qlik Sense*](../Apps/working-with-apps-hub.htm)
2. Publish the application to a managed space

   When the base sheets and data structure are finalized, publish the application to a managed space. At this time, you can also configure how the application will be reloaded to reflect new data.

   [*Publishing applications*](../Apps/publish-app-cloud-hub.htm)

   [*Reloading application data*](../Apps/reloading-apps-cloud-hub.htm)
3. Activate anonymous access

   For each application that you want to make available with anonymous access, you need to first turn on anonymous access. When you do this, the application link and embed code become visible, and can be used.

   [*Turning anonymous access on and off*](#Activate)
4. Option 1: Distribute the application link for anonymous access

   [*Sharing application links for anonymous access*](anonymous-access-app-link.htm)
5. Option 2: Use the embed code to integrate the application content into web sites and applications

   [*Sharing embed codes for anonymous access*](anonymous-access-embed-code.htm)

## Security considerations

When you make application content available with anonymous access, it becomes accessible without authentication to Qlik Cloud. In some cases (for example, in the case of embedding in websites), it becomes available to the public.

Consider the following best practices for data security when working with anonymous access:

- Do not share apps containing sensitive information via anonymous access.
- Use extra caution when loading data from shared data sources into apps, and then making it available with anonymous access. These data sources can change over time and you might not be aware of changes by other users.

## Setting permissions

Tenant administrators control the ability of each user in the tenant to configure [anonymous access](#glossary-2 "Glossary term") for applications. They do this in the Administration [activity center](#glossary-3 "Glossary term").

For more information, see [*Setting permissions for users who can configure anonymous access*](../Admin/permissions-anonymous-access.htm).

## Requirements

To work with anonymous access, you need:

- Access to a tenant created within a Qlik Anonymous Access subscription. Applications you want to share need to be located in this tenant.
- The required permissions in both the [tenant](#glossary-4 "Glossary term") and in the space where the application is located. See [*Permissions for configuring anonymous access*](#PermissionsAnonymous).
- The application you are sharing for anonymous access needs to be in a [managed space](#glossary-5 "Glossary term").
- If you are using qlik-embed, a specific OAuth client must be set up in the tenant. This needs to be done by a tenant administrator. See [*Creating an OAuth client for anonymous embeds of application content*](../Admin/oauth-client-anonymous-embed.htm).

### Permissions for configuring anonymous access

In Qlik Cloud Analytics, working with anonymous access involves the following:

- Turning anonymous access on and off for an application
- Managing access code settings
- Viewing and copying application and embed links

#### Permissions for toggling anonymous access

To turn anonymous access on and off for an application, you need the following space roles and administrator-assigned permissions:

- A value of Allowed for the Anonymous access link permission. This is assigned by a tenant administrator. You can receive the permission through the default permissions or a custom role.

  For more information, see [*Setting permissions for users who can configure anonymous access*](../Admin/permissions-anonymous-access.htm).

  Information note

  Tenant administrators also need this permission to be able to configure anonymous access.
- One of the following space roles in the managed space where the application is located:

  - Owner (of space)
  - Can manage

#### Permissions for copying links

After anonymous access is turned on for an application, a user with one of the following space roles in the application's space can copy the link:

- Owner (of space)
- Can manage
- Can contribute
- Can view
- Has restricted view
- Can operate

For more information, see [*Copying an anonymous access link to an application*](anonymous-access-app-link.htm#CopyAppLink).

#### Permissions for copying embed codes

After anonymous access is turned on for an application, a user with one of the following space roles in the application's space can copy the embed code:

- A value of Allowed for the Anonymous access link permission. This is assigned by a tenant administrator. You can receive the permission through the default permissions or a custom role.

  For more information, see [*Setting permissions for users who can configure anonymous access*](../Admin/permissions-anonymous-access.htm).

  Information note

  Tenant administrators also need this permission to be able to copy embed codes.
- One of the following space roles in the managed space where the application is located:

  - Owner (of space)
  - Can manage

For more information, see [*Copying an embed code for an application*](anonymous-access-embed-code.htm#CopyCode).

## Development of apps used for anonymous access

There are many options available for development of the apps you want to shared from a Qlik Anonymous Access tenant. For example:

- You can develop your application in the Qlik Anonymous Access tenant itself.
- The Qlik Platform Operations connector is also available for Qlik Anonymous Access tenants. With this Qlik Automate connector, you can develop your application in a different tenant, and then distribute it to the tenant from which you are sharing it anonymously. For more information about the connector, see [Qlik Platform Operations connector overview](https://qlik.dev/manage/platform-operations/no-code/overview/).

## Turning anonymous access on and off

When you turn anonymous access on, the application link and embed code become usable, and are made available for copying and distribution.

Do the following:

1. In Qlik Cloud Analytics, open the Insights or Analytics activity center.
2. Right-click the application, or click the ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) icon next to it.
3. Click Invite > Share. The sharing dialog opens.
4. In the section Anyone with the link, use the toggle switch to activate and deactivate anonymous access.

## Revoking anonymous access to an application

If you need to revoke access to the application by anonymous users, there are two actions you should consider: Deactivating anonymous access entirely, and resetting the access code.

### Deactivating the application from anonymous access

When you turn off access entirely, the application will no longer be accessible by any user outside of the tenant. For instructions about turning off anonymous access, see [*Turning anonymous access on and off*](#Activate).

### Resetting the access code

When you turn on anonymous access, the application link and embed code contain an access code. This access code does not expire. You can reset the access code so users with the old access code can no longer access the application, but users with the new access code can access it.

Resetting the access code affects both the application link and embed code.

Do the following:

1. In Qlik Cloud Analytics, open the Insights or Analytics [activity center](#glossary-6 "Glossary term").
2. Right-click the application, or click the ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) icon next to it.
3. Click Invite > Share. The sharing dialog opens.
4. In the section Anonymous access, click ![Cogwheel](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) to open the settings.
5. Click Reset access code.

After you have reset the access code, you can copy the new application link and embed code. Alternatively, return to the previous page in the dialog to copy them.

## Viewing the apps in the space that are activated for anonymous access

Members of the managed space with the Owner and Can manage can see the apps that have anonymous access turned on. This is shown in Space settings > Members. Anonymous access is listed as a space member.

Turn off anonymous access for an application by clicking ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to the application and clicking ![Trash bin](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin2.svg) Turn off.

The Members section of a managed space, showing Anonymous access as a member with access to two apps.

!['Members' section of the Space settings page, listing 'Anonymous access' as a user with access to specific apps](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_space-members-anonymous.png "Click to view full size")

## Consuming content shared through anonymous access

For anonymous users to consume content, temporary application sessions are created to allow them access to the application. Each anonymous session lasts 15 minutes. For an anonymous user to continue analyzing content, they can refresh their browser, starting a new 15 minute session.

For more information about how anonymous users can navigate and explore application content, see [*Analyzing data without being added to a Qlik Cloud tenant*](analyze-anonymous-content.htm).

## Viewing the tenant's anonymous access capacity

Tenant and analytics administrators can view the tenant's purchased capacity for anonymous access. This information is shown in the Administration activity center.

For more information, see [*Anonymous access capacities*](../Admin/mc-monitor-consumption.htm#AnonymousAccess).

## Limitations

In the context of a Qlik Anonymous Access subscription, anonymous access has the following limitations:

- In Qlik Anonymous Access tenants, application developers can access many of the other capabilities that are available in Qlik Cloud tenants. A number of capabilities are not available in Qlik Anonymous Access tenants. For a list of what is available and unavailable, see [*Qlik Anonymous Access specifications and capacity limits*](../Introduction/qcs-specs-capacity-anonymous-access.htm).
- With qlik-embed, you embed visualizations into external sources for anonymous consumption. When embedding visualizations for anonymous access, there are limitations for certain visualizations depending on the [qlik-embed UI types](https://qlik.dev/embed/qlik-embed/parameters/#ui-types). The same visualization-specific limitations also apply for anonymous access. In addition, the NL insights native object cannot be used in any embedding of application content for anonymous access.

  For more information about the limitations, see [Visualizations](https://qlik.dev/embed/foundational-knowledge/visualizations/).
- Large application support is not available in Qlik Anonymous Access subscriptions.
- The write table does not support anonymous access and is not available in Qlik Anonymous Access subscriptions.
