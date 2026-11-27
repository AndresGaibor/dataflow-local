---
title: "Working with scripts in the catalog"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ScriptEditor/using-the-script-editor.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting"]
---

# Working with scripts in the catalog

Prepare data for analytics applications directly in the Analytics [activity center](#glossary-0 "Glossary term") using scripts.
Scripts are task-specific, purpose-built applications for loading, transforming, and exporting data. You create and manage your scripts in catalog.

Scripts allow you to load and transform data without needing an analytics application. The transformations can be reused to provide data to multiple applications. Scripts help you remove data preparation from the analytics application workflow unless users want to build and transform data themselves in their application.

When you add a script in the catalog, it opens in Script. In Script, you can create, preview, and run data scripts.
You can use these scripts to store data in QVD files or other formats with the Store statement. These outputs can then be used by other users when creating analytics applications or when preparing data for Qlik Predict. You can also create scripts that other users can use as templates for analytic application load scripts, rapidly speeding up the creation of applications using similar data models.

In Script, you can view the data sources used by the script as well as the files output by the script. You can access impact analysis and lineage information for your script as well as their inputs and outputs.

Scripts can be set up to run on a predefined schedule or on-demand.

For an overview of scripts in catalog, see [*Navigating scripts in catalog*](navigating-scripts.htm).

A script open in Script

![Script editor overiew, open to the Summary tab. There are two outputs displayed in the Outputs section and two inputs listed in the Inputs section.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_script-editor-overview-rev.png "Click to view full size")

## Permissions

Your ability to create, view, and delete scripts is dependent on the type of space in which you are working and your permissions in that space.

[*Managing permissions in shared spaces*](../Spaces/managing-shared-spaces.htm)

[*Managing permissions in managed spaces*](../Spaces/managing-managed-spaces.htm)

## Creating scripts

You can create scripts by going to the Create page of the Analytics activity center and selecting Script. You can also create scripts from Prepare data in Analytics or by clicking Create new in Catalog. You can also create a script from a dataset by clicking ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the dataset and select Use in > Script.

When you create a new script, you can specify the destination space of the script. By default, scripts are added to the current space or your personal space if no space is selected.

Once you have created a new script, you can develop the load script used to load data into the script and export files from the script. First, you add data sources to your script in the Editor section of Script. You can then use Qlik scripting functions to transform the loaded data. As you work, you can use Preview data to view the data that will be exported by your load scripts. Finally, add Store statements to store and export the loaded data.

### Adding data sources to scripts

You can add data sources to your load script using Qlik scripting functions. You can use existing data files and connections. You can also add new data sources and connections. You can view existing data sources and add new data sources in Data sources.

#### Adding data from existing datasets

Click Add from data catalog to open the [data catalog](#glossary-1 "Glossary term"). You can add data from multiple datasets.

See: [*Loading data from the data catalog*](../LoadData/adding-data-catalog.htm)

#### Creating connections

Click Create new connection add a connection to your script.

See: [*Loading analytics data*](../LoadData/connect-data-sources.htm)

### Building the load script

Scripts use a data load syntax to connect to and retrieve data from your data sources when running the script.

In your load script, you specify the fields and tables to load. The script can be used to define space-aware connections, allowing you to load data from another space or make your load script look for data sources of a specific name in the current space. For more on space-aware connections, see [*Referring to a data connection in the script*](../LoadData/connect-data-sources-data-load-editor.htm#Referrin).

You can then manipulate the loaded data with functions in the load script. The editor in Script provides you with a broad set of tools for loading and transforming application data. You can perform operations such as:

- Calculating new values
- Translating coded values
- Aggregating values
- Joining or concatenating tables
- Validating data

To learn more about creating load scripts, see:

- [*Editing load scripts*](../LoadData/edit-data-load-script.htm)
- [*Understanding script syntax and data structures*](../LoadData/understand-data-structures.htm)
- [*Script syntax overview*](../Scripting/script-syntax.htm)

All scripts include a default locale and regional settings based on the selections in your profile. For information on changing these settings, see [*Modifying regional settings for applications and scripts*](../Apps/regional-settings-in-apps.htm).

### Previewing data

You can preview data in Editor. This allows you to do a partial load without loading and exporting all the data. You can ignore Store statements and define how many rows of data to preview for each table. To preview your data, click Preview data.

For more information on previewing data, see [*Previewing data in load scripts*](previewing-scripts.htm).

### Exporting data

You can export data using Store statements in your script. You can add them manually in the script or click ![Insert Store statement](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_insert_script_outline.svg) in DataFiles to open Insert Store statement for assisted statement creation. To learn more about storing data, see [*Storing data from load scripts*](storing-data.htm).

To run your script and export, click Export data.

## Inserting scripts into other scripts

You can insert scripts into the load script of other scripts, allowing you to reuse scripting content across multiple applications and other scripts.

For more information, see [*Inserting other scripts into load scripts*](../LoadData/QVS/inserting-qvs-script-editor.htm).

## Script limitations

Scripts have the following limitations

- Unlike applications, scripts do not keep any data that is loaded in the script. Once the session is done, the data is removed. For example, if you previewed data and then closed the script, next time you opened the script there you would need to click Preview data again to generate a new preview.
- Partial loads are not supported for scripts.
- Loading scripts with binary statements is not supported. As scripts do not store the loaded data in the script, loading data from a script with a binary statement results in empty tables.
- Scripts do not support section access.
- Previewing the data (without Use Store statement turned on) does not count as a reload for reload information.
- Exported scripts uploaded into Qlik Sense Enterprise on Cloud Services, Qlik Sense Desktop, or Qlik Sense Mobile will display as applications without data.
- Shared space members with Can manage permission can see the Published copies tab in Overview but cannot see published scripts. If they have Can publish permission, they can see their own scripts.
