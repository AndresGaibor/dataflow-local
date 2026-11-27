---
title: "Array functions"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Lakehouse/TransformationFunctions/array/array.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to Qlik Open Lakehouse", "Creating a Qlik Open Lakehouse project", "Transformation functions"]
---

# Array functions

Array functions operate on multiple values stored in an array to process, transform, or analyze the data and return a result.

The following functions are available in Qlik Open Lakehouse:

| Function | Description |
| --- | --- |
| [ARRAY\_DISTINCT](array_distinct.htm) | Return all the distinct elements in the array. |
| [ARRAY\_JOIN](array_join.htm) | This function concatenates the elements of the given array to a string using the separator. |
| [ARRAY\_MAX](array_max.htm) | Return the maximum value in an array. |
| [ARRAY\_MIN](array_min.htm) | Return the minimum value in an array. |
| [ARRAY\_SORT](array_sort.htm) | Returns the values in the array in ascending order |
| [ARRAY\_SORT\_DESC](array_sort_desc.htm) | Returns the values in the array in descending order |
| [ARRAY\_SUM](array_sum.htm) | This function calculates the sum of all non-null elements of the input. If there are no non-null elements, returns 0. The behavior is similar to aggregate function SUM, but operates on an array. |
| [COUNT\_VALUES](count_values.htm) | Returns the amount of non-null items in a given array. |
| [COUNT\_VALUES\_IF](count_values_if.htm) | Returns the amount of `true` values in a given array. This can be used with conditional operators to count the number of array elements that fulfil a condition. For example, `COUNT\_VALUES\_IF(my\_values[] > 3)` will return the number of elements that are greater than 3. |
| [ELEMENT\_AT](element_at.htm) | This function returns an element of an array at a given index. If index >= 0, this function provides the same functionality as the SQL-standard subscript operator ([]). If index < 0, `ELEMENT\_AT` accesses elements from the last to the first. |
| [FIRST\_ELEMENT](first_element.htm) | Returns the first element in the array. |
| [LAST\_ELEMENT](last_element.htm) | Returns the last element in the array. |
| [VALUE\_INDEX\_IN\_ARRAY](value_index_in_array.htm) | Calculates a 1-based positional index for each non-null value within a sub-array, resetting the index with each new sub-array. |
| [VALUE\_INDEX\_IN\_ROW](value_index_in_row.htm) | Calculates a continuous, 1-based positional index for each value in an array, treating the entire row as a single context. It assigns a unique index to each non-null element across the arrays within the row. |
