---
source: https://qlik.dev/embed/foundational-knowledge/visualizations/table/
last_updated: 2025-10-31T14:06:52+01:00
---

# Table

> **Note:** The straight table has replaced the table as the default table visualization.
> Consider upgrading existing tables to straight tables for improved capabilities
> and performance. For information about the straight table, see [straight table](embed/foundational-knowledge/visualizations/straight-table).

The table shows several fields simultaneously, where the content of each row is
logically connected. Typically, a table consists of one dimension and several measures.

You can use a table when you want to view precise values rather than
visualizations of values, and when you want to compare individual values.
A table is particularly useful when drill-down groups are used as a dimension.

You only make selections in the dimension columns. All dimension columns have a
search icon in the header.

## Number of columns (dimensions and measures)

In a table, you can have millions of rows and virtually any number of columns
with dimensions and measures. But because huge tables are impractical and hard
to manage, the limit for what is practical is far less than the theoretical
maximum. In most cases, it is desirable to see all the columns without scrolling
horizontally.

## Default settings for a table

Most native Qlik Sense chart types are automatically sorted on the dimension content:

- Numeric content is numerically sorted.
- Categorical content is alphabetically sorted.

## Data alignment

If Text alignment is set to Auto, column data is aligned according to data
text values are left-aligned and number values, including date related values,
are right-aligned. If you set it to Custom, you can select to align the data to
the left or to the right.

## Sorting

You can adjust both the order of the dimensions and measures from left to right
(column sorting), and the sorting priority order of the rows (row sorting).
In addition, you also have an internal sorting option.

During analysis, you can also use interactive sorting to change the row sorting.

### Column sorting

By default, the order in which columns are sorted is set by the order in which
dimensions and measures are added to the table. If you add the measure Sales
first, it is presented first (leftmost) in the table. The next dimension or
measure that is added is presented in the second column, and so forth. The column
sorting order can be changed in the properties.

### Row sorting

By default, rows are sorted by the first added dimension or measure, numeric
values descending, text values ascending. A small arrow under the column header
shows by which column the table is sorted.

You can change the row sorting in the properties panel, under Sorting. Drag the
dimensions and measures to change the sorting priority order. In many cases,
sorting is not only affected by the first dimension or measure in Sorting, but
also the following ones.

### Internal sorting

Each dimension and measure has a default (Auto) internal sorting order, which
can be changed. Under Sorting, click the item you want to change and click the
button to switch to Custom sorting. Changes made to the internal sorting of an
item may not have any effect if the sorting is in conflict with an item with
higher priority.

### Interactive sorting

During analysis, you can set which column to sort on by clicking the column
header. The first click sorts the table according to the default sorting of the
selected item. A second click reverses the sorting order. Interactive sorting
is session based and is not saved. If you want your changes to the sorting to be
persistent, you need to make the changes in the properties panel.

## Column picker

When space is limited and not all dimensions and measures can be displayed in a
table, the column picker appears on the right in the table. When you click the
column picker, a list is displayed with all dimensions and measures in the table.
You can temporarily change the order of the columns by dragging them in the list,
and you can make selections in all displayed dimensions, as usual.

The order changes that you make in the column picker are not permanent and
do not the affect the column order or the sorting order set in the properties.

## Totals

By default, the totals of numeric values are displayed under the column names.
In the properties panel, you can change this to display the totals at the bottom
of a column, or not at all.

## Search

The usual search options are available when you want to perform a search in a table.

You can use the following options:

- Text search
- Numeric search
- Expression search
- Fuzzy search
