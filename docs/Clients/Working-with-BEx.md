---
title: "Working with BEx and BW queries using a SAP BW connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Connectors_SAP/Clients/Working-with-BEx.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "SAP NetWeaver", "SAP Connector clients", "Using the SAP BW Connector"]
---

# Working with BEx and BW queries using a SAP BW connection

The BW Connectorcan extract data from BEx and BW queries in SAP BW.

## How the BW Connector works

The load script for the BW Connector consists of five parts:

- Dimensions
- Measures
- Units
- Texts
- Variables

This information is sent to function modules on the SAP BW side where the BEx or BW query is executed. Once the query execution is complete and the result is in a temporary table in SAP, the result is sent back to Qlik by way of the connector. The function modules used for metadata extraction and query execution is a mixture of SAP-delivered code and custom development.

## When to use the BW Connector

You can access existing logic in SAP BW, such as:

- Restricted and calculated key figures
- Characteristic text
- Key values

However, there are limitations. See, [*Limitations and suggested workarounds*](#Limitati).

## Select and load data from an SAP BW connection

Once a connection to SAP has been established, you can select data and load it into a Qlik Sense application.

Do the following:

1. Select the SAP BW Connector from the list of data connections.
2. Define the extraction parameters for the desired BEx or BW query.

   Load texts, Load attributes, and Show friendly names only affect InfoProvider extraction. See [*Working with InfoProviders using a SAP BW connection*](Working-with-InfoProviders.htm).
3. Select Provider Types. You might want to filter on BEx Provider Types to limit the list of BW objects below.
4. Select BW Objects. Select the BEx/BW queries whose data you want to load.

   You can filter the BEx/BW queries list using the search field above the list. You can choose to load data from one or moreBEx/BW queries at a time. Clicking on the BEx/BW name causes all of its fields to be displayed.

   Information noteIt is recommended to only select only one query at a time.
5. Select Include LOAD statement, if not already checked, to create a LOAD statement before the SELECT statement.

   The LOAD statement before the SELECT statement allows the LOAD statement to use the SELECT statements as input. Basically, it is a LOAD statement that loads from the LOAD or SELECT statement below, without specifying a source qualifier, such as From or Resident. You can stack any number of LOAD statements this way. The statement at the bottom will be evaluated first, then the statement above, and so on until the top statement has been evaluated. Another advantage of the LOAD preceding SELECT is that you can keep a calculation in one place and reuse it in LOAD statements placed above. For example, when you load data from a database using a SELECT statement, you cannot use Qlik Sense functions to interpret data in the SELECT statement. The solution is to add a LOAD statement and perform data transformations above the SELECT statement.

   The LOAD statement created in the script panel is a simple load.
6. Select Metadata.

   Information noteIt is recommended to start the extraction configuration with the Metadata selection and the Conditions definition. For very large queries, you can set some granular filters through conditions before accessing the Preview window.
7. Select the fields whose data you want to load.

   You can filter the fields shown by using the search field ![Search](../_images/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Resources/Images/Icons/ic_search.svg) above the list of fields. When selecting fields, you can click the Metadata button to see which fields are primary key fields.
8. Select Conditions. These sections contain the variables defined for the selected query. The Sign, Option, Low, and High fields contain drop-down menus (where applicable) for defining the selected variable.

   Information noteWhen the query dimensions and measures selected do not have query variables, the Query variables panel does not appear.

   If the query contains a time dependent hierarchy with a date variable or a Key Date, those time variables will be listed in the variables section. If the query contains more than one variable that is used for defining time dependency, the variables will be linked to each other and set to the same date independent of which one is changed. The date that will be used as default, if Key Date is not actively changed, is today’s date. Transfer of explicit values for Key Date, that are set in the BEx/BW query, is not supported.

   Click the ![menu](../_images/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Resources/Images/Icons/ic_list.svg) to select values for the query variables.

   Values can be selected by scrolling through the list or by entering the value in Selected Values field. You can also use the filter field to find values. If the required value does not fall within the default value range (1 – 2000), the From and To values can be adjusted.

   Where a single value variable is to be defined, only one value can be selected in the dialog. If the variable allows multiple values then more than one value can be selected in the dialog. The values will be added to the variable and be visible in the final script.

   Where the variable requires an interval to be defined then the Option field must be changed to Between, otherwise the variable will be set to the Low value only, that is, no interval.
9. Select Preview. Based on your configuration under Conditions the connector will try to fetch a preview for the desired query. The preview will consist of 50 rows and will include the total number of rows.
10. Select Show descriptions. This shows object descriptions for InfoProviders and BEx/BW queries within the BW Objects list.
11. Select Script Preview. This shows the load script built from the selections made.
12. Select Insert Script to load the data.

### BEx/BW Query design considerations

The SAP BW Connector is able to extract existing BEx/BW queries. However, those queries are typically not designed for 3rd party extraction. Some layout functions might limit re-usability within a Qlik Sense application. For example:

- Conditional show/hide dimensions or key figures
- Dynamic display structures
- Hidden key figures
- Hidden variables

Here are some ways to optimize your query definitions when connecting to Qlik Sense:

#### Use free characteristics instead of predefined column structure

When calling a BEx/BW query, users can decide which dimensions and measures they want to retrieve. If there is a predefined layout configured and the requested structure looks different, the query will be executed twice: first for the query layout, second for the user layout. This slows down the extraction process.

#### Always configure characteristics to display key and text

In this case the characteristic will deliver two fields:

1. The key: For example, for Material this will be the Material number.
2. The text: For example, for Material this will be the Material text.

If you define the Key, Qlik Sense will only receive the Key value and the Text field will be empty. If you define the Text, you will receive the Text value within the Key Field and the Text field will be empty.

#### Expose as many variables as possible to the user

In some cases you can use variables to create a segmented extraction approach. For example, you can retrieve data on a Sales Organization level and Calender Year, which will result in much smaller and faster extraction jobs.

### Default values

Optional variables with default values will still be filtered on the default values, even if the variable has been removed from the script. The default values will be overridden if another value is entered for the variable. To completely remove the filtering from the default values, remove everything but the variable name from the script:

With default values:

[NAME=Z\_INT\_DEF\_OPT\_ZROWNBR, SIGN=I, OPTION=BT, LOW=0000000001, HIGH=0000000100]

Default values removed:

[NAME=Z\_INT\_DEF\_OPT\_ZROWNBR]

### Text Fields

Some dimensions have key and text fields, and some have only key fields (not known when the load script is generated). Inclusion or exclusion of compounded InfoObjects in the dimension selection will also affect the extracted texts.

Text fields are added automatically for all dimensions, whether there are texts or not in the BEx query. As a result, the load script will contain empty fields in the form <InfoObjectName>\_TEXT when a dimension does not have a text field.

![Example image of Display As setting set to Key and Text](../_images/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Resources/Images/ui_BEx-connect-query-value-display.png)

### Non Navigational Attributes

Non Navigational Attributes are not listed among the dimensions. These have to be added manually to the load script. In the load statement section of the script, add a line with the following syntax:

[InfoObjectName\_AttributeName],

For example, if the desired attribute is the 0MANUFACTOR of the info-object 0MATERIAL, the line in script would be:

[0MATERIAL\_0MANUFACTOR] as [Manufactor]

## Limitations and suggested workarounds

### Memory consumption

A common problem is that the SAP BW system runs out of memory when executing a load script that extracts a large amount of data. In general, SAP claims that BEx queries should not be used for mass data extraction. This is discussed in SAP Note 1968598.

How much data can be extracted at one time depends on the allocated memory on the app server where the SAP BW system is running. A common configuration is to have 2GB of memory available, which should allow an upper limit of approximately 500000 cells per extraction with the BEx Connector. There can, however, be other factors besides the amount of extracted data that affects the memory consumption during query execution. This is discussed in SAP Note 1879725.

If large amounts of data will be extracted from BEx queries, it is important to test the capacity of the SAP BW to make sure the extraction will not fail in production. It is possible to increase the query execution capacity in terms of data volumes by increasing the allocated memory in the SAP BW system. Make sure the BEx queries that will be used have variables that can be used to reduce the data volume, such as variables for time slicing (year, month, day).

### Hierarchies

The connector extracts the data in a flat structure. This means that hierarchical structures in the BEx query will not be represented hierarchically in Qlik. The nodes and leaves of a hierarchy will be extracted to the same field (dimension) in Qlik, and that is usually not usable in an analysis scenario. As a workaround to this limitation, hierarchies can be extracted using the Qlik SAP Extractor Connector and then joined with the BEx data in Qlik Sense.

### Collapsed key figure structures

The connector cannot access key figures or characteristics that are hidden in collapsed structures. As a workaround to this limitation, edit the BEx query in Query Designer and set all nodes to expanded.

### Customer exit variables

The behavior of customer exit variables in the connector is different from the behavior of customer exits in SAP reporting products. Some variables function as intended but some do not. The reason is that SAP and Qlik use different methods for extracting the query variables. If the customer exit variable is of type I\_STEP=1, the CMOD code is not executed before the variables are extracted to Qlik. As a result, the variable is not populated with a value before the variables are loaded in the selection dialog. The variable is, however, populated in the background once the query executes, unless it is overwritten with another value actively set in the selection dialog. If the customer exit variable is of type I\_STEP=2, the CMOD code executes after the query executes, but the functionality might differ from the behavior of the variable in SAP.

Because there are various ways of implementing CMOD variables, the general recommendation is to test the behavior for the specific variable. In case of difficulties, change th BEx query to extract the correct data to Qlik.

### Maximum number of dimensions

The maximum number of dimensions that can be extracted in a single load script is 49. To extract more than 49 dimensions from a BEx query, divide the extraction into several load scripts.

### Structures

If the BEx query contains a Structure, the Structure must be selected for extraction in the connector's selection dialog. If there is more than one Structure, only one of the Structures can be selected. If there are dimensions in addition to the Structure, at least one dimension must be selected. Otherwise the script execution will fail in SAP (with an ABAP runtime error).

### Hidden key figures

Hidden key figures are not accessible for extraction. Change the display setting for the key figure in Query Designer to access the key figure with the connector.

## Learn more

- [Qlik SAP Connector Enablement series](https://community.qlik.com/t5/Qlik-Connectors-Documents/Qlik-SAP-Connector-Enablement-Series/ta-p/1726063)
