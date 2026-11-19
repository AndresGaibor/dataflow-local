---
title: "Strings processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataFlow/data-flow-processor-strings.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Data flow", "Data flow processors"]
---
# Strings processor

Performs string related operations.

The **Strings** processor allows you to apply various functions on fields with a string data type, such as formatting, cleaning, adding or removing characters, or searching for specific values.

## Usage

The **Strings** processor requires one input flow and can generate only one output flow.

## Properties

Properties to configure to edit your string fields.

> **Note:** The properties listed in this section are the default properties for all functions of this processor. Additional properties may need to be defined depending on the function you have selected.

Configuration

| Property | Configuration |
| --- | --- |
| **Function name** | - **Change to upper case**: Converts all of the cell text in the field to upper case (capitalize). - **Change to lower case**: Converts all of the cell text in the field to lower case. - **Change to title case**: Converts the text content from the field to title case. For example, "this is an example" will become "This Is An Example". - **Search and replace**: Replaces cells or parts of cells that contain a specific value or matches a regular expression. - **Remove part of the text**: Removes specified text or regex from cells in the field. - **Contains text**: Checks if the cell contains the specified value and returns TRUE or FALSE according to the results. The value entered is case sensitive. - **Match similar text**: Creates a new field with TRUE or FALSE depending on whether the value is less than or equals the Levenshtein distance of a given value. - **Extract a value by index**: Extracts a substring from an index position to a new field. Index 0 corresponds to the first character. - **Remove non alpha numeric characters**: Cleans values that contain unexpected characters by removing all characters that are not 1234567890abcdefghijklmnopqrstuvwxyzáàâäãåæçéèêëíìîïñóòôöõøœßúùûüABCDEFGHIJKLMNOPQRSTUVWXYZÁÀÂÄÃÅÆÇÉÈÊËÍÌÎÏÑÓÒÔÖÕØŒSSÚÙÛÜ. Whitespaces are kept. For example, **Q=+l\*\*i€q$ 20%2,0** will become **Qlik 2020**. - **Remove non numeric characters**: Cleans numeric values by removing all characters that are not 0-9. Decimal separators, the minus sign, and whitespaces are kept. For example, **Q=+l\*\*i€q$ 20%2,0** will become **202,0**. - **Remove trailing and leading characters**: Trims trailing and leading whitespaces or other characters. - **Add padding**: Adds extra characters (padding) on the left or on the right of the original value to match an expected size. - **Convert to string**: Changes the type of the data to string. - **Calculate length**: Returns the number of characters of a string (23562 -> 5; 'example' -> 7). - **Match pattern**: Checks if cells in fields match a specific pattern. - **Remove consecutive characters**: Removes repeated whitespaces or other characters in the cells. |
| **Fields to process** | Select the field or fields on which you want to apply a function in the list. |
| **Create new field** | Enable this option to create a new field after applying the function. If you do not enable this option, the existing field will be kept and modified. |
| **Rename new field** | Give a custom name to the newly created field. |

To rename the processor or edit its description, point your mouse over the name or description to change in the **Properties** panel and click the ![Edit](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) **Edit** icon.
