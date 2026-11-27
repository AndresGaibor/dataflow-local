---
title: "Best practices for writing skill descriptions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/Skills/best-practices-skill-description.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Working with skills", "Creating custom skills"]
---

# Best practices for writing skill descriptions

The description is the trigger for a skill, and the only part of a skill that the agent is guaranteed to see. Focus most of your effort on writing the description.

## Describe the agent's action, not the topic

If a description names a topic, such as "Greeting for the app", "Styling for charts", or "Data governance policy", the skill only loads when the question is about that topic. Questions about data are not about that topic, so the agent skips the skill.

Instead, write a description that tells the agent when to load the skill, based on what the agent is about to do. The skill then loads for the questions that need it.

The following table compares topic-style descriptions with action-style descriptions.

Topic-style and action-style descriptions

| Skill | Topic-style description | Action-style description |
| --- | --- | --- |
| Chart color | "Use this skill whenever the user asks to create... any chart" | "Load this skill before you create any chart, whether or not the user asked for one" |
| Chart color (second application) | "Rules to apply before creating any chart" | Action-style, with chart types and implicit cases |
| Greeting | "Greeting for the app. Use when writing the first answer" | "Load this skill before writing your first answer in a new chat, whatever the user asks" |
| Executive summary | "Response style for senior leadership. Use when the question asks for a summary, overview, performance..." | Format in the description, and "load first, before any data lookup" |
| Customer data rule | "Data governance policy for the app" | Rule in the description, with question types named |

Tip note

General guidance for AI agent skills often recommends a third-person description, such as "Processes Excel files and generates reports". For Qlik Answers, descriptions that tell the agent directly when to load the skill work better in practice. For example, "Load this skill before you create any chart". The examples in this topic use that style. Whichever voice you choose, keep the trigger conditions.

Information note

Matching words is not enough. A description can contain the exact word that the user types, and the skill can still fail to load. Tell the agent to load the skill before the data step.

## Put always-on rules in the description

The description is always in context. If a rule must always apply, write a short version of the rule in the description. The agent can then apply the rule even when it does not load the skill.

The following description includes the rule:

description: >
Rule for the first answer in every new chat in the GreenLeaf Plant Catalog app: it starts with
"Hello, gardening friend!". Load this skill first, before any data lookup, table, chart or
search, when the chat has no earlier answer. This covers every kind of first question: counts,
lists, rankings ("tallest", "most", "top 10"), filters, or a plain "hi".

Keep the rule short enough to fit in one sentence.

## Name implicit cases and question types

List the situations where the rule applies, even when the user does not mention the rule. For most rules, this includes:

- Relative time: "last year", "this year", "YTD", a bare year such as "2024", or "Q2"
- Breakdowns and comparisons: "break down X by Y", year over year, or compare A with B
- Lists and rankings: "top 10", "tallest", "most", or "which items have X"
- Filters: "which plants need full sun and low water"
- Single totals that the agent shows as a KPI
- Follow-up questions in the same chat

The agent most often misses list, ranking, and filter questions, so always name them in the description.

## Include the words that users say

For vocabulary skills, list the words that people use, including synonyms. For example, "expensive, premium, high-end, luxury" or "open, pending, undelivered". Include words that look like plain English but have a business meaning in your application, such as "store" or "make".

If users ask questions in more than one language, list the words they use in each language next to the English words. For example, "expensive, dyr, teuer, cher". The skill then loads for those users, and you do not need to tell the agent to change the language of its answers.

## Limit the description to the application data

A description that is broader than the application data pulls in questions that are not about that data.

For example, a broad vocabulary skill pulled in the general question "What is the difference between a hybrid and a plug-in hybrid?". Instead of explaining the difference, the agent answered "the app doesn't distinguish them".

To prevent this, include "this application's data" in the description. Also add "Not for general questions that are not about this application's data."

## Keep the description short

The descriptions of all skills in an application are in context for every question. Long descriptions with long synonym lists use up that space, and can make it unclear which skill fits. Aim for a few sentences.

List the synonyms that users actually use, not every possible synonym. Do not repeat a synonym that belongs to another skill. Then test that the skill does not load for questions that it should not affect. For more information, see [*Testing skills*](adding-skills.htm#Testing).

## Description checklist

Before you upload a skill, check that the description meets the following criteria:

- The first sentence states the rule and that the rule is required.
- It tells the agent to load the skill before the agent's action, whether or not the user mentions the topic. For example, "before any data lookup" or "before you create any chart".
- It names implicit cases and question types, such as lists, rankings, filters, KPIs, and follow-up questions.
- For vocabulary skills, it lists the words and synonyms that users say.
- For always-on rules, it includes the rule itself.
- It is limited to the application data, and excludes general questions.
- It is a few sentences long, and shares no synonyms with another skill.
