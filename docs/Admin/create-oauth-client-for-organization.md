---
title: "Managing OAuth clients in My Qlik"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/create-oauth-client-for-organization.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing your Qlik Cloud subscription"]
---

# Managing OAuth clients in My Qlik

OAuth is a security protocol for authorization and delegation. It allows third-party applications to access API resources without exposing end-user credentials. An OAuth client requests an authorization code, exchanges it for an access token, and uses the token to access content through APIs.

## About OAuth clients in Qlik Cloud

OAuth clients in Qlik Cloud are configured at different levels depending on how they are used:

- Organization-level OAuth clients

  - Apply to all tenants across multiple subscriptions and regions.
  - Can access Qlik Cloud tenant APIs and perform tenant management tasks.
  - Managed by the service account owner (SAO) in My Qlik.
- Region-level OAuth clients (deprecated)

  - Apply to a specific license number in a region.
  - Managed by the SAO in My Qlik.

  Information noteRegion-level OAuth clients are deprecated and will be removed on or after January 31, 2027. Until this date, existing region-level OAuth clients will remain available. Create organization-level OAuth clients instead.
- Tenant-specific OAuth clients

  - Apply to a single tenant.
  - Managed by tenant administrators in the tenant's Administration activity center.
  - For details, see [*Creating and managing OAuth clients*](mc-create-oauth-client.htm).

## Creating and managing organization-level OAuth clients

Govnote-not-inNot supported in Qlik Cloud Government.

Govnote-not-inNot supported in Qlik Cloud Government - DoD.

You can create and manage organization-level OAuth clients on the OAuth clients page in My Qlik. These clients can access Qlik Cloud tenant APIs and support tenant-management operations across your subscriptions and regions.

### Accessing the OAuth clients page

Do the following:

1. Log in to My Qlik with your service account owner (SAO) credentials.
2. Click List all my tenants at the top of the page.
3. In the left pane, click OAuth.
4. The OAuth clients page opens, where you can create and manage OAuth clients for your organization.

The OAuth clients page.

![Screenshot of the Manage OAuth clients page.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_organization_OAuth_client.png "Click to view full size")

### Finding and viewing OAuth clients

On the OAuth clients page, you can:

- Search by name.
- Filter by region, status, or subscription ID.
- Sort by name, creation or last updated date, or client ID.
- Drag columns to reorder.

### Creating OAuth clients

Do the following:

1. On the OAuth clients page, click Create.
2. Enter a name for the OAuth client.
3. Optionally, add a description.
4. Click Create. A client ID and client secret are displayed.
5. Click ![Copy](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_copy.svg) to copy the client ID.
6. Click Copy secret to copy the client secret.

   Information noteYou will not be able to access the client secret later. Treat it like a password and do not expose it in source code or repositories.
7. Click Close.

After creating the client, you can use the client ID in your applications. You can retrieve it later from the context menu (![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg)) for the OAuth client.

### Editing OAuth clients

Do the following:

1. On the OAuth clients page, locate the OAuth client.
2. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Rename.
3. Modify the name or description as needed.
4. Click Save changes.

### Deleting OAuth clients

You can delete an OAuth client when it is no longer needed or to revoke access.

Do the following:

1. On the OAuth clients page, locate the OAuth client.
2. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Delete.
3. Confirm the deletion.

## Managing client secrets

If a client secret is compromised or your security policy requires periodic updates, you can add or remove secrets. To avoid downtime, you can add multiple client secrets (maximum 5), update your client application, and then remove the old secret.

### Adding a client secret

Do the following:

1. On the OAuth clients page, locate the OAuth client.
2. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Manage secrets.
3. Click Generate a new client secret.
4. Copy the client secret and client ID, and store them securely.

   Information noteYou will not be able to access the client secret later.
5. Click Close.

### Removing a client secret

Do the following:

1. On the OAuth clients page, locate the OAuth client.
2. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Manage secrets.
3. Click ![Delete](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg) next to the client secret you want to remove.
4. Click Close.

## Region-level OAuth clients (deprecated)

Information noteRegion-level OAuth clients are deprecated and will be removed on or after January 31, 2027. Until this date, existing region-level OAuth clients will remain available. Create organization-level OAuth clients instead.

To access region-level OAuth clients:

1. Log in to My Qlik with your service account owner (SAO) credentials.
2. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to My tenants and select Manage OAuth clients.
3. In the dialog, you can

   - View existing clients
   - Regenerate client secrets
   - Delete clients

## Next steps: Building OAuth client applications

After registering an OAuth client with Qlik Cloud, you can build OAuth client applications to access Qlik Cloud content. Use the client ID and client secret associated with your OAuth client. You can retrieve the client ID anytime from the context menu (![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg)) for the OAuth client.

Follow tutorials in the [OAuth Overview](https://qlik.dev/authenticate/oauth/) section of the Qlik Developer Portal. These tutorials cover how to build client applications using popular programming languages.
