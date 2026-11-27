---
title: "If..then..elseif..else..end if"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptControlStatements/If.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script control statements"]
---

# If..then..elseif..else..end if

The if..then control statement is a script selection construct forcing the script execution to follow different paths depending on one or several logical conditions.

Control statements are typically used to control the flow of the script execution. In a chart expression, use the if conditional function instead. For more information see [*if Script and chart function*](../ConditionalFunctions/if.htm).

Syntax:

If 
condition then

  [ statements ]

{ elseif condition then

  [ statements ] }

[ else

  [ statements ] ]

end if

Since the if..then statement
is a control statement and as such is ended with either a semicolon or
end-of-line, each of its four possible clauses (if..then,
elseif..then, else
and end if) must not cross a line
boundary.

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| condition | A logical expression which can be evaluated as True or False. |
| statements | Any group of one or more Qlik Sense script statements. |

Example 1:

if a=1 then

> LOAD \* from
> abc.csv;
>
> SQL SELECT
> e, f, g from tab1;

end if

Example 2:

if a=1 then; drop table xyz; end if;

Example 3:

if x>0
then

> LOAD \* from
> pos.csv;

elseif
x<0 then

> LOAD \* from
> neg.csv;

else

> LOAD \* from
> zero.txt;

end
if

## Learn more

- [*End*](End.htm)
