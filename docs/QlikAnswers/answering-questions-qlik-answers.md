---
title: "Answering questions with Qlik Answers"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/answering-questions-qlik-answers.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Using Qlik Answers and choosing your context"]
---

# Answering questions with Qlik Answers

Chat with Qlik Answers to get answers to your questions, create charts and sheets, view sources, manage conversations, and more.

Qlik Answers provides an agentic generative AI (GenAI) chat experience for asking questions and getting answers from your data sources. You can conversationally explore your structured and unstructured data in these contexts:

- Help
- Answers assistants
- Application analysis

As you ask questions, the Qlik Answers agent interprets them and builds responses from the available sources so that the responses are relevant to your needs. You can view the sources used to create the answers.

Click Qlik Answers in the navigation bar to start asking questions.

Qlik Answers open, showing available contexts

![An open Qlik Answers agentic chat, contexts to choose from: Help, Application analysis, and Answers assistants](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_QlikAnswersAgents-rev.png "Click to view full size")

You can expand Qlik Answers to full-screen mode for better readability of detailed responses. Click the ![Expand](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expand_3_outline.svg) in the chat interface to open full-screen mode. In full-screen mode, you can access conversation history and view sources through side panels.

Qlik Answers in full-screen mode

![Qlik Answers in full-screen mode, showing the history panel, main chat area, and close button in the top bar](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_QlikAnswersFullScreen-rev2.png "Click to view full size")

You can also access a full-screen Qlik Answers chat from Answers in the navigation menu in the Insights and Analytics activity centers.

You require user role permissions to ask Qlik Answers questions. For more information, see [*Qlik Answers access and permissions*](qlik-answers-permissions.htm).

If you have permissions to create and edit assistants, see [*Working with assistants*](Assistants/assistants.htm) for more information.

## Chatting with Qlik Answers

To start a chat, open Qlik Answers and select the context you want to work in. If you have an open application that is activated for Qlik Answers, the application is selected by default.

Qlik Answers chat

![Qlik Answers chat session, with an application selected. The user is asking How did sales change in this October compared to October last year](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_QlikAnswersChat-rev.png "Click to view full size")

Enter your question and Qlik Answers generates a response. If Qlik Answers needs more details, it asks clarifying questions.

Qlik Answers provides responses that are as complete as possible, including charts and recommendations. Qlik Answers selects the most appropriate visualizations based on your question and the underlying data context.

Tip noteQlik Answers can remember your preferences, such as for chart colors and currency. Tell it what you prefer, and it applies your preferences to future content. For more information, see [*Remembering your preferences in Qlik Answers*](Qlik-Answers-learning-memory.htm).

Information note

