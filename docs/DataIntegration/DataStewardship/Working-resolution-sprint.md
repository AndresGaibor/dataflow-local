---
title: "Working in a resolution sprint"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataStewardship/Working-resolution-sprint.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Validating and correcting your data with data stewardship"]
---

# Working in a resolution sprint

The goal of a resolution sprint is to curate invalid values contained in the records, making sure that data is valid and complete.

Information noteTo start working in a sprint, you must be assigned as Data steward in the sprint. You can be assigned by any user with the Can manage role in the space of the sprint.

You can find all sprints in Data stewardship in the Qlik Talend Data Integration activity center. You can only view sprints in spaces that you have access to.

For information about notifications when sprint assignments change, see [*Sprint notifications*](Sprint-notifications.htm). Notifications prompt you to check the sprint; the sprint view is the source of truth for the current assignment state.

1. Click on a sprint to open it.

   You will see the sprint overview, which displays sprint information and progress.
2. Click on Assigned to me to open a view of your assigned records.

## Adding and replying to comments

Use cell comments to document a decision, ask a follow-up question, or provide context for a value while you work in the sprint. Keep the discussion in context by replying in the same comment thread instead of creating duplicate comments elsewhere. For detailed steps, see [*Working with cell comments in a resolution sprint*](Working-with-cell-comments-in-a-resolution-sprint.htm).

## Assigning records

If the sprint creator selected automatic assignment when creating the sprint, records will automatically be distributed evenly between data stewards. If manual assignment was selected, all data stewards and sprint owners can assign records to a data steward.

1. Go to Unassigned.
2. Select the records to assign.
3. Click Assign.
4. Select the data steward and click Assign.
5. Click Apply changes to confirm the assignment.

The records are now moved to Assigned to me for the selected data steward.

Information noteYou can re-assign records the same way in Assigned to me or Assigned to others.

## Working with your assigned records

You can now start verifying and editing the assigned records. Data quality indicators are displayed for each column, and invalid values are highlighted. You can hover on an invalid value to find out more about why it is considered invalid.

If AI remediation is enabled on the sprint, an AI agent corrects invalid cell values and reassigns the records to a data steward for review. AI-edited values are marked with an indicator badge. For more information, see [*Reviewing AI fixes in a resolution sprint*](Reviewing-AI-suggestions.htm).

- When you have verified a record, select the record and click Mark as ready.

  The record will be removed from your view of assigned records, and moved to Pending changes.
- You can also assign a record to another data steward that may have more knowledge about it.

  Select the record, click Assign, and select the data steward to assign the record to.

Tip noteInitially, the view loads 100 records to ensure good performance and cost balance. You can load more records by clicking Fetch more.

You can review all records that you have verified or assigned to another data steward, by clicking on Pending changes.

- When you want to resolve your validated records, click Apply changes in your view of assigned records or in Pending changes.

This will move all pending records to Resolved or To be validated. Records that you marked to assign to another steward will also be re-assigned.

- If the sprint requires a second validation step by sprint owners, and you are not a sprint owner, the records will be moved to To be validated.
- In all other cases the records will be moved to Resolved.
