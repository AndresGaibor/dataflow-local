---
title: "Previewing tables and fields in the data model viewer"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataModeling/preview-tables-fields-data-model-viewer.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Modeling your data", "Viewing and transforming the data model"]
---

# Previewing tables and fields in the data model viewer

In the data model viewer, you can preview any data table in the panel at the bottom of the screen. In the preview, you can quickly inspect the contents of a table or [field](#glossary-0 "Glossary term"). You can also add [dimensions](#glossary-1 "Glossary term") and [measures](#glossary-2 "Glossary term") to the application if you select a field.

Additionally, metadata for the selected table or field are displayed in the preview panel.

You can show and hide the preview panel in two ways:

- Click ![Open bottom panel](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_toggle_bottom.svg) in the toolbar.
- Click the Preview header.

Information noteThe visual representation of data order in this preview may not correspond to the actual load order.

## Showing a preview of a table

Do the following:

- Click a table header in the data model viewer.

The preview panel is displayed with fields and values of the selected table.

![Preview panel with a  preview of a table.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_PreviewTable_dmv.png)

## Showing a preview of a field

Do the following:

- Click a table field in the data model viewer.

The preview panel is displayed with the selected field and its values, and metadata for the field. You can also add the field as a master dimension or measure.

![Preview panel with a  preview of a field.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_PreviewField_dmv.png)

- Density is the number of records that have non-NULL values in this field, as compared to the total number of records in the table.
- Subset ratio is the number of distinct values of the field found in this table, as compared to the total number of distinct values of this field in other tables in the data model. This is only relevant for key fields.
- If the field is marked with [Perfect key], every row contains a key value that is unique.

To learn more about creating a master dimension, see [*Creating a master dimension from the data model viewer*](../Dimensions/create-master-dimension-from-data-model-viewer.htm).

To learn more about creating a master dimension, see
[*Creating a master measure from the data model viewer*](../Measures/create-master-measure-data-model-viewer.htm)
