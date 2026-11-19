---
title: "Script control statements"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptControlStatements/script-control-statements.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords"]
---
Expand/Collapse all

# Script control statements

The Qlik Sense script consists of a number of statements. A statement
can be either a regular script statement
or a script control statement.

Control statements are typically used for controlling the flow of the
script execution. Each clause of a control statement must be kept inside
one script line and may be terminated by semicolon or end-of-line.

Prefixes are never applied to control statements, with the exceptions
of the prefixes when and unless which may be used with a few
specific control statements.

All script keywords can be typed with any combination of lower case
and upper case characters.

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

Call

The call control statement calls
a subroutine which must be defined by a previous sub
statement.

[**Call**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptControlStatements/Call.htm) name ( [ paramlist ])

Do..loop

The do..loop control statement is a script iteration construct which executes one or several statements until a logical condition is met.

[**do**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptControlStatements/do.htm) [ ( while |
until ) condition ] [statements]  
[exit do [ ( when | unless )
condition ] [statements]  
loop [ ( while | until ) condition ]

Exit script

This control statement stops script execution. It may be inserted anywhere in the script.

[**exit script**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptControlStatements/exit%20script.htm)[ (when | unless)
condition ]

Exit error

The Exit error statement ends script execution and raises a user-defined script error.

[**exit error**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptControlStatements/exit%20error.htm) expression [ (when | unless)
condition ]

For each ..next

The for each..next control statement is a script iteration construct which executes one or several statements for each value in a comma separated list.
The statements inside the loop enclosed by for
and next will be executed for
each value of the list.

[**For Each**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptControlStatements/For%20Each.htm) var in list

[statements]

[exit for [ ( when
| unless )
condition ]

[statements]

next [var]

For..next

The for..next control statement
is a script iteration construct with a counter. The statements inside the loop enclosed
by for and next
will be executed for each value of the counter variable between specified
low and high limits.

[**For**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptControlStatements/For.htm)counter = expr1 to expr2 [ stepexpr3 ]

[statements]

[exit for [ ( when
| unless )
condition ]

[statements]

Next [counter]

If..then

The if..then control statement is a script selection construct forcing the script execution to follow different paths depending on one or several logical conditions.

> **Note:** Since the if..then statement
> is a control statement and as such is ended with either a semicolon or
> end-of-line, each of its four possible clauses (if..then,
> elseif..then, else
> and end if) must not cross a line
> boundary.

[**If**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptControlStatements/If.htm)
condition then

  [ statements ]

{ elseif condition then

  [ statements ] }

[ else

  [ statements ] ]

end if

Sub

The sub..end sub control statement
defines a subroutine which can be called upon from a call
statement.

[**Sub**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptControlStatements/Sub.htm) name [
( paramlist )] statements end sub

Switch

The switch control statement is a script selection construct forcing the script execution to follow different paths,
depending on the value of an expression.

[**Switch**](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptControlStatements/Switch.htm) expression {case valuelist [ statements ]} [default statements] end switch
