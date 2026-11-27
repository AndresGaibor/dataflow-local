---
title: "Working with applications in Qlik Answers"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/Applications/working-with-apps-in-qlik-answers.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers"]
---

# Working with applications in Qlik Answers

Applications allow Qlik Answers to provide responses from structured data sources. Applications can be added as a content source for assistants. Applications can also be individually made available for Qlik Answers.

Qlik Answers can also generate charts and sheets for the user, allowing for rapid creation of application content.

Information noteQlik Answers supports applications using Section Access and respects the Section Access rules of the application. When accessing applications, Qlik Answers uses the permissions of the user. It can only access content from a Section Access application to which the user has permission to access. Users cannot expand their visibility through natural language questions in Qlik Answers.

Qlik Answers indexes applications to create internal definitions of application data. These are then used to answer user questions and generate charts and sheets. Qlik Answers uses an indexing user to determine the content to access during the index:

- Standard applications use the following user when indexing:

  - Personal space: Application owner.
  - Shared space: Application owner.
  - Managed space: Space owner. If the space owner does not have access to the application, then the application owner is used.
- Section Access applications are indexed using the following users when indexing:

  - Shared space: Stored index user. If no stored index user is available, the application owner is used. The user should have ADMIN access.
  - Managed space: Stored index user. If no stored index user is available, the space owner is used. If no space owner is available, then the application owner is used. The user should have ADMIN access.

  For information about index users, see [*Using Section Access and Qlik Answers*](../../Scripting/Security/manage-security-with-section-access.htm#Using).

Information noteFor Section Access applications, regardless of the indexing user, the data provided to end users is still controlled by the section access limitation.

Applications are indexed when added to an assistant or when made available for Qlik Answers. They are reindexed with every reload.

Qlik Answers uses the following to understand application data:

- The data model

  The fields and data model of the application are the primary information used by Qlik Answers.
- Logical model

  The logical model created by business logic is used by Qlik Answers, but only the information in Overview and Fields and master items.

  For more information, see [*Optimizing your application for Qlik Answers with business logic*](../BusinessLogicAI/business_logic-qlik-answers.htm).

  Fields hidden in the logical model and ungrouped items are not used by Qlik Answers.
- Master items

  Qlik Answers puts a priority on the use of master dimensions and measures when indexing the data model, as they are user-created.
- Qlik Answers-generated field descriptions

  When Qlik Answers indexes an application, it automatically generates descriptions for all fields and master items in the data model. These AI-generated descriptions provide semantic context that helps Qlik Answers understand field meanings and select appropriate metrics. You can review and refine these descriptions in Semantic understanding.

  For more information, see [*Managing Qlik Answers-generated field and master item descriptions with Semantic understanding*](../BusinessLogicAI/business-logic-semantic-understanding.htm).
- Master item descriptions

  User-provided descriptions in master items are used alongside AI-generated descriptions to provide additional context information for fields and their use.
- Business logic synonyms

  Terms added as synonyms are used to provide alternative terminology for user questions.
- Business glossary terms

  Glossary term definitions and synonyms linked to master items are used for additional context.

  Information noteMaster items and their linked business glossary terms are evaluated at indexing time. If a glossary term's definition changes after the application has been indexed, Qlik Answers does not pick up that update automatically. Reindex the app for the change to take effect.

  For more information on how master item definitions and business glossary terms are used by Qlik Answers, see [*Combining master item descriptions and business glossary terms*](glossary-aware-master-items.htm).

To check how well your application is prepared for Qlik Answers, review its AI readiness score. For more information, see [*Understanding Qlik Answers AI readiness score*](../BusinessLogicAI/understanding-ai-readiness-score.htm). To view general best practices for preparing your applications for use with Qlik Answers, see [*Best practices for preparing applications for Qlik Answers*](best-practices-applications.htm).

Tip noteAfter an application is indexed, you can adjust the semantic understanding of your application's data in AI optimization. For more information, see [*Managing Qlik Answers-generated field and master item descriptions with Semantic understanding*](../BusinessLogicAI/business-logic-semantic-understanding.htm).

## Adding skills to an application

You can add skills to an application from the Skills tab in AI optimization. Skills teach Qlik Answers how to handle specific topics and tasks, drawing on that knowledge automatically when relevant. You can add a maximum of five skills to an application.

For more information, see [*Working with skills*](../Skills/working-with-skills.htm) and [*Adding skills to applications and assistants*](../Skills/adding-skills.htm).

## Making applications available for Qlik Answers

You can make individual applications available for Qlik Answers. Applications are available from Qlik Answers in Application analysis. Users will be able to use Qlik Answers with the application when they open Answers.

Applications available for Qlik Answers can also be added to assistants as a content source.

To make an application available for Qlik Answers, you need the Activate Qlik Answers for applications permission. For more information, see [*Qlik Answers access and permissions*](../qlik-answers-permissions.htm).

Do the following:

1. In your application, click ![More actions](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > Settings.
2. Click Capabilities.
3. Select Available in Qlik Answers.

   To view the indexing progress, click View progress.

### Creating the search index on reload

You can add the variable CreateSearchIndexOnReload so that a search index is created for Qlik Answers with the next reload.

If you do not add this variable, the first question with Qlik Answers using this application will take longer as Qlik Answers will create the search index while also answering the question.

Do the following:

1. In your application, open Data load editor.
2. Add the following to your load script: SET CreateSearchIndexOnReload = 1;
3. Click Load data.

## Adding applications to assistants

Applications made available for Qlik Answers can be added to assistants as a content source. Each assistant can have a maximum of five applications assigned to it. Before you add an application to an assistant, the application must be available to Qlik Answers and must finish indexing.

Assistants have a number of advantages when using applications as data sources:

- Customizable chat options: Assistants offer more options for customizing the agent chat experience.
- Feedback: Assistants allow you to review feedback from users chatting with your application.
- Combined data sources: You can use unstructured data sources from knowledge bases with the structured data source of your application. This allows the use of supplementary documentation to help explain and provide context to your applications.
- Embed in other webpages: Assistants can be embedded in other webpages, providing access to Qlik Answers agentic chat outside Qlik Cloud.

For more information about adding an application as content to an assistant, see [*Managing applications*](../Assistants/create-assistants.htm#Managing)

Do the following:

1. In an assistant, open the Content tab.
2. Click Add content > Add application.
3. Select an application and click Add.

## Scheduling indexing for applications

Applications are indexed after every reload. If your application's data sources are regularly updated and you want regular indexing, create a reload task to schedule the reload of your application data.

Information noteIndexing applications does not consume indexing capacity.

For more information, see [*Scheduling reloading application data*](../../Apps/reloading-apps-cloud-hub.htm#Scheduli).

## Reviewing AI readiness and customizing Qlik Answers settings

You can review your application's AI readiness score in the Overview tab of AI optimization. The score helps you understand how well your application is configured for Qlik Answers to interpret your data. For more information, see [*Viewing the overview of business logic for Qlik Answers*](../BusinessLogicAI/business-logic-overview-qlik-answers.htm).

You can customize your application's Qlik Answers experience with default questions and assistant behaviors in AI optimization from the navigation menu. For more information, see [*Configuring Qlik Answers behavior with business logic*](../BusinessLogicAI/business-logic-qlik-answers-settings.htm).

## Reviewing conversations with applications

You can review conversations Qlik Answers users have had with applications in Answers review portal in the Analytics activity center.

For more information, see [*Reviewing conversations from Qlik Answers agentic experiences*](../reviewing-with-answers-review-portal.htm).

Information noteTo access Answers review portal, you must have a custom role with the Agentic AI > Review agent and chat interactions permission set to Allowed. For more information about user permissions, see [*Default permissions and custom roles*](../../Admin/permissions-scopes.htm).

## Best practices for preparing applications for Qlik Answers

While any application can be used for Qlik Answers, time spent preparing the application for use with Qlik Answers improves the quality of responses.

Clarity and context are the most important factors for ensuring good results from Qlik Answers. Clarity makes it easy for Qlik Answers to understand the data in an application. Context helps Qlik Answers interpret and correctly use the data within an application. The following best practices for preparing an application help ensure clarity and context:

- Use unambiguous and descriptive field names
- Streamline your data model
- Check the data formats of fields
- Use master items
- Use business logic vocabulary to add terminology
- Remove unnecessary fields from your data model
- Review and refine AI-generated field descriptions

### Use unambiguous and descriptive field names

Your data model should use fields that are descriptive and unambiguous. Field names should:

- Clarify the business meaning of each field.
- Apply clear, business-aligned naming that outline differences or similarities to other fields.

Try doing the following to help make fields clear to Qlik Answers:

- Use full wording, such as Customer Name instead of CUST\_NM. This helps align fields with natural language questions.
- Provide contextual qualifiers in the field names to help disambiguate between fields. For example:
- Make locations clear. Use Customer City and Store City instead of two fields both named City.
- Make data/time clear. Use Order Date and Shipment Date instead of two fields both named Date.
- Try to indicate the role and type of the field. Incorporate words like count, total, amount, or percentage to clarify their aggregative nature. For example, Order Count. If your field names use Booleans, they should read as prepositions, such as by using prefixes such as is\_active or has\_churned.

### Review and refine AI-generated field descriptions

When Qlik Answers indexes your application, it automatically generates descriptions for all fields and master items. While Qlik Answers creates useful baseline descriptions, reviewing and refining these descriptions can significantly improve accuracy, especially for domain-specific or ambiguous fields.

You can view and edit AI-generated descriptions in Semantic understanding. Focus on refining descriptions for:

- Fields with technical or abbreviated names that may not be self-explanatory
- Fields that are frequently queried by users
- Fields with domain-specific meanings that an LLM might not interpret correctly
- Fields where users commonly ask questions using different terminology

For more information on managing field descriptions, see [*Managing Qlik Answers-generated field and master item descriptions with Semantic understanding*](../BusinessLogicAI/business-logic-semantic-understanding.htm). For best practices for writing semantic descriptions, see [*Writing semantic descriptions for Qlik Answers*](../best-practices-for-descriptions-semantic.htm).

Avoid using fields names that do the following:

- Use opaque codes or technical jargon.
- Use Flag or a bare adjective such as Active for a Boolean field as this can hinder the interpretation by Qlik Answers.
- Use ambiguous or generic nouns without context. A field called Amount, for example, does not communicate what it is an amount of. Multiple generic fields can make it hard for Qlik Answers to reliably map natural language queries to the correct field.
- Use cryptic abbreviations, such as cust\_no for customer number or txn for transaction. These make it more difficult for Qlik Answers to understand the field.

### Streamline your data model

Streamlining your data model by removing unnecessary fields produces more accurate, predictable answers from Qlik Answers. A curated selection of fields reduces the chances of incorrect field selection or confusion from Qlik Answers. Streamlined data models are also faster to index. To streamline your data model:

- Hide technical fields.
- Consolidate redundant or near-duplicate fields into a single authoritative version.

#### Hide technical fields

Your data model should present Qlik Answers with fields that contain real analytic value. Avoid including technical fields that do not contribute to Qlik Answers understanding the application. Technical fields contain information such as:

- IDs
- Keys
- Load timestamps
- Staging columns

You can remove unnecessary fields by hiding them. Hidden fields are still available for script logic or internal calculations, but are excluded from Qlik Answers analysis.

- In load script or Data manager, add a % prefix in their name (for example, %Discount2)
- In the logical model in business logic, set their visibility to Hidden.

  For more information, see [*Visibility*](../BusinessLogicAI/business-logic-fields-master-items-qlik-answers.htm#Visibility).

#### Consolidate and rename fields

You should consolidate redundant or near-duplicate fields into a single authoritative version. Ambiguous fields make it difficult for Qlik Answers to interpret data correctly.

Rename or consolidate fields to make the data model as clear as possible for Qlik Answers to understand.

#### Example: Streamlining the data model by fixing ambiguous fields

Consider the following field names from a data model:

- Discount\_Amount
- Discount\_Value
- Discount1
- Discount2

These field names create a number of issues for Qlik Answers when it tries to interpret them:

- Multiple fields compete for the term discount, creating ambiguity for Qlik Answers.
- Numeric suffixes (1, 2) and vague field names provide no clear business meaning.
- Mixed naming conventions reduce clarity.

To fix these issues, the fields should be renamed when preparing the application for use with Qlik Answers. If the fields represent different concepts, they should be renamed to be clearer to their use and purpose. For example:

- Product Discount
- Promotional Discount
- Coupon Discount
- Loyalty Discount

If they represent the same concept, they should be consolidated into a single authoritative field, such as Discount Amount. If any of these fields are technical or legacy, they should be hidden.

### Format data/time fields loaded as plain text

Some fields contain date/time information, but are loaded as plain text in the data model. As they are not classified as date/time fields, but rather text fields, they will not be used correctly in Qlik Answers analyses as they will not be treated as true date fields.

If a field containing date/time information is tagged or stored as text, convert it to the proper format during the load, either with tools in Data manager or with date functions in the load script. This ensures that:

- The field is recognized as containing dates.
- The auto-calendar generation works.
- Time-based questions from users map correctly to the data/time fields.
- Sorting and filtering behave correctly.

### Use master items

Master items improve the ability of Qlik Answers to interpret application data. When interpreting questions, Qlik Answers weighs master items more heavily than fields in the data model as they are user-created. They are important because a user thought they were important enough to create them.

Master items add clarity and reduce ambiguity by creating a single, trusted version of each important metric or field in a data model. This also helps keep similar answers aligned across users. When someone asks about Profit margin and there is a corresponding master measure, the answer is based on the same definition, no matter who asks or who the question is phrased.

One of the most important elements of master items are descriptions. Descriptions are used by Qlik Answers to provide context for interpreting master items. Strong descriptions in master items clearly explain:

- Intent
- Meaning
- Business context

Master item descriptions make it easier for Qlik Answers to understand a master dimension or measure and pick the correct metric, even if users ask in an unexpected way.

For additional best practices for master items and Qlik Answers, see [*Writing semantic descriptions for Qlik Answers*](../best-practices-for-descriptions-semantic.htm).

Example: Useful master item description

Master measure: Customer Acquisition Cost

Description: Average cost to acquire a new customer. Calculated as total marketing and sales spend divided by the number of newly acquired customers. Excludes retention or renewal spend. Also known as CAC.

### Use business logic synonyms to add value

Business logic synonyms help you to refine how Qlik Answers interprets terminology. While Qlik Answers understands common business language, your data model may include terminology that a LLM would not naturally recognize or interpret correctly. Synonyms help Qlik Answers understand the terminology unique to your organization's data. The following categories of terms benefit from adding synonyms:

- Organization-specific jargon or acronyms
- Internal KPI nicknames
- Product or process codes that double as business terms
- Metrics that appear similar but have distinct internal definitions
- Domain-specific language not widely used outside your industry

Try to avoid synonyms that do the following:

- Add ambiguity. Including top or bottom, for example, can cause issues as they are not clear. For example, 0 could mean the top 5, the top 10%, top by revenue or number of deals.

  Adding synonyms that duplicate values from fields can also add ambiguity.
- Duplicate vocabulary for the same terms, for example, adding the synonym sales to two separate fields.
- Include stop words, as they can cause questions to be disallowed.

To learn more, see [*Adding synonyms for Qlik Answers*](../BusinessLogicAI/business-logic-synonyms-qlik-answers.htm).
