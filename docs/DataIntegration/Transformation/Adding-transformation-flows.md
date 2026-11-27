---
title: "Adding transformation flows"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Transformation/Adding-transformation-flows.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Onboarding data to a data warehouse", "Transforming data"]
---

# Adding transformation flows

You can include flows in transformation tasks. The flow designer allows you to create a transformation flow using sources, processors and targets to define complex or simple transformations.

Transformation flows and processors are logical representations. It means that in ELT tasks, only one table is created for each target, and that all processors are compiled into a single SQL statement per target.

## Supported target platforms

The following platforms are supported with transformation flows:

- Snowflake
- Databricks
- Google BigQuery
- Azure Synapse Analytics
- Microsoft Fabric
- Microsoft SQL Server
- Amazon Redshift

  Information noteThe following Amazon Redshift functions are not available: UUID string generation and Edit Distance.

## Prerequisites

Before you create a transformation flow, you must:

- Populate the storage task with onboarded data that you want to use in the transformation flow, or register existing data. For more information about how to onboard and register data, see [*Onboarding data to a data warehouse*](../Onboarding/Onboarding-data.htm) and [*Registering data that is already on the data platform*](../Onboarding/Registering-data.htm).
- Prepare and run the storage or transform task used as a source in your transformation flow. Running the storage task is not mandatory, but it is recommended to be able to display data preview
  at every step of the flow.

## Creating a transformation flow

To create a valid transformation flow, you need at least one source dataset, and one named target with defined keys.

1. Open the Transform data task in your data pipeline.
2. In Transform, select the source datasets to include in the transformation flow, and click Add transformation flow.

   Add transformation flow is displayed where you can provide settings for the transformation.
3. Enter a name for the target dataset in Name.

   You can also add a longer description in Description.
4. In Materialization, select if the transformed output should be materialized or not. You can choose to inherit the setting from the data task settings.

   - On will create tables and will handle associated ELT processing.
   - Off will create views that perform transformations on the fly.
5. In Historical Data Store (Type 2), select if you want to keep historical data. You can choose to inherit the setting from the data task settings. This setting requires that Materialization is on.
6. Incremental load allows you to adjust the query for an incremental data load by applying filters or other conditions to reduce the set of data being processed using macros. Incremental load is only available if the data is materialized as tables.

   - When Incremental load is On

     The first execution of the task will perform an initial load, inserting all results of the query into your target table. Subsequent executions will execute incremental loads leveraging filters or specific conditions you have defined for incremental processing. During incremental load, the task will only process data as an update or an insert, deletes are not managed.
   - When Incremental load is Off

     The first execution of the task will perform an initial load, inserting all results of the query into your target table. Subsequent executions will process all results of the query by comparing to your target table, and processing records that are new, changed or deleted.

   Information noteIf the query will select all records that should exist in the target, set Incremental load to off. Records that are not selected will be deleted in the target.
7. Click Add when you are ready to create the transformation flow.

   The flow designer opens, the target is created and displayed in your flow as a target component.

   Information noteIt is mandatory to provide a unique name for your flow target. If you want to rename the flow target later, select the target and enter the new name in Dataset name.
8. If no keys are defined for your target, click Edit next to the Key(s) & nullables field. The configuration window opens.

   Information noteKeys are not inherited from source datasets and must be manually defined. Nullables are inherited from source datasets and can be modified.
9. In Configure keys and nullables, select Key in the column you want to define as primary key, and select Nullables in the column or columns you want to define as nullable.
10. Click Confirm to save your changes and close the configuration window.

Information note

When you change a target primary key, verify that the flow produces no duplicate values for the new key before loading data to the next transformation. Duplicate-key handling depends on the target platform. Snowflake does not check for duplicate primary key values by default. A query can succeed and load rows with duplicate key values, producing undefined results. Some target platforms might fail to load the data.

The [*Select columns processor*](Processor-select-columns.htm) processor can remove identical output rows with its Distinct option, but this does not ensure unique key values when other columns differ. To produce one row per key, use the [*Aggregate processor*](Processor-aggregate.htm) processor to group by the new key and aggregate other columns.

If the status of your transformation flow is valid, you can close the flow and prepare your data.

You can change the settings for Materialization and Incremental load later in Target settings.

- Select the target and click Edit next to Settings in the target configuration.

## Adding a processor

You can add processors to your flows.

Processors are components that you can add to your flows in order to transform your incoming data and return the transformed data to the next step of the flow.

1. In the flow designer, select the flow component after which you want to add a processor.
2. Click ![Vertical ellipsis icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/ic_VerticalEllipsis.png) in the flow component, then Add processor, and select which processor to add. You can also drag the processor from the left panel to the canvas.

Tip noteA short description of the processor can be displayed by selecting the processor from the Processors panel.

