---
title: "StateName  - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/SystemFunctions/StateName.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "System functions"]
---
# StateName - chart function

StateName() returns the name of the alternate state of the visualization in which it is used. StateName can be used, for example, to create visualizations with dynamic text and colors to reflect when the state of a visualization is changed. This function can be used in chart expressions, but cannot be used to determine the state that the expression refers to.

Syntax:

StateName ()

Example 1:

Dynamic Text

='Region - ' & if(StateName() = '$', 'Default', StateName())

Example 2:

Dynamic Colors

if(StateName() = 'Group 1', rgb(152, 171, 206),

> if(StateName() = 'Group 2', rgb(187, 200, 179),

> > rgb(210, 210, 210)

> )

)
