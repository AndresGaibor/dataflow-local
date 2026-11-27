---
title: "Generic databases"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataSource/generic-databases.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Modeling your data", "Best practices for data modeling"]
---

# Generic databases

A generic database is a table in which the [field](#glossary-0 "Glossary term") names are stored as field values in one column, while the field values are stored in a second. Generic databases are usually used for attributes of different objects.

Look at the example GenericTable below. It is a generic database containing two objects, a ball and a box. Obviously some of the attributes, like color and weight, are common to both the objects, while others, like diameter, height, length and width are not.

GenericTable

| object | attribute | value |
| --- | --- | --- |
| ball | color | red |
| ball | diameter | 10 cm |
| ball | weight | 100 g |
| box | color | black |
| box | height | 16 cm |
| box | length | 20 cm |
| box | weight | 500 g |
| box | width | 10 cm |

On one hand it would be awkward to store the data in a way giving each attribute a column of its own, since many of the attributes are not relevant for a specific object.

On the other hand, it would look messy displaying it in a way that mixes lengths, colors and weights.

If this database is loaded into Qlik Sense using the standard way and the data is displayed in a table, it looks like this:

![Data base data displayed in a table.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_gen_NonGeneric.png)

However, if the table is loaded as a generic database, column two and three will be split up into different tables, one for each unique value of the second column:

![Generic data model.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_gen_GenericDatabase.png)

The syntax for doing this is simple, as shown in the following example.

Example

### Load script

Add the example script to your application and run it. To see the result, add the fields listed in the results column to a sheet in your application.

```
Sheet1:
Generic Load * inline [
object, attribute, value
ball, color, red
ball, diameter, 10 cm
ball, weight, 100 g
box, color, black
box, height, 16 cm
box, length, 20 cm
box, weight, 500 g
box, width, 10 cm ];
```

For more information about using inline loads, see [*Using inline loads to load data*](../Scripting/inline-loads-qs.htm).

### Result

Resulting table

| object | color | diameter | length | height | width | weight |
| --- | --- | --- | --- | --- | --- | --- |
| ball | red | 10 cm | - | - | - | 100 g |
| box | black | - | 20 cm | 16 cm | 10 cm | 500 g |
