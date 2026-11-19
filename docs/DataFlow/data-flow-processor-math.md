---
title: "Math processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataFlow/data-flow-processor-math.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Data flow", "Data flow processors"]
---
# Math processor

Performs calculations on numbers.

The **Math** processor allows you to perform calculation operations on fields containing numbers. You can compute and calculate values within a field, as well as between fields.

## Usage

The **Math** processor requires one input flow and can generate only one output flow.

## Properties

Properties to configure to compute or calculate values from fields.

Configuration

| Property | Configuration |
| --- | --- |
| **Function name** | - **Add**: Performs an addition on the field with another field or with a fixed value. - **Modulo**: Calculates the remainder of a division operation. - **Absolute value**: Calculates the absolute value for all the numeric values in the field. - **Divide**: Performs a division on the field with another field or with a fixed value. - **Negate**: Negates the field numbers. - **Min**: Compares with another field or a constant and returns the smallest value. - **Max**: Compares with another field or a constant and returns the largest value. - **Base 10 Logarithm**: Computes the base 10 logarithm from the field. - **Multiply**: Performs a multiplication on the field with another field or with a fixed value. - **Natural logarithm**: Computes the natural logarithm from a field. - **Exponential**: Calculates the exponential of the field numbers. - **Power**: Multiplies to the power of another field or a constant. - **Square root**: Calculates the square root of the field numbers. - **Subtract**: Performs a subtraction on the field with another field or with a fixed value. - **Cosine**: Computes the trigonometric Cosine from the field. - **Sine**: Computes the trigonometric Sine from the field numbers. - **Tangent**: Computes the trigonometric Tangent from the field numbers. |
| **Fields to process** | Select the field or fields on which you want to apply a function in the list. |
| **Create new field** | Enable this option to create a new field after applying the function. If you do not enable this option, the existing field will be kept and modified. |
| **Rename new field** | Give a custom name to the newly created field. |

To rename the processor or edit its description, point your mouse over the name or description to change in the **Properties** panel and click the ![Edit](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) **Edit** icon.

## Example

The data used as source in this example contains data about sales to different customers with details on costs, prices, and number of units sold.

![Dataset with the number and price of orders](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/maths_example_1.png)

However, it is missing important information that could be used in analytics applications, namely total cost, total revenue and total profit. Using the **Math** processor you can calculate these numbers by performing operations between columns.

Calculating these three figures will require three processors since only one operation can be performed by a processor:

1. The first processor will be used to multiply the number of units sold by the price of an unit to calculate the total revenue. Select the **Add, subtract, multiply, and divide** function and **Units sold** as field to process. Choose **x** as operator, and use **Unit Price** as second field to use. Select the **Create new field** checkbox, and name the new field Total\_revenue.
2. Then, the second processor will be used to multiply the number of units sold by the cost of an unit to calculate the total cost. Select the **Add, subtract, multiply, and divide** function and **Units sold** as field to process. Choose **x** as operator, and use **Unit Cost** as second field to use. Select the **Create new field** checkbox, and name the new field Total\_cost.
3. Finally, the third processor will subtract the total cost from the total revenue to obtain the total profit. Select the **Add, subtract, multiply, and divide** function and **Total\_revenue** as field to process. Choose **-** as operator, and use **Total\_cost** as second field to use. Select the **Create new field** checkbox, and name the new field Total\_profit.

![A data flow with math processors to calculate total profit and cost](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/maths_example_2.png)

Running the data flow will create three new fields with the results of the calculation in the target, and allow you to analyze the data further.
