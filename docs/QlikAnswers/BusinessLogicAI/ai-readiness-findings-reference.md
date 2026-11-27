---
title: "Qlik Answers AI readiness suggestions summary"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/BusinessLogicAI/ai-readiness-findings-reference.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Working with applications in Qlik Answers", "Optimizing your application for Qlik Answers with business logic", "Viewing the overview of business logic for Qlik Answers"]
---

# Qlik Answers AI readiness suggestions summary

This reference describes the types of suggestions that appear in your AI readiness score. Each suggestion points to something in your application that makes it harder for the AI to pick the right field, link tables correctly, or calculate the right number.

## Working through the suggestions

This topic uses "the AI" for the language model that reads your app and builds the answer. Like any AI model, it only knows what the data model, field names, and descriptions tell it. The AI readiness suggestions help close those gaps.

A suggestion is not always a defect. Many of the patterns flagged here are standard Qlik modeling techniques that a developer added on purpose. For example:

- A what-if table
- A selector list
- A sort-order table,
- A helper flag

Those patterns work in sheets because the developer controls every chart expression. An AI model has no such context. It sees every visible field and tries to use it. For each suggestion, decide first whether the pattern is intentional. If it is, the fix is usually to hide it from Qlik Answers, not to rebuild it.

This is the recommended order for addressing suggestions:

1. Fix data model suggestions that change numbers:

   - Island tables
   - Fan traps
   - Chasm traps
   - Synthetic keys

   These cause wrong answers, not only unclear ones.
2. Hide noise:

   - Keys
   - Technical and helper fields
   - Synthetic fields
   - Free-text fields
3. Improve what remains visible:

   - Business names
   - Groups
   - Master item descriptions

Hiding a field from Qlik Answers does not remove it from the data model, does not change sheets or charts, and does not change how the field links tables.

The AI readiness score updates after you apply a change in AI optimization. Load script changes show in the score after the next reload.

## Suggestions ovewview

The following table lists the suggestions and whether you can fix them in AI optimization.

AI readiness suggestions

| Suggestion | Category | Actionable in AI optimization |
| --- | --- | --- |
| Island tables are not connected to the data model | Data model | Partly. Hide the table's fields now. Connect or remove the table in the load script. |
| Loosely coupled tables in the data model | Data model | No, it requires load script changes. |
| Chasm traps in the data model | Data model | No, it requires data model restructuring. |
| Table pairs at risk of fan traps | Data model | No, it requires data model restructuring. |
| Tables in the data model are not connected to each other | Data model | Partly. Hide the fields of tables that are not needed for questions. Linking tables requires load script changes. |
| Synthetic tables in the data model | Data model | Partly. Hide the synthetic fields now. Remove the synthetic keys in the load script. |
| Fields are not grouped | Fields | Yes, you can group the fields. |
| Master items are not grouped | Fields | Yes, you can group the master items. |
| Fields have technical names | Fields | Yes, you can create master items or hide the fields. |
| Key fields visible to Qlik Answers | Fields | Yes, you can hide the fields. Create a counting master item first if users ask "how many". |
| Fields with a single value | Fields | Yes, you can hide the fields. |
| Text fields with many distinct values | Fields | Yes, you can hide the fields. |
| Synthetic fields visible to Qlik Answers | Fields | Yes, you can hide the fields. |
| Fields are already covered by master items | Fields | Yes, you can hide the fields. |
| Fields have near-duplicate names | Fields | Yes, you can hide or rename the fields. |
| Master items have unclear names or no analytical value | Fields | Yes, you can rename or hide the master items. |
| Master items with invalid expressions | Fields | Yes, you can fix or hide the master items. |
| Master items have no description | Fields | Yes, you can apply descriptions suggested by Qlik Answers. |
| Data product master items have no description | Fields | No, it requires changes in the data product. |
| Data product master items have unclear names | Fields | No, it requires changes in the data product. |
| Data product master items have an invalid expression | Fields | No, it requires changes in the data product. |
| Flat tables in the data model | Metadata | Partly. Hide the table's fields now. Remove or remodel the table in the load script. |
| No date field for time-based questions | Metadata | No, it requires load script changes. |
| Expressions used in charts have no master item | Metadata | Yes, you can create master items. |
| Charts have invalid expressions | Metadata | No, it requires fixing the chart expression. |

