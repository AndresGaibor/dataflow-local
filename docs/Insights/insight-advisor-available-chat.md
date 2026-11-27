---
title: "Making applications available in Insight Advisor Chat"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Insights/insight-advisor-available-chat.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Managing applications"]
---

# Making applications available in Insight Advisor Chat

You can make your applications available in Insight Advisor Chat in the Analytics and Insights [activity centers](#glossary-0 "Glossary term").

When your application is available, users with access to that application can search [Insight Advisor](#glossary-1 "Glossary term") in your application with [Insight Advisor Chat](#glossary-2 "Glossary term"). For more information on Insight Advisor Chat, see [*Exploring applications with conversational analytics*](insights-chat.htm).

When your application is available, users with access to that application can also interact with the application using conversational analytics in Microsoft Teams. For more information, see [*Exploring application content with conversational analytics in Microsoft Teams*](insight-advisor-chat-microsoft-teams.htm).

Information noteApplications that use Section Access require additional configuration for service users to be available in Insight Advisor Chat. If you have sensitive information in application names, field names, or master item names, these may be exposed by making applications using Section Access available for Insight Advisor Chat. Application suggestions for queries include applications in spaces to which users have access. These may include applications to which users do not have access in an application's Section Access. Selecting these applications will do nothing, however. When clicking Dimensions or Measures to view the available items from an application using Section Access, users may see items to which they do not have access. Clicking on these items will not provide any data to the users, however. For more information, see [*Using Section Access and Insight Advisor Chat*](../Scripting/Security/manage-security-with-section-access.htm#Section).

Information note

Insight Advisor Chat is not available when a tenant is use the Qlik Answers agentic experience. Users can use Qlik Answers to explore applications with natural language.

## Application content availability in Insight Advisor Chat

What users can search for and access with the Measure and Dimension buttons with Insight Advisor Chat depends on the space [permissions](#glossary-3 "Glossary term") of users, if the application is published, and if there is a [logical model](#glossary-5 "Glossary term") applied to your application.

For your own applications in your [personal space](#glossary-6 "Glossary term"), you can search for fields and master items from the application.

For applications in [shared spaces](#glossary-7 "Glossary term"), users with Can edit, Can edit data in applications, or Can manage permissions can search for fields and master items. Users with Can view permission can only search for master items.

For applications in [managed spaces](#glossary-8 "Glossary term"), users with Can manage permission can search for fields and master items. Users with Can contribute or Can view permissions can search for master items.

If you have [business logic](#glossary-9 "Glossary term") applied to an application in a shared or managed space, users can search for available fields and master items based on the logical model regardless of their permissions in the space.

Clicking the Measure or Dimension button (or entering show [measure](#glossary-10 "Glossary term") or show [dimension](#glossary-11 "Glossary term")) will show the corresponding master items. If the application has no master items, fields related to measures or dimensions are shown instead. Fields or master items hidden in the logical model will not appear when the button is clicked, but can be searched for in a query.

## Turning on Insight Advisor Chat

To turn Insight Advisor Chat on and off for an application in a collaborative space, you need the following roles in the space:

- Shared space: Can edit or higher permissions. See [*Managing permissions in shared spaces*](../Spaces/managing-shared-spaces.htm).
- Managed space: Can manage, Can operate, or higher permissions. See [*Managing permissions in managed spaces*](../Spaces/managing-managed-spaces.htm).

Information noteFor user-based subscriptions, the Can operate role also requires a Professional user entitlement.

Do the following:

1. In the application navigation bar, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > Settings.
2. In the menu, switch to the Capabilities tab.
3. Turn on Enable application for Insight Advisor Chat in activity centers.

Related learning:

- [How do I make applications accessible to Insight Advisor in Qlik Cloud?](/lnk/How_make_apps_access_Insight_Advisor)
