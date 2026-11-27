---
title: "Loading and transforming data with scripting"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/introduction-data-modeling.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data"]
---

# Loading and transforming data with scripting

Applications use a [data load script](#glossary-0 "Glossary term"), which is managed in the [Data load editor](#glossary-1 "Glossary term"), to connect
to and retrieve data from various data sources. A data source can be a data file, for example an Excel file or a .csv file. A data source can also be a database, for example a Google BigQuery or Salesforce database.

You can also load data using the [Data manager](#glossary-2 "Glossary term"), but when you want to create, edit and run a data load script you use the data load editor.

In the script, the fields and tables to load are specified. Scripting is often used to specify what data to load from your data sources. You can also manipulate the data structure by using script statements.

During the data load, Qlik Sense identifies
common [fields](#glossary-3 "Glossary term") from different tables (key fields) to associate the data. The resulting data structure of the data in the application can be monitored
in the data model viewer. Changes to the data structure can be achieved by renaming fields to obtain different associations between tables.

After the data has been loaded into an application, it is stored in the application.

- To learn more about Data load editor, see [*Using Data load editor*](../LoadData/use-data-load-editor.htm).
- To learn more about script syntax and data structures, see [*Understanding script syntax and data structures*](../LoadData/understand-data-structures.htm).
- To learn more about data and fields, see [*Guidelines for data and fields*](../Introduction/guidelines-data-fields.htm).

Analysis in Qlik Sense always happens while the application
is not directly connected to its data sources. So, to refresh
the data, you need to run the script to reload the data.

You can also use scripting to create data sources with scripts. Scripts use a load script to load data, transform it, and export it as data sources. Scripts are added from the Create page of the Analytics [activity center](#glossary-5 "Glossary term"). To learn more, see [*Working with scripts in the catalog*](../ScriptEditor/using-the-script-editor.htm).

You can create common blocks of load script to be used in multiple applications and scripts using QlikView script (QVS) files. For more information, see [*Creating reusable load script with QVS files*](../LoadData/QVS/create-common-scripting-qvs.htm).

In shared spaces, multiple users can collaborate on the load script in applications or scripts. For more information, see [*Collaboratively developing data load scripts in shared spaces*](../LoadData/script-codevelopment.htm).

Warning noteRunning an imported or shared asset in Qlik Cloud can potentially be used to execute malicious script. Make sure your trust the source of your asset before refreshing or running it.

## Interaction between Data manager and the data load script

When you add data tables in the Data manager, data load script code is generated. You can view the script code in the Auto-generated section of the data load editor. You can also choose to unlock and edit the generated script code, but if you do, the data tables will no longer be managed in the Data manager.

By default, data tables defined in the load script are not managed in Data manager. That is, you can see the tables in the data overview, but you cannot delete or edit the tables in Data manager, and association recommendations are not provided for tables loaded with the script. If you synchronize your scripted tables with Data manager, however, your scripted tables are added as managed scripted tables to Data manager.

Warning note

If you have synchronized tables, you should not make changes in the data load editor with Data manager open in another tab.

To learn more about synchronized tables, see [*Synchronizing scripted tables in Data manager*](../LoadData/synchronizing-scripted-tables.htm).

You can add script sections and develop code that enhances and interacts with the data model created in Data manager, but there are some areas where you need to be careful. The script code you write can interfere with the Data manager data model, and create problems in some cases, for example:

- Renaming or dropping tables added with Data manager in the script.
- Dropping fields from tables added with Data manager.
- Concatenation between tables added with Data manager and tables loaded in the script.
- Using the Qualify statement with fields in tables added with Data manager.
- Loading tables added with Data manager using Resident in the script.
- Adding script code after the generated code section. The resulting changes in the data model are not reflected in Data manager.

History only saves scripting created in Data load editor. It does not include auto-generated scripting sections created by Data manager. For example, if you restore a load script that contains auto-generated scripts in a locked section, the script outside of the auto-generated sections is restored to the old version while the script inside the auto-generated sections remains the same.

It is not recommended to co-develop application data models using Data manager. For more information, see [*Collaborative development and Data manager*](../LoadData/script-codevelopment.htm#Co-devel).

To learn more about the data load script, see [*Editing load scripts*](../LoadData/edit-data-load-script.htm).

## Loading and transforming data from the Analytics activity center

You can load and transform data using scripts in the Analytics activity center. In Analytics, scripts are applications built to load, transform, and export data using the same scripting as analytic applications.
Scripts allow you to load and transform data without analytics.

To learn more, see [*Working with scripts in the catalog*](../ScriptEditor/using-the-script-editor.htm).

Related learning:

- [Introduction to the data load editor](/lnk/Intro_Data_Load_Editor_QS)
- [Data Load Basics](/lnk/Data_load_basics_QS)
