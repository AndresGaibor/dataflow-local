---
title: "Qlik Answers"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/Qlik-Answers.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data"]
---

# Qlik Answers

Create AI-based assistants and AI-enabled applications with Qlik Answers. Ask questions and get answers from both structured and unstructured data sources.

Qlik Answers adds plug-and-play generative AI (GenAI) agents for Qlik Cloud.

Qlik Answers provides an agentic chat interface for asking questions and getting personalized, relevant answers. Answers are sourced using AI agents from curated structured and unstructured data sources, ensuring responses relevant to your needs. Users can view the sources that the agent used to create its answers, providing transparency over where the information comes from.

Qlik Answers supports both unstructured and structured data:

- Unstructured data sources include file types such as HTML, DOCX, TXT, and PDF, which are added to knowledge bases and indexed. Qlik Answers assistants use knowledge bases to answer user questions.
- Structured data sources are data from Qlik analytic applications. Applications can be made available to Qlik Answers for agentic conversations. Assistants can also include a maximum of five applications as content sources. Combining your structured and unstructured data sources provides greater context to help Qlik Answers understand and interpret the structured data from your applications.

Qlik Answers also offers an alternative retrieval augmented generation (RAG) model, the Qlik Answers legacy experience, for Qlik Cloud users unable to user the agentic experience. For more information, see [*Qlik Answers legacy experience*](Legacy/legacy-answers.htm).

Qlik Answers can be useful for:

- Providing conversational access to curated documentation, FAQs, and support content, allowing users to ask natural language questions and receive precise, contextual answers.
- Enabling deep, agentic exploration of structured application data, allowing users to ask complex analytical questions that would traditionally require significant analyst effort.
- Driving decision making by combining semantic understanding, business logic, and live application data in guided, multi step analytical workflows.
- Generating sheets, charts, and analytical artifacts directly from conversational interactions within analytic applications.
- Embedding agentic analytical experiences into external applications or websites, extending Qlik-powered insights beyond the Qlik environment.

Before beginning to use Qlik Answers, administrators should review [*Deploying and administering Qlik Answers*](administering-qlik-answers.htm).

Information note

To use the agentic Qlik Answers experience, you must opt in to cross-region inference. This allows Qlik Cloud to send inference requests outside your tenant region.

If you are using the legacy Qlik Answers experience (Q&A chatbot for unstructured data), you can choose to stay in-region by not opting in to cross-region inference. You can switch to newer models by opting in.

For details and the latest information about inference processing locations, see [*Enabling cross-region inference*](../Admin/cross-region-data-processing.htm).

Access to Qlik Answers depends on both user role and space permissions. For more information, see [*Qlik Answers access and permissions*](qlik-answers-permissions.htm).

Qlik Cloud Government noteQlik Answers is not supported in Qlik Cloud Government or Qlik Cloud Government - DoD.

Warning noteQlik Answers uses generative artificial intelligence (“GenAI”). It is the user’s responsibility to review and verify any GenAI output before using or sharing it, and to evaluate whether the use of Qlik Answers is appropriate for any particular use case and whether it complies with applicable laws.

Information noteQlik Answers is offered and supported in the English language only, but is available for preview in other languages pursuant to the evaluation terms in the Qlik Customer Agreement at www.qlik.com/legal-agreements.

Information noteQlik Answers is not available in Qlik Anonymous Access subscriptions.

