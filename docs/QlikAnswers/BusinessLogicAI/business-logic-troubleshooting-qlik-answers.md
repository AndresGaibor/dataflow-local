---
title: "Troubleshooting business logic for Qlik Answers"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikAnswers/BusinessLogicAI/business-logic-troubleshooting-qlik-answers.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Qlik Answers", "Working with applications in Qlik Answers", "Optimizing your application for Qlik Answers with business logic"]
---

# Troubleshooting business logic for Qlik Answers

Most business logic issues with Qlik Answers come from the data model and logical model becoming unaligned. This page suggests solutions to common issues you might encounter when working with business logic AI optimization.

## Error: "Business logic errors detected, which can prevent Qlik Answers from being synced."

A error message appears in AI optimization indicating Business logic errors detected, which can prevent Qlik Answers from being synched.

Possible cause

There are issues in the logical model. The most common cause is an invalid field in the logical model. This is usually from fields items that have been removed from the data model but not from the logical model. The logical model is not automatically updated when fields or master items are removed, so these must be removed manually.

Other changes that leave the data model and logical model out of alignment can also produce this error.

Proposed action

To resolve issues from removed fields or master items, do the following:

1. Open the Fields and master items tab.
2. Select any field with a yellow warning icon and click Ungroup.
3. Open the Overview tab.
4. Click Sync application.

Confirm that the sync completes successfully, the business logic error is no longer displayed, and the removed field no longer appears as an invalid entry in Fields and master items.

If you cannot resolve your logical model issues, try deactivating and reactivating Qlik Answers.

Warning noteThis will undo any logical model customization and reset your business logic.

Do the following:

1. In Overview, click Deactivate Qlik Answers.
2. Click Confirm.
3. Refresh the application.
4. Click Activate and index.
