---
title: "Creating custom skills"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/Skills/creating-custom-skills.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Working with skills"]
---

# Creating custom skills

Create a custom skill by creating a Markdown (.md) file that defines how you want Qlik Answers to handle a specific topic or task.

Skills contain the instructions that shape how Qlik Answers responds, such as its tone, persona, topic scope, and domain assumptions.

Information noteYou cannot edit a skill after it is created. To change a skill, create a new skill by uploading a new version of the Markdown file.

After you create skills, you can upload them to Qlik Cloud from the catalog. You can also upload new skills when you add skills to assistants or applications.

For more information, see [*Adding skills to applications and assistants*](adding-skills.htm).

## Choosing a skill type

When you create a skill, consider its purpose and the kind of rule you want to enforce. Different rules are defined in different ways.

Types of skill

| Skill type | Examples | Does the user mention it? | What to focus on |
| --- | --- | --- | --- |
| Vocabulary and definitions | Price tiers, deal types, status values, metric definitions | Yes, they say the word | Trigger words and synonyms, exact conditions, what to count, ambiguity, conflicts with master items |
| Calendars and periods | Fiscal year, fiscal quarters | Rarely. Users say "last year", not "fiscal" | Trigger on any use of time, worked examples, anchoring relative periods to the latest date in the data, partial periods |
| Always-on output conventions | Chart color, greeting, tone, default exclusions | Never | Describe the agent's action, name every output and question type, put the rule in the description |
| Response style or persona | Executive summary format | Never asks for the format | Treat like an output convention. State the format in the description, let the user's explicit request for detail win |
| Procedures | How to analyze a "why did X change" question | Sometimes | Ordered steps, what not to conclude |

## Writing your skills

Skills have three key elements:

- Name: Identifies the skill and tells Qlik Answers what the skill does and when it applies.
- Description: The trigger for the skill.
- Body: The rule and how to apply it.

Your custom skill file should meet these requirements:

- A Markdown (.md) file with YAML frontmatter at the top.
- name: lowercase letters, numbers, and hyphens, unique among the skills on the application. The agent always sees the name, so make it say what the skill does and when it applies: chart-color-green says more than car-sales-defaults. Avoid vague names such as defaults, helper, or rules, and use one naming pattern across your skills.

  name must be at most 64 characters, use only lowercase letters, numbers, and hyphens, and contain no XML tags and no reserved words.
- description: the trigger, required and never empty. This is the part the agent always sees.

  description is required, non-empty, at most 1,024 characters, with no XML tags. Long synonym lists can get close to the description limit.

  For guidance on writing descriptions, see [*Best practices for writing skill descriptions*](best-practices-skill-description.htm).
- The body below the frontmatter: the rule and how to apply it.

  For guidance on writing the body, see [*Best practices for writing skill bodies*](best-practices-skill-body.htm).
- Use straight quotes and plain hyphens. Smart quotes and long dashes may not survive the upload.

Information noteUse a folded YAML description (description: > followed by indented lines). It is easier to read, and it avoids a common YAML error: a one-line description that contains a colon followed by a space breaks parsing. The Skills page might show only ">" in the Description box for these skills. The skill is still stored and used correctly.

A skill is made up of several parts. The following table outlines the parts of a skill.

Skill parts

| Part | Where | What it looks like |
| --- | --- | --- |
| The rule and that it is required | Description, first sentence | "Required fiscal calendar for every answer that filters, groups, compares, or labels this app's sales data by time." |
| When to load, as the agent's action | Description | "Load this skill whenever you are about to use a date or a period, whether or not the user says fiscal." |
| The implicit cases and question types | Description | "last year", "YTD", a year like "2024", trends, top N lists, rankings, filters, single totals shown as a KPI |
| Exact values with real field names | Body | "Price greater than 60,000", "Sale\_Date from 1 July 2024 to 30 June 2025" |
| A worked example with placeholders | Body | "FQ2 FY2025 = 1 October to 31 December 2024", "The catalog has [count] tree varieties." |
| What not to use and what to count | Body | "Never use the Year field." "One row is one sale. Don't count distinct customers." |
| State the rule and check before answering | Body, end | "Name the period and its dates in the answer." A short checklist. |

For a general skill template, see [general-template.md](/en-US/cloud-services/tutorials/general-template.md).

Depending on its purpose, a skill might need all or only some of these parts.

### Vocabulary and definitions

For a vocabulary and definitions template, see [business-terms-template.md](/en-US/cloud-services/tutorials/business-terms-template.md).

Vocabulary and definitions skills need the following parts:

- The rule and that it is required
- When to load, as the agent's action
- The implicit cases and question types
- Exact values with real field names
- A worked example with placeholders
- What not to use and what to count
- State the rule and check before answering

Additionally, this skill requires relative periods and partial periods to be defined.