Qlik Answers can combine insights from your data with the AI model’s broader general knowledge. Citations are always provided so you can understand where the information came from and assess its relevance. Review the cited sources before sharing or acting on the response. For more information, see [*Answers from general knowledge*](#Answers).

Qlik Answers response, with charts and recommendations

![A Qlik Answers response, indicating sales were up 6.6% from last October. The response offers three follow-up questions.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_QlikAnswersResponse-rev.png "Click to view full size")

You can request specific charts or sheets, including the type of chart to use. For example:

- Show me a bar chart of sales by region.
- Create a KPI for total revenue.
- Display a line chart of trends over time.

For more information about generating charts and sheets, see [*Creating and editing application content with Qlik Answers*](#Generati).

You can ask follow-up questions. Qlik Answers understands the context from the previous question. Qlik Answers can also suggest follow-up questions. Click a suggested follow-up question to ask it.

If you want to start a new conversation, click ![Start new chat](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg). In a conversation thread, if you want to ask the previous question again without the context of the previous questions and responses, click ![Reload in a new chat without context](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_reload.svg).

Applications and assistants may include default conversation starter questions. Click a conversation starter to ask Qlik Answers that question.

### Approving tool use

Depending on your question, Qlik Answers may need to use a tool to generate the response, such as when creating a sheet. Qlik Answers asks for approval the first time it needs to use a tool. You can choose to approve it once, approve it for all future requests, or deny the use of the tool.

For more information, see [*Managing Qlik Answers tools*](qlik-answers-tools.htm).

Request for tool approval

![A request to approve the tool Forget, with the options Deny, Always allow, and Allow once.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_tool-use.png "Click to view full size")

### Asking questions about charts in applications

If you are using Qlik Answers in an open application, you can also select charts in a sheet to add them to the chat context and ask specific questions about the data in those charts.

When you select a chart, the chart name is added to the chat. If you want to ask questions about multiple charts, select each chart in the sheet and click ![Keep in context](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) on the chart name in the chat to keep it in context.

Multiple charts selected for a question in Qlik Answers

![A chat with multiple charts added as context to the user's question.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_answers-chart-edit-multiple.png "Click to view full size")

### Answering questions using advanced analytics

In addition to answering questions from your sources, Qlik Answers can handle the following kinds of advanced analytics:

- Predictive: Forecasts values, classifies records, flags anomalies, and segments your data.
- Prescriptive: Identifies what drives a result and helps you decide what to do next.
- Simulation: Shows the range of possible outcomes when inputs are uncertain.
- Optimization: Finds the best allocation or plan within your constraints.

#### Predictive

Use the predictive skill to forecast values, score risk, detect anomalies, or segment customers. You can ask in plain language, and Qlik Answers uses the data in your applications to answer.

Responses include:

- A summary of the result, such as a forecast value with its 95% range, the number of customers flagged as high risk, or the number of segments found.
- An explanation of the model quality and the main drivers.
- A note that the trained model is temporary.

Example questions

- Forecast unit sales by month for the next two quarters.
- Which customers are likely to churn?
- Flag unusual transactions in last month's data.
- Group our distributors into segments by order size and frequency.

#### Prescriptive

Use the prescriptive skill to test whether a factor causes an outcome, rather than only correlating with it. Qlik Answers validates the result. If the result passes validation, Qlik Answers can use it to recommend what to do next.

Responses include:

- A one-sentence answer, such as the estimated change in revenue per transaction.
- The range in which the estimate could fall.
- Whether the validation checks passed.
- A diagram of the assumed cause-and-effect structure.

If the validation checks fail, Qlik Answers tells you that the result might not be valid and does not present it as a finding.

Example questions

- Do discounts actually raise revenue, or do we just discount the products that already sell?
- Does AI adoption drive down freight costs, and which warehouses should come online first?
- Does having an executive sponsor make deals bigger, or do big deals just attract sponsors?
- Which branches have the worst default rates, and where should we focus intervention?

#### Simulation

Use the simulation skill to see the realistic range of outcomes for a plan. Qlik Answers runs many scenarios with random variation and shows the likely case, the downside, and the upside. You can use the results to size reserves and set targets based on the risk.

Responses include:

- A headline range, such as the most likely revenue with worst-case and best-case figures.
- A table of scenarios, from pessimistic to optimistic.
- An explanation of the downside in business terms, with a suggestion of what to plan for.

Qlik Answers does not show the methodology unless you ask for it.

Example questions

- What is the range of revenue if demand varies by 20% either way?
- If cloud costs move up or down by 25%, what is the impact on total spend?
- How bad could defaults get if conditions worsen by 20%?
- What is the 95th percentile downside if costs rise 15% and demand drops 10%?

#### Optimization

Use the optimization skill to find the best plan for a goal within your limits, such as budget or capacity. Qlik Answers returns a recommended plan. If your limits cannot all be met, Qlik Answers tells you what would need to change.

Responses include:

- The recommended decision, such as the expected revenue of the best plan.
- A table of recommended allocations, sorted by size.
- If your limits conflict, which limit Qlik Answers loosened and by how much. You can then choose to raise the limit or accept a lower target.

Example questions

- How should we allocate inventory across warehouses to maximize profit?
- How should we split the budget across channels within a $1M cap?
- Minimize transport cost given warehouse capacity limits.
- I need to close $5M this quarter. Is that realistic given the funnel?

### Using actions with assistants

Assistants can offer you actions to take. Actions run automations that assistant creators added to their assistants, for tasks such as sending an email or updating an external source based on the insights uncovered.

Tip note

You can ask an assistant what actions it has available.

When you ask an assistant something related to one of its actions, depending on how the assistant creator configured the action, the assistant either:

- Prompt you to confirm running the automation.
- Start the action without confirmation.

A prompt to run an automation

![Qlik Answers showing a confirmation to start automation message. The message provides the name and description of the automation, with a start automation button.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_assistant-automation-prompt-rev.png "Click to view full size")

Some actions require you to provide input or confirm details before the action runs. The assistant shows you what will be sent before running the automation. After you confirm, the action runs and returns the result in the conversation.

Information note

You cannot ask new questions in the same conversation thread while an automation is waiting for confirmation.

You can view which action and automation were used in the sources section of the response, with a link to the action's run history.

### Creating and editing application content with Qlik Answers

You can use Qlik Answers to generate content for your applications. You can add charts that Qlik Answers generates to your sheets. If you know the kind of chart you want in your application, you can also ask Qlik Answers to generate specific charts. Qlik Answers supports generating the following chart types:

- Bar chart

  [*Bar chart*](../Visualizations/Bar-Chart/bar-chart.htm)
- Combo chart

  [*Combo chart*](../Visualizations/ComboChart/combo-chart.htm)
- KPI

  [*KPI*](../Visualizations/KPI/KPI.htm)
- Line chart

  [*Line chart*](../Visualizations/LineChart/line-chart.htm)
- Pie chart

  [*Pie chart and donut chart*](../Visualizations/PieChart/pie-chart.htm)
- Pivot

  [*Pivot*](../Visualizations/VisualizationBundle/pivot-object.htm)
- Scatter plot

  [*Scatter plot*](../Visualizations/ScatterPlot/scatter-plot.htm)
- Straight table

  [*Straight table*](../Visualizations/StraightTable/sn-straight-table.htm)
- Tree map

  [*Treemap*](../Visualizations/TreeMap/treemap.htm)

In addition to charts, you can also ask Qlik Answers to generate sheets for you. For example, you could ask Create a sheet that examines the impact of discounts on sales by region.

When generating charts and sheets, you can request specific charts or analyses. For example, if you want a chart of sales for the previous 30 days, always relative to the current date, you could ask: Create a chart for the last 30 days of sales, analyzing performance by country and sales office. I want the 30 days to update so that they are always relative to the current date.

Creating a specifically requested chart

![A response to a question asking for a bar chart, showing a bar chart, with results that roll for the last 30 days](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_QlikAnswersChartRequest-rev.png "Click to view full size")

Information noteQlik Answers uses your permissions when determining what you can see and do in an app. If you do not have permission to create sheets in an app, you cannot generate new content for that app.

Tip note

If you are not sure what kind of analyses Qlik Answers can generate for you, try asking Qlik Answers what it can tell you about your data and what analyses it sees.

Tip note

If you do not get the chart you wanted, ask again and describe in more detail what you want to see.

#### Adding charts to sheets

If you are using Qlik Answers within an application, you can add generated charts to your sheets. You can add them to existing sheets or new sheets.

Do the following:

1. On the generated chart, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) > Add to sheet.
2. Select an existing sheet or create a new sheet.
3. Click Add to existing sheet or Add to new sheet.

#### Creating sheets with Qlik Answers

You can ask Qlik Answers to create sheets in your application. For example, the prompt Create a new sheet showing sales data by customer for Boston generates a sheet in the app. You can request multiple sheets in a single request, but for the most reliable results, limit each request to one or two sheets.

Generating a sheet

![A Qlik Answers-generated sheet, with multiple charts showing the discount effectiveness by sales office.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_QlikAnswersSheetCreation-rev.png "Click to view full size")

Your generated sheets appear in the AI Generated section under Your own sheets. You can move sheets out of this section or make them public.

#### Editing charts with Qlik Answers

You can edit charts using Qlik Answers by selecting a chart in a sheet and then requesting the desired changes in Qlik Answers. When a chart is selected in Qlik Answers, Qlik Answers shows the name of the selected chart in the chat.

Editing a bar chart to change dimensions using Qlik Answers

![Editing a chart with Qlik Answers to change the dimension from City to Country.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_answers-chart-edit.png "Click to view full size")

You can edit multiple charts at once. Select each chart in the sheet and click ![Keep in context](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) on the chart name in the chat to keep it in context.

Multiple charts selected for editing in Qlik Answers

![Multiple charts selected for editing in Qlik Answers](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_answers-chart-edit-multiple.png "Click to view full size")

You can use Qlik Answers to change dimensions, measures, limits, sorting, and colors. For example, you could select a bar chart and ask Change the dimension YearMonth to Year quarter. Color the chart by the master measure Sales.

Information noteChanging dimensions and measures in a chart might reset some properties, such as limitations and trend lines.

### Summarizing indexed files

Qlik Answers can list available files and provide document summaries when you ask an assistant about the indexed files in its knowledge bases. For example, you can ask questions such as:

- What files are available?
- Give me an overview of <filename>.
- Summarize <filename>.

Available files for an assistant and a summary of a file in Qlik Answers

![A summary what files are available and the content of Managed data.pdf](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_summary.png "Click to view full size")

You can ask for an overview summary or a detailed summary with citations. You can only ask for one file summary at a time.

## Viewing and downloading sources

If you have permission, you can view the sources used by Qlik Answers in its responses. Click View sources in a response to view the sources. Sources are broken down by their citations in the response. You can also click the citation links in responses to view the sources for just that part of the response.

When you view the source, you can see:

- The user prompt
- How Qlik Answers arrived at the response
- The answer breakdown by source
- The data and expressions used for the charts (if charts were generated)
- The text used for the response (if a knowledge base was used)

  Click ![Copy to clipboard](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_copy.svg) to copy the text used from that source. If you have access to the data source used, you can download the source by clicking ![Download](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_download.svg).

Viewing sources used in an answer for a specific chart

![Viewing the sources for a Qlik Answers response](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_QlikAnswersViewSourceChart-rev.png "Click to view full size")

## Managing conversation history

You can view previous conversations in the menu. Your full conversation history is available by clicking ![Open menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_menu.svg) and clicking View all. Your conversation history shows your previous interactions as conversation threads. You can select conversations to view the individual interactions between you and the assistant from that session. You can still interact with the responses to each of your questions, such as liking or disliking them, just as you can with responses in an active conversation.

Conversation history for an application

![History in Qlik Answers](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_QlikAnswersViewHistory-rev.png "Click to view full size")

By default, your conversation threads are named with the first question asked. You can rename conversations.

Select a conversation to view it. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) to perform actions on a conversation. You can:

- Rename
- Delete
- Pin
- Unpin

### Pinning conversations

Pin the conversations you return to most often. Pinned conversations appear in the Pinned section above Recents in the menu, so new conversations do not push them down the list.

Pins are saved to your account and remain in place when you reload or return later. Pins are personal. Other users cannot see which conversations you pinned.

The menu shows up to five pinned conversations. If you have more, click View all pinned to show all of them. Click Show less to collapse the list.

When you search your conversation history, the Pinned group is hidden, and pinned conversations that match your search appear with the other results

#### Pinning conversation from Recents

Do the following:

1. Click ![Open menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_menu.svg).
2. Under Recents, hover over the conversation and click ![Pin](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_pin_outline.svg).

#### Pinning conversation from your full conversation history

Do the following:

1. Click ![Open menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_menu.svg) and then click Chats.
2. Hover over the conversation and click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg).
3. Click Pin.

