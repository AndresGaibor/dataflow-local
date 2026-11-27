---
title: "Creating and managing OAuth clients"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-create-oauth-client.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Securing the system"]
---

# Creating and managing OAuth clients

OAuth is a security protocol for authorization and delegation. It allows third-party applications to access API resources without disclosing end-user credentials. An OAuth client requests an authorization code, exchanges it for an access token, and uses the token to access content through APIs.

Tenant admins create and manage OAuth clients in the Administration activity center, on the OAuth page.

## About OAuth clients

An OAuth client is a web application or software that requests access to resources in Qlik Cloud on behalf of a user.

### OAuth client types

OAuth defines two client types, depending on whether the client can keep its credentials confidential. For details, see [RFC 6749 Section 2.1: OAuth 2.0 Client Types](https://oauth.net/2/client-types/ "RFC 6749 Section 2.1: OAuth 2.0 Client Types").

Public and confidential describe how the application authenticates itself. They do not describe whether user data is public or confidential, and users still sign in with their own accounts.

#### Confidential clients

Confidential clients can securely store a client ID and client secret, and use them to authenticate with the authorization server. They are typically traditional server-side web applications. Select Web when you create the client.

Example: A web application with a secure backend that calls APIs to manage user access or orchestrate data refresh tasks.

#### Public clients

Public clients cannot keep credentials confidential, so they do not use a client secret. These are native applications and frontend applications like single-page applications (SPA) with embedded analytics, or custom [visualization](#glossary-0 "Glossary term") extensions in Qlik Sense that require user authentication. Select Single-page app, Native, or Anonymous embed when you create the client.

### OAuth authorization flows

Qlik supports two authorization flows (grant types), one for each client type:

Authorization flows

| Flow | Client type | Typical use |
| --- | --- | --- |
| Authorization code | Confidential | Server-side applications |
| Authorization code with Proof Key for Code Exchange (PKCE) | Public | Native and single-page applications |

#### Authorization code flow

The application exchanges an authorization code for an access token, authenticating with the client secret. The application must be server-side, because the client secret is sent to the authorization server during the token exchange.

Information noteNever share your client secret publicly, as it compromises your tenant’s security. Keep it secure and private.

For more information, see the official OAuth 2.0 documentation: [Authorization Code Flow](https://auth0.com/docs/get-started/authentication-and-authorization-flow/authorization-code-flow "Authorization Code Flow").

#### Authorization code flow with PKCE

Native and single-page applications cannot securely store a client secret, because their source code can be decompiled or inspected in a browser. PKCE adds security by requiring a code verifier to obtain an access token.

For more information, see the official OAuth 2.0 documentation: [Authorization Code Flow with Proof Key for Code Exchange (PKCE)](https://auth0.com/docs/get-started/authentication-and-authorization-flow/authorization-code-flow-with-proof-key-for-code-exchange-pkce "Authorization Code Flow with Proof Key for Code Exchange (PKCE)").

### OAuth client setup methods

You can configure OAuth clients in the following ways:

- Manual client setup (static registration): You create and maintain the client definition in your tenant. Use this method for full control over client settings. This topic describes this method.
- Dynamic client registration (DCR): Compatible applications register clients dynamically, based on tenant-level DCR settings. See [*Configuring OAuth dynamic client registration*](oauth-dynamic-client-registration.htm).
- OAuth Client ID Metadata Documents (CIMD): Compatible applications use an HTTPS metadata-document URL as the client ID. The first connection requires tenant administrator approval. See [*Configuring OAuth Client ID Metadata Documents*](oauth-client-id-metadata-documents.htm).

## Creating OAuth clients

Each tenant supports up to 200 OAuth clients. Each client supports up to 5 redirect URLs, 5 allowed origins, and 5 client secrets.

To create an OAuth client manually, do the following:

1. In the Administration activity center, go to OAuth.
2. Click Create new.
3. Select a client type:

   - Web (confidential)
   - Single-page app, Native, or Anonymous embed (public)
4. Enter a name and, optionally, a description.
5. Select the permissions to grant. Browse the list or use the search field.

   For descriptions, see [*Available OAuth scopes*](oauth-scopes.htm#Availabl).

   Tip noteUse All and Changed to view all permissions or only the ones you have changed.
6. Enter one or more redirect URLs (maximum of 5) and click Add.

   The redirect URL is where the authorization server sends the user's browser after successfully authenticating and granting permission to the client application. Qlik Cloud redirects users back to your application after authorization only if the URL is on this list.

   Requirements:

   - URLs must start with https://, except for localhost, which can use http://.
   - Native applications can also use the application-specific link format, such as exampleapp://.
   - Example: https://www.exampleapp.com/oauth/callback, where /oauth/callback handles authentication callbacks from the OAuth provider.
7. Web and Single-page app only: Enter one or more allowed origins (maximum of 5).

   Qlik Cloud grants access only to applications whose origin is on this list.
8. Web only: Optionally, enable automated system access without user interaction:

   - Allow Machine-to-Machine (M2M): System-to-system communication without user involvement. After you create the client, change its consent method to Trusted. See [*Publishing OAuth clients and consent methods*](oauth-publishing-and-consent.htm).
   - Allow M2M user impersonation: Your application authenticates on behalf of users and acts as them.
9. Web only: Under Authentication method and token duration, select a method:

   - Client secret (default)
   - Private key JWT: A more secure option that authenticates with a public/private key pair instead of a shared secret.

     When you select Private key JWT, the Public key field appears. Enter your application's public key in JSON Web Key (JWK) format. The private key stays with your application to sign JWTs. See [Create a public/private key pair for signing JWTs](https://qlik.dev/authenticate/oauth/oauth-private-key-jwt-reference/ "Create a public/private key pair for signing JWTs") on the Qlik Developer Portal, and [*Managing client secrets*](oauth-client-secrets.htm).

     Information noteIf your key is another format, convert it to JWK using a third-party tool.
10. Web, Single-page app, and Native: Optionally set the Access token duration (in minutes) and the Refresh token duration (in hours). See [*Configuring OAuth token duration*](oauth-token-duration.htm).
11. Click Create.
12. Click Copy to clipboard to save the client ID and client secret, and store the client secret securely. Public clients do not have a client secret.
13. Click Done.

## Identifying how a client was registered

Some vendors dynamically register one OAuth client per user. Qlik recommends using OAuth Client ID Metadata Documents (CIMD) to reduce multiple registrations. For details, see [*Managing multiple registrations from vendors*](oauth-dynamic-client-registration.htm#ManagingVendors).

DCR and CIMD clients can be distinguished from manually created clients in the following ways:

OAuth client registration methods

| Registration method | Source column in Administration | createdByType in API |
| --- | --- | --- |
| Manual | User | user |
| DCR | DCR | dcr |
| CIMD | CIMD | cimd |

For CIMD clients, the client ID is the metadata document URL supplied by the client application.

Source (how the client was registered) is separate from client type (the OAuth model). For example, Claude appears as Native (public) and ChatGPT appears as Web (confidential).

## Publishing OAuth clients and consent methods

By default, an OAuth client is bound to the tenant that created it. You can publish a client to share it with other tenants in the same region, so a third-party application can use the same client ID across tenants. The first login from another tenant requires consent from that tenant's administrator.

The consent method controls whether users are prompted to approve access when they authenticate:

- Required (default): Users are prompted for consent whenever the client requests a new scope. Published clients and CIMD clients always use Required.
- Trusted: Users are not prompted for consent. This is available only for unpublished clients. Clients that use Machine-to-Machine (M2M) must be set to Trusted after they are created.

For details, see [*Publishing OAuth clients and consent methods*](oauth-publishing-and-consent.htm).

## Editing OAuth clients

You can rename an OAuth client, update the description, manage redirect URLs, or change token durations.

Token duration changes apply only to newly issued tokens. See [*Configuring OAuth token duration*](oauth-token-duration.htm).

Do the following:

1. In the Administration activity center, go to OAuth.
2. Locate the client, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), and select Edit.
3. Change the options as needed.
4. Click Save.

## Deleting OAuth clients

Delete an OAuth client when it is no longer needed or to revoke access.

Do the following:

1. In the Administration activity center, go to OAuth.
2. Select one or more clients and click Delete.
3. Confirm the deletion.

Tip note

To delete many clients at once, filter the list by vendor or naming pattern, select the matching clients, and delete them in bulk.

## Viewing and copying the OAuth configuration

In the OAuth section of the Administration activity center, select View OAuth configuration. It shows a code snippet with your tenant's OAuth endpoints and settings, as well as a URL that you can copy. Use it to integrate Qlik Cloud with third-party applications, automate API access, or configure authentication for embedded analytics.

## OAuth clients for specific use cases

- Building client applications: After registering an OAuth client, use its client ID and client secret in your application. The [OAuth Overview](https://qlik.dev/authenticate/oauth/) on the Qlik Developer Portal has tutorials for popular languages and an overview of OAuth use cases.
- Qlik add-ins for Microsoft Office: Set up an OAuth client for installation of the Qlik add-in for Microsoft Excel. See [*Creating OAuth clients for Qlik add-ins for Microsoft Office*](oauth-client-office-add-ins.htm).
- Anonymous embeds of application content: Create an OAuth client to enable anonymous access to embedded application content. See [*Creating an OAuth client for anonymous embeds of application content*](oauth-client-anonymous-embed.htm).
- Qlik for VS Code: A tenant admin must give OAuth consent. The client then appears automatically in the Administration activity center, and other users can log in through the extension. See [*Qlik for VS Code Tenant Admin approval (OAuth consent)*](../QlikCode/code-extension-install.htm#OAuthConsent).
- Organization-level OAuth clients: Service account owners can create clients that access tenant information across all tenants in a subscription. See [*Managing OAuth clients in My Qlik*](create-oauth-client-for-organization.htm).
