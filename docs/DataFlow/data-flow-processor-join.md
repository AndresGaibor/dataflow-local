---
title: "Join processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataFlow/data-flow-processor-join.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Data flow", "Data flow processors"]
---

# Join processor

Combines two flows based on one or more keys.

The Join processor allows you to combine data from two output flows. Choose a common key, select the type of join, and combine the data in the output flow.

## Usage

The Join processor requires two input flows and can generate only one output flow.

## Properties

Properties to configure in order to combine your records using Join.

Configuration

| Property | Configuration |
| --- | --- |
| Join type | Select the desired join type in the list:   - Inner join: use this join type to compare two inputs that have matching field values and list all the resulting pairs. Values that do not match each other are being ignored in the result set. - Left outer join: use this option to retain all values of the left dataset in the joined output list. Values that do not match any rows in the right dataset will be listed in the result set as NULL. - Right outer join: use this option to retain all values of the right dataset in the joined output list. Values that do not match any rows in the left dataset will be listed in the result set as NULL. - Full outer join: use this option to combine both left and right outer joins. Every value that has no matching value will be listed in the result set as NULL. |
| Conditions | - Left key: Select or enter the field in the left dataset. Auto-completion is available while typing. - Right key: Select or enter the field in the right dataset. Auto-completion is available while typing. |

To rename the processor or edit its description, point your mouse over the name or description to change in the Properties panel and click the ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit icon.

## Additional information about join operations

The Join processor allows you to apply four different types of join operations to your data.

### Inner join

This type of join operation is used to:

- match the values that are common between two datasets.
- create a result set with all the pairs that match.

![Graphical representation of an inner join.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/inner_join.png)

The result set is determined as follows:

| If the join statement is satisfied (dataset L matches dataset R) | If the join statement is not satisfied |
| --- | --- |
| All matching records are combined and returned in the result set. | Non-matching records are ignored. |

### Left outer join

This type of join operation is used to:

- match the values that are common between two datasets AND retain all the values that exists in the left dataset.
- create a result set combining these records.

![Graphical representation of a left outer join.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/left_outer_join.png)

The result set is determined as follows:

| If the join statement is satisfied (everything that is in dataset L + matches in the two datasets) | If the join statement is not satisfied |
| --- | --- |
| All records in the left dataset as well as the matching records between dataset left and dataset right are combined and returned in the result set. | Non-matching records are ignored. |

### Right outer join

This type of join operation is used to:

- match the values that are common between two datasets AND retain all the values that exists in the right dataset.
- create a result set combining these records.

![Graphical representation of a right outer join.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/right_outer_join.png)

The result set is determined as follows:

| If the join statement is satisfied (everything that is in dataset L and R + matches in the two datasets) | If the join statement is not satisfied |
| --- | --- |
| All records in the left dataset as well as the matching records between dataset left and dataset right are combined and returned in the result set. | Non-matching records are ignored. |

### Full outer join

This type of join operation is used to:

- retain all the values that match in the left and right datasets.
- create a result set combining these records.

![Graphical representation of a full outer join.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/full_outer_join.png)

The result set is determined as follows:

| If the join statement is satisfied (everything that is in dataset L + matches in the two datasets) | If the join statement is not satisfied |
| --- | --- |
| All records in the left dataset as well as the matching records between dataset left and dataset right are combined and returned in the result set. | Non-matching records will be listed in the result set as NULL. |
