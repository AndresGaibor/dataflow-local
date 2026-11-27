---
title: "Adding data"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/load-data-associate-data_.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Tutorial - Build an analytics application"]
---

# Adding data

Your second step towards a complete application is associating and then loading the data.

You will associate the following files:

- Cities.xlsx
- Customers.xlsx
- Item master.xlsx
- Sales rep.csv
- Sales.xlsx

## Associating data

In the Associations view of the Data manager your data is illustrated using bubbles, with each bubble representing a data table. The size of the bubble represents the amount of data in the table. Bubbles marked with \* indicates a new or updated table. You should see five data tables.

Five data tables that have not been associated

![5 bubbles that are not associated.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_bubbles_unassociated.png "Click to view full size")

Now it is time to create an association between the fields in your tables Sales and Sales rep.

Do the following:

1. Drag the Sales rep bubble towards the Sales bubble.

   The Data manager now detects a recommended association to the Sales table. This bubble is marked with green.
2. Drop the Sales rep bubble onto the Sales bubble.

   A link is now created between the bubbles and the tables are associated using the recommended fields.
3. Click the link between the Sales rep bubble and the Sales bubble.

   The association panel, at the bottom of the screen, displays a preview of data in the associated fields.
4. Click the association Sales rep ID-Sales Rep Number in the association panel and rename it Sales Rep Number.

The association is now named Sales Rep Number.

## Adding and associating more data

You have already associated the tables Sales and Sales rep. Data manager helps you identify recommended associations.

Do the following:

1. Click and hold the bubble Customer.

   The bubbles Sales and Cities are marked green because Data manager highly suggests associating these two tables to Customers.
2. Click and hold the bubble Cities.

   The bubble Customer is marked green. The bubble Sales is marked orange, which indicates a medium recommendation.
3. Click and hold the bubble Item master.

   The bubble Sales is marked green.

Recommended associations are identified between all tables. You will now let the Data manager create the associations for you.

Do the following:

1. Make sure the Recommend associations pane is open on the right. If it is closed, you can open it by clicking ![Effects](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_effects.svg).
2. Click Apply all.

   The tables are now associated according to these recommendations. The five tables are all linked.

   ![Data that has been associated. All 5 bubbles are now connected.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_Bubbles_Associated.png)

Now you can load the data.

## Loading data

Now you have added all data files and associated their tables. Before you start building your application you must load the script.

Do the following:

1. Click Load data.

   A progress window is displayed while the data is loading. When the data load is complete, you can continue.
2. Click Close.

## Viewing the data model

Now you are ready to start building your application. Before you start, take a look at the data model.

Do the following:

1. In the toolbar, open the application navigation menu and select Data model viewer.
2. In the toolbar in the Data model viewer, click ![expand](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expand_3_outline.svg) to expand the tables.

All tables are now connected and the Data model viewer should have the following content. A [field](#glossary-1 "Glossary term") connecting one or more tables is called a key.

The Data model viewer with tables connected using key fields

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_AddData8_Customers_dmv.png "Click to view full size")

You have now finished adding data and can start building your application.

Related learning:

- [How do I load data into a Qlik Sense SaaS application?](/lnk/How_load_data_QS_SaaS_app)
