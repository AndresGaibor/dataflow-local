---
title: "Deploying and administering Qlik Answers"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/administering-qlik-answers.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers"]
---

# Deploying and administering Qlik Answers

Qlik Answers is administered from both the Administration activity center and the catalog in Qlik Cloud.

The Qlik Answers agentic experience requires opting in to cross-regional data processing. If you do not use cross-regional data processing in your tenant, you can use the Qlik Answers legacy experience, which offers a retrieval augmented generation (RAG) experience. For more information, see [*Administering the legacy Qlik Answers experience*](Legacy/administering-qlik-answers-legacy.htm).

Monitor capacity and manage user access permissions from the Administration activity center. Manage assistants and knowledge bases from the catalog in Qlik Cloud.

## Supported regions

Qlik Answers is supported for the following regions:

- US East (North Virginia)
- Canada (Montréal)
- Europe (Frankfurt)
- Europe (Ireland)
- Europe (London)
- Asia Pacific (Mumbai)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Tokyo)
- South America (São Paulo)

For more information about Qlik Cloud regions and backup locations, see [Qlik Cloud Regions](https://www.qlik.com/us/regions).

## Opting in to cross-region inference

To use the agentic Qlik Answers experience, you must opt in to cross-region inference. This allows Qlik Answers to send inference requests outside your tenant region.

If you are using the legacy Qlik Answers experience, you can choose to stay in-region by not opting in to cross-region inference. You can switch to newer models by opting in. For information on administering the legacy Qlik Answers experience, see [*Administering the legacy Qlik Answers experience*](Legacy/administering-qlik-answers-legacy.htm).

For details and the latest information about inference processing locations, see [*Enabling cross-region inference*](../Admin/cross-region-data-processing.htm).

## Qlik Answers capacity

Qlik Answers is available as an add-on to Qlik Cloud. Your subscription determines both your quota of questions asked by users and the number of pages indexed.

### Monitoring Qlik Answers capacity

Metering of capacity consumption is visible from Home in the Administration activity center.

Capacity consumption meters

![Capacity meters showing monthly questions and knowledge base pages indexed.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_administration-home-capacities.png "Click to view full size")

Questions (monthly) tracks the number of questions used from your monthly quota. Knowledge base pages measures the number of index pages out of your purchased total. Hover over the bars to see a tooltip with more details. The colors of the bars represent different metrics.

- Blue bar: The consumed amount this period.
- Red bar: Overage consumption. Overage is when the consumption of a resource exceeds the purchased amount for the period.
- Dark gray vertical line: The consumed amount last period

For more information on subscriptions and quotas, see the [Qlik Answers](https://www.qlik.com/us/legal/product-terms) product description.

### Question capacity

Question quotas are per month and reset every month. Questions do not carry over between months. When you hit your limit, users can no longer ask questions until the next month. Overage is only allowed on Qlik Cloud capacity-based subscriptions. For more information on overage, see [*Overage*](../Admin/subscription-options-qlik-cloud.htm#Overage).

Information note

Qlik Help questions are free and are not counted toward usage consumption limits.

Information noteQuestions that return an error do not consume question capacity.

For more information on question capacity, see the [Qlik Answers](https://www.qlik.com/us/legal/product-terms) product description.

### Knowledge base indexing capacity

Each page in an index uses up capacity while it is indexed. Capacity does not expire or reset. Adding, deleting, or updating pages impacts capacity usage. Index capacity overage is only available on Qlik Cloud capacity-based subscriptions.

Pages correspond to 2,000 characters of text data. Only the size of the text data is counted. File size from images and other non-textual content is not counted when calculating pages in Qlik Answers.

### Qlik Answers guardrails

Guardrails are hard limits on capacities, used to ensure Qlik Answers performance and stability. The following guardrails and capacities are used by Qlik Answers:

- Maximum file size on disk: 50 MiB.
- Concurrent documents ingested per data source: 10.

## Managing user access to Qlik Answers

You can manage user access to Qlik Answers in the Administration activity center in both the default permissions and custom roles. There are no default Qlik Answers security roles. You can customize Qlik Answers access using custom roles and the available Qlik Answers permissions. For more information about custom user roles, see [*Managing custom roles*](../Admin/permissions-custom-roles-capacity-model.htm) (capacity-based subscriptions) or [*Managing custom roles*](../Admin/permissions-custom-roles.htm) (user-based subscriptions).

### Agentic Qlik Answers permissions

Under Content types, there are the following permissions for Qlik Answers:

- Enable Qlik Answers for applications: Control whether users can activate Qlik Answers for applications and view AI readiness details and scores. The following permissions are available:

  - Allowed: Users can activate Qlik Answers for applications and view AI readiness details and scores.
  - Not allowed: Users cannot activate Qlik Answers for applications or view AI readiness details and scores.

  Information note

  Although Enable Qlik Answers for applications is allowed by default, we recommend that you set it to Not allowed in the default permissions and create a custom role with it set to Allowed. Assign the custom role to the specific users who should be able to activate Qlik Answers for applications and optimize applications for AI.
- Manage assistants: Control what level of access users have with assistants. The following permissions are available:

  - Allowed: Users can create and manage assistants.
  - Not allowed: Users cannot access assistants.
- Manage knowledge bases: Control what level of access and interaction users have with knowledge bases. The following permissions are available:

  - Allowed: Users can create, manage, index, and search knowledge bases.
  - Not allowed: Users cannot access knowledge bases in Qlik Cloud.
- Index knowledge bases: Control indexing rights with knowledge bases. The following permissions are available:

  - Allowed: Users can index knowledge bases and create a reindexing schedule.
  - Not allowed: Users cannot index knowledge bases.
- Search knowledge bases: Control search access to knowledge bases. Search allows users access to knowledge base contents when asking Qlik Answers questions. The following permissions are available:

  - Allowed: Users can search knowledge bases when asking questions of Qlik Answers assistants.
  - Not allowed: Users cannot search knowledge bases.
- Manage skills: Control what level of access users have with skills. The following permissions are available:

  - Allowed: Users can upload and manage skills.
  - Not allowed: Users cannot upload or manage skills.

Information note

To run actions added to Qlik Answers assistants, users also require Automations > Shared Automations set to Allowed.

Information note

To work with machine learning in Qlik Answers, users also need the corresponding Qlik Predict permissions. For more information, see [*Who can work with Qlik Predict*](../AutoML/who-can-work-with-automl.htm).

Under Features and actions, there are the following permissions for Qlik Answers under Agentic AI:

- Data analysis: Controls user access to Qlik Answers agentic chat from Answers. The following permissions are available:

  - Allowed: Users can use application analysis and Answers assistants within the Qlik Answers agentic chat from Answers.
  - Not allowed: Users cannot access application analysis or Answers assistants from the Qlik Answers agentic chat. If they have the permissions, they can use the experience with legacy assistants.
- Data governance: Controls user access to the data governance tools within Qlik Answers agentic chat from Answers. The following permissions are available:

  - Allowed: Users can interact with data governance in the Qlik Answers agentic chat.
  - Not allowed: Users cannot interact with data governance in the Qlik Answers agentic chat.
- Qlik product help: Controls user access to the Help agent in the Qlik Answers agentic chat.

  - Allowed: Users can access the Help agent.
  - Not allowed: Users cannot access the Help agent.
- Review agent and chat interactions: Allows user access to both Answers review portal and Feedback in agentic assistants to review Qlik Answers conversations. The following permissions are available:

  - Allowed: Users can access the review portal and Feedback in agentic assistants to view conversations from Qlik Answers agentic experiences.
  - Not allowed: Users cannot access the review portal or view Feedback in agentic assistants.

Information noteThe audit admin user role also allows users to review conversations and view feedback in both agentic and legacy assistants.

Additionally, space roles affect access to Qlik Answers. For more information, see [*Spaces permissions and Qlik Answers*](qlik-answers-permissions.htm#Spaces).

### Recommended agentic Qlik Answers user role permissions

The following settings are recommended to define user roles for agent managers and agent consumers when using the Qlik Answers agentic experience.

#### Agent manager

For users who are creating and managing assistants and knowledge bases for other users to consume in Qlik Answers, the following user role permissions are required:

- Manage assistants: Allowed
- Manage knowledge bases: Allowed
- Index knowledge bases: Allowed
- Manage skills: Allowed

If the agent manager also makes applications available to Qlik Answers, the following user permissions are required:

- Enable Qlik Answers for applications: Allowed
- Data analysis: Allowed

#### Agent consumer

For users who just will be using Qlik Answers to answer questions and need access to assistants, apps, and the help agent, the following user role permissions are required:

- Search knowledge bases: Allowed
- Data analysis: Allowed
- Qlik product help: Allowed

#### Conversation reviewer

For users who are reviewing Qlik Answers feedback in Answers review portal to drive improvements, the following user role permissions are required:

- Search knowledge bases: Allowed
- Data analysis: Allowed
- Qlik product help: Allowed
- Review agent and chat interactions: Allowed

## Managing assistants and knowledge bases

Qlik Answers assistants and knowledge bases are managed from the catalog. If you are a tenant administrator or analytics administrator, you can view, move, and delete assistants and knowledge bases from the catalog. For more information, see:

- [*Managing assistants*](Assistants/managing-assistants.htm)
- [*Managing knowledge bases*](KnowledgeBases/managing-knowledge-bases.htm)

Audit administrators can review conversations and feedback in assistants. For more information, see [*Reviewing assistant conversations*](Assistants/reviewing-assistant-conversations.htm).

## Managing skills

If you are a tenant administrator or analytics administrator, you can manage skills from the Administration activity center. You can change the owner of skills, move skills to another space, and delete skills. For more information, see [*Managing skills for tenant and analytics administrators*](../Admin/mc-administer-skills.htm).

## Reviewing agentic conversations

You can review conversations and feedback for assistants, applications, and the help specialist in Answers review portal. The review portal is available from the Analytics activity center.

Information noteTo access Answers review portal, you must have a custom role with the Agentic AI > Review agent and chat interactions permission set to Allowed. For more information about user permissions, see [*Default permissions and custom roles*](../Admin/permissions-scopes.htm).

For more information, see [*Reviewing conversations from Qlik Answers agentic experiences*](reviewing-with-answers-review-portal.htm).

## Managing applications with Qlik Answers

Tenant admin and analytic admins can manage applications activated for Qlik Answers in the Applications tab of the Content page in the Administration activity center.

When using the Qlik Answers agentic experience, the new filter option Activated for Qlik Answers is available from the dropdown list above the table. This filters the applications to only those activated and index for use with Qlik Answers.

In Activated for Qlik Answers, you can:

- Deactivate applications for Qlik Answers
- Delete the applications

### Deactivating applications for Qlik Answers

You can deactivate one or more applications for Qlik Answers. Deactivating applications removes it from the index. Applications can be reactivated for Qlik Answers at any time.

Do the following:

1. In the Administration activity center, go to Content > Applications.
2. Select Activated for Qlik Answers.
3. Select one or more applications and click Deactivate Qlik Answers.

   Alternatively, click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Deactivate Qlik Answers
4. Click Confirm.

## Monitoring Qlik Answers usage

Tenant administrators can monitor Qlik Answers usage using the Qlik Cloud Answers Analyzer monitoring application. The Qlik Cloud Answers Analyzer monitoring application helps tenant administrators:

- Track and analyze user questions across knowledge bases, assistants, and sources.
- Track inaccurate, unused, and unreferenced data sources.
- Monitor knowledge base and page sizes to help keep to quotas.
- Monitor knowledge base indexing to ensure data is up-to-date.

Qlik Cloud Answers Analyzer is a part of the Qlik Cloud Monitoring Apps, which are community-supported. As such, they are not officially supported by Qlik. To quickly install and update these apps, use the Qlik Cloud Monitoring App Installer with Qlik Automate. For details on installation and support, see [*App Installers*](../../Sense_QlikAutomation/introduction/template-list.htm#App).

For more information about the Qlik Cloud Answers Analyzer app, see:

- [The Qlik Sense Monitoring Applications for Cloud and On Premise](https://community.qlik.com/t5/Official-Support-Articles/The-Qlik-Sense-Monitoring-Applications-for-Cloud-and-On-Premise/ta-p/1822454)
- [GitHub: Qlik Cloud Answers Analyzer](https://github.com/qlik-oss/qlik-cloud-app-analyzer)
