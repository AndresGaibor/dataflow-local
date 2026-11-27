---
title: "Replacing field values in a table"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/replacing-field-values.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and managing data with Data Manager", "Editing a table"]
---

# Replacing field values in a table

The Replace card enables you to replace different [field](#glossary-0 "Glossary term") values in your tables with other values.

In a data set, different terms might be used for the same object or concept. For example, the full name of a country and its abbreviation might both be found in the same data set. The Replace card enables you to ensure that these instances are treated as a single distinct value rather than different distinct values. For example, in a field that contains country data, you could replace U.S, US, and U.S.A with USA. You can also use the Replace card to change individual values, such as when a name in a data set needs to be changed.

You can set replace values in fields that contain up to a maximum of 5,000 distinct values.

In addition, calculated fields ignore replacement values and will use the original values instead.

The Replace card consists of two sections: Distinct values and Replacement value. Distinct values lists all distinct values and any replacement values. Replacement value contains a field to enter the replacement term and a list of values selected to be replaced. You replace field values by selecting distinct values, entering the replacement value, and applying the replacement. You can also select a replacement value in Distinct values and edit it to change the values being replaced or the value being used for the replacement. You can add or edit multiple replacement values before applying the replacements.

## Replacing values

Do the following:

1. In Data manager, select a table and click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg).
2. Select a dimension field.
3. In the data profiling card, click the Replace tab.
4. Under Distinct values, select the distinct values you want to replace.
5. Under Replacement value, enter the new value for these distinct values.
6. Click Replace.

## Editing a replacement value

You can add more distinct values to a replacement value, remove distinct values from a replacement value, or change the replacement value.

### Adding distinct values to a replacement value

Do the following:

1. In the Replace card, under Distinct values, select a replacement value.
2. Under Distinct values, select the distinct values you want to add.
3. Click Replace.

### Removing distinct values from a replacement value

Do the following:

1. In the Replace card, under Distinct values, select a replacement value.
2. After each distinct value you want to remove, click ![Cancel](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_remove.svg).
3. Click Replace.

### Changing a replacement value

Do the following:

1. In the Replace card, under Distinct values, select a replacement value.
2. Under Replacement, enter a new value.
3. Click Replace.

## Deleting a replacement value

Replacement values can be deleted by removing all associated distinct values.

Do the following:

1. In the Replace card, under Distinct values, select a replacement value.
2. Click Remove All.
3. Click Replace.

Related learning:

- [Data manager calculations and transformations](/lnk/Data_Manager_Calculations_Transformations_QS)
- [How do I replace data values?](/lnk/How_replace_data_values)
