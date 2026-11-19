---
title: "Trigonometric and hyperbolic functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/TrigonometricAndHyperbolicFunctions/trigonometric-hyperbolic-functions.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions"]
---
Expand/Collapse all

# Trigonometric and hyperbolic functions

This section describes functions for performing trigonometric and hyperbolic operations. In all of the functions, the arguments are expressions resolving to angles measured in radians, where x should be interpreted as a real number.

All angles are measured in radians.

All functions can be used in both the data load script and in chart expressions.

cos

Cosine of x. The result is a number between -1 and 1.

cos( x
)

acos

Inverse cosine of x. The function is only defined if -1≤x≤1.
The result is a number between 0 and p.

acos( x
)

sin

Sine of x.
The result is a number between -1 and 1.

sin( x
)

asin

Inverse sine of x.
The function is only defined if -1≤x≤1.
The result is a number between - p/2
and p/2.

asin( x
)

tan

Tangent of x.
The result is a real number.

tan( x
)

atan

Inverse tangent of x.
The result is a number between - p/2
and p/2.

atan( x
)

atan2

Two-dimensional generalization of the inverse
tangent function. Returns the angle between the origin and the point represented
by the coordinates x and y. The result is a number between -
p and + p.

atan2( y,x
)

cosh

Hyperbolic cosine of x. The result is a
positive real number.

cosh( x
)

sinh

Hyperbolic sine of x.
The result is a real number.

sinh( x
)

tanh

Hyperbolic tangent of x.
The result is a real number.

tanh( x
)

acosh

Inverse hyperbolic cosine of x. The result is a
positive real number.

acosh( x
)

asinh

Inverse hyperbolic sine of x.
The result is a real number.

asinh( x
)

atanh

Inverse hyperbolic tangent of x.
The result is a real number.

atanh( x
)

Examples:

The following script code loads a sample table, and then loads a table containing the calculated trigonometric and hyperbolic operations on the values.

SampleData:
LOAD \* Inline
[Value
-1
0
1];
Results:
Load \*,
cos(Value),
acos(Value),
sin(Value),
asin(Value),
tan(Value),
atan(Value),
atan2(Value, Value),
cosh(Value),
sinh(Value),
tanh(Value)
RESIDENT SampleData;
Drop Table SampleData;
