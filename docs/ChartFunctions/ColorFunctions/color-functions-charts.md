---
title: "Color functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/ColorFunctions/color-functions-charts.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions"]
---

# Color functions

Expand/Collapse all

# Color functions

These functions can be used in expressions associated with setting and evaluating the color [properties](#glossary-0 "Glossary term") of [chart](#glossary-1 "Glossary term") objects, as well as in data load scripts.

Information noteQlik Sense supports the color functions Color(), qliktechblue, and qliktechgray for backwards compatibility reasons, but use of them is not recommended.

Use the drop-down on each function to see a brief description and the syntax of each function. Click the function name in the syntax description for further details.

ARGB

ARGB() is used in expressions to set or evaluate the color properties of a chart object, where the color is defined by a red component r, a green
component g, and a blue component
b, with an alpha factor (opacity)
of alpha.

[**ARGB**](ARGB.htm)(alpha,
r, g,
b)

HSL

HSL() is used in expressions to set or evaluate the color properties of a chart object, where the color is defined by
values of hue, saturation, and luminosity between 0
and 1.

[**HSL**](HSL.htm) (hue,
saturation, luminosity)

RGB

RGB() returns an integer corresponding to the color code of the color defined by the three parameters: the red component r, the green component g, and the blue component b. These components must have integer values between 0 and 255. The function can be used in expressions to set or evaluate the color properties of a chart object.

[**RGB**](RGB.htm) (r, g, b)

Colormix1

Colormix1() is used in expressions to return an ARGB color representation from a two color gradient, based on a value between 0 and 1.

Colormix1 (Value , ColorZero , ColorOne)

Value is a real number between 0 and 1.

- If Value = 0 ColorZero is returned.
- If Value = 1 ColorOne is returned.
- If 0 < Value< 1 the appropriate intermediate shading is returned.

ColorZero is a valid RGB color representation for the color to be associated with the low end of the interval.

ColorOne is a valid RGB color representation for the color to be associated with the high end of the interval.

Information note

In Excel versions of downloaded charts, exported text is not automatically adjusted to a contrasting color if the chart is configured with a Background color expression that uses the colormix1 or colormix2 functions, or dark colors. This limitation applies to Qlik Cloud Analytics.

Example:

Colormix1(0.5, red(), blue())

returns:

ARGB(255,64,0,64) (purple)

Colormix2

Colormix2() is used in expressions to return an ARGB color representation from a two color gradient, based on a value between -1 and 1, with the possibility to specify an intermediate color for the center (0) position.

Colormix2 (Value ,ColorMinusOne , ColorOne[ , ColorZero])

Value is a real number between -1 and 1.

- If Value = -1 the first color is returned.
- If Value = 1 the second color is returned.
- If -1 < Value< 1 the appropriate color mix is returned.

ColorMinusOne is a valid RGB color representation for the color to be associated with the low end of the interval.

ColorOne is a valid RGB color representation for the color to be associated with the high end of the interval.

ColorZero is an optional valid RGB color representation for the color to be associated with the center of the interval.

SysColor

SysColor() returns the ARGB color representation for the Windows system color nr, where nr corresponds to the parameter to the Windows API function GetSysColor(nr).

SysColor (nr)

ColorMapHue

ColorMapHue() returns an ARGB value of a color from a colormap that varies the hue component of the HSV color model. The colormap starts with red, passes through yellow, green, cyan, blue, magenta, and returns to red. x must be specified as a value between 0 and 1.

ColorMapHue (x)

ColorMapJet

ColorMapJet() returns an ARGB value of a color from a colormap that starts with blue, passes through cyan, yellow and orange, and returns to red. x must be specified as a value between 0 and 1.

ColorMapJet (x)

## Pre-defined color functions

The following functions can be used in expressions for pre-defined colors. Each function returns an RGB color representation.

Optionally a parameter for alpha factor can be given, in which case an ARGB color representation is returned. An alpha factor of 0 corresponds to full transparency, and an alpha factor of 255 corresponds to full opacity. If a value for alpha is not entered, it is assumed to be 255.

Pre-defined color functions

|  |  |
| --- | --- |
| Color function | RGB value |
| black ([alpha]) | (0,0,0) |
| blue([alpha]) | (0,0,128) |
| brown([alpha]) | (128,128,0) |
| cyan([alpha]) | (0,128,128) |
| darkgray([alpha]) | (128,128,128) |
| green([alpha]) | (0,128,0) |
| lightblue([alpha]) | (0,0,255) |
| lightcyan([alpha]) | (0,255,255) |
| lightgray([alpha]) | (192,192,192) |
| lightgreen([alpha]) | (0,255,0) |
| lightmagenta([alpha]) | (255,0,255) |
| lightred([alpha]) | (255,0,0) |
| magenta([alpha]) | (128,0,128) |
| red([alpha]) | (128,0,0) |
| white([alpha]) | (255,255,255) |
| yellow([alpha]) | (255,255,0) |

Examples and results:

Examples and results

| Examples | Results |
| --- | --- |
| Blue() | RGB(0,0,128) |
| Blue(128) | ARGB(128,0,0,128) |
