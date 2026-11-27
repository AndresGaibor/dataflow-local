---
title: "Reviewing legacy assistant conversations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/Legacy/reviewing-legacy-assistant-conversations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Qlik Answers legacy experience", "Working with legacy assistants"]
---

# Reviewing legacy assistant conversations

In Review, you can view your legacy assistant's conversations and feedback from your users. Reviewing requires the audit admin user role.

Review provides a table, Review feedback, with filters contains all the questions users have asked a legacy assistant. You can select individual questions and view the answers with other details and information. You can also view questions in context of larger conversations. chat details, and other information. You can filter the conversations by different criteria. You can download data from the table.

Review

![The Review section of an assistant, showing a table with seven questions.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_assistant-review-rev.png "Click to view full size")

Review feedback summarizes key details for your legacy assistant’s conversations. The following columns are included:

- Question: The question asked by the user. If the question is cut off, hover over it to view the question in full.
- Answer: The assistant’s answer to the question. If the answer is cut off, hover over it to view the answer in full.
- Feedback: Shows if the answer was liked or disliked.
- Reason: If the answer was disliked, the reason the user disliked the answer.
- Comment: Any comments the user included with their feedback. If the comment is cut off, hover over it to view the comment in full.
- Status: If the question had feedback, whether the questions has been reviewed or not.
- Sources used: What sources the legacy assistant used to answer the question. You can hover over cells in Sources used to view the names of the sources.
- Date & time: When the question was asked.

Review feedback can be sorted by clicking the header of the following columns:

- Feedback
- Status
- Date & time

You can sort by multiple columns by holding CTRL while selecting a column.

Review feedback includes filters to help you quickly find conversations. You can filter to display:

- Unanswered questions
- Questions with likes
- Questions with dislikes
- Questions with specific reasons for dislikes
- Questions answered by specific knowledge bases
- Questions status (reviewed or not reviewed)
- Questions from a date range.

For each question, you can click ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) for the following options:

- View conversation details: View the conversation, including sources. You can view the full conversation if the question was in a larger conversation.
- Create conversation starter: Turn the conversation into a conversation starter.

## Viewing conversation details

You can view questions and answers in more detail by clicking ![More](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > View conversation details on a question.

Conversation details shows both the question and answer as a conversation. In the answer, you can click View <number> sources to view the sources used. You can click Mark as reviewed to review the answer. In the question, click Create a conversation starter to add a question as a conversation starter.

If you select View full conversation, you can see the question in context of the full conversation with the legacy assistant.

Viewing a full conversation

![The Review section, with a conversation open. View full conversation is selected, showing the question in convtext of the full conversation with the assistant.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_assistant-review-conversation-rev.png "Click to view full size")

## Downloading conversation data for review

You can download data from the Review feedback table as a CSV file. You can download all the content currently displayed in the table. You can also select individual rows to download.

Information noteSpecial characters in the legacy assistant name are removed from the file name when downloading.

Do the following:

1. In Review, click Download.

   Optionally, you can select specific conversations to download.
2. Click Download.
3. If you have conversations selected, select Download all or Download selected.
4. Click Download.

## Improving legacy assistants using feedback

Reviewing your users' answers is key for content improvement. As answers are unique each time, with no specific caching, even similar questions may generate different answers and give users different experiences.

Provide your subject matter experts with access to legacy assistants to review answers. They can help assess how the legacy assistant is meeting user needs and if the data used by the legacy assistant is serving the right purpose.

If not, you may need to look at improving your data sources to better meet user needs. For example, maybe feedback is indicating that there are gaps in the information that need to be filled. Alternatively, it may be that there are too many data sources in the knowledge bases used by the assistant. The legacy assistant may need a smaller, more focused pool of resources to draw on.

You can also look at the kinds of information users are asking for, but that Qlik Answers cannot provide itself. For example, Qlik Answers does not create aggregate or ranked answers, but it can use aggregate and ranked content in the data sources. If your customers are looking for ranked answers or options in their questions, you can add that to the data sources used by the legacy assistant.
