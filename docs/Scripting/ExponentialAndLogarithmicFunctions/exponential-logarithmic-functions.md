---
title: "Exponential and logarithmic functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ExponentialAndLogarithmicFunctions/exponential-logarithmic-functions.htm#exp?id=1316
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions"]
---
Expand/Collapse all

# Exponential and logarithmic functions

This section describes functions related to exponential and logarithmic calculations. All functions can be used in both the data [load script](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ExponentialAndLogarithmicFunctions/exponential-logarithmic-functions.htm#glossary-0 "Glossary term") and in [chart](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ExponentialAndLogarithmicFunctions/exponential-logarithmic-functions.htm#glossary-1 "Glossary term") expressions.

In the functions below, the parameters are expressions where x and y
should be interpreted as real valued numbers.

exp

The natural exponential function, e^x, using the natural logarithm e
as base. The result is a positive number.

exp(x
)

Examples and results:

`exp(3)` returns 20.085.

log

The natural logarithm of x.
The function is only defined if x>
0. The result is a number.

log(x
)

Examples and results:

`log(3)` returns 1.0986

log10

The common logarithm (base 10) of x.
The function is only defined if x>
0. The result is a number.

log10(x
)

Examples and results:

`log10(3)` returns 0.4771

pow

Returns x
to the power of y. The result
is a number.

pow(x,y
)

Examples and results:

`pow(3, 3)` returns 27

sqr

x squared (x to the power of 2).
The result is a number.

sqr (x )

Examples and results:

`sqr(3)` returns 9

sqrt

Square root of x. The function
is only defined if x >= 0.
The result is a positive number.

sqrt(x
)

Examples and results:

`sqrt(3)` returns 1.732
