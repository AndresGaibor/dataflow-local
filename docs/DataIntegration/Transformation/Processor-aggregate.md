---
title: "Aggregate processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Transformation/Processor-aggregate.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to a data warehouse", "Transforming data", "Adding transformation flows"]
---

# Aggregate processor

Aggregates the incoming schema based on one or more columns and performs sets of operations.

The Aggregate processor groups the input flow by aggregation sets which values can be used for calculations in a transformation flow.

## Aggregate properties

Properties to configure to aggregate your records.

Configuration

| Category name | Property name | Configuration |
| --- | --- | --- |
| Group by | Column path | In the list, select the column you want to use for your aggregation sets. |
| Operations | Column path | Select the column on which you want to perform a calculation operation. |
| Operations | Operation | Select the operation you want to apply on your aggregation set: Average, Count, List, Maximum, Minimum, Sum. |
| Operations | Output column name (optional) | Enter a name for the generated output column. If left empty, the default generated column name will contain the name of the selected column with the name of the selected operation.  The expected format is the following:   - must begin with [A-Za-z\_] characters. - can only contain [A-Za-z0-9\_] characters.   Example: ASDasd123\_4564 |

To rename the processor, click the ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/processor-select-columns-edit_26x24.png)Edit icon that is displayed when hovering over the default name of the processor.

To edit its description, click the ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/processor-select-columns-edit_26x24.png)Edit icon that is displayed when hovering over Description.
