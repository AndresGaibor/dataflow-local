---
title: "Loading and managing data with Data Manager"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/managing-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data"]
---

# Loading and managing data with Data Manager

Add and manage data from your datasets and [connections](#glossary-0 "Glossary term") with Data manager so that you can load the data into your application.

There are two views in data manager:

- ![Associations view](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_association_outline.svg) Associations

  You can create and edit association between tables.
- ![Table ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_outline.svg) Tables

  You get an overview of all data tables in the application, whether you added them using Add data, or loaded them with the data [load script](#glossary-2 "Glossary term"). Each table is displayed with the table name, the number of data fields, and the name of the data source.

Warning noteWhen using the ODBC (via Direct Access gateway) connector, ODBC drivers that cannot retrieve foreign keys from the database (for example, MS Access) are not supported.

## Previewing a data table

You can preview a table to see which columns it contains, and a sample set of the data.

Do the following:

- Select the data table you want to preview.

A preview of the table data set is displayed.

## Adding a new data table

You can quickly add data tables to your application. Open Data manager and then click ![Add](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg). You can then choose between adding data from the data catalog or from connections and files. You can also drag and drop a data files into Data manager. You are also prompted to add data when you create a new application.

You can add data from the following data sources:

Data sources

| Data source | Method |
| --- | --- |
| Manual entry | You can manually enter data using Add data > Files and other sources and selecting Manual entry under In-app.  [*Adding data manually*](adding-data-manually.htm) |
| New data files | You can add a new data files to the space your application is in and load it into your application using Add data > Files and other sources. To learn more about supported file types, see [*File formats*](../DataSource/load-data-from-files.htm#top).  [*Adding data from uploaded data files*](adding-data-datafiles.htm)  You can also add new data files directly to spaces for use with applications in those spaces.  [*Adding and managing your analytics data*](../Spaces/managing-data-resources-spaces.htm#Adding2) |
| Data files in spaces | You can add data from existing [dataset](#glossary-3 "Glossary term") using Add data > Data [catalog](#glossary-4 "Glossary term").  [*Loading data from the data catalog*](adding-data-catalog.htm)  If an existing data files needs additional preparation, such as specifying filters or delimiters, Add data > Files and other sources.  [*Adding data from uploaded data files*](adding-data-datafiles.htm) |
| Data connections | You can add a new [connection](#glossary-5 "Glossary term") or load data from an existing connection using Add data > Files and other sources.  [*Adding data from a new data source*](adding-data-new-data-source.htm)  [*Adding data from an existing data source*](adding-data-existing-source.htm) |

## Editing a data table

You can edit all the data tables that you have added with Add data. You can rename the table and fields in the data table, and update the fields from the data source. It is also possible to add a calculated [field](#glossary-6 "Glossary term") and adjust date and time formats.

Do the following:

1. Click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) on the data table you want to edit.

   The data table editor opens, and you can perform the edits and transformations you want to do.
2. Click Close to return.

The table is now marked Pending update, and the changes will be applied to the application data the next time you reload data.

For more information, see [*Editing a table*](editing-table.htm).

Information noteYou can only edit data tables added with Add data. If you click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) on a table that was loaded using the load script, the data load editor opens. For more information, see [*Using Data load editor*](use-data-load-editor.htm).

## Deleting a data table

You can only delete data tables added with Add data. Data tables that were loaded using the load script can only be removed by editing the script in the data load editor.

Do the following:

- Click ![Delete](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin.svg) on the data table you want to delete.

The table is now marked Pending delete and will be removed the next time you reload data.

You can undo and redo your delete actions by clicking ![Undo](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_back_outline.svg) and ![Redo](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_forward_outline.svg).

Warning noteIf you have used fields from the data table in a [visualization](#glossary-7 "Glossary term"), removing the data table will result in an error being shown in the application.

## Managing data table associations

When you add several tables that need to be associated, the perfect situation is that the tables associate with key fields that have identical names in the different tables. If that is the case, you can add them to Qlik Sense with the data profiling disabled option of Add data, and the result will be a data structure with the tables associated correctly.

If you have less than ideal data sources, there are a number of possible association problems.

- If you have loaded two fields containing the same data but with a different field name from two different tables, it's probably a good idea to name the fields identically to relate the tables.
- If you have loaded two fields containing different data but with identical field names from two different tables, you need to rename at least one of the fields to load them as separate fields.
- If you have loaded two tables containing more than one common field.

If you want to associate your data, we recommend that you use the Add data option with data profiling enabled. This is the default option. You can verify this setting by clicking ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) beside the Add data button in the lower right corner of the Add Data page.

Qlik Sense performs data profiling of the data you want to load to assist you in fixing the table association. Existing bad associations and potential good associations are highlighted, and you get assistance with selecting fields to associate, based on analysis of the data.

You can manage table associations in two different ways:

- In the ![Associations view](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_association_outline.svg) Associations view of data manager.

  You can create associations based on Insight Advisor recommendations, or create custom associations based on one or more fields.

  For more information, see [*Managing data associations*](associating-data.htm).
- Using the Associate option in the table editor.

  You can create custom associations and composite key associations based on several fields.

  For more information, see [*Managing associations to other tables*](editing-table.htm#Managing).

Information noteIf you disable data profiling when adding data, Qlik Sense will associate tables based on common field names automatically.

## Applying changes and reloading data

Changes that you have made in the Data manager will not be available in the application until you have reloaded data. When you reload data, the changes are applied and any new data that you have added is loaded from the external data sources. Data that you loaded previously is not reloaded.

You can reload all the data from the external data sources by using the ![reload](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_sync.svg) button in the Data manager footer.

![Data manager footer.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_DataManagerDataReload_revised.png)

The ![reload](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_sync.svg) button reloads all the data for the selected table. It does not reload all the data for all the tables in the application.

If the data in Data manager is out of sync with the application data, the Load data button is green. In the Associations view, all new or updated tables are indicated with \*, and deleted tables are a lighter color of gray. In the Tables view, all new, updated, or deleted tables are highlighted in blue and display an icon that shows the status of the table:

- Tables marked with Pending delete ![Delete](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin_outline.svg) will be deleted.
- Tables marked with Pending update ![reload](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_sync.svg) will be updated with fields that have been added, renamed, or removed, or the table will be renamed.
- Tables marked with Pending add ![ ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_tick.svg) will be added.

Do the following:

- Click Load data to load the changes in the application.

The application data is now updated with changes you made in Data manager.

To apply changes and reload all the data in the selected table from the external data sources:

Do the following:

- Click the ![reload](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_sync.svg) button in the Data manager footer.

## Undo and Redo actions in Data manager

When you are editing in Data manager, you can undo or redo some actions by clicking ![Undo](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_back_outline.svg) and ![Redo](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_forward_outline.svg), or by using the keyboard shortcuts Ctrl + Z and Ctrl + Y.

The log of actions is cleared if you:

- Change view, for example, going from the table overview to Associations.
- Load data.
- Close Data manager.

## Viewing table transformation details in Data manager

You can view the operations and transformations performed on a table in Data manager using the Details dialog. The Details dialog is available in the Associations and Table views.

Details displays the current operations and transformations made to the selected table. This shows you the source of a table, the current changes that have been made, and the sequence in which the changes have been applied. Details enables you to more easily understand how a table got into a current state. You can use Details, for example, to easily see the order in which tables were concatenated.

For more information, see [*Viewing table and field transformation details in Data manager*](viewing-table-field-details.htm).

## Interaction between Data manager and the data load script

When you add data tables in the Data manager, data load script code is generated. You can view the script code in the Auto-generated section of the data load editor. You can also choose to unlock and edit the generated script code, but if you do, the data tables will no longer be managed in the Data manager.

By default, data tables defined in the load script are not managed in Data manager. That is, you can see the tables in the data overview, but you cannot delete or edit the tables in Data manager, and association recommendations are not provided for tables loaded with the script. If you synchronize your scripted tables with Data manager, however, your scripted tables are added as managed scripted tables to Data manager.

Warning note

If you have synchronized tables, you should not make changes in the data load editor with Data manager open in another tab.

To learn more about synchronized tables, see [*Synchronizing scripted tables in Data manager*](synchronizing-scripted-tables.htm).

You can add script sections and develop code that enhances and interacts with the data model created in Data manager, but there are some areas where you need to be careful. The script code you write can interfere with the Data manager data model, and create problems in some cases, for example:

- Renaming or dropping tables added with Data manager in the script.
- Dropping fields from tables added with Data manager.
- Concatenation between tables added with Data manager and tables loaded in the script.
- Using the Qualify statement with fields in tables added with Data manager.
- Loading tables added with Data manager using Resident in the script.
- Adding script code after the generated code section. The resulting changes in the data model are not reflected in Data manager.

History only saves scripting created in Data load editor. It does not include auto-generated scripting sections created by Data manager. For example, if you restore a load script that contains auto-generated scripts in a locked section, the script outside of the auto-generated sections is restored to the old version while the script inside the auto-generated sections remains the same.

It is not recommended to co-develop application data models using Data manager. For more information, see [*Collaborative development and Data manager*](script-codevelopment.htm#Co-devel).

To learn more about editing the data load script, see [*Editing load scripts*](edit-data-load-script.htm).

## Concatenating tables in Data manager

Concatenation combines two tables into a single table with combined fields. It consolidates content, reducing the number of separate tables and fields that share content. Tables in Data manager can be automatically or forcibly concatenated.

For more information, see [*Concatenating tables in Data manager*](concatenating-tables-in-data-manager.htm).

Concatenated table in Tables view and Associations view.

![Concatenated table.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ex_concatenated.png)

Related learning:

- [Introduction to the data manager](/lnk/Intro_Data_Manager_QS)
- [Reload data for analysis](/lnk/Reload_Data_Analysis_QS)
- [How do I load data into a Qlik Sense application?](/lnk/How_load_data_QS_SaaS_app)
- [Getting started with Qlik Sense](/lnk/Getting_started_QS)
