---
title: "Configuring an identity provider (IdP)"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-creating-idp.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Deploying Qlik Cloud", "Identity providers in Qlik Cloud"]
---

# Configuring an identity provider (IdP)

An identity provider (IdP) enables user authentication for logging in, accessing APIs, and managing multi-cloud deployments. As a tenant administrator, you can configure and manage IdPs in the Administration activity center.

## Configuring an interactive IdP for user login

Set up an interactive IdP to enable user login. Choose the authentication standard that your IdP supports:

- OpenID Connect (OIDC)
- Security Assertion Markup Language (SAML)

Information note

Each Qlik Cloud tenant can only have one active interactive IdP at a time. When you deploy your corporate IdP, it replaces the default Qlik Account login flow with the authentication process defined by your chosen IdP.

### Configuring an interactive OIDC IdP

Set up an OIDC identity provider for interactive login. For detailed steps, see [*Configuring an interactive OIDC IdP*](mc-creating-oidc-idp.htm).

### Configuring an interactive SAML IdP

Set up a SAML identity provider for interactive login. For detailed steps, see [*Configuring an interactive SAML IdP*](mc-creating-saml-idp.htm).

### Supported identity providers

Qlik Cloud supports multiple identity providers, including:

- Microsoft Entra ID (formerly Azure AD)
- Okta
- Auth0
- Other providers that support OIDC or SAML

### Handling SSO failures

SSO failure handling must be configured through your identity provider. Qlik Cloud does not support configuring a fallback redirect URL.

## Configuring an IdP for multi-cloud deployments

For seamless identity management across multi-cloud environments, configure a multi-cloud IdP with a local bearer token. For details on setting up a multi-cloud deployment, see [Distributing applications to Qlik Cloud](/en-US/sense-admin/November2026/Subsystems/DeployAdministerQSE/Content/Sense_DeployAdminister/Multi-Cloud/distributing-apps-QSEoW-to-QCS.htm).

## Configuring a JWT IdP

A JSON Web Token (JWT) IdP is designed for embedded use cases where an external, customer-provided portal manages authentication and logs users into Qlik Cloud in the background.

Information note

Use OAuth instead of JWT whenever possible. JWT authentication requires third-party cookie support, which some browsers and organizations disable by default.

For more information, see [Qlik Developer portal: Implement JWT Authorization](https://qlik.dev/authenticate/jwt/implement-jwt-authorization/).
