---
source: https://qlik.dev/embed/foundational-knowledge/visualizations/histogram/
last_updated: 2025-08-04T14:23:38+02:00
---

# Histogram

The histogram is suitable for visualizing distribution of numerical data over a
continuous interval, or a certain time period. The data is divided into bins,
and each bar in a histogram represents the tabulated frequency at each bin.

## Number of columns (dimensions and measures)

You can only apply a single dimension to a histogram. The dimension must be a
numerical field. Histograms do not need a measure, as the frequency of the
binned data is automatically calculated.

> **Note:** You cannot use a master dimension that was created using the expression editor, even if the resulting field is
> numeric.

## Default settings for a histogram

Most native Qlik Sense chart types are automatically sorted on the dimension content:

- Numeric content is numerically sorted.
- Categorical content is alphabetically sorted.
