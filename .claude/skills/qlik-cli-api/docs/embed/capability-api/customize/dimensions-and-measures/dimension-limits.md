---
source: https://qlik.dev/embed/capability-api/customize/dimensions-and-measures/dimension-limits/
last_updated: 2026-03-18T16:49:43Z
---

# Apply dimension limits

> **Note:** Where possible, use [qlik-embed](https://qlik.dev/embed/qlik-embed/) and [qlik-api](https://qlik.dev/toolkits/qlik-api) rather than this framework.

Dimension limits is defined in the `qOtherTotalSpec` object and specifies if some
values, grouped as Others, should be grouped together in the visualization.
This limits the number of displayed values and when such limitation is set,
the only dimensions displayed are those where the measure value meets the
limitation criterion.

- Fixed number: Select to display the top or bottom values. Set the number of
  values. You can also use an expression to set the number.

- Exact value: Use the operators and set the exact limit value. You can also
  use an expression to set the number.

- Relative value: Use the operators and set the relative limit value in percent.
  You can also use an expression to set the number.

## The qOtherTotalSpec object

Dimension limits are set in the `qOtherTotalSpec` object. The object resides
inside the dimension definition which means that each dimension of a hypercube
has its own configuration.

```json
"qOtherTotalSpec": {
     "qOtherMode": "OTHER_COUNTED",
     "qOtherCounted": {
       "qv": "6"
     },
     "qOtherLimit": {
       "qv": "0"
     },
     "qOtherLimitMode": "OTHER_GE_LIMIT",
     "qOtherSortMode": "OTHER_SORT_DESCENDING",
     "qTotalMode": "TOTAL_OFF"
   }
```

Example: `qOtherTotalSpec` formatted to limit on the top 6 values
(including others) of the first measure

<details>
  <summary>qOtherMode</summary>

Sets the dimension limit mode to be used.

- `OTHER_OFF`: no limitation is applied to the dimension.
- `OTHER_COUNTED`: dimension limit set to display a fixed number defined in
`qOtherCounted`, calculated on the first measure.
- `OTHER_ABS_LIMITED`: dimension limit set to display an exact value defined in
`qOtherLimit`, calculated on the first measure.
- `OTHER_ABS_ACC_TARGET`: dimension limit set to display values that accumulate to
an absolute value. All rows up to the current row are accumulated and the result
is compared to the specified absolute value. The absolute value is defined in qOtherLimit.
- `OTHER_REL_LIMITED`: dimension limit set to display values based on a relative
value of the total of the first measure. The percentage is defined in `qOtherLimit`.
- `OTHER_REL_ACC_TARGET`: dimension limit set to display values that accumulate to
a percentage of the total. All rows up to the current row are accumulated and
the result is compared to the total of the dimension values. A percentage is
calculated and this percentage is compared to the specified percentage, defined
in `qOtherLimit`.

Default: `OTHER_OFF`
</details>

<details>
  <summary>qOtherCounted</summary>

Sets the number of values to display when `"qOtherMode": "OTHER_COUNTED"`. The
number of values can be entered as a string or as a calculated formula.

```json
"qOtherTotalSpec": {
  "qOtherMode": "OTHER_COUNTED",
  "qOtherCounted": {
    "qv": "Sum(3+2)"
  },
  "qOtherSortMode": "OTHER_SORT_DESCENDING"
}
```

`qOtherCounted` defined as an expression

</details>

<details>
  <summary>qOtherLimit</summary>

Sets the number of values to display when `"qOtherMode": "OTHER_ABS_LIMITED"`,
`"qOtherMode": "OTHER_REL_LIMITED", "qOtherMode": "OTHER_ABS_ACC_TARGET"` or
`"qOtherMode": "OTHER_REL_ACC_TARGET"`.

The number of values can be entered as a string or as a calculated formula.
Inequality relation is defined in qOtherLimitMode.
</details>

<details>
  <summary>qOtherLimitMode</summary>

Sets the inequality relation to the value of `qOtherLimit`. Use this parameter
when `"qOtherMode": "OTHER_ABS_LIMITED", "qOtherMode": "OTHER_REL_LIMITED"`,
`"qOtherMode": "OTHER_ABS_ACC_TARGET"` or `"qOtherMode": "OTHER_REL_ACC_TARGET"`.

Can be one of:

- `OTHER_GE_LIMIT`: include the values greater than or equal to what is defined in
`qOtherLimit`.
- `OTHER_LE_LIMIT`: include the values lower than or equal to what is defined in
`qOtherLimit`.
- `OTHER_GT_LIMIT`: include the values strictly greater than what is defined in `qOtherLimit`.
- `OTHER_LT_LIMIT`: include the values strictly lower than what is defined in `qOtherLimit`.

Default: `OTHER_GT_LIMIT`
</details>

<details>
  <summary>qSuppressOther</summary>

Set to `true` to omit the group Others as a dimension value.

Default: `false`
</details>

<details>
  <summary>qForceBadValueKeeping</summary>

Includes text values in the returned values. Use this parameter when
`"qOtherMode": "OTHER_ABS_LIMITED", "qOtherMode": "OTHER_REL_LIMITED"`,
`"qOtherMode": "OTHER_ABS_ACC_TARGET"` or `"qOtherMode": "OTHER_REL_ACC_TARGET"`
and when dimension values include non-numeric values.

Default: `true`
</details>

<details>
  <summary>qApplyEvenWhenPossiblyWrongResult</summary>

Allows the calculation of Others even if the Qlik associative engine detects
some potential mistakes.

Default: `true`
</details>

<details>
  <summary>qGlobalOtherGrouping</summary>

This parameter applies to inner dimensions. When set to `true`, the restrictions
are calculated on the selected dimension only. All previous dimensions are ignored.

Default: `false`
</details>

<details>
  <summary>qOtherCollapseInnerDimensions</summary>

If set to `true`, it collapses the inner dimensions (if any) in the group Others.

Default: `false`
</details>

<details>
  <summary>qOtherSortMode</summary>

Defines the sort order of the dimension values. Can be one of:

- `OTHER_SORT_DEFAULT`: sort by load order
- `OTHER_SORT_DESCENDING`: sort by descending values
- `OTHER_SORT_ASCENDING`: sort by ascending values

Default: `OTHER_SORT_DESCENDING`
</details>

<details>
  <summary>qTotalMode</summary>

Sets if the total of the dimension values should be included. Can be one of

- `TOTAL_OFF`: no total returned
- `TOTAL_EXPR`: include total

Default: `TOTAL_OFF`
</details>

<details>
  <summary>qReferencedExpression</summary>

This parameter applies when there are several measures.

Defines the measure to use for the calculation of `Others` for a specific dimension.
</details>

## Fixed number limitations

These examples helps you set numbers to display the top or bottom values. You
can also use an expression to set the number.

### Example: Fixed number, top 3, no others

In this example, you want to display only the top three results based on the
first measure. Therefore, set `"qOtherMode": "OTHER_COUNTED"` and then define
`"qOtherCounted": {"qv": "3"}`. If do not want to show an others value, set
`"qSuppressOther": true`.

> **Note:** If `qSuppressOther` is not defined, the last value in the visualization (colored gray), summarizes all the remaining
> values and the value counts as 1 in that setting. In this example, the third value would be `Others`.

Since you want to show the top (highest) three values, set `"qOtherSortMode":`
`"OTHER_SORT_DESCENDING"` to sort the values in descending order.

```json
"qOtherTotalSpec": {
  "qOtherMode": "OTHER_COUNTED",
  "qOtherCounted": {
    "qv": "3"
  },
  "qSuppressOther": true,
  "qOtherSortMode": "OTHER_SORT_DESCENDING"
}
```

### Example: Fixed number, top 3, show others labeled "Other venues"

The below examples are variants of the previous example, where one example include
others and another example shows the bottom three values.

The label for others are set in the `othersLabel` property inside the
NxInlineDimensionDef (`qDef`). In the `qOtherTotalSpec` object, set
`"qSuppressOther": false`, or omit it completely.

```json
{
  "qDef": {
    "qFieldDefs": [
      "City"
    ],
    "othersLabel": "Other venues"
  },
  "qOtherTotalSpec": {
    "qOtherMode": "OTHER_COUNTED",
    "qOtherCounted": {
      "qv": "3"
    },
    "qOtherSortMode": "OTHER_SORT_DESCENDING"
  }
}
```

### Example: Fixed number, bottom 3, no others

This example is a variant of the previous example, where you showed the bottom three
with no others.

Set `"qOtherSortMode": "OTHER_SORT_ASCENDING"` to change the sort order and show
the bottom three results.

```json
"qOtherTotalSpec": {
  "qOtherMode": "OTHER_COUNTED",
  "qOtherCounted": {
    "qv": "3"
  },
  "qSuppressOther": true,
  "qOtherSortMode": "OTHER_SORT_ASCENDING"
}
```

## Exact value limitations

These examples helps you use the operators and set exact limit values. You can
also use an expression to set the number.

### Example: Exact value set to greater or equal to 40000, no others

In this example, you'll display all venues with an attendance average higher
than or equal to 40,000.

Set `"qOtherMode": "OTHER_ABS_LIMITED"` to limit the dimension values to an
absolute value. Then define the actual value `"qOtherLimit": {"qv": "40000"}`.
Set `"qOtherLimitMode": "OTHER_GE_LIMIT"` to include the values greater than or
equal to what was defined in `qOtherLimit`.

If you do not want to show an others value, set `"qSuppressOther": true`.

> **Note:** If qSuppressOther is not defined, the last value in the
> visualization (colored gray), summarizes all the remaining values.

```json
"qOtherTotalSpec": {
  "qOtherMode": "OTHER_ABS_LIMITED",
  "qOtherLimit": {
    "qv": "40000"
  },
  "qOtherLimitMode": "OTHER_GE_LIMIT",
  "qSuppressOther": true
}
```

### Example: Exact value set to less than 40000, no others

This example is a variant of the previous example, where you displayed the venues
with an attendance average less than 40,000.

Set `"qOtherLimitMode": "OTHER_LT_LIMIT"` to include the values less than what
was defined in `qOtherCounted`.

```json
"qOtherTotalSpec": {
  "qOtherMode": "OTHER_ABS_LIMITED",
  "qOtherLimit": {
    "qv": "40000"
  },
  "qOtherLimitMode": "OTHER_LT_LIMIT",
  "qSuppressOther": true
}
```

## Relative value examples

These examples helps you use the operators and set relative limit values. You
can also use an expression to set the number.

### Example: Relative value set to greater than or equal to 12%, no others

In this example, you'll display all venues with an attendance average higher
than or equal to 12 per cent of the total.

Set `"qOtherMode": "OTHER_REL_LIMITED"` to limit the dimension values to a
relative value. Then define the actual value `"qOtherCounted": {"qv": "12%"}`.
Set `"qOtherLimitMode": "OTHER_GE_LIMIT"` to include the values greater than or
equal to what was defined in `qOtherCounted`.

If you do not want to show an others value, set `"qSuppressOther": true`.

```json
"qOtherTotalSpec": {
  "qOtherMode": "OTHER_REL_LIMITED",
  "qOtherLimit": {
    "qv": "12%"
  },
  "qOtherLimitMode": "OTHER_GE_LIMIT",
  "qSuppressOther": true,
  "qOtherSortMode": "OTHER_SORT_DESCENDING"
}
```

### Example: Relative value set to less than 11%, no others

In this example, you'll display all venues with an attendance average less
than 11 per cent of the total.

Set `"qOtherMode": "OTHER_REL_LIMITED"` to limit the dimension values to a
relative value. Then define the actual value `"qOtherCounted": {"qv": "11%"}`.
Set `"qOtherLimitMode": "OTHER_LT_LIMIT"` to include the values lower than what
was defined in `qOtherCounted`.

If you do not want to show an others value, set `"qSuppressOther": true`.

```json
"qOtherTotalSpec": {
  "qOtherMode": "OTHER_REL_LIMITED",
  "qOtherLimit": {
    "qv": "11%"
  },
  "qOtherLimitMode": "OTHER_LT_LIMIT",
  "qSuppressOther": true
  "qOtherSortMode": "OTHER_SORT_DESCENDING"
}
```
