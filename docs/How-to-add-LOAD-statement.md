---
title: "Add a LOAD statement to an ODBC connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/How-to-add-LOAD-statement.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Data sources in Qlik Cloud Analytics", "ODBC databases"]
---

# Add a LOAD statement to an ODBC connection

You can add a LOAD statement to your ODBC connection when you are using the Data load editor. Select Include LOAD statement to create a LOAD statement before the SELECT statement.

The LOAD statement before the SELECT statement allows the LOAD statement to use the SELECT statements as input. Basically, it is a LOAD statement that loads from the LOAD or SELECT statement below, without specifying a source qualifier, such as From or Resident, as you would normally. You can stack any number of LOAD statements this way. The statement at the bottom will be evaluated first, then the statement above, and so on until the top statement has been evaluated.

Another advantage of the LOAD preceding SELECT is that you can keep a calculation in one place and reuse it in LOAD statements placed above. For example, when you load data from a database using a SELECT statement, you cannot use Qlik functions to interpret data in the SELECT statement. The solution is to add a LOAD statement and perform data transformations above the SELECT statement.

In this example, string data is interpreted with the Qlik Sense Date# interpretation function in a LOAD statement, using the previous SELECT statement as source:

```
LOAD Date#(orderDate, 'YYYYMMDD') as OrderDate;
SELECT OrderDate FROM _;
```

The LOAD statement created in the script panel is a simple load.

![Simple load script example image](_images/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Resources/Images/ui_Preceding_Load.png)

To add the Date# function to the LOAD statement as in the example above, you would edit the script in the Data load editor or the Edit script dialog after the script built automatically in the script panel is inserted there.

[Loading data with the data load script](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/introduction-data-modeling.htm)
