---
title: "Viewing the overview of business logic for Qlik Answers"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/BusinessLogicAI/business-logic-overview-qlik-answers.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Working with applications in Qlik Answers", "Optimizing your application for Qlik Answers with business logic"]
---

# Viewing the overview of business logic for Qlik Answers

Use Overview to define the core context that helps Qlik Answers interpret your application before users start asking questions.

In Overview, you can update the AI-generated application description, sync changes you made in AI optimization, and review field visibility counts.

You can open Overview from AI optimization in the navigation menu.

## AI readiness score

In Overview, you can review your application's AI readiness score. The score shows how well your application is configured for Qlik Answers to interpret your data.

The AI readiness score in Overview.

![The AI readiness score for an app, showing 93%.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/QlikAnswers/ui_application-ai-readiness.png "Click to view full size")

The score overview shows:

- A score, shown as a percentage from 0% to 100%, that represents your application's readiness for Qlik Answers.
- First indexed: When the application was first indexed for Qlik Answers.
- Last synced: When the application was last synced. The score recalculates with each sync.
- Whether your score improved or declined, and by how much, since the previous calculation.
- Individual scores for Data model, Fields, and Metadata.

A higher score means Qlik Answers can more accurately reference your data when answering questions. The score is advisory: it identifies opportunities to improve your application but does not change it automatically.

The score is calculated across three equally weighted pillars: Data model, Fields, and Metadata. For more information about what each pillar measures and why AI readiness matters, see [*Understanding Qlik Answers AI readiness score*](understanding-ai-readiness-score.htm).

The score recalculates when the application syncs. For more information, see [*Sync application*](#Sync).

### Reviewing suggestions

The Improve your AI readiness score section lists suggestions with recommendations for improving your application. Each suggestion shows:

- Suggestion: The issue identified for improvement.
- Area: The pillar to which the suggestion belongs: Data model, Fields, or Metadata.
- Details: A description of the issue.
- Items affected: The number of fields, master items, or other elements involved.
- Score impact: A severity indicator (High, Medium, or Low) that shows the suggestion's effect on your score.

To find specific suggestions, search by name or filter by Area to show a single pillar: Data model, Fields, Metadata, or All.

To see remediation options, click See details. Options vary by suggestion type. Some suggestions offer direct actions, such as adding descriptions or selecting items to hide or group. Others, particularly data model issues, require changes outside AI optimization. You choose whether to act on a recommendation. Suggestions remain visible even if you do not resolve them.

For a full list of suggestion types and how to address them, see [*Qlik Answers AI readiness suggestions summary*](ai-readiness-findings-reference.htm).

## Updating the application description

Qlik Answers generates a plain-language description of the application from your field names, existing descriptions, and data. In the Application description card, you can review the generated description. Qlik Answers also considers existing field descriptions and uses that context to produce more accurate and meaningful descriptions.

Review this description and edit it when needed. A clear, accurate description improves the initial context Qlik Answers uses when interpreting questions.

Do the following:

1. In Overview, in the Application description card, click ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg).
2. Edit the description.

   You can clear the description by clicking Clear.

   You can generate a new Qlik Answers generated description by clicking Generate.
3. Click Save.

## Sync application

Click Sync application to make changes immediately available to Qlik Answers. Qlik Answers does not immediately include changes, such as hiding or unhiding items or adding or removing content, synchronizing automatically on a schedule. You can manually sync your changes to make them immediately available.

Information noteSync application does not reload application data. It updates the AI context so Qlik Answers can account for your latest AI optimization configuration changes.

The sync control shows Last synced, the time since the last sync, and Next sync in, the time until the next automatic sync.

Do the following:

- Click Sync application.

## Field and master item counts

Overview shows how fields and master items are currently configured for use with Qlik Answers:

- Hidden: Items that are hidden from Qlik Answers.
- Visible: Items that are available to Qlik Answers.
- Excluded: Items that are not in any group. Qlik Answers does not use excluded items.

Use these counts as a quick check of how broadly your data model is exposed to Qlik Answers and make adjustments in Fields and master items.
