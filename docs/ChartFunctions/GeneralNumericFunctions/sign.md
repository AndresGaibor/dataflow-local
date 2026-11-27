---
title: "Sign Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/GeneralNumericFunctions/sign.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "General numeric functions"]
---

# Sign Script and chart function

Sign() returns 1, 0 or -1 depending on whether x
is a positive number, 0, or a negative number.

Syntax:

Sign(x)

Return data type:  numeric

Limitations:

If no numeric
value is found, NULL is returned.

Examples and results:

Examples and results

| Examples | Results |
| --- | --- |
| Sign( 66 ) | Returns 1 |
| Sign( 0 ) | Returns 0 |
| Sign( - 234 ) | Returns -1 |
