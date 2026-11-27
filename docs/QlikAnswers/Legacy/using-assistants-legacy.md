---
title: "Answering questions with legacy assistants"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/Legacy/using-assistants-legacy.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Qlik Answers legacy experience"]
---

# Answering questions with legacy assistants

Chat with legacy assistants, view and download source documents, manage conversations, and more.

Legacy assistants are similar to assistants, but only get answers from unstructured data sources. Unlike assistants, legacy assistants cannot be accessed from Qlik Answers in the navigation bar and must be accessed from the catalog.

Each legacy assistant is connected to one or more curated knowledge bases. These knowledge bases contain data sources such as PDF documents, PowerPoint presentations, and other unstructured data. As you ask questions, answers are sourced using retrieval augmented generation (RAG) from the knowledge bases, ensuring the responses are relevant to your needs. You can view the sources used to create the answers.

Qlik Answers legacy assistant

![An assistant showing the full-screen chat.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_assistant-full-chat.png "Click to view full size")

You require user role permissions to ask legacy assistants questions. For more information, see [*Qlik Answers access and permissions*](../qlik-answers-permissions.htm).

If you have permissions to create and edit legacy assistants, see [*Working with legacy assistants*](legacy-assistants.htm) for more information.

## Navigating legacy assistants

When you open a legacy assistant, what you see will depend on your Qlik Answers user permissions and your space role. Qlik Answers has the following sections for users with view and chat access:

- Overview: Information about the legacy assistant.
- Chat: Expandable and collapsible chat interface.

## Chatting with legacy assistants

You can chat with a legacy assistant by:

- Entering your question
- Clicking the microphone icon (if your browser's voice-to-text capability is supported in Qlik Answers).

Qlik Answers will then generate a response.

You can ask follow-up questions. Qlik Answers will understand the context from the previous question. If you want to start a new thread of conversation, click New conversation.

Tip note

If your chat is collapsed, click Chat and click New conversation.

A collapsed Qlik Answers chat

![A collapsed assistant chat.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui-assistant-chat-question.png "Click to view full size")

Assistants may include default conversation starter questions. If you click a conversation starter, it will ask Qlik Answers that question.

Chat with conversation starters

![A collapsed chat with 3 conversation starters.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_assistant-chat-conversation-starters.png "Click to view full size")

## Viewing and downloading sources in legacy Qlik Answers

If you have permission, you can view the sources used by Qlik Answers in its responses. Click View <number> sources in a response to view the sources.

Viewing sources used in an answer

![Viewing the sources used by Qlik Answers for generating a selected answer.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_assistant-chat-sources.png "Click to view full size")

Click ![Copy to clipboard](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_copy.svg)to copy the text used from that source. If you have access to the data source used, you can download the source by clicking ![Download](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_download.svg).

## Managing conversation history in legacy Qlik Answers

You can view previous conversations and saved conversations in Conversations. Conversations is available in the full screen view or by clicking Chat > Conversations. Conversations shows your previous history of interactions with the assistant as conversation threads. You can select conversations to view the individual interactions between you and the assistant from that session. You can still interact with the responses to each of your questions, such as liking or disliking them, just as you can with responses in an active conversation.

Conversations  has two sections, Saved and History. History contains your most recent conversations with the assistant. Conversations in your history are removed after a period of time, but you can save important conversations to Saved

Tip note

To view Conversations If your chat is collapsed, click Chat and click Conversations.

By default, your conversation threads are named with the first question asked. You can rename conversations.

Select a conversation to view it. Click ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) to perform actions on a conversation. You can:

- Save
- Remove from saved
- Rename
- Delete

## Providing feedback on responses in legacy Qlik Answers

You can provide feedback to the responses Qlik Answers generates. Click ![Like](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_like_outlined.svg) or ![Dislike](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_dislike_outlined.svg) beside a generated response to rate it. If you click ![Dislike](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_dislike_outlined.svg), you can provide a reason why it was not helpful and optionally provide additional feedback.

Feedback options

![The Improve future answers dialog. The following feedback options are available: Inaccurate, Irrelevant, Repetitive, Unhelpful, and Other. There is a text box for adding additional feedback.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_assistant-chat-feedback.png "Click to view full size")

Feedback is useful to the assistant and knowledge base owners, so they can use it to improve their assistant and knowledge curation.

## Voice-to-text data transfer considerations in legacy Qlik Answers

In many internet browsers, Qlik Answers voice-to-text search functionality uses the [Web Speech API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Speech_API) for external processing of voice-to-text data. The user’s internet browser may send the audio recorded by the browser API to an external source for transcription. Voice processing will be handled by the web service chosen by the user’s web browser. As a result, the captured information could be sent to a third-party server. The data is therefore not guaranteed to stay within the user’s Qlik region. Qlik is not responsible for the data processing by this third-party.

If users want to restrict this information flow to their relevant third-party browser (turn off the voice-to-text feature), this can be achieved through specific controls, including settings within their browser of choice and other security configurations.

## Limitations

Chat has the following limitations:

- There is a 1,000 character limit per question in chat.
