---
title: "Landing dataset segments in parallel"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Landing/Table-settings-landing.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to a data warehouse"]
---

# Landing dataset segments in parallel

During full load, you can accelerate the loading of large datasets by splitting the dataset into segments, which will be loaded in parallel. Tables can be split by data ranges, all partitions, all subpartitions, or specific partitions.

Information noteIf you are using Data Movement gateway, this feature is supported from version 2024.5.35.

Each dataset segment is loaded using a separate sub-task. Therefore, when deciding how to split a dataset, you should always take into account the availability of database and network resources. Splitting a table into too many segments might impact database performance and overburden network capacity. If you choose the Data ranges segmentation method with a partitioned dataset, best practice is to set up the ranges so that each range covers one or more entire partitions. This will expedite data retrieval and minimize the impact on database processing resources.

## Supported data sources and targets

The data task must be defined with a combination of the following data source and target connectors.

Supported data source connectors

- IBM DB2 for LUW
- IBM DB2 for z/OS

  Information note

  Table segmentation by partitions or subpartitions is not supported with the IBM DB2 for z/OS source connector.
- Microsoft SQL Server (log based)
- MySQL
- Oracle
- PostgreSQL

  Information note

  Table segmentation by partitions or subpartitions is not supported with the PostgreSQL source connector.
- SAP (Application)

  Information note

  Tables with the SAP (Application) source endpoint are client dependent by default. The MANDT column is automatically taken directly from the connector.
- SAP HANA (Database)

Supported target connectors

- Amazon Redshift
- Google Cloud BigQuery
- Microsoft Fabric
- Microsoft SQL Server
- Snowflake
- Databricks - If you are using Data Movement gateway, version 2025.11.1 or later is required.

## Setting up parallel load

You can split a table using one of two methods: Data ranges or Partitions. The Data ranges method splits the table by data ranges while the Partitions method splits the table according to partitions.

### Using the data ranges method

To define segment boundaries by data range:

1. Select the Data ranges segmentation method.
2. Click Select columns.

   The Table segmentation columns dialog opens
3. For all supported data sources, the Unique Index column is automatically selected. Select which additional columns with data you want to use to delineate the ranges, and then click OK.

   Information note
   - It is recommended to use columns that do not allow NULLs and that are not updated during normal source database operations (for example, a primary key column or a date column with a fixed date). Using a column that is updated during full load might cause duplicates in the target database.
   - It is recommended to use indexed source columns as this will optimize data retrieval performance.
   - Up to ten columns can be selected
   - Records with null values will not be replicated
   - The following data types cannot be used to define segments by ranges: DOUBLE, FLOAT, and LOB (BLOB, CLOB, NCLOB)
4. Click Add data range to add a data range segment.

   The Add data range dialog will open with your selected columns.
5. For each column, enter the upper data range of the segment.

   Information note

   Values in DATE columns must be entered in the format supported by the source. For example, for an Oracle source, the correct format would be:

   - ALTER SESSION SET NLS\_DATE\_FORMAT:

     'YYYY-MM-DD HH24:MI:SS' (specifying YYYY-MM-DD only is also valid)
   - ALTER SESSION SET NLS\_TIMESTAMP\_FORMAT:

     'YYYY-MM-DD HH24:MI:SS.FF9'
   - ALTER SESSION SET NLS\_TIMESTAMP\_TZ\_FORMAT:

     'YYYY-MM-DD HH24:MI:SS.FF9 TZH:TZM'
6. Click OK to save your settings and close the dialog.

   Each of the selected columns will appear with its specified range.
7. Repeat steps 3-6 as required to add columns and data ranges.
8. Click Validate to validate that the data you entered corresponds to the source column data type and that all of the defined segments contain values.

Information note

With the Data ranges segmentation method, all of the table data will be replicated, even if data ranges are not defined for all of the columns.

To edit a data range:

1. Click the ![More icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_catmore.svg) menu at the end of the row and select Edit.
2. Edit the data range as required and click OK to save your changes.

To delete a data range:

1. Click the ![More icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_catmore.svg) menu at the end of the row and select Delete.
2. When prompted to confirm the deletion, click Delete.

