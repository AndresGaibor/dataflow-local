---
title: "Creating vocabularies for Insight Advisor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/BusinessLogic/business-logic-vocabulary.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Managing your data", "Customizing logical models for Insight Advisor"]
---

# Creating vocabularies for Insight Advisor

You can create vocabularies for [Insight Advisor](#glossary-0 "Glossary term"). This allows you to define synonyms for Insight Advisor and define analyses to be used with specific terms.

You create vocabularies in Vocabulary under Business logic in the application navigation menu.
Vocabularies help improve the success of natural language questions. For example, you can use [vocabulary](#glossary-1 "Glossary term") to:

- Add alternative names for fields, master items, and values.
- Define names for coded values.
- Define the Insight Advisor analysis type to be used with certain terms or questions.
- Provide sample questions for users to ask.

Vocabulary supports the following kinds of vocabulary:

- Synonyms: Synonyms allow you to add alternate terms.

  For more information, see [*Adding synonyms to Insight Advisor*](business-logic-vocabulary-synonyms.htm).
- Custom analysis: Custom analysis allow you to define what analyses should be used with select terms.

  For more information, see [*Adding custom analyses to Insight Advisor*](business-logic-vocabulary-custom-analysis.htm).
- Example questions: Add sample questions users can select to help guide analysis of your application.

  For more information, see [*Adding example questions to Insight Advisor*](business-logic-vocabulary-questions.htm).

## Limitations

Vocabularies have the following limitations:

- Vocabularies are not supported in [associative insights](#glossary-3 "Glossary term").
- Vocabularies do not support creating terms for fields classified as dates.
- The following words are reserved for use in Qlik Sense and cannot be used as a vocabulary term:

  - App
  - Application
  - Dimensions
  - Dim
  - Measure
  - Msr
- Insight Advisor does not lemmatize or stem vocabulary terms. For example, if the term is open, a question using opened or opening will not be treated as having entered open. Similarly, if the term was opened, open and opening would not be recognized as the term.
- If a vocabulary term also exists as a [field](#glossary-4 "Glossary term") value, and a question includes the field containing that value and the shared term, Insight Advisor won't use the vocabulary term and will uses the field value instead when processing the question as the question included the field.