#### Unpinning conversations

When you unpin a conversation, it returns to Recents in date order. When no conversations are pinned, the Pinned section is hidden.

Do the following:

- Do one of the following:

  - In the Pinned section of the menu, click ![Unpin](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_pin.svg) next to the conversation.
  - In your full conversation history, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the conversation and then click Unpin.

## Providing feedback on responses

You can provide feedback on the responses Qlik Answers generates. Click ![Like](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_like_outlined.svg) or ![Dislike](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_dislike_outlined.svg) after a generated response to rate it. If you click ![Dislike](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_dislike_outlined.svg), you can provide a reason why it was not helpful and optionally provide additional feedback.

Feedback options

![The Improve future answers dialog. The following feedback options are available: Inaccurate, Irrelevant, Repetitive, Unhelpful, and Other. There is a text box for adding additional feedback.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_assistant-chat-feedback.png "Click to view full size")

Assistant and knowledge base owners can use your feedback to improve their assistants and knowledge bases.

## Downloading responses

You can download responses as PDFs. Click ![Download](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_download.svg) in the response to download it.

## Answers from general knowledge

When a question is unrelated to any available data source, or when the connected sources cannot fully answer it, Qlik Answers uses general knowledge from the underlying AI model to complete the response.

Qlik Answers does not require a connected data source to answer a general knowledge question, and it does not use web search to do so.

