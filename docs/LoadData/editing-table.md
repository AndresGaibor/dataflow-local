---
title: "Editing a table"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/editing-table.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and managing data with Data Manager"]
---

# Editing a table

You can edit a table that was added to the application in the [Data manager](#glossary-1 "Glossary term") overview, to rename the table, associate the table to other tables, or make [field](#glossary-2 "Glossary term") transformations.

To edit a table, select the table in Data manager and click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg). The table editor is displayed, with a preview of the data in the table. Each field has a field menu with transformation options. You open the field menu by clicking ![Menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_menu.svg). Selecting a field displays the data profiling card pane, which contains a summary of the field’s data as well as additional transformation options.

Information note If the data contains records with identical data in all fields that are loaded, they are represented by a single record in the preview table.

## Renaming a table

When you add a table in Data manager, the table is assigned a default name, based on the name of the database table, data file, or Excel worksheet, for example. If the name is non-descriptive or unsuitable, you can rename it.

Do the following:

1. Click on the table name.
2. Edit the table name.
3. Press Enter or click outside the table name.

The table is now renamed.

## Renaming a field

You can rename fields in a table to get a better name that is easier to understand.

Do the following:

1. Click on the field name that you want to rename, or select Rename from the field menu.
2. Type the new name.

   Information noteField names must be unique. If you have fields with the same name in several tables, Qlik Sense will qualify the field names when you add data, that is, add the table name as prefix.
3. Press the Enter key, or click outside the field.

The field is now renamed.

To learn more about fields, see [*Fields*](../DataSource/fields.htm).

## Managing associations to other tables

You can create custom associations to fields in other tables with Associate in the field menu.

For more information, see [*Associating data in the table editor*](managing-associations-table-editor.htm).

Typically, these are the most common cases where you need to create a custom association instead of following the recommendations:

- You know which fields to associate the tables with, but the score for this table pair is too low to show in the list of recommendations.

  Create an association based on a single field in each table.
- The tables contain more than one common field, and they need to be used to form the association.

  Create a compound key.

In many cases it is easier to manage to your associations in the Associations view

For more information, see [*Managing data associations*](associating-data.htm).

## Changing field type and display format

When data is added, Qlik Sense interprets the field type of each field. The following field types are currently supported:

- ![general](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_general_data_class.svg) General
- ![Date and time](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_calendar.svg) Date
- ![Time](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_clock_3.svg) Timestamp
- ![Map](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_map_outline.svg) Geo data

If the data was not interpreted correctly, you can adjust the field type. You can also change the input and display format of a date or timestamp field.

Fields that contain geographical information in the form of names or codes, such as postal areas, cannot be used for mapping unless they are designated as Geo data fields.

For more information, see [*Changing field types*](changing-date-time-format.htm).

## Hiding fields from analysis

