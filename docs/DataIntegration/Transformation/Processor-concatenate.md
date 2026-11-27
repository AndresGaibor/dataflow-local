---
title: "Concatenate processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Transformation/Processor-concatenate.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to a data warehouse", "Transforming data", "Adding transformation flows"]
---

# Concatenate processor

Merges the content of several columns into a new one.

The Concatenate processor is used in a transformation flow to modify your input columns by allowing you to concatenate them together.

## Concatenate properties

Properties to configure to concatenate your input columns.

Configuration

| Property | Configuration |
| --- | --- |
| Function name | Concatenate with value/another field: Select this function to merge the content of this column with another column or a custom value, and display it in a new column. |
| Columns to process | Select the column or columns on which you want to apply a function in the list.  Information note If you want to apply the same function to multiple columns at once, click Open dialog icon to open a tree view that allows you to select multiple columns. |
| Create new column | Enable this option to create a new column after applying the function. If you do not enable this option, the existing column will be kept and modified. |
| Rename new column | Give a custom name to the newly created column. |
| Prefix (optional) | Add a prefix to the value of the output column. |
| Use with | - Other column: Select this option to concatenate the column to process with another column.- Value: Select this option to concatenate the column to process with the custom value of your choice. |
| Column | Select the column that will be concatenated with the column you have selected as Column to process. |
| Separator | Type in the separator you want to use when combining the two columns/values. If left empty, no separator will be used. |
| Add separator | - Both values are empty: Select this option to add a separator only when both columns/values are not empty.- Always: Select this option to add a separator to all combined columns/values |
| Suffix (optional) | Add a suffix to the value of the output column. |

To rename the processor, click the ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/processor-select-columns-edit_26x24.png)Edit icon that is displayed when hovering over the default name of the processor.

To edit its description, click the ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/processor-select-columns-edit_26x24.png)Edit icon that is displayed when hovering over Description.
