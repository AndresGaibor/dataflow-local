---
title: "Connecting ChatGPT to the Qlik MCP server"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikMCP/connecting-chatgpt-qlik-mcp.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik MCP server", "Connecting to the Qlik MCP server"]
---

# Connecting ChatGPT to the Qlik MCP server

Connect to the Qlik MCP server by
creating an app in ChatGPT.

You can connect ChatGPT to the Qlik MCP server using one of the following methods:

- [*Connecting to ChatGPT using CIMD*](#Connecti)
- [*Connecting to a ChatGPT enterprise organization (DCR)*](#Connecti2)
- [*Connecting to ChatGPT using a manually created OAuth client*](#Connecti3)

Tip note

Before you connect, get the Qlik MCP server URL for your tenant: https://<tenant-id>.<region>.qlikcloud.com/api/ai/mcp

Tip note

Ask your tenant administrator which connection method to use.

Information note

Your ChatGPT plan must support connecting to third party MCP servers.

## Connecting to ChatGPT using CIMD

Use this method when your ChatGPT app offers CIMD as the OAuth registration method. A
tenant administrator must complete the first connection and approve the requested scopes.
After approval, other users in the same tenant can authenticate with the same approved
client identity.

Do the following:

1. In ChatGPT, create a plugin and enter a name for your connection.
2. Enter the MCP server URL: https://<tenant-id>.<region>.qlikcloud.com/api/ai/mcp.
3. In the advanced OAuth settings, select CIMD as the registration method.
4. Review the callback URLs, metadata URLs, and requested scopes displayed by
   ChatGPT.
5. Click Create to connect the plugin.
6. Sign in to your Qlik Cloud tenant to start the consent process.
7. Click Approve.

   Warning noteBy clicking Approve, you will
   enable the Qlik MCP server to
   share your Qlik Cloud data
   ("Content") with a third-party system (like an AI tool). That system is not
   managed by Qlik, and your
   Content will be stored, processed, and managed under the third party's
   control.
8. Test your connection by asking a question about a known application to which you have access.

## Connecting to a ChatGPT enterprise organization (DCR)

The steps depend on whether you are a ChatGPT organization admin or a non-admin user in the organization:

- [*Connecting as a ChatGPT organization admin (DCR)*](#ConnectingAdmin)
- [*Connecting as a non-admin user in a ChatGPT enterprise organization (DCR)*](#ConnectingNonAdmin)

Information note

This section refers to two administrator roles:

- ChatGPT organization admin: An administrator in your
  ChatGPT enterprise account who can publish and manage shared apps.
- Qlik Cloud tenant administrator: An administrator in
  your Qlik Cloud tenant who manages
  OAuth client settings and approvals.

These roles can be assigned to the same person or to different people. The procedures
below assume your Qlik Cloud tenant
administrator is also your ChatGPT organization admin.

### Connecting as a ChatGPT organization admin (DCR)

Use this method when a ChatGPT organization admin creates the first connection and shares
it with other users.

Before you begin, a tenant administrator must enable OAuth DCR for the tenant. For instructions, see [*Configuring OAuth dynamic client registration*](../Admin/oauth-dynamic-client-registration.htm).

Do the following:

1. In ChatGPT, go to Settings > Apps > Advanced Settings and turn on Enable Developer Mode.
2. Click Create App.
3. After Name, enter a name for your
   connection.
4. After MCP Server URL, enter https://<tenant-id>.<region>.qlikcloud.com/api/ai/mcp.
5. Select the confirmation option I understand and
   want to continue.
6. Click Create. ChatGPT registers a dynamic OAuth
   client in your Qlik Cloud
   tenant.
7. Sign in to your Qlik Cloud
   tenant.
8. Click Approve.

   Warning noteBy clicking Approve, you will
   enable the Qlik MCP server to
   share your Qlik Cloud data
   ("Content") with a third-party system (like an AI tool). That system is not
   managed by Qlik, and your
   Content will be stored, processed, and managed under the third party's
   control.
9. To share the connection with your organization, click Publish for the app.
10. Test your connection by asking a question about a known application to which you have access.

### Connecting as a non-admin user in a ChatGPT enterprise organization (DCR)

If you are not a ChatGPT organization admin, you can create and publish the app, but the
app remains unavailable to other users until a ChatGPT organization admin completes an
additional approval step. For more information, see [*ChatGPT organization admin app approval*](#ChatGPT).

Do the following:

1. In ChatGPT, go to Settings > Apps > Advanced Settings and turn on Enable Developer Mode.
2. Click Create App.
3. After Name, enter a name for your
   connection.
4. After MCP Server URL, enter https://<tenant-id>.<region>.qlikcloud.com/api/ai/mcp.
5. Select the confirmation option I understand and
   want to continue.
6. Click Create.
7. Click Publish for the app.
8. Notify your ChatGPT organization admin that they must connect and approve this
   app in their own ChatGPT account within one hour.

   Warning note

   If the ChatGPT organization admin does not approve the app within one hour,
   Qlik Cloud deletes the unapproved
   OAuth client automatically. You must then create the app again.
9. Test your connection by asking a question about a known application to which you have access.

#### ChatGPT organization admin app approval

A ChatGPT organization admin must do the following within one hour after the app is
published:

Do the following:

1. In their own ChatGPT account, open Apps.
2. Select the published app.
3. Click Connect.
4. Sign in to your Qlik Cloud
   tenant.
5. Click Approve.

   Warning noteBy clicking Approve, you will
   enable the Qlik MCP server to
   share your Qlik Cloud data
   ("Content") with a third-party system (like an AI tool). That system is not
   managed by Qlik, and your
   Content will be stored, processed, and managed under the third party's
   control.

## Connecting to ChatGPT using a manually created OAuth client

Use this method if your tenant is not configured for DCR or if your organization requires
manual OAuth client setup.

Do the following:

1. In ChatGPT, go to Settings > Apps > Advanced Settings and turn on Enable Developer Mode.
2. Click Create App.
3. After Name, enter a name for your
   connection.
4. After MCP Server URL, enter https://<tenant-id>.<region>.qlikcloud.com/api/ai/mcp.
5. Under Authentication, select OAuth.
6. Click Advanced settings.
7. Under Registration method, select User-Defined OAuth Client.
8. Copy the Callback URL and do one of the
   following:

   - If you are a tenant administrator, use the callback URL to create an
     OAuth client.

     See [*Manually created OAuth client*](Administering-Qlik-MCP.htm#ManualOAuth).
   - If you are not a tenant administrator, contact your tenant administrator
     and provide the callback URL so they can create an OAuth client for
     you.
9. For the OAuth Client ID, enter the Client
   ID of the OAuth client.
10. For the OAuth Client Secret, do one of the
    following:

    - For Native and Single-page application clients, leave the field empty.
    - For Web clients, enter the client
      secret.
11. Click Create.
12. Sign in to your Qlik Cloud
    tenant.
13. Click Approve.

    Warning noteBy clicking Approve, you will
    enable the Qlik MCP server to
    share your Qlik Cloud data
    ("Content") with a third-party system (like an AI tool). That system is not
    managed by Qlik, and your
    Content will be stored, processed, and managed under the third party's
    control.
14. Test your connection by asking a question about a known application to which you have access.
