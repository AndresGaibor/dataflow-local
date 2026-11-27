---
title: "localtime Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/localtime.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# localtime Script and chart function

This function returns a timestamp of the
current time for a specified time zone.

Syntax:

LocalTime([timezone [, ignoreDST ]])

Return data type:  dual

Arguments

| Argument | Description |
| --- | --- |
| timezone | The timezone is specified as a string containing any of the geographical places listed under Time Zone in the Windows Control Panel for Date and Time or as a string in the form 'GMT+hh:mm'. A list of accepted places and time zones is also presented in the table below.  If no time zone is specified, the local time is returned.  Information noteIf you use a DST offset (that is, you specify an ignoreDST argument value evaluating to False), you must specify a place, rather than a GMT offset, in the place argument. This is because adjusting for Daylight Saving Time requires latitudinal information in addition to the longitudinal information provided by a GMT offset. For more information, see [*Using GMT offsets in combination with DST*](#Using). |
| ignoreDST | If this argument evaluates to True, DST (daylight saving time) is ignored. Valid argument values evaluating to True include -1 and True().  If this argument evaluates to False, the timestamp is adjusted for daylight saving time. Valid argument values evaluating to False include 0 and False().  If the ignoreDST argument value is invalid, the function evaluates the expression as if the ignore\_dst value evaluates to True. If the ignoreDST argument value is not specified, the function evaluates the expression as if the ignore\_dst value evaluates to False. |

Valid places and time zones

| A-C | D-K | L-R | S-Z |
| --- | --- | --- | --- |
| Abu Dhabi | Darwin | La Paz | Samoa |
| Adelaide | Dhaka | Lima | Santiago |
| Alaska | Eastern Time (US & Canada) | Lisbon | Sapporo |
| Amsterdam | Edinburgh | Ljubljana | Sarajevo |
| Arizona | Ekaterinburg | London | Saskatchewan |
| Astana | Fiji | Madrid | Seoul |
| Athens | Georgetown | Magadan | Singapore |
| Atlantic Time (Canada) | Greenland | Mazatlan | Skopje |
| Auckland | Greenwich Mean Time : Dublin | Melbourne | Sofia |
| Azores | Guadalajara | Mexico City | Solomon Is. |
| Baghdad | Guam | Mid-Atlantic | Sri Jayawardenepura |
| Baku | Hanoi | Minsk | St. Petersburg |
| Bangkok | Harare | Monrovia | Stockholm |
| Beijing | Hawaii | Monterrey | Sydney |
| Belgrade | Helsinki | Moscow | Taipei |
| Berlin | Hobart | Mountain Time (US & Canada) | Tallinn |
| Bern | Hong Kong | Mumbai | Tashkent |
| Bogota | Indiana (East) | Muscat | Tbilisi |
| Brasilia | International Date Line West | Nairobi | Tehran |
| Bratislava | Irkutsk | New Caledonia | Tokyo |
| Brisbane | Islamabad | New Delhi | Urumqi |
| Brussels | Istanbul | Newfoundland | Warsaw |
| Bucharest | Jakarta | Novosibirsk | Wellington |
| Budapest | Jerusalem | Nuku'alofa | West Central Africa |
| Buenos Aires | Kabul | Osaka | Vienna |
| Cairo | Kamchatka | Pacific Time (US & Canada) | Vilnius |
| Canberra | Karachi | Paris | Vladivostok |
| Cape Verde Is. | Kathmandu | Perth | Volgograd |
| Caracas | Kolkata | Port Moresby | Yakutsk |
| Casablanca | Krasnoyarsk | Prague | Yerevan |
| Central America | Kuala Lumpur | Pretoria | Zagreb |
| Central Time (US & Canada) | Kuwait | Quito | - |
| Chennai | Kyiv | Riga | - |
| Chihuahua | - | Riyadh | - |
| Chongqing | - | Rome | - |
| Copenhagen | - | - | - |

Examples and results:

The examples below are based on the function being called on 2023-08-14 08:39:47 local time, with the local time zone of the server or desktop environment being GMT-05:00, and in a region which has implemented daylight saving time as of this listed date.

Scripting examples

| Example | Result |
| --- | --- |
| localtime () | Returns the local time 2023-08-14 08:39:47. |
| localtime ('London') | Returns the local time in London, 2023-08-14 13:39:47. |
| localtime ('GMT+02:00') | Returns the local time in the timezone of GMT+02:00, 2023-08-14 14:39:47. No adjustment is made for daylight saving time because a GMT offset, rather than a place, is specified. |
| localtime ('Paris',-1) | Returns the local time in Paris with daylight savings time ignored, 2023-08-14 13:39:47. |
| localtime ('Paris',True()) | Returns the local time in Paris with daylight savings time ignored, 2023-08-14 13:39:47. |
| localtime ('Paris',0) | Returns the local time in Paris, taking daylight savings time into account, 2023-08-14 14:39:47. |
| localtime ('Paris',False()) | Returns the local time in Paris, taking daylight savings time into account, 2023-08-14 14:39:47. |

## Using GMT offsets in combination with DST

Following the implementation of International Components for Unicode (ICU) libraries in Qlik Sense, the use of GMT (Greenwich Mean Time) offsets in combination with DST (Daylight Saving Time) requires additional latitudinal information.

GMT is a longitudinal (east-west) offset, whereas DST is a latitudinal (north-south) offset. For example, Helsinki (Finland) and Johannesburg (South Africa) share the same GMT+02:00 offset, but they do not share the same DST offset. This means that, further to the GMT offset, any DST offset requires information on the latitudinal position of the local time zone (geographical time zone input) in order to have full information about local DST conditions.
