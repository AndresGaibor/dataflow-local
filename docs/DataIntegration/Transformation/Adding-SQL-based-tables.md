---
title: "Adding SQL transformations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Transformation/Adding-SQL-based-tables.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to a data warehouse", "Transforming data"]
---

# Adding SQL transformations

You can include SQL-based tables in transformation tasks. A SQL transformation allows you to input a SQL SELECT query into a pipeline to define complex or simple transformations. You can let SQL assistant generate a query from a text prompt using generative AI. You can also use macros to adapt the query to run if an initial load or an incremental load is performed.

You can use SQL workbench to explore data and validate read-only SQL before adding SQL to a transformation. For more information, see [*Exploring data with SQL Workbench*](SQL-workbench-data-exploration.htm).

For more information about creating a transformation task, see [*Transforming data*](Transformations.htm).

## Adding a SQL transformation

To add a SQL transformation in a Transform data task:

1. In Transform, select the datasets to include in the query, and click Add SQL transformation.

   Set the name of the transformation in Name. For more information about the other settings, see [*Settings*](#Settings).

   Click Add when you are ready to create the SQL transformation.

   Edit SQL transformation is displayed.
2. Write the query to return the SQL-based table in the query pane.

   For more information, see [*Editing the SQL query*](#Editing).
3. Click Run query.

   This will fetch metadata and a preview of the data.
4. Review the parameters in Parameters.

   For more information, see [*Parameters*](#Paramete).
5. Set a primary key in Metadata.

   For more information, see [*Metadata*](#Metadata).
6. When you are satisfied with the results of the query, click Save and close. The dataset is now added to the list of targets, and you can preview it.

## Editing the SQL query

Type the query to return the SQL-based table in the query pane. The query can only read from the source datasets that you selected, but you can add more source datasets with Add.

- You can create a statement to load a dataset from Objects. Click ![more](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_vertical.svg) and then Add SELECT statement.
- You can copy the name of a dataset to the clipboard by clicking ![more](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_vertical.svg) and then Copy.
- Click > to move a dataset or column name to the editor.
- Click ![Search](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_search.svg) to search and replace text in the editor.

Information noteYou can use SQL assistant to generate a query using generative AI. For more information, see [*Generating a SQL transformation from a text prompt*](Generating-SQL-from-text-prompt.htm). SQL assistant is not available in Qlik Cloud Government.

If incremental load is used, you can use Macros to adapt the query to run if an initial load or an incremental load is performed.

For more information, see [*Using macros to adapt the query to load type*](#Using).

### Keyboard shortcuts

Information noteKeyboard shortcuts are expressed assuming that you are working in Windows. For macOS, use Command instead of Ctrl.

- Ctrl+F Search and replace
- Ctrl+/ Comment/uncomment the current line
- Ctrl+Enter Run the query
- Ctrl+Z Undo
- Ctrl+Y Redo

### Previewing results

You can preview the results using a sample of the data in Results.

Information noteData preview must be enabled on tenant level in Administration. You can find the Viewing data in Data Integration option in Settings, under Feature control.

You must be assigned the following roles to be able to preview data:

- Can view data in the space where the connection resides.
- Can view in the space where the project resides.

Results using a sample of the data are displayed. You can set how many data rows to include in the sample with Number of rows.

- Click Last executed query to see the last run time and duration of the last executed query.

#### Filtering the results

You can filter the results by one or more columns.

- Click ![more](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_vertical.svg) on the first column to filter by and then Filter.

  Select which operator to use and which value to filter by.

  You can add more column filters by clicking Add filter.

The filter will only affect the existing sample data.

#### Sorting the results

You can sort the data sample by a specific column.

- Click ![more](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_vertical.svg) on the column to sort by and then Sort ascending or Sort descending.

Sorting will only affect the existing sample data. If you used a filter to only include orders from 2024 and invert the sort order, the sample data will still only contain orders from 2024.

#### Managing displayed columns

You can select which columns to display in the results. The selection is not saved when you save the transformation.

- Hide a column by clicking ![more](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_vertical.svg) on the column and then Hide column.
- Manage display of all columns by clicking ![more](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more_vertical.svg) on any column and then Displayed columns.

### Parameters

Click Parameters to change the parameters in the SELECT query. The parameters should be mapped to the source or target objects.

Parameters are automatically mapped when you:

- Use Add SELECT statement in Objects.
- Click > to move a dataset or column name to the editor.
- A parameter name matches a table name from the tables in Objects.

Information noteIf you use arbitrary parameter names, you must map the parameters manually. Only parameter names that match dataset names will be mapped automatically.

You can map to

- History type 2 structures (\_history)
- Current structures
- Target objects

  You can only map target objects when a parameter is defined inside an incremental macro.

Tip noteYou can replace a parameter with a reference to have a query that is easier to read. Change the value in Parameter, and the reference in SELECT query will change as well.

### Metadata

You can edit the metadata settings in Metadata.

- Set primary keys in the Key column.

  You can get suggestions for suitable primary keys, and validate the keys, by clicking Suggest and validate keys.
- Set if the column is nullable in the Nullable column.
- Select a column and click Edit to set column name, key, nullable and data type.

Information note

When you change a primary key, verify that the query returns no duplicate values for the new key before loading data to the next transformation. Duplicate-key handling depends on the target platform. Snowflake does not check for duplicate primary key values by default. A query can succeed and load rows with duplicate key values, producing undefined results. Some target platforms might fail to load the data.

`SELECT DISTINCT` removes identical rows across all selected columns; it does not ensure that the new key is unique when rows differ in other columns. To produce one row per key, group by the new key and aggregate the other columns as needed.

#### Suggesting and validating keys

You can get suggestions for suitable primary keys, and validate the keys, by clicking Suggest and validate keys. The full SQL query must have been run at least once.

- GenAI is used to suggest keys if you have opted in to cross-region inference. This allows Qlik Cloud to send inference requests outside your tenant region. For details and the latest information about inference processing locations, see [*Enabling cross-region inference*](../../Admin/cross-region-data-processing.htm).

  Information noteQlik does not control the generated output. Due to the nature of GenAI, responses may not produce SQL that meets your requirement without review or editing. The generated query is considered “Content” under the terms of Qlik Customer Agreement.

  Qlik Cloud Government note

  GenAI-assisted key suggestion is not available in Qlik Cloud Government.

  If GenAI is not enabled, keys will be suggested programatically based on the source table data.
- Validation will always be performed without using GenAI by running a SQL query making sure that there are no duplicates or NULL values.

  Information noteValidation is only available when the query has returned data.

- Suggest and validate keys

  This will review the query and source table keys, and suggest valid primary keys. This operation may take some time.
- Validate keys

  This will validate the existing primary keys to ensure that they are unique and non-NULL. This operation may take some time.
- Suggest without validation

  This will review the query and source table keys, and suggest primary keys without validation. Review and validate the keys manually before applying them.

## Running the query

You can run the query at any time during development by clicking Run query. The first time you run a query, metadata will be retrieved. When the query is run you can go to Metadata and set a primary key, which is required for the transformation to be complete.

Information noteIf the editor contains more than one query you can run a single query by selecting the query and clicking Run query.

## Using macros to adapt the query to load type

If incremental load is used, you can use Macros to adapt the query to run if an initial load or an incremental load is performed.

Select the macro and add the query inside the respective clause.

- Q\_RUN\_INCREMENTAL adds a clause where you can place a query that is only run when an incremental load is performed.
- Q\_RUN\_INITIAL\_LOAD adds a clause where you can place a query that is only run when an initial load is performed.

You do not need to specify the complete query with each macro. You can adjust or add code based on your use case.

### Use case: Incremental filter using date range:

In this use case, a set of orders data needs to be transformed with custom SQL. Since this is a large dataset, you want to include incremental filtering to ensure that the incremental load only considers orders from the past 12 hours.

This is the base query:

SELECT O.ORDER\_ID, O.CUSTOMER\_ID, OD.PRODUCT\_ID, OD.QUANTITY, O.AMOUNT , OD.LAST\_UPDATE\_DTM
FROM “mydb”.”myStorageTask”.”ORDER” O
JOIN “mydb”.”myStorageTask”.”ORDER\_DETAIL” OD
ON O.ORDER\_ID = OD.ORDER\_ID

This is the filter to apply during the incremental run, where you only consider orders that were added the past 12 hours:

WHERE OD.UPDATE\_DTM > DATEADD(hour, -12, CURRENT\_TIMESTAMP())

Tip noteWhen implementing a SQL-based table, it is recommended to replace the table names with the ${TABLE} notation. This prevents hard-coding database and schema names which may change from environment to environment, for example when moving from development to production.

This is the complete query, using the filter macro and with table names replaced with the ${TABLE} notation:

SELECT O.ORDER\_ID, O.CUSTOMER\_ID, OD.PRODUCT\_ID, OD.QUANTITY, O.AMOUNT , OD.LAST\_UPDATE\_DTM
FROM ${ORDER} O
JOIN ${ORDER\_DETAIL} OD
ON O.ORDER\_ID = OD.ORDER\_ID
{{#QLIK\_FUNC\_IF Q\_RUN\_INCREMENTAL}}
WHERE OD.UPDATE\_DTM > DATEADD(hour, -12, CURRENT\_TIMESTAMP() )
{{/QLIK\_FUNC\_IF}}

This results in an initial load query:

SELECT O.ORDER\_ID, O.CUSTOMER\_ID, OD.PRODUCT\_ID, OD.QUANTITY, O.AMOUNT , OD.LAST\_UPDATE\_DTM
FROM ${ORDER} O
JOIN ${ORDER\_DETAIL} OD
ON O.ORDER\_ID = OD.ORDER\_ID

And an incremental load query:

SELECT O.ORDER\_ID, O.CUSTOMER\_ID, OD.PRODUCT\_ID, OD.QUANTITY, O.AMOUNT , OD.LAST\_UPDATE\_DTM
FROM ${ORDER} O
JOIN ${ORDER\_DETAIL} OD
ON O.ORDER\_ID = OD.ORDER\_ID
WHERE OD.UPDATE\_DTM > DATEADD(hour, -12, CURRENT\_TIMESTAMP() )

### Use case: Incremental filter using data in the target :

In this use case, a set of orders data needs to be transformed with custom SQL. Since orders are a large dataset, you want to include incremental filtering to ensure that the incremental load only considers order details records that are newer than the data in the target table. You also want to mark if a row was processed by the initial load or an incremental load.

Information noteAs you can see by this example, the macros can be used to adjust any part of the query for initial load or incremental load.

This is the base query:

SELECT O.ORDER\_ID, O.CUSTOMER\_ID, OD.PRODUCT\_ID, OD.QUANTITY, O.AMOUNT , OD.LAST\_UPDATE\_DTM
FROM “mydb”.”myStorageTask”.”ORDER” O
JOIN “mydb”.”myStorageTask”.”ORDER\_DETAIL” OD
ON O.ORDER\_ID = OD.ORDER\_ID

This is the filter to apply during the incremental run. “ORDERS\_DERIVED” is the name of the target dataset.

WHERE OD.UPDATE\_DTM > = (SELECT MAX(LAST\_UPDATE\_DTM) FROM “mydb”.”myTrasformTask”.”ORDERS\_DERIVED” )

Tip noteIncremental loading can also map a ${TABLE} notation to the target objects created by the transform task.

This is the complete query, using the filter macro, and with table names replaced with the ${TABLE} notation. LOADED\_BY is set to INIT if the load is initial, and INCR if the load is incremental:

SELECT O.ORDER\_ID, O.CUSTOMER\_ID, OD.PRODUCT\_ID, OD.QUANTITY, O.AMOUNT, OD.LAST\_UPDATE\_DTM,
{{#QLIK\_FUNC\_IF Q\_RUN\_INITIAL\_LOAD}} ‘INIT’ as LOADED\_BY {{/QLIK\_FUNC\_IF}}
{{#QLIK\_FUNC\_IF Q\_RUN\_INCREMENTAL}} ‘INCR’ as LOADED\_BY {{/QLIK\_FUNC\_IF}}
FROM ${ORDER} O
JOIN ${ORDER\_DETAIL} OD
ON O.ORDER\_ID = OD.ORDER\_ID
{{#QLIK\_FUNC\_IF Q\_RUN\_INCREMENTAL}}
WHERE OD.UPDATE\_DTM >= (SELECT MAX(LAST\_UPDATE\_DTM) FROM ${TARGET\_TABLE} )
{{/QLIK\_FUNC\_IF}}

This results in an initial load query:

SELECT O.ORDER\_ID, O.CUSTOMER\_ID, OD.PRODUCT\_ID, OD.QUANTITY, O.AMOUNT, OD.LAST\_UPDATE\_DTM, ‘INIT’ as LOADED\_BY
FROM ${ORDER} O
JOIN ${ORDER\_DETAIL} OD
ON O.ORDER\_ID = OD.ORDER\_ID

And an incremental load query:

SELECT O.ORDER\_ID, O.CUSTOMER\_ID, OD.PRODUCT\_ID, OD.QUANTITY, O.AMOUNT, OD.LAST\_UPDATE\_DTM, ‘INCR’ as LOADED\_BY
FROM ${ORDER} O
JOIN ${ORDER\_DETAIL} OD
ON O.ORDER\_ID = OD.ORDER\_ID
WHERE OD.UPDATE\_DTM >= (SELECT MAX(LAST\_UPDATE\_DTM) FROM ${TARGET\_TABLE} )

## Settings

Click ![Settings](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) to edit the settings of the SQL transformation.

- Enter a name for the target dataset in Name.

  You can also add a longer description in Description.
- In Materialization, select if the transformed output should be materialized or not. You can choose to inherit the setting from the data task settings.

  - On will create tables and will handle associated ELT processing.
  - Off will create views that perform transformations on the fly.
- In Historical Data Store (Type 2), select if you want to keep historical data. You can choose to inherit the setting from the data task settings. This setting requires that Materialization is on.
- Incremental load allows you to adjust the query for an incremental data load by applying filters or other conditions to reduce the set of data being processed using macros. Incremental load is only available if the data is materialized as tables.

  - When Incremental load is On

    The first execution of the task will perform an initial load, inserting all results of the query into your target table. Subsequent executions will execute incremental loads leveraging filters or specific conditions you have defined for incremental processing. During incremental load, the task will only process data as an update or an insert, deletes are not managed.
  - When Incremental load is Off

    The first execution of the task will perform an initial load, inserting all results of the query into your target table. Subsequent executions will process all results of the query by comparing to your target table, and processing records that are new, changed or deleted.

  Information noteIf the query will select all records that should exist in the target, set Incremental load to off. Records that are not selected will be deleted in the target.

## Best practice

- When you add a SQL transformation, a primary key is not defined automatically. Add a key to the dataset in the Dataset tab.
- Do not create column headers in the transformed output manually.
- Avoid using SELECT with \*, as this may return different columns each time the query is run. If there was a change in the schema, change the query accordingly and perform Describe table again. Then you can edit columns and adjust tables.
