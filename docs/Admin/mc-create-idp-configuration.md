---
title: "Identity providers in Qlik Cloud"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-create-idp-configuration.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Deploying Qlik Cloud"]
---

# Identity providers in Qlik Cloud

An identity provider (IdP) is a service that manages user authentication and login information. In Qlik Cloud, you can use the default Qlik Account or integrate a custom IdP that supports OpenID Connect or SAML standards. This integration ensures secure authentication and consistent user identity across cloud deployments.

## Default identity provider: Qlik Account

The default IdP for Qlik Cloud is Qlik Account (not available with Qlik Cloud Government).

The key features include:

- Service account owner: The email address associated with the service account (the one that received the welcome email during tenant creation), is automatically added as a member of the tenant. For tenants created through My Qlik, the service account owner can log in immediately after the tenant is created.
- Authentication domains: Qlik Account provides authentication for qlik.com and qlikcloud.com.

## Using corporate identity providers

Information note

This functionality is not available in Qlik Sense Business.

You can integrate your own IdP with Qlik Cloud for authentication. Each Qlik Cloud tenant supports only one interactive IdP. Supported providers include:

- Microsoft Entra ID (formerly Azure AD)
- Okta
- Auth0
- Salesforce
- Google Identity (generic integration)
- OneLogin (generic integration)

When you switch to a corporate IdP, the Qlik Account login flow is replaced by the authentication process of your chosen provider.

## Benefits of using an IdP

Integrating an IdP into your Qlik Cloud deployment offers several benefits:

- Secure Authentication: Ensures that users' identities are verified securely.
- Unified user identity: Maintains consistent user IDs and group data across all deployments,
- Simplified licensing: Ensures one identity per user, preventing licensing conflicts and ensures that users are assigned the correct license.
- Access control: Enables consistent application of access controls based on user attributes, such as ID and group memberships.
- Single sign-on (SSO): Allows users to access multiple services with a single login, eliminating the need for separate credentials for each service.
- Cloud-based IdPs: Simplify authentication across online services. For organizations using Active Directory (AD), IdPs can integrate AD-stored accounts into cloud environments.

## Supported IdP standards

Qlik Cloud supports integration with IdPs using OpenID Connect (OIDC) and SAML standards. These integrations support:

- Interactive login: Users log in via a web browser.
- Automated login: API-based authentication for software products.

## Adding users to the tenant

Your subscription determines how users are added to your tenant:

- Identity provider integration: If your license includes IdP integration, the Identity provider pane will be available in the Administration activity center.
- Email invites: If IdP integration is not enabled, you can invite users manually through the Manage users section in the Administration activity center.

Information note

Your subscription allows only one method for adding users—either through an IdP or via email invites. If you switch from email invites to an IdP-based user management, the invite option will remain active until the IdP is fully set up and activated.

## Examples of IdP deployments

### IdP in a cloud deployment

In a Qlik Cloud deployment, the IdP ensures seamless user authentication and centralized management of user identities, attributes, and licenses.

IdP integration in a cloud deployment

![Qlik Sense Enterprise SaaS and Qlik Sense Enterprise on Kubernetes are integrated with an Identity Provider via OIDC. User IDs, email, groups, and jobs are integrated through Qlik Sense Enterprise on Windows via SAML. An Identity Provider authenticates users against their identity (user ID, Password, groups).](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/dr_multi-cloud-idp_V3.svg "Click to view full size")

### IdP in a multi-cloud deployment

In a multi-cloud setup, Qlik Sense Enterprise on Windows integrates with an IdP using the SAML standard or any other method that provides the IdP with a consistent user identity.

IdPs in this scenario must support both OIDC and SAML standards.

IdP integration in a multi-cloud deployment

![Qlik Sense Enterprise SaaS and Qlik Sense Enterprise on Kubernetes are integrated with an Identity Provider via OIDC. User IDs, email, groups, and jobs are integrated through Qlik Sense Enterprise on Windows via SAML. An Identity Provider authenticates users against their identity (user ID, Password, groups).](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/dr_multi-cloud-idp_V2.svg "Click to view full size")

For additional information on how to set up a multi-cloud deployment, see [Distributing applications to Qlik Cloud](/en-US/sense-admin/November2026/Subsystems/DeployAdministerQSE/Content/Sense_DeployAdminister/Multi-Cloud/distributing-apps-QSEoW-to-QCS.htm).

Related learning:

- [Integrating an external identity provider with Qlik Cloud](/lnk/Integrating_external_identity_provider_Cloud)
- [How do I customize an identity provider login?](/lnk/How_customize_identity_provider_login)
