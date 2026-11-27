---
title: "Configuring an interactive OIDC IdP"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-creating-oidc-idp.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Deploying Qlik Cloud", "Identity providers in Qlik Cloud", "Configuring an identity provider (IdP)"]
---

# Configuring an interactive OIDC IdP

This topic describes how to configure the identity provider settings in Qlik Cloud.

## Configuration on the identity provider side

In addition to the configuration in Qlik Cloud, you also need to make configurations on the identity provider side. For a walk-through of those configurations, refer to the following resources:

- [Using Salesforce.com as an IDP for Qlik Sense Enterprise SaaS (OIDC authentication)](/en-US/video/p2-a5D97y6U)
- [Using Active Directory Federation Services as an IDP for Qlik Sense Enterprise SaaS](/en-US/video/LeFqpb1pPpLJYsRX554QAr?)
- [How To: Configure Qlik Sense Enterprise SaaS to use Azure AD as an IdP](https://community.qlik.com/t5/Qlik-Sense-Documents-Videos/How-To-Configure-Qlik-Sense-Enterprise-SaaS-to-use-Azure-AD-as/ta-p/1704442)

## Configuration in Qlik Cloud

Tenant administrators can create new IdP configurations.

Information noteYou can only have one single interactive IdP at a time. If you already have an active one, you need to first deactivate it before you can activate the new one. For more information, see [*Changing corporate identity providers*](mc-change-corporate-idp.htm).

Do the following:

1. In the Administration activity center, go to Identity provider and click Create new.
2. For Type, select OIDC.
3. For Provider, select an identity provider from the list, or choose Generic if your specific provider is not listed.
4. Optionally, enter a description for the IdP configuration.
5. Under Application credentials, you can enter the discovery URL. If a discovery URL is not available or does not give proper metadata, you also have the option to manually enter individual values. Manual configuration should be used only when a discovery URL has not been entered.

   Do one of the following:

   1. Enter the discovery URL. This is the URL to the endpoint that provides configuration data for the OAuth clients to interface with the IdP using the OpenID Connect protocol. The naming conventions for the discovery URL vary based on your chosen provider:

      - ADFS: ADFS discovery URL
      - Auth0: OpenID configuration
      - Keycloak: Keycloak OpenID endpoint configuration
      - Okta or Generic IdP: OpenID Connect metadata URI
      - Salesforce: Salesforce discovery URL

   or

   1. Select Manual configuration.
   2. Enter the following values:

      - Authorization endpoint: The URL for interaction with the resource owner, where you get the authorization to access the resource.
      - End session endpoint (optional): The URL used to trigger a single sign-out.
      - Introspection endpoint (optional): The URL to validate reference tokens or JWTs.
      - Issuer: The URL to the identity provider.
      - JWKS URI: The URI to the JSON Web Key Set containing public keys used for verification of a JSON Web Token (JWT).
      - Token endpoint: The URL to get an access token.
      - User info endpoint (optional): The URL to get user information.

   Configuration using the discovery URL and manual configuration.

   ![Configuration panes shown with and without using discovery URL.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_idp_oidc_config_options.png "Click to view full size")
6. Enter the Client ID: The ID of the configured client at the IdP for interactive user authentication.
7. Enter the Client secret: The secret for the client configured at the IdP.
8. Optionally, enter a Realm. This is the name to associate with the IdP. It is the same as the domain name in Qlik Sense Enterprise on Windows and it is used for naming consistency in multi-cloud.
9. Fill in the fields under Claims mapping.

   Claims are statements (name/value pairs) about the entity (in many cases the user) and metadata about the OpenID Connect service. Mappings are available for sub, name, groups, email, client\_id, picture, and email\_verified (optional).

   Information note
   - You can enter multiple lookup values, separated by a comma, in the input fields. The first non-null value found will be used.
   - The groups claim is needed to receive groups. Note that nested groups are not supported in Microsoft Entra ID.
10. Optionally, configure the advanced options. For more details, see [*Advanced options*](#Advanced).
11. Click Create.

    A confirmation dialog appears with the option to validate the IdP configuration.

    - To validate now, select Validate IdP and click Create. This will initiate the validation process. Follow the steps in the validation wizard to perform a login and verify that the user profile data is correct.
    - If you prefer to create the configuration now but validate it later, clear the Validate IdP checkbox and click Create. You can validate later by clicking ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on your IdP configuration and selecting Validate.

    Validating and creating the IdP configuration.

    ![Confirmation dialog with Validate IdP option selected](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_idp_oidc_confirm_validation.png "Click to view full size")

## Adding your tenant URL to the identity provider allowlist

At your identity provider, add your tenant URL to the allowlist. There are different names for this setting, for example, Allowed Callback URLs, Redirect URI, or Login redirect URI.

When you add the URL, you need to append login/callback to your tenant address, as in https://<tenant name>/login/callback.

Information noteUse the original tenant hostname and not the alias hostname when setting the redirect URI. To find the tenant hostname, open your user profile menu and click About.

## Advanced options

The advanced options provide additional capabilities for certain identity providers.

### Email verified override

Enable this setting to always set the email\_verified claim to 'true'. This ensures that email addresses can be used for identity mapping in ADFS and Microsoft Entra ID. It is particularly useful when switching IdPs and helps distinguish between users with identical names in the Administration activity center.

### Scope

Scopes define the access privileges that are requested when issuing an access token, according to the OAuth 2.0 specification. Enter values separated by spaces to specify the permissions you want to request from the identity provider. For example, include a groups scope if the IdP requires it to support user group features.

### Post logout redirect URI

Use this field to specify a URI to which users will be redirected after logging out. For detailed instructions, see [*Using post logout redirect URI*](mc-idp-redirect.htm).

### Block offline\_access

When using Google Identity or OneLogin as the identity provider, enable this setting to block passing the offline\_access scope to the identity provider. This ensures that the configuration works correctly with Qlik Sense Mobile SaaS and OAuth 2.0 applications.

### ID token signature algorithm

The RSA signature algorithm ensures the authenticity and integrity of ID tokens. Qlik Cloud supports two options:

- RS256 (default)
- RS512

Select algorithm based on your security needs.

### Token signature verification and decryption

Generate key pairs to verify signatures and decrypt encrypted JSON Web Tokens (JWT). For detailed instructions, see [*Managing key pairs for signed and encrypted ID tokens (OIDC)*](mc-idp-token-decryption.htm).
