---
title: "Securing and configuring the Qlik Analytics mobile app with Microsoft Intune"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/configure-mobile-app.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Configuring features and integrations"]
---

# Securing and configuring the Qlik Analytics mobile app with Microsoft Intune

The Qlik Analytics mobile app gives field teams secure access to Qlik Cloud analytics on their mobile devices. You can use Microsoft Intune and Microsoft Entra ID to control access, protect company data, and provide the settings users need to connect to your Qlik Cloud tenant.

This topic covers how to configure Intune app protection policies, app configuration policies, and Qlik Cloud access controls to manage and secure the Qlik Analytics mobile app on Android and iOS devices.

## About the Microsoft Intune integration

- Qlik has integrated Microsoft's standard Intune and Microsoft Authentication Library (MSAL) SDKs in accordance with Microsoft's developer guidance.
- Microsoft Entra ID, Microsoft Intune, and related SDKs are Microsoft products.
- Qlik, including Qlik Support, cannot provide guidance on configuring your Entra or Intune deployment, or on mobile device settings for devices running the Qlik Analytics mobile app.
- Refer to the [Microsoft Intune documentation](https://learn.microsoft.com/en-us/intune/intune-service/apps/app-management) or contact Microsoft Intune support for guidance on mobile device management (MDM) or mobile application management (MAM).

Information noteThe Microsoft Tunnel for Mobile Application Management SDK is not integrated in the Qlik Analytics mobile app.

## What you need before you start

Before configuring the Qlik Analytics mobile app in Intune, make sure you have the following:

- Qlik Cloud tenant using Microsoft Entra ID as the primary identity provider

  Enforcement of Intune MAM requires that your Qlik Cloud tenant is configured to use Entra ID directly as the identity provider through OIDC. For more information, see [*Identity providers in Qlik Cloud*](mc-create-idp-configuration.htm).

  Information noteTenants using a non-Entra identity provider (such as Okta, Auth0, SAML, or Qlik Account) do not support enforcement of Intune MAM. Tenants that federate a non-Entra identity provider into Microsoft Entra ID are not supported in this release. See [*Identity provider compatibility*](#IDP).
- Microsoft Entra ID integrated with Microsoft Intune

  Your organization must have Entra connected with Intune so you can enforce device and app policies.
- Users registered in Microsoft Entra ID

  All users who will access the Qlik Analytics mobile app must have accounts in your Entra ID tenant and be included in the user directory used for Qlik Cloud tenant access.
- Qlik Cloud tenant admin permissions

  You need tenant admin access in Qlik Cloud to assign mobile access controls to users and groups. See [*Configuring mobile access with MAM in Qlik Cloud*](#Configur2).

## Installing the Qlik Analytics mobile app

The Qlik Analytics mobile app is available in the iOS App Store and Google Play Store. For more information, see [*Get started with the Qlik Analytics mobile app*](../Mobile/qsmsaas-get-started.htm).

Information noteDepending on platform and deployment, Microsoft Company Portal and/or Microsoft Authenticator may be required on the device. On Android, Company Portal is required for MAM without device enrollment (MAM-WE) scenarios.

## Setting up Microsoft Intune for the Qlik Analytics mobile app in Microsoft Entra ID

This section outlines the main steps to register and manage the Qlik Analytics mobile app in Entra ID and Intune. Configure Entra ID and Intune according to your organization's requirements. For detailed instructions on application registration, see the [Microsoft Intune documentation](https://learn.microsoft.com/en-us/intune/intune-service/apps/app-management).

### Registering the Qlik Analytics app in Microsoft Entra ID

Register the Qlik Analytics mobile app in Microsoft Entra ID to use it with Microsoft Intune.

Do the following:

1. In Entra ID, go to App registrations and select New registration.
2. Select the link to Enterprise applications, since you are integrating a globally registered application.
3. Search for the application ID: 53dfc2c0-8711-4bb3-a48f-b384ff663ab9. This is the Qlik global app registration.
4. If required, the Intune administrator can initiate registration by signing in and visiting:

   https://login.microsoftonline.com/common/adminconsent?client\_id=53dfc2c0-8711-4bb3-a48f-b384ff663ab9
5. Once the Qlik Analytics mobile app is added and appears under Enterprise applications, complete the following:

   - Assign users and groups if you want to limit who can access the app.
   - Under Permissions, grant admin consent for your domain.

### Conditional Access policy guidance

The Qlik Analytics mobile app is globally registered in Microsoft Entra ID with application ID 53dfc2c0-8711-4bb3-a48f-b384ff663ab9. This registration appears as a cloud application in your tenant. Any Conditional Access policy scoped to All cloud apps applies to this app registration.

#### Conditional Access and authentication flow

The Allowed with Intune authentication flow includes two sign-in steps:

1. App authentication (MSAL sign-in)

   The Qlik Analytics mobile app uses MSAL to authenticate the user with Entra. Intune MAM policies are evaluated during this step.
2. Browser-based Qlik Cloud sign-in

   The app opens an external browser on the device to complete Qlik Cloud authentication. For Intune flows, Microsoft Edge is enforced.

In this second step, Entra evaluates the browser—not the Qlik Analytics mobile app—as the client application when applying Conditional Access policies for the app registration. Any grant control applied to the app registration must be supported by the browser used in this step.

#### Conditional Access scope considerations

Because the Qlik Analytics app registration is visible as a cloud application in your tenant, Conditional Access policies scoped to All cloud apps also apply to the browser sign-in step.

If a policy uses Require app protection policy as the grant control, the browser used in the Qlik sign-in step must satisfy this requirement independently. This requires Microsoft Edge to have an Intune app protection policy deployed for your users. If Edge is not covered by an app protection policy, the browser sign-in step may be blocked.

#### Before deployment

Before deploying the Qlik Analytics mobile app with Intune MAM enforcement, verify with your Microsoft Entra or Intune administrator how your existing Conditional Access policies apply to the browser used in the Qlik sign-in step.

Qlik does not provide guidance on configuring Entra Conditional Access policies or broader Intune deployment configurations. For guidance, see [Learn about Conditional Access and Intune](https://learn.microsoft.com/en-us/intune/intune-service/protect/conditional-access) in the Microsoft documentation.

### How MAM enforcement works for the Qlik Analytics mobile app

When a user is assigned Allowed with Intune access, the Qlik Analytics mobile app initiates Microsoft Intune enrollment as part of the sign-in flow. The app verifies enrollment status before granting access to tenant content. If the device is not properly enrolled or does not meet Intune requirements, access is denied at the app level.

This enforcement is performed in the mobile app and is part of a phased delivery. A future release will add corresponding server-side enforcement at the Qlik Cloud authentication layer for additional defense in depth.

## Configuring mobile access with MAM in Qlik Cloud

Intune (MAM) enforcement is controlled by the mobile access permission assigned to users and groups in the Qlik Cloud Administration activity center. This is the main configuration step on the Qlik side and must be completed alongside your Intune and Entra configuration.

### Mobile access permissions

You configure mobile access permissions in the Administration activity center > Manage users > Permissions.

Click Manage default permissions or open a custom role, expand Features and actions, and locate Mobile > Native mobile app.

For more information about the permission settings, see [*Setting access to the Qlik Analytics mobile app*](mobile-set-access.htm).

### Permission assignment guidance for Intune-governed tenants

For tenants that use Intune app protection, assign Allowed with Intune to all users and groups that require mobile access, regardless of device management state.

#### Why Allowed is not sufficient for Intune-governed users

The mobile access permission applies to the user, not the device. If a user is assigned Allowed on their corporate, MDM-enrolled device, they carry the same access permission when they sign in on a personal, unmanaged device.

That personal device has no MDM enrollment and no Intune broker. With the user's access permission set to Allowed, the Qlik Analyticsmobile app does not require Intune enrollment, and access is granted without app protection policies being applied. The user can access the tenant from an unmanaged device with no Intune protection, bypassing your organization's Intune policies.

#### Recommended assignment pattern for Intune-governed tenants

Assignment pattern

| Assignment | Permission | Reason |
| --- | --- | --- |
| Default permission setting | Not allowed | No mobile access by default |
| MDM-enrolled users | Allowed with Intune | On enrolled devices, enrollment completes silently or near-silently. No meaningful friction is added. The same user on a personal device must complete enrollment before access is granted. |
| BYOD users | Allowed with Intune | Full enrollment requirement on unmanaged devices. |

Use Allowed only for tenants or groups where Intune app protection is not required, such as internal non-Intune tenants or specific service accounts.

### Identity provider compatibility

Enforcement of Intune MAM requires Microsoft Entra ID as the identity provider (IdP) for your Qlik Cloud tenant. The following table summarizes mobile app support across identity provider configurations.

IdP compatibility

| Identity provider | Standard mobile access (Allowed) | Intune enforcement (Allowed with Intune) |
| --- | --- | --- |
| Microsoft Entra ID | Supported | Supported |
| Okta (no Entra federation) | Supported | Not supported — do not assign Allowed with Intune |
| Auth0 (no Entra federation) | Supported | Not supported — do not assign Allowed with Intune |
| SAML / ADFS (no Entra federation) | Supported | Not supported — do not assign Allowed with Intune |
| Qlik Account | Supported | Not supported — do not assign Allowed with Intune |
| Generic OIDC | Supported | Not supported — do not assign Allowed with Intune |
| Federated IdP scenarios (any non-Entra IdP federated into Entra ID) | Supported | Not supported in this release |

Information noteFederated IdP scenarios: Customers who federate Okta, Auth0, SAML, or ADFS into Microsoft Entra ID are not supported for Intune MAM enforcement in this release. Assigning Allowed with Intune to users on a federated IdP tenant will result in authentication failures. Support for federated IdP scenarios is planned for a future release.

## Setting up app protection policies

The Qlik Analytics mobile app supports the following Intune policy features:

- Requiring users to log in with company credentials (Microsoft Entra ID).
- Enforcing a PIN to access the app.
- Restricting copy, paste, and download actions within the app.
- Blocking or controlling screenshots.
- Preloading Qlik Cloud tenant settings using app configuration policies.

### Important considerations

App protection policies control which apps can share data with each other.

- If users need to send diagnostic emails from the Qlik Analytics mobile app, the policy must allow data transfer between apps.
- The Qlik Analytics mobile app requires access to the device browser to complete sign-in. Your app protection policy must permit this.
- Key Intune app policy settings to review:

  - Data protection > Send org data to other apps
  - Data protection > Select apps to exempt (com.qlik.qsm)
  - Functionality > Restrict web content transfer with other apps—when configured to open URLs in Microsoft Edge, the Qlik Cloud sign-in page is opened in Edge. Edge then performs its own Microsoft authentication before rendering the page. If your Conditional Access policies apply a grant control to All cloud apps or to your IdP app registration, that grant control is evaluated against Edge at this point. See [*Conditional Access policy guidance*](#Conditio) for the implications of different grant controls at that evaluation point.
- Cold Start and MAM App Protection Policies — On initial installation, the Qlik Analytics mobile app is in an unmanaged state (no Intune App Protection Policy applied) until it has been launched and policy has been assigned and applied. If Microsoft Edge is configured with a MAM policy that restricts the authentication browser session to only interact with policy-managed apps, the authentication flow may be blocked, as the app has not yet registered as a managed app with the Intune service. Administrators may need to either exempt the Qlik Analytics app from this restriction or ensure App Protection Policy assignment is completed before the user's first launch.

## Setting up app configuration policies

Use app configuration policies in Intune to provide the Qlik Analytics mobile app with the settings it needs to connect to your Qlik Cloud tenant.

The following examples show how to configure key-value pairs for the mobile app in Intune. Replace placeholders (<policy name>, <tenant name>, <tenant URL>) with your own values.

### Managed devices (iOS)

App configurations > Policy name > Properties > Settings:

- Device enrollment type: Managed devices
- Platform: iOS

Key-value pairs:

Key: mdm

Value:

```
{
  "policyName": "<policy name>",
  "Accounts": [
    {
      "name": "<tenant name>",
      "url": "<tenant URL>"
    },
    {
      "name": "<tenant name>",
      "url": "<tenant URL>"
    }
  ]
}
```

Accounts defines one or more Qlik Cloud tenants that the app can connect to.

- name: Your chosen tenant name shown to users.
- url: The URL of the Qlik Cloud tenant (for example, mobileintune.us.qlikcloud.com).

Key: IntuneMAMOID

Value: {{userid}}

Passes the Intune user ID to the app.

OR

- Device enrollment type: Managed devices
- Platform: Android

Key-value pairs:

Key: mdm

Value:

```
{
  "policyName": "<policy name>",
  "Accounts": [
    {
      "name": "<tenant name>",
      "url": "<tenant URL>"
    },
    {
      "name": "<tenant name>",
      "url": "<tenant URL>"
    }
  ]
}
```

Accounts defines one or more Qlik Cloud tenants that the app can connect to.

- name: Your chosen tenant name shown to users.
- url: The URL of the Qlik Cloud tenant (for example, mobileintune.us.qlikcloud.com).

### Managed apps (multiple platforms)

App configurations > Policy name > Properties > Settings:

- Device enrollment type: Managed apps
- Platform: iOS

Key-value pair:

Key: mdm

Value:

```
{
  "policyName": "<policy name>",
  "Accounts": [
    {
      "name": "<tenant name>",
      "url": "<tenant URL>"
    },
    {
      "name": "<tenant name>",
      "url": "<tenant URL>"
    }
  ]
}
```

This JSON performs the same function as in the managed device scenario, defining the available tenant connections for authentication to your Qlik Cloud environment. In this scenario, only the mdm key is required. No user ID mapping is needed.

## Policy information in the app

The About screen in the Qlik Analytics mobile app settings shows whether a policy is applied to the app.

- When any policy is deployed (app protection or app configuration), the screen displays Policy Applied — Yes.
- If the policy has a policy name configured, it also appears on a separate row as the Policy Name.
