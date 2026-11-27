---
title: "For each..next"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartLevelScripting/ControlStatements/for-each.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Chart level scripting", "Control statements"]
---

# For each..next

The for each..next control statement is a script iteration construct which executes one or several statements for each value in a comma separated list.
The statements inside the loop enclosed by for
and next will be executed for
each value of the list.

Syntax:

Special syntax makes it possible to generate lists
with file and directory names in the current directory.

for each var in list

[statements]

[exit for [ ( when
| unless )
condition ]

[statements]

next [var]

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| var | A script [variable](#glossary-0 "Glossary term") name which will acquire a new value from list for each loop execution. If var is specified after next it must be the same variable name as the one found after the corresponding for each. |

The value of the var variable
may be changed by statements inside the loop, but this is not good programming
practice.

If an exit for clause is encountered
inside the loop, the execution of the script will be transferred to the
first statement after the next
clause denoting the end of the loop. An exit
for clause can be made conditional by the optional use of a when or unless
suffix.

Information noteSince the for each..next statement
is a control statement and as such is ended with either a semicolon or
end-of-line, each of its three possible clauses (for
each, exit for and next) must not cross a line boundary.

Syntax:

list := item { , item }

item := constant | (expression) | filelist mask | dirlist mask | fieldvaluelist mask

Arguments

| Argument | Description |
| --- | --- |
| constant | Any number or string. Note that a string written directly in the script must be enclosed by single quotes. A string without single quotes will be interpreted as a variable, and the value of the variable will be used. Numbers do not need to be enclosed by single quotes. |
| expression | An arbitrary expression. |
| mask | A filename or folder name mask which may include any valid filename characters as well as the standard wildcard characters, \* and ?.  You can use absolute file paths or lib:// paths. |
| condition | A logical expression evaluating to True or False. |
| statements | Any group of one or more Qlik Sense script statements. |
| filelist mask | This syntax produces a comma separated list of all files in the current directory matching the filename mask. |
| dirlist mask | This syntax produces a comma separated list of all folders in the current folder matching the folder name mask. |
| fieldvaluelist mask | This syntax iterates through the values of a [field](#glossary-1 "Glossary term") already loaded into Qlik Sense. |

Warning noteThe Qlik Web Storage Provider Connectors and other DataFiles connections do not support filter masks that use wildcard (\* and ?) characters.

Example 1:  Loading a list of files

// LOAD the files 1.csv, 3.csv, 7.csv and xyz.csv
for each a in 1,3,7,'xyz'
LOAD \* from file$(a).csv;
next

Example 2:  Creating a list of files on disk

This example loads a list of all Qlik Sense related files in a folder.

sub DoDir (Root)
for each Ext in 'qvw', 'qva', 'qvo', 'qvs', 'qvc', 'qvf', 'qvd'
for each File in filelist (Root&'/\*.' &Ext)
LOAD
'$(File)' as Name,
FileSize( '$(File)' ) as Size,
FileTime( '$(File)' ) as FileTime
autogenerate 1;
next File
next Ext
for each Dir in dirlist (Root&'/\*' )
call DoDir (Dir)
next Dir
end sub
call DoDir ('lib://DataFiles')

Example 3:  Iterating through a the values of a field

This example iterates through the list of loaded values of FIELD and generates a new field, NEWFIELD. For each value of FIELD, two NEWFIELD records will be created.

load \* inline [
FIELD
one
two
three
];
FOR Each a in FieldValueList('FIELD')
LOAD '$(a)' &'-'&RecNo() as NEWFIELD AutoGenerate 2;
NEXT a

The resulting table looks like this:

Example table

| NEWFIELD |
| --- |
| one-1 |
| one-2 |
| two-1 |
| two-2 |
| three-1 |
| three-2 |

## Learn more

- [*For..next*](For.htm)
- [*Next*](Next.htm)
- [*Exit*](Exit.htm)