3. Configure your processor according to your needs, and click Save to save your changes and update the data preview.

   Information noteYou can preview a sample of your data using SQL and Data preview. For more information, see [*Previewing results*](Adding-SQL-based-tables.htm#Previewi).

### Available processors

![Aggregate](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/ic_ProcessorAggregate.png)

### [*Aggregate processor*](Processor-aggregate.htm)

![Aggregate](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_sparkle.png)

### [*AI processor*](Processor-ai.htm)

![Cleanse](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/ic_ProcessorCleanse.png)

### [*Cleanse processor*](Processor-cleanse.htm)

![Concatenate](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/ic_ProcessorConcatenate.png)

### [*Concatenate processor*](Processor-concatenate.htm)

![Filter](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/ic_ProcessorFilter.png)

### [*Filter processor*](Processor-filter.htm)

![Fork](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/ic_ProcessorFork.png)

### [*Fork processor*](Processor-fork.htm)

![Hash](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/ic_ProcessorHash.png)

### [*Hash processor*](Processor-hash.htm)

![Incremental filter](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/ic_ProcessorIncrementalFilter.png)

### [*Incremental filter processor*](Processor-incremental-filter.htm)

![Join](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/ic_ProcessorJoin.png)

### [*Join processor*](Processor-join.htm)

![Math](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/ic_ProcessorMath.png)

### [*Math processor*](Processor-math.htm)

![Numbers](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/ic_ProcessorNumbers.png)

### [*Numbers processor*](Processor-numbers.htm)

![Remove columns](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/ic_ProcessorRemoveColumns.png)

### [*Remove columns processor*](Processor-remove-columns.htm)

![Select columns](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/ic_ProcessorSelectColumns.png)

### [*Select columns processor*](Processor-select-columns.htm)

![SQL Expression](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/ic_ProcessorSQLExpression.png)

### [*SQL expression processor*](Processor-sql-expression.htm)

![Strings](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/ic_ProcessorStrings.png)

### [*Strings processor*](Processor-strings.htm)

![Union](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/ic_ProcessorUnion.png)

### [*Union processor*](Processor-union.htm)

### Use case: Joining, aggregating and filtering data on Snowflake

In this use case, Snowflake customer data needs to be transformed with processors. Since customer information comes from two datasets, you want to add a Join processor first to combine records. You also want to use an Aggregate processor to calculate the average price of orders, and a Filter processor to filter on the type of customer records that you want to keep in your output datasets.

![A transformation flow with a Join processor, an Aggregate processor and a Filter processor.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/ui_TransformationFlowCanvas.png)

The first dataset is based on a Snowflake table called CUSTOMER\_ACCOUNT and its schema looks like this:

![Snowflake table schema about customer accounts](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/ui_TransformationFlowCustomerAccount.png)

The second dataset is based on a Snowflake table called CUSTOMER\_ORDER and its schema looks like this:

![Snowflake table schema about customer orders](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/ui_TransformationFlowCustomerOrder.png)

1. Drag a Join processor from the Processors left panel onto the canvas.
2. Link the second source to the Join processor so that data from both datasets
   can be combined.
3. Configure the Join processor to join the two source datasets on the customer ID keys (CUSTOMER\_ID) .
4. Drag an Aggregate processor after the Join processor.
5. Configure the Aggregate processor to calculate the average customer purchase amount (ORDER\_TOTAL\_PRICE) and store it in a new column that you can name avg\_order\_price, while grouping records by customer segment type (LEFT\_CUSTOMER\_SEGMENT).
6. Drag and drop a Filter processor from the Processors left panel onto the canvas.
7. Configure the Filter processor to filter on the business customer types (Business).
8. Select ![Vertical ellipsis icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/ic_VerticalEllipsis.png) on the Filter processor to open the menu, and click Add non-matching target to add a second target to your flow.

   This target will contain the records that did not match the filter criteria, the individual customer types (Individual).
9. Enter a name for the new target dataset, individual\_cust for example.
10. Check the output preview in both targets:

    The business\_cust target shows the average order price for Business customer types, here 157.463687151.

    ![Output showing the average order price of business customer types](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/ui_TransformationFlowBusinessOutput.png)

    The individual\_cust target shows the average order price for Individual customer types, here 153.576530612.

    ![Output showing the average order price of individual customer types](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/TransformationFlow/ui_TransformationFlowIndividualOutput.png)
11. Make sure your transformation flow has a valid status, then close it.
12. In the Transform window, click Prepare to prepare your data.

## Limitations and considerations

In transformation flows, the following data types cannot be used directly as values in processors such as Cleanse, Hash, or Filter:

- TIME
- DATE
- DATETIME
- JSON

To work with these data types, first convert them into supported formats (for example, STRING or NUMERIC) and then use them in these processors.

## Best practice

When you add source or target datasets to your flows, you should set the keys and nullables in the configuration panel of the target datasets.
