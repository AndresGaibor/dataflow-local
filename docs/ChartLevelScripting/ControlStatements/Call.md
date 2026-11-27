---
title: "Call"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartLevelScripting/ControlStatements/Call.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Chart level scripting", "Control statements"]
---

# Call

The call control statement calls
a subroutine which must be defined by a previous sub
statement.

Syntax:

Call name ( [ paramlist ])

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| name | The name of the subroutine. |
| paramlist | A comma separated list of the actual parameters to be sent to the subroutine. Each item in the list may be a [field](#glossary-0 "Glossary term") name, a [variable](#glossary-1 "Glossary term") or an arbitrary expression. |

The subroutine called by a call
statement must be defined by a sub
encountered earlier during script execution.

Parameters are copied into the subroutine and, if the parameter in the
call statement is a variable and not an expression,
copied back out again upon exiting the subroutine.

Limitations:

- Since the call statement is
  a control statement and as such is ended with either a semicolon or end-of-line,
  it must not cross a line boundary.
- When you define a subroutine with Sub..end sub inside a control statement, for example if..then, you can only call the subroutine from within the same control statement.
