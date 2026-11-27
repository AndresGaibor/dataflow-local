---
title: "Reviewing assistant conversations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/Assistants/reviewing-assistant-conversations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Working with assistants"]
---

# Reviewing assistant conversations

In Feedback, you can view your assistant's conversations and feedback from your users.

Feedback provides a table containing all the questions users have asked an assistant. You can select individual questions and view the answers with other details and information. You can also view questions in full conversations, with chat details and other information. You can filter the conversations by different criteria.

To review conversations in Feedback, you need one of the following user roles:

- Audit admin
- A user role with the permission Agentic AI > Review agent and chat interactions set to Allowed.

Tip noteFeedback allows you to review conversations within a specific Qlik Answers assistant. To review conversations from Qlik Answers agentic experiences in your tenant, use Answers review portal. For more information, see [*Reviewing conversations from Qlik Answers agentic experiences*](../reviewing-with-answers-review-portal.htm).

Feedback

![The Feedback section of an assistant, showing a table with questions.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_assistant-review-rev2.png "Click to view full size")

Feedback summarizes key details for your assistant’s conversations. The following columns are included:

- Question: The question asked by the user. If the question is cut off, hover over it to view the question in full.
- Answer: The assistant’s answer to the question. Click on the answers to view it in full. To view the sources used, click View source.
- Feedback: Shows if the answer was liked or disliked.
- Reason: If the answer was disliked, the reason the user disliked the answer.
- Additional feedback: Any comments the user included with their feedback. If the comment is cut off, hover over it to view the comment in full.
- Date & time: When the question was asked.
- Status: If the question had feedback, whether the question has been reviewed or not.

Feedback can be sorted by clicking the header of the following columns:

- Feedback
- Date & time
- Status

You can sort by multiple columns by holding CTRL while selecting a column.

Feedback includes filters to help you quickly find conversations. You can filter to display:

- Questions with likes
- Questions with dislikes
- Questions with specific reasons for dislikes
- Questions status (reviewed or not reviewed)
- Questions from a date range.

For each question, you can click ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) for the following options:

- Mark as reviewed: Mark as conversation as reviewed.
- View answer details: View the conversation, including sources. You can view the full conversation if the question was in a larger conversation.

## Viewing answer details

You can view questions and answers in more detail by clicking ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > View answer details on a question.

Conversation details shows both the question and answer as a conversation. In the answer, you can click View source to view the sources used. You can also click the citation to view the source for just that part of the response.

You can click Mark as reviewed to review the answer.

Viewing a full conversation

![The Review section, with a conversation open. View full conversation is selected, showing the question in convtext of the full conversation with the assistant.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_assistant-review-conversation-rev2.png "Click to view full size")

## Improving assistants using feedback

Reviewing your users' answers is key for content improvement. As answers are unique each time, with no specific caching, even similar questions may generate different answers and give users different experiences.

Provide your subject matter experts with access to assistants to review answers. They can help assess how the assistant is meeting user needs and if the data used by the assistant is serving the right purpose.

If not, you may need to look at improving your data sources to better meet user needs. For example, maybe feedback is indicating that there are gaps in the information that need to be filled. Alternatively, it may be that there are too many data sources in the knowledge bases used by the assistant. The assistant may need a smaller, more focused pool of resources to draw on.

You can also look at the kinds of information users are asking for, but that Qlik Answers cannot provide itself. For example, Qlik Answers does not create aggregate or ranked answers, but it can use aggregate and ranked content in the data sources. If your customers are looking for ranked answers or options in their questions, you can add that to the data sources used by the assistant.
