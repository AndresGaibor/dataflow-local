---
title: "Deploying and administering Qlik MCP server"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikMCP/Administering-Qlik-MCP.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik MCP server"]
---

# Deploying and administering Qlik MCP server

Qlik MCP Server is available with all Qlik Cloud subscriptions, but it must be activated by a tenant administrator. Qlik MCP server is administered from the Administration activity center.

## Deploying Qlik MCP server for a tenant

A tenant administrator must do the following to allow their tenant's users to use Qlik MCP server:

1. Update user roles or create a new user role with permission to access Qlik MCP server.
2. Create an OAuth client using one of the supported creation methods.
3. Create the first MCP connection from an MCP client using an OAuth client, such as Claude or ChatGPT.

   This step must be repeated for each different MCP client identity that your users use to connect.

Information noteQlik MCP Server does not require enabling cross-region inference.

### Allowing user access to Qlik MCP server

The tenant administrator grants users access to Qlik MCP server with user role permissions. To use Qlik MCP server, users need the permission Qlik MCP set to Allowed under Features and actions > Agentic AI.

You can provide this permission to users in one of two ways:

- Provide permission to all users in the tenant through the user default permissions.
- Provide permission to select users through a custom role.

#### Providing permission through user default

Allow Qlik MCP in the default permissions to give all users in the tenant access to Qlik MCP server.

Do the following:

1. In the Administration activity center, go to Manage users > Permissions.
2. Click Manage default permissions above the table.
3. Under Features and actions > Agentic AI, set Qlik MCP to Allowed.

   Tip noteUse the search to find the Qlik MCP permission.
4. Save the changes.

   Information noteUsers must log out and log in again for the changes to be applied.

For more information, see [*Default permissions*](../Admin/permissions-admins-users.htm#UserDefault).

#### Providing permission through a custom role

Create a custom role that allows Qlik MCP, and then assign the role to the users who need access to Qlik MCP server. To limit access to these users only, make sure that Qlik MCP is not allowed in the default permissions.

Do the following:

1. In the Administration activity center, go to Manage users > Permissions.
2. Click Create new.
3. In the Create new role dialog, enter a name and description for the role.
4. Under Features and actions > Agentic AI, set Qlik MCP to Allowed.

   Tip noteUse the search to find the Qlik MCP permission.
5. Click Create.
6. Click the arrow ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down.svg) on the new role.
7. On the Users tab, click Assign.
8. Search for users by name or email and add them to the list.
9. Click Assign.

   The users are assigned the role at their next login.

You can also assign the role to groups. For more information, see [*Managing custom roles*](../Admin/permissions-custom-roles.htm) and [*Assigning security roles and custom roles*](../Admin/SaaS-roles.htm).

### Creating an OAuth client

Before connecting an MCP client to the Qlik MCP server, choose the OAuth client creation or registration method
that fits your situation. The following methods are supported:

- OAuth Client ID Metadata Documents (CIMD)
- Manually created OAuth client
- OAuth Dynamic Client Registration (DCR)

Information note

If you prefer to switch from DCR to CIMD, or vice versa, consult your MCP client's documentation to determine which methods it supports.

#### OAuth Client ID Metadata Documents (CIMD)

OAuth Client ID Metadata Documents (CIMD) let an MCP client use an HTTPS URL as its client ID. Use CIMD when your client supports it. For CIMD configuration and management details, see [*Configuring OAuth Client ID Metadata Documents*](../Admin/oauth-client-id-metadata-documents.htm).

#### Manually created OAuth client

A manually created OAuth client is an OAuth client that a tenant administrator creates
directly in the Administration activity center. The administrator provides the client ID
(and secret, for web clients) to the user connecting the MCP client.

Use this method when:

- Your MCP client requires a client ID and secret to be entered manually during
  setup.
- You want explicit administrator control over which clients can connect to your
  tenant.
- Your MCP client does not support OAuth DCR.

Do the following:

1. In the Administration activity center, go to OAuth.
2. Click Create new.
3. For the client type, select Native, Single-page application, or Web.
4. In the dialog, enter a name for the OAuth client.
5. Optionally, add a description.
6. Under Scopes, select user\_default and mcp: execute.

   Optionally, select offline\_access. This setting reduces the need to re-authenticate to once every 30 days.
7. Under Add redirect URLs, enter the authentication callback URL for the MCP client and click Add.

   These URLs come from your MCP client. For example, for Claude this is https://claude.ai/api/mcp/auth\_callback. ChatGPT generates a unique callback URL for each user.
8. Click Create.
9. Copy the Client ID.

   If you created a Web client, also copy the Client secret.

   Users need these values to connect their MCP client to the Qlik MCP server.
