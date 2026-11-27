---
title: "Switch..case..default..end switch"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartLevelScripting/ControlStatements/Switch.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Chart level scripting", "Control statements"]
---

# Switch..case..default..end switch

The switch control statement is a script selection construct forcing the script execution to follow different paths,
depending on the value of an expression.

Syntax:

Switch expression {case valuelist [ statements ]} [default statements] end switch

Information noteSince the switch statement is
a control statement and as such is ended with either a semicolon or end-of-line,
each of its four possible clauses (switch,
case, default and end switch) must not
cross a line boundary.

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| expression | An arbitrary expression. |
| valuelist | A comma separated list of values with which the value of expression will be compared. Execution of the script will continue with the statements in the first group encountered with a value in valuelist equal to the value in expression. Each value in valuelist may be an arbitrary expression. If no match is found in any case clause, the statements under the default clause, if specified, will be executed. |
| statements | Any group of one or more Qlik Sense script statements. |

Example:

Switch I

Case 1

LOAD '$(I):
CASE 1' as case autogenerate 1;

Case 2

LOAD '$(I):
CASE 2' as case autogenerate 1;

Default

LOAD '$(I):
DEFAULT' as case autogenerate 1;

End Switch

## Learn more

- [*End*](End.htm)
