---
title: "Best practices for preparing applications for Qlik Answers"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/Applications/best-practices-applications.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers"]
---

# Best practices for preparing applications for Qlik Answers

While any application can be used for Qlik Answers, time spent preparing the application for use with Qlik Answers improves the quality of responses.

Clarity and context are the most important factors for ensuring good results from Qlik Answers. Clarity makes it easy for Qlik Answers to understand the data in an application. Context helps Qlik Answers interpret and correctly use the data within an application. The following best practices for preparing an application help ensure clarity and context:

- Use unambiguous and descriptive field names
- Streamline your data model
- Check the data formats of fields
- Use master items
- Use business logic vocabulary to add terminology
- Remove unnecessary fields from your data model

To check whether you have applied these best practices, review your application's AI readiness score. The score highlights specific fields, master items, and metadata that you can improve. For more information, see [*Understanding Qlik Answers AI readiness score*](../BusinessLogicAI/understanding-ai-readiness-score.htm).

## Use unambiguous and descriptive field names

Your data model should use fields that are descriptive and unambiguous. Field names should:

- Clarify the business meaning of each field.
- Apply clear, business-aligned naming that outline differences or similarities to other fields.

The following best practices help clarify fields and their uses:

- Use full wording, such as Customer Name instead of CUST\_NM. This helps align fields with natural language questions.
- Provide contextual qualifiers in the field names to help disambiguate between fields. For example:
- Make locations clear. Use Customer City and Store City instead of two fields both named City.
- Make data/time clear. Use Order Date and Shipment Date instead of two fields both named Date.
- Try to indicate the role and type of the field. Incorporate words like count, total, amount, or percentage to clarify their aggregative nature. For example, Order Count. If your field names use Boolean values, they should read as prepositions, such as by using prefixes such as is\_active or has\_churned.
- For key fields, prefix them with context. For example, customer\_id and order\_id is preferable to something like a generic field such as ID or cust\_ref.

Avoid using fields names that do the following:

- Use opaque codes or technical jargon.
- Use Flag or a bare adjective such as Active for a Boolean field as this can hinder the interpretation of the field.
- Use ambiguous or generic nouns without context. A field called Amount, for example, does not communicate what it is an amount of. Multiple generic fields can make it hard to reliably map natural language queries to the correct field.
- Use cryptic abbreviations, such as cust\_no for customer number or txn for transaction. These make it more difficult to understand the field.

## Streamline your data model

Streamlining your data model by removing unnecessary fields produces more accurate, predictable answers. A curated selection of fields reduces the chances of incorrect field selection or confusion. Streamlined data models are also faster to index. To streamline your data model:

- Hide technical fields.
- Consolidate redundant or near-duplicate fields into a single authoritative version.

### Hide technical fields

Your data model should present Qlik Answers with fields that contain real analytic value. Avoid including technical fields that do not contribute to Qlik Answers understanding the application. Technical fields contain information such as:

- IDs
- Keys
- Load timestamps
- Staging columns

You can remove unnecessary fields by hiding them. Hidden fields are still available for script logic or internal calculations, but are excluded from Qlik Answers analysis.