#### Usage example

Let's assume that the following segments are defined:

Example table data

| Column\_1 | Column\_2 | Column\_3 |
| --- | --- | --- |
| 10 | 30 | 105 |
| 20 | 20 | 120 |
| 100 | 12 | 99 |

In this case, the following "WHERE" clauses will be created for each load segment:

- Segment 1:((COL1 < 10) OR ((COL1 = 10) AND (COL2 < 30)) OR ((COL1 = 10) AND (COL2 = 30) AND (COL3 < 105)))
- Segment 2:NOT ((COL1 < 10) OR ((COL1 = 10) AND (COL2 < 30)) OR ((COL1 = 10) AND (COL2 = 30) AND (COL3 < 105))) AND ((COL1 < 20) OR ((COL1 = 20) AND (COL2 < 20)) OR ((COL1 = 20) AND (COL2 = 20) AND (COL3 < 120)))
- Segment 3:NOT ((COL1 < 20) OR ((COL1 = 20) AND (COL2 < 20)) OR ((COL1 = 30) AND (COL2 = 20) AND (COL3 < 120))) AND ((COL1 < 100) OR ((COL1 = 100) AND (COL2 < 12)) OR ((COL1 = 100) AND (COL2 = 12) AND (COL3 < 99)))
- Segment 4:NOT ((COL1 < 100) OR ((COL1 = 100) AND (COL2 < 12)) OR ((COL1 = 100) AND (COL2 = 12) AND (COL3 < 99)))

### Using the partitions method

You can define segment boundaries by all of the table partitions, all of the table's subpartitions (if the data source support subpartitions), or by specific partitions.

Information note

- This method can only be used if the dataset is already partitioned.
- If you have a task that existed before this feature was released, and you either did not start the task yet or want to parallel reload one of more of the tables using this method, you first need to refresh the metadata, as described in [*Registering data that is already on the data platform*](../Onboarding/Registering-data.htm) (The metadata refresh process described in this topic is the same for all types of data task).

#### Using all partitions

To define segment boundaries by all of the table partitions or subpartitions:

1. In the Datasets tab, click the![More icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_catmore_vertical.svg)menu to the right of the dataset and select Settings.

   The Parallel load dialog opens.
2. Select the Partitions segmentation method.
3. Select one the following:

   - Use all main partitions
   - Use all subpartitions

     Information note

     This option will be disabled if the data source does not support subpartitions.
4. Click OK.

#### Using specific partitions

To define segment boundaries by specific partitions:

1. In the Datasets tab, click the![More icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_catmore_vertical.svg)menu to the right of the dataset and select Settings.

   The Parallel load dialog opens.
2. Select the Partitions segmentation method.
3. Select Specify partitions.

   Information note

   When Specify partitions is selected, only the specified partitions will be replicated.
4. Click Add partition.

   The Add partition dialog opens.
5. Specify the name of an existing partition or subpartition.

   If you are adding a subpartition, select the Subpartition check box.
6. Click OK to save your settings.
7. Repeat steps 4-6 as required to add partitions or subpartitions.

To edit a partition:

1. Click the ![More icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_catmore.svg) menu at the end of the row and select Edit.
2. Edit the partition information as required and click OK to save your changes.

To delete a partition:

1. Click the ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_catmore.svg) menu at the end of the row and select Delete.
2. When prompted to confirm the deletion, click Delete.

## Adjusting the number of segments that can be loaded in parallel

You can increase or decrease the number of segments that will be loaded in parallel. The value is inherited from the Full load > Performance tuning > Maximum number of tables to load in parallel field in the data task settings. The current value is displayed in the "Up to <n> segments can be loaded in parallel" string in the Parallel load dialog. Increasing the number might boost performance when a dataset is split into many segments, but will also put a greater strain on database resources and network capacity.

Information noteEach segment is loaded using a dedicated sub-task so, for example, if you select the Use all main partitions option and the source dataset has 20 main partitions, increasing the Maximum number of tables to load in parallel value to 15 will result in 15 segments (partitions) being loaded in parallel. When the sub-tasks complete their run, they will be assigned to loading the remaining 5 partitions.
