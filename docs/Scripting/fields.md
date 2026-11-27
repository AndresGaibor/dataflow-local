---
title: "Fields"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/fields.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Understanding script syntax and data structures"]
---

# Fields

Fields are the primary data-carrying entities in Qlik Sense. A
field typically contains a number of values, called field values.
In database terminology we say that the data processed by Qlik Sense comes
from data files. A file is composed
of several fields where each
data entry is a record. The terms
file, field
and record are equivalent to
table, column
and row respectively. The Qlik Sense
AQL logic works only on the fields and their field values.

Field data is retrieved by script via LOAD, SELECT
or Binary
statements. The only way of changing data in a field is by re-executing the script. The actual field values
can not be manipulated by the user from the layout or by means of automation.
Once read into Qlik Sense they can only be viewed and used for logical selections
and calculations.

Field values consist of numeric or alphanumeric (text) data. Numeric
values actually have dual values, the numeric value and its current, formatted
text representation. Only the latter is displayed in [sheet](#glossary-0 "Glossary term") objects etc.

The content of a field can be represented in a filter pane.
