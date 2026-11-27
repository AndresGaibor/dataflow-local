---
title: "Fact Script and chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/GeneralNumericFunctions/fact.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "General numeric functions"]
---

# Fact Script and chart function

Fact() returns the factorial of a positive integer x.

Syntax:

Fact(x)

Return data type:  integer

Limitations:

If the number x is not an integer, it will be truncated. Non-positive numbers will return NULL.

Examples and results:

Examples and results

| Examples | Results |
| --- | --- |
| Fact( 1 ) | Returns 1 |
| Fact( 5 ) | Returns 120 ( 1 \* 2 \* 3 \* 4 \* 5 = 120 ) |
| Fact( -5 ) | Returns NULL |
