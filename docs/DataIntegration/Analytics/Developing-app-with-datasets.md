---
title: "Creating an analytics application using datasets generated in Data Integration"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/Analytics/Developing-app-with-datasets.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data"]
---

# Creating an analytics application using datasets generated in Data Integration

You can use the datasets and data products created by Qlik Talend Data Integration in an analytics application in Qlik Cloud Analytics.

You can also use the datasets in:

- On-demand applications
- Dynamic views
- Third-party applications

## Creating an application from a data product

Tip note

For data products that are downstream from a Qlik Talend Data Integration data pipeline, original relationships from the source pipeline are provided as suggestions when you edit the semantic model.

For more information, see [*Defining relationships*](../DataProducts/managing-semantic-models.htm#Relationships).

Analytics developers can load data products, with their semantic models, into analytics applications using the data catalog. The data catalog generates the necessary script and creates master items for measures and dimensions.

For full details, see [*Consuming data products in applications*](../DataProducts/consuming-data-products-apps.htm).

## Creating an application from a QVD dataset

Before creating an application, you can see information about the table in the Overview tab.

If you manage the QVD storage yourself you need to connect the table before you can use the Create analytics app button or the Profile tab.

1. Click Catalog and select Datasets in Types to view the tables.
2. Click Open dataset.
3. Click Use in > Application. The Create a new application window opens.
4. Click Next. You are redirected to the list of datasets. They are selected by default.
5. If needed, select or clear datasets' check boxes to include/exclude them, and click Next.
6. Review the summary of the selected data. You can click each individual dataset to get a preview of the fields they contain.
7. Optionally select the Open application check-box to directly view the application once it’s created.
8. Click Load into application.

For more information about creating analytics applications, see [Creating applications and adding data](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/create-app-cloud-hub.htm).

### Connecting a QVD dataset

If you manage the storage yourself, as opposed to using Qlik managed storage, you need to connect the dataset before you can use Create application from data or Data profile.

1. Open the table.
2. Click Connect to dataset.

   Connect to dataset settings are displayed. Bucket Name is already filled in.
3. Add your Access Key and Secret Key for the displayed bucket.
4. Click Connect to dataset.

You should now be able to:

- Click Data profile to view information about the data profile.
- Click Create application from data to create a new analytics application based on the QVD table.

## Using datasets generated in cloud data warehouses

1. Make sure that you have a connection to the cloud data warehouse where the generated datasets are stored.
2. Connect to the cloud data warehouse and add the views you need to your application.

It is best practice to use views when reading the data, instead of the physical storage tables.

For more information about connecting to cloud data warehouses, see the relevant information for your cloud data warehouse in [*Data sources in Qlik Cloud Analytics*](../../../Sense_Helpsites/Connectors_SaaS.htm#Data).

## Reloading data

The tables will be continuously updated by the data tasks to be in sync with the data source, but an application consuming the tables will not be automatically refreshed. When the application is ready you need to create a reload schedule to have the application data refreshed continuously. You can either schedule the application to be reloaded when the data is refreshed, or create a schedule based on time and frequency. If you select a time-based schedule, you need to consider the timing of the reload schedule. We recommend that you reload the application at a time when the tables are likely to have been updated with fresh data if possible.

For more information, see [Reloading application data](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Apps/reloading-apps-cloud-hub.htm).

Information noteEvery time the application gets new data, all visualizations need to be recalculated.

Warning noteIf you keep transactional history that is not available in the source anymore, this data will be lost when you reload the application.
