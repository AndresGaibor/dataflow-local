---
title: "SQL expression processor"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Transformation/Processor-sql-expression.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to a data warehouse", "Transforming data", "Adding transformation flows"]
---

# SQL expression processor

Writes the result of one or more custom SQL expressions in a new column.

The SQL expression processor lets you write simple or complex SQL expressions to process data in a new column of your source dataset. You can add more SQL expressions with ![add](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_plus_outline.svg).

## SQL expression properties

Properties to configure to create a new column and apply SQL expressions on it. Each expression creates a new column.

Configuration

| Property | Configuration |
| --- | --- |
| Name | Enter the name of the new column on which the SQL expression will be applied. |
| Type | Select the data type of the column.  Depending on which data type you select you may also need to set more column properties, for example, Precision, Scale, or Length. |
| Nullable | Select if you want the column to be nullable. |
| SQL expression | Either enter a simple SQL expression in the text box, or click Expression builder icon to open the expression builder. In the expression builder, you can:   - Enter complex SQL expressions in the Build expression text box. You can select the column names on the left panel to auto-complete your expression. - Extract all parameters used in the SQL expression in the Extract parameters area, and test them with custom values. - Test your SQLexpression in the Test expression area. |

To rename the processor, click the ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/processor-select-columns-edit_26x24.png)Edit icon that is displayed when hovering over the default name of the processor.

To edit its description, click the ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/processor-select-columns-edit_26x24.png)Edit icon that is displayed when hovering over Description.
