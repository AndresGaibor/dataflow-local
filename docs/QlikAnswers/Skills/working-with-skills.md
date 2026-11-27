---
title: "Working with skills"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/Skills/working-with-skills.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers"]
---

# Working with skills

Add custom skills to teach Qlik Answers how to handle specific topics and tasks, drawing on that knowledge automatically when relevant.

Skills shape how Qlik Answers responds, including its tone, persona, topic scope, and domain assumptions. When you add a skill to an application or an assistant, Qlik Answers applies the skill whenever the conversation relates to it.

Information note

Skills can be added to assistants and applications. If an application with assigned skills is added as a content source to an assistant, the assistant uses that application's skills only when handling data from that application.

You add custom skills as Markdown (.md) files. Each file contains the instructions that define the behavior you want Qlik Answers to follow. For information on creating custom skills, see [*Creating custom skills*](creating-custom-skills.htm).

You can upload skills to Qlik Cloud from:

- the catalog
- an application's AI optimization settings
- an assistant's Skills tab

Information noteTo upload and manage skills in Qlik Cloud, you need the Manage skills user permission set to Allowed. For more information, see [*Managing user access to Qlik Answers*](../administering-qlik-answers.htm#Access).

## Using custom skills

Custom skills are best used to:

- Define your terms: Say what a word means in your business. For example, what does recent mean? Does it mean the last six months or the current fiscal quarter?
- Add instructions: Give Qlik Answers extra guidance it should always follow, such as how to word an answer or what to mention. For example, state the period you used at the start of the answer.
- Set business rules: Decide what happens when a question leaves something open. For example, if the user does not specify a time period, always use the most recent 6 months.
- Restrict general knowledge: Limit how much Qlik Answers uses general knowledge, so that answers focus strictly on data from applications or knowledge bases. For more information, see [*Example use case: Restricting general knowledge*](example-skill-general-knowledge.htm).

Do not use custom skills for:

- Access control, data masking, or hiding personal data. Use Section Access or the data model instead. For more information, see [*Managing data security with Section Access*](../../Scripting/Security/manage-security-with-section-access.htm).
- Compliance rules that must hold on every answer. Whether a skill loads is decided separately for each question. Even a well-written always-on skill occasionally fails to apply, especially on follow-up questions. A rule with zero tolerance for misses needs an always-on control, not a skill.
- Fixing gaps in the data model. A skill can say what to count, but it cannot create fields. Fix gaps in the data model itself.
- Replacing vetted master items. If the application has an agreed master measure for a core metric, point the skill to it rather than redefine it in a skill. If you have a skill covering a specific scenario where you need a variant of the master item, clearly define how and when to use each, because Qlik Answers and application dashboards will show different numbers.
- Secrets or sensitive information. Skill text can appear in answers and can be read by anyone who manages the application's skills. Leave out credentials, personal data, internal URLs, and confidential figures.
- Overriding the language the user asked their question in, or hiding the agent's behavior from the user. These patterns can also block the upload.
- One large skill for everything. Combining unrelated rules results in each rule loading less precisely. Keep each skill specific to a single concern.

## Skills and spaces

Skills do not need to be in the same space as the applications or assistants to which they are added. You need to have access to the space the skill is in to add the skill to an application or assistant. After the skill has been added to the application or assistant, Qlik Answers users of that application or assistant do not need access to the space the skill is in.

If applications are published to managed spaces, the published copies include any skills added to the original application.

## Using skills and knowledge bases

Use custom skills when you need to tell Qlik Answers how to work. Use knowledge bases to set what the agent can look up. If you can point to a page or paragraph that contains the answers, it belongs in a knowledge base. If you are telling the agent how to interpret a word, format an answer, or behave before it acts, it belongs in a skill.

Use a skill when:

- You define a business term, a synonym, or an abbreviation, and the user might type either word.
- You set a calculation rule, such as what counts as "premium" or how a fiscal year runs.
- You set how answers look: tone, length, language, chart colors, greeting.
- You limit what the assistant answers (stay on topic, decline general knowledge).
- You want the agent to ask a clarifying question before it acts.
- The rule is short enough to read in one minute.

Use a knowledge base when:

- The answer sits in a document: a policy, a manual, a contract, a handbook.
- The content is long, or too long to paste into instructions.
- Users need a citation to the source.
- The content is updated by others on their own schedule.
- The question is "What does our document say about X?"

Use neither when:

- You need to hide or restrict data for certain users. Use Section Access instead. A skill can keep a value out of text, but the value can still appear in a chart.

## Skills and memories

Skills can interact with user preferences remembered by Qlik Answers. Qlik Answers tries to follow all skills and memories. When a skill and a memory conflict, Qlik Answers uses the one that makes the most sense in the context. The response indicates which one was used and how to use the other option instead.

Generally, conflicts are handled as follows:

- Skills that narrow the focus to a specific area are generally applied over memories that request general answers.
- Skills that set thresholds are generally prioritized over user-defined thresholds.
- For definitions and conventions, Qlik Answers prefers memories over skills.
- Memories that filter focus, such as to "only my data", are generally applied over skills that would keep the focus general.
- If a skill indicates that user memories should have priority, Qlik Answers always chooses the user memory.

For more about memories, see [*Remembering your preferences in Qlik Answers*](../Qlik-Answers-learning-memory.htm).

## Skills workflow

The following outlines the workflow for using skills with Qlik Answers.

1. Create a skill

   Create a skill by uploading a Markdown file and adding a name, description, and space.

   [*Creating custom skills*](creating-custom-skills.htm)
2. Add the skill to an application or an assistant

   Add the skill where you want Qlik Answers to apply it.

   [*Adding skills to applications and assistants*](adding-skills.htm)
3. Test and troubleshoot the skill

   Verify that the skill behaves as intended, and refine it if needed.

   [*Troubleshooting skills*](troubleshooting-skills.htm)

## Limitations

Custom skills have the following limitations with Qlik Answers:

- Skills are guidance, not controls. In Qlik Answers, the model decides with every question whether or not a skill applies, so use is never guaranteed. Clear wording, especially in the skill description, makes use very likely but not certain.
- Skill compliance can drop slightly on later follow-up questions. Qlik Answers initially reads the short description of each skill, and then reads the full instructions only when it needs them. After that, it relies on the chat history for follow-up questions.
- When answering a question to which more than one skill applies, the agent might apply one skill and occasionally skip a second relevant skill.
- Self-explanations of skill use are not always reliable. If asked why a skill was skipped, Qlik Answers may give an explanation that does not match what happened.
- In multi-step comparisons using skill-defined periods of time, the agent can occasionally make calculation errors. Ask the agent to query each period separately, and check comparison answers.
- You can limit the use of general knowledge by Qlik Answers with a skill, but you cannot remove it. The model still holds the knowledge, and a slip is possible, especially in follow-up answers. See [*Example use case: Restricting general knowledge*](example-skill-general-knowledge.htm).
- The review results for uploaded skills can vary. The same safe skill file can pass on one upload and be flagged on another if it contains wording that could be flagged. For more information about flagged skill uploads, see [*Validating skills*](creating-custom-skills.htm#Validati).