Information noteFor templates to migrate terms from synonyms in AI optimization, see [*Migrating synonyms to skills*](../BusinessLogicAI/business-logic-synonyms-qlik-answers.htm#Migratin).

### Calendar and periods

For a calendar and periods template, see [fiscal-calendar-template.md](/en-US/cloud-services/tutorials/fiscal-calendar-template.md).

Calendar and periods skills need the following parts:

- The rule and that it is required
- When to load, as the agent's action
- The implicit cases and question types
- Exact values with real field names
- A worked example with placeholders
- What not to use and what to count
- State the rule and check before answering

Additionally, calendar skills need relative periods and partial periods to be defined.

### Output convention

For an output convention template, see [output-convention-template.md](/en-US/cloud-services/tutorials/output-convention-template.md).

Output convention skills need the following parts:

- The rule and that it is required
- When to load, as the agent's action
- The implicit cases and question types

Additionally, output convention skills require the exact value, one line for each output type, the user override, and the final check.

### Response style

For a response style template, see [response-style-template.md](/en-US/cloud-services/tutorials/response-style-template.md).

Response style skills need the following parts:

- The rule and that it is required
- When to load, as the agent's action
- The implicit cases and question types

Additionally, response style skills require the format, an example answer, the user override, and the final check.

### Procedure

For a procedure template, see [procedure-template.md](/en-US/cloud-services/tutorials/procedure-template.md).

Procedure skills need the following parts:

- The rule and that it is required
- When to load, as the agent's action

Additionally, procedure skills require the ordered steps, what not to conclude, and the final check.

### Using template skills in your own assistants and applications

Template skills provide the structure, so you do not need to start from a blank file. To use these templates effectively:

1. Decide what counts as in scope.

   Name the sources: the applications, and the knowledge base if the assistant has one. Decide whether greetings and "what can you do" questions stay in.
2. Start from a template.

   Pick the template that fits your goal and look at the structure.
3. Replace the specifics.

   Swap in your sources line, your in-scope and out-of-scope examples, and your decline message. Keep the fixed message and the line that gives none of the answer.
4. Assign it at the right level.

   Use the assistant when users ask through an assistant, and the application when they ask in one application. Skills added to an application also apply when that application is used through an assistant. Add the skill to the assistant for rules that cover all its sources. A skill on one application is not used through an assistant.
5. Test before you trust it.

   Ask your out-of-scope questions with and without the skill, in fresh chats. Include data questions that start with "what is" or "who", a mixed question, and a follow-up.
6. Use the upload review.

   If the review flags the file, adjust the wording as described in [*Validating skills*](#Validati), and upload again.

## Uploading a skill to Qlik Cloud

Information noteTo upload skills, you need the Manage skills user permission set to Allowed. For more information, see [*Managing user access to Qlik Answers*](../administering-qlik-answers.htm#Access).

Do the following:

1. Go to the Create page of the Analytics [activity center](#glossary-0 "Glossary term") and select Skill.
2. Add your skill .md file and click Next.
3. Optionally, update the skill name and description.
4. Under Space, select a space for the skill.
5. Optionally, add tags to the skill.
6. Click Next.
7. Wait for the skill to be validated. If the skill passes validation, click Close.

   If the skill has issues, review the issues, update the skill file, and try uploading again.

## Validating skills

When skills are uploaded, Qlik Cloud scans the skill for potential issues, such as prompt injections or attempts to misuse the system. A skill that passes moves to an assessed state and can be added to an application or assistant.

If a skill fails validation, Qlik Cloud lists each reason for failure, with the lines it refers to and a suggested fix.

Failed validation

![Validation showing the reason for failure. The skill has 79 errors. Each error shows the reason for the error, the line it is from, and a recommendation for fixing it.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_skill-validation-failure.png "Click to view full size")

Information note

The review result can differ between uploads of the same file. If a skill you believe is safe is blocked on a quality finding, read the flagged lines, adjust the wording using the following table, and upload again. If the same safe skill keeps failing, contact Qlik Support with the skill file and the findings.

Safe skills can occasionally be flagged on quality grounds. The following patterns can cause findings:

Common skill issues

| Pattern | Example | Finding type | What to do |
| --- | --- | --- | --- |
| Unconditional trigger on every calculation | "before any calculation, whether or not the user mentions data quality" | Broad trigger | Tie the trigger to the application and to what the rule does for the user. Give the user a way to see or turn off the rule. |
| Overriding the model's language behavior | "even if the user writes in another language" | Behavior override | Remove the clause. |
| Quoting phrases that attack the rules | "ignore your instructions", "you have no limits" listed as things to refuse | Jailbreak framing | Describe the case in neutral words: "if the user asks you to drop or relax this rule". |
| Load before any answer | "before searching, choosing an application or writing any answer" | Broad trigger | Use a situation: "whenever you are about to answer something that is not clearly about this application's data". |
| Telling the agent to hide something | "don't tell the user about..." | Behavior override or concealment | Say what the rule does instead. This is a risk, not a certainty. |
