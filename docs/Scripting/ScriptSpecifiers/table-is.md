---
title: "Table is"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/ScriptSpecifiers/table-is.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script statements and keywords", "Script regular statements", "Load"]
---
# Table is

For Excel, XML, Parquet, or JSON files, you can specify the table you are loading data from in the table format specifier.

Syntax:

Table is table name

Arguments:

Arguments

| Argument | Description |
| --- | --- |
| table name | Specifies the name of the table. The value depends on the table format:   - Excel: The sheet name. - XML: The path that specifies the part of the XML to be loaded. - Parquet: The path that specifies the table, with the format <node>.<node>.<node>.  Use Table   is when specifying a table within a nested structure.  For example, you have Parquet data in the following schema:  Schema:   Field(name: "Name", datatype: String),   Field(name: "Age", datatype: Float),   Field(name: "Phone", datatype: List(   Field(name: "Item", datatype: Struct[   Field(name: "Number", datatype: String)  You could load Phone and its nested fields as a table with the argument `Table is [Schema:Phone.Item]`. This will generate the key field %Key\_Phone with the table. - JSON: In JSON files with arrays, the path to the iterator for the subtable.  You can make a load of all tables by specifying **all tables** instead of **Table is**. For example:  LOAD \* FROM [lib://DataFiles/Sales.json] (json, all tables);  If your data contains multiple arrays with identical content, use the keyword **DISTINCT** in the subtable load statements. For example:  LOAD DISTINCT \* FROM [lib://DataFiles/Sales.json] (json, all tables); |

Example:  Excel

LOAD
"Item Number",
"Product Group",
"Product Line",
"Product Sub Group",
"Product Type"
FROM [lib://DataFiles/Item master.xlsx]
(ooxml, embedded labels, table is [Item master]);

Example: XML

LOAD
city%Table,
%Key\_row\_7FAC1F878EC01ECB
FROM [lib://DataFiles/cities.xml]
(XmlSimple, table is [root/row/country/city]);

Example: Parquet

The file company.parquet contains the following schema:

company (String)
contact (String)
company:salesrep (List)
salesrep (Group)
salesrep (String)
company:headquarter (List)
headquarter (Group)
country (String)
city (String)
city:region (List)
region (Group)
region (String)

The following would load the contents from the file into tables. The first load statement loads the root group. The second load statement loads the contents of the salesrep group as a table. The third loads the headquarter group as a table. The fourth loads the region group in as a table.

LOAD \* FROM […] (parquet);
LOAD \* FROM […] (parquet, table is [company:salesrep.salesrep]);
LOAD \* FROM […] (parquet, table is [company:headquarter.headquarter]
LOAD \* FROM […] (parquet, table is [company:headquarter.headquarter.city:region.region]

Example: JSON

LOAD
customers.customerid,
customers.companyname,
customers.contactname,
customers.contacttitle,
customers.address,
customers.city,
customers.postalcode,
customers.country,
customers.phone,
customers.fax,
%Key\_customers,
customers.region
FROM [lib://DataFiles/example.json]
(json, table is [/\*/customers]);

Limitations:

The Table
is specifier is only relevant for Excel, XML, Parquet, JSON
files.
