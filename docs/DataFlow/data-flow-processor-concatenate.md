---
title: "Concatenate fields processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataFlow/data-flow-processor-concatenate.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Data flow", "Data flow processors"]
---
# Concatenate fields processor

Merges the content of two fields.

The **Concatenate fields** processor allows you to merge data that is split between different fields or concatenate the content of a field with a constant string.

## Usage

The **Concatenate fields** processor requires one input flow and can generate only one output flow.

## Properties

Properties to configure to concatenate your input fields.

Configuration

| Property | Configuration |
| --- | --- |
| **Function name** | **Concatenate with value/another field**: Select this function to merge the content of this field with another field or a custom value, and display it in a new field. |
| **Fields to process** | Select the field or fields on which you want to apply a function in the list. |
| **Create new field** | Enable this option to create a new field after applying the function. If you do not enable this option, the existing field will be kept and modified. |
| **Rename new field** | Give a custom name to the newly created field. |
| **Prefix** (optional) | Add a prefix to the value of the output field. |
| **Use with** | - **Field**: Select this option to concatenate the field to process with another field from the drop-down list. - **Value**: Select this option to concatenate the field to process with the custom value of your choice, set in the **Suffix** field. |
| **Separator** | Type in the separator you want to use when combining the two fields/values. |
| **Add separator** | - **Both values not empty**: Select this option to add a separator only when both fields/values are not empty. - **Always**: Select this option to add a separator to all combined fields/values. |
| **Suffix** (optional) | Add a suffix to the value of the output field. |

To rename the processor or edit its description, point your mouse over the name or description to change in the **Properties** panel and click the ![Edit](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) **Edit** icon.

## Example

![data with separated date information that need a concatenation](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/concatenate_example_1.png)

![Data flow using a concatenate fields processor](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/concatenate_example_2.png)
