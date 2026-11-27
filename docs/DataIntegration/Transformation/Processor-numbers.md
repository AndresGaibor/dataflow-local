---
title: "Numbers processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Transformation/Processor-numbers.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to a data warehouse", "Transforming data", "Adding transformation flows"]
---

# Numbers processor

Performs multiple transformations (formatting, comparing, rounding) on columns containing numbers.

The Numbers processor allows you to modify records with a numeric data type in a transformation flow.

## Numbers properties

Properties to perform operations on numeric records.

Information note

The properties listed in this section are the default properties for all functions of this processor. Additional properties may need to be defined depending on the function you have selected.

Configuration

| Property | Configuration |
| --- | --- |
| Function name | - Compare numbers: Compares this record to another record or a constant. - Remove fractional part: Rounds towards zero. (3.74 -> 3) and (-3.74 -> -3). - Remove negative values: Replaces negative integers or decimal values with an empty values. - Round value using ceil mode: Rounds up value to the nearest number, depending on the precision you set. (3.14 -> 4 if Precision is set to 0, and 3.14 -> 3.2 if Precision is set to 1). - Round value using down mode: Rounds towards zero. (3.74 -> 3 and -3.74 -> -3 for a Precision set to 0). - Round value using floor mode: Rounds down value to the nearest number, depending on the precision you set. (3.74 -> 3 if Precision is set to 0, and 3.74 -> 3.7 if Precision is set to 1). - Round value using halfUp mode: Rounds value to the closest number, depending on the precision you set. (3.14 -> 3 and 3.74 -> 4 if Precision is set to 0). |
| Columns to process | Select the column or columns on which you want to apply a function in the list.  Information note If you want to apply the same function to multiple columns at once, click Open dialog icon to open a tree view that allows you to select multiple columns. |
| Create new column | Enable this option to create a new column after applying the function. If you do not enable this option, the existing column will be kept and modified. |

To rename the processor, click the ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/processor-select-columns-edit_26x24.png)Edit icon that is displayed when hovering over the default name of the processor.

To edit its description, click the ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/processor-select-columns-edit_26x24.png)Edit icon that is displayed when hovering over Description.

## Limitations

- If the target platform is Amazon Redshift, rounding with ceil or floor will always return an integer, which will ignore the precision.
