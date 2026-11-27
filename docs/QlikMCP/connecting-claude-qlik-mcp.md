---
title: "Connecting Claude to the Qlik MCP server"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikMCP/connecting-claude-qlik-mcp.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik MCP server", "Connecting to the Qlik MCP server"]
---

# Connecting Claude to the Qlik MCP server

Connect Claude to the Qlik MCP server to work with your Qlik Cloud resources from Claude.

You can connect Claude to the Qlik MCP server using one of the following methods:

- Connect with the Qlik Connector
- Connect using OAuth CIMD

Tip note

Before you connect, get the Qlik MCP server URL for your tenant: https://<tenant-id>.<region>.qlikcloud.com/api/ai/mcp

Tip note

Ask your tenant administrator which connection method to use.

Qlik Cloud Government note

The predefined Anthropic Claude clients below are configured for commercial
implementation and not government implementations. Qlik Cloud Government and Qlik Cloud Government - DoD users must create their own OAuth clients. See
Claude for Government and ChatGPT for Government documentation, and
[*Connecting other MCP clients to the Qlik MCP server*](connecting-other-MCP-qlik-mcp.htm).

## Connecting to Claude with the Qlik Connector

The Qlik Connector is available from Claude. You can find and add it from a chat or from settings. For instructions on how to find connections in Claude, see [Use connectors to extend Claude's capabilities](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities).

Information note

If you already have a connection to a Qlik tenant, add any additional connections as custom connectors.

Do the following:

1. In Claude, go to the connectors.
2. Search for Qlik.
3. Select the Qlik Connector.
4. Click Connect.
5. For the Remote MCP server URL, enter https://<tenant-id>.<region>.qlikcloud.com/api/ai/mcp.
6. Click Add.
7. Click Connect on the Qlik Connector.
8. Sign in to your Qlik Cloud
   tenant.
9. Click Approve.

   Warning noteBy clicking Approve, you will
   enable the Qlik MCP server to
   share your Qlik Cloud data
   ("Content") with a third-party system (like an AI tool). That system is not
   managed by Qlik, and your
   Content will be stored, processed, and managed under the third party's
   control.
10. Test your connection by asking a question about a known application to which you have access.

## Connecting to Claude using OAuth CIMD

Claude offers a CIMD flow for custom connectors. Claude uses an Anthropic-hosted metadata document, and a tenant administrator approves the connection the first time it connects to your tenant. You do not need to enter an OAuth client ID or client secret for CIMD.

Do the following:

1. In Claude, open Settings.
2. In Connectors, click Add custom connector.
3. Enter a name for the custom connector, such as Qlik
   MCP.
4. For the Remote MCP server URL, enter https://<tenant-id>.<region>.qlikcloud.com/api/ai/mcp.
5. Under Advanced settings, select CIMD as the registration method.
6. Click Add.
7. Click Connect on your custom connector.
8. Sign in to your Qlik Cloud
   tenant.
9. Click Approve.

   Warning noteBy clicking Approve, you will
   enable the Qlik MCP server to
   share your Qlik Cloud data
   ("Content") with a third-party system (like an AI tool). That system is not
   managed by Qlik, and your
   Content will be stored, processed, and managed under the third party's
   control.
10. Test your connection by asking a question about a known application to which you have access.
