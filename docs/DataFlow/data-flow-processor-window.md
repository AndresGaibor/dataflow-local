---
title: "Window processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataFlow/data-flow-processor-window.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Data flow", "Data flow processors"]
---
# Window processor

Performs calculations on specific data ranges.

The **Window** processor allows you to aggregate and perform calculations using values from multiple rows grouped in a range, and produce a value for each row separately.

## Usage

The **Window** processor requires one input flow and can generate only one output flow.

## Properties

Properties to configure to create windows aggregations.

Configuration

| Property | Configuration |
| --- | --- |
| **Operation** | Use the drop-down to select the operation to apply during the windowing process:   - **Sum**: Calculates the sum of the records in the selected range. - **Avg**: Calculate the average value of the records in the selected range. - **Count**: Retrieves the number of records in the selected range, including duplicates. - **Count distinct**: Retrieves the number of unique records in the selected range. - **Min**: Returns the smallest value of the selected range. - **Max**: Returns the largest value of the selected range. - **First**: Retrieves the value of the first record of the selected range. - **Last**: Retrieves the value of the last record of the selected range. - **Concatenate**: Combines the values into a single string separated by the **Delimiter** of your choice. - **Row number**: Assigns a row number to each value of the selected window. - **Rank**: Calculates the rank of the selected range compared to the other windows. |
| **Fields** | Use the check boxes to select the field or fields on which you want to apply the function. |
| **New field name** | Give a custom name to the output field or edit it. When more than one field was selected, a name is constructed using the field name, the operation and optional range. |
| **Partition by fields** | Use the check boxes to select the field or fields by which to partition. |
| **Start range** | Use the drop-down to select the end range of the partition:   - **Unlimited** - **Current row** - **Preceding** - **Following** |
| **End range** | Use the drop-down to select the end range of the partition:   - **Unlimited** - **Current row** - **Preceding.** Enter a number of rows to set the range of action of the function. - **Following.** Enter a number of rows to set the range of action of the function. |
| **Sort by** | Use the search field to find a field to sort by. Sorting is optional for all operations except for **Row number** and **Rank**. |
| **Sort order** | Select the sorting order between **Ascending** and **Descending**. |

To rename the processor or edit its description, point your mouse over the name or description to change in the **Properties** panel and click the ![Edit](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) **Edit** icon.

## Video summary

[Video: https://share.vidyard.com/watch/dviZjTMPzFGVZdiLr7gmAe]
