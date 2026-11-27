---
title: "Connecting to the Qlik MCP server"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikMCP/Connecting-Qlik-MCP-server.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik MCP server"]
---

# Connecting to the Qlik MCP server

Connect your MCP client to the Qlik MCP server.

## Prerequisites

To connect your MCP client to the Qlik MCP server, you need the following:

- The Qlik MCP permission set to Allowed. A tenant administrator grants this permission through the default permissions or a custom role.
- an MCP client that can connect to remote MCP servers, such as Claude or ChatGPT.
- The Qlik MCP server URL for your tenant: https://<tenant address>/api/ai/mcp.
- An OAuth client for your MCP client. Your tenant administrator creates the OAuth client or sets up registration with one of the supported methods. For more information, see [*Creating an OAuth client*](Administering-Qlik-MCP.htm#ConnectiAuth).
- For each MCP client, a tenant administrator must connect to the Qlik MCP server first. After that, other users can connect with the same MCP client.

## Connecting your MCP client

Follow the directions in the following topics to connect your MCP client to the Qlik MCP server:

- [*Connecting Claude to the Qlik MCP server*](connecting-claude-qlik-mcp.htm)
- [*Connecting ChatGPT to the Qlik MCP server*](connecting-chatgpt-qlik-mcp.htm)
- [*Connecting other MCP clients to the Qlik MCP server*](connecting-other-MCP-qlik-mcp.htm)

These steps provide general guidance for configuring connections in your own MCP
applications. Qlik does not own these
applications and cannot guarantee the accuracy of all steps. Steps are subject to change
by your application provider.

## Limitations

Qlik MCP server has the following
limitations:

- Authentication to the Qlik MCP server is governed by the OAuth client configuration and your identity provider (IdP) configuration:

  - If the OAuth client does not include the offline\_access scope, or your IdP does not issue refresh tokens, users must re-authenticate when the access token expires.
  - If the OAuth client includes the offline\_access scope and your IdP issues refresh tokens, an MCP client that supports refresh tokens can renew its access token without user interaction. Users must re-authenticate when the refresh token expires.

  Tenant administrators can change token durations for the OAuth client. For information about the default token durations and how to change them, see [*Configuring OAuth token duration*](../Admin/oauth-token-duration.htm). These settings do not extend user sessions.
