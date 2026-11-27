---
title: "Building logical models for Insight Advisor with Business logic"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/BusinessLogic/business-logic-logical-models.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Managing your data", "Customizing logical models for Insight Advisor"]
---

# Building logical models for Insight Advisor with Business logic

[Insight Advisor](#glossary-0 "Glossary term") uses a logical model based on learned precedents to generate analyses based on your queries. You can define your own logical model for your applications with Business logic.

Insight Advisor relies on the Qlik cognitive engine and learned precedents to understand the relationships and uses of fields in your data model. Optionally, you can customize the logical model to improve Insight Advisor results. You can customize your logical model in Logical model under Business logic in the application navigation menu.

Information note

When [business logic](#glossary-1 "Glossary term") is enabled in an application, precedent-based learning is disabled for the application.

## Understanding logical models

The logical model of an application is the conceptual model Insight Advisor uses when generating visualizations. It is built from the underlying data model of an application. Each application has a single logical model. Fields and master items are the core components of the logical model. They are organized into groups. Groups indicate a conceptual association or relationship between fields or master items. The logical model also contains information about possible relationships between groups.

The logical model directly influences how Insight Advisor functions. For example, when a user selects a field to show a trend analysis, Insight Advisor tries to find a date field that is part of a primary calendar group. If the field was Sales, Insight Advisor would prioritize a field like Order Date over the field Employee Birth Date.

Business logic also affects how the system chooses between fields in natural language questions. For example, the fields Product Name and Product Code are grouped as a single group. If 'what are sales by product' is used as a natural language question, Product Name would be used for 'product' as it is a better choice for that group.

The default logical model used for business logic is a star schema. Business logic enables you to construct different modeling for your application if a star schema is not optimal. Business logic can also help constrain [aggregation](#glossary-3 "Glossary term") in logical models containing semi-additive [measures](#glossary-4 "Glossary term") or very large measure tables. This improves the exploration of application data in Insight Advisor.

## Customizing logical models

Logical model is divided into the following sections for customizing the logical model of an application:

- Overview: Overview provides a summary of your business logic. Clicking the cards for Fields & groups, Packages, Hierarchies, or Behaviors opens the corresponding section.
- Fields & groups: Fields & groups enables you to define the groups to which your fields and master items belong in the logical model.
- Packages: Packages enables you to create collections of related groups. This prevents groups from being used together that are not in the same package.
- Hierarchies: Hierarchies enables you to define drill-down relationships between groups.
- Behaviors: Behaviors enables you to specify prefer or deny relationships between fields. Behaviors can also enforce required [selections](#glossary-5 "Glossary term").
- Calendar periods: Calendar periods enables you to create default periods of analysis for Insight Advisor.

To customize a logical model, do the following:

1. Enable the customization of the business logic of your application.
2. Define your fields and groups.

   [*Defining fields and groups in Insight Advisor*](business-logic-fields-groups.htm)
3. Optionally, add your groups to packages.

   [*Setting logical model scopefor Insight Advisor with packages*](business-logic-packages.htm)
4. Optionally, define hierarchies between groups

   [*Creating drill-down analysis with hierarchies in Insight Advisor*](business-logic-hierarchies.htm)
5. Optionally, apply behaviors.

   [*Applying behaviors to logical models for Insight Advisor*](business-logic-behaviors.htm)
6. Optionally, create calendar periods.

   [*Defining analysis periods with calendar periods in Insight Advisor*](business-logic-calendar.htm)

You can reset your logical model to the default. You can also disable business logic temporarily.

## Enabling custom business logic

Do the following:

1. In an application, open the application navigation menu and select Logical model.
2. Click Continue.

Custom business logic is now enabled for your application. Precedent-based learning is now disabled.

Information noteWhen you activate a custom logical model, recommendations for field visibility and data value search are automatically applied. This means that certain fields in your data model might not be visible or searchable in Insight Advisor. You can reconfigure the logical model to revert these recommendations, or apply other customizations. See [*Visibility*](business-logic-fields-groups.htm#Visibility) and [*Data value lookup*](business-logic-fields-groups.htm#DataValueLookup).

## Resetting business logic

You can reset your logical model to the default model. Resetting disables custom business logic and enables precedent-based learning in Insight Advisor.

Do the following:

1. In Logical model, click Reset to default.
2. Click Confirm.

## Disabling business logic

You can disable custom logical models. Unlike resetting business logic, you can enable your custom business logic again later. While your business logic is disabled, it will use the default business logic for your application.

Do the following:

1. In Logical model, click Disable logic.
2. Click Confirm.

## Limitations

Business logic has the following limitations:

- If you are using or intend to use business logic, you cannot alter any of the default autoCalendar fields in the load script. Changes to these fields can break the business logic and, once impacted, the business logic cannot be recreated.

Related learning:

- [Using Insights to Create Visualizations](/lnk/Use-Insights-Create-Visualizations_QS)
