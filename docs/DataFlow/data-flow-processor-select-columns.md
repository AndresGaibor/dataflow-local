---
title: "Select fields processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataFlow/data-flow-processor-select-columns.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Data flow", "Data flow processors"]
---
# Select fields processor

Renames and reorganizes your fields.

The **Select fields** processor allows you to manipulate the schema of the input flow and keep only the relevant fields depending on your needs. You can move fields around and rename them.

## Usage

The **Select fields** processor requires one input flow and can generate only one output flow.

## Properties

Properties to configure to select and restructure your data.

Configuration

| Property | Configuration |
| --- | --- |
| **Distinct** | Enable this option to return only different (distinct) values while selecting your fields. If this option is disabled, all duplicate values will be kept in the output. |
| **Select all** | Select this checkbox to select all fields at once. It is particularly useful if you have a large number of fields to edit. |
| ![Move column](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/ic_data_flow_move_column.png) | Hold this icon to move your field up and down in the existing schema. The fields will be reorganized once you save your changes. |
| ![Edit](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ic_qc_Edit.png) | Select this icon that is displayed when hovering the field name to rename your field. |

To rename the processor or edit its description, point your mouse over the name or description to change in the **Properties** panel and click the ![Edit](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) **Edit** icon.

## Example

The data used as source in this example contains data about sales, such as number of units sold, costs, prices, revenue and profits.

![A dataset with fields in the wrong order](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/select_fields_example_1.png)

You can see that three field names have a different format and case from the rest, namely **Total\_cost**, **Total\_revenue** and **Total\_profit**, and it would make more sense for general readability to put them together at the end of the dataset. You can use the **Select fields** processor to reorganize and rename your fields to improve the consistency of your data.

In the processor properties, select the **Select all** checkbox so that all the fields are kept in the output flow. Point your mouse over the fields to rename and click the ![Edit](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ic_qc_Edit.png)**Edit** icon to edit the three field names as follow:

- Total\_cost as Total Cost
- Total\_revenue as Total Revenue
- Total\_profit as Total Profit

Click the **Submit** button or press **Enter**.

Use the **=** icon to drag and drop the three fields at the end of the list in this order: Total Revenue, Total Cost, Total Profit.

![A data flow using the select fields processor to rename and reorder fields](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/select_fields_example_2.png)

The output of the data flow will be easier to read and the field will have a consistent naming convention.
