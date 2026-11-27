---
title: "Managing business glossaries with Qlik Answers"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/glossary-agent.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Using Qlik Answers and choosing your context"]
---

# Managing business glossaries with Qlik Answers

Build, edit, and explore business glossaries using natural language with the business glossary manager.

Business glossary manager in Qlik Answers

![Glossary manager](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_answers_context_glossary.png "Click to view full size")

Govnote-not-inNot supported in Qlik Cloud Government.

Govnote-not-inNot supported in Qlik Cloud Government - DoD.

## What the business glossary manager can do

The business glossary manager allows you to do the following:

- Search for and explore available glossaries and their content.
- Generate business glossaries automatically from applications and data products.
- Manage glossaries and their properties, performing actions such as editing, deleting, and moving between spaces.
- Manage glossary terms and categories, including management of links between glossaries, their terms, and other resources such as data products.

For specific workflows and example questions, see [*Workflows*](#Workflows).

## Before you begin

Prerequisites:

- Your [tenant](#glossary-0 "Glossary term") has cross-region inference turned on and is enabled for the agentic Qlik Answers experience.

  [*Enabling cross-region inference*](../Admin/cross-region-data-processing.htm)
- Your tenant and subscription have capacity for Qlik Answers.

  [*Qlik Answers capacity*](administering-qlik-answers.htm#Capacity)
- You have the required administrator-assigned permissions, as well as access to the required applications, datasets, data products, and glossaries.

  [*Permissions*](#Permissions)

## Chatting with the business glossary manager

Do the following:

1. In the top bar, click Qlik Answers.

   The Qlik Answers chat opens.
2. In the dropdown menu, select Glossary.

   Opening business glossary manager in Qlik Answers

   ![Selecting 'Glossary' context in chat](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_answers-context-selector-glossary.png "Click to view full size")
3. Select one of the available starter questions, or enter your own question.

   Information note

   Depending on your question, Qlik Answers may need to use a tool to generate the response, such as when updating a term. Qlik Answers asks for approval the first time it needs to use a tool. You can choose to approve it once, approve it for all future requests, or deny the use of the tool.

   For more information, see [*Managing Qlik Answers tools*](qlik-answers-tools.htm).

Information note

If Glossary is not available, verify tenant enablement, user permissions, and available Qlik Answers capacity.

## Workflows

These workflows contain helpful example questions to get you started working with the business glossary manager.

### Glossary search and exploration

Example questions for glossary search and exploration

| Action | Example questions | Notes |
| --- | --- | --- |
| Search | - Show me available glossaries - List glossaries | - |
| Exploration | - Show me details for glossary <glossary name> - Help me understand what a term means based on its name. | - |

### Glossary generation

You can generate glossaries from applications, data products, and datasets.

- Terms and categories are created unless you create a blank glossary.
- When you create a glossary from an applications, terms are extracted from application dimensions and measures.
- When you create a glossary based on a data product, you are prompted to link the glossary to the data product.

Example questions for glossary generation

| Action | Example questions | Notes |
| --- | --- | --- |
| Glossary generation—resource not specified | - Help me create a glossary for an application or a data product. | - |
| Glossary generation—from application | - Create a glossary based on the <application name> application | - |
| Glossary generation—from data product | - Create a glossary based on data product <data product name> | - |
| Glossary generation—blank glossary | - Create a glossary named <glossary name> in my personal space | - |

### Glossary management

Example questions for glossary management

| Action | Example questions | Notes |
| --- | --- | --- |
| Glossary deletion | - Delete glossary <glossary name> - Delete this glossary | If you have a glossary open, you can often ask questions without needing to reference the glossary name. |
| Glossary update | - Replace the current glossary overview | If you have a glossary open, you can often ask questions without needing to reference the glossary name. |

### Linking, term, and category management

Example questions for glossary linking, term, and category management

| Action | Example questions | Notes |
| --- | --- | --- |
| Term linking | - Help me link glossary terms to datasets and data products. | For best results, open the related glossary before asking the question. |
| Term and category management | - Delete term <term name> - Rename category <category name> | For best results, open the related glossary before asking the question. |

## Permissions

For full access to the business glossary manager, you need the required Qlik Answers access and permissions to the data and glossary assets used in glossary workflows.

### Administrator-assigned permissions

You need the following permissions, assigned by a tenant admin:

- The Agentic AI > Data governance permission set to Allowed.

  [*Managing user access to Qlik Answers*](administering-qlik-answers.htm#Access)
- Permissions to access and manage business glossaries and related data assets.

  Information noteFull access requires permissions for managing related glossaries and data products. If you only have permissions to view these items, you can still use the agent to explore and learn about the items without editing them.

  - For glossaries, one of the following:

    - Steward built-in security role
    - Manage glossaries and approve terms permission set to Allowed through the default permissions or a custom role
  - For data products, one of the following:

    - Data Product Manager built-in security role
    - Manage data products permission set to Allowed through the default permissions or a custom role

To learn more about assigning permissions as an administrator, refer to the following:

- [*Roles and permissions for users and administrators*](../Admin/permissions-admins-users-capacity-model.htm) (capacity-based subscriptions)
- [*Roles and permissions for users and administrators*](../Admin/permissions-admins-users.htm) (user-based subscriptions)

### Space access

You need access to the spaces where the applications, datasets, data products, and glossaries are located. See:

- [*Shared space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-shared-space-prof-full.htm)
- [*Shared space permissions for users with Analyzer entitlement*](../Spaces/permissions-shared-space-analyzer.htm)
- [*Shared space permissions for administrators*](../Spaces/permissions-shared-space-admin.htm)
- [*Managed space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-managed-space-prof-full.htm)
- [*Managed space permissions for users with Analyzer entitlement*](../Spaces/permissions-managed-space-analyzer.htm)
- [*Managed space permissions for administrators*](../Spaces/permissions-managed-space-admin.htm)

## Limitations

### Language support

The business glossary manager officially supports English. Other languages might work, but behavior is not guaranteed and generated terms, categories, and definitions are translated to English unless you explicitly instruct the agent to preserve the source language.

### Searching for resources

Support is limited for complex questions that search generally for data products, datasets, and glossaries. For example, the following questions are not supported:

- "find me data products that contain the dataset XYZ"
- "find me data products that contain this dataset"

Instead, refine the question so that it asks about a specific data product, dataset, or glossary. For example:

- "for the glossary XYZ, what terms are matching ABC"
- "for the data product XYZ, what datasets are matching ABC"

## Learn more

- [*Answering questions with Qlik Answers*](answering-questions-qlik-answers.htm)
- [*Working with business glossaries*](../Catalog/BusinessGlossary/Working-business-glossaries.htm)
- [*Using Qlik Answers and choosing your context*](choose-context.htm)
- [*Deploying and administering Qlik Answers*](administering-qlik-answers.htm)
- [*Enabling cross-region inference*](../Admin/cross-region-data-processing.htm)
