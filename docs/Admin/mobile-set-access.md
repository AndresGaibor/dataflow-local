---
title: "Setting access to the Qlik Analytics mobile app"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mobile-set-access.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Configuring features and integrations"]
---

# Setting access to the Qlik Analytics mobile app

The Qlik Analytics mobile app is used to access your Qlik Cloud tenant. If you are looking for the Qlik Cloud mobile app, search your app store for Qlik Analytics.

As a tenant administrator, you can set access to the Qlik Analytics mobile app in two ways:

- Setting individual user permissions by using default permissions and custom roles (see [*Setting permissions for the Qlik Analytics mobile app*](#NativeMobileApp)).
- Enabling or disabling offline usage for all users (see [*Enabling or disabling offline usage*](#Enabling)).

Tip note

**Tips for non-administrator users**

If you cannot access the app, ask your tenant administrator to check the Native mobile app permission assigned to you.

Your administrator can determine whether Allowed or Allowed with Intune applies under your organization's policy.

## Setting permissions for the Qlik Analytics mobile app

[Tenant administrators](#glossary-0 "Glossary term") configure permissions to control whether users have full, partial, or no access to the Qlik Analytics mobile app. If a user is granted access to the mobile app, their access to specific applications on mobile devices is further defined by their space access.

The Native mobile app permission controls whether a user has full or no access to the tenant through the Qlik Analytics mobile app. The Native mobile app permission is used in conjunction with space roles to control user access to mobile functionality.

The Native mobile app permission can be configured in the default permissions that apply to all users in the tenant, or in custom security roles. To learn how to assign permissions by using default permissions and custom roles, see:

- [*Roles and permissions for users and administrators*](permissions-admins-users-capacity-model.htm) (capacity-based subscriptions)
- [*Roles and permissions for users and administrators*](permissions-admins-users.htm) (user-based subscriptions)

For information about the permissions available through default permissions and custom roles, see:

- [*Default permissions and custom roles*](permissions-scopes-capacity-model.htm) (capacity-based subscriptions)
- [*Default permissions and custom roles*](permissions-scopes.htm) (user-based subscriptions)
- [*Default permissions and custom roles*](permissions-scopes-anonymous.htm) (Qlik Anonymous Accesssubscriptions)

### Mobile access permissions

You configure mobile access permissions in the Administration activity center > Manage users > Permissions. Click Manage default permissions or open a custom role, expand Features and actions, and locate Mobile > Native mobile app.

The Native mobile app permission can be set to one of the following options:

Mobile access permissions

| Option | Behavior |
| --- | --- |
| Allowed | Standard mobile access. No Intune enrollment is required. Use this for tenants and user groups where MAM enforcement is not required. |
| Allowed with Intune | Mobile access with mandatory Intune enrollment. The Qlik Analytics mobile app initiates Microsoft Intune enrollment as part of the sign-in flow, and access to tenant content is granted only after enrollment is confirmed. Use for all users in Intune-governed tenants. A future release will add corresponding server-side enforcement for additional defense in depth.  Users assigned Allowed with Intune do not also need Allowed. Allowed with Intune already includes permission for mobile access.  For full details about configuring the Qlik Analytics mobile app with Microsoft Intune, see [*Securing and configuring the Qlik Analytics mobile app with Microsoft Intune*](configure-mobile-app.htm). |
| Not allowed | Mobile app access denied. |

### Removing mobile permissions

When a tenant admin changes a user's Native mobile app permission from Allowed to Not allowed, the user does not lose permission to access the tenant through the mobile app until one of the following occurs:

- The user's mobile session ends.
- The user logs out of the mobile app.
- A tenant admin revokes the user's mobile access in the Manage users section of Administration activity center. Select the user, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), and select Revoke mobile devices.

  Information noteAfter Revoke mobile devices is applied, applications downloaded for offline use are no longer accessible to the user. The offline data is retained on the device, and if the user is later granted the Allowed permission again, those offline applications become accessible again without needing to re-download.

## Enabling or disabling offline usage

Offline usage allows users to download applications in [personal](#glossary-1 "Glossary term"), [shared](#glossary-2 "Glossary term") or [managed spaces](#glossary-3 "Glossary term") to their mobile devices and use them without an internet connection. As a tenant admin, you can enable or disable offline usage for all users in the [tenant](#glossary-4 "Glossary term").

Do the following:

1. In the Administration activity center, go to the Settings page.
2. Select the Feature control tab.
3. In the Mobile section, turn the Enable offline usage toggle on or off.

Information noteDisabling offline usage only applies to applications in shared or managed spaces. Users can always download applications from personal spaces.
