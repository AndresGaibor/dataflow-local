---
title: "Reducing data"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Tutorials/reduce-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Tutorial - Scripting for beginners"]
---

# Reducing data

The application provides several different ways to reduce the amount of data that you load into your application. You can, for example, filter data from files or from data connectors.

You can also reduce data directly in the [load script](#glossary-1 "Glossary term").

Do the following:

1. Open the Data load editor in the Scripting Tutorial application.
2. Click Load data.

Based on the load script that you have written so far, the application loads 65,534 lines from the Sales.xlsx data file into Table1. Note that Sales data is the name of the tab that contains your table in the original Sales.xlsx file.

Data load progress window

![Data load progress window.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-load-progress-all.png "Click to view full size")3. In the data load editor, click the Sales tab.
4. Delete the semicolon at the end of this line:

(ooxml, embedded labels, table is [Sales data]);

5. Add the following line at the end of the load script:

```
Where Sales > 100.00 and Date("Invoice Date") >= '01/01/2026';
```

This tells the application to only load data where sales are greater than $100.00. It also uses the Date function to load data where the date is equal to or greater than January 1, 2026.

Your script should look like this:

Load script window with script to reduce amount of data loaded

![Load script window with script to reduce amount of data loaded.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-load_reduce_data-cloud-rev.png "Click to view full size")6. Click Load data.

Based on your updated load script, the application now loads fewer lines from the Sales.xlsx data file.

Data load progress window with reduced data load

![Data load progress window with reduced data load.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-load-progress-reduced.png "Click to view full size")7. If you then add the data to a straight table in your application, you can see that only the data that conforms to the conditions that you created was loaded.

Table containing Bill Date and Sales fields

![Table containing Bill Date and Sales fields.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-load-reduce-table.png "Click to view full size")

Note that we added the Sales [field](#glossary-2 "Glossary term") as a [dimension](#glossary-3 "Glossary term"). This is so that the Sales values are shown individually. If we had added Sales as a [measure](#glossary-4 "Glossary term") the values would have instead been aggregated per date.

Typically, you would add Sales as a measure. With measures you have the option to display values as currency amounts (for example, dollars) by applying number formatting to the column.

Number formatting applied to Sales measure

![Number formatting applied to Sales measure.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial_load-reduce-money.png "Click to view full size")

However, as we are using Sales as a dimension, we need a different approach. In this case, we will use a chart expression. Even though we are not discussing chart functions in detail in this tutorial, this is a good opportunity for a quick example.

When we use Sales as a dimension, the values are displayed as numeric, as shown in the table above.

To fix this, you can open the chart expression editor Sales field by clicking fx, and then using the Money function.

Opening the expression editor

![Opening the expression editor.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial_load-reduce-chart-expression.png "Click to view full size")

Enter the following in the expression editor.

```
=Money( Sales )
```

Expression editor

![Expression editor.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-load-reduce-chart-expression-edit.png "Click to view full size")

The values in the field will now display as monetary units. Those units (in this case, dollars) are specified in the Main section of the load script.

Table containing Bill Date and Sales fields. Sales now shown in dollars

![Table containing Bill Date and Sales fields. Sales now shown in dollars.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-load-reduce-table-money.png "Click to view full size")8. Now that we have completed this example, comment out the Where statement. Don't forget to add a semicolon to the end of your first LOAD statement.

Your script should look like this:

Load script window with Where statement commented out

![Load script window with Where statement commented out.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-where_comment-cloud-rev.png "Click to view full size")
