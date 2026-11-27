---
title: "Enabling automatic group creation"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-enable-idp-groups.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Deploying Qlik Cloud", "Identity providers in Qlik Cloud", "Configuring an identity provider (IdP)"]
---

# Enabling automatic group creation

You can enable automatic group creation to simplify access management in your Qlik Cloud tenant. When enabled, groups are created dynamically based on the groups defined in your identity provider (IdP). This eliminates the need to assign access to individual users manually.

Only groups associated with Qlik Cloud users are added to your tenant.

## How it works

As users log in, new IdP groups are dynamically created. Groups are not imported all at once but discovered as users log in.

To configure the groups, you must use single sign-on (SSO) and have administrative access to your IdP.

## Enabling the feature

Do the following:

1. In the Administration activity center, go to the Settings page.
2. Select the Feature control tab.
3. Turn on the Creation of groups toggle.
