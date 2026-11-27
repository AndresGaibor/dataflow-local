---
title: "Creating an on-demand template application"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/creating-OnDemand-template-app.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Managing your data", "Managing big data with on-demand applications"]
---

# Creating an on-demand template application

An on-demand template application is a regular Qlik Sense application with one important difference: its [load script](#glossary-1 "Glossary term") contains data binding expressions used to formulate the queries made on the data sources. These data binding expressions are used at on-demand application generation time to read values from the selection state of the selection application and bind them to the template application script so that the generated application is loaded with a user-controlled subset of the data.

The template application typically connects to the same data source as the selection application. The load script of a selection application typically loads aggregated data to reduce data volumes while still offering interactive [visualizations](#glossary-2 "Glossary term") of important [dimensions](#glossary-3 "Glossary term") and [measures](#glossary-4 "Glossary term"). The load script of a template application uses queries that load a controlled subset of more granular data.

Template applications must have their sheets made public for other users to generate on-demand applications. For more information, see [*Granting access to sheets, sheet groups, bookmarks, and stories*](../Share/make-public-or-private.htm).

Information noteAn on-demand template application does not load data directly. The template application connection must be valid, but to test whether the connection works correctly, you must generate an on-demand application. When an on-demand application is generated, the load script is modified by the On-demand application service to load the selection state of the on-demand selection application. If the on-demand application generates without error, then you know the connection in template application work correctly.

Information noteConsider the size of your applications when developing on-demand template applications. Depending on your deployment, there may be storage limits, or using a large amount of storage may cause your cloud deployment to scale. Contact your system administrator for more information.

## Structure of a template application

A template application is linked to a selection application using an on-demand application navigation link. The application navigation link includes properties that control the number of records queried when the on-demand application is loaded with data. The load script of the template application contains data binding expressions that specify which [field](#glossary-6 "Glossary term") data from the selection application is used to formulate the queries issued when loading data into the on-demand application.

Information note

A new syntax for data binding expression was introduced in June 2020. The previous syntax and prefixes od\_, ods\_, odo\_, odso\_, and odb\_ behave as before including quantity constraints, \_n suffix, and format specifications. If your application should work on Qlik Sense versions prior to June 2020, use the old syntax. For the old syntax, see [Creating an on-demand template application (old version)](/en-US/sense/April2020/Subsystems/Hub/Content/Sense_Hub/LoadData/creating-OnDemand-template-app.htm).

The \_n suffix is not supported when using the new prefixes.

Basic data binding expressions have the form:

$(odag\_FIELDNAME)

The odag\_ prefix is used to bind the selection state of the selection application to the load script of the on-demand application, which is created by copying the template application. The part of the data binding expression that follows the odag prefix must be a name that matches a field in the selection application. When the on-demand application is generated, the current selection state of the selection application is used to obtain the desired values to bind for each field. Each occurrence of a $(odag\_FIELDNAME) expression in the load script of the newly created on-demand application is replaced with the list of values selected for the corresponding field in the selection state of the selection application.

Other prefixes for more specialized data binding are available. To learn more about tailoring for special cases and optimizing load statements, see [*Binding expressions in on-demand template applications*](bind-expressions-OnDemand-template-app.htm).

On-demand bindings can be inserted directly into SELECT and WHERE statements in your load script. When you add bindings directly into your WHERE statements, it is easy to combine them with other conditions in the statement.

You can add a placeholder variable $(odagActive) when making your load script. This enables you to load sample data into the template application so that master [charts](#glossary-7 "Glossary term") for [dynamic views](#glossary-8 "Glossary term") can be created without loading all data.

Information note

If you change the script of your template application and insert a new binding variable, new on-demand application navigation links must be created to replace any existing application navigation links. If you do not, the selection for the corresponding field will not be sent for existing on-demand applications using that template application.

The following examples illustrate a sample on-demand template load script.

Example: Adding some sample data

This example adds sample values so the application can be loaded even if the bindings are not complete.

```
IF '$(odagActive)'='' THEN
trace ODAG variables not inserted! Loading sample data.;
SET 'odag_Origin Code' = '''LAX''';
SET 'odag_Destination Code' = '''JFK''';
SET odagn_Year = 2015;
SET odag_Quarter = '''1''';
SET 'odag_Ticket Carrier Code' = '''CA''';
SET 'odag_Fare Class' = '''X''';
END IF;
```

Example: Loading data in the template application

The following is a sample load script for loading the sample data and filtering it with the generated odag\_FIELDNAME bindings. The odagn\_<Field Name> bindings pick the numbers in the duals and uses by default no quoting.

```
SQL SELECT *
FROM FlightDB.Flights
WHERE "Origin Code" IN ($(odag_Origin Code))
AND "Destination Code" IN ($(odag_Destination Code))
AND "Year" IN ($(odagn_Year))
AND "Quarter" IN ($(odag_Quarter))
AND "Ticket Carrier Code" IN ($(odag_Ticket Carrier Code))
AND "Fare Class" IN ($(odag_Fare Class));
```

## Single Sign-On (SSO)

On-demand applications can use single sign-on (SSO) with data sources that support SSO. The engine and the data source must be configured to allow SSO.

Once the engine and data source have been configured for SSO, the template application must enable SSO by adding the following syntax to the template application script:

///!ODAG\_SSO

The On-Demand App Service parses the script when an on-demand application is generated and each time it is reloaded.

When an on-demand application is loaded with SSO, the identity of the end user is sent to the data source. The end user must have access to the sources used in the template application's [data connections](#glossary-9 "Glossary term"). Only data that user has access to in those sources is loaded, even if a larger set of data is selected.
