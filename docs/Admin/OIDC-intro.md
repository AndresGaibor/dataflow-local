---
title: "OpenID Connect for integration with identity providers"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/OIDC-intro.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Deploying Qlik Cloud", "Identity providers in Qlik Cloud"]
---

# OpenID Connect for integration with identity providers

OpenID Connect (OIDC) integrates Qlik Cloud with identity providers, adding a layer for user authentication on top of the OAuth 2.0 protocol. This enables secure single sign-on (SSO), allowing users to log in once and access multiple applications and websites without repeated authentication.

## OAuth 2.0 and OIDC

OAuth 2.0 is designed for authorization. It allows one application to grant another application access to its data or features using a secure token, rather than exposing user credentials. This token provides limited access, ensuring you only share information that you have agreed to share. You have the ability to withdraw the token at any time.

OAuth 2.0 does not include user identity information. OpenID Connect (OIDC) enhances this by introducing ID tokens, which contain user login details and profile information. These tokens allow different clients (web-based, mobile, JavaScript, and others) to verify user identity, based on authentication performed by an authorization server. Clients can also request basic profile information about the user.

For an introduction to OAuth and OIDC, watch the video: [An Illustrated Guide to OAuth and OpenID Connect](https://www.youtube.com/watch?v=t18YB3xDfXI).

## ID tokens

ID tokens, used in OpenID Connect (OIDC), handle user authentication and include detailed user information such as identity and profile details. These tokens are typically formatted as JSON Web Tokens (JWT), which support various signature and encryption algorithms.

ID tokens contain claims—pieces of data about the user, such as their ID, name, login time, and indications of tampering. Claims in ID tokens provide the application with necessary details to verify the user's identity and facilitate single sign-on (SSO). The OIDC specification defines a standard set of claims, including name, email, gender, and birth date. Custom claims can be added to include additional user information as needed. Issued by the authorization server after successful user authentication, ID tokens are obtained through OAuth 2.0 flows and are applicable to both web and mobile applications.

To protect sensitive data, such as Personally Identifiable Information (PII), you can use encrypted ID tokens. Encryption helps prevent unauthorized access and ensures privacy and security.

## Access tokens

Access tokens are used in OAuth 2.0 for authorization. They allow an application to access specific data or features on behalf of the user. An access token can be formatted as a JSON Web Token (JWT) or a non-JWT token. It serves as a credential that informs the API of the user's consent and the permissions granted. Unlike ID tokens, access tokens do not include user identity information; they simply grant access to specified resources.

## OpenID Connect specification

The OpenID Connect 1.0 specification consists of several documents that define its core functionality and optional features. Qlik supports this specification but may not support all vendor-specific implementations. However, Qlik may provide convenience configurations for popular identity management platforms.

Key documents in the specification include:

- OpenID Connect Core: Defines core OIDC functionality, including authentication built on OAuth 2.0 and the use of claims to share user information.
- OpenID Connect Discovery (Optional): Defines how clients dynamically discover information about OpenID providers.
- OpenID Connect Dynamic Client Registration (Optional): Defines how clients dynamically register with OpenID providers.
- OAuth 2.0 Multiple Response Types: Defines specific new OAuth 2.0 response types.
- OAuth 2.0 Form Post Response Mode (Optional): Defines how to return OAuth 2.0 Authorization Response parameters using HTML form values that are auto-submitted via HTTP POST.
- OpenID Connect Session Management (Optional): Defines how to manage OIDC sessions, including postMessage-based logout and RP-initiated logout functionality.
- OpenID Connect Front-Channel Logout (Optional): Defines a logout mechanism that does not use an OP iframe on RP pages.
- OpenID Connect Back-Channel Logout (Optional): Defines a logout mechanism using direct back-channel communication between the OP and RPs being logged out.
- OpenID Connect Federation (Optional): Defines how sets of OPs and RPs can establish trust by utilizing a Federation Operator.

To access these documents, visit [Welcome to OpenID Connect](https://openid.net/connect/ "Welcome to OpenID Connect").
