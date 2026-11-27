---
title: "Qlik Answers legacy experience"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/Legacy/legacy-answers.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers"]
---

# Qlik Answers legacy experience

Create AI-based assistants with Qlik Answers to ask questions and get answers from unstructured data sources. Assistants use knowledge bases that you create. Accepted file types to use as sources include HTML, DOCX, TXT, and PDFs.

The Qlik Answers legacy experience offers an alternative to the Qlik Answers agentic experience. Unlike the agentic Qlik Answers experience, the Qlik Answers legacy experience does not require cross-regional data processing.

Answers are sourced using retrieval augmented generation (RAG) from curated knowledge bases of unstructured data added to the assistant, ensuring the responses are relevant to your needs.

Legacy assistants provide a chat interface for asking questions and getting personalized, relevant answers.

Users can view the sources that the assistant used to create its answers, providing transparency over where the information comes from.

Qlik Answers can be useful for:

- Creating an assistant that uses curated knowledge bases of help documentation to allow users to ask questions of your documentation.
- Creating an assistant using knowledge bases of specific or related FAQs to help users find their specific question more quickly.
- Creating an assistant using knowledge bases of support or casework information to allow your users to quickly find pertinent information from the material.

Before beginning to use the legacy Qlik Answers experience, administrators should review [*Administering the legacy Qlik Answers experience*](administering-qlik-answers-legacy.htm).

Access to Qlik Answers depends on both user role and space permissions. For more information, see [*Legacy Qlik Answers access and permissions*](qlik-answers-legacy-permissions.htm).

Qlik Cloud Government noteQlik Answers is not supported in Qlik Cloud Government or Qlik Cloud Government - DoD.

Warning noteQlik Answers uses generative artificial intelligence (“GenAI”). It is the user’s responsibility to review and verify any GenAI output before using or sharing it, and to evaluate whether the use of Qlik Answers is appropriate for any particular use case and whether it complies with applicable laws.

Information noteQlik Answers is offered and supported in the English language only, but is available for preview in other languages pursuant to the evaluation terms in the Qlik Customer Agreement at www.qlik.com/legal-agreements.

Information noteQlik Answers is not available in Qlik Anonymous Access subscriptions.

Information noteQlik does not use the customer’s data to train any AI model external to the customer’s tenant. Any training of models internal to the customer’s tenant, such as using the machine learning aspects of Qlik Predict, is exclusively to the benefit of that customer and is not shared with others. For more information, see [Trust & AI](https://www.qlik.com/us/trust/ai).

## Qlik Answers legacy workflow

The following outlines the best workflow for using legacy Qlik Answers assistants and knowledge bases to provide a generative AI chat experience.

1. Add knowledge bases

   Create your knowledge bases and add knowledge sources to them.

   [*Creating knowledge bases*](../KnowledgeBases/creating-knowledge-bases.htm)
2. Create your assistant

   Create your assistant and add knowledge bases to the assistant.

   [*Creating legacy assistants*](create-legacy-assistants.htm)
3. Customize the assistant chat experience

   Add conversation starter questions and customize your chat.

   [*Adding conversation starters*](create-legacy-assistants.htm#Adding)

   [*Customizing legacy assistant settings*](create-legacy-assistants.htm#Customiz)
4. Make your assistant available

   Make your assistant available to your users. Invite users to the space with your assistant or move the assistant to a space to which your users have access.
5. Synchronize the indexing of the knowledge base

   Keep data sources up-to-date with scheduled indexing of data sources.

   [*Indexing knowledge base data sources*](../KnowledgeBases/indexing-knowledge-bases.htm)
6. Manage the conversation history and improve your assistant

   Review the history of conversations with your assistant, mark them as reviewed, and adjust the knowledge bases used by the assistant to provide better answers.

   [*Reviewing legacy assistant conversations*](reviewing-legacy-assistant-conversations.htm)

## Legacy Qlik Answers guardrails

Qlik Answers makes best efforts with the following guardrails when processing data into the large language model (LLM) and outputting it to the assistant:

- LLM monitoring for harmful content

  Qlik Answers scans and rejects questions that contain invisible text or prompt injections.
- Sanitization of Personal Identifying Information (PII) and secrets

  Qlik Answers detects and removes PII data and secrets when sending data to the LLM. The detected information is added back when providing responses.
- Hallucinations

  Qlik Answers mitigates hallucinations by detecting contextual relevance in the provided content. Additionally, users can view the content used as a source to verify responses.

## Limitations

Assistants and knowledge bases have the following limitations:

- The chat experience is supported for mobile browsers, but creating and managing knowledge bases and assistants are not optimized for standard mobile browser screen sizes.
