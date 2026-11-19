---
title: "Script syntax overview"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/script-syntax.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions"]
---
# Script syntax overview

In a script, the name of the data source, the names of the tables, and the names of the fields included in the logic are defined. Furthermore, the fields in the access rights definition are defined in the script. A script consists of a number of statements that are executed consecutively.

The Qlik Sense command line syntax and script
syntax are described in a notation called Backus-Naur Formalism, or
BNF code.

[*What is Backus-Naur formalism?*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/Backus-Naur-formalism.htm)

The first lines of code are already generated when a new Qlik Sense file
is created. The default values of these number interpretation [variables](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/script-syntax.htm#glossary-0 "Glossary term") are derived from the regional settings of
the OS.

[*Working with variables in the data load editor*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/work-with-variables-in-data-load-editor.htm)

[*Number interpretation variables*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/NumberInterpretationVariables/number-interpretation-variables.htm)

The script consists of a number of script statements and keywords
that are executed consecutively. All script statements must end with a semicolon, ";".

[*Script statements and keywords*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/script-statements-keywords.htm)

You can use expressions and functions in the LOAD-statements to transform the data that has been loaded.

[*Script expressions*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/script-expressions.htm)

For a table file with commas, tabs or semicolons
as delimiters, a LOAD-statement
may be used. By default a LOAD-statement
will load all fields of the file.

General databases can be accessed through ODBC or OLE DBdatabase connectors.
Here standard SQL statements are used. The
SQL syntax accepted differs between different ODBC drivers.

Additionally, you can access other data sources using custom connectors.

[*Loading analytics data*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/connect-data-sources.htm)
