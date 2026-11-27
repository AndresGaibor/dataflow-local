---
title: "Force"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptRegularStatements/Force.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements"]
---

# Force

The force statement forces Qlik Sense
to interpret field values of subsequent LOAD
and SELECT
statements as written with only upper case letters, with only lower case
letters, as always capitalized or as they appear (mixed). This statement
makes it possible to associate field values from tables made according
to different conventions.

The force statement can also change field names during a load or select with the following data sources:

- QVD
- CSV (text files)
- XLS
- QVX (files and ODBC connections)

The force statement only changes field names if the data is loaded in compact mode (loaded with \*).

The field names of the following data sources are not affected by the force statement:

- JSON
- Parquet
- XML
- XLSX

Syntax:

Force ( capitalization | case upper | case
lower | case mixed )

If nothing is specified, force case mixed is assumed. The force statement
is valid until a new force statement is made.

The force
statement has no effect in the access section: all [field](#glossary-0 "Glossary term") values loaded are case insensitive.

Examples and results

| Example | Result |
| --- | --- |
| This example shows how to force capitalization.  FORCE Capitalization;  Capitalization:  LOAD \* Inline [  ab  Cd  eF  GH  ]; | The Capitalization table contains the following values:  Ab  Cd  Ef  Gh  All values are capitalized. |
| This example shows how to force case upper.  FORCE Case Upper;  CaseUpper:  LOAD \* Inline [  ab  Cd  eF  GH  ]; | The CaseUpper table contains the following values:  AB  CD  EF  GH  All values are upper case. |
| This example shows how to force case lower.  FORCE Case Lower;  CaseLower:  LOAD \* Inline [  ab  Cd  eF  GH  ]; | The CaseLower table contains the following values:  ab  cd  ef  gh  All values are lower case. |
| This example shows how to force case mixed.  FORCE Case Mixed;  CaseMixed:  LOAD \* Inline [  ab  Cd  eF  GH  ]; | The CaseMixed table contains the following values:  ab  Cd  eF  GH  All values are as they appear in the script. |

## Learn more

- [*Load*](Load.htm)
- [*Select*](Select.htm)
