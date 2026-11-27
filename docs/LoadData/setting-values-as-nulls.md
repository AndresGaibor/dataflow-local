---
title: "Setting field values as null in a table"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/setting-values-as-nulls.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and managing data with Data Manager", "Editing a table"]
---

# Setting field values as null in a table

In the Set nulls card, you select distinct values from a [dimension](#glossary-0 "Glossary term") [field](#glossary-1 "Glossary term") to be treated as null values in Qlik Sense.

For example, if your source data includes representations such as X for nulls, you can use the Set nulls card to set that value to be treated as a null value in Qlik Sense. If your table contains fields with empty spaces, you can set these as null values using the Set nulls card. You can also use the Set nulls card to clean your data of unwanted values by setting these values as null.

If you want to use a specific value as your null value, you can replace the default null value, - (Null), using the Replace card. For more information, see [*Replacing field values in a table*](replacing-field-values.htm).

You can set field values as null in fields that contain up to a maximum of 5,000 distinct values.

The Set nulls card consists of two sections, Distinct values and Manual null values. When you select values from Distinct values, they are added to Manual null values. When you apply the null values, all instances of the selected values are set to null in the field's data. You can restore individual or all values set as null.

## Setting field values as null

Do the following:

1. In Data manager, select a table and click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg).
2. Select a field.
3. In the data profiling card, click the Set nulls card.
4. Under Distinct values, select the values you want set as null.
5. Click Set null values.

## Restoring values manually set as null

Do the following:

1. In Data manager, select a table and click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg).
2. Select a field.
3. In the data profiling card, click the Set nulls card.
4. In the Set nulls card, under Manual null values, do one of the following:

   - Click ![Cancel](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_remove.svg) after the values you no longer want set as null.
   - Click Remove All to restore all values set as null.
5. Click Set null values.

Related learning:

- [Data manager calculations and transformations](/lnk/Data_Manager_Calculations_Transformations_QS)
