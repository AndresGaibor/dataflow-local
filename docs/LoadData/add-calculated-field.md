---
title: "Using calculated fields"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/add-calculated-field.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and managing data with Data Manager", "Editing a table"]
---

# Using calculated fields

There are many cases where you need to adjust or transform the [field](#glossary-0 "Glossary term") data that is loaded. For example, you may need to concatenate a first name and a last name to a full name, extract part of a product number, convert the data format or multiply two numbers.

You can add calculated fields to manage many cases like this. A calculated field uses an expression to define the result of the field. You can use functions, fields and operators in the expression. You can only refer to fields in the table that you are editing. You can reference another calculated field in your calculated field.

You add and edit calculated fields in the table editor of the data manager.

To learn more about editing tables, see [*Editing a table*](editing-table.htm).

## Adding a calculated field

Do the following:

1. Click Add field and select Calculated field.

   The editor for Add calculated field opens.
2. Type the name of the calculated field in Name.
3. Define the expression of the calculated field in Expression. There are two different ways to do this.

   - Use the ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) (Functions), ![List box](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_field.svg) (Fields) and ![operators](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_operators_outline.svg) (Operations) lists to select and insert items into the expression.

     The item you select is inserted at the cursor position in Expression.
   - Type the expression for the calculated field in Expression.

     As you type, you get assistance with suggested functions and fields, as well as function syntax.

   Example results of the calculated field is displayed in Preview.
4. Click Create to create the calculated field and close the calculated field editor.

## Editing a calculated field

You can change the name or edit the expression of a calculated field.

Do the following:

1. Select Edit from the drop-down menu next to the field name.

   The editor for Update calculated field opens.
2. Edit the name of the calculated field in Name if you want to change it.
3. Edit the expression of the calculated field.
4. Click Update to update the calculated field and close the calculated field editor.

## Which functions can I use in a calculated field expression?

