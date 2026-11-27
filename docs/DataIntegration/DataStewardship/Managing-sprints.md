---
title: "Managing your sprints"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataStewardship/Managing-sprints.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Validating and correcting your data with data stewardship"]
---

# Managing your sprints

As a sprint owner you can validate records marked as ready by data stewards, and export a CSV file with validated records.

You can find all your sprints in Data stewardship in the Qlik Talend Data Integration activity center. The sprints are sorted by the priority you can set when creating the sprint.

## More about sprints

A sprint is the main body of work for performing the required stewardship tasks.

Click on a sprint in Data stewardship to open it. You will see the sprint overview, but there are more tabs available.

- Overview

  This contains general sprint information and a progress indicator. If AI remediation is enabled, the overview also displays the AI processing status.
- Assigned to me

  This is where data stewards perform validation on assigned records.

  See [*Working in a resolution sprint*](Working-resolution-sprint.htm).
- Assigned to others

  This is where you can see records that are assigned to other stewards.

  For information about notifications for record assignments, see [*Sprint notifications*](Sprint-notifications.htm).
- To be validated

  This is where you can see records that are marked as ready and need a second step of validation by a sprint owner.
- Resolved

  This is where you can view all records that are marked as resolved by stewards.

## Validating records marked as ready

You can set a sprint to require a second step of validation by a sprint owner. You can set this when creating the sprint, or change it later in Settings.

To validate records, open To be validated.

Select the record to validate, and choose any of the actions:

- Approve

  This will move the record to Resolved
- Reject

  This will re-assign the record back to the data steward. Data values are not changed or reverted.

The records are now moved to Resolved.

Information noteYou can reopen resolved records by selecting the record, clicking Reopen and selecting a data steward.

## Exporting resolved records to a CSV file

You can export all resolved records to a CSV file.

- Click Export in the sprint Overview .

The CSV file is created with the name of the sprint.

## Editing a sprint

You can change sprint settings by clicking Edit and selecting which settings to edit. It is not possible to change the settings for data storage. You need the Can manage role in the space of the sprint to edit the sprint, you do not need to ba a sprint owner. Editing the sprint includes:

- Adding, removing, activating, and deactivating validation rules.
- Modifying column data types.

Information noteIf you turn off Validation required by sprint owner in Record flow, all records that are pending validation will be automatically resolved.

## Closing a sprint

You can close a sprint when you do not need it to be active.

- Click ... and select Close in the sprint overview.

When the sprint is closed, sprint owners can still access resolved records in read-only mode and export records. The sprint will not be populated with new records even if the Talend Studio Job is run.

You can resume sprint activity by clicking ... and selecting Resume.

## Deleting a sprint

You can delete a sprint in Sprints or in the sprint overview.

- Click ... and select Delete.

Information noteThe work area in Snowflake created for the sprint will not be deleted when you delete a sprint. You must clean this up manually if required.
