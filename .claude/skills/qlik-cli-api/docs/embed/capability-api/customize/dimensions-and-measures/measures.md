---
source: https://qlik.dev/embed/capability-api/customize/dimensions-and-measures/measures/
last_updated: 2025-07-08T16:09:30Z
---

# Measures

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

Measures are calculations used in visualizations, typically represented on the
y-axis of a bar chart or a column in a table. Measures are created from an
expression composed of aggregation functions, such as `Sum` or `Max`, combined with
one or several fields.

An expression is a combination of functions, fields, and mathematical operators
(+ \* / =). Expressions are used to process data in the app to produce a
result that can be seen in a visualization.

## Overview

There are three different ways of specifying measures in the columns definition:

- As a string
- As a `NxMeasure` structure
- As a reference to a predefined measure, a so-called master measure

> **Note:** The order of the columns are not always important.
> For a basic bar chart with one dimension and one measure, the columns can be specified in any order.
> However, for a table it matters which order the columns are specified, since the order specified in the cols parameter
> is the order shown in the table.

## Defining measures using string syntax

Using the string syntax is the easiest way of defining measures. But there are
some limitations and if you want create more advanced measures, you should use
the object syntax instead.

```json
[
  "NetScoreName",
  "=Count(NetScoreName)"
]
```

One dimension (NetScoreName) and one measure (=Count(NetScoreName))

## Defining measures using the object syntax

Use the object syntax if you want to set more options for your measures,
for example, if you want to set labels or define number formatting.

```json
{
  /*NxMeasure structure*/
  "qSortBy": {
    "qSortByNumeric": -1
  },
  "qAttributeExpressions": [
    {
      "qExpression": "If(Avg(FwHit)<0.5,RGB(255, 115, 115),If(Avg(FwHit)>0.7,RGB
      (145, 194, 106)))",
      "id": "cellBackgroundColor"
    }
  ],
  "qDef": {
    /*NxInlineMeasureDef structure*/
    "qLabel": "FIR%",
    "qDef": "Avg(FwHit)",
    "qNumFormat": {
      "qType": "F",
      "qnDec": 2,
      "qUseThou": 0,
      "qFmt": "0.0%",
      "qDec": ".",
      "qThou": ","
    }
  }
}
```

### The NxMeasure structure

When defining measures using the object syntax you define it as a `NxMeasure`
structure. Most settings are however done inside `"qDef"`, which is a
`NxInlineMeasureDef` structure.

For full details, see [Qlik Sense Engine API: NxMeasure](https://qlik.dev/apis/json-rpc/qix/schemas/#nxmeasure).

- qLibraryId: Refers to a measure stored in the library.

- qDef: The definition of the measure. For full details, see [Qlik Sense Engine API: NxInlineMeasureDef](https://qlik.dev/apis/json-rpc/qix/schemas/#nxinlinemeasuredef).

- qSortBy: Defines the sort criteria. The default value is sort by ascending
  alphabetic order.

- qCalcCond: Specifies a calculation condition, which must be fulfilled for the
  measure to be calculated. If the calculation condition is not met, the measure
  is excluded from the calculation.

- qAttributeExpressions: List of attribute expressions.

- qAttributeDimensions: List of attribute dimensions.

## Referencing predefined measures

You can use measures that are predefined in the app. You must know the
Measure ID, which is defined in the `qLibraryID` property. You must also state
that it is a measure in the `qType` property.

```json
{
  "qLibraryId":"eqZkF",
  "qType":"measure"
}
```
