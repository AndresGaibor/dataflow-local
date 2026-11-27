---
title: "Table labels"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/table-labels.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Understanding script syntax and data structures", "Logical tables"]
---

# Table labels

A table can be labeled for later reference, for example by a LOAD
statement with a resident clause
or with expressions containing the peek
function. The label, which can be an arbitrary string of numbers or characters,
should precede the first LOAD
or SELECT
statement that creates the table. The label must be followed by a colon ":".

Labels containing blanks must be quoted using single or double quotation marks or square brackets.

Example 1:

Table1:

LOAD a,b
from c.csv;

LOAD x,y
from d.csv where x=peek('a',y,'Table1');

Example 2: Table label containing a blank

[All Transactions]:

SELECT \*
from Transtable;

LOAD
Month, sum(Sales) resident [All Transactions] group by Month;

## Learn more

- [*Load*](ScriptRegularStatements/Load.htm)
- [*Select*](ScriptRegularStatements/Select.htm)
