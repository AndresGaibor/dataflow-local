---
title: "Validating and correcting your data with data stewardship"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataStewardship/Governing-data-stewardship.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data"]
---

# Validating and correcting your data with data stewardship

With Data stewardship in Qlik Talend Cloud, you can draw on subject matter experts to validate and correct your data. Use your existing semantic types and validation rules to make sure that the data is consistently formed. This extends automated pipelines with human-in-the-loop remediation from domain expertise. When the data is validated you can re-inject it into the original data source, or to any downstream system.

Information noteYou need one of the following subscriptions:

- Qlik Talend Cloud Enterprise
- Qlik Talend Cloud Premium

Qlik Cloud Government note

Data remediation using GenAI is not available in Qlik Cloud Government.

You create a sprint which is the main body of work for the validation and remediation. The sprint contains information about:

- The source data
- The data schema to use for validation
- The owners of the sprint
- The data stewards that are defined
- The data storage used for sprint data
- Workflow settings

For information about data storage options and data residency during a sprint, see [*Creating a resolution sprint from a CSV file*](Creating-sprint-file.htm#Connect-to-data-storage).

You can define the following user roles:

- Sprint owner

  Sprint owners can validate records that are resolved by data stewards. They can also access records that are resolved and export data.
- Data steward

  A data steward is assigned records to resolve quality issues.

During a sprint, data stewards and sprint owners can also collaborate directly on individual records by adding comments to cells and building a chronological discussion list on each cell. A cell comment can capture context for a value, explain a correction, or ask for clarification before a record is resolved. For more information, see [*Working with cell comments in a resolution sprint*](Working-with-cell-comments-in-a-resolution-sprint.htm) and [*Comment threads and permissions in a sprint*](Comment-threads-and-permissions-in-a-sprint.htm).

You create sprints in Data stewardship in the Qlik Talend Data Integration activity center. You can create Resolution sprints that correct and curate data in one or more fields in the dataset that requires validation. This is the workflow:

1. [*Creating a resolution sprint*](Creating-sprint.htm)

   Create a sprint and define the data to validate. You can either populate the sprint with a Talend Studio Job, or import a CSV file with data.

   Data stewards are defined to perform the validation. Records can be assigned either manually or automatically.
2. [*Working in a resolution sprint*](Working-resolution-sprint.htm)

   Data stewards validate the data in the assigned records. If Data remediation is enabled, an AI agent corrects invalid cell values and reassigns records to stewards for review. For more information, see [*Reviewing AI fixes in a resolution sprint*](Reviewing-AI-suggestions.htm).
3. [*Managing resolved records*](Managing-resolved%20records.htm)

   - If you populated the sprint with a Talend Studio Job, you create a Talend Studio Job to retrieve the validated records and return them to the original data source, or to any other required destination.
   - If you populated the sprint with a CSV file, the sprint is concluded by exporting the validated data to a CSV file. You can update the data source with validated data by importing the exported CSV file.
