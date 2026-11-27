---
title: "Setting conditions for alerts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Alerting/setting-conditions-for-alerts.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Using analytics to explore data", "Monitoring data with alerts"]
---

# Setting conditions for alerts

When you create a data alert, you can set up multiple conditions that need to be fulfilled to trigger the alert. Each condition compares one of the [measures](#glossary-0 "Glossary term") or [dimensions](#glossary-1 "Glossary term") in the alert with a value, a measure or the current set. You can combine multiple conditions with AND and OR. You can also create multi-step conditions by grouping conditions and applying them in order.

For more information about alerts, see [*Monitoring data with alerts*](monitoring-changes-with-alerts.htm).

In the condition you can compare the value with:

- Another value that can be fixed, or calculated by an expression.
- Another measure.
- An [aggregation](#glossary-2 "Glossary term") of the current data set.
- The last evaluation of the alert.

When you compare you can use an offset, a value that you want to offset the returned value by. For more information, see [*Using an offset when comparing*](#Using).

## Comparing with a value

You can compare a measure or dimension value with a value that can be fixed, or calculated by an expression.

- Select Value in Compare with.

Information noteThe expression is calculated at the alert evaluation level. This means that it will not be calculated by the dimension that you used to split up the measure in Show by dimension.

## Comparing with another measure

You can compare a measure or dimension value with the value of another measure used in the alert.

- Select Measure in Compare with.

You can define an offset, a value that you want to offset the returned value by. This can be either a number or a percentage. For more information, see [*Using an offset when comparing*](#Using).

## Comparing with the current set

You can compare a measure value with an aggregation of the current data set. You cannot compare a dimension with the current set.

- Select Set (advanced) in Compare with.

The following aggregations are available:

- Average

  This compares the measure with the average of the values in the current data set.

  You can define an offset. This is a value that you want to offset the returned value by. This can be either a number or a percentage.
- Min

  This compares the measure with the minimum of the values in the current data set.

  You can define an offset. This is a value that you want to offset the returned value by. This can be either a number or a percentage.
- Max

  This compares the measure with the maximum of the values in the current data set.

  You can define an offset. This is a value that you want to offset the returned value by. This can be either a number or a percentage.
- Percentile

  This compares the measure with the value of a selected percentile value in the current data set.

  For example, if you select Operator: Greater than and Percentile: 90, the comparison is if the measure is greater than the 90th percentile value of the measure set.
- Standard deviation

  This compares the measure with the boundary of a multiple of standard deviations from the mean of the current data set. Use a positive number to compare with the upper boundary, and a negative number to compare with the lower boundary.

  For example, if you select Operator: Greater than and Standard deviation: 1.5, the comparison is if the measure value is greater than the boundary value of 1.5 standard deviations from the mean of the data set.

You can define an offset, a value that you want to offset the returned value by. This can be either a number or a percentage. For more information, see [*Using an offset when comparing*](#Using).

## Comparing with the last evaluation of the alert

You can compare a measure value or a dimension with the same value in the last evaluation of the alert with Last evaluation in Compare with. If you refined the alert using a dimension, the values for each dimension are compared with the same value for the last evaluation.

You can use an offset to find values that had a big change since the last evaluation. The offset can be either a number or a percentage. For more information, see [*Using an offset when comparing*](#Using).

Information noteFor data alerts with last evaluation conditions, the evaluation history is deleted when:

- Ownership of the alert is changed in the Administration activity center.
- Section access is added or removed for the application in data load editor.

Example: Excluding values that have not changed

If you have an alert set for the sum of sales exceeding 100, the alert will continue to trigger on coming evaluations even if the sum of sales value has not changed.

If you only want to get alerts for when something has changed, you can add a second condition to the alert:

- Measure or dimension: The same measure that you use in the condition comparing the value.
- Compare with: Last evaluation
- Operator: Not equal to

The alert will trigger when the sum of sales exceeds 100. On coming evaluations, it will not trigger until the value has changed to another value exceeding 100.

Example: Significantly changed values since the last evaluation

You want to create an alert that triggers when the price of a stock jumps significantly compared with the last evaluation.

1. Create an alert using the stock price as measure.
2. Split up the measure by the stock name as a dimension. You can do this in Show by dimension.
3. Add a condition with the following settings:

   - Measure or dimension: The stock price.
   - Compare with: Last evaluation
   - Operator: Greater than
   - Offset: 10
   - Offset as percentage: Checked

The alert will trigger when one or more stocks jump by more than 10 % in price since the last evaluation, and show the name and the price of these stocks.

## Using an offset when comparing

You can define an offset. An offset is a value that you want to offset the returned value by when you compare with a measure or the current set. This can be an absolute value, a calculated value, or a percentage. You can use this to set a threshold to trigger the alert.

Example:

You may want a threshold of 10% when you compare your sales with the average sales of the current set. The alert should trigger only if the sales are 10% greater than the average sales. In this case you would use the following settings in the condition:

- Operator: Greater than
- Compare with: Current set
- Aggregation: Average
- Offset: 10
- Offset as percentage: Checked

## Multi-step conditions

You can group conditions and apply each group of conditions in order. This allows you to filter by a measure value before looking for outlier values.

- Use the Ungroup (![Ungroup](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_link_outline.svg)) button to split the conditions in two groups.
- Use the Group (![Group](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_unlink_outline.svg)) button to merge two groups to one group.
- Use Then to specify that the next condition group is evaluated only for values that are true from the first condition group. You need at least two groups to use Then.

Example:

You have a [visualization](#glossary-3 "Glossary term") that shows sales and gross margin for a number of stores. You want to see the worst performing 10% of stores in terms of gross margin %. Additionally, you only want to see the results from stores with sales over $50,000.

For a visual demo about multi-step conditions, see [Creating an alert with multi-step conditions](https://share.vidyard.com/watch/qB49morBxTa5beEhAPPqUx?).

1. Create an alert and add the measures for sales and gross margin.
2. Create a condition using the sales measure.

   - Operator: Greater than
   - Compare with: Value
   - Value: 50000
3. Create another condition using the gross margin measure. This should be placed after the condition already created.

   - Operator: Less than
   - Compare with: Current set
   - Aggregation: Percentile
   - Percentile: 10
4. Click the ![Ungroup](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_link_outline.svg) button between the two conditions.

   The conditions are now in separate groups.
5. Select Then.

The alert will now first find stores with sales greater than $50,000. Then it will evaluate to find the 10% of these stores with lowest gross margin.

## Supported operators

When you compare the values, you can use the following operators:

- Greater than (numeric)
- Less than (numeric)
- Equal to (numeric and text)
- Not equal to (numeric and text)
- Includes (text)
- Starts with (text)
- Ends with (text)
