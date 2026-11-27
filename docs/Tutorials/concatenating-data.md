---
title: "Concatenation"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Tutorials/concatenating-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Tutorial - Scripting for beginners"]
---

# Concatenation

Concatenation is an operation that takes two tables and combines them into one.

The two tables are added to each other by stacking one on top of the other, with a column for each distinct column name. The data is not changed and the resulting table contains the same number
of records as the two original tables together. Several concatenate operations can be performed
sequentially, so that the resulting table is concatenated from more than
two tables.

## Automatic concatenation

If the [field](#glossary-0 "Glossary term") names and the number of fields of two or more loaded tables are exactly the same, the application will automatically concatenate the content of the different statements into one table.

The number and names of the fields must be exactly the same for automatic concatenation to take place. The order of the two LOAD statements is arbitrary, but the table will be given the name of the table that is loaded first.

Do the following:

1. Open the Data load editor in the Scripting Tutorial application.
2. Click the Date tab.
3. Click Load data.

Based on the [load script](#glossary-1 "Glossary term") that you have written so far, the application loads 628 lines from the Dates.xlsx data file into Table2.

Data load progress window

![Data load progress window](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-load-progress-dates.png "Click to view full size")4. On a new line in the script in the section Dates, copy and paste the LOAD statement for Table2. This will cause the data to be loaded twice. Name the second table Table2a.

You could also delete the existing script, and copy and paste the following:

```
Table2:
					LOAD
					"Date",
					Month (Date) as "Month",
					Quarter,
					"Week",
					"Year"
					FROM [lib://DataFiles/Dates.xlsx]
					(ooxml, embedded labels, table is Dates);

					Table2a:
					LOAD
					"Date",
					Month (Date) as "Month",
					Quarter,
					"Week",
					"Year"
					FROM [lib://DataFiles/Dates.xlsx]
				(ooxml, embedded labels, table is Dates);
```

Your script should look like this:

Load script in Dates tab

![Load script in Dates tab.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-load_dates_concat-cloud-rev.png "Click to view full size")5. Click Load data.

The application does not load Table2 and then Table2a. Instead, it recognizes that Table2a has the same field names and the number of fields as Table2. It then adds the data of Table2a to Table2, and deletes table Table2a. The result is that Table2 now has 1,256 lines.

Concatenation in data load progress window

![ Concatenation in data load progress window.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-load-progress-dates-concat.png "Click to view full size")6. Open the Data model viewer.
7. Click Show preview.

Only Table2 was created. Select Table2. The table has 1256 rows.

[Data model viewer](#glossary-2 "Glossary term") showing Table2

![Data model viewer showing Table2. ](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_data_model_viewer_table2.png "Click to view full size")

## Forced concatenation

Even if two or more tables do not have exactly the same set of fields, it is still possible to force the application to concatenate the two tables. This is done with the Concatenate prefix in the script, which concatenates a table with another named table or with the most recently created table.

Do the following:

1. Edit the LOAD statement for Table2a, adding Concatenate and commenting out Week.

Your script should now appear as follows:

```
Table2a:
					Concatenate LOAD
					"Date",
					Month (Date) as "Month",
					Quarter,
					// "Week",
					"Year"
					FROM [lib://DataFiles/Dates.xlsx]
				(ooxml, embedded labels, table is Dates);
```

By commenting out Week, we make sure that the tables are not identical.

2. Click Load data.
3. Open the Data model viewer.

Now you can see that Table2a has not been created.

4. Click Table2 in the data model viewer, and then click Preview.

The table has the fields Date, Month, Quarter, Week, and Year. The field Week is still showing, because it was loaded from Table2.

5. Click Week in Table2. The preview shows that the number of non-null values for the field is 628. However, it you click any of the other fields, you see that number of non-null values is 1256. Week was loaded just once, from Table2. The number of values, or records, is the sum of the number of records in Table2 and Table2a.

## Preventing concatenation

If the field names and the number of fields of two or more loaded tables are exactly the same, the application will automatically concatenate the content of the different statements into one table. This can be prevented with a NoConcatenate statement. The table loaded with the associated LOAD or SELECT statement will then not be concatenated with the existing table.

Do the following:

1. To be able to separate the content of the two tables completely, add NoConcatenate to the LOAD statement in Table2a, and rename the fields so that the application does not create a synthetic key based on the matching fields. Uncomment Week in Table2 so that the two tables have the same fields.

Your script should now appear as follows:

```
Table2:
					LOAD
					"Date",
					Month (Date) as "Month",
					Quarter,
					"Week",
					"Year"
					FROM [lib://DataFiles/Dates.xlsx]
					(ooxml, embedded labels, table is Dates);

					Table2a:
					NoConcatenate LOAD
					"Date" as "Date2",
					Month (Date) as "Month2",
					Quarter as "Quarter2",
					"Week" as "Week2",
					"Year" as "Year2"
					FROM [lib://DataFiles/Dates.xlsx]
				(ooxml, embedded labels, table is Dates);
```

2. Click Load data.
3. Open the Data model viewer.

Now you can see that the two tables are completely separated.

Data model viewer showing Table2 and Table 2a

![Data model viewer showing Table2 and Table 2a.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-data-model-sales-noconcat.png "Click to view full size")4. Now that we have finished demonstrating concatenation, we no longer need Table2a. Delete all the rows in the LOAD statement for Table2a, and then click Load data.
