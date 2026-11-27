---
title: "Best practices for creating and managing assistants and knowledge bases"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/qlik-answers-best-practices.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers"]
---

# Best practices for creating and managing assistants and knowledge bases

Learn how to use Qlik Answers to best help your users find the answers they seek with Qlik Answers assistants.

## Plan governance of data sources

Successful assistants depend on governance of their data sources. Ensure owners of content used by the assistant are responsible for maintaining their content and keeping it up to date.

## Curate information sources

Curate your data sources to be as specific to the use case as possible. Do not add unrelated knowledge bases to assistants. Qlik Answers works best when it is finding specific information and providing a summary. It is not as effective when there are a lot of potential answers and you are expecting an aggregation or different answer each time. Minimize repetitive content and try to include single versions of possible answers.

Qlik Answers does not generate its own rankings or aggregations, but it can present them if such summaries already exist in your data sources. If you think your users need that information, add them to the sources used by your assistants.

Qlik Answers does not select or prioritize information sources by age or filtering, just semantic relevance. An old document in a knowledge base is treated just as relevant as a new document. Update your source content and knowledge bases as newer information becomes available. Dynamic filters in data connections can help exclude older content that may no longer be relevant or accurate.

## Make specific and targeted assistants

Create assistants that are unique and targeted to specific purposes. Your end users need to know that they have single points to go to for information on a specific subject. Identify your use cases, identify the right people to build and maintain the content, and the right people to use the content. Do not create multiple assistants that overlap in the questions they can answer.

Create conversation starters for users. These can cover commonly asked questions for your users. They can also help guide users as to both the kinds of questions the assistant can answer and how users can ask their questions. For example, instead of just having a question that directly asks what something can do, such as What can the TRIM() function do?, instead show how users can ask a question that describes the problem they are trying to solve, such as When I read text line by line, what function should I use to remove extra spaces?.

Similarly, ensuring your assistant has a helpful description and welcome message can also help users orientate themselves to the kinds of questions your assistants can answer.

## Review questions

Provide your subject matter experts with access to assistants to review answers. Subject matter experts can help assess if the assistant is meeting user needs and if the data used by the assistant is serving the right purpose. If not, update your data sources to better meet user needs.

Reviewing your users' answers is key for content improvement. Answers are unique each time, with no specific caching, so review similar questions to see how similar the answers are.

The kinds of answers users receive can help the curation of your assistants. Unanswered questions can show you if content is missing or if users are having trouble getting answers from your assistants. Disliked answers that include a reason or comments can help you understand if the knowledge bases are missing information or if the assistant is hallucinating when trying to provide the correct answer. Additionally, liked answers can provide good candidates for using as entries when creating FAQs.

Reviewing the sources used by the questions can also help guide the curation of information in your knowledge bases. Seeing what sources are being used can drive what additional sources may need to be added to the assistant.

Data can be exported from Review for further analysis in analytic apps.

## Validate content in knowledge bases

When creating knowledge bases, you should validate their contents. Assign the new knowledge base to an assistant as the only knowledge source. Then, start asking questions to which you know the answer and that should be answerable using the data sources in the knowledge base. For example, in a Qlik Cloud knowledge base, you might ask:

- Give me an introduction on Qlik Cloud and list the top 10 features
- What is Qlik-embed for and how do I set it up?
- Create a list of 10 keywords glossary for Qlik Predict

Validate each response to confirm that your data sources have been properly added and indexed by the knowledge base.

## Control access to assistants and knowledge bases with spaces

Keep your assistants and knowledge bases in different spaces to manage what content is available in your assistant for different users.

When using the assistant, users get answers limited by which knowledge bases they have access to. If they do not have permission to access data sources in a space, the answers they receive will not use knowledge bases from that space. By keeping assistants and knowledge bases in separate spaces, you can control which what kinds of answers users can get from a single assistant.

When controlling access with spaces, consider use the assistant settings to manage the welcome message, conversation starters, and the error messages to help explain to users why they may not get answers to certain questions. Review the conversation history of your assistant and evaluate user feedback to manage content in your knowledge bases in case users need broader or more narrow scopes of information.

To learn more about space permissions for knowledge bases and assistants, see [*Qlik Answers access and permissions*](qlik-answers-permissions.htm)

## Keep your knowledge bases specific in scope

When creating knowledge bases, limit the scope of data sources within a single knowledge base to a specific category or domain.

A narrow knowledge base scope keeps the information sources focused on the specific subject, which in turn helps assistants answer questions on the subject more easily. With specific knowledge bases, it is also easier to tailor the exact information available in assistants. It also makes it easier for curators to manage and validate content from a knowledge base when it has a specific and defined scope.

Additionally, when you have specific knowledge bases, if it easier to control user access to specific categories or domains of information. By putting each knowledge base in a separate space, you can tailor user access to these sources using separate permissions in each space. Even if an assistant has all possible knowledge bases, users will only get answers using knowledge bases that their space permissions allow them to access. This allows a single assistant to offer different users different answers based on what information it is appropriate for them to access.

Tip noteWhen mapping user role-based access to assistant data sources, consider drawing a diagram to map out the appropriate space requirements and settings.

## Create reusable knowledge bases

When creating knowledge bases, it is better to create reusable knowledge bases rather than making new knowledge bases for each assistant. When you create knowledge bases that are reusable, you avoid redundant indexing of content that has already been indexed elsewhere. Modularity of content allows you to quickly assemble and tailor assistants for different users while limiting the number of new knowledge bases you need to create.

Examine your intended data sources and map them to what can be shared broadly, what can be shared within a related category or domain, and what may truly be specific to a single assistant.