Information noteQlik does not use the customer’s data to train any AI model external to the customer’s tenant. Any training of models internal to the customer’s tenant, such as using the machine learning aspects of Qlik Predict, is exclusively to the benefit of that customer and is not shared with others. For more information, see [Trust & AI](https://www.qlik.com/us/trust/ai).

## Qlik Answers workflows

The following outlines the best workflows for using Qlik Answers to provide an agentic generative AI chat experience, either using Qlik Answers directly with individual applications or Qlik Answers assistants.

### Qlik Answers-available applications

1. Prepare your application for Qlik Answers

   Review your application and make sure it is optimized for use as a source for Qlik Answers.

   [*Working with applications in Qlik Answers*](Applications/working-with-apps-in-qlik-answers.htm)

   [*Best practices for preparing applications for Qlik Answers*](Applications/working-with-apps-in-qlik-answers.htm#Best)
2. Make your application available to Qlik Answers

   Make your application available to Qlik Answers.

   [*Making applications available for Qlik Answers*](Applications/working-with-apps-in-qlik-answers.htm#Making)
3. Optimize your application for Qlik Answers

   Review your AI readiness score and recommendations and use the options in AI optimization to customize how Qlik Answers uses your application.

   [*Optimizing your application for Qlik Answers with business logic*](BusinessLogicAI/business_logic-qlik-answers.htm)
4. Add skills to your application

   Create skills and add them to your application to teach Qlik Answers how to handle specific topics and tasks.

   [*Working with skills*](Skills/working-with-skills.htm)

### Qlik Answers assistants

1. Prepare your content sources

   If you are using unstructured data, create your knowledge bases and add knowledge sources to them.

   [*Creating knowledge bases*](KnowledgeBases/creating-knowledge-bases.htm)

   If you are using structured data, prepare your application for use with Qlik Answers.

   [*Best practices for preparing applications for Qlik Answers*](Applications/working-with-apps-in-qlik-answers.htm#Best)
2. Create your assistant

   Create your assistant and add content sources to the assistant.

   [*Creating assistants*](Assistants/create-assistants.htm)
3. Add actions to your assistant

   Optionally, add automations to your assistant that can be run as actions.

   [*Managing assistant actions*](managing-actions.htm)
4. Customize the assistant chat experience

   Add conversation starter questions and customize your chat.

   [*Adding conversation starters*](Assistants/create-assistants.htm#Adding)

   [*Customizing assistant settings*](Assistants/create-assistants.htm#Customiz)
5. Add skills to your assistant

   Create skills and add them to your assistant to teach Qlik Answers how to handle specific topics and tasks.

   [*Working with skills*](Skills/working-with-skills.htm)
6. Make your assistant available

   Make your assistant available to your users. Invite users to the space with your assistant or move the assistant to a space to which your users have access.
7. Schedule the indexing of the content sources

   Keep data sources up to date with scheduled indexing of data sources. Knowledge bases can have scheduled indexes.

   [*Indexing knowledge base data sources*](KnowledgeBases/indexing-knowledge-bases.htm)

   Applications are indexed after every reload, so schedule indexing by scheduling reloads.

   [*Reloading application data*](../Apps/reloading-apps-cloud-hub.htm)
8. Manage the conversation history and improve your assistant

   Review the history of conversations with your assistant, mark them as reviewed, and adjust the knowledge bases used by the assistant to provide better answers.

   [*Reviewing assistant conversations*](Assistants/reviewing-assistant-conversations.htm)

## Qlik Answers guardrails

Qlik Answers implements the following guardrails when processing data into the large language model (LLM) and outputting it to Qlik Answers agents:

- LLM monitoring for harmful content

  Qlik Answers scans and rejects questions that contain invisible text or prompt injections.
- Sanitization of Personal Identifying Information (PII) and secrets

  Qlik Answers detects and removes PII data and secrets when sending data to the LLM. The detected information is added back when providing responses.
- Hallucinations

  Qlik Answers mitigates hallucinations by detecting contextual relevance in the provided content. Additionally, users can view the content used as a source to verify responses.

## Qlik Answers and Insight Advisor

Qlik Answers replaces Insight Advisor and Insight Advisor Chat in tenants enabled for the agentic Qlik Answers experience. Insight Advisor and Insight Advisor Chat options and settings will also be hidden tenant-wide for applications. Qlik Answers provides a superior natural language interface for creating in-application content and exploring your data.

If you want to switch back to using Insight Advisor and the legacy Qlik Answers experience, a tenant administrator must do the following:

- Set all related AI feature permissions to Not allowed in the default permissions and any custom user roles.
- Turn off cross-region inference.

Once cross-region inference is turned off, Insight Advisor will become available again after approximately 15 minutes.

For more information on turning off cross-region inference, see [*Turn off cross-region inference*](../Admin/cross-region-data-processing.htm#Turn).

## Qlik Answers and business logic

Business logic features in applications that do not apply to Qlik Answers are removed in tenants enabled for Qlik Answers. Available business logic features are available in AI optimization:

- Overview: Customize the Qlik Answers-generated application description and resync the application's data to business logic.

  [*Viewing the overview of business logic for Qlik Answers*](BusinessLogicAI/business-logic-overview-qlik-answers.htm)
- Fields and master items: Customize the fields and groups used in the logical model.

  [*Defining fields and master items for Qlik Answers*](BusinessLogicAI/business-logic-fields-master-items-qlik-answers.htm)
- Semantic understanding: Customize the semantic understanding of the fields and master items in the application used by Qlik Answers.

  [*Managing Qlik Answers-generated field and master item descriptions with Semantic understanding*](BusinessLogicAI/business-logic-semantic-understanding.htm)
- Synonyms: Synonyms allow you to add alternate terms.

  [*Adding synonyms for Qlik Answers*](BusinessLogicAI/business-logic-synonyms-qlik-answers.htm)
- Skills: Add skills that teach Qlik Answers how to handle specific topics and tasks.

  [*Adding skills to applications and assistants*](Skills/adding-skills.htm)
- Settings: Customize additional AI options for Qlik Answers.

  [*Configuring Qlik Answers behavior with business logic*](BusinessLogicAI/business-logic-qlik-answers-settings.htm)
