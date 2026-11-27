---
title: "Strings functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/TableRecipe/strings-functions-table-recipe.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Table recipe", "Table recipe functions"]
---

# Strings functions

## Add padding

Adds one or more occurrence of a character at the beginning or the end of the content of the cells.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Repeat count | Number of times the chosen character will be added to the content of the cell. |
| Add character | Enter the character you want to add to the content of the cell as padding. |
| Position | Select where you want to add the padding character.   - Left: The chosen character will be added before the content of the cells. - Right: The chosen character will be added after the content of the cells. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| TableRecipe | - Repeat count: 5 - Add character 1 - Position: Left | 11111TableRecipe |

## Calculate length

Calculates the number of characters from each cell of the column and outputs the result in new column.

A new column containing the result of the function will be created for each of the selected column. The default name of the new columns will be <original\_column\_name>\_length.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |

### Example

| Input | Output |
| --- | --- |
| TableRecipe | 11 |

## Change to lower case

Converts all the text from the column cells to lower case.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Output |
| --- | --- |
| Table Recipe | table recipe |

## Change to title case

Converts all the text from the column cells to title case.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Output |
| --- | --- |
| table recipe | Table Recipe |

## Change to upper case

Converts all the text from the column cells to upper case.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Output |
| --- | --- |
| Table Recipe | TABLE RECIPE |

## Concatenate columns

Merges the content of a column with another one or a fixed value.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Prefix | Optionally add a character or string at the beginning of the merged data. |
| Use with | - Value: Select this option to concatenate the column content with a fixed value, set in the Value field. - Other column: Select this option to concatenate the column content with the content from another column, set in the Column drop-down list. |
| Separator | Input any character to act as separator for the merged data. |
| Add separator | Select the condition on which the separator will be applied. |
| Suffix | Optionally add a character or string at the end of the merged data. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| - Column A: Table - Column B: Recipe | - Columns to process: A - Prefix: a - Use with: Other column - Column: B - Separator: @ - Add separator: Both values not empty - Suffix: ! | - Column A: aTable@Recipe! - Column B: Recipe |
| - Column A: Qlik - Column B: Cloud - Column C: Analytics | - Columns to process: A, B - Prefix: # - Use with: Other column - Column: C - Separator: + - Add separator: Both values not empty - Suffix: ! | - Column A: #Qlik+Analytics! - Column B: #Cloud+Analytics! - Column C: Analytics |

## Contains text

Checks if the cells contain a specific value. The function will return TRUE if the selected text is found within the cell, otherwise it will return FALSE. This function is case sensitive.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Use with | - Value: Select this option to check the column against a fixed value, set in the Constant value field. - Column: Select this option to check the column against values from another column, set in the Other column drop-down list. |

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| - Table Recipe - Data Flow | - Use with: Value - Constant value: Recipe | - TRUE - FALSE |

## Convert to text

Converts the type of strings contained in the column so that they are interpreted as text in the system.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

## Extract a value by index

Extracts a substring selected using index positions, to a new column.

An index represents a number of characters from which or to which the selection applies. Index 0 corresponds to the first character.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| From | Select how you want to start the value selection:   - From beginning to use the beginning of the string as starting point. - From index to specify the character number at which to start the selection, set in the following Beginning index field. - From N before end to specify how many characters from the end of the string to start the selection, set in the following From N before end field. |
| To | Select how you want to end the value selection:   - To end to use the end of the string as ending point. - To index to specify the character number at which to end the selection, set in the following End index field. - To N before end to specify how many characters from the end of the string to end the selection, set in the following To N before end field. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

## Hash data

