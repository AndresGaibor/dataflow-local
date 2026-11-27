---
title: "Troubleshooting skills"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/Skills/troubleshooting-skills.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Working with skills"]
---

# Troubleshooting skills

Resolve common issues that can occur when you create, add, or use skills in Qlik Answers.

## A skill never loads on data questions

A question that would require a chart, such as "Show sales by brand", uses the skill, but questions that would not require a chart, such as "How many shrubs are in the catalog?", do not use the skill and no loading step appears.

Possible cause

The skill description probably implies that the skill is only needed for charts.

Proposed action

Rewrite the description around the action. For example:

- "Load this skill before you create any chart, whether or not the user asked for one"
- "Load this skill first, before any data lookup"

## A skill works on counts but misses lists and rankings

A greeting skill is used for count questions and for greetings such as "hi", but is not used for list, ranking, and filter questions. For example, "Tell me the tallest perennials", "Which plants need full sun and low water?", or "Top 5 shrubs by spread".

Possible cause

When a question maps directly to a table query, the agent plans the data step first and does not check the list of skills again.

Proposed action

In the description, state that the skill must load before any data lookup, table, chart, or search. Name the question types it covers:

- Counts
- Lists
- Rankings, with example words such as "tallest", "most", and "top 10"
- Filters

Also include the rule itself in the description.

## A skill loads, but the output is still wrong

A chart color skill loads for a combo chart, but the chart still uses several colors. A greeting skill can also load, but the greeting is still missing from the answer.

Possible cause

The body of the skill is too general, such as "use green for charts". The default color scheme of the combo chart is used because the skill does not say otherwise.

Proposed action

Make the body more specific:

- Add one line for each output type. For example, "Combo chart: also single color. Do not fall back to the combo chart's default multi-color scheme".
- Use exact values.
- Add a final check for the agent to run before answering.

## A skill uses the right filter but returns the wrong count

A question such as "How many financed deals?" returns the number of customers with a loan, instead of the number of loan deals.

Possible cause

The application has no order ID. The agent filters correctly, but then counts distinct customers. One customer can buy several cars.

Proposed action

In the body, define what to count. For example: "How many cars, deals or orders = the number of sale records that match. One row is one sale. Never count distinct Customer\_ID."

## A one-off request carries over to later answers

A user asks for a red chart, and the next chart is also red. After a question about a calendar year, the next question about "last year" also uses the calendar year.

Possible cause

The skill does not say how long a request from a user lasts, so the agent applies the request for the rest of the chat.

Proposed action

In the body, separate one-off requests from standing requests. For example:

"A one-off request covers this answer only. A request with 'from now on', 'always' or 'stop' lasts for the rest of the chat."

## A skill applies to general questions

A general question such as "What is the difference between a hybrid and a plug-in hybrid?" gets the answer "the app doesn't distinguish them".

Possible cause

The description of the vocabulary skill covers every descriptive word about cars, not only the words used in the application data.

Proposed action

Limit the description to "this application's data", and add: "Not for general questions that are not about this application's data. Answer those from general knowledge."

To have an assistant decline general questions instead, see [*Example use case: Restricting general knowledge*](example-skill-general-knowledge.htm).

## A partial period is not flagged

A question such as "What were sales in FY2015?" returns the right number. However, the answer does not say that the data starts in January 2015, so the fiscal year has only six months of data.

Possible cause

The partial period check is only in the edge-case section of the skill. The agent runs one query without checking the first date in the data.

Proposed action

Move "Check the first and last date in the period before reporting it" into the main rule and into the final check.

## A comparison has the wrong total

For a question such as "Compare this year with last year", the skill is applied correctly. The right periods are used, the partial year is flagged, and the same months are compared. However, the agent adds six monthly figures in its answer text and gets the total wrong. For example, a 1.8% decline is reported as 4.4% growth.

Possible cause

The agent calculated the totals itself across a multi-step comparison. This is an issue with the accuracy of the agent, not with when the skill loads.

Proposed action

Add the following to the body: "Compute every compared period with its own query. Never add or subtract figures by hand."

Check comparison answers against the data.

## A second relevant skill is not loaded

A question such as "How many expensive cars did my dealership sell?" loads only the chart color skill. The agent uses its own threshold for "expensive", such as above average, and returns the wrong count.

Possible cause

The agent decides to create a chart and loads the chart skill. It then treats the brand filter as the main task. The business terms skill also has "expensive" in its description, but the agent does not load it for this question.

Proposed action

Do the following:

- In each description, name the question types that the skill covers. Include questions that also need a chart, such as "expensive cars by brand as a chart".
- In the chart skill, add "Other skills still set the numbers."
- Add questions that need more than one skill to your tests.

For more information, see [*Limitations*](working-with-skills.htm#Limitations) and [*Testing skills*](adding-skills.htm#Testing).

## A chart shows values that a skill should hide

A skill tells the agent never to show individual customer IDs. The skill loads, and the answer text does not include IDs. However, the answer can still include a bar chart of 300 customer IDs, while the text says that IDs are not shown.

Possible cause

A skill steers what the agent writes. It does not control the data that a chart or table query returns.

Proposed action

You cannot fix this with a skill. Use Section Access in the application, or remove the field from the data model. For more information, see [*Managing data security with Section Access*](../../Scripting/Security/manage-security-with-section-access.htm) and [*Limitations*](working-with-skills.htm#Limitations).
