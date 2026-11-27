---
title: "Discovery Agent"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DiscoveryAgent/discovery-agent.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data"]
---

# Discovery Agent

The Discovery Agent empowers business users to monitor changing data trends over time in scrollable feeds. With AI-assisted anomaly and outlier detection, the Discovery Agent simplifies how you can uncover key patterns in data, allowing you to take swift action on rapidly shifting trends that affect your organization.

Govnote-not-inNot supported in Qlik Cloud Government.

Govnote-not-inNot supported in Qlik Cloud Government - DoD.

## Use cases

In a world of constantly changing data, the Discovery Agent offers a way to spot trends and anomalies in time to take action on them. This is achieved by focusing on what has changed from one data refresh to the next, and then delivering the resulting insights in a format that is easy to scan.

In the past, trend analysis involved monitoring multiple applications for insights, acting only after uncovering trends. These trends can sometimes be difficult to find without spending large amounts of time performing complex analysis. Within this window of time, insights can be missed or addressed too late.

The Discovery Agent allows a more proactive approach in which insights are delivered continuously in the familiar form of a feed. This reduces the barriers to entry for advanced trend analysis and accelerates understanding of enterprise data.

Examples of specific use cases are:

- Executives scan their feeds to view how sales and margins are changing over time, using insights to take action on critical issues.
- Business analysts inspect their feeds for changes to global market performance.
- Sales teams use their feeds to track opportunities for revenue, growth, and increased customer satisfaction.

## Features

The Discovery Agent has the following features:

- A simple in-application experience for configuring insight tracking, featuring intuitive design and concepts that are familiar to Qlik analytics developers.
- Simple consumption of insights in the scrollable, familiar feed format.
- Support for exposing feed cards in external web applications by using qlik-embed.

  [*Embedding feeds in external web applications*](feeds.htm#EmbedCards)
- Integration with Qlik Answers, making it easy to further explore insights using generative AI.

## Workflow

1. Application developer creates insight triggers

   An application developer creates insight triggers to control the insights that are generated for users.

   [*Working with Discovery Agent insight triggers*](insight-triggers.htm)
2. Insights are generated as data changes

   Set up a reload schedule to update the data in the application on a regular basis. Insight triggers are evaluated when data changes. When noteworthy changes are found, they are presented in the feeds of users that have view access to the application.

   [*Refreshing analytics data*](../Refresh/refresh-analytics-data.htm)

   [*Working in spaces*](../Spaces/Spaces.htm)
3. Analysts inspect their feed

   Business users can open their feed from Qlik Cloud activity centers to review insights and use them to take data-driven action.

   [*Analyzing Discovery Agent feeds*](feeds.htm)

## Requirements

- Your access to Discovery Agent is governed by the terms of your Qlik Cloud subscription. For more information, see the following, or contact your Qlik account representative:

  - [Qlik Pricing](https://www.qlik.com/us/pricing)
  - [Qlik Cloud® Subscriptions](https://www.qlik.com/us/legal/product-terms)
- The Qlik Cloud tenant needs to have cross-region inference turned on in order for Discovery Agent to be available. For more information, see [*Enabling cross-region inference*](../Admin/cross-region-data-processing.htm).
- Permissions control user access to Discovery Agent. These permissions are also only available for tenants with cross-region inference turned on.

  Discovery Agent tenant-level permissions are turned off by default in the default permissions. To activate Discovery Agent, administrators can either enable the Discovery Agent permissions in the default permissions or assign them to specific users through a custom role. Using a custom role allows administrators to grant access based on specific use cases.

  For information about these permissions, see [*Administering Discovery Agent*](discovery-agent-admin.htm).
- The Discovery Agent supports exploration of insights in Qlik Answers. The following requirements apply:

  - Your tenant needs to have capacity for Qlik Answers and Qlik Answers needs to be activated. See [*Qlik Answers*](../QlikAnswers/Qlik-Answers.htm).
  - The application you are exploring needs to be indexed for Qlik Answers. In other words, it needs to be made available in Qlik Answers. See [*Making applications available for Qlik Answers*](../QlikAnswers/Applications/working-with-apps-in-qlik-answers.htm#Making).
  - User permissions for exploring insights in Qlik Answers are governed by Qlik Answers permissions, as well as the permissions for Discovery Agent.

    See [*Qlik Answers access and permissions*](../QlikAnswers/qlik-answers-permissions.htm) and [*Discovery Agent permissions*](discovery-agent-admin.htm#Permissions).

## Discovery Agent capacities and limitations

### Guardrails

Discovery Agent guardrails

| Limit | Value |
| --- | --- |
| Maximum number of insight triggers per application (including active and inactive) | 50 |
| Maximum number of breakdown dimensions per insight trigger | 3 |
| Maximum number of values that can be used per breakdown dimension | 50 |
| Maximum number of insight triggers per tenant | 200 |

### General limitations

These limitations apply to both insight triggers and feeds.

- The Discovery Agent is available in English only.
- The Discovery Agent does not support fine-grained access control. To work with insight triggers and feeds for an application, you need to be a member of the space with the required space permissions.
- Insight triggers are not available for applications that use [section access](#glossary-0 "Glossary term"). Likewise, applications that use section access cannot generate insights in feeds.

### Insight trigger limitations

These limitations apply to insight triggers.

- Data volume requirements apply for insight triggers depending on time period and insight type. For more information, see [*Data volume requirements — insight triggers*](#DataVolume).
- For applications that are duplicated or published, insight triggers must be created again. See [*Scenarios for moving, publishing, and duplication*](insight-triggers.htm#Scenarios).
- Master dimensions are not supported when defining insight triggers, neither for the time dimension nor breakdown dimensions.

#### Data volume requirements — insight triggers

Minimum and maximum data points per insight type

| Insight type | Aggregation period | Minimum number of data points | Maximum number of data points |
| --- | --- | --- | --- |
| Spike detection | Year, quarter, month, week | 4 | 50 |
| Spike detection | Day | 7 | 365 |
| Record high or record low | Year, quarter, month, week | 4 | 50 |
| Record high or record low | Day | 7 | 365 |
| Change in trend | Year, quarter, month, week | 20 | 50 |
| Change in trend | Day | 20 | 365 |
| Change in baseline | Year, quarter, month, week | 20 | 50 |
| Change in baseline | Day | 20 | 365 |
| Above model or below model | Year, quarter, month, week | 4 | 50 |
| Above model or below model | Day | 7 | 365 |

### Feed limitations

- Insights in feeds expire and are deleted after 90 days.

## Learn more

- [*Working with Discovery Agent insight triggers*](insight-triggers.htm)
- [*Analyzing Discovery Agent feeds*](feeds.htm)
- [*Administering Discovery Agent*](discovery-agent-admin.htm)
