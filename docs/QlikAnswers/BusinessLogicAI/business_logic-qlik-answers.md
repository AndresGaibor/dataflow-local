---
title: "Optimizing your application for Qlik Answers with business logic"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/BusinessLogicAI/business_logic-qlik-answers.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Working with applications in Qlik Answers"]
---

# Optimizing your application for Qlik Answers with business logic

Business logic allows you to customize how Qlik Answers interprets your application data when generating analysis from queries. Business logic is automatically available when you activate an application for Qlik Answers.

Business logic represents the semantic model built on top of your application's data model. The data model provides the fields and data structure, while the semantic model organizes those fields and master items so Qlik Answers knows how they should be used. It also allows you to edit the semantic understanding Qlik Answers generates for its own use. You can add [vocabulary](#glossary-1 "Glossary term") to your business logic that helps Qlik Answers handle alternate terminology users might use when using Qlik Answers with your application.

You can customize the following areas of [business logic](#glossary-2 "Glossary term"):

- Overview: Review the application's AI readiness for Qlik Answers, customize the Qlik Answers-generated application description, and resync the application's data to business logic.

  [*Viewing the overview of business logic for Qlik Answers*](business-logic-overview-qlik-answers.htm)
- Fields and master items: Customize the fields, master items, and groups used in the logical model.

  [*Defining fields and master items for Qlik Answers*](business-logic-fields-master-items-qlik-answers.htm)
- Semantic understanding: Customize the semantic understanding of the fields and master items in the application used by Qlik Answers.

  [*Managing Qlik Answers-generated field and master item descriptions with Semantic understanding*](business-logic-semantic-understanding.htm)
- Synonyms: Synonyms allow you to add alternate terms.

  [*Adding synonyms for Qlik Answers*](business-logic-synonyms-qlik-answers.htm)
- Skills: Add skills that teach Qlik Answers how to handle specific topics and tasks.

  [*Adding skills to applications and assistants*](../Skills/adding-skills.htm)
- Settings: Customize additional AI options for Qlik Answers.

  [*Configuring Qlik Answers behavior with business logic*](business-logic-qlik-answers-settings.htm)

Business logic is available in the application navigation menu in AI optimization.

To see which parts of your application to optimize, review its AI readiness score. The score highlights suggestions you can address using the business logic tools, such as grouping fields and master items or refining descriptions. For more information, see [*Understanding Qlik Answers AI readiness score*](understanding-ai-readiness-score.htm).

Information note

Only the application owner or space members with Can edit data in applications can customize an application's logical model and vocabulary. For more information on co-development, see [*Co-developing business logic in shared spaces*](../../BusinessLogic/business-logic-codevelopment.htm).
