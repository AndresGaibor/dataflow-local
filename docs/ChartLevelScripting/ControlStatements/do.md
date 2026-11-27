---
title: "Do..loop"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartLevelScripting/ControlStatements/do.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Chart level scripting", "Control statements"]
---

# Do..loop

The do..loop control statement is a script iteration construct which executes one or several statements until a logical condition is met.

Syntax:

Do [ ( while |
until ) condition ] [statements]
[exit do [ ( when | unless )
condition ] [statements]
loop[ ( while | until ) condition ]

Information noteSince the do..loop statement
is a control statement and as such is ended with either a semicolon or
end-of-line, each of its three possible clauses (do,
exit do and loop)
must not cross a line boundary.

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| condition | A logical expression evaluating to True or False. |
| statements | Any group of one or more Qlik Sense script statements. |
| while / until | The while or until conditional clause must only appear once in any do..loop statement, i.e. either after do or after loop. Each condition is interpreted only the first time it is encountered but is evaluated for every time it encountered in the loop. |
| exit do | If an exit do clause is encountered inside the loop, the execution of the script will be transferred to the first statement after the loop clause denoting the end of the loop. An exit do clause can be made conditional by the optional use of a when or unless suffix. |

## Learn more

- [*Exit*](Exit.htm)
