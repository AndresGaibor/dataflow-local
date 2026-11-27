---
title: "Enabling on-demand data in applications"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-odag.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Configuring features and integrations"]
---

# Enabling on-demand data in applications

On-demand application generation is controlled by the On-Demand App Service. [Tenant admins](#glossary-1 "Glossary term") can enable the On-Demand App Service in the Administration activity center, on the Settings page. The service is disabled by default and must be enabled before selection and template applications can be linked and on-demand applications generated.

When the service is switched from enabled to disabled, any pending requests to generate on-demand applications are allowed to finish. But once the service has been disabled, no new requests to generate applications will be accepted nor will developers be able to create or edit new On-demand application navigation links. These capabilities are restored once the service is re-enabled.

See also: [*Managing big data with on-demand applications*](../DataSource/Manage-big-data.htm)

## Enabling on-demand application generation

On-demand applications are generated in activity centers from navigation links that connect selection applications to template applications. The On-Demand App Service must be enabled to generate on-demand applications.

Do the following:

1. In the Administration activity center, go to the Settings page, then select the Feature control tab.
2. In the On-demand data section, toggle on On-demand application generation.

   Users are now allowed to produce and load data into applications on-demand.

### Switching off on-demand application generation

If you switch off the toggle, any pending requests to generate on-demand applications will complete. Once disabled, no new application generation requests are accepted.

## Enabling dynamic views

With the [dynamic views](#glossary-2 "Glossary term") option turned on, you can refresh charts from within your analytic tool environment.

Do the following:

1. In the Administration activity center, go to the Settings page, then select the Feature control tab.
2. In the On-demand data section, toggle on Enable dynamic views.

   Application sheets are now allowed to contain charts loaded from data sources on-demand.

### Switching off dynamic views

If you switch off the toggle when you have existing applications containing dynamic view-based charts, the applications will still function but with the following limitations:

- Dynamic charts will appear dimmed (and without data).
- The sheet editor will not expose dynamic view assets.

All charts and features not related to dynamic views will continue to function normally.
