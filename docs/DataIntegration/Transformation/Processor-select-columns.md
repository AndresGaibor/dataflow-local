---
title: "Select columns processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Transformation/Processor-select-columns.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to a data warehouse", "Transforming data", "Adding transformation flows"]
---

# Select columns processor

Selects (with or without distinct), renames, and reorganizes your input columns.

The Select columns processor edits your input columns by allowing you to select them with or without distinct, to rename them, and to move them in the schema according to your needs.

## Select columns properties

Properties to configure to select and restructure your data. You can add up to 10 selectors in the processor configuration.

Configuration

| Property | Configuration |
| --- | --- |
| Distinct | Enable this option to return only distinct records while selecting your columns. If this option is disabled, all duplicate records (rows) will be kept in the output. |
| Select all | Select this check box to select all columns at once. It is particularly useful if you have a large number of columns to edit. |
| Move column icon | Hold this icon to move your column up and down in the existing schema. The columns will be reorganized once you save your changes. |
|  | Select this icon that is displayed when hovering the column name to rename your column. |

To rename the processor, click the ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/processor-select-columns-edit_26x24.png)Edit icon that is displayed when hovering over the default name of the processor.

To edit its description, click the ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/processor-select-columns-edit_26x24.png)Edit icon that is displayed when hovering over Description.
