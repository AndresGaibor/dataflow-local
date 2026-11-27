---
title: "Hash processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Transformation/Processor-hash.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to a data warehouse", "Transforming data", "Adding transformation flows"]
---

# Hash processor

Hides the original data by modifying it through hashing.

The Hash processor allows you to alter the value of your data in order to protect it in a transformation flow.

## Hash properties

Properties to configure to hash your data.

Configuration

| Property | Configuration |
| --- | --- |
| Function name | Hash data: Select this function to hash the content of a column using the SHA-256 algorithm. |
| Columns to process | Select the column or columns on which you want to apply a function in the list.  Information note If you want to apply the same function to multiple columns at once, clickOpen dialog icon to open a tree view that allows you to select multiple columns. |
| Create new column | Enable this option to create a new column after applying the function. If you do not enable this option, the existing column will be kept and modified. |
| Rename new column | Give a custom name to the newly created column. |

To rename the processor, click the ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/processor-select-columns-edit_26x24.png)Edit icon that is displayed when hovering over the default name of the processor.

To edit its description, click the ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/processor-select-columns-edit_26x24.png)Edit icon that is displayed when hovering over Description.
