---
title: "Adding synonyms to Insight Advisor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/BusinessLogic/business-logic-vocabulary-synonyms.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Managing your data", "Customizing logical models for Insight Advisor", "Creating vocabularies for Insight Advisor"]
---

# Adding synonyms to Insight Advisor

You can create vocabularies for [Insight Advisor](#glossary-0 "Glossary term"). This enables you to define terms and values that may be used in questions that are not present in your data model.

Information note

If you have Qlik Answers, synonyms can also be used to add terms for Qlik Answers. For information, see [*Adding synonyms for Qlik Answers*](../QlikAnswers/BusinessLogicAI/business-logic-synonyms-qlik-answers.htm).

You can create vocabularies in Vocabulary under Business logic in the application navigation menu.
Vocabularies help improve the success of natural language queries. For example, you can use vocabularies to define:

- Alternative names or synonyms for fields, master items, and values.

  For example, Earnings, Proceeds, and Revenue for the [field](#glossary-1 "Glossary term") Income.
- Names for coded values

  For example, names for medical classifications codes.
- Names for groups of values from a field

  For example, defining named age ranges for a field containing ages.
- Common acronyms and abbreviations not in the data.

  For example, yr for year or num for number.

When you create a [vocabulary](#glossary-2 "Glossary term"), you define the terms associated to that vocabulary. You then associate the terms to fields and master items in your application. Optionally, terms can be associated to individual values from the selected fields and master items. The following conditions are available when defining terms for values from fields:

- Greater than
- Greater than or equal to
- Less than
- Less than or equal to
- In
- Not in
- In range

Information noteThe availability of conditions for fields varies depending on the values in the fields.

Vocabularies are created by language for an application. Each language's vocabulary is separate.

Information note

The following languages are supported for vocabularies:

- English
- Dutch
- French
- German
- Italian
- Polish
- Portuguese
- Russian
- Spanish
- Swedish

## Adding terms

Do the following:

1. In an application, open the application navigation menu and select Vocabulary.
2. Select a language from the language drop-down.
3. Click Create terms.
4. Enter terms for the vocabulary.
5. Select the field or [master item](#glossary-4 "Glossary term") to which the vocabulary applies.
6. Optionally, select a condition and the values to which the condition applies.
7. Click Create.

## Importing terms

You can upload terms using a XLSX file. The XSLX file requires the use of specific headings and values:

- Field: The corresponding field from the application data.
- Locale: The language for the term. The following options are available:

  - En: English
  - De: German
  - Es: Spanish
  - Fr: French
  - It: Italian
  - Ja: Japanese
  - Nl: Dutch
  - Pl: Polish
  - Pt: Portuguese
  - Ru: Russian
  - Sv: Swedish
- Terms: The terms for the synonym. Separate terms with ||. For example, clients||customers||users.
- Condition Type: Optionally, include the type of condition for the values to which the terms apply.

  The available condition types vary depending on the type of values in the field.

  Text values:

  - In: The field values to which the term applies. Separate multiple values with a comma.
  - NotIn: The field values to which the term does not apply. Separate multiple values with a comma.

  Numeric values:

  - >: Field values greater than the specified number.
  - >=: Field values equal to or greater than the specified number.
  - <: Field values less than the specified number.
  - <=: Field values less than or equal to the specified number.
  - InRange: Field values in the specified range. Separate the range values with ||. For example, 0||1000

  Information note

  Fields containing dates do not support conditions.
- Condition Value: Optionally, enter the condition values for which the terms apply.
- Master Item: If the field is a master item, enter True.

A sample XSLX file with the headings formatted is available [here](https://cdn.qlikcloud.com/qmfe/assets/sense-client/vocabulary/synonym-bulk-import/file_structure_template_v1.xlsx).

Do the following:

1. In an application, open the application navigation menu and select Vocabulary.
2. Click Import.
3. Select your import file and click Import.
4. If there are any issues with your import, review the warnings.
5. Click Finish.

## Limitations

Synonyms have the following limitations:

- Master items and temporal fields do not support conditions.
