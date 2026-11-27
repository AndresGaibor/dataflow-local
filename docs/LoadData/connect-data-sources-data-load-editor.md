---
title: "Connect to data sources in load scripts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/connect-data-sources-data-load-editor.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Scripting to load or export data"]
---

# Connect to data sources in load scripts

[Data connections](#glossary-0 "Glossary term") in [Data load editor](#glossary-1 "Glossary term") and Script let you save shortcuts to the data sources you commonly use: databases, local files, or remote files.

Data connections lists the connections you have saved in alphabetical order grouped by the spaces to which they belong. You can use the search box to narrow the list down to connections with a certain name or type. You can access Data connections by clicking Data sources.

Information noteYou can only see data connections that you own, or have been given rights to access. Please contact your Qlik Sense system administrator to acquire access if required.

## Creating a new data connection

Do the following:

1. Click Data sources.
2. Click Create new connection.
3. Under Space, select the space where the connection will be located.
4. Select the type of data source you want to create from the drop-down list.

   The settings dialog, specific for the type of data source you selected, opens.
5. Enter the data source settings and click Create to create the data connection.

## Deleting a data connection

Do the following:

1. Click Data sources.
2. Click ![Delete](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin_outline.svg) on the data connection you want to delete.
3. Confirm that you want to delete the connection.

The data connection is now deleted.

## Editing a data connection

Do the following:

1. Click Data sources.
2. Under Data connections, select the space containing the data connection you want to edit.
3. Click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) on the data connection you want to edit.
4. Edit the data connection details. Connection details are specific to the type of connection.

   You may need to provide the connection's credentials.

The data connection is now updated.