- In load script or Data manager, add a % prefix in their name (for example, %Discount2)
- In the logical model in business logic, set their visibility to Hidden.

  For more information, see [*Visibility*](../BusinessLogicAI/business-logic-fields-master-items-qlik-answers.htm#Visibility).

### Consolidate and rename fields

Consolidate redundant or near-duplicate fields into a single authoritative version. Ambiguous fields make it difficult to interpret data correctly.

Rename or consolidate fields to make the data model as clear as possible to understand.

### Example: Streamlining the data model by fixing ambiguous fields

Consider the following field names from a data model:

- Discount\_Amount
- Discount\_Value
- Discount1
- Discount2

These field names create a number of issues for Qlik Answers when it tries to interpret them:

- Multiple fields compete for the term discount, creating ambiguity for Qlik Answers.
- Numeric suffixes (1, 2) and vague field names provide no clear business meaning.
- Mixed naming conventions reduce clarity.

To fix these issues, the fields should be renamed when preparing the application for use with Qlik Answers. If the fields represent different concepts, rename them to clearly indicate their use and purpose. For example:

- Product Discount
- Promotional Discount
- Coupon Discount
- Loyalty Discount

If they represent the same concept, they should be consolidated into a single authoritative field, such as Discount Amount. If any of these fields are technical or legacy, they should be hidden.

## Format data/time fields loaded as plain text

Some fields contain date/time information, but are loaded as plain text in the data model. As they are not classified as date/time fields, but rather text fields, they will not be used correctly in Qlik Answers analyses as they will not be treated as true date fields.

If a field containing date/time information is tagged or stored as text, convert it to the proper format during the load, either with tools in Data manager or with date functions in the load script. This ensures that:

- The field is recognized as containing dates.
- The auto-calendar generation works.
- Time-based questions from users map correctly to the data/time fields.
- Sorting and filtering behave correctly.

## Use master items

Master items improve the ability of Qlik Answers to interpret application data. When interpreting questions, Qlik Answers weighs master items more heavily than fields in the data model as they are user-created. Master items help Qlik Answers interpret application data more accurately. When processing questions, Qlik Answers gives greater weight to master items than to raw fields in the data model, because master items represent user defined semantics and business intent. This allows Qlik Answers to prioritize curated definitions over underlying technical fields.

Master items add clarity and reduce ambiguity by creating a single, trusted version of each important metric or field in a data model. This also helps keep similar answers aligned across users. When someone asks about Profit margin and there is a corresponding master measure, the answer is based on the same definition, no matter who asks or how the question is phrased.

One of the most important elements of master items are descriptions. Master item descriptions are used by Qlik Answers to provide context for interpreting master items. When an application is indexed, Qlik Answers also generates AI-based descriptions for all fields and master items, which you can review and refine in Semantic understanding. Strong descriptions in master items clearly explain:

- Intent
- Meaning
- Business context

Master item descriptions make it easier for Qlik Answers to understand a master dimension or measure and pick the correct metric, even if users ask in an unexpected way.

For additional best practices for master items and Qlik Answers, see [*Writing semantic descriptions for Qlik Answers*](../best-practices-for-descriptions-semantic.htm).

Example: Useful master item description

Master measure: Customer Acquisition Cost

Description: Average cost to acquire a new customer. Calculated as total marketing and sales spend divided by the number of newly acquired customers. Excludes retention or renewal spend. Also known as CAC.

Information note

In addition to manually created master item descriptions, Qlik Answers automatically generates descriptions for all fields and master items when indexing your application. You can review and refine these AI-generated descriptions in Semantic understanding. For more information, see [*Managing Qlik Answers-generated field and master item descriptions with Semantic understanding*](../BusinessLogicAI/business-logic-semantic-understanding.htm).

## Use business logic synonyms to add value

Business logic synonyms help you to refine how Qlik Answers interprets terminology. While Qlik Answers understands common business language, your data model may include terminology that a LLM would not naturally recognize or interpret correctly. Synonyms help Qlik Answers understand the terminology unique to your organization's data. The following categories of terms benefit from adding synonyms:

- Organization-specific jargon or acronyms
- Internal KPI nicknames
- Product or process codes that double as business terms
- Metrics that appear similar but have distinct internal definitions
- Domain-specific language not widely used outside your industry

Try to avoid synonyms that do the following:

- Include terms such as top or bottom, as they are often underspecified and can be interpreted in multiple ways. For example, top 5 could refer to top by revenue, number of deals, percentage, or absolute rank. Using more precise synonyms helps ensure consistent interpretation.

  Adding synonyms that duplicate values from fields can also add ambiguity.
- Duplicate existing field values, as this can introduce ambiguity.
- Assign the same synonym to multiple fields, such as using sales for two different measures. This makes it unclear which field should be used.
- Include stop words, as they are ignored during question processing and may prevent questions from being accepted.

To learn more, see [*Adding synonyms for Qlik Answers*](../BusinessLogicAI/business-logic-synonyms-qlik-answers.htm).
