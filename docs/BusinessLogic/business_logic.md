---
title: "Customizing logical models for Insight Advisor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/BusinessLogic/business_logic.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Managing your data"]
---

# Customizing logical models for Insight Advisor

Business logic enables you to customize how Insight Advisor interprets your application data when generating analysis from queries.

Business logic defines how Insight Advisor interprets your data and handles alternative terms for values in your data model with:

- Insight Advisor Search
- Insight Advisor Analysis Types
- Insight Advisor Chat
- Associative insights

Tip noteFor information on business logic and Qlik Answers, see [*Optimizing your application for Qlik Answers with business logic*](../QlikAnswers/BusinessLogicAI/business_logic-qlik-answers.htm).

Insight Advisor relies on the Qlik cognitive engine and learned precedents to understand the relationships and uses of fields in your data model. You can optionally customize the [logical model](#glossary-1 "Glossary term") used by Insight Advisor for an application. You can add [vocabulary](#glossary-2 "Glossary term") to your business logic that helps Insight Advisor handle alternate terminology users might use when querying Insight Advisor.

You can customize the following areas of [business logic](#glossary-3 "Glossary term") in Qlik Sense:

- Logical model: Customize the fields and groups used in the model, create packages, define [field](#glossary-4 "Glossary term") hierarchies, and set behavior.

  [*Building logical models for Insight Advisor with Business logic*](business-logic-logical-models.htm)
- Vocabulary: Add synonyms, custom analyses, and example questions to expand user options when using natural language questions with Insight Advisor.

  [*Creating vocabularies for Insight Advisor*](business-logic-vocabulary.htm)

Business logic options are available in the application navigation menu.

Information note

Only the application owner or space members with Can edit data in applications can customize an application's logical model and vocabulary. For more information on co-development, see [*Co-developing business logic in shared spaces*](business-logic-codevelopment.htm).

Related learning:

- [Using Insights to Create Visualizations](/lnk/Use-Insights-Create-Visualizations_QS)
