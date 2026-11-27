---
title: "Differences between the Qlik Cloud Analytics subscription models"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/comparing-subscriptions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Planning your Qlik Cloud deployment", "Qlik Cloud capacity-based subscriptions", "Qlik Cloud Analytics subscription options"]
---

# Differences between the Qlik Cloud Analytics subscription models

Qlik Cloud Analytics offers a capacity-based subscription model with updated pricing and packaging. If you are transitioning from a user-based Qlik Sense Enterprise SaaS or Qlik Sense Business subscription, there are key changes to be aware of.

## Capacity-based subscription model

The capacity-based model measures pricing based on data capacity, whereas the user-based model is based on the number of users.

The capacity-based model provides organization-wide access to analytics and data from complex sources like mainframes and SAP. It also includes additional capabilities, such as:

- Data movement to Qlik Cloud
- Catalog and lineage features
- Free tiers of Automations and Qlik Predict

The capacity-based model allows overage when resource usage exceeds the purchased capacity, ensuring uninterrupted access to Qlik Cloud.

## Subscription comparisons

Qlik Cloud Analytics Premium is comparable to Qlik Sense Enterprise SaaS and Qlik Cloud Analytics Standard is comparable to Qlik Sense Business.

You can combine different editions of Qlik Cloud Analytics and Qlik Talend Data Integration, depending on how much capacity you need for analyzed and moved data. Qlik Cloud Enterprise combines the highest editions of Qlik Cloud Analytics and Qlik Talend Data Integration as one package.

Contact Qlik Sales for more information.

## Changes in user management

There are some important differences in user management between user-based and capacity-based subscriptions.

- In user-based subscriptions, user entitlements (Professional and Analyzer) come with predefined permissions. For example, an Analyzer user cannot create applications unless their entitlement is upgraded to Professional. Additional permissions can be assigned on top of these entitlements.
- In capacity-based subscriptions, user actions depend only on assigned roles and permissions.

### Comparing Analyzer entitlement and capacity-based roles

A user with an Analyzer entitlement can:

- View applications created by others, but cannot create or edit them.
- Create personal sheets, stories, bookmarks, and snapshots in applications that are shared with them, based on their assigned space roles.
- Generate on-demand applications, print objects, stories, and sheets, and export data to Microsoft Excel.

In capacity-based subscriptions, similar permissions can be granted by assigning the Has restricted view role in [managed spaces](#glossary-0 "Glossary term"). This role allows the user to:

- View sheets and applications created by others but only in managed spaces.
- Create personal notes and private bookmarks.
- Depending on the default permissions, they may also have permission to download application content.

For more details, see:

- Analyzer permissions in shared spaces: [*Shared space permissions for users with Analyzer entitlement*](../Spaces/permissions-shared-space-analyzer.htm)
- Analyzer permissions in managed spaces: [*Managed space permissions for users with Analyzer entitlement*](../Spaces/permissions-managed-space-analyzer.htm)
- The Has restricted view role: [*Managed space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-managed-space-prof-full.htm)
- Default permissions: [*Default permissions and custom roles*](permissions-scopes.htm).
