---
title: "Adding data from uploaded data files"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/adding-data-datafiles.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and managing data with Data Manager", "Adding data to the application from connections and new files"]
---

# Adding data from uploaded data files

You can upload certain file types and load that data in [Data load editor](#glossary-0 "Glossary term") or [Data manager](#glossary-1 "Glossary term").

You can upload datasets directly to spaces in the Analytics [activity center](#glossary-2 "Glossary term").
You can also upload datasets to your spaces while working in an application. To add and use a [dataset](#glossary-4 "Glossary term") in your application, you must:

- Upload your data files to your cloud. Each data file can be up to 100 GB. However, when uploading very large data files (over 6 GB), you might experience constraints with engine capacity. These constraints are more likely to be encountered with QVD data files due to the memory usage necessary to load QVD files into the engine. For more information about increasing the capacity available, see [*Large application support*](../Admin/large-app-support.htm).
- Add the data to your application. This is a preliminary step that allows you to select and prepare the data that you want to load.
- Load the data into your application. When you are done selecting and preparing the data, you can load the data into your application. After you load the data, you can use it to create visualizations in your application.

Information noteThe file extension of DataFiles connections is case sensitive. For example: .qvd.

## Uploading your data files to your cloud

You can upload data files to your cloud from the DataFiles window. There are different ways to open this window. You can select which space to upload the data files from the spaces drop-down list. You must have editing permission to add data files to a space.

### In a new application

Do the following:

1. Open the application.
2. Click Files and other sources.
3. In the left menu, under Existing connections, select the space where you want to upload the file.
4. In the left menu, click Data files.
5. Under Folder shortcuts, click DataFiles.
6. If needed, navigate to the folder within the space where you want to upload the file. Navigate by selecting folders in the list, or type a specific folder path under Path.
7. Upload a data file.

### In an existing application

Do the following:

1. Open the application.
2. In the top menu, click ![Navigation](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg), and then click Files and other sources.
3. In the left menu, under Existing connections, select the space where you want to upload the file.
4. In the left menu, click Data files.
5. Under Folder shortcuts, click DataFiles.
6. If needed, navigate to the folder within the space where you want to upload the file. Navigate by selecting folders in the list, or type a specific folder path under Path.
7. Upload a data file.

### In the Data load editor from an existing DataFile connection

Do the following:

1. Open the application.
2. Open the Data load editor.
3. Go to the Data connections window on the right. You will see folders from personal and shared spaces that you can access.

   For datasets in spaces you can access, you can select a space using the drop down menu.
4. Choose a DataFiles folder, and click ![Select data](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok_outline.svg).
5. If you are accessing the DataFiles for a space in Qlik Cloud Analytics, you can navigate to the folder within the space where you want to upload the file. Navigate by selecting folders in the list, or type a specific folder path under Path.
6. Upload a data file.

After you have uploaded a file to your cloud, you can add the data to your application, and then load data into your application.

## Loading data into your application

Warning note

Do not add a table in Data manager that has already been added as a scripted table with the same name and same columns in Data load editor.

### In Data manager

Do the following:

1. Open an application.
2. Open the Data manager, and then click ![Add](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) Add data > Files and other sources. You can also click Add data in ![Navigation](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) in the top bar. Adding data allows you to select and prepare your data before you load the data into your application.
3. Click Data files.
4. In the left menu, under Existing connections, select the space where the file containing your data is located.
5. If needed, navigate to the folder within the space where the file is located. Navigate by selecting folders in the list, or type a specific folder path under Path.
6. Choose the file that contains your data. Qlik Sense provides you with a preview of your data.
7. Select the tables and fields to load.
8. Click Add data to open the data in the Associations view of the data manager. This allows you to continue to add data sources, transform the data, and associate the tables in Data manager.

   Data profiling is enabled by default when you click Add data. Data profiling does the following:

   - Recommends data associations.
   - Auto-qualifies common fields between tables. This adds a unique prefix based on table name.
   - Maps date and time fields to autoCalendar.

   Tables are not associated on common field names automatically. You can associate tables in the Associations view.

   Tip noteIf you want to load the data directly into your application, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and then disable data profiling. This will also reload all existing data from data sources when you add the data. Tables will be associated on common field names automatically. Date and time fields will not be created.
9. Click Load data when you are done preparing the data. If serious problems are detected, you need to resolve the problems in Data manager before you can load data into the application.

Information note

If your data includes city or country geographic information, the following QVD files might automatically be added to the current space:

- countryAliases.qvd
- countryGeo.qvd
- cityAliases.qvd
- cityGeo.qvd

These files are used to provide additional geographic data for the locations included in your added data. Qlik Sense manages and updates these files as necessary. If they are deleted, they are automatically added back after the next reload.

### From a data connection in the data load editor

You can go to Data Connections, and use the ![Data Selection](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok_outline.svg) Select data dialog to select data to load.

For more information, see [*Selecting data in load scripts*](select-data-to-load.htm).

### From a file by writing script code

Files are loaded using a LOAD statement in the script. LOAD statements can include the full set of script expressions. To read in data from another Qlik Sense application, you can use a Binary statement.

For more information, see [*Load*](../Scripting/ScriptRegularStatements/Load.htm).

## Uploading an updated data file

To update data in an application, you can upload an updated data file with the same name as the file you that you previously uploaded. When prompted, choose the replace the previous file. After you have uploaded the data file, you can reload the data into your application.

Related learning:

- [How do I load data into a Qlik Sense application?](/lnk/How_load_data_QS_SaaS_app)
