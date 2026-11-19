---
title: "Loosen Table"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/loosen-table.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---
# Loosen Table

One or more Qlik Sense internal data tables can be explicitly declared loosely
coupled during script execution by using a Loosen Table statement. When a table is loosely coupled, all associations between field values in the table are removed. A similar effect could be achieved by loading each field of the loosely coupled table as independent, unconnected tables. Loosely coupled can be useful during testing to temporarily isolate different parts of the data structure. A loosely coupled table can be identified in the table viewer by the dotted lines. The use of one or more Loosen Table
statements in the script will make Qlik Sense disregard any setting of tables
as loosely coupled made before the script execution.

Syntax:

Loosen Tabletablename [
, tablename2 ...]

Loosen Tablestablename [
, tablename2 ...]

Either syntax: Loosen Table
or Loosen Tables can be used.

> **Note:** Should Qlik Sense find circular references in the data structure which cannot
> be broken by tables declared loosely coupled interactively or explicitly
> in the script, one or more additional tables will be forced loosely coupled
> until no circular references remain. When this happens, the **Loop Warning** dialog, gives a warning.

Example:

Tab1:

SELECT \*
from Trans;

Loosen Table
Tab1;
