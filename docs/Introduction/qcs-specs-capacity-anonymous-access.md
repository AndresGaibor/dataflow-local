---
title: "Qlik Anonymous Access specifications and capacity limits"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/qcs-specs-capacity-anonymous-access.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Planning your Qlik Cloud deployment", "Qlik Anonymous Access subscriptions"]
---

# Qlik Anonymous Access specifications and capacity limits

This topic outlines the specifications and capacities for Qlik Anonymous Access subscriptions.

There are some differences between Qlik Anonymous Access subscriptions and other Qlik Cloud subscriptions. While you might need to consider some of the same requirements as for a [capacity-based](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/subscription-options-qlik-cloud.htm) subscription, Qlik Anonymous Access subscriptions also require attention to capacities for [anonymous access](#glossary-0 "Glossary term"), including:

- Maximum memory that can be consumed concurrently by all applications
- Maximum number of application sessions being consumed concurrently by all anonymous users

For more information about these metrics, see [*Understanding the subscription value meters*](../Admin/subscription-value-meters.htm). For information about differences between Qlik Anonymous Access and capacity-based subscriptions, see [*Differences between Qlik Anonymous Access and capacity-based subscriptions*](../Admin/subscription-options-anonymous.htm#Differences).

## Terminology on this page

The following terminology is used in content about anonymous access:

- Anonymous users: Users who are accessing application content without signing in, either through anonymous access links to an application or by consuming embedded analytics anonymously. These users are not members of the Qlik Cloud tenant, and also do not require Qlik accounts.
- Tenant users: Users who are members of the tenant and manage the tenant or develop analytics for consumption by anonymous users. Tenant users may have administrator privileges in the tenant.

## Available capabilities

This section describes the capabilities that are available for [tenant users and anonymous users](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Introduction/qcs-specs-capacity-anonymous-access.htm#Definitions) in Qlik Anonymous Access.

### Tenant users

#### Available capabilities for tenant users

The following features are available to tenant users:

- A [personal space](#glossary-1 "Glossary term") to create your own content
- Group collaboration in [shared spaces](#glossary-2 "Glossary term") where team members can develop and share applications
- Full Qlik Sense analytic capabilities, including Insight Advisor, Alerting, and Notes
- Drag-and-drop application creation and fully interactive applications
- Many of Qlik’s augmented intelligence capabilities, including Insight Advisor Chat and insight suggestions
- Access to Qlik Talend Data Integration for creating QVD files in a Qlik Cloud data platform The QVD files can be used in analytics applications.
- Direct data connectivity to over 40 data sources
- Data movement to Qlik Cloud from [relational database sources](../DataIntegration/SourcesConnections/supported-sources.htm) and [SaaS sources](../DataIntegration/Landing/connecting-web-applications.htm#Supporte)
- Qlik Automate: The basic tier of Qlik Automate is included with a Qlik Anonymous Access subscription.
- Script interface
- Catalog tools (Dataset viewer, impact analysis, lineage)
- Business glossaries
- Automated data refreshes

#### Available with additional purchase

The following are not included in a Qlik Anonymous Access subscription, but can be added with an additional purchase:

- Qlik Reporting Service
- Qlik Geocoding

For more information, contact your Qlik account representative.

#### Unavailable capabilities for tenant users

The following features are not available for any tenant user:

- In-application capabilities:

  - Key driver analysis
- Qlik Answers
- Qlik Predict, including Qlik Predict analytics connector
- Write table

### Anonymous users

#### Available capabilities for anonymous users

Anonymous users have access to limited versions of the Qlik Sense applications shared with them. In these applications, they have restricted permissions, and certain capabilities are not available. Other than applications, they do not have access to any other capability in Qlik Cloud.

The permissions granted to an anonymous user allow them to open and consume applications, sheets, or visualizations (depending on use case), making selections and applying public bookmarks. For more information about what anonymous users can do in an application, see [*Managed space permissions for anonymous users*](../Spaces/permissions-managed-space-anonymous.htm).

#### Unavailable capabilities for anonymous users

The following in-application capabilities are available in anonymous access tenants. However, they are not available for anonymous users when they open or consume application content.

- Storytelling
- Notes
- Insight Advisor
- Key driver analysis
- Visualization extensions
- NL insights visualization
- Write table visualization
- Reporting
- Alerts
- Subscriptions
- Associative insights

Besides applications in this restricted format, all other Qlik Cloud capabilities are unavailable for anonymous users.

## Subscription-based limits

The limits below apply to Qlik Anonymous Access subscriptions and are related to anonymous access capabilities.

Subscription-based limits for anonymous access capabilities

| Limit | Value |
| --- | --- |
| Application size: in-memory  Information note Large application support is not available in Qlik Anonymous Access subscriptions. | 1 GB |
| Application file size: upload from other Qlik Sense versions via activity center[1 Applies to the disk space used by application files, not the in-memory limit.](javascript:void(0)) | 200 MB |
| Applications opened concurrently | 50 |
| Engine hypercube memory limit[2 The standard hypercube memory limit in Qlik Cloud is 10 GB, but for Qlik Anonymous Access, this limit is constrained by the in-memory application size limit.](javascript:void(0)) | 1 GB |
| Tenants per license | 1 |
| User session timeout: anonymous sessions | 15 minutes |

In addition to the limits above, the following limits apply to scheduled reloads.

Subscription-based limits for scheduled reloads

| Limit | Value |
| --- | --- |
| Concurrent scheduled reloads[3 Applies to reloads across all tenants sharing the same entitlement. If all reloads are in use by one tenant, others must wait.](javascript:void(0)) | 10 |
| Scheduled reloads per application per day[4 Applies also to scripts, data flows, and table recipes.](javascript:void(0)) | 48 |

For more information about subscription limits, see:

- [Qlik Pricing](https://www.qlik.com/us/pricing)
- [Qlik Product Terms](https://www.qlik.com/us/legal/product-terms) (Qlik Cloud® Subscriptions)

## Platform guardrails

To maintain performance and stability, Qlik Cloud enforces guardrails—fixed limits that help prevent resource overuse. These guardrails apply to all tenants.

Platform guardrails

Qlik Cloud Analytics platform guardrails

| Limit | Value |
| --- | --- |
| Variables in exported application content (see [*Working with sheets*](../Sheets/working-with-sheets.htm)) | 1,100 |
| File size: export to Microsoft Excel (see [*Downloading application content*](../Download/downloading-visualization.htm)) | 100 MB |
| Tasks for scheduled data refreshes per application, script, data flow, or table recipe | 10 |
| Reload runtime limit (see [*Reloading application data*](../Apps/reloading-apps-cloud-hub.htm)) | 3 hours |
| Rows in data alerts (see [*Troubleshooting alerts*](../Alerting/troubleshooting-alerts.htm)) | 100,000 |
| Rows in email notifications (see [*Troubleshooting alerts*](../Alerting/troubleshooting-alerts.htm)) | 10 |
| Data alerts per user (see [*Troubleshooting alerts*](../Alerting/troubleshooting-alerts.htm)) | 50 |
| Webhooks per user | 150 |
| Subscriptions per user (see [*Scheduling reports with subscriptions*](../Reporting/Subscriptions/Subscription-reports.htm)) | 100 |
| Recipients per subscriptions (see [*Scheduling reports with subscriptions*](../Reporting/Subscriptions/Subscription-reports.htm)) | 100 |
| Session inactivity timeout: tenant user sessions | See [*Configuring session timeouts*](../Admin/configure-session-timeout.htm) for defaults and ranges |
| Maximum session duration: tenant user sessions | See [*Configuring session timeouts*](../Admin/configure-session-timeout.htm) for defaults and ranges |
| Application timeout (starts after session timeout + 120 seconds) | 60 seconds |
