---
title: "Step-by-step - Combining tables using forced concatenation"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/step-by-step-concatenate-tables.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and managing data with Data Manager"]
---

# Step-by-step - Combining tables using forced concatenation

Expand/Collapse all

# Step-by-step - Combining tables using forced concatenation

This step-by-step walkthrough shows how you can use forced concatenation to combine two similar data tables.

Forced concatenation can be used to clean up your data before you use it for analysis in a [sheet](#glossary-0 "Glossary term"). You can concatenate two tables into one table. You can also add another table later, for example if you initially add a table from June, and then later want to add a second table from July.

## Concatenation at a glance

- Tables are automatically concatenated in [Data manager](#glossary-1 "Glossary term") when Qlik Sense detects that one or more added tables have both the same number of fields and identical field names as another table. In this case, you can split the tables if needed.
- Two tables can be force concatenated when tables do not entirely share the same fields or data. Only two tables can be force concatenated. To concatenate three tables, for example, concatenate the first two tables into one table. Concatenate the third table to that created table.
- Tables that are not similar enough will not automatically be concatenated. You also will not be able to forcibly concatenate them. In this case, the fields in the table should instead be associated in the Data manager.

## Walkthrough - Forced concatenation

These are the tasks required to complete the walkthrough:

1. Prepare the data tables
2. Add data tables to an application
3. Concatenate and load data tables into an application
4. A step further - adding a new table and concatenating the data fields

### Prerequisites

You should know how to create an application in Qlik Sense. For more information, see [*Creating applications and adding data*](../Apps/create-app-cloud-hub.htm).

### Prepare the data tables

We have supplied some sample data for you to use to demonstrate forced concatenation. You can also use your own data, provided the fields and data are mostly the same in your two tables.

For example, here is the header and first row of the data that we supplied below. It has been pasted into two Excel tables. Note the differences in the fields.

![Excel tables.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/concat_excel_tabs.png)

If you want to use the sample data, expand the section below, and copy the tables, including the column headings, into two separate tabs in an empty Excel file on your computer. For this walkthrough, we named the Excel tabs *Data Table 1* and *Data Table 2*. We named the Excel file *Concatenate\_Data.xlsx*.

Data Table 1

Data Table 1

| SalesOrderID | SalesOrderDetailID | TrackingNumber | OrderQty | PID | SpecialOfferID | UnitPrice | Modified Date |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 43659 | 1 | 4911-403C-98 | 1 | 776 | 1 | 1822.4946 | 7/1/2013 0:00 |
| 43659 | 2 | 4911-403C-98 | 3 | 777 | 1 | 1822.4946 | 7/2/2013 0:00 |
| 43659 | 3 | 4911-403C-98 | 1 | 778 | 1 | 1098.9 | 7/2/2013 0:00 |
| 43659 | 4 | 4911-403C-98 | 1 | 771 | 1 | 1835.9946 | 7/2/2013 0:00 |
| 43659 | 5 | 4911-403C-98 | 1 | 772 | 1 | 1835.9946 | 7/3/2013 0:00 |
| 43659 | 6 | 4911-403C-98 | 2 | 773 | 1 | 1835.9946 | 7/3/2013 0:00 |
| 43659 | 7 | 4911-403C-98 | 1 | 774 | 1 | 1835.9946 | 7/4/2013 0:00 |
| 43659 | 8 | 4911-403C-98 | 3 | 714 | 1 | 25.95636 | 7/4/2013 0:00 |
| 43659 | 9 | 4911-403C-98 | 1 | 716 | 1 | 25.95636 | 7/5/2013 0:00 |
| 43659 | 10 | 4911-403C-98 | 6 | 709 | 1 | 5.13 | 7/5/2013 0:00 |
| 43659 | 11 | 4911-403C-98 | 2 | 712 | 1 | 4.66785 | 7/6/2013 0:00 |
| 43659 | 12 | 4911-403C-98 | 4 | 711 | 1 | 18.16785 | 7/6/2013 0:00 |
| 43660 | 13 | 6431-4D57-83 | 1 | 762 | 1 | 377.51301 | 7/7/2013 0:00 |
| 43660 | 14 | 6431-4D57-83 | 1 | 758 | 1 | 787.3146 | 7/7/2013 0:00 |
| 43661 | 15 | 4E0A-4F89-AE | 1 | 745 | 1 | 728.784 | 7/7/2013 0:00 |
| 43661 | 16 | 4E0A-4F89-AE | 1 | 743 | 1 | 643.23387 | 7/8/2013 0:00 |
| 43661 | 17 | 4E0A-4F89-AE | 2 | 747 | 1 | 643.23387 | 7/8/2013 0:00 |
| 43661 | 18 | 4E0A-4F89-AE | 4 | 712 | 1 | 4.66785 | 7/8/2013 0:00 |
| 43661 | 19 | 4E0A-4F89-AE | 4 | 715 | 1 | 25.95636 | 7/9/2013 0:00 |

DataTable 2

Data Table 2

| SalesOrderID | SalesOrderDetailID | TrackingNumber | OrderQty | ProductID | UnitPrice | Modified Date |
| --- | --- | --- | --- | --- | --- | --- |
| 43662 | 20 | 2E53-4802-85 | 3 | 764 | 377.51301 | 7/12/2013 0:00 |
| 43662 | 21 | 2E53-4802-85 | 5 | 770 | 377.51301 | 7/12/2013 0:00 |
| 43662 | 22 | 2E53-4802-85 | 2 | 730 | 165.54438 | 7/13/2013 0:00 |
| 43662 | 23 | 2E53-4802-85 | 4 | 754 | 787.3146 | 7/14/2013 0:00 |
| 43662 | 24 | 2E53-4802-85 | 3 | 725 | 165.54438 | 7/14/2013 0:00 |
| 43662 | 25 | 2E53-4802-85 | 5 | 762 | 377.51301 | 7/14/2013 0:00 |
| 43662 | 26 | 2E53-4802-85 | 3 | 765 | 377.51301 | 7/14/2013 0:00 |
| 43662 | 27 | 2E53-4802-85 | 2 | 768 | 377.51301 | 7/15/2013 0:00 |
| 43662 | 28 | 2E53-4802-85 | 1 | 753 | 1932.2658 | 7/15/2013 0:00 |
| 43663 | 29 | 2E53-4802-85 | 1 | 756 | 787.3146 | 7/16/2013 0:00 |
| 43663 | 30 | 2E53-4802-85 | 3 | 763 | 377.51301 | 7/17/2013 0:00 |
| 43664 | 31 | 2E53-4802-85 | 1 | 732 | 321.2082 | 7/18/2013 0:00 |
| 43664 | 32 | 2E53-4802-85 | 6 | 758 | 787.3146 | 7/19/2013 0:00 |
| 43665 | 33 | 2E53-4802-85 | 1 | 729 | 165.54438 | 7/19/2013 0:00 |

### Add data tables to an application

Do the following:

1. Click Create new app in your work area. The Create new app window opens.
2. Name your application, and then click Create. The application is created. We named our application *ConcatenateExample*
3. Click Open app. The application opens and displays a dialog where you can add data.
4. Drag and drop your Excel file into the Add data from files and other sources dialogue. Your tables are displayed in the Associations view of the Data manager. Click a bubble to see the data for that table.

   Information noteIf you add data instead from Data manager, you will first be asked to select table fields before being taken to the Associations view of the Data manager. In this case, select all the fields for both tables.

   ![Associations view with two bubbles.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_Concat_AssociationsView_SaaS.png)

### Concatenate tables and load data tables into an application

After the data tables have been added to the application, the tables can be concatenated.

Do the following:

1. In the Associations view of Data manager, select one table by clicking the bubble. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and then select Concatenate or join.

   ![Associations view with option Concatenate tables.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_Concat_Select_SaaS.png)
2. Click the bubble for the other table, and then click Edit mappings.

   ![Associations view with option Edit mappings](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ConcatMappings_SaaS.png)
3. You can now do the following as required:

   1. In Table name, rename the table that will be created when you combine the tables.
   2. Combine fields by dragging and dropping field labels.
   3. Rename fields.
   4. Delete fields by clicking ![Cancel](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_remove.svg) for the field.

   ![Edit mappings view with several options.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ConcatEditing_SaaS.png)

   In our example, we did the following:

   1. Renamed our table to Data Table.
   2. Dragged the ProductID label and field to below the PID field, to combine the fields.
   3. Renamed the PID field to Product ID.
   4. Deleted the SpecialOfferID field.

   Our table now looks like this:

   ![Edit mappings view with the result after editing.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ConcatTableDone_SaaS.png)
4. In the Selection action drop-down, click Concatenate, and then click Apply. The tables are concatenated on the mapped fields. The \* indicates that the data has not yet been loaded into the application.

   ![Table 'Data Table' with an *.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ConcatBubble2.png)
5. Click Load data. A message is displayed indicating that the data was loaded successfully. Click Edit sheet to create visualizations using the data.

## A step further - adding a new table and concatenating the data fields

The sample data provided above was pasted into two tabs in the same Excel file. However, the tables do not need to be in same file when you want to concatenate fields. The tables can be in separate files that are added to the application. Another table can also be added later, for example if you initially add a table from June, and then later want to add a second table from July.

In this example, we add another table with similar fields to the concatenated table we created above.

Here is the sample data. We named the tab that contains the table *DataTable\_Newest*. We named the data file *Concatenate\_Data2.xlsx*.

DataTable\_Newest

DataTable\_Newest

| SalesOrderID | SalesOrderDetailID | TrackingNumber | ZIP | OrderQty | ID | UnitPrice | Modified Date |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 43666 | 34 | 568E-472E-9C | 20012 | 3 | 764 | 377.51301 | 7/12/2013 0:00 |
| 43666 | 34 | 568E-472E-9C | 23220 | 5 | 770 | 377.51301 | 7/12/2013 0:00 |
| 43667 | 35 | AB6C-4FF9-9D | 30004 | 2 | 730 | 165.54438 | 7/13/2013 0:00 |
| 43668 | 36 | AB6C-4FF9-9D | 11215 | 4 | 754 | 787.3146 | 7/14/2013 0:00 |
| 43668 | 36 | AB6C-4FF9-9D | 55401 | 3 | 725 | 165.54438 | 7/14/2013 0:00 |
| 43668 | 36 | AB6C-4FF9-9D | 20003 | 5 | 762 | 377.51301 | 7/14/2013 0:00 |
| 43668 | 36 | AB6C-4FF9-9D | 15213 | 3 | 765 | 377.51301 | 7/14/2013 0:00 |
| 43669 | 37 | C618-4998-BE | 33125 | 2 | 768 | 377.51301 | 7/15/2013 0:00 |
| 43669 | 37 | C618-4998-BE | 11215 | 1 | 753 | 1932.2658 | 7/15/2013 0:00 |

Do the following:

1. From the Analytics [activity center](#glossary-3 "Glossary term"), click the application that you created in the procedures above. The application opens.
2. Select Data manager from the drop-down list in the top toolbar. The Data manager opens and the table you created in the procedure above is shown.

   ![Data manager with bubble 'Data Table'.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ConcatDataManagerNew_SaaS.png)
3. Click the ![Add](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) button to add data.
4. Click Data files in the left menu, and then click DataFiles under Folder shortcuts. Upload your new data file.
5. Select the file. The Add data window opens.
6. Click Add data to add the data table to the application.

   The new table is added to your application.

   ![Associations view with two bubbles.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ConcatTableAddNew_SaaS.png)
7. You can now concatenate the tables, edit the mappings, and then load the data.
