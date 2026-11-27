---
title: "Managing Qlik Answers -generated field and master item descriptions with Semantic understanding"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/BusinessLogicAI/business-logic-semantic-understanding.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Working with applications in Qlik Answers", "Optimizing your application for Qlik Answers with business logic"]
---

# Managing Qlik Answers-generated field and master item descriptions with Semantic understanding

When Qlik Answers indexes an application, it automatically generates semantic understanding for all fields and master items in the data model. You can review and refine this AI-generated semantic understanding in your logical model in Semantic understanding to improve how Qlik Answers interprets your data.

Semantic understanding provides Qlik Answers with semantic context about fields and master items, helping it to:

- Understand field meanings: Descriptions provide semantic context that helps Qlik Answers understand what each field represents.
- Select appropriate metrics: When users ask questions, Qlik Answers uses descriptions to choose the most relevant fields for the answer.
- Interpret natural language: Descriptions help map user terminology to technical field names in your data model.

Good semantic understanding makes it easier for Qlik Answers to understand a field or master item and pick the correct metric, even if users ask in an unexpected way.

## Semantic understanding

Qlik Answers draws on five inputs to generate semantic understanding for fields and master items:

- Field names: The underlying name of the field as it exists in the data, which is not always the same as the label you gave the master item.
- Master item names: The label set in the master item editor.
- Master item description: The user-defined description of the master item. When there is none, Qlik Answers proceeds without it.
- Expressions: The calculation or logic that actually produces the value.
- Linked terms: Any linked synonyms or business glossary terms.

Qlik Answers also reads the values behind the item, looking at its format, range, distribution, and common entries. It uses this to build a profile from them. The generated semantic understanding of the fields and master items is a combination of the five inputs and the profile.

Semantic understanding is descriptive metadata. It tells Qlik Answers what a field or master item represents, but not how Qlik Answers should act on it. The description is used to decide whether an item is relevant to a question, but does not control what Qlik Answers does with the field once it is selected.

## Navigating Semantic understanding

Semantic understanding displays a table with information about each field and master item in your data model:

- Name: The field or master item name.
- Type: Whether the item is a master dimension, master measure, or field. This column is only available when Order by type is turned off.
- Semantic understanding: The description currently used by Qlik Answers. This may be the AI-generated description or a custom description you have edited.

You can filter and sort the table to find specific fields:

- Search for fields and master items by clicking ![Filter](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_filter2.svg).
- Click column headers to sort the table.
- Select Order by type to group fields and master items by name or show them separately.

## Editing field semantic understanding

You can edit semantic understanding to provide more accurate or domain-specific context for Qlik Answers. When you edit semantic understanding, it becomes custom semantic understanding that is protected from automatic regeneration. Custom semantic understanding persists even when the app data is reloaded or reindexed.

Information notePublishing an app from a shared space to a managed space keeps your custom semantic understanding. Duplicating the app, or exporting and importing it (with or without data), does not. After a duplicate or an import, the new app shows Qlik Answers-generated descriptions and you must redo your edits. To keep descriptions across copies, write them in the master item description or the logical model, which travel with the app.

Do the following:

1. In the Semantic understanding table, locate the field or master item you want to edit.
2. Click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > Edit.
3. Modify the semantic understanding.
4. Click Update.

Your custom description is now used by Qlik Answers and will not be overwritten by automatic regeneration when the app is reloaded.

## Clearing custom semantic understanding

If you want to restore the original AI-generated description for a field that has a custom description, you can clear the custom semantic understanding.

Do the following:

1. In the Semantic understanding table, locate the field with the custom description.
2. Click ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > Clear edit.

The field now uses the original AI-generated description.

## Importing and exporting semantic understanding

You can import or export the semantic understanding for all fields and master items using an Excel file (.xls or .xlsx). You can use this to edit the descriptions in bulk and then import the file to update the semantic understanding for your application.

Semantic understanding that you import becomes custom semantic understanding that is protected from automatic regeneration, in the same way as descriptions you edit individually.

Tip note

You can download a template Excel file with examples.

### Exporting semantic understanding

Export the semantic understanding to an Excel file that you can edit outside Qlik Answers.

Do the following:

1. In Semantic understanding, click Export.
2. Save the Excel file.

The exported file contains the fields and master items and their current semantic understanding.

### Importing semantic understanding

After editing the descriptions in the exported Excel file, import the file to update the semantic understanding for all fields and master items at once.

Do the following:

1. In Semantic understanding, click Import.
2. Select the Excel file and click Load.
3. Review the imported descriptions for any issues and click Finish.

The semantic understanding for your fields and master items is updated with the descriptions from the file.

## Writing effective semantic understanding

When editing descriptions, follow these best practices to improve Qlik Answers accuracy:

- Focus on frequently queried fields: Prioritize editing descriptions for fields that users commonly ask about.
- Use domain-specific terminology: Include industry terms and organization-specific language that users might use when asking questions.
- Be concise but descriptive: Explain what the field represents and why it matters, without unnecessary detail.
- Include synonyms and alternative phrasings: Add terms users might use when referring to the field in different contexts.
- Clarify ambiguous fields: For technical or abbreviated field names, provide clear business context.

Information note

Do not add prompts or instructions to descriptions as Qlik Answers will ignore these.

For detailed guidance on writing effective descriptions, see [*Writing semantic descriptions for Qlik Answers*](../best-practices-for-descriptions-semantic.htm). The principles for writing master item descriptions apply equally to AI-generated field descriptions.

Example: Improving a field description

A field named RevRec has an AI-generated description:

RevRec - A date field

This is too generic. An improved custom description would be: Revenue recognition date - the accounting period when revenue is officially booked per GAAP standards. Used to determine when sales are recorded for financial reporting purposes.

The improved description includes:

- Full field meaning (revenue recognition)
- Business context (GAAP standards, financial reporting)
- Synonyms and usage (sales, recorded)
