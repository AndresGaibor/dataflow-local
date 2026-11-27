---
title: "Creating a resolution sprint with a Talend Studio job"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataStewardship/Creating-sprint-job.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Validating and correcting your data with data stewardship", "Creating a resolution sprint"]
---

# Creating a resolution sprint with a Talend Studio job

You can create a resolution sprint with a Talend Studio job as data source.

This is the workflow for creating and populating a sprint:

1. Create the sprint

   You create the sprint in Data stewardship in Qlik Talend Data Integration
2. Populate the sprint

   You create a Job in Talend Studio to populate the sprint. You can create a task to run the Job periodically to submit new records for validation.

## Prerequisites

Before you create the sprint, you need the following:

- Your Qlik Cloud and Talend Cloud tenants must be connected. For more information, see [*Connecting Qlik Cloud with Talend Cloud*](../../Admin/connect-qlik-talend-tenants.htm) .
- A space to use when creating the sprint.

  Sprint owners/creators must have the following permissions in the space: Can manage, Can edit, Can view, Can view data

  Data stewards must have the following permissions in the space: Can edit, Can view, Can view data
- Optionally, if you want to work in pushdown mode, a connection to the Snowflake data warehouse that you want to use to store sprint data. Do not use a data gateway for the connection.

  All sprint users must have the following permissions in the space of the connection: Can edit, Can view, Can view data

  You can create a connection in Connections in the Qlik Talend Data Integration activity center.

  For more information about Snowflake connections, see [*Snowflake*](../TargetConnections/snowflake-target.htm).

To create a resolution sprint, click Create sprint in Data stewardship in the Qlik Talend Data Integration activity center.

## General sprint settings

1. Name

   Add a name for the sprint.
2. Space

   Select which space to create the sprint in.
3. Description

   Add a description of the sprint.
4. Sprint population

   Select Talend Studio job.

Click Next when you are ready to proceed to define the data schema.

## Define the data schema

You must now define the data schema.

Information noteThe data schema must conform to the data schema of the output from the Talend Studio Job that populates the sprint.

Add columns to the data schema by clicking Add column. Click Next when you are ready to proceed to define the data storage.

Supply Name, Description, and Type for each column.

You can use Lock column and Exclude column to control which columns can be viewed and edited. This is helpful to create a validation view with only the columns required for validation available.

- Lock column

  If you select this, the column will be visible for data stewards, but cannot be edited. Use this for columns that do not need to be validated, but are useful as reference for the data stewards.
- Exclude column

  If you select this, the column will not be visible for data stewards. Use this for columns that are not needed as reference for the data stewards.

### Applying validation rules

You can apply validation rules to a column to make it easier to spot invalid data. Invalid data will be highlighted in the column.

- Click + to apply a validation rule.

You can either select an existing validation rule or create a new validation rule.

For more information about creating validation rules, see [*Creating a validation rule*](../DataProducts/Working-with-validation-rules.htm#Creating).

## Connect to data storage

You can select where to store sprint data.

- Qlik Cloud storage

  Sprint data is securely stored in Qlik Cloud in encrypted form.

  Information noteQlik Cloud storage capacity is limited to 10 GB per tenant.
- External data storage

  Data remains in your selected storage. Snowflake is currently the only supported data warehouse. Stewardship runs in push-down mode, meaning processing happens directly in Snowflake .

### Connecting to external storage

You must connect to the cloud data warehouse that you want to use to store sprint data. Snowflake is currently the only supported data warehouse.

1. Select the connection to the data warehouse.
2. Select which database to use.
3. Select if you want to use an existing database schema, or a new database schema.

   If you select New database schema, set the name of the new schema.
4. Set the name of the table to use for resolved sprint data in Table name for resolved records.

Click Next when you are ready to proceed to define roles and other settings for the sprint workflow.

## Define roles and settings for the sprint workflow

The last step is to define roles and other settings.

1. Add owners

   Add all users that should be owner of the sprint.
2. Add stewards

   Add all data stewards for this sprint.
3. Data remediation

   Enable this option to let an AI agent correct invalid cell values in the sprint. The AI agent edits the values and marks records as ready, then reassigns them to a data steward for review.

   This option requires that a Tenant Admin has enabled cross-region inference. For more information, see [*Enabling cross-region inference*](../../Admin/cross-region-data-processing.htm).

   Qlik Cloud Government note

   Data remediation is not available in Qlik Cloud Government.
4. Record workflow

   You can select if you want to add a second validation step by sprint owners.

   Information noteIf a user that is both sprint owner and data steward validates a record, the second validation step is by-passed.
5. Record assignment

   Select if you want to auto-assign records, or if you want to assign records manually to data stewards.

   For information about who receives notifications when roles or records are assigned, see [*Sprint notifications*](Sprint-notifications.htm).

   - Auto

     Records are assigned automatically to data stewards with an even distribution. Records will not be assigned to sprint owners that are not also a data steward.
   - Manual

     Records will initially not be assigned to a data steward. Sprint owners and data stewards can assign records from Unassigned.
6. Priority

   You can set priority for the sprint. Priority is used to sort sprints in the sprint list.

Click Save when you are ready to create the sprint.

The sprint is now created. The next step is to populate the sprint using a Talend Studio job.

## Populating the sprint

You create a Job in Talend Studio using the tdsOutput component to populate the sprint. You can create a task to run the Job periodically to submit new records for validation.

For more information, see [tDSOutput settings](https://help.qlik.com/talend/en-US/components/8.0/data-stewardship/tdsoutput).