## Data model suggestions

Data model suggestions identify structural issues in how tables, keys, and relationships are configured. They have the largest effect on answer accuracy, because a wrong link between tables produces a wrong number, not only an unclear answer. Most need load script changes. Where a pattern is intentional, hiding its fields in AI optimization is a safe interim step.

### Island tables are not connected to the data model

Why it matters

An island table has no links to the rest of the data model. The AI does not know the table is separate. If a question names a field from the island table, the AI can try to use it as a dimension next to a measure from the main model. Because the two are not linked, the result repeats the same total on every row or returns an unrelated value. For example, "Sales by Scenario" shows the full sales total for every scenario.

When an island table is intentional

Application developers often add island tables on purpose. Common reasons:

- What-if or scenario values used in variables, such as a growth rate slider.
- Selector lists that switch a chart's measure or dimension.
- Sort-order or display tables used only in chart properties.
- Helper values read in set analysis or in Only() expressions.

How to address

To address island tables:

- If the table is intentional, hide all of its fields from Qlik Answers. Sheets and charts keep working.
- If the the table should be part of the model, give it a field with the same name and values as a field in the related table in the load script, then reload.
- If the table is not used, remove it from the load script, or drop it with DROP TABLE at the end of the script.

Information note

Do not leave an island table visible to Qlik Answers. At minimum, hide its fields.

### Loosely coupled tables in the data model

Why it matters

A circular reference is a loop of links between three or more tables. It causes the analytics application to break the loop by marking one or more tables as loosely coupled. Selections and answers do not carry across the loosened link, so a question that spans it can return a total that ignores the filter.

How to address

Find the loosened link: the data model viewer shows it as a dashed line, and the reload log reports the circular reference. A developer can also set it on purpose with LOOSEN TABLE. Remove the circular reference by renaming or removing one of the shared fields in the load script, or by combining the tables that cause the loop into one table (concatenate) or a link table. Then reload the data.

### Chasm traps in the data model

Why it matters

A chasm trap forms when two fact tables, such as Sales and Returns, both link to the same dimension table, such as Customer, but not to each other. A question that combines both facts in one expression, such as Sum(Sales - Returns) by customer, can return wrong or incomplete results, because Qlik Answers calculates across rows that do not exist together. Rows in either fact table with no matching dimension value also drop out of the answer.

How to address

To address chasm traps:

- Define measures that aggregate each fact separately, for example Sum(Sales) - Sum(Returns), as master items. The AI then uses the correct form.
- Or concatenate the fact tables into one table with a type field, or build a link table.
- Map missing key values to an "Unknown" member in the dimension table so no fact rows drop out.

### Table pairs at risk of fan traps

Why it matters

The Qlik engine always aggregates a field over its own table, so a simple Sum(Freight) does not double count. The risk appears when a measure stored at a higher level is split by a dimension at a lower level. For example, freight is stored per order, and the question asks for freight by product. Each product line of the order shows the full order freight, and the lines add up to more than the total. Expressions that multiply fields from two tables, such as Sum(Quantity \* Price) with price on a different table, have the same risk.

How to address

To address fan traps:

- Store the measure at the level users will ask about, for example allocate order freight to order lines in the load script.
- Or create a master measure that states the level, for example Freight (order level), with a description that says it cannot be split by product.
- Keep fields used in one expression on the same table where you can.

### Tables in the data model are not connected to each other

Why it matters

Without key fields linking your tables, the AI can only work with one table at a time. It cannot answer questions that span multiple tables, and it can return misleading results if it combines fields from unlinked tables, as described for island tables.

Separate tables can be intentional, for example two subject areas kept in one app for convenience. In that case, hide the subject area that users do not ask about, or split the app.

