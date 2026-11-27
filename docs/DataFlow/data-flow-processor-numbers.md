---
title: "Numbers processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataFlow/data-flow-processor-numbers.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Data flow", "Data flow processors"]
---

# Numbers processor

Performs number related operations.

The Numbers processor allows you to apply various functions to fields with a numeric data type, such as formatting, comparing, or rounding numbers.

## Usage

The Numbers processor requires one input flow and can generate only one output flow.

## Properties

Properties to configure to perform operations on your Number fields.

Configuration

| Property | Configuration |
| --- | --- |
| Function name | - Round value using halfUp mode: Rounds value to the closest number, depending on the precision you set. (3.14 -> 3 and 3.74 -> 4 if Precision is set to 0). - Round value using ceil mode: Rounds up value to the nearest number, depending on the precision you set. (3.14 -> 4 if Precision is set to 0, and 3.14 -> 3.2 if Precision is set to 1). - Round value using floor mode: Rounds down value to the nearest number, depending on the precision you set. (3.74 -> 3 if Precision is set to 0, and 3.74 -> 3.7 if Precision is set to 1). - Round value using down mode: Rounds towards zero. (3.74 -> 3 and -3.74 -> -3 for a Precision set to 0). - Remove fractional part: Rounds towards zero. (3.74 -> 3) and (-3.74 -> -3). - Compare numbers: Compares this record to another record or a constant. - Remove negative values: Replaces negative integers or decimal values with an empty values. - Convert to numbers: Interprets a string as number using decimal and thousand separators specified manually. - Format number: Changes how numeric values are displayed using predefined patterns or custom patterns. |
| Fields to process | Select the field or fields on which you want to apply a function in the list. |
| Create new field | Enable this option to create a new field after applying the function. If you do not enable this option, the existing field will be kept and modified. |
| Rename new field | Give a custom name to the newly created field. |

To rename the processor or edit its description, point your mouse over the name or description to change in the Properties panel and click the ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit icon.
