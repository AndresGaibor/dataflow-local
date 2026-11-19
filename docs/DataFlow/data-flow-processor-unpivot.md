---
title: "Unpivot processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataFlow/data-flow-processor-unpivot.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Data flow", "Data flow processors"]
---
# Unpivot processor

Unpivots table columns to rows.

For data stored in tables, the **Unpivot** processor allows you to rearrange the table so that some or all columns are stored as rows instead, highlighting data differently according to your needs. Users familiar with Qlik script may know this operation as crosstable.

## Usage

The **Unpivot** processor requires one input flow and can generate only one output flow.

## Properties

Properties to configure to unpivot your columns.

Configuration

| Property | Configuration |
| --- | --- |
| **Unpivot fields** | Select the field or fields on which you want to apply a function in the list. |
| **Attribute field name** | Give a name to the field that will represent the field names in the input. |
| **Value field name** | Name of the field with the values. |

To rename the processor or edit its description, point your mouse over the name or description to change in the **Properties** panel and click the ![Edit](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) **Edit** icon.

## Example

The following example describes the effect of the unpivot function on a table containing a target number for sales, by region and sales person. In this case, each target sales number needs to be displayed on a single row. To obtain this output, configure the processor to unpivot the **Lisa**, **James** and **Sharon** fields, enter sales person as name for the **Attribute field name**, and target as **Value field name**.

![effect of the unpivot function on a table](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/unpivot_example_data_flow.png)
