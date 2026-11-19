---
source: https://qlik.dev/embed/capability-api/customize/dimensions-and-measures/sorting/
last_updated: 2025-07-03T16:05:11+02:00
---

# Sort dimensions and rows

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik/api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

You can set the internal sort order for dimensions and rows. This is defined in
the column definition.

## Default sorting

By default (if `"autoSort": true`), the dimensions and rows are sorted in the
order they are defined in the columns. Each dimension is sorted internally in
the most common way for that type of data. Numbers are sorted numerically,
ascending. Text is sorted alphabetically, ascending.

Default sorting method by chart type

| Qlik Sense native chart | Default sorting                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ----------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bar chart               | By default, a bar chart with one measure and one dimension is presented with vertical bars sorted descending on the measure. When a dimension has less than 10 values, the sorting is by dimension, alphabetically. You sort the dimensions individually of each other.  > **Note:** In bar charts with multiple dimensions, sorting is locked to the first dimension. This dimension is what groups and stacks are based on, and sorting on a different dimension or a measure would break up these groups in an undesirable way. If you still want to sort by the measure value, try using the option Sort by expression on the first dimension. |
| Box plot                | By default, a box plot is sorted by the center line. You can also sort by first whisker, box start, box end or last whisker.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Combo chart             | Sorted by the first item added, either the dimension or the measure.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Distribution plot       | By default, a distribution plot is sorted by the outer dimension.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Gauge                   | A gauge only uses a single measure value, the first one under Measures.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Histogram               | The histogram does not have any sorting section.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| KPI                     | By default, the first added measure becomes the main value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Line chart              | By default, a line chart is sorted by the dimension.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Listbox                 | By default, a list box is sorted in ascending order.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Pie chart               | A pie chart uses one measure and one dimension. By default, a pie chart is sorted by the measure in descending order.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| Pivot table             | A pivot table is sorted by the first dimension in the rows section (vertical).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| Scatter plot            | The scatter plot does not have any sorting section, but the order of the measures decides where they are used. The first measure is used on the x-axis, the second measure is used on the y-axis, and the third (optional) measure is used for the bubble size (it is used to set the color on large data sets) in the scatter plot. You can only have one dimension in a scatter plot.                                                                                                                                                                                                                                                            |
| Table                   | By default, the column presents the dimensions and measures in the order they were added. Sorting order of rows: By default, the table is sorted in ascending order by the first dimension or measure.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Treemap                 | The treemap does not have any sorting section. The sorting is automatically by measure size.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| Waterfall chart         | -                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

## Sorting dimensions

Sorting on the dimensions are defined in the `qSortCriterias` object.

### The qSortCriterias object

The `qSortCriterias` object defines the sorting criteria in the field and should
be defined if `"autoSort": false`. If auto-sorting has been turned off and
`qSortCriterias` is not defined, the visualization is by default sorted
alphabetically ascending. The `qSortCriterias` object consists of the following properties:

- qSortByState

  Sorts the field values according to their logical state (selected, optional,
  alternative, or excluded). Can be one of:

  - `-1` for sorting descending
  - `0` for no sorting
  - `1` for sorting ascending

- qSortByFrequency

  Sorts the field values by frequency (number of occurrences in the field). Can be
  one of:

  - `-1` for sorting ascending
  - `0` for no sorting
  - `1` for sorting descending

- qSortByNumeric

  Sorts the field values by numeric value. Can be one of:

  - `-1` for sorting descending
  - `0` for no sorting
  - `1` for sorting ascending

- qSortByAscii

  Sorts the field by alphabetical order. Can be one of:

  - `-1` for sorting descending
  - `0` for no sorting
  - `1` for sorting ascending

- qSortByLoadOrder

  Sorts the field values by the initial load order. Can be one of:

  - `-1` for sorting descending
  - `0` for no sorting
  - `1` for sorting ascending

- qSortByExpression

  Sorts the field by an expression, defined in `qExpression`. Can be one of:

  - `-1` for sorting descending
  - `0` for no sorting
  - `1` for sorting ascending

