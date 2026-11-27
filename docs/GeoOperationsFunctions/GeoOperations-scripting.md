---
title: "Scripting with Qlik GeoOperations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Global_Common/GeoOperationsFunctions/GeoOperations-scripting.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Qlik GeoOperations analytics sources"]
---

# Scripting with Qlik GeoOperations

Qlik GeoOperations connectors create and format GeoOperations scripts for you. You can modify these scripts in Data load editor. You can also manually script with GeoOperations functions instead of using Qlik GeoOperations connectors.

## How Qlik GeoOperations works

First, you add a Qlik GeoOperations connector as a data source. In Data load editor in your application, when you select data to load from the connector, you can select operations to perform and the parameters to apply. The Qlik GeoOperations connector then adds the corresponding GeoOperations script to your load script. You can also add this script manually.

Each operations script consists of a load statement, which selects the data use, and the operation. These are sent to the GeoOperations extension in the load script. The server-side extension then returns the data. Qlik GeoOperations makes an Advanced Analytics Integration object called GeoOperations available in the script language. This provides the function ScriptEval for sending the script and the table to the extension.

For example, the following is the load script for applying the Travel areas operation to the previously loaded table MyPoints and specify parameters for the size/cost of the travel area:

Load \* Extension GeoOperations.ScriptEval('TravelAreas(costValue="10", costUnit="Minutes")', MyPoints);

The script is sent as the first parameter to ScriptEval and the table as the second.

The GeoOperations are functions that operate on datasets. The datasets either come from data loaded in Qlik Sense or from external sources such as geographic files or the location service. The data sent out from the script is available as a dataset named INTABLE. If you want to specify additional parameters on that data, you need to declare it after the function call as a DATASOURCE. For example:

Load \* Extension GeoOperations.ScriptEval('TravelAreas(costValue="10", costUnit="Minutes")
DATASOURCE myPoints INTABLE pointField="Point"', MyPoints);

Other data sources always need to be declared and parameters such as URLs need to be specified. In each operation you can specify the data sources to use. By default, operations pick up the available datasets as described for each operation in [Operation](/en-US/geoanalytics/Content/Ref-GeoOperationsService/connector-geoanalytics_reference-Operation.htm).

## Selecting and renaming GeoOperations fields

GeoOperations functions return fields. By default, all fields are returned and included. You can precede GeoOperations functions with a SELECT statement to select and optionally rename specific fields in which you are interested. For example, this script uses SELECT to load only two of the postal code fields from the location service:

Load \* Extension GeoOperations.ScriptEval('

SELECT Name as PostalCode, LocationArea FROM

Load() DATASOURCE PostalCodes LOCATIONSERVICE type="PostalCode", country="se"');

Using a SELECT statement in the GeoOperations script can be more efficient than specifying fields in Qlik LOAD statement as the data is not loaded into Qlik Sense if it is not selected in the GeoOperations script.

SELECT can be used to avoid calculating some fields by choosing not to return them in the results. For example, the relative overlap fields returned by Intersects can be excluded.

Information note

If you are using the same operation multiple times in your load script, use a SELECT statement to rename the fields.

## Script syntax

The script that sent to GeoOperations has the following syntax:

### 1. Operation

The simplest form of the script performs an operation.

Syntax:

Operation(paramName="paramValue", ...)

Example:

Cluster(distance="100000")

For more information, see the list of Operations and their parameters.

### 2. Dataset

The second step is to load a dataset for your chosen operation(s) to be applied to.

Syntax:

Operation(paramName="paramValue", ...)

DATASOURCE name TYPE paramName="paramvalue", ...

Example:

Within()

DATASOURCE states LOCATIONSERVICE type="STATE", country="US"

For more information, see the list of Datasets and their parameters.

### 3. Putting it together

This is how the completed script would look in the Data load editor:

[MyPointsInStates]:

Load \* Extension GeoOperations.ScriptEval(’

Within()

DATASOURCE states LOCATIONSERVICE type=”STATE”, country=”US”

’, MyTable);

In this example, MyTable can be any other loaded table containing points, lines, named areas, or other geographic data.

### 4. Filter fields

The following additions allow the results of the operation to be further filtered.

[MyPointsInStates]:

Load \* Extension GeoOperations.ScriptEval(’

SELECT Name, states.Name as State FROM

Within()

DATASOURCE states LOCATIONSERVICE type=”STATE”, country=”US”

’, MyTable{Name, Point});

Parameter names and field names are case sensitive but operations, parameter options (like meters, minutes, car, and so on) or keywords such as SELECT and FROM are not.

## Troubleshooting AddressPointLookup and PointToAddressLookup scripting
