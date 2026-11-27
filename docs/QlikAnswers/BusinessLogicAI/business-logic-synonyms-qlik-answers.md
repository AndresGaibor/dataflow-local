---
title: "Adding synonyms for Qlik Answers"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/BusinessLogicAI/business-logic-synonyms-qlik-answers.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Working with applications in Qlik Answers", "Optimizing your application for Qlik Answers with business logic"]
---

# Adding synonyms for Qlik Answers

You can define synonym vocabularies for Qlik Answers. This enables you to define terms and values that may be used in questions that are not present in your data model and that Qlik Answers could not infer on its own.

You can create synonyms in AI optimization under Business logic in the application navigation menu.

When you create a [vocabulary](#glossary-0 "Glossary term"), you define the terms associated to that vocabulary. You then associate the terms to fields and master items in your application. Optionally, terms can be associated to individual values from the selected fields and master items.

Information note

Previously, synonyms supported conditions and single values or lists of values from a field or master item. These are no longer supported in the Qlik Answers single-agent experience.

If you have synonyms that use conditions, migrate these terms and their definitions to a skill. For more information, see:

- [*Migrating synonyms to skills*](#Migratin)
- [*Vocabulary and definitions*](../Skills/creating-custom-skills.htm#Vocabula)

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

## Best practices for defining synonyms

The Qlik Answers model understands general English vocabulary, common business terms, and standard synonym relationships (revenue and income, customer and client, etc). Synonym vocabulary closes the gap between the model's general knowledge and your application's specific vocabulary.

Synonyms are best used to define:

- Abbreviations and acronyms specific to your organization, not industry-standard ones the model would already know, such as

  - Internal codes
  - Ticket prefixes
  - System shorthand

  For example, you could give the dimension value REG-APAC-01 the synonyms Asia-Pacific and APAC as internal region codes can be opaque without mapping.
- Legacy or renamed field names when that users may still use when asking questions.
- Regional or team-specific jargon, where different parts of the business use different terms for the same field. For example, renewal rate versus retention.

  For example, the term tier 1 account can be given the synonyms top account, key account, or strategic account if that how the business actually refers to it.
- Ambiguous internal shorthand that has more than one plausible meaning and needs an explicit mapping to resolve correctly in the context of a specific application. For example, an abbreviation that could refer to a person's initials or a unit of measurement.

  For example, the field CUST\_REV\_TYD can be clarified with the synonyms customer revenue, revenue, and YTD revenue.

When defining synonyms, avoid making terms the model already can resolve correctly without help. These entries add overhead without benefit, and if they become inaccurate, they can steer the model towards the wrong field. The following are examples of bad synonyms:

- The field Revenue with the synonyms money, income, and sales.
- The field Customer with the synonyms client and buyer.
- The field Date with the synonym when and time.

## Adding terms

Do the following:

1. In an application, open the application navigation menu and select AI Optimization
2. Click Synonyms.
3. Select a language from the language drop-down.
4. Click Create terms.
5. Enter terms for the vocabulary.
6. Select the field or [master item](#glossary-2 "Glossary term") to which the vocabulary applies.
7. Click Create.

## Importing terms

You can upload terms using a XLSX file. The XLSX file requires the use of specific headings and values:

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
- Master Item: If the field is a master item, enter True.

A sample XLSX file with the headings formatted is available [here](https://cdn.qlikcloud.com/qmfe/assets/sense-client/vocabulary/synonym-bulk-import/file_structure_template_v1.xlsx).

Do the following:

1. In an application, open the application navigation menu and select Vocabulary.
2. Click Import.
3. Select your import file and click Import.
4. If there are any issues with your import, review the warnings.
5. Click Finish.

## Migrating synonyms to skills

The Qlik Answers single-agent experience does not support conditions for synonyms. If you have synonyms that use conditions, add vocabulary skills to your application that define the terms and their conditions.

Template skills are available for defining vocabulary:

- Synonyms to skill

  For migrating entries from Synonyms, including conditions. Use one line per meaning, include every term in the skill description, and label words in other languages with the language in brackets.

  [synonyms-terms-template.md](/en-US/cloud-services/tutorials/synonyms-terms-template.md)
- Synonyms for field and master item names

  For entries that define a field or master item name. These entries are still supported on the Synonyms tab. Use this template if you want to keep all your terms in one place as skills.

  [synonyms-names-template.md](/en-US/cloud-services/tutorials/synonyms-names-template.md)
- Synonyms for terms with conditions and thresholds

  For entries with a rule or conditions such as:

  - Greater or lesser than
  - Ranges
  - A list of field values
  - Not in

  [synonyms-conditions-template.md](/en-US/cloud-services/tutorials/synonyms-conditions-template.md)
- Synonyms for terms in several languages

  For entries that define a term in more than one language. Keep every language in the same skill and label each word with the language.

  [synonyms-languages-template.md](/en-US/cloud-services/tutorials/synonyms-languages-template.md)

When preparing your synonyms in skills for Qlik Answers, keep the following in mind:

- Every term must be present in the skill description.

  Qlik Answers looks at the skill description when determining whether it should apply the skill. The terms must be in the description for Qlik Answers to know to use the skill. Descriptions have a limit of 1,024 characters, so for large sets of synonyms, you might need to use multiple skills.
- Applications can have a maximum of five skills.

  There is a limit of five skills per application for Qlik Answers. If you have a large terminology set, prioritize terms that use conditions or value lists, and leave synonyms for field names in Synonyms.
- Fields must be visible to Qlik Answers.

  If the field is present in the application data model, but is hidden in Fields and master items in AI optimization, the term for the field will not be used in the skill.
- Keep your old synonym entries.

  Entries in Synonyms can be used by other parts of applications. Keep the entries in Synonyms until you have verified that your skills work as expected.
- Skills provide guidance, but not security.

  Skills can steer answers, but they cannot hide data.

### Converting synonyms to skill entries

Use the following table as a guide when converting Synonyms tab entries to skill entries.

Synonym tab terms and example conversions in skills

| Entry on the Synonyms tab | Example line in a skill |
| --- | --- |
| Word for a field | pod: the Dealer field. |
| Word for a master item | HIM2: the master item Luxury Car Count. Use the master item as is; don't rebuild its formula. |
| Word with greater than or less than condition | expensive: Price greater than 60,000 (60,000 does not count). |
| Word with at least or at most condition | slow delivery: Time\_to\_Deliver\_Days 30 or more (30 counts). |
| Word with one value | canadian seafood: Brand = NovaFishCo. |
| Word with a list of values | Maritimes: Province is one of New Brunswick, Prince Edward Island, and Nova Scotia. |
| Word with a not-in list | Contiguous states: State is anything except Alaska and Hawaii. |
| Word with a range | budget: Price from 0 to 25,000. 0 is not included. 25,000 is included. |
| Word with the same meaning in several languages | premium (German teuer; Spanish caro; Swedish dyr). |

### Migration best practices

Use the following best practices to help move your synonyms over to a skill:

- Check the list against the application first.

  A misspelled field or value moves into the skill without any error. Fix the list, then convert.
- Move the terms with conditions first.

  Synonyms with conditions no longer work in Qlik Answers. Synonyms for field names work as expected, so they can remain in Synonyms or be migrated later.
- Use one line per meaning, not per word.

  Put all the words for one meaning on one line, and group by what the line defines, not by who wrote it or in which language.
- Use master item names.

  A skill must name the item rather than referencing an ID for the master item.
- Define what happens at the boundary of a condition.

  For conditions that define boundaries (for example, Greater than 60,000), state whether the ends of the range count.
- Label every word that is in another language.

  If your synonyms include words in other languages, put the languages in brackets beside the terms. When the same word means different things in two languages, keep two labeled lines. Do not merge them into a single line.
- Add guards for words that could be interpreted as field values.

  If you have terms that could be interpreted as field values, make clear that these are not field values. For example, suppose that you have defined the terms Black Friday and white-glove delivery. You also have the field Color, which has the values Black and White. For your terms, add This is not the Color field. If the user means the color, use Color.
- Keep the terms users really use.

  Every term takes room in the maximum character count. Remove rare variants of field synonyms before you drop a conditional synonym from your skill. Do not repeat a term in two skills.
- Split terms by group when they do not fit in a single skill.

  If your terms do not fit in a single skill, split them into multiple skills by logical group. Keep the naming pattern of the vocabulary skills the same.
- If the application or assistant already has a vocabulary skill, do not overwrite it.

  Add your terms in a new skill and list the words that appear in both. Where they might disagree, state which skill wins.
- Test your skills before removing terms from Synonyms.

  Test your migrated synonyms three times in each language, using a new chat each time. Ask follow-up questions, a question using numbers (for synonyms that define numbers or ranges), and a question that the vocabulary skill must not answer. Keep your synonyms on the Synonyms tab until the results match.
- After migrating vocabulary to skills, edit the terms only in skills.

  After migration, update only the skill. Updates to entries in Synonyms do not update the skill.

## Limitations

Synonyms have the following limitations:

- Master items and temporal fields do not support conditions.
