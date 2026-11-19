---
title: "Pivot processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataFlow/data-flow-processor-pivot.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Data flow", "Data flow processors"]
---
# Pivot processor

Pivots field values into columns.

For data stored in tables, the **Pivot** processor allows you to rearrange the table so that values from a field are stored as fields instead, highlighting data differently according to your needs.

## Usage

- The **Pivot** processor requires one input flow and can generate only one output flow.
- Ensure that enough data is loaded in the preview to generate all the output columns. Use the cog icon in the Preview panel to set the load limit.
- When applying the pivot processor configuration, the data flow has to run in the background first.

## Properties

Properties to configure to pivot your columns.

Configuration

| Property | Configuration |
| --- | --- |
| **Field to pivot** | Use the check box to select the field to pivot into a column. |
| **Value field** | Use the check box to select the field that contains the values that will be used in the pivoted field. |
| **Aggregation function** | Select the operation you want to apply on the values for your new fields:   - No aggregation (Only)  **Note:** An aggregation based on the [Only](https://help.qlik.com/en-US/qlikview/May2024/Subsystems/Client/Content/QV_QlikView/Scripting/AggregationFunctions/only.htm) script function still occurs. - Sum - Average - Count - Count Distinct - Minimum - Maximum - Concatenate |

To rename the processor or edit its description, point your mouse over the name or description to change in the **Properties** panel and click the ![Edit](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) **Edit** icon.

## Example

The following example describes the effect of the pivot function on a table containing some attributes about inventory items (ID, size colour, availability), but organized in rows, where you would need multiple rows to get all information about a specific product.

In this case, you want to use the different values of the **Attribute** field to create new fields, and fill them with the values contained in the **Value** field. To get this result, configure the processor with **Attribute** as **Field to pivot**, and use the **Value** field as **Value field**. You do not need to add any aggregation operation, as you want to have every value displayed according to the **Product ID**.

![effect of the unpivot function on a table](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/pivot_example_data_flow.jpg)
