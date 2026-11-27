---
title: "Example use case: Restricting general knowledge"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/Skills/example-skill-general-knowledge.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Working with skills"]
---

# Example use case: Restricting general knowledge

Skills can be used for a variety of purposes in Qlik Answers. This example shows how to use a skill to limit answers that are based on general knowledge.

While general knowledge can be useful as a source for Qlik Answers, you might want to restrict its use for some assistants or applications. For example, you may want general knowledge questions declined if you have a customer-facing assistant, an assistant that should read as a data tool, or a team that needs every answer traced to a calculation or a document.

You can add a skill that sets a rule to restrict the use of general knowledge sources when answering user questions. The skill does not remove general knowledge sources from Qlik Answers, but it changes which questions the assistant answers.

Warning noteSkills can steer what data is used in responses, but they cannot hide data entirely. Do not use skills as a security control for data.

## Example: Car sales assistant

The assistant in this example has three car sales applications (United States, India, and Europe) and a knowledge base of brochures, manuals, and market reports. You want it to decline questions that are not related to car sales, using the following guidelines:

- Decline facts about the world, math, code, writing, translation, recipes, advice, current events, and general explanations, including general car topics that no document defines.
- Answer questions about the applications and the knowledge base as before.
- Answer greetings and "what can you do" questions.
- Split mixed questions. For example, when handling the question "What is the capital of Japan, and how many cars were sold in India?", return an answer for how many cars were sold in India and include a sentence declining the other part of the question.
- Resist framing and pressure. For example, decline requests to write a poem about the answer or to ignore instructions.

The following skill can be used to restrict the scope to meet these needs: [scope-guard.md](/en-US/cloud-services/tutorials/scope-guard.md).

## Why it is written this way

The skill scope-guard.md is written to ensure that general knowledge is not used when answering questions:

- The description names the agent's situation, not a topic. It says to load the skill when the agent is about to answer something not clearly about the data, or could answer from its own knowledge. The in-scope examples (such as "What is the top-selling model in India?") keep ordinary data questions that start with "What is" out of the guard.
- It provides one test the agent can apply ("Can I support this answer with a calculation on an app, or with a passage I retrieved from the knowledge base?"), which is easier to follow than a list of banned topics.
- A fixed decline message and an instruction to provide none of an answer. The message keeps the reply predictable, and the second rule rules out labeling a reply as general knowledge and answering anyway, which is what the assistant did without the skill.
- Named special cases. Mixed questions, pressure, role-play and topics that touch the data each have a line. The last one keeps a topic the documents mention, such as the Chinese car market, from making every question about China in scope.
- A final check the agent runs before sending.
- Neutral wording for the upload review. The first upload was flagged for quoting phrases such as "ignore your instructions" and for a "load first, before any answer" trigger. Describing those cases in plain words passed.

## Using template skills in your own assistants and applications

Template skills provide the structure, so you do not need to start from a blank file. To use these templates effectively:

1. Decide what counts as in scope.

   Name the sources: the applications, and the knowledge base if the assistant has one. Decide whether greetings and "what can you do" questions stay in.
2. Replace the specifics.

   Swap in your sources line, your in-scope and out-of-scope examples, and your decline message. Keep the fixed message and the line that gives none of the answer.
3. Assign it at the right level.

   Use the assistant when users ask through an assistant, and the application when they ask in one application. Skills added to an application also apply when that application is used through an assistant. Add the skill to the assistant for rules that cover all its sources. A skill on one application is not used through an assistant.
4. Test before you trust it.

   Ask your out-of-scope questions with and without the skill, in fresh chats. Include data questions that start with "what is" or "who", a mixed question, and a follow-up.
5. Use the upload review.

   If the review flags the file, adjust the wording as described in [*Validating skills*](creating-custom-skills.htm#Validati), and upload again.
