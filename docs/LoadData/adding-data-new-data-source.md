---
title: "Adding data from a new data source"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/adding-data-new-data-source.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and managing data with Data Manager", "Adding data to the application from connections and new files"]
---

# Adding data from a new data source

You can add data to your application from a new data source. When you add data from a new data source, a [connection](#glossary-1 "Glossary term") to the data source is created in Data Connections, making it easier to add more data from the same data source.

Warning note

Do not add a table in Data manager that has already been added as a scripted table with the same name and same columns in Data load editor.

To learn more about available data sources, see [*Adding data to the application from connections and new files*](adding-data.htm).

To learn more about connecting to data sources, see [*Loading analytics data*](connect-data-sources.htm).

You can delete connections from Add data by right-clicking the connection and selecting ![Delete](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin_outline.svg).

Warning note

If you delete a connection, you must delete any tables from Data manager that used that connection before you load data.

Do the following:

1. Open an application.
2. Open the Data manager, and then click ![Add](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) Add data > Files and other sources. You can also click Add data in ![Navigation](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) in the top bar.
3. Under Connect to a new data source, select a source.
4. Enter the connection parameters required by the data source.
5. Select the tables and fields to load.

   For more information, see [*Selecting data fields*](select-data-fields.htm).
6. Optionally, select to apply a data filter if you want to select a subset of the data contained in the fields you have selected.

   If your data source is a file, select Filters. Beside the table to which you want to add a filter, click Add filter, select a field, select a condition, and then enter a value with which to filter. For information, see [*Filtering data from files*](Filter-data.htm).

   Information note

   Qlik Sense does not support filters on date fields from QVD files.

   Note the following:

   - You can apply multiple filters to the same field.
   - You can remove filters in the Associations view of Data manager or from Select data from source. For the changes to take effect, reload data by clicking the Load data button.

   For databases and connectors, when you select Filter data, a text box opens for the filter criteria. For information about criteria, see [*Filtering data from files*](Filter-data.htm).

   Note the following:

   - Filters are applied to field names from the database. If you rename a field in the Data manager, you have to apply the filter to the original field name from the database. For example, if a field is named EMP in your database, and you rename it to EMPLOYEE in the Data manager, you have to apply the filter EMP = ‘filter\_value’ .
   - You can clear data filters in the Associations view of the Data manager. For the changes to take effect, reload data by clicking the Load data button. You have to split concatenated tables before clearing filters.
   - Filtering data is not currently available for all connectors, or for attached files.
7. Click Add data to open the data in the Associations view of the data manager. This allows you to continue to add data sources, transform the data, and associate the tables in Data manager.

   Data profiling is enabled by default when you click Add data. Data profiling does the following:

   - Recommends data associations.
   - Auto-qualifies common fields between tables. This adds a unique prefix based on table name.
   - Maps date and time fields to autoCalendar.

   Tables are not associated on common field names automatically. You can associate tables in the Associations view.

   Tip noteIf you want to load the data directly into your application, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and then disable data profiling. This will also reload all existing data from data sources when you add the data. Tables will be associated on common field names automatically. Date and time fields will not be created.

   For more information, see [*Managing data associations*](associating-data.htm).
8. Click Load data when you are done preparing the data. If serious problems are detected, you need to resolve the problems in Data manager before you can load data into the application.

   For more information, see [*Troubleshooting - Loading data*](../Troubleshooting/troubleshooting-load-data.htm).

Information note

If your data includes city or country geographic information, the following QVD files might automatically be added to the current space:

- countryAliases.qvd
- countryGeo.qvd
- cityAliases.qvd
- cityGeo.qvd

These files are used to provide additional geographic data for the locations included in your added data. Qlik Sense manages and updates these files as necessary. If they are deleted, they are automatically added back after the next reload.
