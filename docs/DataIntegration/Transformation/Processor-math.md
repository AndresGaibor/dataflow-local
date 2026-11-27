---
title: "Math processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Transformation/Processor-math.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to a data warehouse", "Transforming data", "Adding transformation flows"]
---

# Math processor

Performs calculation and computation operations on columns containing numbers.

The Math processor allows you to compute and calculate values from and between columns in a transformation flow.

## Math properties

Properties to configure to compute or calculate values from columns.

Configuration

| Property | Configuration |
| --- | --- |
| Function name | - Add, substract, multiply, and divide: Performs an operation/calculation on the column with another columnor with a fixed value: Add/sum (+), multiply (x), subtract (-), or divide(/). - Base 10 Logarithm: Computes the base 10 logarithm from the column. - Absolute value: Calculates the absolute value for all the numeric values in the column. - Cosine: Computes the trigonometric Cosine from the column. - Exponential: Calculates the exponential of the column numbers. - Max:Compares with another column or a constant and returns the largest value. - Min: Compares with another column or a constant and returns the smallest value. - Modulo: Calculates the remainder of a division operation. - Natural logarithm: Computes the natural logarithm from a column. - Negate: Negates the column numbers. - Power: Multiplies to the power of another column or a constant. - Sine: Computes the trigonometric Sine from the column numbers. - Square root: Calculates the square root of the column numbers. - Tangent: Computes the trigonometric Tangent from the column numbers. |
| Columns to process | Select the column or columns on which you want to apply a function in the list.  Information note If you want to apply the same function to multiple columns at once, click Open dialog icon to open a tree view that allows you to select multiple columns. |
| Create new column | Enable this option to create a new column after applying the function. If you do not enable this option, the existing column will be kept and modified. |

To rename the processor, click the ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/processor-select-columns-edit_26x24.png)Edit icon that is displayed when hovering over the default name of the processor.

To edit its description, click the ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/processor-select-columns-edit_26x24.png)Edit icon that is displayed when hovering over Description.
