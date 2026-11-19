---
title: "Using the Crosstable prefix"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/use-crosstable-prefix.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Tutorial - Next steps in scripting", "Transforming data"]
---
# Using the Crosstable prefix

Cross tables are a common type of table featuring a matrix of values between two orthogonal lists of header data. Whenever you have a cross table of data, you can use the Crosstable prefix to transform the data and create the desired [fields](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/use-crosstable-prefix.htm#glossary-0 "Glossary term").

## Crosstable prefix

In the following Product table you have one column per month and one row per product.

Product table

| Product | Jan 2014 | Feb 2014 | Mar 2014 | Apr 2014 | May 2014 | Jun 2014 |
| --- | --- | --- | --- | --- | --- | --- |
| A | 100 | 98 | 100 | 83 | 103 | 82 |
| B | 284 | 279 | 297 | 305 | 294 | 292 |
| C | 50 | 53 | 50 | 54 | 49 | 51 |

When you load the table, the output is a table with one field for Product and one field for each of the months.

Product table with Product field, and one field each for the months

![Product table with Product field, and one field each for the months.](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-crosstable-data-model-before.png)

If you want to analyze this data, it is much easier to have all numbers in one field and all months in another. In this case, that is a three-column table with one column for each category (Product, Month, Sales).

Product table with Product, Month, and Sales fields

![Product table with Product, Month, and Sales fields.](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-crosstable-data-model-after.png)

The Crosstable prefix converts the data to a table with one column for Month and another for Sales. Another way to express it is to say that it takes field names and converts these to field values.

Do the following:

1. Create a new application and call it Advanced Scripting Tutorial.
2. Add a new script section in the **Data load editor**.
3. Name the section Product.
4. Under **DataFiles** in the right menu, click **Select data**.
5. Upload and then select Product.xlsx.
6. Select the Product table in the **Select data from** window.
> **Tip:** Under **Field names**, make sure that **Embedded field names** is selected to include the names of the table fields when you load the data.

7. Click **Add**.

Your script should look like this:

LOAD
Product,
"Jan 2014",
"Feb 2014",
"Mar 2014",
"Apr 2014",
"May 2014",
"Jun 2014"
FROM [lib://DataFiles/Product.xlsx]
(ooxml, embedded labels, table is Product);

8. Click **Load data**.
9. Open the **Data model viewer**. The data model looks like this:

Product table with Product field, and one field each for the months

![Product table with Product field, and one field each for the months.](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-crosstable-data-model-before.png)10. Click the Product tab in the **Data load editor**.
11. Enter the following above the LOAD statement:

```
CrossTable(Month, Sales)
```

12. Click **Load data**.
13. Open the **Data model viewer**. The data model looks like this:

Product table with Product, Month, and Sales fields

![Product table with Product, Month, and Sales fields.](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-crosstable-data-model-after.png)

Note that the input data typically has only one column as a qualifier field; as an internal key (Product in the above example). But you can have several. If so, all qualifying fields must be listed before the attribute fields in the LOAD statement, and the third parameter to the Crosstable prefix must be used to define the number of qualifying fields. You cannot have a preceding LOAD or a prefix in front of the Crosstable keyword. However, you can use auto-concatenate.

In a table in Qlik Sense, your data looks like this:

Table showing data loaded using Crosstable prefix

![Table showing data loaded using Crosstable prefix.](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-crosstable-sense-table.png)

You can now, for example, create a bar chart using the data:

Bar chart showing data loaded using Crosstable prefix

![Bar chart showing data loaded using the Crosstable prefix.](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-crosstable-sense-chart.png)
> **Note:** To learn more about Crosstable, see this blog post in Qlik Community: [The Crosstable Load](https://community.qlik.com/t5/Qlik-Design-Blog/The-Crosstable-Load/ba-p/1468083).
> The behaviors are discussed in the context of QlikView. However, the logic applies equally to Qlik Sense.

Numeric interpretation will not work for the attribute fields. This means that if you have months as column headers, these will not be automatically interpreted. The work-around is to use the Crosstable prefix to create a temporary table, and to run a second pass through it to make the interpretations as shown in the following example.

Note that this is an example only. There are no accompanying exercises to be completed in Qlik Sense.

tmpData:
Crosstable (MonthText, Sales)
LOAD Product, [Jan 2014], [Feb 2014], [Mar 2014], [Apr 2014], [May 2014], [Jun 2014]
FROM ...
Final:
LOAD Product,
Date(Date#(MonthText,'MMM YYYY'),'MMM YYYY') as Month,
Sales
Resident tmpData;
Drop Table tmpData;

## Clearing the memory cache

You can delete tables that you create to clear the memory cache. When you load into a temporary, as in the previous section, you should drop it when it is not needed anymore. For example:

DROP TABLE Table1, Table2, Table3, Table4;
DROP TABLES Table1, Table2, Table3, Table4;

You can also drop fields. For example:

DROP FIELD Field1, Field2, Field3, Field4;
DROP FIELDS Field1, Field2, Field3, Field4;
DROP FIELD Field1 from Table1;
DROP FIELDS Field1 from Table1;

As you can see, the keywords TABLE and FIELD and can be singular or plural.
