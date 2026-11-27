---
title: "Creating applications and adding data"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/create-app-cloud-hub.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with applications"]
---

# Creating applications and adding data

Applications can be added to Qlik Cloud Analytics by creating new applications, duplicating existing applications, or uploading exported applications.

Information note

- To create applications in your personal space, you need the Private Analytics Content Creator role.
- In user-based subscriptions, creating applications requires a Professional user entitlement.

## Creating a new application

You can create applications by going to Create in the Analytics [activity center](#glossary-1 "Glossary term") and selecting Analytics application.
You can also create analytic applications from Analyze in Analytics or by clicking Create new > Application in Catalog.
When you create a new application, you can specify the destination space of the application. By default, applications are added to the current space.

## Creating an application from data

You can create a new application directly from a [dataset](#glossary-2 "Glossary term"). Applications created this way are added to the same spaces as the data.

Do the following:

1. You can either:

   - In your activity center, click ![More actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the dataset and select Use in > Application.
   - In an open dataset, click Use in > Application.

   The Create a new application dialog opens.

   From the Use in dropdown list, you can also use the dataset in a table recipe, data flow, script, or ML experiment.
2. In the corresponding field, enter a Name for the application.
3. From the corresponding drop-down list, select in which Space you want to save the application.
4. Add a Description to document the purpose of the application.
5. Add some Tags to the application to make it easier to find.
6. Click Next. You are redirected to the list of datasets. They are selected by default.
7. If needed, select or clear datasets' check boxes to include/exclude them, and click Next.
8. Review the summary of the selected datasets. You can click each individual dataset to get a preview of the fields they contain.
9. Optionally select the Open application check-box to directly view the application once it’s created.
10. Click Load into application.

## Adding data to applications

Once you create your new application, you need to add data to your application. Data files and connections to data sources can be added directly in a space. See [*Adding and managing your analytics data*](../Spaces/managing-data-resources-spaces.htm). You can also add them from within an application, either in Data manager or Data load editor.

Qlik Sense uses a data [load script](#glossary-3 "Glossary term") to connect to and retrieve data from your data sources in an application. You can interact with the data load script using Data manager or Data load editor.

### Data manager

[Data manager](#glossary-4 "Glossary term") provides a guided interface for adding and loading data in a Qlik Sense application. You can also edit and transform data in the loaded tables, such as replacing values, setting nulls, and splitting fields. You can also concatenate or join tables. If you create your application directly from a data source, it will be automatically be loaded in Data manager.

Data manager also allows you to also manage the associations between tables to link key fields across tables. Data manager generates a load script automatically for the data you load and transform in Qlik Sense.

Information note

Data manager (including its Data catalog interface) does not support adding data from data products. To add data from data products, use Data load editor—either using Data load editor's Data catalog interface or by writing script manually.

For more information on Data manager, see [*Loading and managing data with Data Manager*](../LoadData/managing-data.htm).

### Data catalog

The [data catalog](#glossary-5 "Glossary term") allows you to view all the datasets to which you have access. This makes it easy to select the tables and fields you want to add to your application from the datasets available to you.

Once you add data with the data catalog, you can make associations and edit the data in Data manager or Data load editor before loading it into your application.

For more information, see [*Loading data from the data catalog*](../LoadData/adding-data-catalog.htm).

### Data load editor

[Data load editor](#glossary-6 "Glossary term") allows you to directly work in the application load script, adding and loading data using Qlik scripting functions.

In your load script, you specify the fields and tables to load. During the load, Qlik Sense automatically identifies key fields to associate the data. You can monitor this data structure in the data model viewer.

You can manipulate the data structure with script statements using functions. Data load editor provides you with a broad set of tools for loading and transforming application data. You can use the script to perform operations such as:

- Calculating new values
- Translating coded values
- Aggregating values
- Joining or concatenating tables
- Validating data

Some application settings and functionality can only be set in the Data load editor. Space-aware connections, which allow you to load data from another space or make your load script look for data sources of a specific name in the current space, can only be defined in Data load editor. Changing an application's locale and regional settings can only be set in the load script. For more information, see [*Modifying regional settings for applications and scripts*](regional-settings-in-apps.htm).

For more information on Data load editor, see [*Loading and transforming data with scripting*](../Scripting/introduction-data-modeling.htm).

## Adding content to applications

After you add data, you can create sheets, stories, and visualizations. Sheets, stories, and bookmarks in your application are private until you make them public. For more information, see [*Granting access to sheets, sheet groups, bookmarks, and stories*](../Share/make-public-or-private.htm).

For more information on creating sheets and visualizations, see: [*Creating and editing visualizations*](../Visualizations/create-visualizations-overview.htm).

Related learning:

- [Getting Started with Qlik Cloud](/lnk/Getting_started_Qlik_Cloud)
- [How do I create an application?](/lnk/How_create_app)
