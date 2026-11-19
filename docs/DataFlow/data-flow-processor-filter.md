---
title: "Filter processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataFlow/data-flow-processor-filter.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Data flow", "Data flow processors"]
---
# Filter processor

Filters data based on conditions.

The **Filter** processor allows you to filter input data based on one or more conditions set by operators. You can also split the result between two output flows, for matching and non-matching rows.

## Usage

- The **Filter** processor requires one input flow and can generate up to two output flows: one for data that matches your filters, and one for data that does not match.
- When using operators (=, <, >, etc.) to compare two fields containing `null` values, all rows are considered non-matching rows and will be available in the second output of the **Filter** processor.
- Click the **+** icon in the processor configuration panel to create more than one filter.

## Properties

Properties to filter on the values of your fields.

Configuration

| Property | Configuration |
| --- | --- |
| **Filters** | - **Field to process**: Select the field to apply a filter on. - **Apply a function**: Optionally, select the operation you want to apply while filtering the selected field:    - **None**: Does not apply any functions while filtering.   - **To absolute value**: Calculates the absolute value for all the numeric values in the field.   - **To lower case**: Converts all the text in the field to lower case.   - **To upper case**: Converts all the text in the field to upper case.   - **First character to lower case**: Puts the first letter of every word in the field to lower case.   - **First character to upper case**: Puts the first letter of every word in the field to upper case.   - **Length**: Extracts the number of digits from a value in the field. - **Operator**: Select the operator that will be used to filter the selected field:    - = equals   - <> is not equal   - < is lower than   - <= is lower than or equals   - > is greater than   - >= is greater than or equals   - Contains   - Does not contain   - Is null   - Is not null   - Is empty   - Is not empty   - Matches wildcard   - Does not match wildcard   - Matches regex   - Does not match regex - **Use with**:    - **Value**: Select this option to compare the field to process with the custom value of your choice, set in the **Value** field.   - **Field**: Select this option to compare the field to process with another field from the drop-down list. |
| **Select rows that match** | In case you have defined multiple filters, select the type of matching to apply to the rows to be filtered:   - **All filters**: returns rows that match filter A **and** filter B. - **Any filter**: returns rows that match filter A **or** filter B. - **None of the filters**: returns rows that do not match filter A or B. |

To rename the processor or edit its description, point your mouse over the name or description to change in the **Properties** panel and click the ![Edit](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) **Edit** icon.

## Example

The data used as source in this example contains customer information such as names, age groups, and occupation.

![dataset with customer information for the filtering scenario](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/filter_example_1.png)

Let's say you want to focus on a specific demographic group for your analytics, namely customers from the 18-24 range, and unemployed. You can use the **Filter** processors to isolate the corresponding data before using it.

In the processor properties, for your first filter, select **Occupation** as field to process, **=** as operator and Unemployed as value to look for. Click the + icon to create another filter, this time for the **Age** field with a value equal to 18-24.

At the bottom of the processor configuration panel, in the **Select rows that match** list, you can choose from three different options:

- If you select **All filters**, all the unemployed customers from the 18-24 age group will be returned.
- If you select **Any filter**, all the unemployed customers and all the people from the 18-24 age group will be returned.
- If you select **None of the filters**, all the customers that are not unemployed or from the 18-24 age group will be returned.

In this example, **All filters** is selected.

![data flow to filter on age and employment](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/filter_example_2.png)

When running this data flow, all the matching rows will be sent to a specific target file, while the rest will be sent to another target.