Masks the information contained in a column. The input data is replaced using a 256 bit version of the Fowler-Noll-Vo algorithm.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Output |
| --- | --- |
| Table recipe | G=HE!D)EV^\*H2%ZB-.(,I?.4+4J`Q%M]B&G\_L5D0?2- |

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| TableRecipe | - From: From beginning - To: To index - End index: 5 | Table |
| QlikCloudAnalytics | - From: From index - Beginning index: 4 - To: To index - End index: 9 | Cloud |

## Match pattern

Checks if the cell is similar to a specific pattern. The function will return TRUE if the selected pattern is found within the cell, otherwise it will return FALSE.

A new column containing the result of the function will be created for each of the selected column. The default name of the new columns will be <original\_column\_name>\_matches.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Pattern | Select one of the predefined regex patterns, or another combination of operator and value:   - [a-z]+ (a word in lower case) - [A-Z]+ (a word in upper case) - [0-9]+ (number) - [a-zA-Z]+ (a word , case insensitive) - [a-zA-Z0-9]+ (any literal with alpha-numeric characters) - Other |
| Operator | If you have selected Other as Pattern, you can select one of the following operator, and set you custom value in the following Value field:   - Equals - Contains - Starts with - Ends with - Regex |

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| - 992424254-8 - ISBN 2-22605257-7 | - Pattern: Other - Operator: Regex - ^[ISBN]{4}[ ]{0,1}[0-9]{1}[-]{1}[0-9]{3}[-]{1}[0-9]{5}[-]{1}[0-9]{0,1}$ | - FALSE - TRUE |
| - Terminator - Terminator 2 | - Pattern: [a-zA-Z]+ (a word , case insensitive) | - TRUE - FALSE |

## Match similar text

Checks if the cell is similar to a specific value. The function will return TRUE if the selected text is found within the cell, otherwise it will return FALSE.

A new column containing the result of the function will be created for each of the selected column. The default name of the new columns will be <original\_column\_name>\_matches.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Use with | - Value: Select this option to check the column against a fixed value, set in the Reference field. - Other column: Select this option to check the column against values from another column, set in the Column drop-down list. |
| Fuziness | Set a number that corresponds to the Levenshtein distance you want to use for the check. The Levenshtein distance represents the number of edits you need to make in order to transform a string into another. |

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| - Remark - Remodel | - Use with: Value - Reference: Remake - Fuziness: 2 | - TRUE - FALSE |

## Remove non alpha numeric characters

Removes all characters that are not 0-9, Aa-Zz, and accented letter from the content of a cell. The following character, as well as whitespaces, are kept: 1234567890abcdefghijklmnopqrstuvwxyzáàâäãåæçéèêëíìîïñóòôöõøœßúùûüABCDEFGHIJKLMNOPQRSTUVWXYZÁÀÂÄÃÅÆÇÉÈÊËÍÌÎÏÑÓÒÔÖÕØŒSSÚÙÛÜ.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Output |
| --- | --- |
| Q=+L\*\*€IK#$ 12%3,4 | QLIK 1234 |

## Remove non numeric characters

Remove all characters that are not 0-9. Decimal separators and whitespaces are also kept.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Output |
| --- | --- |
| Q=+L\*\*€IK#$12%3,4 | 123,4 |

## Remove part of text

Removes the specified strings from the cells in the column.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Operator | Select the operator that will be used to match the text to remove:   - Equals - Contains - Starts with - Ends with |
| Value | Enter the character or string to remove. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| - New York - New york - Yorkshire | - Operator: Contains - Value:York | - New - New york - shire |

## Remove trailing and leading characters

Removes trailing and leading spaces or other specified characters.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Padding character | - Whitespace: Unnecessary blank spaces at the beginning and end of the cells will be removed. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Output |
| --- | --- |
| [][]TableRecipe[] | TableRecipe |

## Search and replace

Replaces cells or parts of cells which contain a specific value with another one.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Operator | Select the operator that will be used to match the text to search:   - Equals - Contains - Starts with - Ends with - Matches regex - Matches wildcard |
| Value | Enter the character or string to search. |
| Replace | Select the behavior of the replace action:   - Matching text with replace value - Entire cell with replace value - Entire cell with null |
| Replace with | Enter the value with which to replace the specified strings. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

Tip noteAlternatively, you can start a search and replace operation in a column by right-clicking a cell in the table and selecting the Replace this value in this column option. A recipe step then opens where the string to replace is already set. Finish the step configuration and click Apply.

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| - France - Canada - United States of America - United States | - Operator: Contains - Value: America - Replace with: USA - Overwrite entire cell | - France - Canada - USA - United States |

## Split column

Splits the content of a cell in several columns, based on a separator.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Parts | Enter the number of columns you want to create.  If the original string contains more parts than what you have specified in the Parts field, the remaining string will be returned in the last created column. |
| Separator | From the drop-down list, select the character used as basis for the split:   - , - : - ; - . - - - @ - Space - Other (String). When using this option, enter your custom value in the Custom separator field. |

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| Column A: 12/07/1998 | - Parts: 3 - Separator: Other (String) - Custom separator: / | - Column A: 12/07/1998 - Column B: 12 - Column C: 07 - Column D: 1998 |
| Column A: 20-03-2025 | - Parts: 2 - Separator: - | - Column A: 20-03-2025 - Column B: 20 - Column C: 03-2025 |
