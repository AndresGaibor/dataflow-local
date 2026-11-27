---
title: "Filter processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Transformation/Processor-filter.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to a data warehouse", "Transforming data", "Adding transformation flows"]
---

# Filter processor

Filters columns based on one or multiple conditions, splits them, and passes the separated data to the next step of the flow.

The Filter processor uses different operators to filter on the values of your columns in a transformation flow.

## Filter properties

Properties to filter on the values of your columns.

Configuration

| Property | Configuration |
| --- | --- |
| Filters | - Input: Select the column to apply a filter on.- Optionally select a function to apply: If needed, select the operation you want to apply while filtering the selected column:  - None: Does not apply any functions while filtering. - To absolute value: Calculates the absolute value for all the numeric values in the column. - To lower: Converts all the text in the column to lower case. - To upper case: Converts all the text in the column to upper case. - First character to lower case: Puts the first letter of every word in the column to lower case. - First character to upper case: Puts the first letter of every word in the column to upper case. - Length: Extracts the number of digits from a value in the column.  - Operator: Select the operator that will be used to filter the selected column. - Value: Type in the value of the selected column. |
| Select rows that match | In case you have defined multiple filters, select the type of matching to apply to the rows to be filtered: All, Any or None.  Example: You have defined the two following filter criteria: age > 18 and name Contains Tom:   - If you select All, all the 18-year olds named Tom or with a name containing Tom (Tommy for example) will be returned.- If you select Any, all the 18-year olds and all the people named Tom or with a name containing Tom will be returned.   - If you select None, all the less-than-18 years old that are not named Tom or with a name not containing Tom will be returned. |

To rename the processor, click the ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/processor-select-columns-edit_26x24.png)Edit icon that is displayed when hovering over the default name of the processor.

To edit its description, click the ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/processor-select-columns-edit_26x24.png)Edit icon that is displayed when hovering over Description.
