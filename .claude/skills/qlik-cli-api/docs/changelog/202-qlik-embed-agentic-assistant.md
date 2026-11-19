---
source: https://qlik.dev/changelog/202-qlik-embed-agentic-assistant/
last_updated: 2026-03-25T16:41:23+01:00
---

# qlik-embed adds Qlik Answers agent support with ai/agentic-assistant

The new `ai/agentic-assistant` UI brings the agentic [Qlik Answers](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/Qlik-Answers.htm)
experience in embedded format. It combines knowledge bases with a Qlik app to answer complex questions and surface
insights with citations and AI-generated explanations.

> **Cross-region inference required:** To use the agentic Qlik Answers experience, you must opt in to cross-region inference.
> This allows Qlik Cloud to temporarily process data outside your tenant region.
> For more information, see the [Qlik Answers documentation](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/Qlik-Answers.htm) on Qlik Help.

```html
<qlik-embed
  ui="ai/agentic-assistant"
  assistant-id="<ASSISTANT_ID>"
></qlik-embed>
```

You can also copy the embed code snippet from the assistant's settings:

![a screenshot of the AI assistant settings panel showing the embed code snippet](https://qlik.dev/_astro/ai-assistant-settings-panel.CZ1mBTH9.png)

Review the [ai/agentic-assistant parameters](https://qlik.dev/embed/qlik-embed/parameters/#aiagentic-assistant),
or learn more about the other [UIs and parameters in qlik-embed](https://qlik.dev/embed/qlik-embed/parameters/).