You can hide fields so that they are only available in Data manager and [Data load editor](#glossary-3 "Glossary term")
. You might, for example, have fields that are only used for calculating another field. You can hide these fields so that they are not available in the [sheets](#glossary-4 "Glossary term") or [Insight Advisor](#glossary-5 "Glossary term") assets panel but remain available in Data manager.

For more information, see [*Hiding fields from analysis*](hiding-fields-from-analysis.htm).

## Assessing table field data before loading data

You can examine the data in your table for potential quality issues such as null values and outlier values before you load it using the Summary data profiling card. The Summary card categorizes fields as [dimensions](#glossary-6 "Glossary term") ,[measures](#glossary-7 "Glossary term"), or temporal fields, providing different data summaries for each and enabling different transformation options in other data profiling cards. Fields set as measures in the Summary card can be grouped using the Bucket card. Fields set as dimensions in the Summary card can have a custom order applied in the Order card. For fields that can be classified in multiple categories, you can switch between each possible category's summary for the field.

For more information, see [*Assessing table field data before loading data*](Previewing-table-fields.htm).

## Replacing field values in a table

You can replace values in a field using the Replace data profiling card. The Replace card enables you to select one or more values from a field and then replace them with another value. For example, in a data set that contains country names in both full and abbreviated formats, you could replace them with a single shared value.

For more information, see [*Replacing field values in a table*](replacing-field-values.htm).

## Setting field values as null in a table

You can set distinct values from a dimension field to be treated as null values using the Set nulls data profiling card. The Set nulls card enables you to select values from a table field and then manually set them as null. For example, if your data set represents nulls using a character such as X, you can use the Set nulls card to enable Qlik Sense to treat that value as null. The Set nulls card can also be used to clean your data set by setting unwanted values as nulls.

For more information, see [*Setting field values as null in a table*](setting-values-as-nulls.htm).

## Setting a custom order for field values

Depending on your data, it may be more meaningful to display dimension values in an order other than alphabetical or numerical. Fields set as dimensions in the Summary data profiling card may have a custom order of data applied using the Order data profiling card, enabling you to set the default organization of field data in [visualizations](#glossary-8 "Glossary term").

For more information, see [*Customizing the order of dimension values*](Customizing-the-order-of-dimension-values.htm).

## Splitting a field in a table

You can extract information from an existing field into new fields using the Split data profiling card. The Split card enables you to split content from a field into multiple fields. You could, for example, split a field that contains an address to extract the zip or postal code. This enables you to quickly create new fields containing relevant sections of existing data.

For more information, see [*Splitting a field in a table*](splitting-a-field.htm).

## Grouping measure data into ranges

You can group values in a table measure field into ranges using the Bucket data profiling card. The Bucket card enables you to group a field’s value in user-defined buckets, creating a new field that is added to the table. You could, for example, group ages into age ranges to use as a dimensions in your visualizations.

For more information, see [*Grouping measure data into ranges*](Grouping-measure-data-into-ranges.htm).

## Viewing field transformation details

You can view the current operations and transformations performed on a field and their sequence in the Details dialog. Details enables you to understand where a field came from, what changes have been made to it, and the sequence in which the transformations were applied.

For more information, see [*Viewing table and field transformation details in Data manager*](viewing-table-field-details.htm).

## Unpivoting crosstab data

If you have loaded data in crosstab format, the best option is usually to unpivot the table, that is, transposing parts of the table into rows. This will make it easier to work with the data and create associations to your other data tables.

![From crosstab to unpivoted crosstab.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_gen_unpivoting.png)

For more information, see [*Unpivoting crosstab data in the data manager*](unpivot-crosstable.htm).

## Updating a table from the data source

You may want to change the selection of fields from the data source. For example, you may need to add a field that was left out, or the data source may have been updated with added fields. In this case, you can update the table from the data source. If the table was created with Manual entry, you can add, edit, or delete table data as well as add new rows and columns. For more information, see [*Adding data manually*](adding-data-manually.htm).

Do the following:

1. Click Select data from source.

   The data selection wizard opens with your current selections.
2. Make the required changes in selection.

   For more information, see [*Selecting data fields*](select-data-fields.htm).
3. Click Add data with data profiling enabled.

The table is now updated with fields according to the selections you made.

## Adding a calculated field

There are many cases where you need to adjust or transform the field data that is loaded. For example, you may need to concatenate a first name and a last name to a full name, extract part of a product number, convert the data format or multiply two numbers.

You can add calculated fields to manage many cases like this. A calculated field uses an expression to define the result of the field. You can use functions, fields and operators in the expression. You can only refer to fields in the table that you are editing.

For more information, see [*Using calculated fields*](add-calculated-field.htm).

## Sorting a table

You can sort a table based on a specific field while you are editing the table, to get a better overview of the data. You can only sort on one field at a time.

Do the following:

- From the field menu, select Sort.

The table data is now sorted in ascending order according to this field. If you want to sort in descending order, select Sort again.

Information noteThe sort order is not maintained in the loaded application data.

## Undo and redo actions

You can undo and redo your table edit actions by clicking ![Redo](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_forward_outline.svg) and ![Undo](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_back_outline.svg) .

The undo/redo history is cleared when you close the table editor.

Related learning:

- [Introduction to the data manager](/lnk/Intro_Data_Manager_QS)
- [Data manager calculations and transformations](/lnk/Data_Manager_Calculations_Transformations_QS)
