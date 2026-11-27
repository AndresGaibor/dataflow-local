---
title: "Storing data from load scripts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ScriptEditor/storing-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Scripting to load or export data"]
---

# Storing data from load scripts

Store data using the Store statement. You can store tables as QVD, PARQUET, CSV, or TXT files.

Data load editor and Script include an option, Insert Store statement, to create and format a Store statement.

Insert Store statement

![Insert Store statement dialog, with no parameters configured.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_insert-store-rev.png "Click to view full size")

You can also add and format your own Store statements in your script, which have additional options. For more information, see [*Store*](../Scripting/ScriptRegularStatements/Store.htm).

Do the following:

1. In Data sources, click ![Insert Store statement](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_insert_script_outline.svg) on a data source.
2. After Store, enter the name of the table to store.
3. After Path, enter the destination path for the stored file.

   Click ![Browse icon](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_folder_open.svg) to browse for the path.

   Information note

   For Google Drive targets, folders are specified by ID, not by name or folder path. You must enter the folder ID in the file portion followed by a path separator and the file name. For example:

   ```
   STORE [SampleTable] INTO [lib://<connection-name>/<folder-ID>/test.parquet](parquet);
   ```

   You can obtain the folder ID by logging into your Google Drive account.
4. After File, enter the output name and a select the file type.
5. Click Insert.

   The statement is inserted in your script.

## Limitations

Inserting Store statements has the following limitations:

- Insert Store statement (![Insert Store statement](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_insert_script_outline.svg)) is not available with OneDrive connections.
