---
title: "Rem"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Rem.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---
# Rem

The rem statement is used for
inserting remarks, or comments, into the script, or to temporarily deactivate script
statements without removing them.

Syntax:

Rem string

Everything between the rem
and the next semicolon ; is considered
to be a comment.

There are two alternative methods available for making comments in the
script:

1. It is possible to create a comment anywhere in the script - except
   between two quotes - by placing the section in question between /\* and \*/.
2. When typing //
   in the script, all text that follows to the right on the same row becomes
   a comment. (Note the exception //: that may be used as part of an Internet
   address.)

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| string | An arbitrary text. |

Example:

Rem
\*\* This is a comment \*\*;

/\* This is also a comment \*/

// This is a comment as well
