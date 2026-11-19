---
source: https://qlik.dev/embed/capability-api/customize/dimensions-and-measures/columns/
last_updated: 2025-07-03T16:05:11+02:00
---

# Overview - Hypercube columns

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik-api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

When using the Visualization API, hypercubes are defined in the cols parameter.
The number of columns needed to be specified vary depending on the visualization
type. If too few columns are specified you will receive an incomplete
visualization error just as if the visualization was created in the Qlik Sense client.

There are three different ways of specifying the columns:

- As a string.
- As a NxDimension or NxMeasure structure:
  - Engine API: NxDimension
  - Engine API: NxMeasure
- As a reference to a predefined dimension or measure, a so-called master item.

The preceding three methods can be combined in the same `create` statement. You can
use a simple string syntax for one column, a more advanced object for another
and a predefined master measure for the third.

> **Note:** The order of the columns are not always important.
> For a basic bar chart with one dimension and one measure, the columns can be specified in any order.
> However, for a table it matters which order the columns are specified, since the order specified in the cols parameter
> is the order shown in the table.

## String syntax

If a string starts with `=`, it will be treated as a measure, otherwise it is
treated as a dimension.

```json
[
  "Case Owner Group",
  "=Avg([Case Duration Time])"
]
```

> **Note:** Using the string syntax is quite easy but at the same time there are some limitations.
> If you want to set labels or limit the data-set to only the top five values, you should use the object syntax instead.

## Object syntax

Use the object syntax if you want to set more options for your columns. If you.
for example, create a pivot table with labels, you should use qFieldLabels for
dimensions and qLabel for measures.

```json
[
   {
    "qDef": {
      "qFieldDefs": ["Case Owner Group"],
      "qFieldLabels": ["Group"]
    }
  },
  /*measure with label*/ 
  {
    "qDef": {
      "qDef": "=Avg([Case Duration Time])",
      "qLabel": "Avg Case Duration Time"
    }
  },
  /*measure with label*/
  {
    "qDef": {
      "qDef": "Sum( [Open Cases] )",
      "qLabel": "Open Cases"
    }
  }
]
```

You can limit the data set to only show the top five values using qOtherTotalSpec.

```json
[
  {
    "qDef": {
      "qFieldDefs": ["Case Owner Group"],
      "qFieldLabels": ["Group"]
    },
    "qOtherTotalSpec": {
      "qOtherMode": "OTHER_COUNTED",
      "qOtherCounted": "5"
    }
  }
  "=Avg([Case Duration Time])"
]
```

## Referencing predefined dimensions and measures

You can use dimensions and measures that are predefined in the app. This is
mostly relevant if the user should be able to select dimensions and measures from
lists. You must know the Dimension ID or the Measure ID, which is defined in the
qLibraryID property. You must also state if it is a measure or a dimension in
the qType property.

```json
[
  {
    "qLibraryId":"eqZjE",
    "qType":"measure"
  }
]
```
