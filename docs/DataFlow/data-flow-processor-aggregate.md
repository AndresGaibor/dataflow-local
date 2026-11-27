---
title: "Aggregate processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataFlow/data-flow-processor-aggregate.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Data flow", "Data flow processors"]
---

# Aggregate processor

Performs operations on groups of the data.

The Aggregate processor allows you to group data from the input flow by aggregation sets, which values can then be used for operations that are outputted in a new field.

## Usage

The Aggregate processor requires one input flow and can generate only one output flow.

## Properties

Properties to configure to aggregate your records.

Configuration

| Category name | Property name | Configuration |
| --- | --- | --- |
| Group by (optional) | Field | In the list, select one or more fields you want to use for your aggregation sets. |
| Aggregate fields | Fields | Select the field or fields on which you want to perform a calculation operation. |
| Aggregate fields | Operation | Select the operation you want to apply on your aggregation set:   - Average - Count - Count Distinct - Concatenate - First - Last - Maximum - Maximum string - Median - Minimum - Minimum string - Percentile - Standard deviation - Sum |
| Aggregate fields | Delimiter | Only applicable for Concatenate operation. Enter the text that separates each concatenated item. |
| Percentile | Percentile | Only applicable for Percentile operation. Enter an integer between 1 and 99, indicating the value at which aggregations are divided. The higher the percentile, the higher the corresponding aggregated values. |
| Aggregate fields | Output field name (optional) | Enter a name for the generated output field. If left empty, the default generated field name will contain the name of the selected field with the name of the selected operation. |

To rename the processor or edit its description, point your mouse over the name or description to change in the Properties panel and click the ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit icon.

## Example

The data used as source in this example contains customer information such as names, age groups, gender and number of purchases.

![dataset containing customer information](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/aggregate_example_1.png)

To gain more insight on the data, you can use the Aggregate processor to create new statistics, such as the average number of purchases by age group.

In the processor properties, configure the Age group field as field to group by, and Purchases as the field to perform operations on. Select Average as operation, and give a name to the field that will be generated in the output.

To perform another operation based on the age groups like the total number of purchases for example, click Add new. This time select Sum as operation.

![a data flow configuration to aggregate purchases per age group](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/aggregate_example_2.png)

The output flow now contains the Age group field, as well as the two fields containing the new data for statistical analysis. Other fields from the source data are not included in the output of the processor.
