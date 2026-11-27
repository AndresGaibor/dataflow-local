---
title: "Incremental filter processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Transformation/Processor-incremental-filter.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to a data warehouse", "Transforming data", "Adding transformation flows"]
---

# Incremental filter processor

Filters data incrementally to only load recent updates or additions using change detection.

The Incremental filter processor allows you to filter your columns on data changes using either the high watermark method or a time-based method in a transformation flow.

Information noteThis processor is available only if you have selected Materialized and Incremental load when creating your transformation flow.

## Filter properties

Properties to filter on data changes incrementally.

Configuration

| Property | Configuration |
| --- | --- |
| Change detection | In the list, select the change detection method you want to use to filter on data changes.  For more information, see [*Change detection*](../Onboarding/Registering-data.htm#Change). |
| High watermark | If you select this change detection method, select the Input column as well as the column to be compared with, the Target watermark column . |
| Time-based | If you select this change detection method, select the Input column and a specific timestamp in Last to detect changes made to this column since the selected time. |

To rename the processor, click the ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/processor-select-columns-edit_26x24.png)Edit icon that is displayed when hovering over the default name of the processor.

To edit its description, click the ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/processor-select-columns-edit_26x24.png)Edit icon that is displayed when hovering over Description.
