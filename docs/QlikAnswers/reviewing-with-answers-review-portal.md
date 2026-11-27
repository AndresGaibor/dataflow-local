---
title: "Reviewing conversations from Qlik Answers agentic experiences"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/reviewing-with-answers-review-portal.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers"]
---

# Reviewing conversations from Qlik Answers agentic experiences

You can review conversations from Qlik Answers agentic experiences in the review portal. This portal provides visibility into interactions across agents.

Answers review portal provides a comprehensive view of Qlik Answers agentic conversations in your tenant. Unlike assistant-specific review, which focuses on a single Qlik Answers assistant, the review portal allows you to monitor and review interactions from multiple agent contexts. For reviewing conversations specific to a single assistant, see [*Reviewing assistant conversations*](Assistants/reviewing-assistant-conversations.htm).

Information noteTo access Answers review portal, you must have a custom role with the Agentic AI > Review agent and chat interactions permission set to Allowed. For more information about user permissions, see [*Default permissions and custom roles*](../Admin/permissions-scopes.htm).

You can access Answers review portal from the Analytics activity center. The review portal displays a table with conversations from different agent contexts. Conversations from the following contexts are supported:

- Help specialist
- Assistants
- Applications

Answers review portal, showing feedback for the Help specialist.

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_answers-review-portal.png "Click to view full size")

You will only see conversations from content to which you have access. By default, you will see questions to the Help Agent. For assistants and applications, you must have the following space permissions:

- Shared spaces: You must have Can edit or greater permission in the space containing the assistant or application.
- Managed spaces: You must have Can contribute or greater permission in the space containing the assistant or application.

## Understanding the review table

The review table summarizes key details for agent conversations. The following columns are included:

- Question: The question asked by the user. If the question is cut off, hover over it to view the question in full.
- Answer: The agent's answer to the question. Click the answer to view it in full. To view the sources used, click View source.
- Context: The agent context where the conversation occurred, such as the assistant or application.
- Feedback: Shows if the answer was liked or disliked.
- Reason: If the answer was disliked, the reason the user disliked the answer.
- Additional feedback: Any comments the user included with their feedback. If the comment is cut off, hover over it to view the comment in full.
- Date & time: When the question was asked.
- Status: If the question had feedback, whether the question has been reviewed or not.

You can sort the table with the following columns:

- Feedback
- Date & time
- Status

You can sort by multiple columns by holding CTRL while selecting a column.

The review table includes filters to help you quickly find conversations. You can filter to display:

- Questions with likes
- Questions with dislikes
- By context:

  - Help specialist
  - Assistant
  - Application
- Questions with specific reasons for dislikes
- Questions status (reviewed or not reviewed)
- Questions from a date range.

## Viewing and reviewing conversation details

For each conversation, you can click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) for the following options:

- Mark as reviewed: Mark the conversation as reviewed.
- View answer details: View the conversation, including sources. You can view the full conversation if the question was part of a larger conversation.

When you view answer details, the conversation shows both the question and answer. In the answer, you can click View source to view the sources used. You can also click individual citations to view the source for specific parts of the response.

Viewing a conversation

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_answers-review-portal-answer-details.png "Click to view full size")
