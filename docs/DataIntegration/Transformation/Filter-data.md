---
title: "Filtering a dataset"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Transformation/Filter-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Managing datasets"]
---

# Filtering a dataset

You can add a filter to a dataset to reduce the set of data values in Landing data tasks that land data through Qlik Data Gateway - Data Movement, Storage, and Transform data tasks.

You can either filter the data during loading or - if SAP ODP or SAP OData is your data source - directly on the data source itself.

## Filtering during data loading

This method filters the data in memory during data loading. Use this method if your data source is not SAP ODP or SAP OData, or if your data source is SAP ODP or SAP OData and you need to define or edit a complex expression on a dataset.

Information noteIf your data source is SAP ODP or SAP OData, best practice is to filter directly on the data source as described in [*Filtering on the data source*](#Filterin) below.

To filter a dataset

Information noteTesting calls to `$SOURCE_LOOKUP` and `$TARGET_LOOKUP` is not supported.

1. Open the data task.
2. Click Datasets and then select the dataset you want to filter.
3. Click the Filter button on the top right.

   If your data source is SAP ODP or SAP OData, select During data loading from the drop-down menu.

   The expression builder opens.
4. Build an expression to define the filter. The filter should evaluate to a true value for the data rows to keep.

   For shared editor guidance, see [*Building expressions*](Building-expressions.htm).

   You can use columns in the dataset, functions, and operators.

   Click ![Right arrow icon](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_right.svg) to move an item to the expression.

   You can also use all functions supported by the cloud data platform.

   Information noteIf you use Azure Synapse Analytics as data platform, $RTRIM and $LTRIM will only trim space characters regardless of which character you specify to trim.
5. Click Extract parameters.

   You can now add a test value to Value to test for all parameters.
6. Click Test expression.

   You should now see the result of the filter expression, using the test values.
7. Click OK to save the filter.

   The funnel on the Filter button becomes green indicating that a filter has been defined for that dataset.

   You can see the filter expression by hovering on the Filter button.

## Filtering on the data source

This method filters the data directly on the data source and is only available for the SAP ODP and SAP OData data sources. Filtering directly on the data source prevents high volumes of data being transferred unnecessarily to the Data Movement gateway machine. This both improves performance and alleviates cost uncertainty, which makes it easier to meet project deadlines.

To filter a dataset

1. Open the data task.
2. Click Datasets and then select the dataset you want to filter.
3. Click the Filter button on the top right and then select On data source from the drop-down menu.

   The Add/Edit "On data source" filter: <dataset> dialog opens.

   Information noteColumns that are filtered are indicated with a ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_filter.svg) icon.
4. Select a column in the left pane and then define Include or Exclude criteria in the "<column name>" filtering criteria pane on the right.

   For example, selecting the BIRTHDATE column and defining Include - Less than or equal to - 19700101 will exclude all records with birth dates after the specified date.
5. To define additional filtering criteria for the same column, click Add.
6. To remove filtering criteria for a column, click the ![](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin_outline.svg)icon next to the criteria.
7. Repeat Step 3 to define filters on additional columns.
8. To view the filter details, expand the Filter summary pane at the bottom of the dialog.
9. Click OK to save the filter.

   The funnel on the Filter button becomes green indicating that a filter has been defined for that dataset.

Information noteEditing the filter requires you to prepare and run the task again.
