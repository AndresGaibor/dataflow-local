---
title: "Configuring OAuth Client ID Metadata Documents"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/oauth-client-id-metadata-documents.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Securing the system", "Creating and managing OAuth clients"]
---

# Configuring OAuth Client ID Metadata Documents

OAuth Client ID Metadata Documents (CIMD) let compatible client applications use an HTTPS metadata-document URL as the OAuth client ID. Qlik Cloud retrieves the client metadata from that URL when the client connects.

CIMD is the preferred registration method when a client supports both CIMD and OAuth Dynamic Client Registration (DCR). CIMD does not require DCR to be enabled in the tenant, and the client application supplies its own metadata document.

## Prerequisites and limitations

Prerequisites:

- You are a tenant administrator in Qlik Cloud.
- Your client application supports CIMD.

CIMD has the following limitations:

- CIMD supports the none and private\_key\_jwt client authentication methods. It does not support client\_secret.
- CIMD clients always use Required consent. You cannot change the consent method to Trusted, regardless of publishing status.
- CIMD does not support Machine-to-Machine (M2M) or service-to-service connections. For M2M integrations, use a manually created Web OAuth client.

## Connecting with CIMD

Start the connection in the CIMD-capable client application. The client supplies its metadata-document URL, and Qlik Cloud retrieves the metadata from that URL.

The first connection requires approval from a tenant administrator. The connection is then approved for the tenant, and subsequent users can authenticate with the same approved client identity when they use an application that references the same CIMD document URL. Each user still authenticates with their own Qlik Cloud account, roles, and permissions. A provider can use different metadata-document URLs for different applications.

The initial default scopes for a CIMD connection are user\_default, mcp:execute, and offline\_access. A tenant administrator can edit the allowed scopes after approval. If you remove all scopes from a CIMD connection, the connection has no access. It does not fall back to the initial default scopes.

For provider-specific connection procedures, see [*Connecting to the Qlik MCP server*](../QlikMCP/Connecting-Qlik-MCP-server.htm).

## Managing CIMD connections

After approving a CIMD connection, you can change its access and refresh token durations for your tenant. See [*Configuring OAuth token duration*](oauth-token-duration.htm).

Switching an existing DCR connection to CIMD is not an in-place upgrade. Disconnect the existing connection in the client application, and then reconnect using CIMD to create a separate CIMD connection. A tenant administrator must manually delete the old DCR client from the OAuth clients list. Until then, both client records exist.

Deleting a CIMD connection removes your tenant's connection configuration and revokes tokens for that client in your tenant. The shared CIMD client used by other tenants is not deleted.

Qlik Cloud fetches and verifies the CIMD metadata document every 24 hours and updates the stored metadata only if the document has changed.

This registration method is based on an evolving OAuth standard, so setup details in your client application may change over time.

For information about the metadata-document schema and protocol, see [OAuth Client ID Metadata Documents](https://qlik.dev/authenticate/oauth/oauth-client-id-metadata-documents/) on the Qlik Developer Portal.

## Identifying CIMD clients

In the Administration activity center, the OAuth clients list identifies CIMD clients with a Source value of CIMD. For API details about the createdByType value and the difference between Source and Client type, see [*Managing multiple registrations from vendors*](oauth-dynamic-client-registration.htm#ManagingVendors).
