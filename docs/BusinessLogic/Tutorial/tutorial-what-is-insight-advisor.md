---
title: "What is Insight Advisor and business logic?"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/BusinessLogic/Tutorial/tutorial-what-is-insight-advisor.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Managing your data", "Customizing logical models for Insight Advisor", "Tutorial – Customizing how Insight Advisor interprets data"]
---

# What is Insight Advisor and business logic?

[Insight Advisor](#glossary-0 "Glossary term") is a suite of Qlik Sense features. Insight Advisor helps you build your data model, create [visualizations](#glossary-1 "Glossary term"), and analyze data. [Business logic](#glossary-2 "Glossary term") helps Insight Advisor interpret your data.

## Insight Advisor

Insight Advisor comprises the following Qlik Sense features:

- Insight Advisor Search: [Insight Advisor Search](#glossary-3 "Glossary term") is available from Sheet in the app navigation menu. Insight Advisor Search creates visualizations based on natural language searches or [selections](#glossary-4 "Glossary term") of fields and master items. Insight Advisor Search can also generate [charts](#glossary-5 "Glossary term") of potential interest.
- Insight Advisor Analysis Types: [Insight Advisor Analysis Types](#glossary-6 "Glossary term") is available from Sheet in the app navigation menu. Insight Advisor Analysis Types allows you to select an analysis type and the data to include. Insight Advisor then generates charts based on your parameters.
- Insight Advisor Chat: [Insight Advisor Chat](#glossary-7 "Glossary term") is a chat-based interface for conversational analytics. Insight Advisor Chat enables you to make natural language searches from your [activity centers](#glossary-8 "Glossary term") to apps to which you have access. Insight Advisor Chat then returns relevant visualizations.
- Associative insights: [Associative insights](#glossary-9 "Glossary term") helps you uncover blind spots and reveal relationships you may have missed. Associative insights compares the contributions of your selections and excluded values against your [measures](#glossary-10 "Glossary term").
- Chart suggestions: Chart suggestions enable you to select data fields when editing a [sheet](#glossary-11 "Glossary term") and let Qlik Sense choose the [dimensions](#glossary-12 "Glossary term"), measures, and [visualization](#glossary-13 "Glossary term") types. The suggested [chart](#glossary-14 "Glossary term") adjusts itself based on your changes. You can customize a suggested visualization with a focused set of properties.
- Recommended associations: Insight Advisor can recommend associations between your data tables in the Associations view in [Data manager](#glossary-15 "Glossary term"). The Recommended associations panel lets you view and apply these recommendations.

This tutorial will focus on improving search-based analysis in Insight Advisor Search with business logic.

### Insight Advisor Search

Insight Advisor Search is available from Sheet in the app navigation menu in an app.  You can enter natural language searches in the search box, such as 'what is profit by employee for 2020'. If you click Insight Advisor, you can also select specific data assets. Insight Advisor then generates charts or finds matching charts in the app. If you are creating apps, Insight Advisor Search helps you making apps based on the questions you want answered. If you are using an app, Insight Advisor helps you find the right visualization to answer your question, either in the app or by creating it for you.

For example, you are interested in viewing some visualizations that show profit earned by each employee. Open the tutorial app in Qlik Sense. In Sheet, search for show profit by employee. Insight Advisor generates results.

Results for show profit by employee

![Insight results for 'show profit by employee'. There is a bar chart show shows the sum of Gross Profit by Employee ID, a table of values for employee ID and Gross Profit, and a combo chart that shows the contribution of employee ID to the sum of gross profit.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial_what-is-insight-advisor-saas-rev.png "Click to view full size")

You have one matching result, that shows the sum of Gross Profit by EmployeeID, and some additional results. You can add these charts to [sheets](#glossary-16 "Glossary term") in our app or monitor them in activity centers by right-clicking on them and selecting from the options.

While these results matched what we were looking for, the [fields](#glossary-17 "Glossary term") selected could be improved. In trying to pick a field to match employee from the data model, Insight Advisor selected EmployeeID. The field EmployeeName is more useful in analysis, however. The sum of Gross Profit in the chart is also for all time. While this is not wrong, you may want to see more recent data by default.

In Analysis properties, you can teach Insight Advisor that you prefer EmployeeName by selecting that dimensions. These precedents are learned on a user-by-user basis. An app developer, however, can create a model that shows Insight Advisor exactly how to interpret the data model and use the fields within it. This [logical model](#glossary-18 "Glossary term") is used by Insight Advisor for all users using the app. You can do this using business logic.

## Business logic

Business logic is an optional part of data preparation that defines the logical model used by some Insight Advisor features to interpret your data model. Business logic comprises two main features:

- Logical model: The data model of the app used when generating visualizations.
- Vocabulary: Alternative terms for natural language questions.

Insight Advisor uses business logic in the following Insight Advisor features:

- Insight Advisor Analysis Types
- Insight Advisor Search
- Insight Advisor Chat
- Associative insights

### Logical model

The logical model is the conceptual model Insight Advisor uses when creating visualizations. It is built from the data model of an app. Each app has a single logical model. Fields and master items are the core components of this model. They are organized into groups. Groups indicate a conceptual association or relationship between fields or master items. Once you define these, you can then specify other relationships and handling behavior. These include:

- Packages: Packages enables you to create collections of related groups. This prevents groups from being used together that are not in the same package.- Hierarchies: Hierarchies enables you to define drill-down analytical relationships between groups.
  - Calendar periods: Calendar periods enables you to create default periods of analysis for Insight Advisor.
  - Behaviors: Behaviors enables you to specify prefer or deny relationships between fields. Behaviors can also enforce required selections and default calendar periods.

### Vocabulary

Business logic [vocabulary](#glossary-19 "Glossary term") enables you to improve the success of natural language questions. With vocabulary, you can define terms and values that may be used in natural language questions that are not present in your data model. You can also set the analysis types to be used for questions containing specific terms. For example, you can use vocabulary to:

- Add alternative names for fields, master items, and values.

  For example, Earnings, Proceeds, and Revenue for the field Income.
- Define names for coded values.

  For example, names for medical classifications codes.
- Common acronyms and abbreviations not in the data.

  For example, yr for year or num for number.
- Define the Insight Advisor analysis type to be used with certain terms or questions.

  For example, setting it so the map distribution analysis type is always used by Insight Advisor when a question includes the term regional view.
- Add example questions to help guide app users with their analysis.

  For example, provide questions such as what are the sales for this quarter compared to last quarter.
