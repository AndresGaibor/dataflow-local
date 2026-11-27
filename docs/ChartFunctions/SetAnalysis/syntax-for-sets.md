---
title: "Syntax for set expressions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/SetAnalysis/syntax-for-sets.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Chart expressions", "Set analysis"]
---

# Syntax for set expressions

The full syntax (not including the optional use of standard brackets to define precedence) is described using Backus-Naur Formalism:

set\_expression ::= { set\_entity { set\_operator set\_entity } }

set\_entity ::= set\_identifier [ set\_modifier ] | set\_modifier

set\_identifier ::= 1 | $ | $N | $\_N | bookmark\_id | bookmark\_name

set\_operator ::= + | - | \* | /

set\_modifier ::= < field\_selection {, field\_selection } >

field\_selection ::= field\_name [ = | += | –= | \*= | /= ] element\_set\_expression

element\_set\_expression ::= [ - ] element\_set { set\_operator element\_set }

element\_set ::= [ field\_name ] | { element\_list } | element\_function

element\_list ::= element { , element }

element\_function ::= ( P | E ) ( [set\_expression] [field\_name] )

element ::= field\_value | " search\_mask "

## Learn more

- [*What is Backus-Naur formalism?*](../../Scripting/Backus-Naur-formalism.htm)
