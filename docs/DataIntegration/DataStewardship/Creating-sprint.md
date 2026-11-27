---
title: "Creating a resolution sprint"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataStewardship/Creating-sprint.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Validating and correcting your data with data stewardship"]
---

# Creating a resolution sprint

Creating a resolution sprint is the first step when validating data using Data stewardship.

You create a sprint which is the main body of work for the required stewardship tasks.

## Prerequisites

Before you create the sprint, you need:

- A data space to use when creating the sprint.

  You must have Can manage permission to be able to create a sprint.

  - Sprint owners must have the following permissions in the space: Can manage, Can edit, Can view, Can view data
  - Data stewards must have the following permissions in the space: Can edit, Can view, Can view data
- Optionally, if you want to work in pushdown mode, a Snowflake data warehouse that can be used to store sprint data. You also need a data connection to the data warehouse.

## Creating a sprint

You can create the sprint using either a Talend Studio job or an exported CSV file. When creating the sprint, you can enable AI remediation to let an AI agent correct invalid cell values and reassign records to stewards for review. AI remediation requires that cross-region inference is enabled by a tenant admin.

For instructions, see:

[*Creating a resolution sprint with a Talend Studio job*](Creating-sprint-job.htm)

[*Creating a resolution sprint from a CSV file*](Creating-sprint-file.htm)
