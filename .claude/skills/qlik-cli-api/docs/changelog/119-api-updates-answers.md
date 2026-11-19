---
source: https://qlik.dev/changelog/119-api-updates-answers/
last_updated: 2025-01-16T11:31:06Z
---

# New APIs - Qlik Answers Assistants and Knowledgebases APIs

> Updated on January 16, 2025: Paths to the invoke and stream endpoints were corrected.

Qlik Answers leverages two services - Knowledgebases and Assistants - to first build the
data leveraged by an assistant and then configure the assistant. The [Knowledgebases API](https://qlik.dev/apis/rest/knowledgebases/)
and [Assistants API](https://qlik.dev/apis/rest/assistants/) are now published and generally available
for programmatic use cases.

These APIs support both the configuration of Qlik Answers, as well as asking questions
to an Assistant by using the `/api/v1/assistants/{assistantId}/threads/{threadId}/actions/invoke`
or `/api/v1/assistants/{assistantId}/threads/{threadId}/actions/stream`
endpoints, allowing you to create your own embedded version of Qlik Answers.

This release complements the previously available [qlik-embed support for Qlik Answers](https://qlik.dev/changelog/103-qlik-embed-ai-assistant/),
which allows you to embed the native user interface into your web applications
and portals.

For more information:

- Learn how to use [Qlik Answers](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/Qlik-Answers.htm).
- Review the specifications for the [Assistants API](https://qlik.dev/apis/rest/assistants/)
  and [Knowledgebase API](https://qlik.dev/apis/rest/knowledgebases/).
