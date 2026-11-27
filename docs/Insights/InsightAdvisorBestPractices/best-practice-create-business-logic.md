---
title: "Best practices for using business logic"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Insights/InsightAdvisorBestPractices/best-practice-create-business-logic.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating visualizations with Insight Advisor", "Insight Advisor best practices"]
---

# Best practices for using business logic

Learn how to create a useful vocabulary and logical model for application users. Creating a user-specific business logic allows users to quickly and effectively use your applications.

## What is business logic in Qlik Cloud?

Business logic defines how Insight Advisor interprets your data and handles alternative terms for values in your data model. There are two parts to Qlik Cloud's business logic: the logical model and the vocabulary.

### What is the logical model?

The logical model of an application is the conceptual model Insight Advisor uses when generating visualizations. It is built from the underlying data model of an application. Each application has a single logical model. Fields and master items are the core components of the logical model. They are organized into groups. Groups indicate a conceptual association or relationship between fields or master items. The logical model also contains information about possible relationships between groups.

The logical model directly influences how Insight Advisor functions. For example, when a user selects a field to show a trend analysis, Insight Advisor tries to find a date field that is part of a primary calendar group. If the field was Sales, Insight Advisor would prioritize a field like Order Date over the field Employee Birth Date.

Application developers can ensure a consistent experience for their users by creating a logical model during the development phase before releasing an application.

### What is the vocabulary?

You create vocabularies in Vocabulary under Business logic in the application navigation menu.
Vocabularies help improve the success of natural language questions. For example, you can use vocabulary to:

- Add alternative names for fields, master items, and values.
- Define names for coded values.
- Define the Insight Advisor analysis type to be used with certain terms or questions.
- Provide sample questions for users to ask.

## Creating example questions for users

You can create example questions to help guide your application's users with the kinds of questions they can ask Insight Advisor in an application. The questions should be relevant to the type of analysis that your application's users want to perform. Example questions help users understand the structure and input requirements for asking their own questions.

Your example questions should guide users to use direct and simple questions that can be easily recognized by Insight Advisor. Users should use industry standard terminology, although this is dependent on if you have added synonyms to the business logic.

For example, Insight Advisor does not recognize items that are not in the data model. If you ask, Show me the bids we won, Insight Advisor will not understand the term we won. Instead, you should ask Show me bids where, followed by the field that corresponds to winning is equal to true.

Tip noteYou can use features like vocabulary to connect phrases like we won to your underlying data. Insight Advisor can then understand those phrases.

See [*Adding example questions to Insight Advisor*](../../BusinessLogic/business-logic-vocabulary-questions.htm) for instructions on creating example questions.

## Creating synonyms for Insight Advisor

Many companies have their own terminology when it comes to measures like revenue, profitability, and even performance. You can add synonyms into your business logic vocabulary to allow users to ask questions using their own terminology. Adding custom terms to your vocabulary ensures that users who do not use the exact spelling of a field can still ask questions and use Insight Advisor.

Insight Advisor recognizes the measures, dimensions, and fields that are defined in your application. For example, if you ask, what are my sales, and your data model contains a measure named revenue, Insight Advisor will not know that these are synonyms. By adding sales as a synonym of the measure revenue, Insight Advisor will answer questions correctly. You can use business logic to connect these terms, as well as link any other terms.

See [*Adding synonyms to Insight Advisor*](../../BusinessLogic/business-logic-vocabulary-synonyms.htm) for instructions on creating synonyms.

## Linking terms with custom analysis

You can add custom analysis mapping so that certain terms or phrases return specific analyses in Insight Advisor. This can help provide your users with expected results when asking Insight Advisor questions.

For example, a general manager might prefer to see sales as always ranked among their sales representatives. You could link the term performance to always return a rank chart when used in a question.

See [*Adding custom analyses to Insight Advisor*](../../BusinessLogic/business-logic-vocabulary-custom-analysis.htm) for instructions on creating custom analyses.

## Managing new data in the logical model

If you add new data to your application after creating business logic, those items, fields, and measures will show up as ungrouped items in your logical model. Ungrouped items are not used by Insight Advisor. You must manually group them in the logical model to make them available in Insight Advisor.

Warning note You can click Reset to default to have business logic create a new default logical model including your new data. Clicking Reset to default removes any custom work you have done to the logical model, including any packages, hierarchies, or behaviors that you created.

## Learn more

- [*Tutorial – Customizing how Insight Advisor interprets data*](../../BusinessLogic/Tutorial/tutorial-customizing-insight-advisor.htm)
- [*Enabling a custom logical model*](../../BusinessLogic/Tutorial/tutorial-enabling-logical-model.htm)
- [*Creating vocabularies for Insight Advisor*](../../BusinessLogic/business-logic-vocabulary.htm)
