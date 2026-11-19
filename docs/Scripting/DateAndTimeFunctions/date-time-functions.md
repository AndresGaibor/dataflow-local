---
title: "Date and time functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/date-time-functions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions"]
---
Expand/Collapse all

# Date and time functions

Qlik Sense date and time functions are used to transform and convert date and time values. All functions can be used in both the data [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/date-time-functions.htm#glossary-0 "Glossary term") and in chart expressions.

Functions are based on a date-time serial number that equals the number of days since December 30, 1899. The integer value represents the day and the fractional value represents the time of the day.

Qlik Sense uses the numerical value of the parameter, so a number is valid as a parameter also when it is not formatted as a date or a time. If the parameter does not correspond to numerical value, for example, because it is a string, then Qlik Sense attempts to interpret the string according to the date and time environment [variables](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/date-time-functions.htm#glossary-1 "Glossary term").

If the time format used in the parameter does not correspond to the one set in the environment variables, Qlik Sense will not be able to make a correct interpretation. To resolve this, either change the settings or use an interpretation function.

In the examples for each function, the default time and date formats hh:mm:ss and
YYYY-MM-DD (ISO 8601) are assumed.

> **Note:** When processing a timestamp with a date or time function, Qlik Sense ignores any daylight savings time parameters unless the date or time function includes a geographical position.
>
> For example, `ConvertToLocalTime( filetime('Time.qvd'), 'Paris')` would use daylight savings time parameters while `ConvertToLocalTime(filetime('Time.qvd'), 'GMT-01:00')` would not use daylight savings time parameters.

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

### Integer expressions of time

second

This function returns an integer representing the second when the fraction
of the expression is interpreted as a time
according to the standard number interpretation.

[**second**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/second.htm)(expression)

minute

This function returns an integer representing the minute when the fraction
of the expression is interpreted as a time
according to the standard number interpretation.

[**minute**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/minute.htm)(expression)

hour

This function returns an integer representing the hour when the fraction of the
expression is interpreted as a time
according to the standard number interpretation.

[**hour**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/hour.htm)(expression)

day

This function returns an integer
representing the day when the fraction of the expression
is interpreted as a date according to the standard number interpretation.

[**day**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/day.htm)(expression)

week

This function returns an integer representing the week number according to ISO 8601. The week number is calculated from the date interpretation of the expression, according to the standard number interpretation.

[**week**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/week.htm)(expression)

month

This function returns a dual value: a month name as defined in the environment variable MonthNames and an integer between 1-12. The month is calculated from the date interpretation of the expression, according to the standard number interpretation.

[**month**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/month.htm)(expression)

quarter

The quarter function returns an integer representing the quarter of the provided date. The returned value is between 1 and 4. The function can be used in both load scripts and chart expressions.

[**quarter**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/quarter.htm)(date [,

first\_month\_of\_year]

)

year

This function returns an integer representing the year when the
expression is interpreted as a date
according to the standard number interpretation.

[**year**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/year.htm)(expression)

weekyear

This function returns the year to which the week number belongs according to the environment variables. The week number ranges between
1 and approximately 52.

[**weekyear**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/weekyear.htm)(expression)

weekday

This function returns a dual value with:

- A day name as defined in the environment variable DayNames.
- An integer between 0-6 corresponding to the nominal day of the week (0-6).

[**weekday**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/weekday.htm)(date)

### Timestamp functions

now

In Qlik Cloud, this function returns a timestamp in UTC format. The function returns values in the TimeStamp system variable format. The default timer\_mode value is 1.

[**now**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/now.htm)([
timer\_mode])

today

This function returns the current date, evaluated as per UTC time. The function returns values in the `DateFormat` system variable format.

[**today**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/today.htm)([timer\_mode])

LocalTime

This function returns a timestamp of the
current time for a specified time zone.

[**localtime**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/localtime.htm)([timezone [, ignoreDST ]])

### Make functions

makedate

This function returns a date calculated from the year YYYY, the month MM and the day DD.

[**makedate**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/makedate.htm)(YYYY [ , MM [ , DD ] ])

makeweekdate

This function returns a date calculated from the year, the week number, and the day of week .

[**makeweekdate**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/makeweekdate.htm)(YYYY [ , WW [ , D ] ])

maketime

This function returns a time calculated from the hour hh, the minute mm, and the second ss.

[**maketime**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/maketime.htm)(hh [ , mm [ , ss [ .fff ] ] ])

### Other date functions

AddMonths

This function returns the date occurring n months after startdate or, if
n is negative, the date occurring
n months before startdate.

[**addmonths**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/addmonths.htm)(startdate, n
, [ , mode])

AddYears

This function returns the date occurring n years after startdate or, if
n is negative, the date occurring
n years before startdate.

[**addyears**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/addyears.htm)(startdate, n)

yeartodate

This function finds if the input timestamp falls within the year of the date the script was last loaded, and returns True if it does, False if it does not. The year of the date the script was last loaded is evaluated as per UTC time.

[**yeartodate**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/yeartodate.htm)(date [ , yearoffset
[ , firstmonth [ , todaydate] ] ])

### Timezone functions

timezone

In Qlik Cloud, this function returns the time zone name representation of UTC.

[**timezone**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/timezone.htm)( )

GMT

This function returns the current Greenwich
Mean Time, as derived from the regional settings.

[**GMT**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/GMT.htm)( )

UTC

Returns the current Coordinated
Universal Time.

[**UTC**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/UTC.htm)( )

daylightsaving

Returns a dual value corresponding to the current adjustment for daylight saving time, as per the system time. In Qlik Sense Client-Managed, the function returns different values depending on the time of year and current system time. In Qlik Cloud, the function always uses UTC time so the returned value is always a dual value indicating no time adjustments.

[**daylightsaving**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/daylightsaving.htm)(
)

converttolocaltime

Converts
a UTC or GMT timestamp to local time as a dual value. The
place can be any of a number of cities, places and time zones around the
world.

[**converttolocaltime**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/converttolocaltime.htm)(timestamp [, place [, ignore\_dst=false]])

### Set time functions

setdateyear

This function takes as input a timestamp and a year and updates the timestamp with the year specified in input.

[**setdateyear**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/setdateyear.htm)
(timestamp, year)

setdateyearmonth

This function takes as input a timestamp, a month and a year and updates the timestamp with the year and the month specified in input.

[**setdateyearmonth**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/setdateyearmonth.htm)
(timestamp, year, month)

### In... functions

inyear

This function returns
True if timestamp lies inside the
year containing base\_date.

[**inyear**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inyear.htm)(date, basedate , shift [, first\_month\_of\_year
= 1])

inyeartodate

This function returns
True if timestamp lies inside the
part of year containing base\_date
up until and including the last millisecond of base\_date.

[**inyeartodate**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inyeartodate.htm)
(date, basedate , shift [, first\_month\_of\_year
= 1])

inquarter

This function returns
True if timestamp lies inside the
quarter containing base\_date.

[**inquarter**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inquarter.htm)
(date, basedate , shift [, first\_month\_of\_year
= 1])

inquartertodate

This function returns
True if timestamp lies inside the
part of the quarter containing base\_date
up until and including the last millisecond of base\_date.

[**inquartertodate**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inquartertodate.htm)
(date, basedate , shift [, first\_month\_of\_year
= 1])

inmonth

This function returns
True if timestamp lies inside the
month containing base\_date.

[**inmonth**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inmonth.htm)(date, basedate , shift)

inmonthtodate

Returns
True if date lies inside the
part of month containing basedate
up until and including the last millisecond of basedate.

[**inmonthtodate**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inmonthtodate.htm)
(date, basedate , shift)

inmonths

This function finds if a timestamp falls within the same month, bi-month, quarter, four-month period, or half-year as a base date. It is also possible to find if the timestamp falls within a previous or following time period.

[**inmonths**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inmonths.htm)(n, date, basedate , shift [, first\_month\_of\_year
= 1])

inmonthstodate

This function finds if a timestamp falls within the part a period of the month, bi-month, quarter, four-month period, or half-year up to and including the last millisecond of `base_date`. It is also possible to find if the timestamp falls within a previous or following time period.

[**inmonthstodate**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inmonthstodate.htm)
(n, date, basedate , shift [, first\_month\_of\_year
= 1])

inweek

This function returns
True if timestamp lies inside the
week containing base\_date.

[**inweek**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inweek.htm)(date, basedate , shift [, weekstart])

inweektodate

This function returns
True if timestamp lies inside the
part of week containing base\_date
up until and including the last millisecond of base\_date.

[**inweektodate**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inweektodate.htm)
(date, basedate , shift [, weekstart])

inlunarweek

This function determines if timestamp lies inside the
lunar week
containing base\_date. Lunar weeks in Qlik Sense are defined by counting January 1 as the first day of the week., Apart from the final week of the year, each week will contain exactly seven days.

[**inlunarweek**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inlunarweek.htm)
(date, basedate , shift [, weekstart])

inlunarweektodate

This function finds if timestamp lies inside the
part of the lunar week up to and including the last millisecond of base\_date. Lunar weeks in Qlik Sense are defined by counting January 1 as the first day of the week and, apart from the final week of the year, will contain exactly seven days.

[**inlunarweektodate**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inlunarweektodate.htm)
(date, basedate , shift [, weekstart])

inday

This function returns
True if timestamp lies inside
the day containing base\_timestamp.

[**inday**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/inday.htm)(timestamp, basetimestamp , shift [, daystart])

indaytotime

This function returns
True if timestamp lies inside
the part of day containing base\_timestamp
up until and including the exact millisecond of base\_timestamp.

[**indaytotime**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/indaytotime.htm)(timestamp, basetimestamp , shift [, daystart])

### Start ... end functions

yearstart

This function returns
a timestamp corresponding to the start of the first day of the year containing date.
The default output format will be the DateFormat set in the script.

[**yearstart**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/yearstart.htm)( date [, shift = 0 [, first\_month\_of\_year
= 1]])

yearend

This function returns
a value corresponding to a timestamp of the last millisecond of the
last day of the year containing date.
The default output format will be the DateFormat set in the script.

[**yearend**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/yearend.htm)( date [, shift = 0 [, first\_month\_of\_year
= 1]])

yearname

This function returns
a four-digit year as display value with an underlying numeric value corresponding
to a timestamp of the first millisecond of the first day of the year
containing
date.

[**yearname**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/yearname.htm)(date [, shift = 0 [, first\_month\_of\_year
= 1]] )

quarterstart

This function returns
a value corresponding to a timestamp of the first millisecond of the
quarter containing date. The
default output format will be the DateFormat set in the script.

[**quarterstart**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/quarterstart.htm)(date [, shift = 0 [, first\_month\_of\_year
= 1]])

quarterend

This function returns
a value corresponding to a timestamp of the last millisecond of the
quarter containing date. The
default output format will be the DateFormat set in the script.

[**quarterend**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/quarterend.htm)(date [, shift = 0 [, first\_month\_of\_year
= 1]])

quartername

This function returns
a display value showing the months of the quarter (formatted according
to the MonthNames script variable) and year with an underlying numeric
value corresponding to a timestamp of the first millisecond of the first
day of the quarter.

[**quartername**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/quartername.htm)(date [, shift = 0 [, first\_month\_of\_year = 1]])

monthstart

This function returns
a value corresponding to a timestamp of the first millisecond of the
first day of the month containing date. The default output format will be the DateFormat set in the script.

[**monthstart**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthstart.htm)(date [, shift = 0])

monthend

This function returns
a value corresponding to a timestamp of the last millisecond of the
last day of the month containing `date`.
The default output format will be the `DateFormat` set in the script.

[**monthend**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthend.htm)(date [, shift = 0])

monthname

This function returns
a display value showing the month (formatted according to the MonthNames script variable) and year with an underlying numeric value corresponding
to a timestamp of the first millisecond of the first day of the month.

[**monthname**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthname.htm)(date [, shift = 0])

monthsstart

This function returns a value corresponding to the timestamp of the first millisecond of the month, bi-month, quarter, four-month period, or half-year containing a base date. It is also possible to find the timestamp for a previous or following time period.The default output format is the DateFormat set in the script.

[**monthsstart**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthsstart.htm)(n, date [, shift = 0 [, first\_month\_of\_year
= 1]])

monthsend

This function returns
a value corresponding to a timestamp of the last millisecond of the month, bi-month, quarter, four-month period, or half-year containing a base date. It is also possible to find the timestamp for a previous or following time period.

[**monthsend**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthsend.htm)(n, date [, shift = 0 [, first\_month\_of\_year
= 1]])

monthsname

This function returns
a display value representing the range of the months of the period (formatted according
to the MonthNames script variable) as well as the year. The underlying numeric
value corresponds to a timestamp of the first millisecond of the month, bi-month, quarter, four-month period, or half-year containing a base date.

[**monthsname**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/monthsname.htm)(n, date [, shift = 0 [, first\_month\_of\_year = 1]])

weekstart

This function returns
a value corresponding to a timestamp of the first millisecond of the
first day of the calendar week containing date.
The default output format is the DateFormat set in the script.

[**weekstart**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/weekstart.htm)(date [, shift = 0 [,weekoffset = 0]])

weekend

This function returns
a value corresponding to a timestamp of the last millisecond of the
last day of the calendar week containing date.
The default output format will be the DateFormat set in the script.

[**weekend**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/weekend.htm)(date [, shift = 0 [,weekoffset = 0]])

weekname

This function returns
a value showing the year and week number with an underlying numeric
value corresponding to a timestamp of the first millisecond of the first
day of the week containing date.

[**weekname**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/weekname.htm)(date [, shift = 0 [,weekoffset = 0]])

lunarweekstart

This function returns a value corresponding to a timestamp of the first millisecond of the first day of the lunar week containing date. Lunar weeks in Qlik Sense are defined by counting January 1 as the first day of the week and, apart from the final week of the year, will contain exactly seven days.

[**lunarweekstart**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekstart.htm)(date [, shift = 0 [,weekoffset = 0]])

lunarweekend

This function returns a value corresponding to a timestamp of the last millisecond of the last day of the lunar week containing date. Lunar weeks in Qlik Sense are defined by counting January 1 as the first day of the week and, apart from the final week of the year, will contain exactly seven days.

[**lunarweekend**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekend.htm)(date [, shift = 0 [,weekoffset = 0]])

lunarweekname

This function returns a display value showing the year and lunar week number corresponding to a timestamp of the first millisecond of the first day of the lunar week containing date. Lunar weeks in Qlik Sense are defined by counting January 1as the first day of the week and, apart from the final week of the year, will contain exactly seven days.

[**lunarweekname**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lunarweekname.htm)(date [, shift = 0 [,weekoffset = 0]])

daystart

This function returns
a value corresponding to a timestamp with the first millisecond of the
day contained in the time argument. The
default output format will be the TimestampFormat
set in the script.

[**daystart**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/daystart.htm)(timestamp [, shift = 0 [, dayoffset = 0]])

dayend

This function returns
a value corresponding to a timestamp of the final millisecond of the
day contained in time. The
default output format will be the TimestampFormat set in the script.

[**dayend**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/dayend.htm)(timestamp [, shift = 0 [, dayoffset = 0]])

dayname

This function returns
a value showing the date with an underlying numeric value corresponding
to a timestamp of the first millisecond of the day containing time.

[**dayname**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/dayname.htm)(timestamp [, shift = 0 [, dayoffset = 0]])

### Day numbering functions

age

The age function returns
the age at the time of timestamp
(in completed years) of somebody born on date\_of\_birth.

[**age**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/age.htm)(timestamp,
date\_of\_birth)

networkdays

The networkdays function returns
the number of working days (Monday-Friday) between and including start\_date and end\_date
taking into account any optionally listed holiday.

[**networkdays**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/networkdays.htm)
(start:date, end\_date {, holiday})

firstworkdate

The firstworkdate function returns
the latest starting date to achieve no\_of\_workdays
(Monday-Friday) ending no later than end\_date taking into account any
optionally listed holidays. end\_date
and holiday should
be valid dates or timestamps.

[**firstworkdate**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/firstworkdate.htm)(end\_date, no\_of\_workdays {, holiday} )

lastworkdate

The lastworkdate function returns
the earliest ending date to achieve no\_of\_workdays
(Monday-Friday) if starting at start\_date
taking into account any optionally listed holiday.
start\_date and holiday
should be valid dates or timestamps.

[**lastworkdate**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/lastworkdate.htm)(start\_date, no\_of\_workdays {, holiday})

daynumberofyear

This function calculates
the day number of the year in which a timestamp falls. The calculation is made from the first millisecond
of the first day of the year, but the first month can be offset.

[**daynumberofyear**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/daynumberofyear.htm)(date[,firstmonth])

daynumberofquarter

This function calculates
the day number of the quarter in which a timestamp falls. This function is used when creating a Master Calendar.

[**daynumberofquarter**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/daynumberofquarter.htm)(date[,firstmonth])
