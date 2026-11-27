---
title: "OAuth scopes reference"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/oauth-scopes.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Securing the system", "Creating and managing OAuth clients"]
---

# OAuth scopes reference

Use this reference to find the OAuth scopes that are available in Qlik Cloud and the permissions that each scope grants to OAuth client applications.

OAuth scopes define the level of access granted to OAuth client applications. For example, an access token can allow full access to resources or restrict it to read-only access. In Qlik Cloud,
scopes control client access to available functionality and resources. Without scopes, clients cannot access any resources.

Information note

API credentials provide direct programmatic access to Qlik Cloud and are not limited to workflows available in the user interface. Assign roles and OAuth scopes using the principle of least privilege. Treat service accounts and API credentials with the same level of care as administrator credentials. For more information, see [API access control and trust boundaries](https://qlik.dev/manage/access-control/api-trust-boundaries/).

## Choosing scopes

Grant only the scopes that the client application needs. Scopes are evaluated together with the user's roles, so a scope grants access only within what the user's roles allow. Start with the narrowest scopes, such as the :read variants, and add scopes only when the application requires them.

## Available OAuth scopes

The table lists available scopes and their associated permissions:

Available scopes and associated permissions

| Scope | Permission |
| --- | --- |
| user\_default | Full access to your account and content |
| admin\_classic | Full administrator access to your tenant  See also: [*Deploying and administering Qlik Cloud*](../Introduction/qlik-sense-administration.htm)  Information noteNot supported with the Single-page app or Native client types. |
| admin.apps | Read and manage all applications in the tenant.  See also: [*Managing applications*](../Apps/manage-apps.htm) |
| Indicates a child item admin.apps:export | Export all applications in the tenant  See also: [*Downloading applications*](../Apps/export-apps-cloud-hub.htm) |
| Indicates a child item admin.apps:read | Read all applications in the tenant |
| admin.automations | Read and manage all automations in the tenant  See also: [*Managing automations*](mc-managing-automations.htm) |
| Indicates a child item admin.automations:read | Read all automations in the tenant |
| admin.direct-access-gateways:remote\_configuration | Edit Direct Access gateway settings  See also: [*Configuring and troubleshooting Qlik Data Gateway - Direct Access*](../Gateways/direct-access-gateway-troubleshooting.htm) and [Public API](https://qlik.dev/apis/rest/direct-access-agents/). |
| admin.spaces | Read and manage all spaces in the tenant  See also: [*Managing spaces*](mc-administer-spaces.htm) |
| Indicates a child item admin.spaces:read | Read all spaces in the tenant |
| apps | Read and manage your applications  See also: [*Managing applications*](../Apps/manage-apps.htm) |
| Indicates a child item apps:export | Export your applications  See also: [*Downloading applications*](../Apps/export-apps-cloud-hub.htm) |
| Indicates a child item apps:read | Read your applications |
| automations | Read and manage your automations  See also: [*Managing automations*](mc-managing-automations.htm) |
| Indicates a child item automations:read | Read your automations |
| automl-experiments | Read and manage your ML experiments |
| automl-deployments | Read and manage your ML deployments |
| direct-access-gateways:consume\_data | Load data via Direct Access gateway connectors  See also: [*Qlik Data Gateway - Direct Access*](../Gateways/direct-access-gateway.htm) |
| identity.email:read | Read your email address  See also: [*Identity providers in Qlik Cloud*](mc-create-idp-configuration.htm) |
| identity.name:read | Read your full name |
| identity.picture:read | Read your profile picture  See also: [*Identity providers in Qlik Cloud*](mc-create-idp-configuration.htm) |
| identity.subject:read | Read your user subject identifier |
| spaces.data | Read and manage your data spaces  See also: [*Managing spaces*](mc-administer-spaces.htm) |
| Indicates a child item spaces.data:read | Read your data spaces |
| spaces.managed | Read and manage your managed spaces  See also: [*Managing spaces*](mc-administer-spaces.htm) |
| Indicates a child item spaces.managed:read | Read your managed spaces |
| spaces.shared | Read and manage your shared spaces  See also: [*Managing spaces*](mc-administer-spaces.htm) |
| Indicates a child item spaces.shared:read | Read your shared spaces |
| offline\_access | Access resources while you are offline  Information noteNot supported with the Single-page app client type. |

Information noteThis list reflects the scopes supported in the initial release. You can find a complete list of scopes on the Qlik Developer Portal [Scopes](https://qlik.dev/manage/access-control/scopes/).
