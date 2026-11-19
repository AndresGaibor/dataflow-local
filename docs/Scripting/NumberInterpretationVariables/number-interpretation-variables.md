---
title: "Number interpretation variables"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/number-interpretation-variables.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Working with variables in the data load editor"]
---
Expand/Collapse all

# Number interpretation variables

Number interpretation [variables](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/number-interpretation-variables.htm#glossary-0 "Glossary term") are system defined. The variables are included
at the top of the [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/number-interpretation-variables.htm#glossary-1 "Glossary term") and apply number formatting settings at the
time of the script execution. They can be deleted, edited, or duplicated.

Default regional settings in applications are based on a combination of identity provider settings, system settings, or browser settings. These regional format settings are not related to the language displayed in the Qlik Cloud user interface. Qlik Cloud will be displayed in the same language as the browser you are using.

If you are an application creator, you can set the default region for applications you create. For more information, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/UserInterface/Languages.htm#Setting).

## Currency formatting

MoneyDecimalSep

The decimal separator defined replaces the decimal symbol for currency set by your regional settings.

[**MoneyDecimalSep**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/MoneyDecimalSep.htm)

MoneyFormat

The symbol defined replaces the currency symbol set by your regional settings.

[**MoneyFormat**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/MoneyFormat.htm)

MoneyThousandSep

The thousands separator defined replaces the digit grouping symbol for
currency set by your regional settings.

[**MoneyThousandSep**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/MoneyThousandSep.htm)

## Number formatting

DecimalSep

The decimal separator defined replaces the decimal symbol set by your regional settings.

[**DecimalSep**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/DecimalSep.htm)

ThousandSep

The thousands separator defined replaces the digit grouping symbol of the operating
system (regional
settings).

[**ThousandSep**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/ThousandSep.htm)

NumericalAbbreviation

The numerical abbreviation sets which abbreviation to use for scale prefixes of numerals, for example M for mega or a million (106), and µ for micro (10-6).

[**NumericalAbbreviation**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/NumericalAbbreviation.htm)

## Time formatting

DateFormat

This environment variable defines the date format used as the default in the application. The format is used both to interpret and format dates. If the variable is not defined, the date format of the regional settings of the operating system will be fetched when the script runs.

[**DateFormat**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/DateFormat.htm)

TimeFormat

The format defined replaces the time format of the operating
system (regional
settings).

[**TimeFormat**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/TimeFormat.htm)

TimestampFormat

The format defined replaces the date and time formats of the operating
system (regional
settings).

[**TimestampFormat**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/TimestampFormat.htm)

MonthNames

The format defined replaces the month names convention of the regional settings.

[**MonthNames**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/MonthNames.htm)

LongMonthNames

The format defined replaces the long month names convention in the regional settings.

[**LongMonthNames**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/LongMonthNames.htm)

DayNames

The format defined replaces the weekday names convention set by your regional settings.

[**DayNames**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/DayNames.htm)

LongDayNames

The format defined replaces the long weekday names convention in the regional settings.

[**LongDayNames**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/LongDayNames.htm)

FirstWeekDay

Integer that defines which day to use as the first day of the week.

[**FirstWeekDay**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/FirstWeekDay.htm)

BrokenWeeks

This setting defines if weeks are broken or not.

[**BrokenWeeks**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/BrokenWeeks.htm)

ReferenceDay

The setting defines which day in January to set as reference day to define week 1.

[**ReferenceDay**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/ReferenceDay.htm)

FirstMonthOfYear

The setting defines which month to use as first month of the year, which can be used to define financial years that use a monthly offset, for example starting April 1.

> **Note:** This setting is currently unused but reserved for future use.

Valid settings are 1 (January) to 12 (December). Default setting is 1.

Syntax:

FirstMonthOfYear

Example:

Set FirstMonthOfYear=4; //Sets the year to start in April
