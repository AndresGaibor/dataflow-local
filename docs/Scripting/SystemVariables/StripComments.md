---
title: "StripComments"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemVariables/StripComments.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Working with variables in the data load editor", "System variables"]
---

# StripComments

If this variable is set to 0, stripping of /\*..\*/ and // comments in the
script will be inhibited. If this variable is not defined, stripping of comments will always
be performed.

Syntax:

StripComments

Certain
database drivers use /\*..\*/ as optimization hints in SELECT
statements. If this is the case, the comments should not be stripped before sending the SELECT statement to the database driver.

Information note It is recommended that this
variable be reset to 1 immediately after the statement(s) where it is
needed.

Example:

set StripComments=0;

SQL SELECT \* /\* <optimization directive> \*/ FROM Table ;

set StripComments=1;

## Learn more

- [*System variables*](system-variables.htm)
