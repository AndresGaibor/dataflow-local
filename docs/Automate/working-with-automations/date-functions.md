---
title: "Date functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/working-with-automations/date-functions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Qlik Automate", "Working with automations", "Working with formulas"]
---

# Date functions

This help topic outlines the available date functions in Qlik Automate. Date functions change the date from one format to another, or they return information about a date.

## Date

The date function converts a date from one format to another. It requires a date as input, and the new date format as a parameter. You can use an optional input parameter to specify the format of the input date. The date function also works date strings, like today, now, yesterday or tomorrow.

With a date as input:

`{$.inputs.date}` = June 1, 2021

`{date:{$.inputs.date},'d-m-y'}` = 01-06-21

With a date string as input:

`{$.inputs.date}` = tomorrow

`{date:{$.inputs.date},'d-m-y'}` = 30-07-21

Configuration of the date formula

![Image showing the automation structure and input configuration using the date formula](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/automation-working-with-dates.png)

### Convert to Qlik date format

The date formula converts the date to a Unix format, and then applies division and addition to create the Qlik date format.

`{add: {divide: {date: {$.vDate}, 'U'}, 86400}, 25569}`

## Convert time zone

The convert time zone function converts the date and time from one time zone to another. It requires a data and time as input, and an input and output time zone. Optionally add input and output format to adjust the date format.

To convert a timezone, click Add formula > Date functions > Convert timezone in the input field.

Configuration of the convert time zone function

![Image showing the Select formula dialog to convert a time zone](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/automations-select-convert-timezone_781x828.png)

`{$.inputs.date}` = today 09:24

`{converttimezone: {$.inputs.date}, , 'America/Toronto', , 'Europe/Paris'}` =
2021-07-29 15:24:00

Configuration of the convert time zone function

![Image showing the automation structure and input configuration for convertin timezones](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/automation-convert-timezone.png)

## List time zones

The list time zones function is a function that takes no input. It is used by itself to return a list of available time zones for the convert time zone function.

## Parameters

Use these parameters to specify the input and output format in the date formulas.

Parameters for dates

| Character | Description | Example returned value |
| --- | --- | --- |
| d | Day of the month. Two digits with leading zeros | 01 to 31 |
| D | A textual representation of a day with three letters | Mon through Sun |
| j | Day of the month without leading zeros | 1 to 31 |
| l (lowercase 'L') | A full textual representation of the day of the week | Sunday through Saturday |
| N | ISO-8601 numeric representation of the day of the week | 1 (for Monday) through 7 (for Sunday) |
| S | English ordinal suffix for the day of the month with two characters | st, nd, rd or th. Works well with j |
| w | Numeric representation of the day of the week | 0 (for Sunday) through 6 (for Saturday) |
| z | The day of the year (starting from 0) | 0 through 365 |
| W | ISO-8601 week number of year with weeks starting on Monday | 42 (the 42nd week in the year) |
| F | A full textual representation of a month, such as January or March | January through December |
| m | Numeric representation of a month with leading zeros | 01 through 12 |
| M | A short textual representation of a month with three letters | Jan through Dec |
| n | Numeric representation of a month without leading zeros | 1 through 12 |
| t | Number of days in the given month | 28 through 31 |
| L | Leap year designation | 1 for leap year, otherwise 0 |
| o | ISO-8601 week-numbering year. This has the same value as Y, except that if the ISO week number (W) belongs to the previous or following year, that year is used instead. | 1999 or 2003 |
| Y | A full numeric representation of a year with 4 digits | 1999 or 2003 |
| y | A two-digit representation of a year | 99 or 03 |

Parameters for time

| Character | Description | Example returned value |
| --- | --- | --- |
| a | Lowercase Ante meridiem and Post meridiem | am or pm |
| A | Uppercase Ante meridiem and Post meridiem | AM or PM |
| B | Swatch Internet time | 000 through 999 |
| g | 12-hour format of an hour without leading zeros | 1 through 12 |
| G | 24-hour format of an hour without leading zeros | 0 through 23 |
| h | 12-hour format of an hour with leading zeros | 01 through 12 |
| H | 24-hour format of an hour with leading zeros | 00 through 23 |
| i | Minutes with leading zeros | 00 through 59 |
| s | Seconds with leading zeros | 00 through 59 |
| u | Microseconds | Example: 654321 |
| v | Milliseconds | Example: 654 |
| e | Timezone identifier | Example: UTC, GMT, Atlantic/Azores |
| I (uppercase 'i') | Indicates whether or not the date is in daylight saving time | 1 for Daylight Savings, otherwise 0 |
| O | Difference to Greenwich time (GMT) in hours | Example: +0200 |
| P | Difference to Greenwich time (GMT) with colon between hours and minutes | Example: +02:00 |
| T | Timezone abbreviation | Example: EST, MDT |
| Z | Timezone offset in seconds. The offset for timezones west of UTC is negative, and positive for timezones east of UTC. | -43200 through 50400 |
| c | ISO 8601 date | 2004-02-12T15:19:21+00:00 |
| r | [RFC 2822](http://www.faqs.org/rfcs/rfc2822.html) formatted date | Example: Thu, 21 Dec 2000 16:01:07 +0200 |
| u | Seconds since the Unix Epoch (January 1 1970 00:00:00 GMT) | 1552054674 |

To access the list of parameters when you are working on your automations, click on Show more in the Edit Formula dialog.

Edit formula input

![Edit formula dialog box emphasizing the link to show the parameters that can be used when working with date functions](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Sense_QlikAutomation/img/ui_QAA_edit-formula_489x418.png)
