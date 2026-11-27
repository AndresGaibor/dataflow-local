---
title: "daylightsaving Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/DateAndTimeFunctions/daylightsaving.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Date and time functions"]
---

# daylightsaving Script and chart function

Returns a dual value corresponding to the current adjustment for daylight saving time, as per the system time. In Qlik Sense Client-Managed, the function returns different values depending on the time of year and current system time. In Qlik Cloud, the function always uses UTC time so the returned value is always a dual value indicating no time adjustments.

Syntax:

DaylightSaving(
)

Return data type:  dual

Example:

daylightsaving(
)
