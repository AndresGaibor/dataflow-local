---
title: "Circular references"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/circular-references.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Tutorial - Scripting for beginners"]
---

# Circular references

If there are circular references (loops) in a data structure, the tables are associated in such a way that there is more than one path of associations between two fields.

Do the following:

1. Open the Data load editor in the Scripting Tutorial application.
2. Click ![Create new section](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) to add a new script section.
3. Name the section Region.
4. Under DataFiles in the right menu, click Select data.
5. Upload and then select Region.txt. A data preview window opens.
6. Select all fields and make sure that Embedded field names under Field names is selected to include the names of the table fields when you load the data.
7. Click Add.
8. Click Load data.

This time it appears that something has gone wrong with your data load. A circular reference has been created. The Data load progress window will show an error message, stating that a circular reference was found during the load. However, the load is completed and the application is saved.

9. Open the Data model viewer.

You can drag the tables around to reorganize them in a way so that the connections between the tables are easy to see.

Data model viewer showing circular reference

![Data model viewer showing circular reference.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-circular-reference.png "Click to view full size")

The red dotted lines indicate that a circular reference has been created. This is something that you should avoid, because it may cause ambiguities in the data interpretation.

## Resolving circular references

To be able to understand what caused the circular references, let us take a closer look at your tables in the Data model viewer.

If you look at Table1 and the Table2 in the screenshot above, you can see that they have the Date [field](#glossary-1 "Glossary term") in common. You can also see that Table1 and Region have the SalesKey field in common. Finally, notice that Table2 and Region have the field Week in common. This means that a loop, a circular reference, has been created. Since this can cause problems in the data analysis later on, let us remove it.

The easiest way to resolve this is to rename or remove one of the fields. In our case, we have loaded some data that we do not need for our application, and we can remove it.

Do the following:

1. Open the Data load editor.
2. Click on the section Region and delete the following two rows in the LOAD statement:

"Week",

SalesKey

3. Make sure to also remove the comma after "Region Code".

Your script should now appear as follows:

```
LOAD
    Region,
    "Region Code"
FROM [lib://DataFiles/Region.txt]
(txt, codepage is 28591, embedded labels, delimiter is '\t', msq);
```

4. Click Load data.
5. Open the Data model viewer.

The undesired references to Region have been removed.

Data model viewer showing that circular reference has been removed

![Data model viewer showing that circular reference has been removed.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-circular-reference-fixed.png "Click to view full size")
