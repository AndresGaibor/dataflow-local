---
title: "For..next"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptControlStatements/For.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script control statements"]
---

# For..next

The for..next control statement
is a script iteration construct with a counter. The statements inside the loop enclosed
by for and next
will be executed for each value of the counter variable between specified
low and high limits.

Syntax:

For counter = expr1 to expr2 [ step expr3 ]

[statements]

[exit for [ ( when
| unless )
condition ]

[statements]

Next [counter]

The expressions expr1, expr2 and expr3
are only evaluated the first time the loop is entered. The value of the
counter [variable](#glossary-0 "Glossary term") may be changed by statements inside the loop, but this
is not good programming practice.

If an exit for clause is encountered
inside the loop, the execution of the script will be transferred to the
first statement after the next
clause denoting the end of the loop. An exit
for clause can be made conditional by the optional use of a when or unless
suffix.

Information noteSince the for..next statement
is a control statement and as such is ended with either a semicolon or
end-of-line, each of its three possible clauses (for..to..step,
exit for and next)
must not cross a line boundary.

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| counter | A variable name. If counter is specified after next it must be the same variable name as the one found after the corresponding for. |
| expr1 | An expression which determines the first value of the counter variable for which the loop should be executed. |
| expr2 | An expression which determines the last value of the counter variable for which the loop should be executed. |
| expr3 | An expression which determines the value indicating the increment of the counter variable each time the loop has been executed. |
| condition | a logical expression evaluating to True or False. |
| statements | Any group of one or more Qlik Sense script statements. |

Example 1: Loading a sequence of files

// LOAD
files file1.csv..file9.csv

for a=1
to 9

> LOAD \* from
> file$(a).csv;

next

Example 2: Loading a random number of files

In this example, we assume there are data files x1.csv, x3.csv, x5.csv, x7.csv and x9.csv. Loading is stopped at a random point using the if rand(
)<0.5 then condition.

for counter=1
to 9 step 2

> set filename=x$(counter).csv;
>
> if rand(
> )<0.5 then
>
> > exit for
> > unless counter=1
>
> end if
>
> LOAD a,b
> from $(filename);

next

## Learn more

- [*For each..next*](For%20Each.htm)
- [*Next*](Next.htm)
- [*To*](To.htm)
- [*Exit*](Exit.htm)
