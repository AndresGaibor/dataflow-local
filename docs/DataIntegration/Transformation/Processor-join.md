---
title: "Join processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Transformation/Processor-join.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to a data warehouse", "Transforming data", "Adding transformation flows"]
---

# Join processor

Transforms several existing datasets to a new set of combined records.

The Join processor maps, combines, and transforms hierarchical data by matching values that are common between two datasets.

## Join properties

Properties to configure to combine your records using Join. You can add as many keys as you want in the processor configuration..

Configuration

| Property | Configuration |
| --- | --- |
| Join type | Select the desired join type in the list:   - Inner join: Use this join type to compare two datasets that have matching column values and list all the resulting pairs. Values that do not match each other are being ignored in the result set. - Left outer join: Use this option to retain all values of the left dataset in the joined output list. Values that do not match any rows in the right dataset will be listed in the result set as NULL. - Right outer join: Use this option to combine left and right outer joins. Values that do not match any rows in the left dataset will be listed in the result set as NULL. - Full outer join: Use this option to combine both left and right outer joins. Every value that has no matching value will be listed in the result set as NULL. |
| Merge input records | Enable this option in order to even and group the hierarchical structure of both left and right datasets.  By default, if you do not enable this option, the left and right datasets will be output with the same structure they had before the join operation. |
| Conditions | - Left key: Select or enter the path to the existing record in the left dataset. Auto-completion is available while typing.- Right key: Select or enter the path to the existing record in the right dataset. Auto-completion is available while typing. |

To rename the processor, click the ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/processor-select-columns-edit_26x24.png) Edit icon that is displayed when hovering over the default name of the processor.

To edit its description, click the ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/processor-select-columns-edit_26x24.png) Edit icon that is displayed when hovering over Description.

## Additional information about join operations

The Join processor allows you to apply four different types of join operations to your hierarchical data. For more information and examples of join operations, see [*Join*](../../Scripting/ScriptPrefixes/Join.htm).

### Inner join

This type of join operation is used to:

- match the values that are common between two datasets.
- create a result set with all the pairs that match.

The result set is determined as follows:

- If the join statement is satisfied (dataset L matches dataset R), all matching records are combined and returned in the result set.
- If the join statement is not satisfied, non-matching records are ignored.

### Left outer join

This type of join operation is used to:

- match the values that are common between two datasets AND retain all the values that exists in the left dataset.
- create a result set combining these records.

The result set is determined as follows:

- If the join statement is satisfied (everything that is in dataset L + matches in the two datasets), all records in the left dataset as well as the matching records between dataset left and dataset right are combined and returned in the result set.
- If the join statement is not satisfied, non-matching records are ignored.

### Right outer join

This type of join operation is used to:

- match the values that are common between two datasets AND retain all the values that exists in the right dataset.
- create a result set combining these records.

The result set is determined as follows:

- If the join statement is (everything that is in dataset L and R + matches in the two datasets), all records in the right dataset as well as the matching records between dataset left and dataset right are combined and returned in the result set.
- If the join statement is not satisfied, non-matching records are ignored.

### Full outer join

This type of join operation is used to:

- retain all the values that match in the left and right datasets.
- create a result set combining these records.

The result set is determined as follows:

- If the join statement is (everything that is in dataset L and R + matches in the two datasets), all records in the left and right datasets as well as the matching records between them are combined and returned in the result set.
- If the join statement is not satisfied, non-matching records will be listed in the result set as NULL.