- qSExpression

  The expression definition when sorting by expression.

  `"qv": "<expression>"` where `<expression>` is a string.

  Example:

  ```json
  {
    "qSortByExpression": 1,
    "qExpression": {
      "qv": "NetScoreDiff"
    }
  }
  ```

## Sorting measures

Sorting on the measures are defined in the `qSortBy` object.

### The qSortBy object

The `qSortBy` object defines the sorting criteria in the field and should be
defined if `"autoSort": false`. If auto-sorting has been turned off and `qSortBy`
is not defined, the visualization is by default sorted alphabetically ascending.
The `qSortBy` object consists of the following properties:

- qSortByState

  Sorts the field values according to their logical state (selected, optional,
  alternative, or excluded). Can be one of:

  - `-1` for sorting descending
  - `0` for no sorting
  - `1` for sorting ascending

- qSortByFrequency

  Sorts the field values by frequency (number of occurrences in the field). Can be
  one of:

  - `-1` for sorting ascending
  - `0` for no sorting
  - `1` for sorting descending

- qSortByNumeric

  Sorts the field values by numeric value. Can be one of:

  - `-1` for sorting descending
  - `0` for no sorting
  - `1` for sorting ascending

- qSortByAscii

  Sorts the field by alphabetical order. Can be one of:

  - `-1` for sorting descending
  - `0` for no sorting
  - `1` for sorting ascending

- qSortByLoadOrder

  Sorts the field values by the initial load order. Can be one of:

  - `-1` for sorting descending
  - `0` for no sorting
  - `1` for sorting ascending

- qSortByExpression

  Sorts the field by an expression, defined in `qExpression`. Can be one of:

  - `-1` for sorting descending
  - `0` for no sorting
  - `1` for sorting ascending

- qExpression

  The expression definition when sorting by expression.

  `"qv": "<expression>"` where `<expression>` is a string.

  Example:

  ```json
  {
    "qSortByExpression": 1,
    "qExpression": {
      "qv": "NetScoreDiff"
    }
  }
  ```

## Inter column sort order

You can define the sort order of the columns in the hypercube. This is done in
`qInterColumnSortOrder` that resides in the `qHyperCubeDef`.

Column numbers are separated by a comma. `"qInterColumnSortOrder": [ 1, 0, 2 ]`
means that the first column to be sorted should be column 1, followed by
column 0 and column 2.

Example:

```json
"qHyperCubeDef": {
  "qInterColumnSortOrder": [
    1,
    0
  ]
}
```

## Sorting examples

This section shows some common sorting examples.

### Sorting by frequency

This example sorts the field values by frequency, that is number of occurrences
in the field, ascending order.

```json
{
  "qDef": {
    "qFieldDefs": [
      "NetScoreName"
    ],
    "qSortCriterias": [
      {
        "qSortByFrequency": 1
      }
    ],
    "autoSort": false
  }
}
```

### Sorting by numeric values

This example sorts the field values by numeric value, ascending order.

```json
{
  "qDef": {
    "qDef": "Count(NetScoreName)",
    "autoSort": false
  },
  "qSortBy": {
    "qSortByNumeric": -1
  }
}
```

### Sorting alphabetically

This example sorts the field by alphabetical, ascending order.

```json
{
  "qDef": {
    "qFieldDefs": [
      "NetScoreName"
    ],
    "qSortCriterias": [
      {
        "qSortByAscii": 1
      }
    ],
    "autoSort": false
  }
}
```

### Sorting by expression

This example sorts the field values by an expression, ascending order.

```json
{
  "qDef": {
    "qFieldDefs": [
      "NetScoreName"
    ],
    "qSortCriterias": [
      {
        "qSortByExpression": 1,
        "qExpression": {
          "qv": "NetScoreDiff"
        }
      }
    ],
    "autoSort": false
  }
}
```

### Sorting by load order

This example sorts the field values by initial load order.

```json
{
  "qDef": {
    "qFieldDefs": [
      "NetScoreName"
    ],
    "qSortCriterias": [
      {
        "qSortByLoadOrder": 1
      }
    ],
    "autoSort": false
  }
}
```