You can use the functions listed here when you create a calculated field expression. This is a subset of the expressions available in the data [load script](#glossary-1 "Glossary term"). The expression cannot result in any [aggregation](#glossary-2 "Glossary term") of data from several records, or use inter-record functions to refer to data in other records.

For more information, see [*Script expressions*](../Scripting/script-expressions.htm).

### String functions that can be used in a calculated field expression

These functions can be used to modify or extract data in text string format.

String functions

| Function | Description |
| --- | --- |
| [**Capitalize**](../Scripting/StringFunctions/Capitalize.htm) | Capitalize() function converts the first character of each word in a text string to uppercase and converts all other characters to lowercase. |
| [**Chr**](../Scripting/StringFunctions/Chr.htm) | Chr() returns the Unicode character corresponding to the input integer, also known as a code point. |
| [**FindOneOf**](../Scripting/StringFunctions/FindOneOf.htm) | FindOneOf() searches a string to find the position of the occurrence of any character from a set of provided characters. The position of the Nth occurrence of any character from the search set is returned where N is the optional third parameter of the function. If no third parameter is supplied, the first occurrence is returned. If no match is found, 0 is returned. |
| [**Index**](../Scripting/StringFunctions/Index.htm) | Index() searches a string to find the starting position of the nth occurrence of a provided substring. An optional third argument provides the value of n, which is 1 if omitted. A negative value searches from the end of the string. The positions in the string are numbered left to right from 1 and up. |
| [**KeepChar**](../Scripting/StringFunctions/KeepChar.htm) | KeepChar() returns a string consisting of any of the characters in the first string that match the characters in the second string. This function is case-sensitive. |
| [**Left**](../Scripting/StringFunctions/Left.htm) | Left() returns a string consisting of the first (leftmost) characters of the input string, where the number of characters is determined by the second argument. |
| [**Len**](../Scripting/StringFunctions/Len.htm) | Len() returns the length of the input string. |
| [**Lower**](../Scripting/StringFunctions/Lower.htm) | Lower() converts all the characters in the input string to lower case. |
| [**LTrim**](../Scripting/StringFunctions/LTrim.htm) | LTrim() returns the input string trimmed of any leading spaces. |
| [**Mid**](../Scripting/StringFunctions/Mid.htm) | Mid() returns the part of the input string starting at the position of the character defined by the second argument, 'start', and returning the number of characters defined by the third argument, 'count'. If 'count' is omitted, the rest of the input string is returned. The first character in the input string is numbered 1. |
| [**Ord**](../Scripting/StringFunctions/Ord.htm) | Ord() returns the numeric (ASCII or Unicode) value of the first character of a string. This function is useful to evaluate or compare strings based on their underlying character codes, for example, when sorting or filtering strings with non-standard characters. |
| [**PurgeChar**](../Scripting/StringFunctions/PurgeChar.htm) | PurgeChar() returns a string consisting of the characters contained in the input string ('text'), excluding any that appear in the second argument ('remove\_chars'). |
| [**Repeat**](../Scripting/StringFunctions/Repeat.htm) | Repeat() forms a string consisting of the input string repeated the number of times defined by the second argument. |
| [**Replace**](../Scripting/StringFunctions/Replace.htm) | Replace() returns a string after replacing all occurrences of a given substring within the input string with another substring. The function is non-recursive and works from left to right. |
| [**Right**](../Scripting/StringFunctions/Right.htm) | Right() returns a string consisting of the last (rightmost) characters of the input string, where the number of characters is determined by the second argument. |
| [**RTrim**](../Scripting/StringFunctions/RTrim.htm) | RTrim() returns the input string trimmed of any trailing spaces. |
| [**SubStringCount**](../Scripting/StringFunctions/SubStringCount.htm) | SubStringCount() returns the number of occurrences of the specified substring in the input string text. If there is no match, 0 is returned. |
| [**TextBetween**](../Scripting/StringFunctions/TextBetween.htm) | TextBetween() returns the text in the input string that occurs between the characters specified as delimiters. |
| [**Trim**](../Scripting/StringFunctions/Trim.htm) | Trim() returns the input string trimmed of any leading and trailing spaces. |
| [**Upper**](../Scripting/StringFunctions/Upper.htm) | Upper() converts all the characters in the input string to upper case for all text characters in the expression. Numbers and symbols are ignored. |

### Date functions that can be used in a calculated field expression

Qlik Sense date and time functions are used to transform and convert date and time values.

Functions are based on a date-time serial number that equals the number of days since December 30, 1899. The integer value represents the day and the fractional value represents the time of the day.

Qlik Sense uses the numerical value of the argument, so a number is valid as a argument also when it is not formatted as a date or a time. If the argument does not correspond to a numerical value, for example, because it is a string, then Qlik Sense attempts to interpret the string according to the date and time environment variables.

If the date format used in the argument does not correspond to the one set in the DateFormat system variable, Qlik Sense will not be able to interpret the date correctly. To resolve this, either change the settings or use an interpretation function.

For more information, see [*DateFormat*](../Scripting/NumberInterpretationVariables/DateFormat.htm).

Date functions

| Function | Description |
| --- | --- |
| [**addmonths**](../Scripting/DateAndTimeFunctions/addmonths.htm) | This function returns the date occurring n months after startdate or, if n is negative, the date occurring n months before startdate. |
| [**addyears**](../Scripting/DateAndTimeFunctions/addyears.htm) | This function returns the date occurring n years after startdate or, if n is negative, the date occurring n years before startdate. |
| [**age**](../Scripting/DateAndTimeFunctions/age.htm) | The age function returns the age at the time of timestamp (in completed years) of somebody born on date\_of\_birth. |
| [**converttolocaltime**](../Scripting/DateAndTimeFunctions/converttolocaltime.htm) | Converts a UTC or GMT timestamp to local time as a dual value. The place can be any of a number of cities, places and time zones around the world. |
| [**day**](../Scripting/DateAndTimeFunctions/day.htm) | This function returns an integer representing the day when the fraction of the expression is interpreted as a date according to the standard number interpretation. |
| [**dayend**](../Scripting/DateAndTimeFunctions/dayend.htm) | This function returns a value corresponding to a timestamp of the final millisecond of the day contained in time. The default output format will be the TimestampFormat set in the script. |
| [**daylightsaving**](../Scripting/DateAndTimeFunctions/daylightsaving.htm) | Converts a UTC or GMT timestamp to local time as a dual value. The place can be any of a number of cities, places and time zones around the world. |
| [**dayname**](../Scripting/DateAndTimeFunctions/dayname.htm) | This function returns a value showing the date with an underlying numeric value corresponding to a timestamp of the first millisecond of the day containing time. |
| [**daynumberofquarter**](../Scripting/DateAndTimeFunctions/daynumberofquarter.htm) | Converts a UTC or GMT timestamp to local time as a dual value. The place can be any of a number of cities, places and time zones around the world. |
| [**daynumberofyear**](../Scripting/DateAndTimeFunctions/daynumberofyear.htm) | This function calculates the day number of the year in which a timestamp falls. The calculation is made from the first millisecond of the first day of the year, but the first month can be offset. |
| [**daystart**](../Scripting/DateAndTimeFunctions/daystart.htm) | This function returns a value corresponding to a timestamp with the first millisecond of the day contained in the time argument. The default output format will be the TimestampFormat set in the script. |
| [**firstworkdate**](../Scripting/DateAndTimeFunctions/firstworkdate.htm) | The firstworkdate function returns the latest starting date to achieve no\_of\_workdays (Monday-Friday) ending no later than end\_date taking into account any optionally listed holidays. end\_date and holiday should be valid dates or timestamps. |
| [**GMT**](../Scripting/DateAndTimeFunctions/GMT.htm) | This function returns the current Greenwich Mean Time, as derived from the regional settings. |
| [**hour**](../Scripting/DateAndTimeFunctions/hour.htm) | This function returns an integer representing the hour when the fraction of the expression is interpreted as a time according to the standard number interpretation. |
| [**inday**](../Scripting/DateAndTimeFunctions/inday.htm) | This function returns True if timestamp lies inside the day containing base\_timestamp. |
| [**indaytotime**](../Scripting/DateAndTimeFunctions/indaytotime.htm) | This function returns True if timestamp lies inside the part of day containing base\_timestamp up until and including the exact millisecond of base\_timestamp. |
| [**inlunarweek**](../Scripting/DateAndTimeFunctions/inlunarweek.htm) | This function determines if timestamp lies inside the lunar week containing base\_date. Lunar weeks in Qlik Sense are defined by counting January 1 as the first day of the week., Apart from the final week of the year, each week will contain exactly seven days. |
| [**inlunarweektodate**](../Scripting/DateAndTimeFunctions/inlunarweektodate.htm) | This function finds if timestamp lies inside the part of the lunar week up to and including the last millisecond of base\_date. Lunar weeks in Qlik Sense are defined by counting January 1 as the first day of the week and, apart from the final week of the year, will contain exactly seven days. |
| [**inmonth**](../Scripting/DateAndTimeFunctions/inmonth.htm) | This function returns True if timestamp lies inside the month containing base\_date. |
| [**inmonths**](../Scripting/DateAndTimeFunctions/inmonths.htm) | This function finds if a timestamp falls within the same month, bi-month, quarter, four-month period, or half-year as a base date. It is also possible to find if the timestamp falls within a previous or following time period. |
| [**inmonthstodate**](../Scripting/DateAndTimeFunctions/inmonthstodate.htm) | This function finds if a timestamp falls within the part a period of the month, bi-month, quarter, four-month period, or half-year up to and including the last millisecond of base\_date. It is also possible to find if the timestamp falls within a previous or following time period. |
| [**inmonthtodate**](../Scripting/DateAndTimeFunctions/inmonthtodate.htm) | Returns True if date lies inside the part of month containing basedate up until and including the last millisecond of basedate. |
| [**inquarter**](../Scripting/DateAndTimeFunctions/inquarter.htm) | This function returns True if timestamp lies inside the quarter containing base\_date. |
| [**inquartertodate**](../Scripting/DateAndTimeFunctions/inquartertodate.htm) | This function returns True if timestamp lies inside the part of the quarter containing base\_date up until and including the last millisecond of base\_date. |
| [**inweek**](../Scripting/DateAndTimeFunctions/inweek.htm) | This function returns True if timestamp lies inside the week containing base\_date. |
| [**inweektodate**](../Scripting/DateAndTimeFunctions/inweektodate.htm) | This function returns True if timestamp lies inside the part of week containing base\_date up until and including the last millisecond of base\_date. |
| [**inyear**](../Scripting/DateAndTimeFunctions/inyear.htm) | This function returns True if timestamp lies inside the year containing base\_date. |
| [**inyeartodate**](../Scripting/DateAndTimeFunctions/inyeartodate.htm) | This function returns True if timestamp lies inside the part of year containing base\_date up until and including the last millisecond of base\_date. |
| [**lastworkdate**](../Scripting/DateAndTimeFunctions/lastworkdate.htm) | The lastworkdate function returns the earliest ending date to achieve no\_of\_workdays (Monday-Friday) if starting at start\_date taking into account any optionally listed holiday. start\_date and holiday should be valid dates or timestamps. |
| [**localtime**](../Scripting/DateAndTimeFunctions/localtime.htm) | This function returns a timestamp of the current time for a specified time zone. |
| [**lunarweekend**](../Scripting/DateAndTimeFunctions/lunarweekend.htm) | This function returns a value corresponding to a timestamp of the last millisecond of the last day of the lunar week containing date. Lunar weeks in Qlik Sense are defined by counting January 1 as the first day of the week and, apart from the final week of the year, will contain exactly seven days. |
| [**lunarweekname**](../Scripting/DateAndTimeFunctions/lunarweekname.htm) | This function returns a display value showing the year and lunar week number corresponding to a timestamp of the first millisecond of the first day of the lunar week containing date. Lunar weeks in Qlik Sense are defined by counting January 1as the first day of the week and, apart from the final week of the year, will contain exactly seven days. |
| [**lunarweekstart**](../Scripting/DateAndTimeFunctions/lunarweekstart.htm) | This function returns a value corresponding to a timestamp of the first millisecond of the first day of the lunar week containing date. Lunar weeks in Qlik Sense are defined by counting January 1 as the first day of the week and, apart from the final week of the year, will contain exactly seven days. |
| [**makedate**](../Scripting/DateAndTimeFunctions/makedate.htm) | This function returns a date calculated from the year YYYY, the month MM and the day DD. |
| [**maketime**](../Scripting/DateAndTimeFunctions/maketime.htm) | This function returns a time calculated from the hour hh, the minute mm, and the second ss. |
| [**makeweekdate**](../Scripting/DateAndTimeFunctions/makeweekdate.htm) | This function returns a date calculated from the year, the week number, and the day of week . |
| [**minute**](../Scripting/DateAndTimeFunctions/minute.htm) | This function returns an integer representing the minute when the fraction of the expression is interpreted as a time according to the standard number interpretation. |
| [**month**](../Scripting/DateAndTimeFunctions/month.htm) | This function returns a dual value: a month name as defined in the environment variable MonthNames and an integer between 1-12. The month is calculated from the date interpretation of the expression, according to the standard number interpretation. For more information, see [*MonthNames*](../Scripting/NumberInterpretationVariables/MonthNames.htm). |
| [**monthend**](../Scripting/DateAndTimeFunctions/monthend.htm) | This function returns a value corresponding to a timestamp of the last millisecond of the last day of the month containing date. The default output format will be the DateFormat set in the script. |
| [**monthname**](../Scripting/DateAndTimeFunctions/monthname.htm) | This function returns a display value showing the month (formatted according to the MonthNames script variable) and year with an underlying numeric value corresponding to a timestamp of the first millisecond of the first day of the month. For more information, see [*MonthNames*](../Scripting/NumberInterpretationVariables/MonthNames.htm). |
| [**monthsend**](../Scripting/DateAndTimeFunctions/monthsend.htm) | This function returns a value corresponding to a timestamp of the last millisecond of the month, bi-month, quarter, four-month period, or half-year containing a base date. It is also possible to find the timestamp for a previous or following time period. |
| [**monthsname**](../Scripting/DateAndTimeFunctions/monthsname.htm) | This function returns a display value representing the range of the months of the period (formatted according to the MonthNames script variable) as well as the year. The underlying numeric value corresponds to a timestamp of the first millisecond of the month, bi-month, quarter, four-month period, or half-year containing a base date. |
| [**monthsstart**](../Scripting/DateAndTimeFunctions/monthsstart.htm) | This function returns a value corresponding to the timestamp of the first millisecond of the month, bi-month, quarter, four-month period, or half-year containing a base date. It is also possible to find the timestamp for a previous or following time period.The default output format is the DateFormat set in the script. |
| [**monthstart**](../Scripting/DateAndTimeFunctions/monthstart.htm) | This function returns a value corresponding to a timestamp of the first millisecond of the first day of the month containing date. The default output format will be the DateFormat set in the script. |
| [**networkdays**](../Scripting/DateAndTimeFunctions/networkdays.htm) | The networkdays function returns the number of working days (Monday-Friday) between and including start\_date and end\_date taking into account any optionally listed holiday. |
| [**now**](../Scripting/DateAndTimeFunctions/now.htm) | In Qlik Cloud, this function returns a timestamp in UTC format. The function returns values in the TimeStamp system variable format. The default timer\_mode value is 1.In Qlik Sense Client-Managed, this function returns a timestamp of the current time. The function returns values in the TimeStamp system variable format. The default timer\_mode value is 1. |
| [**quarterend**](../Scripting/DateAndTimeFunctions/quarterend.htm) | This function returns a value corresponding to a timestamp of the last millisecond of the quarter containing date. The default output format will be the DateFormat set in the script. |
| [**quartername**](../Scripting/DateAndTimeFunctions/quartername.htm) | This function returns a display value showing the months of the quarter (formatted according to the MonthNames script variable) and year with an underlying numeric value corresponding to a timestamp of the first millisecond of the first day of the quarter. |
| [**quarterstart**](../Scripting/DateAndTimeFunctions/quarterstart.htm) | This function returns a value corresponding to a timestamp of the first millisecond of the quarter containing date. The default output format will be the DateFormat set in the script. |
| [**second**](../Scripting/DateAndTimeFunctions/second.htm) | This function returns an integer representing the second when the fraction of the expression is interpreted as a time according to the standard number interpretation. |
| [**timezone**](../Scripting/DateAndTimeFunctions/timezone.htm) | In Qlik Cloud, this function returns the time zone name representation of UTC.In Qlik Sense Client-Managed, this function returns the time zone, as defined on the computer where the Qlik engine is running. |
| [**today**](../Scripting/DateAndTimeFunctions/today.htm) | This function returns the current date, evaluated as per UTC time. The function returns values in the DateFormat system variable format.This function returns the current date. The function returns values in the DateFormat system variable format. |
| [**UTC**](../Scripting/DateAndTimeFunctions/UTC.htm) | Returns the current Coordinated Universal Time. |
| [**week**](../Scripting/DateAndTimeFunctions/week.htm) | This function returns an integer representing the week number according to ISO 8601. The week number is calculated from the date interpretation of the expression, according to the standard number interpretation. |
| [**weekday**](../Scripting/DateAndTimeFunctions/weekday.htm) | This function returns a dual value with: A day name as defined in the environment variable DayNames. An integer between 0-6 corresponding to the nominal day of the week (0-6). |
| [**weekend**](../Scripting/DateAndTimeFunctions/weekend.htm) | This function returns a value corresponding to a timestamp of the last millisecond of the last day of the calendar week containing date. The default output format will be the DateFormat set in the script. |
| [**weekname**](../Scripting/DateAndTimeFunctions/weekname.htm) | This function returns a value showing the year and week number with an underlying numeric value corresponding to a timestamp of the first millisecond of the first day of the week containing date. |
| [**weekstart**](../Scripting/DateAndTimeFunctions/weekstart.htm) | This function returns a value corresponding to a timestamp of the first millisecond of the first day of the calendar week containing date. The default output format is the DateFormat set in the script. |
| [**weekyear**](../Scripting/DateAndTimeFunctions/weekyear.htm) | This function returns the year to which the week number belongs according to the environment variables. The week number ranges between 1 and approximately 52. |
| [**year**](../Scripting/DateAndTimeFunctions/year.htm) | This function returns an integer representing the year when the expression is interpreted as a date according to the standard number interpretation. |
| [**yearend**](../Scripting/DateAndTimeFunctions/yearend.htm) | This function returns a value corresponding to a timestamp of the last millisecond of the last day of the year containing date. The default output format will be the DateFormat set in the script. |
| [**yearname**](../Scripting/DateAndTimeFunctions/yearname.htm) | This function returns a four-digit year as display value with an underlying numeric value corresponding to a timestamp of the first millisecond of the first day of the year containing date. |
| [**yearstart**](../Scripting/DateAndTimeFunctions/yearstart.htm) | This function returns a timestamp corresponding to the start of the first day of the year containing date. The default output format will be the DateFormat set in the script. |
| [**yeartodate**](../Scripting/DateAndTimeFunctions/yeartodate.htm) | This function finds if the input timestamp falls within the year of the date the script was last loaded, and returns True if it does, False if it does not. The year of the date the script was last loaded is evaluated as per UTC time.This function finds if the input timestamp falls within the year of the date the script was last loaded, and returns True if it does, False if it does not. |

### Formatting and interpretation functions that can be used in a calculated field expression

The formatting functions use the numeric value of the input expression, and convert this to a text value. In contrast, the interpretation functions do the opposite: they take string expressions and evaluate them as numbers, specifying the format of the resulting number. In both cases the output value is dual, with a text value and a numeric value.

For example, consider the differences in output between the Date and the Date# functions.

Date and the Date# functions

| Function | Output (text) | Output (numeric) |
| --- | --- | --- |
| Date#('20140831', 'YYYYMMDD') | 20140831 | 41882 |
| Date(41882, 'YYYY.MM.DD') | 2014.08.31 | 41882 |

These functions are useful when your data contains date fields that are not interpreted as dates as the format does not correspond to the date format setting in Qlik Sense. In this case, it can be useful to nest the functions:

Date(Date#(DateInput, 'YYYYMMDD'),'YYYY.MM.DD')

This will interpret the DateInput field according to the input format, YYYYMMDD, and return it in the format you want to use, YYYY.MM.DD.

Formatting and interpretation functions

| Function | Description |
| --- | --- |
| [**Date**](../Scripting/FormattingFunctions/Date.htm) | Date() formats an expression as a date using the format set in the system variables in the data load script, or the operating system, or a format string, if supplied. |
| [**date\_hash**](../Scripting/InterpretationFunctions/date_hash.htm) | Date# evaluates an expression as a date in the format specified in the second argument, if supplied. |
| [**Dual**](../Scripting/FormattingFunctions/Dual.htm) | Dual() combines a number and a string into a single record, such that the number representation of the record can be used for sorting and calculation purposes, while the string value can be used for display purposes. |
| [**Interval**](../Scripting/FormattingFunctions/Interval.htm) | Interval() formats a number as a time interval using the format in the system variables in the data load script, or the operating system, or a format string, if supplied. |
| [**interval\_hash**](../Scripting/InterpretationFunctions/interval_hash.htm) | Interval#() evaluates a text expression as a time interval in the format set in the operating system, by default, or in the format specified in the second argument, if supplied. |
| [**Money**](../Scripting/FormattingFunctions/Money.htm) | Money() formats an expression numerically as a money value, in the format set in the system variables set in the data load script, or in the operating system, unless a format string is supplied, and optional decimal and thousands separators. |
| [**money\_hash**](../Scripting/InterpretationFunctions/money_hash.htm) | Money#() converts a text string to a money value, in the format set in the load script or the operating system, unless a format string is supplied. Custom decimal and thousand separator symbols are optional parameters. |
| [**Num**](../Scripting/FormattingFunctions/Num.htm) | Num() formats a number, that is it converts the numeric value of the input to display text using the format specified in the second parameter. If the second parameter is omitted, it uses the decimal and thousand separators set in the data load script. Custom decimal and thousand separator symbols are optional parameters. |
| [**num\_hash**](../Scripting/InterpretationFunctions/num_hash.htm) | Num#() interprets a text string as a numerical value, that is it converts the input string to a number using the format specified in the second parameter. If the second parameter is omitted, it uses the decimal and thousand separators set in the data load script. Custom decimal and thousand separator symbols are optional parameters. |
| [**Text**](../Scripting/InterpretationFunctions/Text.htm) | Text() forces the expression to be treated as text, even if a numeric interpretation is possible. |
| [**Time**](../Scripting/FormattingFunctions/Time.htm) | Time() formats an expression as a time value, in the time format set in the system variables in the data load script, or in the operating system, unless a format string is supplied. |
| [**time\_hash**](../Scripting/InterpretationFunctions/time_hash.htm) | Time#() evaluates an expression as a time value, in the time format set in the data load script or the operating system, unless a format string is supplied. |
| [**Timestamp**](../Scripting/FormattingFunctions/Timestamp.htm) | TimeStamp() formats an expression as a date and time value, in the timestamp format set in the system variables in the data load script, or in the operating system, unless a format string is supplied. |
| [**timestamp\_hash**](../Scripting/InterpretationFunctions/timestamp_hash.htm) | Timestamp#() evaluates an expression as a date and time value, in the timestamp format set in the data load script or the operating system, unless a format string is supplied. |

### Numeric functions that can be used in a calculated field expression

You can use these functions to round numeric values.

Numeric functions

| Function | Description |
| --- | --- |
| [**ceil**](../ChartFunctions/GeneralNumericFunctions/ceil.htm) | Ceil() rounds up a number to the nearest multiple of the step shifted by the offset number. |
| [**div**](../ChartFunctions/GeneralNumericFunctions/div.htm) | Div() returns the integer part of the arithmetic division of the first argument by the second argument. Both parameters are interpreted as real numbers, that is, they do not have to be integers. |
| [**even**](../ChartFunctions/GeneralNumericFunctions/even.htm) | Even() returns True (-1), if integer\_number is an even integer or zero. It returns False (0), if integer\_number is an odd integer, and NULL if integer\_number is not an integer. |
| [**fabs**](../ChartFunctions/GeneralNumericFunctions/fabs.htm) | Fabs() returns the absolute value of x. The result is a positive number. |
| [**fact**](../ChartFunctions/GeneralNumericFunctions/fact.htm) | Fact() returns the factorial of a positive integer x. |
| [**floor**](../ChartFunctions/GeneralNumericFunctions/floor.htm) | Floor() rounds down a number to the nearest multiple of the step shifted by the offset number. |
| [**fmod**](../ChartFunctions/GeneralNumericFunctions/fmod.htm) | fmod() is a generalized modulo function that returns the remainder part of the integer division of the first argument (the dividend) by the second argument (the divisor). The result is a real number. Both arguments are interpreted as real numbers, that is, they do not have to be integers. |
| [**frac**](../ChartFunctions/GeneralNumericFunctions/frac.htm) | Frac() returns the fraction part of x. |
| [**mod**](../ChartFunctions/GeneralNumericFunctions/mod.htm) | Mod() is a mathematical modulo function that returns the non-negative remainder of an integer division. The first argument is the dividend, the second argument is the divisor, Both arguments must be integer values. |
| [**odd**](../ChartFunctions/GeneralNumericFunctions/odd.htm) | Odd() returns True (-1), if integer\_number is an odd integer or zero. It returns False (0), if integer\_number is an even integer, and NULL if integer\_number is not an integer. |
| [**round**](../ChartFunctions/GeneralNumericFunctions/round.htm) | Round() returns the result of rounding a number up or down to the nearest multiple of step shifted by the offset number. |
| [**sign**](../ChartFunctions/GeneralNumericFunctions/sign.htm) | Sign() returns 1, 0 or -1 depending on whether x is a positive number, 0, or a negative number. |

### Conditional functions that can be used in a calculated field expression

You can use these functions to evaluate a condition and then return different answers depending on the condition value.

Conditional functions

| Function | Description |
| --- | --- |
| [**alt**](../Scripting/ConditionalFunctions/alt.htm) | The alt function returns the first of the parameters that has a valid number representation. If no such match is found, the last parameter will be returned. Any number of parameters can be used. |
| [**class**](../Scripting/ConditionalFunctions/class.htm) | The class function assigns the first parameter to a class interval. The result is a dual value with a<=x<b as the textual value, where a and b are the upper and lower limits of the bin, and the lower bound as numeric value. |
| [**if**](../Scripting/ConditionalFunctions/if.htm) | The if function returns a value depending on whether the condition provided with the function evaluates as True or False. |
| [**match**](../Scripting/ConditionalFunctions/match.htm) | The match function compares the first parameter with all the following ones and returns the numeric location of the expressions that match. The comparison is case sensitive. |
| [**mixmatch**](../Scripting/ConditionalFunctions/mixmatch.htm) | The mixmatch function compares the first parameter with all the following ones and returns the numeric location of the expressions that match. The comparison is case insensitive and insensitive to the Japanese Hiragana and Katakana character systems. |
| [**pick**](../Scripting/ConditionalFunctions/pick.htm) | The pick function returns the n:th expression in the list. |
| [**wildmatch**](../Scripting/ConditionalFunctions/wildmatch.htm) | The wildmatch function compares the first parameter with all the following ones and returns the number of the expression that matches. It permits the use of wildcard characters ( \* and ?) in the comparison strings.  \* matches any sequence of characters. ? matches any single character. The comparison is case insensitive and insensitive to the Japanese Hiragana and Katakana character systems. |

### NULL functions that can used in a calculated field expression

You can used these functions to return or detect null values.

NULL functions

| Function | Description |
| --- | --- |
| [**Null**](../Scripting/NULLFunctions/Null.htm) | The Null function returns a null value. |
| [**IsNull**](../Scripting/NULLFunctions/IsNull.htm) | The IsNull function tests if the value of an expression is NULL and if so, returns -1 (True), otherwise 0 (False). |

### Mathematical functions that can used in a calculated field expression

You can use these functions for mathematical calculations.

Mathematical functions

| Function | Description |
| --- | --- |
| [e](../Scripting/MathConstantsAndParamFreeFunctions/mathematical-functions.htm#e) | The function returns the base of the natural logarithms, e ( 2.71828...). |
| [rand](../Scripting/MathConstantsAndParamFreeFunctions/mathematical-functions.htm#rand) | The function returns a random number between 0 and 1. This can be used to create sample data. |

### Exponential and Logarithmic functions that can used in a calculated field expression

You can use these functions for exponential and logarithmic calculations.

Exponential and Logarithmic functions

| Function | Description |
| --- | --- |
| [*exp*](../Scripting/ExponentialAndLogarithmicFunctions/exponential-logarithmic-functions.htm#exp) | The natural exponential function, e^x, using the natural logarithm e as base. The result is a positive number. |
| [*log*](../Scripting/ExponentialAndLogarithmicFunctions/exponential-logarithmic-functions.htm#log) | The natural logarithm of x. The function is only defined if x> 0. The result is a number. |
| [*log10*](../Scripting/ExponentialAndLogarithmicFunctions/exponential-logarithmic-functions.htm#log10) | The common logarithm (base 10) of x. The function is only defined if x> 0. The result is a number. |
| [*pow*](../Scripting/ExponentialAndLogarithmicFunctions/exponential-logarithmic-functions.htm#pow) | Returns x to the power of y. The result is a number. |
| [*sqr*](../Scripting/ExponentialAndLogarithmicFunctions/exponential-logarithmic-functions.htm#sqr) | x squared (x to the power of 2). The result is a number. |
| [*sqrt*](../Scripting/ExponentialAndLogarithmicFunctions/exponential-logarithmic-functions.htm#sqrt) | Square root of x. The function is only defined if x >= 0. The result is a positive number. |

### Distribution functions that can used in a calculated field expression

You can use these functions for statistical distribution calculations.

Distribution functions

| Function | Description |
| --- | --- |
| [**ChiDist**](../Scripting/StatisticalDistributionFunctions/ChiDist.htm) | ChiDist() returns the one-tailed probability of the chi2 distribution. The chi2 distribution is associated with a chi2 test. |
| [**ChiInv**](../Scripting/StatisticalDistributionFunctions/ChiInv.htm) | ChiInv() returns the inverse of the one-tailed probability of the chi2 distribution. |
| [**FDist**](../Scripting/StatisticalDistributionFunctions/FDist.htm) | FDist() returns the accumulated probability of the F distribution. |
| [**FInv**](../Scripting/StatisticalDistributionFunctions/FInv.htm) | FInv() returns the inverse of the accumulated probability of the F distribution. |
| [**NormDist**](../Scripting/StatisticalDistributionFunctions/NormDist.htm) | NormDist() returns the cumulative normal distribution for the specified mean and standard deviation. If mean = 0 and standard\_dev = 1, the function returns the standard normal distribution. |
| [**NormInv**](../Scripting/StatisticalDistributionFunctions/NormInv.htm) | NormInv() returns the inverse of the normal cumulative distribution for the specified mean and standard deviation. |
| [**TDist**](../Scripting/StatisticalDistributionFunctions/TDist.htm) | TDist() returns the probability for the student's t distribution where a numeric value is a calculated value of t for which the probability is to be computed. |
| [**TInv**](../Scripting/StatisticalDistributionFunctions/TInv.htm) | TInv() returns the t value of the student's t distribution as a function of the probability and the degrees of freedom. |

### Geospatial functions that can used in a calculated field expression

You can use this function to handle geospatial data.

Geospatial functions

| Function | Description |
| --- | --- |
| [**GeoMakePoint**](../Scripting/GeospatialFunctions/GeoMakePoint.htm) | GeoMakePoint() is used in scripts and chart expressions to create and tag a point with latitude and longitude. |

### Color functions that can used in a calculated field expression

You can use these functions for setting and evaluating color [properties](#glossary-3 "Glossary term").

Color functions

| Function | Description |
| --- | --- |
| [**ARGB**](../ChartFunctions/ColorFunctions/ARGB.htm) | ARGB() is used in expressions to set or evaluate the color properties of a chart object, where the color is defined by a red component r, a green component g, and a blue component b, with an alpha factor (opacity) of alpha. |
| [**HSL**](../ChartFunctions/ColorFunctions/HSL.htm) | HSL() is used in expressions to set or evaluate the color properties of a chart object, where the color is defined by values of hue, saturation, and luminosity between 0 and 1. |
| [**RGB**](../ChartFunctions/ColorFunctions/RGB.htm) | RGB() returns an integer corresponding to the color code of the color defined by the three parameters: the red component r, the green component g, and the blue component b. These components must have integer values between 0 and 255. The function can be used in expressions to set or evaluate the color properties of a chart object. |

### Logical functions that can used in a calculated field expression

You can use these functions for handling logical operations.

Logical functions

| Function | Description |
| --- | --- |
| [IsNum](../Scripting/LogicalFunctions/logical-functions.htm#IsNum) | Returns -1 (True) if the expression can be interpreted as a number, otherwise 0 (False). |
| [IsText](../Scripting/LogicalFunctions/logical-functions.htm#IsText) | Returns -1 (True) if the expression has a text representation, otherwise 0 (False). |

### System functions that can be used in a calculated field expression

You can use these functions for accerssing system ,device, and Qlik Sense application properties.

System functions

| Function | Description |
| --- | --- |
| [**system-functions**](../Scripting/SystemFunctions/system-functions.htm#OSuser) | This function returns a string containing the name of the user that is currently connected. It can be used in both the data load script and in a chart expression. |
| [ReloadTime](../Scripting/SystemFunctions/system-functions.htm#ReloadTime) | This function returns a timestamp for when the last data load finished. It can be used in both the data load script and in a chart expression. |

Related learning:

- [Data manager calculations and transformations](/lnk/Data_Manager_Calculations_Transformations_QS)
- [How do I create calculated fields?](/lnk/How_create_calculated_fields)
