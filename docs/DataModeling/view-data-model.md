---
title: "Viewing and transforming the data model"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataModeling/view-data-model.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Modeling your data"]
---

# Viewing and transforming the data model

The data model viewer is an overview of the data structure of an application. You can view detailed metadata about the tables and fields. You can also create [dimensions](#glossary-1 "Glossary term") and [measures](#glossary-2 "Glossary term") from the data fields.

Click [Data model viewer](#glossary-3 "Glossary term") in the application navigation menu to open the data model viewer.

Each data table is represented by a box, with the table name as title and with all fields in the table listed. Table associations are shown with lines, with a dotted line indicating a circular reference. When you select a table or a field, the highlighting of associations instantly gives you a picture of how fields and tables are related. You can search for specific tables and fields by clicking ![Search data model](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_search.svg).

The data model displays the data structure of the application.

![Data model viewer.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_data_model_viewer.png "Click to view full size")

You can change the zoom level by clicking ![zoom in](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_zoom_in.svg), ![zoom out](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_zoom_out.svg) or using the slider. Click ![Home](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_home_2.svg) to restore the zoom level to 1:1.

In the preview pane, you can inspect the contents of a table or field. You can also add dimensions and measures to the application if you select a field. For more information, see [*Previewing tables and fields in the data model viewer*](preview-tables-fields-data-model-viewer.htm).

## Moving tables

You can move tables by dragging them on the canvas. The table positions will be saved when the application is saved.

You can lock the table layout (positions and sizes), by clicking ![Locked](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_lock_outline.svg) in the right part of the canvas. To unlock the table layout, click ![Unlocked](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_unlock_outline.svg).

You can also arrange the layout automatically using the options under ![Grid View](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_grid_outline.svg) in the toolbar:

Options for moving tables

| UI item | Name | Description |
| --- | --- | --- |
| Grid View | Grid layout | To arrange the tables in a grid. |
| auto | Auto layout | To arrange the tables to fit in the window. |
| Time | Restore layout | To revert to the layout state present when the data model viewer was last opened. |

## Resizing tables

You can adjust the display size of a table with the arrow in the bottom right corner of the table. The display size will not be saved when the application is saved.

You can also use the automatic display size options in the toolbar:

Options for resizing tables

| UI item | Name | Description |
| --- | --- | --- |
| Collapse | Collapse all | To minimize all tables to show the table name only. |
| Reduce | Show linked fields | To reduce the size of all tables to show the table name and all fields with associations to other tables. |
| Expand | Expand all | To maximize all tables to show all fields in the table. |

## Data model performance

These are indicators that can impact data model performance. Each one is a best practice that will improve application usability.

Data model performance best practices

| Action | Description |
| --- | --- |
| Synthetic keys removed | Qlik Sense creates synthetic keys when two or more data tables have two or more fields in common. This may mean that there is an error in the script or the data model. To diagnose synthetic keys, see [*Synthetic keys*](../Scripting/synthetic-keys.htm). |
| Circular references removed from data model | Circular references occur when two fields have more than one association. Qlik Sense will attempt to resolve these by changing the connection to one of the tables. However, all circular reference warnings should be resolved, see [*Understanding and solving circular references*](../LoadData/understand-circular-references.htm). |
| Appropriate granularity of data | You should only load data that is necessary. For example: a group of users only need data divided by week, month, and year. You can either load in the aggregated data or aggregate the data within the load script to save memory. If a user does need to visualize data at a lower level of granularity, you can use ODAG or document chaining. |
| QVDs used where possible | A QVD is a file containing a table of data exported from Qlik Sense. This file format is optimized for speed when reading data from a script, but is still very compact. Reading data from a QVD file is typically 10-100 times faster than reading from other data sources. For more information, see: [*Working with QVD files*](../Scripting/work-with-QVD-files.htm). |
| QVD files optimized on load | QVD files can be read in two modes: standard (fast) and optimized (faster). The selected mode is determined automatically by the script engine. There are some limitations regarding optimized loads. It is possible to rename fields, but any of these operations will result in a standard load:   - Any transformations on the fields that are loaded. - Using a where clause causing Qlik Sense to unpack the records. - Using Map on a field that is loaded. |
| Incremental loads leveraged | If your application connects to a large amount of data from databases that are continuously updated, reloading the entire data set can be time consuming. Instead, you should use incremental load to retrieve new or changed records from the database. For more information, see [*Loading new and updated records with incremental load*](../LoadData/use-QVD-files-incremental-load.htm). |
| Snowflake model consolidated | If you have a snowflake data model, you may be able to reduce the number of data tables by joining some of them using the Join prefix or other mapping. This is especially important for large fact tables. A good rule of thumb is to have only one large table. For more information see [To Join or Not to Join](https://community.qlik.com/t5/Qlik-Design-Blog/To-Join-or-not-to-Join/ba-p/1463102). |
| Tables that have a small number of fields are denormalized | If you have two tables with few fields, it may improve performance to join them. For more information, see [*Combining tables with Join and Keep*](../Scripting/combine-tables-with-join-keep.htm). |
| Denormalized lookup (leaf) tables with mapping loads | You should not use the Join prefix if you only need to add one field from a table to another. You should use the ApplyMap lookup function, see [Don't join - use ApplyMap](https://community.qlik.com/t5/Qlik-Design-Blog/Don-t-join-use-Applymap-instead/ba-p/1467592). |
| Time stamps removed or decoupled from date field | Date fields can fill up space when the timestamp is present as the string representation is larger, and the number of distinct values is larger. If the precision is not necessary for your analysis, you can round the timestamp to e.g. the nearest hour using Timestamp(Floor(YourTimestamp,1/24)) or remove the time component completely using Date(Floor(YourTimestamp)).  If you want the timestamp, you can decouple it from the date itself. You can use the same Floor() function, and then create a new field with the extracted time by using something along the lines of: Time(Frac(YourTimestamp)). |
| Unnecessary fields removed from data model | You should only load necessary fields in your data model. Avoid using Load \* and SELECT. Make sure you keep:   - Fields that are necessary for your analysis. - Fields that are actually being used in the application. |
| Link tables avoided when dealing with high data volumes | You should use link tables where possible. However, if you are dealing with large data volumes, concatenated tables can out-perform link tables. |
| Concatenated dimensions broken to new fields | You should break apart concatenated dimensions into separate fields. This reduces the number of unique occurrences of values in your fields. This is similar to how timestamps can be optimized. |
| AutoNumber used where possible | You can create an optimized load by loading your data from a QVD file first, and then using the AutoNumber statement to convert values to symbol keys. For more information, see [*AutoNumber*](../Scripting/ScriptRegularStatements/Autonumber.htm). |
| Data islands avoided | Data islands can be useful, but they usually affect performance. If you are creating islands for selection values, use variables. |
| QVDs are stored based on incremental timeframes | You should store QVD in segments, such as monthly. These smaller monthly QVD can then support many different applications that might not need all of the data. |

For more best practices, see [*Best practices for data modeling*](best-practices-data-modeling.htm).

Related learning:

- [Introduction to the data model viewer](/lnk/Intro_Data_Model_Viewer_QS)
- [Loading Data from a Database](/lnk/Loading_data_from_database_QS)
