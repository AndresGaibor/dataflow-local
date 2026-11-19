---
title: "Previous Script function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/InterRecordFunctions/Previous.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Inter-record functions"]
---
# Previous Script function

Previous() finds the value of the expr expression using data from the previous input record that has not been discarded because of
a where clause. In the first record
of an internal table, the function will return NULL.

Syntax:

Previous(expr)

Return data type:  dual

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| expr | The expression or field containing the data to be measured. The expression can contain nested Previous() functions in order to access records further back. Data are fetched directly from the input source, making it possible to refer also to fields that have not been loaded into Qlik Sense, that is, even if they have not been stored in its associative database. |

Limitations:

In the first record
of an internal table, the function returns NULL.

Example:

Input the following into your [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/InterRecordFunctions/Previous.htm#glossary-0 "Glossary term"):

Sales2013:

Load \*, (Sales - Previous(Sales) )as Increase Inline [

Month|Sales

1|12

2|13

3|15

4|17

5|21

6|21

7|22

8|23

9|32

10|35

11|40

12|41

] (delimiter is '|');

By using the Previous() function in the Load statement, we can compare the current value of Sales with the preceding value, and use it in a third [field](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/InterRecordFunctions/Previous.htm#glossary-1 "Glossary term") Increase.

Resulting table

| Month | Sales | Increase |
| --- | --- | --- |
| 1 | 12 | - |
| 2 | 13 | 1 |
| 3 | 15 | 2 |
| 4 | 17 | 2 |
| 5 | 21 | 4 |
| 6 | 21 | 0 |
| 7 | 22 | 1 |
| 8 | 23 | 1 |
| 9 | 32 | 9 |
| 10 | 35 | 3 |
| 11 | 40 | 5 |
| 12 | 41 | 1 |

## Learn more

- [*Peek Script function*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/InterRecordFunctions/Peek.htm)
