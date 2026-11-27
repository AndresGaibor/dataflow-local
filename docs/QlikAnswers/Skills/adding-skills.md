---
title: "Adding skills to applications and assistants"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/Skills/adding-skills.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Working with skills"]
---

# Adding skills to applications and assistants

Add a skill to an application or an assistant so that Qlik Answers applies it when answering related questions.

You add and manage skills from the Skills tab. The Skills tab is available in two places:

- In an application, in AI optimization.
- In an assistant.

You can add a maximum of five skills to an application or assistant. You can only add or remove skills that are in a space to which you have access.

Information noteTo manage skills in applications, you need the Manage skills and Enable for Qlik Answers user permissions set to Allowed. For more information, see [*Managing user access to Qlik Answers*](../administering-qlik-answers.htm#Access).

Information noteYou cannot edit a skill after it is created. To change a skill, create a new skill by uploading a new version of the Markdown file, then add the new skill. For more information, see [*Creating custom skills*](creating-custom-skills.htm).

## Navigating the Skills tab

The Skills tab shows a searchable list of the skills added to the application or assistant. Each skill in the list shows its name and description.

When you select a skill, the Skill details panel shows a table with the skill's name and description, followed by the rendered skill text. A side panel shows the following information:

- Details: The date the skill was added and the owner of the skill.
- Usage: The number of applications the skill is used in and the number of assistants the skill is used in. Click View next to either count to see where the skill is used.

If no skills have been added, the Skills tab shows three template skills that you can add to your application or assistant. After skills have been added, you can add these template skills from Add skills > Choose skill template. The following template skills are available:

- Stay on topic: Only answer using data from the application, never from general knowledge.
- Executive brief tone: Format the answers from Qlik Answers to follow a specific style for a business leader.
- Green visual styling: Format all charts created by Qlik Answers to use a specific shade of green.

## Adding existing skills

Do the following:

1. Open the Skills tab in your assistant or application.
2. Click Add skills > Choose skill.
3. Select the skill to add.

   You can only add skills that are in a space you have access to.
4. Click Add.

After you add a skill, test it to confirm that it works as expected. For more information, see [*Testing skills*](#Testing).

## Uploading and adding new skills

You can upload and add a new skill at the same time.

Do the following:

1. Open the Skills tab in your assistant or application.
2. Click Add skills > Upload skill.
3. Add your skill .md file and click Next.
4. Optionally, update the skill name and description.
5. Under Space, select a space for the skill.
6. Optionally, add tags to the skill.
7. Click Next.
8. Wait for the skill to be validated. If the skill passes validation, click Close.

   If the skill has issues, review the issues, update the skill file, and try uploading again. For more information, see [*Validating skills*](creating-custom-skills.htm#Validati).

## Adding skills from a template

Do the following:

1. Open the Skills tab in your assistant or application.
2. Do one of the following:

   - If the application or assistant has no skills, click the template skill you want to add.
   - If the application or assistant already has skills, click Add skills > Skill template and then select the template skill you want to add.
3. Optionally, update the skill name and description.
4. Under Space, select a space for the skill.
5. Optionally, add tags to the skill.
6. Click Next.
7. Wait for the skill to be validated, and then click Close.

## Downloading skills

Do the following:

1. In the Skills tab, find the skill you want to download.
2. Click ![Skill actions](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Download skill.

## Removing skills

Removing a skill from an application or an assistant stops Qlik Answers from applying it there. Removing a skill does not delete the skill from the catalog.

Do the following:

1. In the Skills tab, find the skill you want to remove.
2. Click ![Skill actions](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Remove skill.

## Testing skills

After you add a skill to an application or an assistant, test it in Qlik Answers to confirm that it behaves as intended.

A skill shapes how Qlik Answers responds, such as its tone, persona, topic scope, and domain assumptions. Because a skill influences responses rather than appearing in them, test the skill by asking questions that relate to the topic or task it covers, and review how Qlik Answers answers.

The following is a suggested test plan for custom skills:

1. Check the data first. Confirm field names, values, and the numbers you expect. Compute expected answers in the application, not with another AI tool.
2. Ask the same questions with and without the skill. The difference shows the value of the skill.
3. Use a fresh chat for each first question. A skill loads once per chat, so a second question in the same chat does not test loading.
4. Include every question type:

   - Questions that name the rule
   - Questions that need the rule but do not name it
   - Lists, rankings, and filters, where skills are most often skipped
   - Questions the skill must not affect, such as general knowledge
   - A user override, followed by a plain question to check the reset
   - Follow-ups, for rules that must hold on every answer
5. Ask each implicit question at least five times in fresh chats for rules that matter, and record the pass rate, such as 4 of 5. A rule that applies 70% of the time passes two runs about half the time.
6. Change one thing at a time between versions, and compare them on identical questions.
7. Read every answer, not just the score. Correct answers sometimes fail a strict check, and wrong ones sometimes pass.
8. For any "don't show X" rule, check the chart and table data, not only the text. A chart can show values the text leaves out.
9. Test combinations. Include questions that need two or three of your skills at once.
10. Test as different users if the application uses Section Access. What a user can see changes the data, including the latest date in it.
11. Try real use, not only test questions. Ask the people who will use the application whether the skill applies when they expect it, whether answers are clear, and what is missing.
12. Watch what the agent does, not only the score. You can remove a section that the agent never needs. A rule that the agent keeps missing might need to move into the description.

If the responses do not match what you expect, refine the skill. You cannot edit a skill after it is created, so create a new skill by uploading a revised version of the Markdown file, then add the new skill and test it again. For more information, see [*Creating custom skills*](creating-custom-skills.htm).
