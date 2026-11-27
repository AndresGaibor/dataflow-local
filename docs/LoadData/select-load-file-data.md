---
title: "Selecting and loading data"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/select-load-file-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Tutorial - Scripting for beginners"]
---

# Selecting and loading data

Loading data from files, such as Microsoft Excel or any other supported file format, is easily done by using the data selection dialog in the data load editor.

Do the following:

1. Create a new application.
2. Name the application Scripting Tutorial, and then click Create.
3. Open the application.

Information noteBefore you load data into your application for the first time, there is an option to use Add data to easily load data from files. However, in this tutorial we want to see the script, so we will use the data load editor.

4. Open Data load editor from the drop-down menu in the top toolbar.
5. Click ![Create new section](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) in the left menu to add a new script section below the section named Main.

Using more than one section makes it easy to keep your script organized. The script section will execute in order when you load data.

6. Give the section a name by typing Sales.
7. Expand the Data sources panel if not already expanded. A menu appears on the right.
8. Under DataFiles in the right menu, click Select data.

Select data window

![Select data window.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-select-data-cloud-rev2.png "Click to view full size")9. Upload and then select Sales.xlsx. A data preview window opens.

Data preview window for Sales data file

![Data preview window for Sales data file.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial_data-preview-rev.png "Click to view full size")10. Deselect the fields # of Days Late and # of Days to Ship. You might need to click on the field headings to see the complete field names.
11. Search for date in the Filter fields search field.
12. Click on the heading Invoice Date and type Bill Date to rename the field.
13. Click Add.
     The load script is inserted into the Sales section of the script editor. Note that the application puts double quotes around field names that contain a space.

Your script should look like this:

Load script in Sales tab

![Load script in Sales tab.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-insert_sales_script-cloud-rev.png "Click to view full size")14. Add the following row above the LOAD statement to name the table Table1:

```
Table1:
```

15. Now adjust the script to ensure that the dates are interpreted correctly. Change the Date field to the following:

```
Date(`Date`,'MM/DD/YYYY') as "Date",
```

Your script should look like this:

Updated load script in Sales tab

![Updated load script in Sales tab.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-insert_script_sales_update-cloud-rev.png "Click to view full size")16. In the upper right corner, click Load data.

This will load the data into the application. A script execution progress window is displayed. When it is finished you will see a summary of possible errors and synthetic keys even if there are none.

17. Click Close.
18. Open the data model viewer from the drop-down menu in the top toolbar. By clicking ![New tab](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_new_tab.svg) the data model viewer will open in a new tab.
19. Select ![Expand](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expand_3_outline.svg) and ![Scatter chart](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_scatter_chart_outline.svg) in the top menu to show the table view that is used in this tutorial. If your table is not displayed properly, you can remove the existing load script and build the script again.

Table view in data model viewer of Sales data

![Table view in data model viewer of Sales data.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-data-model-sales.png "Click to view full size")

Now, let's load another table called Dates. After we load the table, the application will connect it with the Sales table on the Date [field](#glossary-1 "Glossary term").

20. Open the Data load editor.
21. Click ![Create new section](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) to add a new script section.
22. Name the section Dates. If the new section Dates is not already placed below Sales, move the pointer over ![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/LUIicons_draggable.svg), and then drag the section down below the section Sales to rearrange the order.
23. Click on the top row of the script and click ![Comment / Uncomment](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_comment_outline.svg).

    Make sure // is added into the script.
24. Add the following text after //:

```
Loading data from Dates.xlsx
```

The top line of your script should now look like this:

// Loading data from Dates.xlsx

25. Under DataFiles in the right menu, click Select data.

Tip noteUnder Field names, make sure that Embedded field names is selected to include the names of the table fields when you load the data.

26. Upload and then select Dates.xlsx. A data preview window opens.

Data preview window for Dates data file

![Data preview window for Dates data file.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial_data-preview-dates-rev.png "Click to view full size")27. Click Add.

Your script should look like this:

Load script in Dates tab

![Load script in Dates tab.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial_insert_script_dates_cloud-rev.png "Click to view full size")28. Add the following on the row above the LOAD statement to name the table Table2:

```
Table2:
```

29. To ensure that the Month column in the file Dates.xlsx is interpreted correctly in the application, we need to apply the Month function to the Date field.

Change the Month field to the following:

```
Month (Date) as "Month",
```

Your script should look like this:

Updated load script in Dates tab

![Updated load script in Dates tab.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-format_month-cloud-rev2.png "Click to view full size")

Now you have created a script to load the selected data from the file Dates.xlsx. It is time to load the data into the application.

30. In the upper right corner, click Load data.

When you click Load data, the data is loaded into the application and the script is saved.

31. When the script execution is finished, click Close.
32. Open the Data model viewer.

Now you can see that a connection has been made between the two fields named Date in the two tables.

Table view in data model viewer

![Table view in data model viewer. Tables are connected on Date field.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-data-model-sales-dates.png "Click to view full size")33. Click Preview in the bottom left corner. Click on the name of the table Table2.

This will display information about the table. In the Preview field you can see that 628 rows of data have been loaded into the internal table Table2. If you instead click on a field in the table, you will see information about the field.

Table preview in data model viewer

![Table preview in data model viewer.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-data-model-preview-sales-dates.png "Click to view full size")

The data is now available to use in [visualizations](#glossary-2 "Glossary term") in an application. We will show you how later in this tutorial.
