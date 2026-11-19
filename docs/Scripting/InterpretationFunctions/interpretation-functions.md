---
title: "Interpretation functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/InterpretationFunctions/interpretation-functions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions"]
---
Expand/Collapse all

# Interpretation functions

The interpretation functions evaluate the contents of input text fields or expressions, and impose a specified data format on the resulting numeric value. With these functions, you can specify the format of the number, in accordance with its data type, including attributes such as: decimal separator,
thousands separator,and date format.

The interpretation functions all return a dual value with both the string and the number value, but can be thought of as performing a string-to-number conversion. The functions take the text value of the input expression and generate a number representing the string.

In contrast, the formatting functions do the opposite: they take numeric expressions and evaluate them as strings, specifying the display format of the resulting text.

If no interpretation functions are used, Qlik Sense interprets the data
as a mix of numbers, dates, times, time stamps and strings, using the
default settings for number format, date format, and time format, defined
by script [variables](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/InterpretationFunctions/interpretation-functions.htm#glossary-0 "Glossary term") and by the operating system.

All interpretation functions can be used in both data load scripts and chart expressions.

> **Note:** All number representations are given with a decimal point as the decimal separator.

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

Date#

Date# evaluates
an expression as a date in the format specified in the second argument, if supplied.
If the format code is omitted, the default date format set in the operating
system is used.

[*Date# Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/InterpretationFunctions/date_hash.htm)(text[, format])

Interval#

Interval#() evaluates
a text expression as a time interval
in the format set in the operating system, by default, or in the format specified in the second argument, if supplied.

[*Interval# Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/InterpretationFunctions/interval_hash.htm)(text[, format])

Money#

Money#() converts a text string to a money value, in the format set in the load script or the operating system, unless a format string is supplied. Custom decimal and thousand separator symbols are optional parameters.

[*Money# Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/InterpretationFunctions/money_hash.htm)(text[, format[, dec\_sep[, thou\_sep ] ] ]**)**

Num#

Num#() interprets a text string as a numerical value, that is it converts the input string to a number using the format specified in the second parameter. If the second parameter is omitted, it uses the decimal and thousand separators set in the data load script. Custom decimal and thousand separator symbols are optional parameters.

[*Num# Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/InterpretationFunctions/num_hash.htm)(text[
, format[, dec\_sep[
, thou\_sep]]]**)**

Text

Text() forces the
expression to be treated as text, even if a numeric interpretation is possible.

[**Text**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/InterpretationFunctions/Text.htm)(expr)

Time#

Time#() evaluates
an expression as a time value, in the time format set in the data load script or the operating system, unless a format string is supplied..

[*Time# Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/InterpretationFunctions/time_hash.htm)(text[, format])

Timestamp#

Timestamp#() evaluates
an expression as a date and
time value, in the timestamp format set in the data load script or the operating system, unless a format string is supplied.

[*Timestamp# Script and chart function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/InterpretationFunctions/timestamp_hash.htm) (text[,
format])

## Learn more

- [*Formatting functions*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FormattingFunctions/formatting-functions.htm)
