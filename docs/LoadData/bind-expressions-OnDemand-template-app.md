---
title: "Binding expressions in on-demand template applications"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/bind-expressions-OnDemand-template-app.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Managing your data", "Managing big data with on-demand applications", "Creating an on-demand template application"]
---

# Binding expressions in on-demand template applications

Data bindings in a template application specify which data from a corresponding selection application is used to formulate the queries issued when loading data into an on-demand application.

The basic form of binding expressions--$(odag\_FIELDNAME)--is not the only method available to bind expressions. Other prefixes can be used to refine [selections](#glossary-2 "Glossary term") and to ensure that the template application loads data correctly.

## Available binding prefixes

The general prefix form is odag[s|o][n][cnt] where:

- s - include only selected values
- o - include only optional values
- n - pick the numeric version, by default unquoted
- cnt - insert the number of values instead of actual values

The following table provides a list of all versions of the binding prefixes available. The examples assume a [field](#glossary-3 "Glossary term") named MyField with 1,2,3 as the selected values (green values) and 4 as an optional selected value (white value).

Binding prefixes

| Prefix | Description | Example | Replaced with |
| --- | --- | --- | --- |
| odag\_ | Replaced by the selected (green) and optional (white) values. Picks the text version of the values. This is the standard prefix for string values. | $(odag\_MyField) | '1','2','3','4' |
| odagcnt\_ | Replaced by the number of values in the corresponding odag\_ binding. This prefix is used for optimization of queries. | $(odagcnt\_MyField) | 4 |
| odagn\_ | Replaced by the selected (green) and optional (white) values. Picks the numeric version of the values. This is the standard prefix for numeric values.  Information note If the data model is such that there can be no selected or optional values of the field, a noValue must be specified in the expression. For example, $(odagn\_MyField){"noValue":"-99999"}.  For more information, see [*Changing the value quotation and delimiter characters*](#Changing). | $(odagn\_MyField) | 1,2,3,4 |
| odagncnt\_ | Replaced by the number of values in the corresponding odagn\_ binding. This is for optimization of queries. | $(odagncnt\_MyField) | 4 |
| odago\_ | Replaced by the optional (white) values. Picks the text version of the values. This is for optimization of queries.  [*Optimizing for large database*](#Optimizi). | $(odago\_MyField) | '4' |
| odagocnt\_ | Replaced by the number of values in the corresponding odago\_ binding. This is for optimization of queries. | $(odagocnt\_MyField) | 1 |
| odagon\_ | Replaced by the optional (white) values. Picks the numeric version of the values. This is for optimization of queries.  [*Optimizing for large database*](#Optimizi). | $(odagon\_MyField) | 4 |
| odagoncnt\_ | Replaced by the number of values in the corresponding odagon\_ binding. This is for optimization of queries. | $(odagoncnt\_MyField) | 1 |
| odags\_ | Replaced by the selected (green) values. Picks the text version of the values. This is for optimization of queries.  [*Optimizing for large database*](#Optimizi). | $(odags\_MyField) | '1','2','3' |
| odagscnt\_ | Replaced by the number of values in the corresponding odags\_ binding. This is for optimization of queries. | $(odagscnt\_MyField) | 3 |
| odagsn\_ | Replaced by the selected (green) values. Picks the numeric version of the values. This is for optimization of queries.  [*Optimizing for large database*](#Optimizi). | $(odagsn\_MyField) | 1,2,3 |
| odagsncnt\_ | Replaced by the number of values in the corresponding odagsn\_ binding. This is for optimization of queries. | $(odagsncnt\_MyField) | 3 |

Information note

Empty values are filtered away in the text versions. Non numeric and NaN values are filtered away in the numeric versions.

## Optimizing for large database

The odags\_ and odagsn\_ prefixes are intended for optimization of queries. When there are no selections in the bound fields, odag\_ includes all the values while odags\_ includes no values. In some cases, it is more efficient to use the odags\_ and odagscnt\_ prefixes. This enables you to test if the set of values are empty. For example, the following is more efficient when no selections are made in MyField than testing for all values in odag\_MyField:

WHERE ($(odagscnt\_MyField)=0 OR MyColumn IN ($(odags\_MyField)))

odags\_ cannot be used when there is an alternate field to select from in the selection application that is not an on-demand field. For example, if the user makes selections in CountryName, but the binding expression is on the associated field CountryCode, odags\_ could not be used. In these cases, odago\_ can be used instead. If there are no values in a odago\_ binding, it could either mean that either all values should be included or that no values should be included.

## Binding numeric values

When the data to be bound to the on-demand application consists of numbers instead of strings, it is useful to disable the quote wrapping behavior on the numeric fields. For example, if the sales records include a numeric DAY\_OF\_WEEK column and you want the user of the selection application to choose arbitrary combinations of DAY\_OF\_WEEK, you would augment the aggregation query used for loading the selection application to include DAY\_OF\_WEEK in both the SELECT list as well as the GROUP BY list. If quotation marks are wrapped around DAY\_OF\_WEEK values when they are selected, a runtime query error could result if the database does not support automatic type conversion from string to numeric.

To handle this situation, you can use a numeric version of the binding expression suffix. This forces the field binding to use the numeric values from the selection application rather than string values. The following numeric version are available:

- odagn\_
- odagon\_
- odagsn\_

By using numeric versions, the values are picked up from the numeric part in the duals that store selected values and the values are unquoted by default.

## Requiring a certain number of selections

In some situations, it may be necessary to require that the on-demand application query contain a specific number or range of values for a specific field. For example, if the on-demand application's query contains a BETWEEN clause to obtain all sales between a start and end date, the bind expression for the YEARQUARTER field can have a suffix syntax of [2] that will require exactly two values be selected for YEARQUARTER, as in:

$(odag\_YEARQUARTER)[2]

The on-demand application navigation point on the selection application will remain disabled as long as there are not exactly two values of YEARQUARTER selected. A message will display to indicate that exactly two values of YEARQUARTER must be selected.

Selection quantity constraints create a prerequisite linkage between the selection application and the on-demand application. This is different from bind expressions that do not use quantity constraints. For example, when the template application's script contains a bind expression without a quantity constraint, as in:

$(odag\_MYFIELD)

there is no requirement that the selection application contain a field named MYFIELD nor for there to be any selected values of that field if it does exist. If the selection application does not contain a field named MYFIELD or if the user simply neglects to make any selections from it, the on-demand application navigation point can still become enabled when other selections are made to fulfill the record-limit value condition.

If on the other hand, the bind expression is:

$(odag\_MYFIELD)[1+]

there are now two requirements placed on the selection application:

- The selection application must contain a field named MYFIELD.
- The user must select at least one value for MYFIELD.

This type of bind expression must be used carefully because it limits which selection applications can be used with the template application. You should not use this quantity constraint on bindings of a template application unless you are certain you want to impose that selection quantity requirement on all selection applications that link to that template application.

To perform the data binding process, the On-demand application service uses a string substitution approach that is insensitive to comments in the script. This means you should not use bind expressions in comments unless you want those comments to contain the list of bound values following application generation. Any bindings in comments will also show up in the field list of the On-demand application generation link, which may be undesirable.

Other quantity constraints are possible. The following table summarizes the different combinations of selection quantity constraints.

Different combinations of selection quantity constraints

| Constraint pattern | Selection requirement |
| --- | --- |
| $(odag\_YEARQUARTER)[2] | Exactly 2 values of YEARQUARTER must be selected. |
| $(odag\_YEARQUARTER)[2-4] | Between 2 and 4 values of YEARQUARTER must be selected. |
| $(odag\_YEARQUARTER)[2+] | At least 2 values of YEARQUARTER must be selected. |
| $(odag\_YEARQUARTER)[2-] | At most 2 values of YEARQUARTER can be selected. |

Information noteThe check to determine if all the quantity constraints in the template application have been met is performed during the application generation process. If a quantity constraint is violated, the request to generate the application will be rejected and an error message will be displayed.

## Changing the value quotation and delimiter characters

When a list of values from a field selected in a selection application is inserted into the script of a template application, the values are surrounded by single quotation marks and separated by commas. These are the default characters for quotations and delimiters. These values can be changed in syntax appended to binding statement for each field. For example:

$(odag\_ORIGIN){"quote": "|", "delimiter": ";"}

These new values are then used when formulating the list of binding values taken from the selection application. For example, if the selected values are the first three months of the year, the list would be constructed as:

|January|;|February|;|March|

The default values for the quotation and delimiter characters work for most standard SQL databases. But they might not work for some SQL databases and do not work for many dynamic data sources such as NoSQL and REST. For those sources, you need append this binding expression to change the quotation and delimiter characters.

The following table outlines format parameters for changing quotation and delimiter characters.

Format parameters

| Parameter | Default value | Definition |
| --- | --- | --- |
| quote | ' (single quote) for text prefixes  empty for numeric prefixes | Will be added before and after each value |
| delimiter | , (comma) | Will be added between all values |
| quoteReplace | '' (double single quotes) | When the value is not empty and the quotation is not empty, then all occurrences of the of the quote inside the values will be replaced by the specified string.  Information notequoteReplace is not supported as a parameter for numeric prefixes such as odagn\_. quoteReplace is ignored by numeric prefixes. |
| noValue | (empty) | When there are no values selected for a field, this value will be used instead. This parameter is useful when there can be no values of a particular field in the selection.  The value should be set to a value that does not exist in the source data. For numeric values, for example, use a negative value if all values in the database are positive.  Information note For unquoted values, noValue must be specified if selected values of the field can be an empty set. |

The following tables outline the format specification and generated values for odag\_ and odagn\_. The generated inserted values are based on the default data values of VAL1, VAL2.

odag\_ example format specifications and generated values

| Format specification | Description | Generated inserted values |
| --- | --- | --- |
| not specified | Comma separated list of values, quoted with ' . | 'VAL1','VAL2' |
| {"quote": "", "delimiter": ""} | Concatenated values | VAL1VAL2 |
| {"quote": "X", "delimiter": "Y"} | Values quoted by X and delimited by Y. | XVAL1XYXVAL2X |
| {"quote": "XX", "delimiter": "YY"} | Values quoted by XX and delimited by YY. | XXVAL1XXYYXXVAL2XX |
| {"quote": "X"} | Values quoted by X and delimited by , (default). | XVAL1X,XVAL2X |
| {"delimiter": "YY"} | Values quoted by ' (default) and delimited by YY | 'VAL1'YY'VAL2' |
| {"quote": ""} | Unquoted values delimited by ,. | VAL1,VAL2 |
| {"quote": "A", "quoteReplace": "\\A"} | Values quoted by A and delimited by comma (default). A values inside the field will be replaced by \A.  Information note In this example, there needs to be double \ since \ is the escape character in json format. | AV\AL1A,AV\AL2A |

odagn\_ example format specifications and generated values

| Format specification | Description | Generated inserted values |
| --- | --- | --- |
| not specified | Comma separated list of unquoted values. Note that the numeric values will be used. | VAL1,VAL2 |
| {"delimiter": "YY"} | Unquoted values delimited by YY | VAL1YYVAL2 |
| {"quote": "A", "quoteReplace": "\\A"} | Compared to the odag\_ prefix the quoteReplace parameter will be ignored. | AVAL1A,AVAL2A |

## Processing individual values

When individual processing of field values is required, you can use an inline method to generate values in the variable Values and perform arbitrary processing with Replace or another function. In the example below, Replace is used with placeholder values.

MyTempBindingData:
LOAD \* INLINE [VAL
$(odag\_MyField){"quote": "", "delimiter": "\n"}
];
\_TempTable:
LOAD Concat(chr(39) & Replace(text, from\_str, to\_str) & chr(39), ',') as CombinedData Resident MyTempBindingData;
LET Values = Peek('CombinedData',0,'\_TempTable');
drop table \_TempTable;
drop table MyTempBindingData;
