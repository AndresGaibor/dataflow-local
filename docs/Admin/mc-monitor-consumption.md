---
title: "Monitoring resource consumption"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-monitor-consumption.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Monitoring system and resources"]
---

# Monitoring resource consumption

Administrators can track usage of licensed resources in the Home pane of the Administration activity center. This page provides an overview of capacity usage, such as users, data, and reports. It also lists the capabilities that are enabled in your subscription and their limits.

## Understanding what is shown

The information and charts visible on the Home pane depend on your subscription type:

- Capacity-based subscriptions show the total number of users in the tenant, while user-based subscriptions track Professional and Analyzer entitlements.
- Some charts are not available in Qlik Sense Enterprise SaaS or Qlik Sense Business.

Tip note

If you have a capacity-based subscription, you can view detailed usage information in a dedicated application. For more information, see [*Monitoring detailed consumption for capacity-based subscriptions*](usage-metrics-app.htm)

## Switching between tenant views

If your license includes multiple tenants, you can switch between viewing data for a single tenant or for all tenants combined.

- This tenant shows usage for the current tenant.
- All tenants shows aggregated usage across all tenants.

Information noteSome charts do not support both views. Large application utilization is available only in the This tenant view, while the users charts always display total values across all tenants, regardless of the selected view.

## Reading the consumption charts

The Home pane includes bar charts that show how much of each resource you've used compared to what's included in your subscription.

Here’s an example of what the Home page looks like:

Example of the Home page showing usage charts

![The Home pane in the Administration activity center with consumption charts](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_administration-home.png "Click to view full size")

Each chart uses colors and symbols to help you understand usage:

- Blue bar: Consumed amount current period.
- Light gray bar: Purchased amount current period.
- Dark gray bar: Purchased amount previous period.
- Red bar: Overage consumption (when usage exceeds the purchased amount for the period). For more information, see [*Overage*](subscription-options-qlik-cloud.htm#Overage).
- Dark gray vertical line: Consumed amount previous period.
- Black vertical line: Peak consumed amount
- Orange warning triangle: Usage is close to the purchased amount
- Red warning triangle: Usage has exceeded the purchased amount

You can hover over a chart to see a tooltip with more details.

## Users

The users charts show the total number of entitlements available across all tenants in your license. Which charts are shown depends on your subscription: user-based subscriptions display Professional, Analyzer, and Analyzer capacity entitlements, while capacity-based subscriptions show only total users.

## Data for Analysis

The Data for Analysis chart shows the total data moved into Qlik Cloud. This includes data analyzed, profiled by the catalog, or landed in Qlik Cloud. The amount of data is calculated as total loaded data minus deleted data. The chart is updated regularly throughout the day, with the last update shown below the chart.

The chart shows:

- Color-coded categories for types of data, such as application imports, data files, or application reloads.
- Peak usage for the current month (black vertical line), which is the highest data usage across all tenants in your license.

Important to know:

- The chart shows a snapshot of current usage, not the full month's history.
- You can see current overages (when usage exceeds the purchased amount), but overages from earlier in the month are not retained in the chart.

To see daily usage details, including any overages, use the Data Capacity Reporting App. See [*Monitoring detailed consumption for capacity-based subscriptions*](usage-metrics-app.htm) for details.

For more information, see [*Data for Analysis*](subscription-value-meters-data-for-analysis.htm).

## Large application capacity

The Large application utilization chart shows the current usage of large application capacity for the tenant. The peak capacity is indicated by a black vertical line on the chart, representing the maximum consumption for the day.

Large application capacity is assigned on a per-tenant basis, and there is no overall aggregate for the license. As a result, the chart will not appear if All tenants is selected from the dropdown.

For more information, see [*Monitoring large application capacity*](large-app-support.htm#Monitori).

## Data Moved

The Data Moved chart shows the volume of data moved with Qlik Talend Data Integration for the month. The Data Moved metric is the sum of all data moved—full load and CDC—to cloud destinations. The metric does not include the move of data into Qlik Cloud for analytics, which is counted as Data for Analysis. The initial full load of any new table or file is not included. For more information, see [*Data Moved*](subscription-value-meters.htm#Data2).

## Third-party data transformation

The Third-party data transformation chart shows the volume of all datasets that are registered and used in transformations but not moved by Qlik Talend Data Integration. Data that is both transformed and moved is only counted once.

## Open Lakehouse compute

The Open Lakehouse compute chart shows the amount of lakehouse core-hours used with Qlik Open Lakehouse for the month. This metric is the sum of all Open Lakehouse core-hours across lakehouse clusters. For more information, see [*Open Lakehouse compute*](subscription-value-meters.htm#Open).

## Automation runs

The Standard automation runs [chart](#glossary-0 "Glossary term") shows the number of automations of non-billable automations executed in the current month. The Third-party automation runs chart shows the number of billable automation runs that used at least one third-party block in the current month.

In both charts, run types can include manual, test, scheduled, triggered, or webhook executions.

The maximum number of third-party automation runs is determined by your license. Contact your tenant admin for more information.

## Reports generated

The Reports generated chart shows the number of reports generated from the value-add Qlik Reporting Service capabilities for the month.

## Qlik Predict deployed models

The Qlik Predict deployed models chart shows the number of deployed ML models that are activated for making predictions.

A Qlik Cloud Analytics subscription defines a maximum number of deployed models that can be active at the same time (across all tenants within the subscription, for multi-tenant subscriptions). This consumption limit is defined per model, meaning that multiple ML deployments created from a single model count as a single deployed model. If you have reached the maximum number of active deployed models, you can do one of the following:

- Deactivate one or more currently active models to make room for new ones.
- Delete one or more existing deployed models to make room for new ones.
- If you need to have all current and future models activated at the same time, upgrade the subscription to a higher tier. For information about upgrade options, see the [Qlik Cloud® Subscriptions](https://www.qlik.com/us/legal/product-terms) product description.

For more information about monitoring Qlik Predict consumption, see [*Monitoring Qlik Predict consumption for the subscription*](mc-managing-experiments-deployments.htm#MonitorConsumption).

## Reloads

The reloads chart shows the number of scheduled reloads for the month.

## Questions (monthly)

The Questions (monthly) chart shows the number of questions that Qlik Answers has been asked this month.

For more information, see [*Working with assistants*](../QlikAnswers/Assistants/assistants.htm).

## Knowledge base pages

The Knowledge base pages chart shows the number of indexed pages in Qlik Answers knowledge bases.

For more information, see [*Working with knowledge bases*](../QlikAnswers/KnowledgeBases/knowledge-bases.htm).

## Capabilities

The list shows the capabilities that are enabled with your subscription and the limits on the capabilities. Capabilities are features in Qlik Cloud such as managed spaces, Reporting, automations, or [anonymous access](#glossary-1 "Glossary term"). Your subscription determines which capabilities you can use and their respective limits. For example, your subscription might include automations with a limit of running 10 automations concurrently.

### Anonymous access capacities

If you have a Qlik Anonymous Access subscription, the following capabilities are shown:

- Anonymous Capacity:
  This value meter refers to the total RAM usage that all applications loaded into memory can consume at a given time. This includes tenant user sessions (sessions opened by users and administrators within the tenant) and anonymous user sessions (sessions opened by users who are not logged into the Qlik Cloud tenant).
- Anonymous Concurrent Sessions:
  This value meter defines the maximum number of application sessions that can be run concurrently by anonymous users (users who are not logged into the Qlik Cloud tenant).

For more information, see [*Qlik Anonymous Access subscriptions*](subscription-options-anonymous.htm).
