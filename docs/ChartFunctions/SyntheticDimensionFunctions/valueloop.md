---
title: "ValueLoop - chart function"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/SyntheticDimensionFunctions/valueloop.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Aggregation functions", "Synthetic dimension functions"]
---

# ValueLoop - chart function

ValueLoop() returns a set
of iterated values which, when used in a calculated dimension, will form a synthetic dimension.

The values generated will start with the from value and end with the to
value including intermediate values in increments of step.

Information noteIn [charts](#glossary-0 "Glossary term") with a synthetic dimension created with the ValueLoop function it is possible to reference the [dimension](#glossary-1 "Glossary term") value corresponding to a specific expression cell by restating the ValueLoop
function with the same parameters in the chart expression. The function may of course be used anywhere in the layout, but apart from when used
for synthetic dimensions it will only be meaningful inside an aggregation function.

Information noteSynthetic dimensions are not affected by selections.

Syntax:

ValueLoop(from [, to [, step ]])

Return data type:  dual

Arguments:

Arguments

| Arguments | Description |
| --- | --- |
| from | Start value in the set of values to be generated. |
| to | End value in the set of values to be generated. |
| step | Size of increment between values. |

Examples and results:

Function examples

| Example | Result |
| --- | --- |
| ValueLoop(1, 10) | This creates a dimension in a table, for example, that can be used for purposes such as numbered labeling. The example here results in values numbered 1 to 10. These values can then be referenced in an expression. |
| ValueLoop(2, 10,2) | This example results in values numbered 2, 4, 6, 8, and 10 because the argument step has a value of 2. |