Answers from general knowledge are indicated in the following areas:

- Source citation: Answers using general knowledge have AI beside the source citation in the response.

  Source citation showing the use of general knowledge

  ![The response to the question what is the capital of Sweden. There is a citation marked AI beside the answer of Stockholm.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_general-knowledge-answer-citation-rev.png "Click to view full size")

If a question is partially answered by your connected data, Qlik Answers combines the sourced portion with general knowledge and labels each part accordingly.

Information noteGeneral knowledge answers are not grounded in your data. They reflect the AI model's training data and are not guaranteed to be current. Review this content before sharing or acting on it, consistent with the GenAI Warning that applies to all Qlik Answers output.

## Exploring Discovery Agent insights with Qlik Answers

You can explore insights in your Discovery Agent feed in Qlik Answers. You access this functionality from your feed by clicking ![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_answers_outline.svg) Explore further in Answers on an insight card. For more information, see [*Navigating insights in feeds*](../DiscoveryAgent/feeds-navigate.htm) and [*Analyzing Discovery Agent feeds*](../DiscoveryAgent/feeds.htm).

## Limitations

Qlik Answers agentic chat has the following limitations:

- There is a 500-character limit per question in chat.
- Visualizations generated by Qlik Answers have the following limitations:

  - Properties outside of dimensions, measures, limits, sorting, and color specification are not supported by Qlik Answers and must be set by the user.
  - The following visualizations are not supported:

    - Box plots
    - Distribution plots
    - Funnel charts
    - Histograms
    - Map charts
    - Org charts
    - Pivot tables
    - Sankey charts
    - Waterfall charts
  - Dashboard visualizations are not supported.
  - Legacy visualizations are not supported.
  - Custom extensions are not supported.
