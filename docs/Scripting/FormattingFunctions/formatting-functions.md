---
title: "Formatting functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FormattingFunctions/formatting-functions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions"]
---
Expand/Collapse all

# Formatting functions

The formatting functions impose the display format on the input numeric fields or expressions. Depending on data type, you can specify the characters for the decimal separator, thousands
separator, and so on.

The functions all return a dual value with both the string and the number value, but can be thought of as performing a number-to-string conversion. Dual() is a special case, but the other formatting functions take the numeric value of the input expression and generate a string representing the number.

In contrast, the interpretation functions do the opposite: they take string expressions and evaluate them as numbers, specifying the format of the resulting number.

The functions can be used both in data load scripts and chart expressions.

> **Note:** All number representations are given with a decimal point as the decimal separator.

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

ApplyCodepage

ApplyCodepage() applies a different code page character set to the field
or text stated in the expression. The codepage argument must be in number format.

[**ApplyCodePage**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FormattingFunctions/ApplyCodePage.htm) (text,
codepage)

Date

Date() formats an
expression as a date using the format set in the system variables in the data load script, or the operating system, or a format string, if supplied.

[**Date**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FormattingFunctions/Date.htm)(number[, format])

Dual

Dual() combines a number and a string into a single record, such that the number representation of the record can be used for sorting and calculation purposes, while the string value can be used for display purposes.

[**Dual**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FormattingFunctions/Dual.htm)(text, number)

Interval

Interval() formats
a number as a time interval
using the format in the system variables in the data load script, or the operating system, or a format string, if supplied.

[**Interval**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FormattingFunctions/Interval.htm)(number[, format])

Money

Money() formats an
expression numerically as a money value, in the format set in the system variables set in the data load script, or in the operating system, unless a format string is supplied, and optional decimal and thousands separators.

[**Money**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FormattingFunctions/Money.htm)(number[, format[, dec\_sep
[, thou\_sep]]])

Num

Num() formats a number, that is it converts the numeric value of the input to display text using the format specified in the second parameter. If the second parameter is omitted, it uses the decimal and thousand separators set in the data load script. Custom decimal and thousand separator symbols are optional parameters.

[**Num**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FormattingFunctions/Num.htm)(number[, format[, dec\_sep
[, thou\_sep]]])

Time

Time() formats an expression as a time value, in the time format set
in the system variables in the data load script, or in the operating system, unless a format string is supplied.

[**Time**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FormattingFunctions/Time.htm)(number[, format])

Timestamp

TimeStamp() formats
an expression as a date and
time value, in the timestamp format set in the system variables in the data load script, or in the operating
system, unless a format string is supplied.

[**Timestamp**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/FormattingFunctions/Timestamp.htm)(number[,
format])

## Learn more

- [*Interpretation functions*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/InterpretationFunctions/interpretation-functions.htm)
