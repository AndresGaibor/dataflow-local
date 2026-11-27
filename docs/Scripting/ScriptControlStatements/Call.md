---
title: "Call"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptControlStatements/Call.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script control statements"]
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
| paramlist | A comma separated list of the actual parameters to be sent to the subroutine. Each item in the list may be a [field](#glossary-0 "Glossary term") name, a [variable](#glossary-1 "Glossary term"), or an arbitrary expression. |

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

Example:

This example lists all Qlik related files in a folder and its subfolders, and stores file information in a table. It is assumed that you have created a [data connection](#glossary-2 "Glossary term") named Applications to the folder .

The DoDir subroutine is called with the reference to the folder, 'lib://Applications', as parameter. Inside the subroutine, there is a recursive call, Call DoDir (Dir), that makes the function look for files recursively in subfolders.

sub DoDir (Root)
For Each Ext in 'qvw', 'qvo', 'qvs', 'qvt', 'qvd', 'qvc', 'qvf'
For Each File in filelist (Root&'\\*.' &Ext)
LOAD
'$(File)' as Name,
FileSize( '$(File)' ) as Size,
FileTime( '$(File)' ) as FileTime
autogenerate 1;
Next File
Next Ext
For Each Dir in dirlist (Root&'\\*' )
Call DoDir (Dir)
Next Dir
End Sub
Call DoDir ('lib://Applications')
