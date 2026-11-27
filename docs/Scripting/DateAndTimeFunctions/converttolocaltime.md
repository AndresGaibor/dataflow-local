---
title: "converttolocaltime Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/converttolocaltime.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# converttolocaltime Script and chart function

Converts
a UTC or GMT timestamp to local time as a dual value. The
place can be any of a number of cities, places and time zones around the
world.

Syntax:

ConvertToLocalTime(timestamp [, place [, ignore\_dst=false]])

Return data type:  dual

Arguments

| Argument | Description |
| --- | --- |
| timestamp | The timestamp, or expression resolving to a timestamp, to convert. |
| place | A place or timezone from the table of valid places and timezones below. Alternatively, you can use GMT or UTC to define the local time. The following values and time offset ranges are valid:   - GMT - GMT-12:00 - GMT-01:00 - GMT+01:00 - GMT+14:00 - UTC - UTC-12:00 - UTC-01:00 - UTC+01:00 - UTC+14:00   Information noteIf you use a DST offset (that is, you specify an ignore\_dst argument value evaluating to False), you must specify a place, rather than a GMT offset, in the place argument. This is because adjusting for Daylight Saving Time requires latitudinal information in addition to the longitudinal information provided by a GMT offset. For information, see [*Using GMT offsets in combination with DST*](#Using).  Information noteYou can only use standard time offsets. It's not possible to use an arbitrary time offset, for example, GMT-04:27. |
| ignore\_dst | If this argument evaluates to True, DST (daylight saving time) is ignored. Valid argument values evaluating to True include -1 and True().  If this argument evaluates to False, the timestamp is adjusted for daylight saving time. Valid argument values evaluating to False include 0 and False().  If the ignore\_dst argument value is invalid, the function evaluates the expression as if the ignore\_dst value evaluates to True. If the ignore\_dst argument value is not specified, the function evaluates the expression as if the ignore\_dst value evaluates to False. |

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

Scripting examples

| Example | Result |
| --- | --- |
| ConvertToLocalTime('2023-08-14 08:39:47','Paris') | Returns '2023-08-14 10:39:47' and the corresponding internal timestamp representation. |
| ConvertToLocalTime(UTC(), 'Stockholm') | Returns the time for Stockholm, adjusting for daylight saving time. |
| ConvertToLocalTime(UTC(), 'Stockholm', -1) | Returns the time for Stockholm, without daylight saving time adjustment. |
| ConvertToLocalTime(UTC(), 'GMT-05:00') | Returns the time for the North American east coast, for example, New York. No adjustment is made for daylight saving time because a GMT offset, rather than a place, is specified. |
| ConvertToLocalTime(UTC(), 'New York', -1) | Returns the time for the North American east coast (New York), without daylight saving time adjustment. |
| ConvertToLocalTime(UTC(), 'New York', True()) | Returns the time for the North American east coast (New York), without daylight saving time adjustment. |
| ConvertToLocalTime(UTC(), 'New York', 0) | Returns the time for the North American east coast (New York), adjusting for daylight saving time. |
| ConvertToLocalTime(UTC(), 'New York', False()) | Returns the time for the North American east coast (New York), adjusting for daylight saving time. |

## Using GMT offsets in combination with DST

Following the implementation of International Components for Unicode (ICU) libraries in Qlik Sense, the use of GMT (Greenwich Mean Time) offsets in combination with DST (Daylight Saving Time) requires additional latitudinal information.

GMT is a longitudinal (east-west) offset, whereas DST is a latitudinal (north-south) offset. For example, Helsinki (Finland) and Johannesburg (South Africa) share the same GMT+02:00 offset, but they do not share the same DST offset. This means that, further to the GMT offset, any DST offset requires information on the latitudinal position of the local time zone (geographical time zone input) in order to have full information about local DST conditions.
