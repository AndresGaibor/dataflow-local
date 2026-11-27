---
title: "General numeric functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/GeneralNumericFunctions/general-numeric-functions-charts.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions"]
---

# General numeric functions

Expand/Collapse all

# General numeric functions

In these general numeric functions, the arguments are expressions where x
should be interpreted as a real valued number. All functions can be used in both data load scripts and chart expressions.

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

bitcount

BitCount() returns how many bits in the binary equivalent of a decimal number are set to 1. That is, the function returns the number of set bits in integer\_number, where integer\_number is interpreted as a signed
32-bit integer.

[**bitcount**](bitcount.htm)(integer\_number)

div

Div() returns the integer part of the arithmetic division of the first argument by the second argument. Both parameters are interpreted as real numbers, that is,
they do not have to be integers.

[**div**](div.htm)(integer\_number1, integer\_number2)

fabs

Fabs() returns the absolute value of x. The result is a positive number.

[**fabs**](fabs.htm)(x)

fact

Fact() returns the factorial of a positive integer x.

[**fact**](fact.htm)(x)

frac

Frac() returns the fraction part of x.

[**frac**](frac.htm)(x)

sign

Sign() returns 1, 0 or -1 depending on whether x
is a positive number, 0, or a negative number.

[**sign**](sign.htm)(x)

## Combination and permutation functions

combin

Combin() returns the number of combinations of q
elements that can be picked from a set of p items. As represented by the formula: Combin(p,q) = p! / q!(p-q)! The order in which the items are selected is insignificant.

[**combin**](combin.htm)(p, q)

permut

Permut() returns the number of permutations of q elements that can be selected from a set of p items. As represented by the formula: Permut(p,q) = (p)! / (p - q)! The order in which the items are selected is significant.

[**permut**](permut.htm)(p, q)

## Modulo functions

fmod

fmod() is a generalized modulo function that returns the remainder part of the integer division of the first argument (the dividend) by the second argument (the divisor). The result is a real number. Both arguments are interpreted as real
numbers, that is, they do not have to be integers.

[**fmod**](fmod.htm)(a, b)

mod

Mod() is a mathematical modulo function that returns the non-negative remainder of an integer division. The first argument is the dividend, the second argument is the divisor, Both arguments must be integer values.

[**mod**](mod.htm)(integer\_number1, integer\_number2)

## Parity functions

even

Even() returns True (-1), if integer\_number is an even integer or zero. It returns False (0), if integer\_number is an odd
integer, and NULL if integer\_number is not
an integer.

[**even**](even.htm)(integer\_number)

odd

Odd() returns True (-1), if integer\_number is an odd
integer or zero. It returns False (0), if integer\_number is an even integer, and NULL if integer\_number is not
an integer.

[**odd**](odd.htm)(integer\_number)

## Rounding functions

ceil

Ceil() rounds up a number to the nearest multiple of the step shifted by the offset number.

[**ceil**](ceil.htm)(x[, step[, offset]])

floor

Floor() rounds down a number to the nearest multiple of the step shifted by the offset number.

[**floor**](floor.htm)(x[, step[, offset]])

round

Round() returns the result of rounding a number up or down to the nearest multiple of step shifted by the offset number.

[**round**](round.htm)( x [ , step
[ , offset ]])
