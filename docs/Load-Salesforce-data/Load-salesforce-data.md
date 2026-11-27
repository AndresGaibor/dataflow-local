---
title: "Select and load Salesforce data"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Salesforce_Connector_help/Content/Connectors_Salesforce/Load-Salesforce-data/Load-salesforce-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "Salesforce"]
---

# Select and load Salesforce data

Once a connection to Salesforce has been established, you can select data and load it into an application. You select data by selecting Salesforce objects/tables and fields in the Create Select Statement dialog or in the Select data to load step.

Data properties that can be configured

| Properties | Description |
| --- | --- |
| Tables | Shows the tables that are available for this Salesforce account.  Selecting a table will cause the table fields to be displayed in the Data preview tab. |
| Fields | Shows the fields that are associated to the selected table.  Field names can be changed by clicking on the existing name. An edit box opens around the name allowing you to change the name. The new name is then used as an alias for the original name the field has in the database. Fields with unsupported data types are not shown. |
| Data preview | Shows a preview of the fields and data of the selected table.  You can select which data columns to include by checking the box beside the field name. You can also change the field name by clicking on the existing field name. The new name is then used as an alias for the name the field has in the database. |
| Metadata | Shows a table of the fields and whether they are primary keys. Primary-key fields are also labeled with a key icon Primary key beside the field name. |
| Include LOAD statement | Adds a LOAD statement before the SELECT statement.  [*Add a LOAD statement*](#Select2) |
| Add data | Opens the Associations view of the Data manager.  Allows you add more data sources, fix any errors in your data, and create table associations. This option is available only when you use Add data.  [Managing data associations](/en-US/sense/November2026/Subsystems/Hub/Content/Sense_Hub/LoadData/associating-data.htm) |
| Insert script | Inserts the script displayed in the Data preview panel into the script editor. This option is available only when you use the Data load editor. |

## Add a LOAD statement

You can add a LOAD statement to your script when you are loading Salesforce data using the Bulk API.

The LOAD statement before the SELECT statement allows the LOAD statement to use the SELECT statements as input. Basically, it is a LOAD statement that loads from the LOAD or SELECT statement below, without specifying a source qualifier, such as From or Resident, as you would normally. You can stack any number of LOAD statements this way. The statement at the bottom will be evaluated first, then the statement above, and so on until the top statement has been evaluated. Another advantage of the LOAD preceding SELECT is that you can keep a calculation in one place and reuse it in LOAD statements placed above. For example, when you load data from a database using a SELECT statement, you cannot use Qlik functions to interpret data in the SELECT statement. The solution is to add a LOAD statement and perform data transformations above the SELECT statement. In this example, string data is interpreted with the Qlik Date# interpretation function in a LOAD statement, using the previous SELECT statement as source:

LOAD Date#(orderDate, 'YYYYMMDD') as OrderDate;

SELECT OrderDate FROM \_;

The LOAD statement created in the script panel is a simple load.

![Simple load script example with LOAD Id, SELECT Id, and FROM statement](../_images/en-US/cloud-services/Subsystems/Salesforce_Connector_help/Content/Resources/Images/ui_gen_Include_LOAD2.png)

To add the Date# function to the LOAD statement as in the example above, you would edit the script in the script panel.

## Change the data selection manually

While the SELECT and LOAD statements are built automatically when you select tables and fields, you can make certain changes to those statements manually. You can make changes to SELECT and LOAD statements in the Qlik Sense Data load editor.

In Qlik Sense, field names can be changed in the Fields panel by clicking on the existing name. The changed name is then used as an alias for the original name when the field is loaded.

Information noteWhen a field name is changed while in Bulk mode, Include load statement is used automatically because the LOAD statement is where AS is used to create an alias.

Information noteField names cannot be changed in SOAP mode because preceding LOAD statements are not used in SOAP mode. Aliases are defined in LOAD statements.

When SELECT statements are generated, they do not include a WHERE clause, but one can be added in the script panel. The statement for the Salesforce Connector supports the addition of WHERE clauses.

Information note

Changes entered manually in the script panel will be lost if new table or field selections are made. Changes are also lost when you select Preceding load or Include LOAD statement. Select all tables and fields, as well as Preceding load or Include LOAD statement before editing the script manually.

Information noteThe keywords WITH, GROUP, ORDER, LIMIT, OFFSET, and FOR are not allowed when using the PK Chunking mode.

When a WHERE clause is used and the selected field uses a date or date-time data type, the date-time format YYYY-MM-DD hh:mm:ss is automatically converted to the SOQL date-time (YYYY-MM-DDThh:mm:ssZ) if ConvertSQLdates is selected in the Salesforce connection dialog. SOQL uses "Z" on the time to indicate that the time is to be read as absolute, with no time zone offset. In SOQL, “Z” can be substituted with an offset value. For example, the date “2009-02-24 23:01:01” in Eastern US time zone would be “2009-02-24T23:01:01-05:00” in SOQL. Because the YYYY-MM-DD hh:mm:ss format has no offset value, the date-time is converted to Coordinated Universal Time (UTC).

Information noteThe Convert UTC to local time setting does not affect the time zone in date-time values sent to Salesforce.com in WHERE clauses. The Convert UTC to local time setting handles the display of date-time values returned from Salesforce.com, not the values sent to Salesforce.com.

The SELECT statement for the Salesforce Connector also supports:

- SELECT \* statement: The Salesforce Connector allows you to use the SELECT \* statement to select all fields in the table. You add the SELECT \* statement manually in the script panel.

  The SOQL query language does not support the SELECT \* statement, but the Salesforce Connector has been enhanced to recognize that syntax. Only asterisks (\*) and simple field names can be used in the SELECT \* statement.

  The SELECT \* statement can only be used when Bulk API is selected in the Salesforce connection dialog.

- String escape characters: The Salesforce Connector uses the single quotation mark character as an escape character instead of the back slash (\) used by SOQL. To include a single quotation mark in a query string, it must be prefaced by another single quotation mark. The Salesforce Connector uses the single quotation mark character as an escape character instead of the back slash (\) used by SOQL. To include a single quotation mark in a query string, it must be prefaced by another single quotation mark. For example, the following string encloses Captain Awesome in single quotation marks:

  Devon ''Captain Awesome'' Woodcomb

The SELECT statement for the Salesforce Connector does not support:

- Qualified field names: Field names cannot be prefixed by object names. For example, “Contact.FirstName” is not permitted.
- Salesforce prefix: It is not permissible to prefix the table name with the string “Salesforce.” For example, “Salesforce.Contact” is not allowed.
- Bracketed names: table and field names cannot be put in brackets. For example, the following SELECT statement is not valid:

  SELECT [FirstName] FROM [Contact]
- SOQL aliases: The syntax for creating aliases in SOQL cannot be used. For example, the following SOQL syntax is not valid for the Salesforce Connector:

  SELECT Id BusinessID FROM Contact

## Load Salesforce objects with relationship queries

SELECT statements can be written to load Salesforce objects with relationship queries. To create a relationship query, you must add it manually, which requires that you use the Edit Script dialog or the Data load editor. Relationship query statements must be entered directly in the script panel. They cannot be created simply by selecting multiple tables and fields from the Objects/Tables and Fields lists.

Information note

SOAP API is required for relationship queries.

In the following example, the SELECT statement includes fields from multiple tables.

SELECT Name,

(SELECT Name FROM Contacts), (SELECT Subject, CaseNumber FROM Cases)

FROM Account;

Information noteWhen loading multiple objects in a relationship query, you must use a relationship name instead of a table name. For standard tables, the relationship name is the plural of the table name. In the example above, that requirement for the table/object name is indicated in red.

From this SELECT statement, the connector creates separate load statements for each of the related tables/objects.

//The LOAD Statements below will only work with SOAP (non-Bulk mode) of the Salesforce connection.
SalesforceConnectorMaster:
SELECT Name,
(SELECT Name FROM Contacts), (SELECT Subject, CaseNumber FROM Cases)
FROM Account;
Account.Contacts:
LOAD Account.Contacts.Name,
PK\_Account.Contacts AS Account.ContactsKey ,
FK\_AccountContacts AS AccountKey
RESIDENT SalesforceConnectorMaster WHERE NOT IsNull([FK\_AccountContacts]);
Account.Cases:
LOAD Account.Cases.Subject,
Account.Cases.CaseNumber,
PK\_Account.Cases AS Account.CasesKey ,
FK\_AccountCases AS AccountKey
RESIDENT SalesforceConnectorMaster WHERE NOT IsNull([FK\_AccountCases]);
Account:
LOAD Account.Name,
PK\_Account AS AccountKey
RESIDENT SalesforceConnectorMaster WHERE NOT IsNull([PK\_Account]);
DROP Table SalesforceConnectorMaster;

The resulting load produces three related tables.

![Example of three related tables: Account, Account.Contacts and Account.Cases](../_images/en-US/cloud-services/Subsystems/Salesforce_Connector_help/Content/Resources/Images/ui_Multi-load-data-model.png)
