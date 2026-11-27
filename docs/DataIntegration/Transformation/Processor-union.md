---
title: "Union processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Transformation/Processor-union.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to a data warehouse", "Transforming data", "Adding transformation flows"]
---

# Union processor

Appends similar records from a dataset to the end of another, with or without removing duplicates (union all).

The Union processor allows you to append records from multiple datasets in a transformation flow.

Tip noteDrag and drop datasets to the Union processor to add more datasets to the union.

## Union properties

Properties to configure to append records from multiple datasets.

Configuration

| Property | Configuration |
| --- | --- |
| Union all | Enable this option to return only distinct values while appending your columns. If this option is disabled, all duplicate values will be kept in the output. |

To rename the processor, click the ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/processor-select-columns-edit_26x24.png)Edit icon that is displayed when hovering over the default name of the processor.

To edit its description, click the ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/processor-select-columns-edit_26x24.png)Edit icon that is displayed when hovering over Description.

## Limitations

Fields are matched according to the ordinal order, and not using their names. For example, if there are:

- Table t1 with fields f1, f2, f3
- Table t2 with fields f3, f2, f1

When running union with t1 and t2 to table t3:

- For each record from t1, its fields would be f1, f2, f3.
- For each record from t2 its fields would be f3, f2, f1.

If you want to match the fields differently, use the Select columns processor to change column order in one of the input tables.
