---
title: "Using feedback and usage metrics to improve application usability"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Insights/insight-advisor-usage-metrics.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating visualizations with Insight Advisor"]
---

# Using feedback and usage metrics to improve application usability

If you are assigned the [audit administrator](#glossary-0 "Glossary term") role in a Qlik Cloud [tenant](#glossary-1 "Glossary term"), you can access usage metrics for Insight Advisor and Insight Advisor Chat through the Natural Language API. The metrics include feedback from application users on their experience using Insight Advisor and Insight Advisor Chat to generate [visualizations](#glossary-3 "Glossary term").

User interactions with an application through Insight Advisor, such as natural language questions, providing feedback, or method of analysis creation (for example, through the assets panel or by selecting an analysis type), are logged as events which can be accessed by audit administrators. The metrics can be used to improve application user experience through changes to the [logical model](#glossary-4 "Glossary term") or the data itself. These records will be retained for 30 calendar days.

Usage metrics can help application creators assess the success of application users in finding helpful insights in their data. For example, the metrics will identify what types of questions are not producing any results. The interpreter of the metrics can then make the needed adjustments to the application's data model or logical model to make the application more helpful. Additionally, if the metrics reveal a large number of unanswered questions, a possible solution could be to enable Insight Advisor Chat for more applications and to create new applications to help answer these questions.

Usage metrics for Insight Advisor and Insight Advisor Chat are collected for all application users in a shared or [managed space](#glossary-5 "Glossary term"). The metrics are collected from natural language API endpoints. As an audit administrator, it is not possible to view usage and feedback data for an application user's [personal space](#glossary-6 "Glossary term").

To view usage metrics and feedback for an application, you need the following:

- The Manage API keys permission in the tenant in which the application is located.
- Audit administrator role in the tenant in which the application is located.
- One of the following [permissions](#glossary-7 "Glossary term") in the space in which the application is located:

  - Shared spaces:

    - Owner
    - Can manage
    - Can edit
    - Can view
  - Managed spaces:

    - Is owner
    - Can manage
    - Can contribute
    - Can view
    - Has restricted view

Information note

The Natural Language API does not check section access controls in the application's load script. If an audit administrator has the Manage API keys permission and can open applications (as provided through the space permissions), they can view the application usage metrics.

For more information about the audit administrator role, see:

- [*Permissions for audit administrators*](../Admin/SaaS-user-permissions.htm#Audit) (user-based subscriptions)
- [*Permissions for audit administrators*](../Admin/SaaS-user-permissions-capacity-model.htm#Audit) (capacity-based subscriptions)
- [*Permissions for audit administrators*](../Admin/SaaS-user-permissions-anonymous.htm#Audit) (Qlik Anonymous Access subscriptions)

In addition to direct feedback, this endpoint can deliver other useful metrics, including whether user requests are sent through natural language with Insight Advisor Search, the assets panel, or Insight Advisor Analysis Types.

For specifics about the Natural Language API, see [Natural language](https://qlik.dev/apis/rest/natural-language).

For a tutorial on using the Natural Language API, see [Collect and share Insight Advisor feedback](https://qlik.dev/tutorials/collect-and-share-insight-advisor-feedback).
