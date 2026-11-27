---
title: "Managing data quality with Qlik Answers"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/data-quality-agent.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Using Qlik Answers and choosing your context"]
---

# Managing data quality with Qlik Answers

Manage and monitor data quality in natural language with the data quality manager in Qlik Answers.

Data quality manager in Qlik Answers

![Data quality manager](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_answers_context_data_quality.png "Click to view full size")

Govnote-not-inNot supported in Qlik Cloud Government.

Govnote-not-inNot supported in Qlik Cloud Government - DoD.

## What the data quality manager can do

The data quality manager allows you to do the following:

- Search for and explore existing validation rules that are available to you.
- Explore and learn more about the quality of datasets.
- Recompute quality statistics for datasets.
- Create and apply new validation rules.

For specific workflows and example questions, see [*Workflows*](#Workflows).

## Before you begin

Prerequisites:

- Your [tenant](#glossary-0 "Glossary term") has cross-region inference turned on and is enabled for the agentic Qlik Answers experience.

  [*Enabling cross-region inference*](../Admin/cross-region-data-processing.htm)
- Your tenant and subscription have capacity for Qlik Answers.

  [*Qlik Answers capacity*](administering-qlik-answers.htm#Capacity)
- You have access to the required data sources and permissions to manage data quality for them.

  [*Permissions*](#Permissions)

## Chatting with the data quality manager

Do the following:

1. In the top bar, click Qlik Answers.

   The Qlik Answers chat opens.
2. In the dropdown menu, select Data quality.

   Opening the data quality manager in Qlik Answers

   ![Selecting data quality manager in chat](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_answers-context-selector-data-quality.png "Click to view full size")
3. Select one of the available starter questions, or enter your own question.

   Information note

   Depending on your question, Qlik Answers may need to use a tool to generate the response, such as when checking data quality. Qlik Answers asks for approval the first time it needs to use a tool. You can choose to approve it once, approve it for all future requests, or deny the use of the tool.

   For more information, see [*Managing Qlik Answers tools*](qlik-answers-tools.htm).

## Workflows

These workflows contain helpful example questions to get you started working with the data quality manager.

Example questions for data quality

| Action | Example questions | Notes |
| --- | --- | --- |
| Status and exploration of data quality | - Help me assess the quality of this dataset - What validation rules are applied to this dataset - What percentage of valid values are there in <dataset name>? - Help me enforce validation rules on this dataset - Are there any existing rules I could use for validating phone numbers? | For best results, open the related dataset before asking the question. |
| Quality computation | - Refresh the trust score | For best results, open the related dataset before asking the question. |
| Create and apply validation rules | - I need a rule that ensures the <field name> field is always a number. - I need a rule that ensures the <field name> field is never empty. - The <field name> field should never be null. - Create AI-generated validation rules for this dataset | For best results, open the related dataset before asking the question. |

## Permissions

For full access to the data quality manager, you need the required Qlik Answers access and permissions to the data sources and quality assets you will be using.

### Administrator-assigned permissions

You need the following permissions, assigned by a tenant admin:

- The Agentic AI > Data governance permission set to Allowed. This permission is located in the Features and actions section of the default permissions and custom roles. See [*Default permissions and custom roles*](../Admin/permissions-scopes-capacity-model.htm).

  [*Managing user access to Qlik Answers*](administering-qlik-answers.htm#Access)
- Permissions to access Qlik Cloud data quality features. This includes all permissions included under Features and actions > Data quality in the default permissions and custom roles. See [*Default permissions and custom roles*](../Admin/permissions-scopes-capacity-model.htm).

  Information noteFull access requires permissions for managing related data and quality assets. If you only have permissions to view these items, you can still use the agent to explore and learn about the items without editing them.

To learn more about assigning permissions as an administrator, refer to the following:

- [*Roles and permissions for users and administrators*](../Admin/permissions-admins-users-capacity-model.htm) (capacity-based subscriptions)
- [*Roles and permissions for users and administrators*](../Admin/permissions-admins-users.htm) (user-based subscriptions)

### Space access

You need access to the spaces where the datasets are located. See:

- [*Shared space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-shared-space-prof-full.htm)
- [*Shared space permissions for users with Analyzer entitlement*](../Spaces/permissions-shared-space-analyzer.htm)
- [*Shared space permissions for administrators*](../Spaces/permissions-shared-space-admin.htm)
- [*Managed space permissions for Professional and capacity-based subscription users*](../Spaces/permissions-managed-space-prof-full.htm)
- [*Managed space permissions for users with Analyzer entitlement*](../Spaces/permissions-managed-space-analyzer.htm)
- [*Managed space permissions for administrators*](../Spaces/permissions-managed-space-admin.htm)

## Learn more

- [*Answering questions with Qlik Answers*](answering-questions-qlik-answers.htm)
- [*Assessing data quality*](../DataIntegration/DataProducts/Data-quality-and-data-discovery.htm)
- [*Working with validation rules*](../DataIntegration/DataProducts/Working-with-validation-rules.htm)
- [*Using Qlik Answers and choosing your context*](choose-context.htm)
- [*Deploying and administering Qlik Answers*](administering-qlik-answers.htm)
- [*Enabling cross-region inference*](../Admin/cross-region-data-processing.htm)
