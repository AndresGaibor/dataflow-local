---
title: "Managing feature preview for your tenant"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-manage-preview-features.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Configuring features and integrations"]
---

# Managing feature preview for your tenant

As a tenant administrator, you can control how feature preview is made available in Qlik Cloud.

Govnote-not-inNot supported in Qlik Cloud Government.

Govnote-not-inNot supported in Qlik Cloud Government - DoD.

## Understanding how preview features work

Preview features are optional features that are released before general availability. Users can activate preview features only when both of these conditions are met:

1. Feature preview is enabled for the tenant.
2. The user has the required permissions.

Users without the permission can view available preview features but cannot activate them.

For more information about viewing and activating preview features, see [*Feature preview*](../Introduction/feature-preview-program-overview.htm).

## Enable feature preview for the tenant

Tenant administrators must enable feature preview before users can access preview features.

1. In Administration, go to Settings > Tenant > Feature preview.
2. Open and read the terms and conditions.
3. Turn on Enable feature preview.

Information noteAfter you enable feature preview for the tenant, you cannot turn off this setting at the tenant level. To control which users can activate preview features, use the Activate feature preview permission, which becomes available in Manage users > Permissions.

## Manage access to preview features

The Activate feature preview permission controls whether users can activate and deactivate preview features.

The permission is available in the default permissions and custom roles, under Features and actions > Feature preview.

By default, the Activate feature preview permission is set to Allowed in the default permissions. This means that all users can activate and deactivate preview features after feature preview is enabled for the tenant.

To restrict activation to selected users:

1. Set the default permissions to Not allowed.
2. Create a custom role that has Activate feature preview set to Allowed.
3. Assign the custom role to the users who should be able to activate preview features.

For more information, see [*Permission settings — Features and actions*](permissions-scopes-capacity-model.htm#FeaturesActions).

## Preview lifecycle and administration

Preview features follow a lifecycle from announcement to either general availability or discontinuation. During the preview period, Qlik may adjust functionality based on customer feedback.

Because preview features can change during this phase, review your role settings and pilot groups regularly.

## Security and compliance

Preview features follow the same security and compliance standards as generally available features.

For privacy details, see the [Qlik Product Privacy Notice](https://www.qlik.com/us/legal/product-privacy-notice).
