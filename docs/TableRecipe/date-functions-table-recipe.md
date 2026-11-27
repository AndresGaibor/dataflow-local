---
title: "Dates functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/TableRecipe/date-functions-table-recipe.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Table recipe", "Table recipe functions"]
---

# Dates functions

In the case that your data is not detected as date, you need to first apply the Convert to date function to the column with dates before applying any other date-related function. The format information that you need to fill is just to configure the display text format of the date, not to parse a text not detected as date.

## Add duration

Adds duration to a date, time, or timestamp, in the specified time unit.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Time unit | Select which part of the date, time, or timestamp you want to add time to:   - Year - Month - Week - Day - Hour - Minute - Second - Millisecond - Microsecond |
| Use with | - Value: Select this option to add a fixed value, set in the Value field. - Other column: Select this option to add a value from another column, set in the Column drop-down list. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| 03/03/2023 | - Time unit: Year - Use with: Value - Value: 10 | 03/03/2033 |
| 3/7/2019 2:00:00 PM | - Time unit: Seconds - Use with: Value - Value: 30 | 3/7/2019 2:00:30 PM |

## Calculate date difference

For a given time part unit, calculates the time between the dates in your column and the date of your choice.

The calculation is done by first truncating the dates to the specified date or time part, and then returning the difference between them as an integer.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Time unit | Select the time part to use for the calculation:   - Year - Month - Day - Hour - Minute - Second - Millisecond - Microsecond |
| Until | Select how you want to set the date to target:   - Now, to calculate to difference until the current date and time. - Specific date, to enter the date of your choice, set using the date picker in the This date field. - Other column to use dates from another column, set in the Column drop-down list. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| 06/12/1989 | - Time unit: Day - Until: Specific date - This date: 31/12/2000 | 4044 |
| - Column A: 8/4/2016 - Column B: 8/4/2025 | - Time until: Week - Until: Other column - Column: B | 468 |

## Compare dates

Compares the dates in the column with a specific value, or values from another column. The function will return TRUE if the condition set by the operator is met, otherwise it will return FALSE.

Times can only be compared with times but timestamps and dates can be compared. In this case, a date will be interpreted as a timestamp with time set to 00:00.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Compare mode | Select the operator that will be used to compare the dates.   - Equals - Not equals - After - After or equals - Before - Before or equals |
| Use with | - Value: Select this option to check the column against a fixed value, set with the Value date picker. Select dates in mm/dd/yyyy format.  Information noteIf you previously configured this function with a fixed date in a different format, attempts will be made to parse the input to display it correctly in the new date input. However, if you see an empty input, you may need to reconfigure the Value. - Other column: Select this option to check the column against values from another column, set in the Column drop-down list. |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| - 1969-02-27 - 1989-11-09 | - Compare mode: After - Use with: Value - Value: 01/01/1989 | - FALSE - TRUE |

## Convert to date

Converts the type of data contained in the column so that it is interpreted as dates in the system.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Date format | Select the expected date format for the column.   - Auto, to automatically detect the current format. - Custom, to enter your specific date format, set in the Date pattern field. - YYYY-MM-DD - YYYYMMDD - M/D/YYYY - M/D/YY - MM/DD/YY - MMM D, YYYY - MMMM D, YYYY |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

## Convert to time

Converts the type of data contained in the column so that it is interpreted as time in the system.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Date format | Select the expected time format for the column.   - Auto, to automatically detect the current format. - Custom, to enter your specific time format, set in the Date pattern field. - hh:mm - hh:mm:ss - hh:mm AM/PM - hh:mm:ss AM/PM |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

## Convert to timestamp

Converts the type of data contained in the column so that it is interpreted as timestamp in the system.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Date format | Select the expected timestamp format for the column.   - Auto, to automatically detect the current format. - Custom, to enter your specific timestamp format, set in the Date pattern field. - YYYYMMDD hh:mm - YYYYMMDD hh:mm:ss - YYYYMMDDThh:mm - YYYYMMDDThh:mm:ss - M/D/YYYY hh:mm AM/PM - M/D/YY hh:mm AM/PM - MM/DD/YY hh:mm AM/PM - M/D/YYYY hh:mm:ss AM/PM - M/D/YY hh:mm:ss AM/PM - MM/DD/YY HH:mm:ss AM/PM - MMM D, YYYY hh:mm:ss AM/PM - Weekday, MMMM D, YYYY hh:mm:ss AM/PM |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

## Create date from parts

Creates a new date column by concatenating numeric parts from other columns.

### Properties

| Property | Configuration |
| --- | --- |
| Year | Select the column that contains the information with the year for the date you want to create. |
| Month | Select the column that contains the information with the month for the date you want to create. |
| Day | Select the column that contains the information with the day for the date you want to create. |
| New column name | Enter the name of the column that will be created for the concatenation. If you do not enter a new name, the default column name will be new\_date. |

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| - Column A: 10 - Column B: 2021 - Column C: 12 | - Year: Column B - Month: Column A - Day: Column C | Column D: 10/21/2021 |

## Create time from parts

Creates a new time column by concatenating numeric parts from other columns.

