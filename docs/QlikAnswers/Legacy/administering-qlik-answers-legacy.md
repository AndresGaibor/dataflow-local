---
title: "Administering the legacy Qlik Answers experience"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/Legacy/administering-qlik-answers-legacy.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Qlik Answers legacy experience"]
---

# Administering the legacy Qlik Answers experience

If you do not enable cross-regional data processing, or are in an unsupported region for cross-regional data processing, you can use the legacy Qlik Answers experience instead of the agentic experience. Unlike agentic Qlik Answers, legacy Qlik Answers sources uses retrieval augmented generation (RAG) from curated knowledge bases of unstructured data added to legacy assistants, ensuring the responses are relevant to your needs.

Qlik Answers is administered from both the Administration activity center and the catalog in Qlik Cloud.

Monitor capacity and manage user access permissions from the Administration activity center. Manage legacy assistants and knowledge bases from the catalog in Qlik Cloud.

## Supported regions

Qlik Answers is supported for the following regions:

- US East (North Virginia)
- Canada (Montréal)
- Asia Pacific (Mumbai)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Tokyo)
- Europe (Frankfurt)
- Europe (Ireland)
- Europe (London)

For more information about Qlik Cloud regions and backup locations, see [Qlik Cloud Regions](https://www.qlik.com/us/regions).

## Qlik Answers capacity

Qlik Answers is available as an add-on to Qlik Cloud. Your subscription determines both your quota of questions asked by users and the number of pages indexed.

### Monitoring Qlik Answers capacity

Metering of capacity consumption is visible from Home in the Administration activity center.

Capacity consumption meters

![Capacity meters showing monthly questions and knowledge base pages indexed.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_administration-home-capacities.png "Click to view full size")

Questions (monthly) tracks the number of questions used from your monthly quota. Knowledge base pages measures the number of index pages out of your purchased total. Hover over the bars to see a tooltip with more details. The colors of the bars represent different metrics.

- Blue bar: The consumed amount this period.
- Red bar: Overage consumption. Overage is when the consumption of a resource exceeds the purchased amount for the period.
- Dark gray vertical line: The consumed amount last period

For more information on subscriptions and quotas, see the [Qlik Answers](https://www.qlik.com/us/legal/product-terms) product description.

### Question capacity

Question quotas are per month and reset every month. Questions do not carry over between months. When you hit your limit, users can no longer ask questions until the next month. Overage is only allowed on Qlik Cloud capacity-based subscriptions. For more information on overage, see [*Overage*](../../Admin/subscription-options-qlik-cloud.htm#Overage).

For more information on question capacity, see the [Qlik Answers](https://www.qlik.com/us/legal/product-terms) product description.

### Indexing capacity

Each page in an index uses up capacity while it is indexed. Capacity does not expire or reset. Adding, deleting, or updating pages impacts capacity usage. Index capacity overage is only available on Qlik Cloud capacity-based subscriptions.

Pages correspond to 2,000 characters of text data. Only the size of the text data is counted. File size from images and other non-textual content is not counted when calculating pages in Qlik Answers.

### Qlik Answers guardrails

Guardrails are hard limits on capacities, used to ensure Qlik Answers performance and stability. The following guardrails and capacities are used by Qlik Answers:

- Maximum file size on disk: 50 MiB.
- Concurrent documents ingested per data source: 10.
- Knowledge base search rate limit: 50 per minute per subscription.
- Assistant question rate limit: 20 per minute per subscription.

## Managing user access to the legacy Qlik Answers experience

You can manage user access to Qlik Answers in the Administration activity center in both the default permissions and custom roles. There are no default Qlik Answers security roles. You can customize Qlik Answers access using custom roles and the available Qlik Answers permissions. For more information about custom user roles, see [*Managing custom roles*](../../Admin/permissions-custom-roles-capacity-model.htm) (capacity-based subscriptions) or [*Managing custom roles*](../../Admin/permissions-custom-roles.htm) (user-based subscriptions).

Under Content types, there are the following permissions for the legacy Qlik Answers experience:

- Manage assistants: Control what level of access users have with legacy assistants. The following permissions are available:

  - View assistants: Users can view assistants and ask questions.
  - Allowed: Users can create, view, and manage legacy assistants.
  - Not allowed: Users cannot access assistants.
- Manage knowledge bases: Control what level of access and interaction users have with knowledge bases. The following permissions are available:

  - View knowledge bases: Users can view knowledge bases.
  - Allowed: Users can create, view, manage, index, and search knowledge bases.
  - Not allowed: Users cannot access knowledge bases in Qlik Cloud.
- Index the contents of a knowledge base source: Control indexing rights with knowledge bases. The following permissions are available:

  - Allowed: Users can index knowledge bases and create a reindexing schedule.
  - Not allowed: Users cannot index knowledge bases.
- Search knowledge bases: Control search access to knowledge bases. Search allows users access to knowledge base contents when asking Qlik Answers questions. The following permissions are available:

  - Allowed: Users can search knowledge bases when asking questions of Qlik Answers assistants.
  - Not allowed: Users cannot search knowledge bases.

Additionally, to review conversations and view feedback in legacy assistants, users require the audit admin user role.

Tip note

The minimum level of access for a consumer of legacy assistants is:

- Managed assistants: View assistants
- Search knowledge bases: Allowed

Additionally, space roles affect access to Qlik Answers. For more information, see [*Spaces permissions and Qlik Answers*](../qlik-answers-permissions.htm#Spaces).

## Managing legacy assistants and knowledge bases

Qlik Answers legacy assistants and knowledge bases are managed from the catalog. If you are a tenant administrator or analytics administrator, you can view, move, and delete legacy assistants and knowledge bases. For more information, see:

- [*Managing legacy assistants*](managing-legacy-assistants.htm)
- [*Managing knowledge bases*](../KnowledgeBases/managing-knowledge-bases.htm)

Audit administrators can review conversations and feedback in legacy assistants. For more information, see [*Reviewing legacy assistant conversations*](reviewing-legacy-assistant-conversations.htm).

## Monitoring Qlik Answers usage

Tenant administrators can monitor Qlik Answers usage using the Qlik Cloud Answers Analyzer monitoring application. The Qlik Cloud Answers Analyzer monitoring application helps tenant administrators:

- Track and analyze user questions across knowledge bases, assistants, and sources.
- Track inaccurate, unused, and unreferenced data sources.
- Monitor knowledge base and page sizes to help keep to quotas.
- Monitor knowledge base indexing to ensure data is up-to-date.

Qlik Cloud Answers Analyzer is a part of the Qlik Cloud Monitoring Apps, which are community-supported. As such, they are not officially supported by Qlik. To quickly install and update these apps, use the Qlik Cloud Monitoring App Installer with Qlik Automate. For details on installation and support, see [*App Installers*](../../../Sense_QlikAutomation/introduction/template-list.htm#App).

For more information about the Qlik Cloud Answers Analyzer app, see:

- [The Qlik Sense Monitoring Applications for Cloud and On Premise](https://community.qlik.com/t5/Official-Support-Articles/The-Qlik-Sense-Monitoring-Applications-for-Cloud-and-On-Premise/ta-p/1822454)
- [GitHub: Qlik Cloud Answers Analyzer](https://github.com/qlik-oss/qlik-cloud-app-analyzer)
