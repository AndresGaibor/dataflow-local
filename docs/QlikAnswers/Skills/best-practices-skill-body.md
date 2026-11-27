---
title: "Best practices for writing skill bodies"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/Skills/best-practices-skill-body.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Working with skills", "Creating custom skills"]
---

# Best practices for writing skill bodies

After a skill loads, the body must leave no room for interpretation. The agent follows exact conditions much better than descriptions of intent.

## Include the core parts of a body

The core of the body includes the following parts:

- The rule: State the rule in one or two sentences at the top of the body. The rest of the body supports the rule.
- Exact values: Spell field names exactly as they appear in the application. Use exact thresholds, date boundaries, formulas, and output text. For example, use "Price greater than 60,000", not "high-priced cars".
- A worked example with the answer: Show how the rule applies to real values. For example, "FY2025 = 1 July 2024 to 30 June 2025." or "A car sold for 60,000 is mid-range. A car sold for 60,001 is expensive."

  Also add one question with the finished answer it should get. For example, "How many expensive cars did we sell?" should get the answer "[count] cars were sold for more than 60,000 (expensive = price over 60,000, counted as sale records)."
- Placeholders in examples: Use placeholders, not real numbers, in examples. The agent can copy real-looking numbers into answers instead of querying the data. Write "[count]", and add "Always take numbers from the application's data."
- What not to use: Name the tempting shortcut and forbid it. For example, "Never use the Year field: it is the calendar year of the sale."
- What to count: For anything that produces a number, define what one unit is. A missing unit is the most common cause of a wrong number. For example, the agent uses the right filter, but counts distinct customers instead of sale rows.
- One term per concept: Pick one word for each unit and measure, such as "sale record" or "fiscal year", and use it throughout the skill. Map the words that users say to that term. For example, "deal", "order", and "sale" all mean one sale record. Mixed terms can change what the agent counts.

## Define behavior in tricky cases

Tell the agent what to do when the rule is not straightforward to apply:

- Conflicts: State what wins in a conflict between the skill and a master measure, an application field, or the wording of the user. If the application has a master measure with a different definition, the skill must state which one wins.
- User overrides: Separate one-off requests from standing requests, and state how long each one lasts.

  - A one-off request, such as "make this chart red" or "cars over 50K", applies to that answer only. The next answer goes back to the rule.
  - A standing request, such as "from now on use red", "always use calendar years", or "stop greeting me", lasts for the rest of the chat.

  Without these limits, a one-off request can carry over to later answers, or the agent can forget a standing request.
- Ambiguous wording: Pick one reading, and tell the agent to state which reading it used. For example, "the most expensive cars" can mean the highest prices, or the most cars in the expensive tier. Without a rule, the same question can get different readings on different runs.
- Edge cases: Cover partial periods, periods with no data, and invalid records such as negative prices. Put the checks that matter in the main rule and in the final check, not only in an edge-case section.
- Out of scope: For terms that the skill does not define, tell the agent to say so and ask. For general knowledge questions, state that the skill does not apply.

## Define output and verification

Tell the agent how to present the result, and how to check it before answering:

- Stated rule: Tell the agent to state the applied rule in the answer. For example, "FY2025 (1 July 2024 to 30 June 2025)" or "Excludes 388 open orders". Users can trust the number, and anyone who checks the answer can see what happened.

  A stated rule works well for definitions and calendars. For a chart color or a greeting, check the output itself instead. For a short summary format, ask for the rule in one short clause.
- Placement: For skills that control the output, state where the output goes. For example, "Put the greeting first, before any text, chart or table." and "After the greeting, answer the question in full."
- Output types: Add one line for each output type. For a chart rule, state what to do for bar charts, line charts, combo charts, KPIs, and tables separately. Chart types with their own default colors, such as combo charts, need their own line.
- Per-answer rules: If a rule must apply on every turn, state that explicitly. For example, "This applies to every answer in the chat, not only the first." Also give examples of follow-up questions.
- Final check: End the body with a short list of checks that the agent runs before answering. The final check catches cases where the skill loaded, but the agent only applied part of it.

## Match strictness to the cost of mistakes

Match how exact an instruction is to how much a mistake costs:

- Strict: Definitions, thresholds, date boundaries, field names, what to count, hex colors, and fixed text such as a greeting. Write these as exact rules.
- Flexible: Tone, level of detail, and the wording of a summary. Give a sensible default, and let the agent adjust to the question. For example, "Usually one short paragraph. Go longer only if the question needs it."

## Keep only the current rule

Keep only the current rule in the skill. Avoid instructions such as "before 2025 use 50,000, after that use 60,000", unless the agent needs both rules. Record the old rule and the date it changed in a change log outside the skill.

Write calendar examples as a pattern, so that they stay accurate over time. For example, "FY[n] = 1 July [n-1] to 30 June [n]".

## Keep skills small and focused

Follow these guidelines for the shape and size of a skill:

- One concern per skill: For example, a fiscal calendar and business terms are two skills, not one. Small skills load more precisely, and are easier to maintain.
- Length: Most skills fit in about 80 lines. If a skill grows much longer, split it by concern before you add more.
- Plain language: You do not need technical setting names. Exact values matter, not vague wording.
