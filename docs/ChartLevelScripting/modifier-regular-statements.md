---
title: "Regular statements"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartLevelScripting/modifier-regular-statements.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Chart level scripting"]
---

# Regular statements

Expand/Collapse all

# Regular statements

Regular statements are typically used for manipulating data in one way
or another. These statements may be written over any number of lines in
the script and must always
be terminated by a semicolon, ";".

All script keywords can be typed with any combination of lower case and upper case characters. Field and variable names used in the statements are however case sensitive.

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

LOAD

In a [chart](#glossary-0 "Glossary term") modifying context, the LOAD statement loads additional data to the hypercube from data defined in the script, or from a previously
loaded table. It is also possible to load data from analytic connections.

Information noteThe LOAD statement must have either Replace or Add prefix, or it will be rejected.

Add | Replace [**Load**](RegularStatements/Load.htm) [ distinct
] fieldlist

(

inline data [ format-spec ] |

resident table-label

) | extension pluginname.functionname([script] tabledescription)]

[
where criterion | while criterion
]

[
group by groupbyfieldlist
]

[order by orderbyfieldlist ]

Let

The let statement is a complement to the set
statement, used for defining script variables.
The let statement, in opposition
to the set statement, evaluates
the expression on the right side of the ' =' at script run time before it is assigned to
the variable.

[**Let**](RegularStatements/Let.htm) variablename=expression

Set

The set statement is used for
defining script variables. These can
be used for substituting strings, paths, drives, and so on.

[**Set**](RegularStatements/Set.htm) variablename=string

Put

The Put statement is used to set some numeric value in the hypercube.

HCValue

The HCValue statement is used to retrieve values in a row of a specified column.
