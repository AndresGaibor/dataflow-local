---
title: "Cleanse processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataFlow/data-flow-processor-cleanse.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Data flow", "Data flow processors"]
---

# Cleanse processor

Fills or replaces fields with a given value.

The Cleanse processor allows you to modify the content of your fields by using either the value of your choice, or a standardized value from another field.

## Usage

The Cleanse processor requires one input flow and can generate only one output flow.

## Properties

Properties to configure to cleanse fields and records.

Configuration

| Property | Configuration |
| --- | --- |
| Function name | - Fill cells with value: Select this function to fill all cells from this field with a given value. - Fill empty cells with values: Select this function to fill empty cells from this field with a given value. |
| Fields to process | Select the field or fields on which you want to apply a function in the list. |
| Use with | - Other field: Select this option to concatenate the field to process with another field from the drop-down list. - Value: Select this option to concatenate the field to process with the custom value of your choice, set in the Value field. |

To rename the processor or edit its description, point your mouse over the name or description to change in the Properties panel and click the ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit icon.
