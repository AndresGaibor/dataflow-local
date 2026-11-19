---
title: "IterNo Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/CounterFunctions/IterNo.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Counter functions"]
---
# IterNo Script function

This script function returns an integer indicating for which time one single record
is evaluated in a LOAD statement
with a while clause. The first
iteration has number 1. The IterNo function is only meaningful if used together with a while clause.

Syntax:

IterNo( )

Examples and results:

Example:

LOAD   
   IterNo() as Day,  
   Date( StartDate + IterNo() - 1 ) as Date  
   While StartDate + IterNo() - 1 <= EndDate;

LOAD \* INLINE

[StartDate, EndDate

2014-01-22, 2014-01-26

];

This LOAD statement will generate one record per date within the range defined by StartDate and EndDate.

In this example, the resulting table will look like this:

Results table

| Day | Date |
| --- | --- |
| 1 | 2014-01-22 |
| 2 | 2014-01-23 |
| 3 | 2014-01-24 |
| 4 | 2014-01-25 |
| 5 | 2014-01-26 |
