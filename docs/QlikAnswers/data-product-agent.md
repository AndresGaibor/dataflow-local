---
title: "Managing data products with Qlik Answers"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/data-product-agent.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Using Qlik Answers and choosing your context"]
---

# Managing data products with Qlik Answers

The data product manager lets you work with data products within Qlik Answers. You can manage data products through all stages of their lifecycle, including creation, activation, governance, and semantic model development.

Data product manager in Qlik Answers

![Selecting data product manager in chat](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_answers_context_data_product.png "Click to view full size")

## Before you begin

Prerequisites:

- Your [tenant](#glossary-0 "Glossary term") has cross-region inference turned on and is enabled for the agentic Qlik Answers experience.

  [*Enabling cross-region inference*](../Admin/cross-region-data-processing.htm)
- Your tenant and subscription have capacity for Qlik Answers.

  [*Qlik Answers capacity*](administering-qlik-answers.htm#Capacity)
- You have access to the required data products, datasets, and related assets.

  [*Permissions*](#Permissions)

## Chatting with the data product manager

Do the following:

1. In the top bar, click Qlik Answers.

   The Qlik Answers chat opens.
2. In the dropdown menu, select Data product.

   Opening the data product manager in Qlik Answers

   ![Selecting data product manager in chat](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_answers-context-selector-data-product.png "Click to view full size")
3. Select one of the available starter questions, or enter your own question.

   Information note

   Depending on your question, Qlik Answers may need to use a tool to generate the response, such as when creating a data product. Qlik Answers asks for approval the first time it needs to use a tool. You can choose to approve it once, approve it for all future requests, or deny the use of the tool.

   For more information, see [*Managing Qlik Answers tools*](qlik-answers-tools.htm).

## Permissions

You need the required Qlik Answers access and permissions to data products and related assets.

Specifically, you need the following:

- Professional user entitlement (only applicable to user-based subscriptions)
- The required Agentic AI > Data governance permission set to Allowed. This permission is assigned by a tenant admin.

  [*Managing user access to Qlik Answers*](administering-qlik-answers.htm#Access)
- Permissions to access and manage data products and related data assets in spaces.

## Limitations

- The Data product context is available only when your tenant and subscription meet the required availability prerequisites.
- Operations that can change data products, such as activate, deactivate, and delete, require confirmation in chat.

## Example use case: create and activate a data product

You can use the data product agent to create a data product and move it through activation with guided prompts.

Example prompts for a data product workflow

| Action | Example prompts | Notes |
| --- | --- | --- |
| Create a data product | - Create a data product called Sales performance - Create a data product for weekly demand planning with a short description | Start by describing the business purpose and owner. |
| Add related assets | - Add datasets from the supply chain space to this data product - Link the customer glossary terms to this data product | Use follow-up prompts to refine what is included. |
| Manage semantic model | - In this data product, create a measure for total sum of sales - Can you build a semantic model for this data product, linking Cities, Sales, and Customers on their common keys? | Use follow-up prompts to refine what is included. |
| Update metadata | - Set the owner to Data Governance Team - Add tags finance, trusted, and monthly | Use updates to align naming, ownership, and discoverability. |
| Activate and verify | - Activate this data product - Show me the current status and linked datasets | Activation and deactivation actions include confirmation steps. |

## Learn more

- [*Using Qlik Answers and choosing your context*](choose-context.htm)
- [*Answering questions with Qlik Answers*](answering-questions-qlik-answers.htm)
- [*Working with data products*](../DataIntegration/DataProducts/Data-products.htm)
- [*Creating data products*](../DataIntegration/DataProducts/Creating-data-products.htm)
- [*Deploying and administering Qlik Answers*](administering-qlik-answers.htm)
