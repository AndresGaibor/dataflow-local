---
title: "Publishing OAuth clients and consent methods"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/oauth-publishing-and-consent.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Securing the system", "Creating and managing OAuth clients"]
---

# Publishing OAuth clients and consent methods

You can publish a OAuth client to share it with other tenants in the same region, so a third-party application can use the same client ID across tenants. The consent method controls whether users are prompted to approve access when they authenticate.

## Publishing OAuth clients

OAuth clients are initially bound to the tenant that created them. To allow other tenants in the same region to connect to a client, you must publish it.

Application owners can rotate secrets and update the configuration without interaction from a [tenant admin](#glossary-0 "Glossary term"). Tenant admins do not need to manage credentials or be aware of any configuration details for the published client.

To publish an OAuth client, do the following:

1. In the Administration activity center, go to OAuth.
2. Locate the OAuth client that you want to publish.
3. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to the client and select Publish.
4. Click Publish to confirm.

Once the OAuth client is published, it becomes available for external use by other tenants. When a user visits an external website that uses this OAuth client, they are prompted to enter their tenant hostname and user credentials, unless they already have an active SaaS session.

The first sign-in from another tenant requires approval from the tenant admin of that tenant. Once approved, the OAuth client appears in the Administration activity center of that tenant.

## Consent methods

By default, Qlik Cloud prompts users for consent when authenticating. To streamline the process for trusted applications, you can set the consent method to Trusted, which skips the consent prompt.

There are two consent methods:

- Required: The user is prompted for consent each time the OAuth client requests a new scope. This method ensures explicit user approval for each access level.
- Trusted: The user is not prompted for consent. This method is only available for unpublished clients. For published clients, the consent method is always Required to maintain security across multiple tenants.

For clients used as Machine-to-Machine (M2M), you must change the consent method to Trusted after you create the client. OAuth Client ID Metadata Documents (CIMD) connections always use Required consent. You cannot change them to Trusted, regardless of published status.

## Changing the consent method

To change the consent method for an OAuth client, do the following:

1. In the Administration activity center, go to OAuth.
2. On the OAuth client, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Change consent method.
3. Select Required or Trusted and then click Change consent method.