Information noteIf you edit the name of a data connection, you also need to edit all existing references (lib://) to the connection in the script, if you want to continue referring to the same connection.

## Editing data connection credentials

Some data connectors support User defined credentials. With proper permissions, you can add, edit, and remove your own sets of credentials for a data connection, including for connections you do not own.

For more information, see the connectors documentation at [Data sources in Qlik Cloud Analytics](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Helpsites/Connectors_SaaS.htm).

Do the following:

1. Click Data sources.
2. Under Data connections, select the space containing the data connection.
3. Click ![Edit credentials](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_key_outline.svg) on a connection that has User defined credentials turned on.

   A dialog opens.
4. In the drop down menu, select an existing credentials set to edit, or create new credentials.

   You can also delete existing credentials.
5. Edit the credential settings.
6. Click Apply.

## About DataFiles connections

DataFiles connections are automatically created for each space you can access. The connections are available from each space section under Data Connections.

Information noteThe file extension of DataFiles connections is case sensitive. For example: .qvd.

## Selecting data from a data connection

If you want to select data from a data connection to load in your application do the following:

1. Click Data sources.
2. Create new connection linking to the data source (if the data connection does not already exist).
3. ![Data Selection](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok_outline.svg) Select data from the connection.

## Referring to a data connection in the script

You can use the data connection to refer to data sources in statements and functions in the script, typically where you want to refer to a file name with a path.

The following list outlines rules for referencing data files in load scripts within Qlik Cloud Analytics:

- The syntax for referring to a file in the load script is:

  [lib://(space\_name):DataFiles/(folder\_name)/(file\_name)]
- If the space name is omitted, the current space is used. For examples, see [*Data sources for applications in managed spaces*](../Spaces/app-data-managed-spaces.htm).
- The full folder path must be provided. Relative paths are not supported.
- The folder path can include multiple folders in a hierarchical structure. Each folder\_name in the path must be delimited with / characters.
- The following are not allowed in the path when referencing files residing in a folder structure:

  - //
  - \
  - \\
  - /./
  - /../
- Trailing period symbols (.) in the space, folder, or file name are acceptable as long as they do not appear in the configurations in the above list.
- You need to reference the underlying data file, not the dataset for the file. A dataset can have a different name than its underlying data file. For more information about the differences between data files and datasets, see [*Distinctions between data files and datasets*](../Catalog/data-files-and-datasets.htm).

Examples: Non-compliant syntax

These examples are considered invalid syntax for the path:

Load [Transactions] from 'lib:\\Demo:DataFiles\Sales2024\France.qvd';

store [Transactions] into 'lib://Demo:DataFiles/Sales2024/./France.qvd';

Load [Transactions] from 'lib://Demo:DataFiles/Sales2024/../France.qvd';

store [Transactions] into 'lib://Demo:DataFiles//Sales2024//France.qvd';

Depending on the type of script statement being used, non-compliant syntax might cause reload failure, or could still be executed with different behavior. For specific details, see:

- [Loading data from files](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/manage-data-files-spaces.htm)
- [Storing data into files](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/manage-data-files-spaces.htm)

You do not need to add the space\_name if you are connecting to a [personal space](#glossary-3 "Glossary term").

Example: Loading a file from a DataFiles connection

This example loads the file orders.csv from a personal space defined in the Data data connection.

```
LOAD * FROM [lib://DataFiles/orders.csv];
```

This example loads the file orders.csv from a [shared space](#glossary-4 "Glossary term") defined in the Data data connection.

```
LOAD * FROM [lib://TeamSharedConnection:DataFiles/orders.csv];
```

This example loads the file orders\_Europe.csv from the folder Orders By Region within a personal space.

```
LOAD * FROM [lib://DataFiles/Orders By Region/orders_Europe.csv];
```

This example loads the file orders\_Europe.csv from the folder Orders By Region within a [shared](#glossary-5 "Glossary term"), [managed](#glossary-6 "Glossary term"), or [data space](#glossary-7 "Glossary term"). The name of the space is SalesSpace.

```
LOAD * FROM [lib://SalesSpace:DataFiles/Orders By Region/orders_Europe.csv];
```

This example loads the file orders.csv from the current space. If the application is moved to another space, for example, it will use the file orders.csv in the new space.

```
LOAD * FROM [lib://:DataFiles/orders.csv];
```

Example: Loading from a database in the current user's personal space

This example loads the table Sales\_data from the DataSource database connection in a user's personal space.

```
LIB CONNECT TO 'DataSource';
LOAD *;
SQL SELECT * FROM `Sales_data`;
```

Example: Loading from a database in another space

This example loads the table Sales\_data from the DataSource database connection in the current space.

```
LIB CONNECT TO ':DataSource';
LOAD *;
SQL SELECT * FROM `Sales_data`;
```

Example: Loading from a database in a specific space

This example loads the table Sales\_data from the DataSource database connection in the space SalesSpace.

```
LIB CONNECT TO 'SalesSpace:DataSource';
LOAD *;
SQL SELECT * FROM `Sales_data`;
```

Examples: Loading from analytic connections

The following examples show how to write expressions to load data from analytic connections. Use the SSE syntax to connect to data from an analytic connection.

These examples demonstrate the use of the connections in scripts. For examples showing how to reference analytic connections in charts, see [*Using analytic connections and server-side extensions syntax*](load-data-from-advanced-analytic-connections.htm#Using).

Loading from an analytic connection in the current space

```
EXTENSION endpoints.ScriptEval('{"RequestType":"endpoint", "endpoint":{"connectionname":":Amazon_Titan_(Amazon_Bedrock)"}}', QuestionsTable{Question_ID,Question});
```

Loading from an analytic connection in the current user's personal space

```
EXTENSION endpoints.ScriptEval('{"RequestType":"endpoint", "endpoint":{"connectionname":"Amazon_Titan_(Amazon_Bedrock)"}}', QuestionsTable{Question_ID,Question});
```

Loading from an analytic connection in a specific space

This example loads data from the connection named Amazon\_Titan\_(Amazon\_Bedrock) in the space SalesSpace.

```
EXTENSION endpoints.ScriptEval('{"RequestType":"endpoint", "endpoint":{"connectionname":"SalesSpace:Amazon_Titan_(Amazon_Bedrock)"}}', QuestionsTable{Question_ID,Question});
```

Related learning:

- [Introduction to the data load editor](/lnk/Intro_Data_Load_Editor_QS)
- [Loading Data from a Database](/lnk/Loading_data_from_database_QS)
