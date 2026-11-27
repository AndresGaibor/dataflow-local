---
title: "Configuring OAuth dynamic client registration"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/oauth-dynamic-client-registration.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Securing the system", "Creating and managing OAuth clients"]
---

# Configuring OAuth dynamic client registration

OAuth Dynamic Client Registration (DCR) is a tenant-level OAuth capability that allows compatible OAuth client applications to register OAuth clients dynamically. In this context, a compatible OAuth client application is one that supports the OAuth 2.0 DCR protocol and meets your tenant policy requirements.

The primary use case for DCR is connecting Model Context Protocol (MCP) server clients, but you can also use it for other compatible third-party applications.

For more methods to connect to an MCP client, see [*Creating an OAuth client*](../QlikMCP/Administering-Qlik-MCP.htm#ConnectiAuth).

Information note

Publishing and consent are separate controls:

- Publishing constrains whether an OAuth client can be used by other tenants in the same region.
- Consent method (Required or Trusted) controls whether users are prompted during authorization.

For details on manual setup and consent behavior, including publication constraints, see [*Creating OAuth clients*](mc-create-oauth-client.htm#Creating2) and [*Consent methods*](oauth-publishing-and-consent.htm#Consent) .

## Prerequisites and cautions

Prerequisites:

- You are a tenant administrator in Qlik Cloud.

Cautions:

- When DCR is enabled, compatible OAuth client applications can request OAuth client registration in your tenant according to your DCR policy. Review your allowed authentication methods and approval process before enabling DCR in production.
- DCR-created clients are initially assigned the user\_default, mcp:execute, and offline\_access scopes. To learn more on these scopes,
  see a complete list of scopes on the Qlik Developer Portal [Scopes](https://qlik.dev/manage/access-control/scopes/).
- Unapproved DCR clients are automatically deleted after one hour. If no tenant administrator approves the client in the third-party application within that period, the client is deleted and users must create the connection again.

## Configuring DCR settings

Configure Dynamic Client Registration settings to control how OAuth client applications can register OAuth clients in your tenant.

### Configuring DCR in Qlik Cloud

Do the following:

1. In the Administration activity center, go to Settings > Security.
2. Enable Dynamic client registration.

   When DCR is disabled, no new clients can be registered dynamically. Existing dynamically registered clients remain functional until you manually remove them or revoke their approval.
3. From Allowed authentication methods, select the authentication methods that dynamically registered clients can use:

   - Client secret: Allows confidential clients, such as web applications with secure backends.
   - Client secret + None: Allows both confidential clients and public clients.
   - None: Allows public clients, such as single-page applications or native applications.

   Applications attempting to register with a method not allowed by your policy are rejected.

   For more information on these authentication methods, see the following section [*Authentication methods*](#Authenti).

### Configuring DCR in OAuth client app

After you configure DCR in Qlik Cloud, configure the DCR connection in your OAuth client application. The connection details differ by use case.

Do the following:

1. Use the connection URL for your use case when configuring the connection in the OAuth client application:

   | Use case | Connection URL format |
   | --- | --- |
   | MCP or GenAI clients | https://<tenant-id>.<region>.qlikcloud.com/api/ai/mcp For more MCP configuration information, see [*Connecting to the Qlik MCP server*](../QlikMCP/Connecting-Qlik-MCP-server.htm). |
   | Other OAuth client applications | https://<tenant-id>.<region>.qlikcloud.com |
2. Review the approval and consent behavior for newly registered DCR clients:

   - Verify that new DCR clients require explicit tenant approval before they can be used. In the third-party application, grant approval when prompted.
   - The first approved connection uses Required consent.
   - After approval, edit the client in Qlik Cloud and change its consent method to Trusted if that matches your security policy.

   Tenant approval establishes tenant-level trust between your Qlik Cloud tenant and the OAuth client application. After a tenant administrator connects, authenticates, and approves the consent request, other users can connect to Qlik Cloud through the same OAuth application without requiring their own consent approval.

   The consent method is managed per client after approval. For more information, see [*Consent methods*](oauth-publishing-and-consent.htm#Consent) .

### Authentication methods

When configuring DCR settings, you can specify which authentication methods dynamically registered clients are allowed to use. The following authentication methods are available:

- Client secret: Allows confidential clients that authenticate using a client secret. The client receives a client secret when registered. This includes both client\_secret\_basic and client\_secret\_post authentication methods.
- None: Allows public clients that do not use a client secret. These clients use authorization code flow with PKCE (Proof Key for Code Exchange) for authentication.

By default, dynamically registered clients use the client\_secret\_basic authentication method unless specified otherwise during registration.

## Managing multiple registrations from vendors

After approving a DCR client, you can change its access and refresh token durations. See [*Configuring OAuth token duration*](oauth-token-duration.htm).

Many OAuth client applications dynamically register a single OAuth client with Qlik Cloud. Users of the application share the same OAuth client.

Some OAuth client applications dynamically register multiple OAuth clients, one per user. This behavior has been observed with:

- Anthropic Claude
- Antigravity

If you see many DCR clients from the same vendor, review how that OAuth client application registers clients and whether a shared-connector option is available. To delete unwanted DCR clients in bulk, see [*Deleting OAuth clients*](mc-create-oauth-client.htm#Deleting).

Claude and Claude Code support CIMD, which avoids the multiple-registration problem. See [*Connecting Claude to the Qlik MCP server*](../QlikMCP/connecting-claude-qlik-mcp.htm).

## MCP access example

One use case for DCR is onboarding OAuth clients for Qlik MCP server integrations. DCR is not limited to MCP and can be used by other compatible OAuth client applications. For MCP-based connections, the tenant administrator usually creates the first connection and approves the client before other users connect.

For MCP administration and connection guidance, see:

- [*Deploying and administering Qlik MCP server*](../QlikMCP/Administering-Qlik-MCP.htm)
- [*Connecting to the Qlik MCP server*](../QlikMCP/Connecting-Qlik-MCP-server.htm)

For guidance on managing OAuth clients after they're created—including handling multiple vendor registrations, bulk deletion, and identifying DCR or CIMD clients—see [*Identifying how a client was registered*](mc-create-oauth-client.htm#Managing2).
