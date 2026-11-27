---
title: "Understanding Qlik Answers AI readiness score"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/BusinessLogicAI/understanding-ai-readiness-score.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Working with applications in Qlik Answers", "Optimizing your application for Qlik Answers with business logic", "Viewing the overview of business logic for Qlik Answers"]
---

# Understanding Qlik Answers AI readiness score

The AI readiness score helps you understand how well your application is configured for Qlik Answers to interpret your data. A higher score indicates better preparation for AI-powered analytics.

## What is the AI readiness score

The AI readiness score evaluates how your application is configured across three pillars. It gives a score as a percentage from 0% to 100% and lists suggestions with recommendations you can act on. The score is advisory: it identifies opportunities to improve your application but does not change it automatically.

The score reflects the current state of your application's tables, fields, master items, and metadata. A higher score means Qlik Answers can more accurately reference your data when answering questions.

Information note

A high AI readiness score, including a score of 100%, does not guarantee that every answer will be correct.

A high score shows that your application gives Qlik Answers the structure and context it needs to interpret your data. It does not guarantee the result of every question. Answer quality also depends on factors the score does not measure, such as:

- How a question is phrased, and whether it can be read in more than one way.
- Whether the data in your application is complete and accurate.
- Whether your application contains the data needed to answer the question.

Before you share your application, ask Qlik Answers the questions your users are likely to ask and review the answers.

## Why AI readiness matters

Application configuration directly affects Qlik Answers performance. When users ask questions, Qlik Answers must identify the right fields, understand relationships, and interpret business meaning. Applications with higher readiness scores provide the context Qlik Answers needs to deliver accurate, relevant answers.

Without clear guidance, it is difficult to tell whether poor question results come from product limitations or from application setup. The AI readiness score shows what to improve.

## The three pillars

The AI readiness score evaluates your application across three equally weighted pillars. Improving any pillar can improve your overall score.

### Data model pillar

The data model pillar covers the tables, keys, and relationships used to navigate your data. This pillar identifies structural issues, such as disconnected tables, synthetic tables, and ambiguous relationships like fan traps and chasm traps. Data model suggestions are informational only. They require load script or data model changes outside AI optimization.

### Fields pillar

The fields pillar covers the names, visibility, and types that help Qlik Answers reference the right fields. This pillar surfaces ungrouped fields and master items, technical or unclear names, fields and master items that should be hidden, and master items without descriptions. You can resolve most suggestions in this pillar directly in AI optimization. Suggestions for master items that come from a data product must be resolved in the data product.

### Metadata pillar

The metadata pillar covers the descriptions, naming, and table setup that give Qlik Answers business context. This pillar highlights flat tables, missing date fields, chart expressions that have no master item, and charts with invalid expressions. You can create master items from chart expressions directly in AI optimization. Other metadata suggestions require changes in the load script or in charts.

## Informational and actionable suggestions

Suggestions fall into two categories:

- Informational suggestions identify issues that you resolve outside AI optimization, such as load script modifications, data model restructuring, chart expression fixes, or changes in a data product.
- Actionable suggestions identify issues that you can resolve directly in AI optimization, such as applying suggested master item descriptions, hiding unnecessary fields, grouping related fields and master items, or creating master items.

Some suggestions might offer options in the See details panel. You choose whether to act on them. For example, a suggestion might recommend hiding a text field with many distinct values, but you might choose to keep it visible because the field is important for your analysis.

For a full list of suggestions and how to address them, see [*Qlik Answers AI readiness suggestions summary*](ai-readiness-findings-reference.htm).

## How scores change over time

Your score updates as you act on recommendations and as your application data changes. A trend indicator shows whether your score improved or declined, and by how much, since the last calculation.

The score recalculates when the application syncs. Syncing happens automatically on a schedule, and you can also sync manually. Your score also updates after you reload application data. Syncing is available to all users with access to business logic for the application. For more information, see [*Sync application*](business-logic-overview-qlik-answers.htm#Sync).

## Master item descriptions

Master item descriptions help Qlik Answers understand your metrics and dimensions. Without a description, Qlik Answers relies on the master item name alone, which is unreliable for master items with similar names.

The fields pillar surfaces master items that lack descriptions. From See details, you can apply descriptions suggested by Qlik Answers. For master items that come from a data product, add the descriptions in the data product. Adding clear, business-focused descriptions improves both the score and Qlik Answers performance.
