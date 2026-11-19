---
source: https://qlik.dev/embed/foundational-knowledge/visualizations/boxplot/
last_updated: 2025-08-04T14:23:38+02:00
---

# Box plot

The box plot is suitable for comparing range and distribution for groups of
numerical data, illustrated by a box with whiskers, and a center line in the
middle. The whiskers represent high and low reference values for excluding
outlier values. You can define the box start and end points, and whiskers ranges
with a few different presets, or define your own settings using expressions.

## Number of columns (dimensions and measures)

In a box plot you need to use one or two dimensions, and one measure. If you
use a single dimension you will receive a single box visualization. If you use
two dimensions, you will get one box for each value of the second, or outer, dimension.

## Default settings for a box plot

Most native Qlik Sense chart types are automatically sorted on the dimension content:

- Numeric content is numerically sorted.
- Categorical content is alphabetically sorted.

## Box plot elements

You can use one of the three presets to define your box plot. These are defined
in the **calculations** object.

- Standard (Tukey)

  This preset is based on the original box plot definition by J. Tukey. The
  center line represents the median (second quartile), and the box start and
  end points represent the first and third quartiles. Whisker length can be
  set to `1`, `1.5` or `2` inter-quartile ranges. An inter-quartile range represents
  the distance between two adjacent quartiles, for example, the first and the
  second quartiles.

  `"mode": "tukey"`

  The whisker length is set in `"parameters": {"tukey": 1.5}`, where the number
  indicates the whisker length:

  - 1: 1 interquartile range
  - 1.5: 1.5 interquartile range
  - 2: 2 interquartile ranges

- Percentile-based

  This preset is also defined with the box start and end points representing the
  first and third quartiles, and the center line representing the median, but
  the whisker length is adjusted by setting a percentile based whisker position.

  `"mode": "fractiles"`

  The whisker length is set in `"parameters": {"fractiles": 0.01}`, where the
  number indicates the whisker length:

  - **0**: Min/max. This setting sets the whisker start and end points to the
    minimum and maximum values.
  - **0.01**: first/ninety-ninth percentile
  - **0.05**: fifth/ninety-fifth percentile
  - **0.1**: tenth/ninetieth percentile

- Standard deviation

  This preset is based on standard deviations, with the center line representing
  the average value, and the box start and end points representing one standard
  deviation variance. You can set the whisker length to a multiple of standard deviations.

  `"mode": "stdDev"`

  The whisker length is set in `"parameters": {"stdDev": 3}`, where the number
  indicates the whisker length:

  - **2**: one standard deviation
  - **3**: two standard deviations
  - **4**: three standard deviations

You can also define a custom box plot where you set the value of each box plot
element using an expression.