### Properties

| Property | Configuration |
| --- | --- |
| Hour | Select the column that contains the information with the hours for the time you want to create. |
| Minute | Select the column that contains the information with the minutes for the time you want to create. |
| Second | Select the column that contains the information with the seconds for the time you want to create. |
| Millisecond | Select the column that contains the information with the milliseconds for the time you want to create. |
| New column name | Enter the name of the column that will be created for the concatenation. If you do not enter a new name, the default column name will be new\_time. |

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| - Column A: 9 - Column B: 1 - Column C: 30 - Column D: 56 | - Hour: Column A - Minute: Column D - Second: Column C - Millisecond: Column B | Column E: 09:56:30.100 |

## Create timestamp from parts

Creates a new timestamp column by concatenating numeric parts from other columns.

### Properties

| Property | Configuration |
| --- | --- |
| Year | Select the column that contains the information with the year for the timestamp you want to create. |
| Month | Select the column that contains the information with the month for the timestamp you want to create. |
| Day | Select the column that contains the information with the day for the timestamp you want to create. |
| Hour | Select the column that contains the information with the hours for the timestamp you want to create. |
| Minute | Select the column that contains the information with the minutes for the timestamp you want to create. |
| Second | Select the column that contains the information with the seconds for the timestamp you want to create. |
| Millisecond | Select the column that contains the information with the milliseconds for the timestamp you want to create. |
| New column name | Enter the name of the column that will be created for the concatenation. If you do not enter a new name, the default column name will be new\_timestamp. |

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| - Column A: 10 - Column B: 2021 - Column C: 12 - Column D: 9 - Column E: 1 - Column F: 30 - Column G: 56 | - Year: Column B - Month: Column A - Day: Column C - Hour: Column D - Minute: Column G - Second: Column F - Millisecond: Column E | Column H: 10/12/2021 9:56:30 AM |

## Extract date parts

Extracts parts of a date and creates separate columns with the selected date parts.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| - AM/PM - Day - Day name - Day of week - Day of year - Hour (12-hour clock) - Hour (24-hour clock) - Minute - Month - Month name - Quarter of year - Quarter number - Second - Week - Year - Year-Month - Year-Quarter - Year-Week | Select which columns will be created using the toggles. Each selected part will be extracted in a different column. The default column name will be <prefix\_or\_source\_column\_name>\_<date\_part>. |
| Date part prefix | Enter a custom prefix that will be added to the name of each created column. If you do not specify a prefix, the name of the source column with the dates will be used as prefix. |

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| 10/12/2021 9:56:30 AM | - Day name - Day of week - Month name - Quarter of year - Week - Date part prefix: extracted | - extracted\_dayLabel: Thu - extracted\_dayOfWeek: 4 - extracted\_monthLabel: Oct - extracted\_quarterLabel: Q4 - extracted\_weekOfYear: 43 |

## Format date

Changes the date format to use in a date column.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Date format | Select one of the predefined formats from the drop-down list or enter a custom one to apply on the dates:   - Custom, to enter your specific date format, set in the Date pattern field. - YYYY-MM-DD - YYYYMMDD - M/D/YYYY - M/D/YY - MM/DD/YY - MMM D, YYYY - MMMM D, YYYY - YYYYMMDD hh:mm - YYYYMMDD hh:mm:ss - YYYYMMDDThh:mm - YYYYMMDDThh:mm:ss - M/D/YYYY hh:mm AM/PM - M/D/YY hh:mm AM/PM - MM/DD/YY hh:mm AM/PM - M/D/YYYY hh:mm:ss AM/PM - M/D/YY hh:mm:ss AM/PM - MM/DD/YY HH:mm:ss AM/PM - MMM D, YYYY hh:mm:ss AM/PM - Weekday, MMMM D, YYYY hh:mm:ss AM/PM - hh:mm - hh:mm:ss - hh:mm AM/PM - hh:mm:ss AM/PM |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| 12-31-2000 | - Date format: Custom - Date pattern: DD/MM/YYYY | 31/12/2000 |
| 05/04/2017 | Date format: Weekday, MMMM D, YYYY hh:mm:ss AM/PM | Thursday, May 4, 2017 12:00:00 am |

## Truncate date

Removes part of a date. The date or timestamp will be set to the first point of the unit to which you are truncating.

### Properties

| Property | Configuration |
| --- | --- |
| Columns to process | Select the column or columns on which you want to apply the function.  If you want to apply it on more than one column, use the drop-down list to select which columns, and click Apply. |
| Time unit | Select the part of the date after which the value will be truncated. If truncating to Day or higher, the value returned will be a date, otherwise, it will be a timestamp.   - Year - Month - Day - Hour - Minute - Second |
| Create new column | Select this check box if you want to output the result of this function in a new column and keep the original untouched. |

### Example

| Input | Configuration | Output |
| --- | --- | --- |
| 2024-06-22 | Time unit: Year | 2024-01-01 |
| 2024-06-22 11:05 | Time unit: Month | 2024-06-01 |
| 2024-06-22 11:05:35 | Time unit: Second | 2024-06-22 11:05:01 |
