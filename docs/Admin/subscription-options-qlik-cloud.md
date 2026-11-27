---
title: "Qlik Cloud capacity-based subscriptions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/subscription-options-qlik-cloud.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Planning your Qlik Cloud deployment"]
---

# Qlik Cloud capacity-based subscriptions

Qlik Cloud offers capacity-based subscriptions for analytics and data integration. Each tier includes different capabilities and capacity limits, allowing you to choose the best fit for your organization. This page explains subscription options and key concepts, such as value meters, capacity limits, guardrails, and overage.

## Qlik Cloud Analytics

Qlik Cloud Analytics is a hosted analytics platform that helps your organization make data-driven decisions. It supports the entire data-to-insight life cycle, including:

- Interactive data visualizations and dashboards
- AI-powered analytics
- Predictive analytics with machine learning
- Collaboration and sharing with your team
- Custom and embedded analytics options
- Automated report generation and distribution
- A no code automation builder to trigger actions across systems

You can choose from the following subscription tiers:

- Starter
- Standard
- Premium
- Enterprise

Higher-tier editions include additional features and capacity. The highest tier, Qlik Cloud Enterprise combines the full capabilities of Qlik Cloud Analytics and Qlik Talend Cloud.

Analytics-only subscriptions include access to Qlik Talend Data Integration, allowing you to create QVD files in a Qlik Cloud data platform. These QVD files can be used in analytics applications.

For more details on the subscriptions, see [*Qlik Cloud Analytics subscription options*](subscription-options-analytics.htm).

## Qlik Talend Data Integration

Qlik Talend Data Integration is a hosted platform for building data pipelines and performing data integration tasks. It supports:

- Real-time, log-based change data capture with secure access to on-premises data behind firewalls
- Full load capabilities for SaaS data sources

Qlik Talend Data Integration is available in the following Qlik Talend Cloud subscription tiers:

- Starter
- Standard
- Premium
- Enterprise

Higher-tier editions provide more advanced data sources and transformations, as well as governance and deployment capabilities. This includes features from Qlik Talend Data Integration and Talend Data Fabric.

All subscriptions include default analytics capabilities in Qlik Cloud.

For more details on the subscriptions, see [*Qlik Talend Cloud subscription options*](subscription-options-QTC.htm).

## Qlik Cloud Enterprise

Qlik Cloud Enterprise includes all features of Qlik Cloud Analytics Premium and Qlik Talend Cloud Enterprise, plus increased capacity. It supports advanced transformations and real-time data movement from any source.

For more details, see:

- [*Qlik Cloud Analytics subscription options*](subscription-options-analytics.htm)
- [*Qlik Talend Cloud subscription options*](subscription-options-QTC.htm)

## Subscription value meters

Value meters determine pricing and billing for Qlik Cloud subscriptions by tracking resource usage. Capacity-based subscriptions primarily track data volume. Qlik Talend Cloud subscriptions also track third-party data transformations, job execution and duration, and Open Lakehouse compute. For a full list of value meters and how they are calculated, see [*Understanding the subscription value meters*](subscription-value-meters.htm).

When selecting a subscription, estimate your expected data volume and how you plan to use Qlik Cloud. Then choose capacity packs based on the value meters that apply to your subscription:

- Data for Analysis (Qlik Cloud Analytics subscriptions)
- Data Moved (Qlik Talend Cloud Cloud subscriptions)

Qlik Talend Cloud subscriptions with streaming workloads on streaming-enabled lakehouse clusters also use the Open Lakehouse compute value meter.

For Qlik Cloud Enterprise, you can subscribe to Data for Analysis, Data Moved, or both.

For Qlik Cloud Analytics Starter, pricing is based on the number of users.

### Monitoring usage

Administrators can track data capacity and other consumption-based resources in the Administration activity center. To analyze usage in more detail, use the detailed consumption report application.

For more information, see:

- [*Monitoring resource consumption*](mc-monitor-consumption.htm)
- [*Monitoring detailed consumption for capacity-based subscriptions*](usage-metrics-app.htm)

## Capacities, guardrails, and capabilities

All Qlik Cloud subscriptions provide the same speed, performance, and availability. They share the same user interface and [activity centers](#glossary-0 "Glossary term") on Qlik Cloud. However, each edition has different capacity limits and capabilities.

### Capacities

Capacities define how much of a resource you can consume. Some capacities are fixed, such as the number of parallel reloads. Others are consumption-based and measured over time, such as data capacity, application reloads, or reports generated per month.

Capacity usage is tracked across all tenants within a Qlik Cloud license. For example, if tenant A uses 200 reloads and tenant B uses 100 reloads under the same license, the total consumption is 300 reloads.

### Guardrails

Guardrails are hard limits on capacities. They prevent excessive usage when a capacity metric reaches a critical threshold. Guardrails help maintain Qlik Cloud performance and stability, for example, by limiting the number of parallel reloads to prevent system overload.

### Capabilities

Capabilities are Qlik Cloud features, such as managed spaces, reporting, and automations. Your subscription determines which capabilities are available and their capacity limits.

You can view the capabilities available in your tenant in the Administration activity center.

## Overage

Overage occurs when your usage of a resource, such as Data for Analysis, Data Moved, job executions, or job durations, exceeds the purchased capacity limit. When applicable, overage allows continued access without interruption.

- You can continue using the resource until the consumption reaches 10 times the purchased capacity limit.
- Overage consumption is calculated and billed monthly.

For more information, see the [Qlik Cloud® Subscriptions](https://www.qlik.com/us/legal/product-terms) product description.

### Overage notifications

When your usage approaches or exceeds a capacity limit (at 80%, 90%, and 100%), notifications appear in the Administration activity center. The service account owner (SAO) receives an email and may be contacted by Qlik about add-ons or upgrade options.

### Resources without allowed overage

Overage consumption is not allowed for the following resources:

- Qlik Predict deployed models: Your subscription includes a maximum number of deployed models across all tenants within the license. This limit applies per model, meaning that multiple ML deployments from the same model count as a single deployed model.

  - If you reach the limit, delete an existing deployed model or upgrade to a higher tier.
- Data for Analysis in Qlik Cloud Analytics Starter: The Starter edition has a fixed capacity. If you reach the limit, you cannot import or reload applications or add data files.

  - To free up capacity, delete applications and data files.
  - To increase capacity, upgrade your subscription.
