---
title: "Cleanse processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Transformation/Processor-cleanse.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to a data warehouse", "Transforming data", "Adding transformation flows"]
---

# Cleanse processor

Replaces the content of records or fills records with a given value.

The Cleanse processor allows you to perform different operations to cleanse columns and records in a transformation flow.

## Cleanse properties

Properties to configure to cleanse columns and records.

Configuration

| Property | Configuration |
| --- | --- |
| Function name | - Fill cells with value: Select this function to fill all cells from this column with a given value. - Fill empty cells with text: Select this function to fill empty cells from this column with a given value. |
| Columns to process | Select the column or columns on which you want to apply a function in the list.  Information note If you want to apply the same function to multiple columns at once, click Open dialog icon to open a tree view that allows you to select multiple columns. |
| Use with | - Other column: Select this option to concatenate the column to process with another column.- Value: Select this option to concatenate the column to process with the custom value of your choice. |

To rename the processor, click the ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/processor-select-columns-edit_26x24.png)Edit icon that is displayed when hovering over the default name of the processor.

To edit its description, click the ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/processor-select-columns-edit_26x24.png)Edit icon that is displayed when hovering over Description.
