---
title: "Connecting other MCP clients to the Qlik MCP server"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikMCP/connecting-other-MCP-qlik-mcp.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik MCP server", "Connecting to the Qlik MCP server"]
---

# Connecting other MCP clients to the Qlik MCP server

Use these general guidelines to add the Qlik MCP server to an MCP client.
The specific steps depend on your MCP client.

You can connect other MCP clients to the Qlik MCP server. Use CIMD when the MCP client supports it. Otherwise, use DCR or manual setup, depending on the client and your tenant configuration. For CIMD, start the connection from the MCP client. A tenant administrator must approve the client the first time it connects. For DCR, a tenant administrator must enable DCR for the tenant before clients can register. For setup details, see [*Configuring OAuth Client ID Metadata Documents*](../Admin/oauth-client-id-metadata-documents.htm), [*Configuring OAuth dynamic client registration*](../Admin/oauth-dynamic-client-registration.htm), and [*Manually created OAuth client*](Administering-Qlik-MCP.htm#ManualOAuth). For developer guidance on metadata documents, see [OAuth Client ID Metadata Documents](https://qlik.dev/authenticate/oauth-client-id-metadata-documents/) on the Qlik Developer Portal.

Tip note

For some additional guidelines for connecting to other MCP clients, see [Connecting third party MCP clients to Qlik MCP server](https://community.qlik.com/t5/Official-Support-Articles/Connecting-third-party-MCP-clients-to-Qlik-MCP-server/ta-p/2552672).

Do the following:

1. In your MCP client, add a new remote connection.
2. For the URL, enter https://<tenant-id>.<region>.qlikcloud.com/api/ai/mcp.
3. If you use a manually created OAuth client or DCR, enter the client ID of the OAuth client.

   If you use CIMD, follow your MCP client's CIMD flow instead. You do not need to enter a client ID or client secret.
4. If the OAuth client is a Web client, also enter the client secret.
5. Create the connection.
6. Sign in to your Qlik Cloud
   tenant.
7. Click Approve.

   Warning noteBy clicking Approve, you will
   enable the Qlik MCP server
   to share your Qlik Cloud data
   ("Content") with a third-party system (like an AI tool). That system is not
   managed by Qlik, and your
   Content will be stored, processed, and managed under the third party’s
   control.
8. Test your connection by asking a question about a known application to which you have access.
