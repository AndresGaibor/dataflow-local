---
title: "Modifying regional settings for applications and scripts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/regional-settings-in-apps.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with applications"]
---

# Modifying regional settings for applications and scripts

By default, applications and scripts you create will use the regional settings you specify in your profile in Settings and Management. You can edit or change these in the [load script](#glossary-0 "Glossary term") of your application or script.

All new applications and scripts have section in the load script called Main. Main contains SET functions with variables for the regional settings. These set the formats for money, dates, and decimals, as well as the localization names of days and months based on the regional settings set in your profile. For information on setting regional preferences, see [*Setting your preferred regional settings for creating apps and scripts in Qlik Cloud Analytics*](../UserInterface/Languages.htm#Setting).

Main, with regional settings [variables](#glossary-2 "Glossary term")

![The automatically generated Main section of Data load editor, with regional settings](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_main-regional-settings.png "Click to view full size")

You can modify the [variable](#glossary-3 "Glossary term") values in Data load editor to change regional settings.

The following number formatting variables are available

- ThousandSep: This defines the separator used to mark thousands. For more information, see [*ThousandSep*](../Scripting/NumberInterpretationVariables/ThousandSep.htm).
- DecimalSep: This defines the punctuation used to mark decimals. For more information, see [*DecimalSep*](../Scripting/NumberInterpretationVariables/DecimalSep.htm).
- NumericalAbbreviation: This defines numerical abbreviations for large and small numbers. For more information, see [*NumericalAbbreviation*](../Scripting/NumberInterpretationVariables/NumericalAbbreviation.htm).

The following currency formatting variables are available:

- MoneyThousandSep : This defines the separator used for thousands. For more information, see [*MoneyThousandSep*](../Scripting/NumberInterpretationVariables/MoneyThousandSep.htm).
- MoneyDecimalSep ; This defines the punctuation used to mark decimals in currency. For more information, see [*MoneyDecimalSep*](../Scripting/NumberInterpretationVariables/MoneyDecimalSep.htm).
- MoneyFormat: this defines the currency symbol and format. For more information, see [*MoneyFormat*](../Scripting/NumberInterpretationVariables/MoneyFormat.htm).

The following time formatting variables are available:

- TimeFormat: This defines the time format for the application. For more information, see [*TimeFormat*](../Scripting/NumberInterpretationVariables/TimeFormat.htm).
- DateFormat: This defines the date format for the application. For more information, see [*DateFormat*](../Scripting/NumberInterpretationVariables/DateFormat.htm).
- TimestampFormat: This defines the data and time format for timestamps in the application. For more information, see [*TimestampFormat*](../Scripting/NumberInterpretationVariables/TimestampFormat.htm).
- FirstWeekDay: This defines which day should be defined as the first day of the week. For more information, see [*FirstWeekDay*](../Scripting/NumberInterpretationVariables/FirstWeekDay.htm).
- BrokenWeeks: This defines if weeks are broken over years or not. For more information, see [*BrokenWeeks*](../Scripting/NumberInterpretationVariables/BrokenWeeks.htm).
- ReferenceDay: This defines which day in January to set as a reference day to define week 1 of the year. For more information, see [*ReferenceDay*](../Scripting/NumberInterpretationVariables/ReferenceDay.htm).
- FirstMonthOfYear: This defines which month to use as the first month of the year. For more information, see [*FirstMonthOfYear*](../Scripting/NumberInterpretationVariables/number-interpretation-variables.htm#FirstMon).
- MonthNames: This defines the short forms of month names used in the application. For more information, see [*MonthNames*](../Scripting/NumberInterpretationVariables/MonthNames.htm).
- LongMonthNames: This defines the long form of month names used in the application. For more information, see [*LongMonthNames*](../Scripting/NumberInterpretationVariables/LongMonthNames.htm).
- DayNames: This defines the short form of day names used in the application. For more information, see [*DayNames*](../Scripting/NumberInterpretationVariables/DayNames.htm) .
- LongDayNames: This defines the long form of day names used in the application. For more information, see [*LongDayNames*](../Scripting/NumberInterpretationVariables/LongDayNames.htm) .

The following variable is available for sort order and search matching:

- CollationLocale: Specifies which locale to use for sort order and search matching. The value is the culture name of a locale, for example 'en-US'.
