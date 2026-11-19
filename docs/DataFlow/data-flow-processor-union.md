---
title: "Union processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataFlow/data-flow-processor-union.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Data flow", "Data flow processors"]
---
# Union processor

Appends records from a second flow.

The **Union** processor allows you to append fields and records from one input flow to the end of another. You can choose to include or exclude duplicates from the resulting flow. Users familiar with Qlik script may know this operation as concatenate.

## Usage

- The **Union** processor can have multiple input flows and can generate only one output flow.
- All inputs don't need to have the same fields. If one input has a field the other does not have, the field is added and missing values filled with **Null**.

## Properties

Properties to configure to append records from multiple inputs.

Configuration

| Property | Configuration |
| --- | --- |
| **Union all** | Enable this option to return all values, including duplicates, while appending your fields. If this option is disabled, all duplicate values will be excluded from the output. |

To rename the processor or edit its description, point your mouse over the name or description to change in the **Properties** panel and click the ![Edit](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) **Edit** icon.
