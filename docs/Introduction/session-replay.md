---
title: "Session replay in Qlik Cloud"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/session-replay.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Configuring features and integrations"]
---

# Session replay in Qlik Cloud

Session replay helps Qlik understand how users interact with its products—where they click, what paths they take, and where they encounter friction.

Session replay collects interaction data, such as clicks, navigation patterns, and interface usage. No customer content or customer data is collected. These interactions are reconstructed to visually simulate a session so that Qlik product and design teams can experience what the user experienced.

Session replay has no impact on product performance and is used solely for improving Qlik products.

For more information about how Qlik manages privacy in its products, refer to the [Qlik Product Privacy Notice](https://www.qlik.com/us/legal/product-privacy-notice).

## Session replay settings

Session replay can be activated and deactivated at both the tenant and user levels. The settings for session replay are found in each of these designated areas:

- [Tenant](#glossary-0 "Glossary term") level: Administration activity center > Settings > Tenant.
- User level: User profile menu > Settings > Profile.

### Tenant level

The tenant-level session replay settings are controlled by [tenant administrators](#glossary-1 "Glossary term").

The implications of activating or deactivating session replay at the tenant level are:

- Off: If a tenant admin does not allow session replay, all users within that tenant are automatically excluded from session replay.
- On: If a tenant admin allows session replay, each individual user can [turn session replay on and off](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/session-replay.htm#UserLevel) in their personal settings.

Do the following:

1. In the Administration activity center, go to the Settings page, then select the Tenant tab.
2. Under Usage tracking, turn Allow session replay on or off.

### User level

Users can individually choose to participate in session replay. If users choose to turn on the feature, session replay will be active.
Changing this preference takes effect immediately and can be updated at any time.

If [the tenant admin has not allowed session replay](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/session-replay.htm#AdminLevel), you are automatically excluded from session replay and will not see Session replay settings in your personal settings.

Do the following:

1. Click your user profile in Qlik Cloud, then select Settings.
2. In the Profile tab, you can find the option to turn Allow session replay on and off.

## Learn more

- [*Managing your personal settings*](profile-settings.htm)
- [*Configuring features and integrations*](system-admin.htm)