How to address

Open the data model viewer and check which tables should be related. In the load script, give related tables a field with the same name and matching values, and reload. A common target is one fact table in the center, linked to dimension tables such as Customer, Product, and Date (a star schema).

### Synthetic tables in the data model

Why it matters

A synthetic table (shown as $Syn in Data model viewer) is created by analytic applications when two tables share more than one field. It can cause incorrect results in AI answers, because the link uses every shared field, including fields such as Date or Status that the developer never meant as keys.

A synthetic key is not always a problem. One deliberate synthetic key on a real composite key works. Several synthetic keys, or a synthetic key on fields like Date or Status, usually mean the tables are linked by accident.

How to address

To address synthetic tables in the data model:

- Rename fields that are shared by accident, for example LOAD Status AS OrderStatus, or use QUALIFY.
- For a real composite key, build one key field and keep it in both tables, for example AutoNumber(OrderID & '|' & LineNo) AS OrderLineKey. Then drop the separate fields from one of the tables.
- Until you change the script, hide the synthetic fields from Qlik Answers (see [*Synthetic fields visible to Qlik Answers*](#Syntheti)).

## Fields suggestions

Fields suggestions identify issues with how fields and master items are grouped, named, described, and exposed to Qlik Answers. Hiding affects Qlik Answers only. The field stays in the data model, keeps linking tables, and keeps working in sheets, charts, and master items.

### Fields are not grouped/Master items are not grouped

Why it matters

Without grouping, the AI treats fields as unrelated and can miss how they connect. This leads to less accurate interpretation. For example, grouping Customer Name, Customer City, and Customer Segment in the group Customer tells the AI that "customers in Berlin" refers to Customer City.

How to address

Click See details and select the ungrouped fields. Qlik Answers moves the selected fields into matching groups. You can also manage groups in Fields and master items. For more information, see [*Defining fields and master items for Qlik Answers*](business-logic-fields-master-items-qlik-answers.htm). Review the proposed groups before you apply them.

### Fields have technical names

Why it matters

The AI can fail to match fields with technical names to the business terms used in questions. A user asks for "customer name", and the field is called cust\_nm or KNA1\_NAME1.

Some technical fields are intentional: helper flags such as \_IsCurrentYear, keys, and fields used only inside expressions. Hide those rather than renaming them.

How to address

Click See details to review the affected fields. For each field, Qlik Answers recommends one of the following actions:

- Create a master item with a business-friendly name.
- Hide the field from Qlik Answers.

To fix the name at the source, rename it in the load script, for example LOAD cust\_nm AS [Customer Name]. Renaming a field in the script breaks chart expressions that use the old name.

### Key fields visible to Qlik Answers

Why it matters

The AI can use visible key fields in place of fields with business meaning. For example, it can group by CustomerID instead of Customer Name.

How to address

Click See details and select the key fields to hide.

Information noteBefore you hide a key, check whether users ask "how many" questions that depend on it. If you hide OrderID, create a master measure such as "Number of orders" with Count(distinct OrderID) first. Keep keys visible when users look them up by value, such as an order or invoice number.

### Fields with a single value

Why it matters

A field that holds the same value in every row cannot help the AI filter or group results.

Single value fields are common in reduced apps and in apps with Section Access, where each user sees one region or one currency. The value still matters as context. Put it in the app or master item descriptions, for example "All amounts are in EUR", before you hide the field.

How to address

Click See details and select the fields to hide.

### Text fields with many distinct values

Why it matters

Text fields with many distinct values add irrelevant matches to AI responses. Comments, descriptions, and addresses are typical examples.

How to address

Click See details and select the fields to hide.

Information noteDo not hide names that users search by, even when they have many values. Customer Name, Product Name, and Supplier Name often have thousands of values and are the fields users ask about most. Hide free-text fields; keep entity names.

### Synthetic fields visible to Qlik Answers

Why it matters

The AI can match visible synthetic fields to questions by mistake. Synthetic fields are the $Syn fields that analytic applications create for synthetic keys. They have no business meaning.

How to address

Click See details and select the synthetic fields to hide. To remove them from the model, see [*Synthetic tables in the data model*](#Syntheti2).

### Fields are already covered by master items

Why it matters

When a field has the same name as a master item, the AI sees the same thing twice. It might use the field instead of the master item.

How to address

Click See details and select the fields to hide. The master item keeps working after you hide the field.

### Fields have near-duplicate names

Why it matters

When a field is named almost the same as another field or master item, the AI cannot tell which one to use. This can lead to inconsistent results.

How to address

Click See details and select the fields to hide. If both items are needed and mean different things, such as Order Date and Ship Date, rename them so the difference is clear, and add descriptions.

### Master items have unclear names or no analytical value

Why it matters

The AI matches questions to master item names. Abbreviations such as YTD, LY, or Net, and names without the unit or currency, lead to the wrong item or a wrong reading of the result.

How to address

Click See details to review the affected master items. For each master item, Qlik Answers recommends one of the following actions:

- Rename the master item using the name suggested by Qlik Answers.
- Hide the master item from Qlik Answers.

Rename the master item using the name suggested by Qlik Answers, or hide the master item from Qlik Answers. Check that the suggested name keeps the meaning, for example that "Net sales" still says whether it is before or after returns.

### Master items with invalid expressions

Why it matters

A master item with an invalid expression returns errors when the AI uses it.

How to address

Fix the expression in the master item first. Sheets that use it are also broken. If you cannot fix it now, click See details and select the master items to hide.

### Master items have no description

Why it matters

The AI uses descriptions to decide which master item answers a question and how to explain the result. A description is where filters, currency, and fiscal periods belong.

How to address

Click See details and select the master items to which you want to apply the descriptions suggested by Qlik Answers.Review each suggested description before you apply it. Check that it states any filter in the expression, the currency or unit, and whether periods are calendar or fiscal.

### Data product master items (no description, unclear names, invalid expression)

Why it matters

Without a description, Qlik Answers relies on the master item name alone to understand what it means. This is unreliable for master items with similar names.

How to address

These master items come from a data product and cannot be edited in the application. Add descriptions to the master items in the data product. If you do not own the data product, ask its owner to make the change.

## Metadata suggestions

Metadata suggestions identify issues in your load script and charts that limit the business context available to Qlik Answers.

### Flat tables in the data model

Why it matters

A flat table holds facts and descriptive fields together in one wide table, so the same values repeat across many rows. The AI can find it hard to tell what one row represents, and what to count. Tables left over from loading, such as staging, audit, or log tables, are also flagged and add fields with no analytical value.

A wide table can be a deliberate choice for performance or simplicity. If its fields are clearly named and each row has a clear meaning, keep it and add descriptions.

How to address

Review the affected tables in your load script. Remove tables that are not needed for analysis, for example with DROP TABLE at the end of the script. Until you change the script, hide the fields of those tables from Qlik Answers.

### No date field for time-based questions

Why it matters

Without a recognized date or time field, the AI cannot answer questions about trends, changes over time, or specific periods.

A common cause is a date loaded as text, so it is not recognized as a date.

How to address

Add a date field or a master calendar in the load script. If the date is loaded as text, convert it, for example Date(Date#(OrderDate, 'YYYY-MM-DD')) AS OrderDate. If the application has several dates, such as order date and ship date, describe each one and state which date to use by default.

### Expressions used in charts have no master item

Why it matters

The AI can reuse calculations that exist as master items. A calculation that lives only inside a chart is invisible to it, so the AI writes its own version, which can differ from the one on the sheet.

How to address

Click See details and select the expressions from which to create master items with readable names. The expressions come from charts in public sheets. Add a description to each new master item.

### Charts have invalid expressions

Why it matters

A broken chart means the sheet shows no number for that calculation. Users who compare an answer from Qlik Answers with the sheet then have nothing to check it against.

How to address

Click See details to review the affected charts. Fix the invalid expressions in the charts.
