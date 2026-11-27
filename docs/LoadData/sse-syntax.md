---
title: "Server side extensions syntax"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/sse-syntax.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics"]
---

# Server side extensions syntax

This help topic outlines the Qlik server side extensions syntax.

## Script functions

There are eight script function variations. In the [load script](#glossary-0 "Glossary term"), they all should behave the same, but it is typical to use ScriptEval in this scenario.

The load script usage LOAD \* EXTENSION operates on a table in table out approach and infers the correct data types from the internal table definitions and metadata.

When using these functions as chart expressions, the function used is important and will have a significant difference in the results and performance of the request.

## ScriptEval vs ScriptAggr

There are two sets of script functions, ScriptEval and ScriptAggr:

ScriptEval: after the hypercube has been aggregated, all rows in the specified columns are sent to the SSE connector. The response expected is a single column. If multiple columns are returned, the first column that has the same number of rows as the input will be picked. The rows in the returned column must be in the same order as the input.

ScriptAggr: before the hypercube is aggregated, all rows for a single [dimension](#glossary-1 "Glossary term") group in the hypercube are sent and the SSE is expected to return a single 1 column, 1 row response. There will be one request sent to the SSE for each dimension value. While there are use cases for this, it is rare for this method to be used, as it can create performance issues if ScriptAggr is called with a large number of dimension values.

## Data types

There are four variations of the requests, which specify the input and output data type combinations:

- ScriptEval(Script, Field1, [Field n]): In this example, the input fields must all be numeric and the response must be numeric.
- ScriptEvalStr(Script, Field 1, [Field n]): In this example, the input fields must all be string and the response must be string.
- ScriptEvalEx(DataTypes, Script, Field 1, [Field n]): In this example, the input fields can be either string or numeric, however the first parameter is a string of the datatypes and the response must be numeric.
- ScriptEvalExStr(DataTypes, Script, Field 1, [Field n]): In this example, the input fields can be either string or numeric, however the first parameter is a string of the datatypes and the response must be string.

The DataTypes parameter is a string on S and N characters in the order of the fields.

## Examples

Example:

A script that adds 2 numeric fields:

ScriptEval('Script',num1,num2)

Example:

A script that concatenates 2 strings:

ScriptEvalStr('Script',str1,str2)

Example:

A script that predicts a probability (number) with a mixture of string and numeric inputs:

ScriptEvalEx('SSNN','Script',str1, str2, num1, num2)

Example:

A script that predicts a classification (string) with a mixture of string and numeric inputs:

ScriptEvalExStr('SSNN','Script',str1, str2, num1, num2)
