---
title: "Qlik Talend Cloud subscription options"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/subscription-options-QTC.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Planning your Qlik Cloud deployment", "Qlik Cloud capacity-based subscriptions"]
---

# Qlik Talend Cloud subscription options

Qlik Talend Cloud subscriptions are based on a [capacity model](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/subscription-options-qlik-cloud.htm) with three primary value meters: volume of [Data Moved](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/subscription-value-meters.htm#Data2), Job executions, and Job duration.

Tip note

Not sure which subscription plan (pricing plan, tier, or edition) your organization is on? Ask your service account owner (SAO) to check in [My Qlik](https://account.myqlik.qlik.com/). In the subscription overview, the SAO can see the current plan and subscription type. To learn more about available pricing plans, see [Qlik Pricing](https://www.qlik.com/us/pricing).

## Qlik Talend Cloud editions

Qlik Talend Cloud combines the capabilities of Qlik Talend Data Integration and Talend Cloud, and is available as a subscription option in the form of four tiers: Starter, Standard, Premium, and Enterprise. The higher editions provide more advanced capabilities including additional data sources and transformations, as well as governance, AI, and deployment capabilities.

All subscriptions include default analytics capabilities in Qlik Cloud with 25GB capacity.

Tip note

You can start a free trial of Qlik Talend Cloud from [Qlik Free Trials](https://www.qlik.com/us/free-trial).

## Synchronization with Talend Cloud

With Qlik Talend Cloud Premium and Enterprise editions, data spaces, users, and roles are automatically synchronized between Qlik Cloud and Talend Cloud. For more information, see [*Synchronization between Qlik and Talend - Qlik Talend Cloud subscriptions*](synchronized-resources.htm).

If your subscription includes Talend Cloud capabilities, you might need to connect Talend Cloud to Qlik Cloud manually. Once unified administration is enabled for your account, the tenants are linked automatically and these steps are no longer required. For more information, see [*Connecting Qlik Cloud with Talend Cloud*](connect-qlik-talend-tenants.htm).

Information noteTalend Studio 8.0.1 R2024-05 or higher is required to use Talend Cloud Studio capabilities with a Qlik Talend Cloud Premium or Qlik Talend Cloud Enterprise license.

## Regional availability

Talend Cloud capabilities are not yet available in all regions, and availability can vary by capability.

- For the regions where Qlik Talend Cloud capabilities are supported, see [Accessing Talend Cloud applications](https://help.qlik.com/talend/en-US/installation-guide-linux/Cloud/talend-cloud-application-url#region-code-mapping).
- For Qlik Cloud regions and backup locations, see [Qlik Cloud Regions](https://www.qlik.com/us/regions).
- For data integration capabilities in Qlik Cloud Government, see [*Qlik Cloud Government overview*](../../Global_Common/HelpSites/about-qs-government.htm).

## Subscription details

Supported capabilities are described in the [Qlik Cloud® Subscriptions](https://www.qlik.com/us/legal/product-terms) product description. To find out more about what is included and available in your region, visit [Qlik Pricing](https://www.qlik.com/us/pricing/data-integration-products-pricing) or contact Qlik Sales.

## Qlik Talend Cloud Starter

Qlik Talend Cloud Starter lets you replicate your data from all supported SaaS applications and from a limited set of databases, to any supported target. A simplified creation flow is used to easily set up a replication task with just a few clicks.

No additional customer infrastructure is required to connect to data sources, as a fully managed data gateway for simple replication projects is included. Qlik Talend Cloud Starter does not support all sources or low-latency change data capture, nor does it provide a way for clients to host and manage their own data gateway. Review your use case to determine if you require a higher subscription tier (Standard, Premium, or Enterprise) that provides [*Qlik Data Gateway - Data Movement*](../Gateways/replication-gateway.htm)

See also: [*Replicating data with a Qlik Talend Cloud Starter subscription*](../DataIntegration/Replicating/replicating-starter-subscription.htm)

## Qlik Talend Cloud Standard

Qlik Talend Cloud Standard
provides real-time data movement to any [target](#glossary-0 "Glossary term") from all supported relational databases and SaaS applications including CDC (Change Data Capture) when possible. Data pipeline and replication use cases are supported.

Basic transformation capabilities are provided to [transform](#glossary-1 "Glossary term") data as part of
the data [onboarding](#glossary-2 "Glossary term") process and include filtering and renaming datasets, adding, editing, and deleting columns.

Information noteThis edition does not include support for real-time SAP and mainframe sources, or advanced transformations. Consider Qlik Talend Cloud Premium or Qlik Talend Cloud Enterprise editions to achieve those use cases.

## Qlik Talend Cloud Premium

Qlik Talend Cloud Premium adds transformation capabilities to deliver ETL (Extract-Transform-Load) or ELT(Extract-Load-Transform) data transformation solutions. This supports a wide variety of use cases across client managed, hybrid and multi-cloud deployments, including data warehouse, data lake and data lakehouse architectures.

In addition, Qlik Talend Cloud Premium
enables customers to solve their operational data integration use cases such as application and API integration, including API design and testing. A set of mostly technical data quality features, plus basic data governance capabilities is also included.

This edition also includes data quality and governance capabilities, including semantics-based data validity and profiling. It also allows the creation of trusted data products and their activation and consumption in the data marketplace.

Information noteThis edition does not include support for real-time SAP and mainframe sources. Consider Qlik Talend Cloud Enterprise to achieve those use cases.

## Qlik Talend Cloud Enterprise

The Qlik Talend Cloud Enterprise
subscription includes all the features available with Qlik Talend Cloud Premium, as well as:

- Real-time data movement from SAP and mainframe sources.

Some of the extended capabilities included are:

- Data stewardship

Information noteQlik Talend Cloud Enterprise
does not include Qlik Cloud Analytics Premium capabilities. This requires a full Qlik Cloud Enterprise subscription.

## Minimum allowed scheduling intervals

When you land or replicate data, there are minimum allowed scheduling intervals depending
on your Qlik Talend Cloud subscription tier.

Minimum allowed scheduling intervals for database sources

| Qlik Talend Cloud subscription | Starter | Standard | Premium | Enterprise |
| --- | --- | --- | --- | --- |
| Without using Data Movement gateway | 1 hour | 1 hour | 30 minutes | 30 minutes |
| Using Data Movement gateway | N/A | Continuous | Continuous | Continuous |

Minimum allowed scheduling intervals for SaaS applications

| Qlik Talend Cloud subscription | Starter | Standard | Premium | Enterprise |
| --- | --- | --- | --- | --- |
| Without using Data Movement gateway | 1 hour | 1 hour | 30 minutes | 30 minutes |
| Using Data Movement gateway | N/A | 15 minutes | 5 minutes | 5 minutes |
| Streaming sources (Qlik Open Lakehouse) |  |  |  |  |
| Without using Data Movement gateway | N/A | Continuous | Continuous | Continuous |
