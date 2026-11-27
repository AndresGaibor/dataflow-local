---
title: "Strings processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Transformation/Processor-strings.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to a data warehouse", "Transforming data", "Adding transformation flows"]
---

# Strings processor

Applies multiple functions on columns with a string data type.

The Strings processor allows you to perform different character operations on String columns in a transformation flow.

## Strings properties

Properties to configure to edit your string columns.

Information note

The properties listed in this section are the default properties for all functions of this processor. Additional properties may need to be defined depending on the function you have selected.

Configuration

| Property | Configuration |
| --- | --- |
| Function name | - Add padding: Adds extra characters (padding) on the left or on the right of the original value to match an expected size. - Calculate length: Extracts the number of digits from a value (23562 -> 5; 'example' -> 7). - Change to lower case: Converts all of the cell text in the column to lower case. - Change to title case: Converts the text content from the column to title case  For example, "this is an example" will become "This Is an Example". - Change to upper case: Converts all of the cell text in the column to upper case (capitalize). - Contains text:Checks if the cell contains the specified value and returns TRUE or FALSE according to the results. The value entered is case sensitive. - Convert character width: Converts the character width to half or full width, or normalize strings. - Extract a value by index: Extracts a substring from an index position to a new column. - Generate unique identifier (UUID): Generates a unique identifier for each row of the column. - Match pattern: Creates a new column with true or false depending on whether the value matches a given pattern. - Match similar text:Creates a new column with true or false depending on whether the value is less than or equals the Levenshtein distance of a given value. - Remove all non alpha numeric characters: Cleans values that contain unexpected characters by removing all characters that are not 0-9, Aa-Zz, and accented letters. Whitespaces are kept. For example, Q=+l\*\*i€q$ 20%2,0 will become Qlik 2020. - Remove all non numeric characters: Cleans numeric values by removing all characters that are not 0-9. Decimal separators and whitespaces are kept. For example, Q=+l\*\*i€q$ 20%2,0 will become 202,0. - Remove consecutive characters: Removes consecutively repeated characters in the column. - Remove part of the text: Removes specified text from cells in the column. - Remove trailing and leading characters: Trims trailing and leading spaces or other specified characters. - Search and replace: Replaces cells or parts of cells that contain a specific value. - Simplify text (remove case, accent, etc.): Simplifies the content of the column by putting it in lower case, removing accents, normalizing using NFKD, splitting combined characters and trimming the whole string. For example, François will become francois. |
| Columns to process | Select the column or columns on which you want to apply a function in the list.  Information note If you want to apply the same function to multiple columns at once, click Open dialog icon to open a tree view that allows you to select multiple columns. |
| Create new column | Enable this option to create a new column after applying the function. If you do not enable this option, the existing column will be kept and modified. |

To rename the processor, click the ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/processor-select-columns-edit_26x24.png)Edit icon that is displayed when hovering over the default name of the processor.

To edit its description, click the ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/processor-select-columns-edit_26x24.png)Edit icon that is displayed when hovering over Description.