10. Click Done.

#### OAuth Dynamic Client Registration (DCR)

OAuth DCR allows an MCP client to register itself automatically with Qlik Cloud without the tenant administrator needing to
create an OAuth client in advance. The client presents its metadata to a
Qlik DCR endpoint, receives a
client ID dynamically, and proceeds to connect.

Use this method when:

- Your MCP client does not support CIMD.
- Your MCP client supports OAuth DCR natively. Consult your MCP client's
  documentation to confirm this support.
- You want to reduce administrator overhead, particularly when supporting
  self-service connections or connecting multiple clients.

A tenant administrator must enable OAuth DCR for the tenant before users can connect with
this method. After DCR is enabled, users with a DCR-capable MCP client can complete registration
and connection without any administrator action per client. For setup details, see
[*Configuring OAuth dynamic client registration*](../Admin/oauth-dynamic-client-registration.htm).

Warning noteQlik Cloud automatically
deletes unapproved OAuth clients created through dynamic client registration (DCR)
after one hour. This can occur in any MCP client workflow where a connection is
created but not approved within the one-hour window.

### Creating MCP connections from MCP clients

The tenant administrator must be the first user to create the connection to each new MCP client and then connect and authenticate with an OAuth client. This establishes tenant-level trust for the MCP client and the Qlik OAuth app. After the tenant administrator connects and authenticates, other users can connect to Qlik MCP server.

Follow the steps in the following topics to connect to specific MCP clients:

- [*Connecting Claude to the Qlik MCP server*](connecting-claude-qlik-mcp.htm)
- [*Connecting ChatGPT to the Qlik MCP server*](connecting-chatgpt-qlik-mcp.htm)
- [*Connecting other MCP clients to the Qlik MCP server*](connecting-other-MCP-qlik-mcp.htm)

Information noteIf your users will be using different MCP clients, you will need to repeat the connection and authentication for each different MCP client connecting to your tenant.

Information noteIf you are connecting to Qlik MCP using an orchestration framework rather than directly from an MCP client, you must create a web OAuth client. Your OAuth client must allow Allow Machine-to-Machine (M2M). This means the orchestration framework will access resources using the permissions of the OAuth user created on the first API call from the client. This user will need to be added to relevant spaces to access content.

## Administering Qlik MCP server

Qlik MCP server is administered from the Administration activity center, where you can monitor capacity usage

### Qlik MCP server capacity

Your Qlik Cloud subscription determines the quota of questions asked by users. If you are licensed for Qlik Answers, both MCP and Qlik Answers will use your monthly questions capacity

Tool calls are aggregated per user, within a tenant. Every five billable tool calls made by a user consume one question. The counter only increments once the next multiple of five is reached, so a partial group of calls is not rounded up early.

Not every tool call is billable. Some tools are excluded from billing because of how frequently they are expected to be called as part of normal platform behaviour, for example status-polling tools, rather than as a direct result of a distinct user request. These tools are marked as non-billable in the tool table below.

- qlik\_get\_automation\_run
- qlik\_get\_automation\_run\_display

### Monitoring Qlik MCP server capacity

Metering of capacity consumption is visible from Home in the Administration activity center.

Capacity consumption meter

![Capacity meter showing monthly questions.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikMCP/ui_administration-home-capacities.png "Click to view full size")

Questions (monthly) tracks the number of questions used from your monthly quota. Hover over the bars to see a tooltip with more details. The colors of the bars represent different metrics.

- Blue bar: The consumed amount this period.
- Red bar: Overage consumption. Overage is when the consumption of a resource exceeds the purchased amount for the period.
- Dark gray vertical line: The consumed amount last period

For more information on subscriptions and quotas, see the [Qlik MCP server](https://www.qlik.com/us/legal/product-terms) product description.

#### Question capacity

Question quotas are per month and reset every month. Questions do not carry over between months. When you hit your limit, users can no longer ask questions until the next month. Overage is only allowed, depending on your subscription. For more information, see [Qlik MCP server](https://www.qlik.com/us/legal/product-terms) product description.

For more information on overage, see [*Overage*](../Admin/subscription-options-qlik-cloud.htm#Overage).

#### Qlik MCP server guardrails

Guardrails are hard limits on capacities. They are used to ensure Qlik MCP server performance and stability. The following guardrails and capacities are used by Qlik MCP server:

- A tenant's Qlik MCP server can have a maximum of 200 concurrent analytics applications loaded into memory at one time. Any number of users can be connected to these applications, irrespective of whether the applications use Section Access. Connections to applications beyond 200 will fail.
- There is a maximum of 300 MCP tool calls per user per minute.
