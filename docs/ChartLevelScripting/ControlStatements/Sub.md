---
title: "Sub..end sub"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartLevelScripting/ControlStatements/Sub.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Chart level scripting", "Control statements"]
---

# Sub..end sub

The sub..end sub control statement
defines a subroutine which can be called upon from a call
statement.

Syntax:

Sub name [
( paramlist )] statements end sub

Arguments are copied into the subroutine and, if the corresponding actual parameter
in the call statement
is a [variable](#glossary-0 "Glossary term") name, copied back out again upon exiting the subroutine.

If a subroutine has more formal parameters than actual parameters passed
by a call statement, the extra
parameters will be initialized to NULL and can be used as local variables
within the subroutine.

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| name | The name of the subroutine. |
| paramlist | A comma separated list of variable names for the formal parameters of the subroutine. These can be used as any variable inside the subroutine. |
| statements | Any group of one or more Qlik Sense script statements. |

Limitations:

- Since the sub statement is a
  control statement and as such is ended with either a semicolon or end-of-line,
  each of its two clauses (sub and
  end sub) must not cross a line
  boundary.
- When you define a subroutine with Sub..end sub inside a control statement, for example if..then, you can only call the subroutine from within the same control statement.

Example 1:

Sub INCR
(I,J)

I = I +
1

Exit Sub
when I < 10

J = J +
1

End Sub

Call INCR
(X,Y)

Example 2: - parameter transfer

Sub ParTrans
(A,B,C)

A=A+1

B=B+1

C=C+1

End Sub

A=1

X=1

C=1

Call ParTrans
(A, (X+1)\*2)

The result of the above will be that locally, inside the subroutine, A will be initialized to 1, B will be initialized to 4 and C will be initialized to NULL.

When exiting the subroutine, the global variable A will get 2 as value (copied back from subroutine). The second actual parameter “(X+1)\*2” will not be copied back since it is not a variable. Finally, the global variable C will not be affected by the subroutine call.

## Learn more

- [*Call*](Call.htm)
- [*Exit*](Exit.htm)
- [*End*](End.htm)
