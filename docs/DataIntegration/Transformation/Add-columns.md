---
title: "Adding columns to a dataset"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Transformation/Add-columns.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Managing datasets"]
---

# Adding columns to a dataset

You can add columns to apply basic row-based transformations to a dataset.

You can add columns in Landing tasks that use Qlik Data Gateway - Data Movement, Storage, Transform, and Data mart tasks. You can also add columns in SaaS-managed landing, lake landing, replication, and Streaming Transform tasks. Expression elements depend on the task, source endpoint, and data platform.

1. Click Datasets.
2. Click Add column.

   You will need to provide a name for the column, and a data type.

   You can also set the column to be a key, and if it should be nullable.

   For some data types you can make additional settings, for example, length or precision.
3. Click the ![Open expression builder](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression.svg) control on the column that you added.

   The expression builder is opened.
4. Build and test an expression to define the column values. See [*Building expressions*](Building-expressions.htm).
5. When you are ready, click OK.

The column is now added, based on the expression you used.

Tip noteTo remove an added column, select it and click Revert.

## Limitations

- It is not possible to use space characters in the column name when using Google BigQuery as data platform.
