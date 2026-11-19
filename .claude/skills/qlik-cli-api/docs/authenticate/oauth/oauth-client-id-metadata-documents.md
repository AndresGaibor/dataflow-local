---
source: https://qlik.dev/authenticate/oauth/oauth-client-id-metadata-documents/
last_updated: 2026-09-29T07:48:54Z
---

# OAuth Client ID Metadata Documents (CIMD)

OAuth Client ID Metadata Documents (CIMD) let an OAuth client use an HTTPS URL as its
`client_id`. The URL points to a document that describes the client, including information
such as its redirect URIs and authentication method.

When the client connects, Qlik Cloud retrieves the metadata document.
A tenant administrator must approve the client through the OAuth consent form before it can
be used on the tenant.

CIMD is defined by the IETF
[OAuth Client ID Metadata Document](https://datatracker.ietf.org/doc/draft-ietf-oauth-client-id-metadata-document/)
Internet-Draft.

> **Warning:** The CIMD specification is still an Internet-Draft and hasn't been finalized as an RFC.
> The specification may change as the draft evolves.

## When to use CIMD

Use CIMD when an OAuth client application supports CIMD and publishes a client ID metadata
document.

For Model Context Protocol (MCP) integrations that support both CIMD and
[Dynamic Client Registration (DCR)](https://qlik.dev/authenticate/oauth/oauth-dynamic-client-registration/),
use CIMD.

Unlike DCR, CIMD doesn't require DCR to be enabled on the tenant.

For applications that don't support CIMD, use another
[OAuth registration method](https://qlik.dev/authenticate/oauth/).

> **Note:** CIMD doesn't support the `client_credentials` grant type. For machine-to-machine
> authentication, use an [M2M OAuth client](https://qlik.dev/authenticate/oauth/create/create-oauth-client/)
> instead.

## Prerequisites

To connect using CIMD:

- The OAuth client must support CIMD.
- The client must publish its metadata document at the HTTPS URL used as its `client_id`.
- The metadata document must conform to the
  [OAuth Client ID Metadata Document](https://datatracker.ietf.org/doc/draft-ietf-oauth-client-id-metadata-document/)
  specification.
- A tenant administrator must approve the client the first time it connects to a tenant.

## How CIMD works with Qlik Cloud

A CIMD connection is initiated from the OAuth client application. A tenant administrator
doesn't create a CIMD client manually from the Qlik Cloud Administration activity center.
Instead, the administrator approves the client for the tenant when it first connects.

When a client connects:

1. The client starts the OAuth authorization flow using its client metadata document URL as
   the `client_id`.
2. Qlik Cloud retrieves and validates the metadata document.
3. The tenant administrator authenticates and approves the client.
4. Qlik Cloud creates the OAuth client connection for the tenant.

After approval, the client appears on the **OAuth** page in the Administration activity
center with **CIMD** as its source.

Other users on the tenant can then authorize access through the approved client when
their application uses the same CIMD document URL. Each user authenticates with their
own Qlik Cloud account and permissions.

### Client type

Qlik Cloud determines the OAuth client type from the token endpoint authentication method
specified in the client metadata document.

| Token endpoint authentication method | OAuth client type  |
| ------------------------------------ | ------------------ |
| `private_key_jwt`                    | Web (confidential) |
| `none`                               | Native (public)    |

### Default scopes

For Qlik MCP Server connections using CIMD, the following scopes are selected by default:

- `user_default`
- `mcp:execute`
- `offline_access`

A tenant administrator can add or remove OAuth scopes after the client is approved.

## Discover CIMD support

Qlik Cloud advertises its OAuth capabilities in the authorization server metadata document.

The document includes:

```json
{
  "client_id_metadata_document_supported": true
}
```

The authorization server metadata is available at:

```text
https://<tenant-hostname>/.well-known/oauth-authorization-server
```

OAuth clients that support CIMD publish their client metadata at the URL they use
as their `client_id`. Qlik Cloud retrieves this document to determine the client's
metadata and OAuth configuration.

For example:

- Claude: `https://claude.ai/oauth/mcp-oauth-client-metadata`
- Claude Code: `https://claude.ai/oauth/claude-code-client-metadata`
- ChatGPT: `https://chatgpt.com/oauth/client.json`

OAuth clients can use the Qlik Cloud authorization server metadata to discover supported OAuth
capabilities, including CIMD and token endpoint authentication methods.

## Manage CIMD clients

A tenant administrator can manage an approved CIMD client from the **OAuth** page in the
Administration activity center.

They can:

- Add or remove OAuth scopes assigned to the client.
- Remove the CIMD connection from the tenant.

Properties supplied by the client metadata document can't be changed in Qlik Cloud.
These include:

- Client name and description
- Redirect URIs
- Authentication method

CIMD clients use the **Required** consent method. A tenant administrator can't change the
consent method to **Trusted**.

## Identify CIMD clients using the API

CIMD clients have `createdByType` set to `cimd` in the
[OAuth clients API](https://qlik.dev/apis/rest/oauth-clients/).

For example, to list CIMD clients:

```bash
curl -X GET \
  'https://<tenant-hostname>/api/v1/oauth-clients?filter=createdByType eq "cimd"' \
  -H 'Authorization: Bearer <ACCESS_TOKEN>'
```

For more information about filtering and listing OAuth clients, see the
[OAuth clients API reference](https://qlik.dev/apis/rest/oauth-clients/).

## Related resources

- [OAuth overview](https://qlik.dev/authenticate/oauth/): OAuth client types and registration methods
- [OAuth dynamic client registration](https://qlik.dev/authenticate/oauth/oauth-dynamic-client-registration/):
  Register compatible OAuth clients using DCR
- [OAuth clients API](https://qlik.dev/apis/rest/oauth-clients/): List and manage OAuth clients
- [Connecting to the Qlik MCP server](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikMCP/Connecting-Qlik-MCP-server.htm):
  Configure supported Large Language Model (LLM) clients to connect to the Qlik MCP server
- [OAuth Client ID Metadata Document](https://datatracker.ietf.org/doc/draft-ietf-oauth-client-id-metadata-document/):
  IETF Internet-Draft defining CIMD
- [MCP authorization specification](https://modelcontextprotocol.io/specification/2026-07-28/basic/authorization):
  Model Context Protocol authorization guidance
