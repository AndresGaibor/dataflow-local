---
title: "Remembering your preferences in Qlik Answers"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/Qlik-Answers-learning-memory.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Using Qlik Answers and choosing your context", "Answering questions with Qlik Answers"]
---

# Remembering your preferences in Qlik Answers

Qlik Answers can learn and remember your preferences for use in future conversations.

Memory saves short facts about one user. Qlik Answers saves a memory when you state a lasting preference or define a word, and it uses your saved memories when it builds later answers. You manage your memories by asking in the chat: what do you remember, change this, forget that.

Qlik Answers remembers two kinds of information:

- Preferences: How you like answers. Chart color and chart type, money and percent format, a default filter such as your region or dealership, your fiscal year start, answer length, the language you want, your name and team.
- Terminology: What your words mean. "Premium cars = Price above 50,000", "EV = Fuel\_Type is Electric", "margin leakage = Sum(Discount\_Amount)/Sum(Price)", "shop means Dealer".

Saying the same thing again updates the existing memory instead of adding a second one.

Qlik Answers usually says which memory it applied in its answers, for example "filtered to Lakeside Motors, per your saved preference". Read those notes to know when a saved memory affected the answer.

You can view and edit your memories from Settings. Click ![Open menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_menu.svg) > Settings to view your memories.

Memories in Settings

![Saved memories listed in Settings.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_settings-memory.png "Click to view full size")

## Application of memory

In Qlik Answers, memory is applied as follows:

- Per user. Your memories apply only to your answers. A colleague asking the same question gets their own memories, or none. Qlik Answers does not read or change another user's memories.
- Across chats. A new chat starts with your saved memories already in place.
- Across applications. Memories follow you into every app you ask questions in. A default filter or a definition saved in one app also applies in the next one.

Information note

Memories are not tenant-wide and cannot be set for other users. "Remember this for everyone" saves nothing for other users. For a shared rule, use a skill or a master item.

When memories conflict with skills set in an assistant or application, Qlik Answers uses the one that makes the most sense in the context. The response indicates which one was used and how to use the other option instead. For more information about skills, see [*Working with skills*](Skills/working-with-skills.htm).

## Saving memories

You can save a memory by stating a preference for how Qlik Answers generates content. Saying remember is optional.

For example:

- My favorite color is teal. From now on, use teal for charts.
- I prefer bar charts, never pie charts.
- Always show money in Swedish krone.
- I manage the Lakeside office. Unless I say otherwise, filter my analysis to the Lakeside office.
- Remember: my fiscal year starts in April.
- Respond to me in Swedish from now on.

To set a one-time preference that is not saved as a memory, state it in your question. For example, "Just for this question, use a pie chart: share of orders by Fuel\_Type."

## Changing memories

You can update memories by saying the new value you want remembered. For example:

- My favorite color is orange now.
- I like line charts better for trends over time, but keep bar charts for comparisons.

You can also edit them in Settings by clicking ![Open menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_menu.svg) > Settings and clicking Edit memory.

## Reviewing saved memories

To review what Qlik Answers has remembered, ask it. For example, What do you know about me? or List all my memories with their type.

## Forgetting memories

You can tell Qlik Answers to forget memories. For example:

- Forget my favorite color
- Forget that I prefer bar charts, but keep everything else
- Forget everything you know about me

## Memory limitations

Memories have the following limitations:

- Do not use memory for:

  - Shared business definitions. Memory is personal. Use a skill or a master measure so everyone gets the same number.
  - Access control. A saved filter is a convenience, not a restriction. Use Section Access instead. For more information, see [*Managing data security with Section Access*](../Scripting/Security/manage-security-with-section-access.htm).
  - Secrets or personal data. Qlik Answers refuses passwords, card numbers, and health data. This information does not belong in a chat.
- Memories belong to the user, not to an app. A default filter such as "Lakeside Motors" or a definition such as "premium = Price above 50,000" carries into every app you open. In an app without those fields, the rule can filter the wrong data, or Qlik Answers has to explain why it skipped it.

  - Keep app-specific rules in a skill on that app.
  - Phrase personal memories so they make sense anywhere ("money in USD with no decimals").
  - Forget field-specific memories when you move to different work.
