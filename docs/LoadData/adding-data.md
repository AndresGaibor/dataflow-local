---
title: "Adding data to the application from connections and new files"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/adding-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and managing data with Data Manager"]
---

# Adding data to the application from connections and new files

You can add data to your application quickly. Open the Data manager, and then click ![Add](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) Add data > Files and other sources. You can also click Add data in ![Navigation](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) in the top bar. You are also prompted to add data when you create a new application. When you are editing a sheet, you can also click Add in the Fields panel to add data.

Information noteThe add data options and data sources that are available to you depend on your Qlik Sense platform and configuration.

Add data view

![Add data view](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_AddDataCloudHub.png "Click to view full size")

## In-Application

Manual entry. Click to create a table in-application and add the data to the application.

## Existing connections

You can view existing [connections](#glossary-1 "Glossary term") and file locations by space. Use the drop-down list to select from which space you want to add data.

### File locations

Data files: Click to upload a data file, or to add data from a file that has already been uploaded.

### Data connections

Displays connections that have been created to an external data source. The connection appears after it has been created under Connect to a new data source.

Click a connection to add data to the application.

## Add data

Click to add data to an application. The button is enabled after you have created a connection and selected your data to load. You can add data with profiling enabled or disabled. Data profiling is recommended and enabled by default. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) to disable data profiling.

## Which data sources are available to me?

The availability of data sources in Data manager depends on a number of factors:

- Space permissions

  To connect to a data source, you need to have access to the space in which it is located. See:

  - [*Managing permissions in shared spaces*](../Spaces/managing-shared-spaces.htm)
  - [*Managing permissions in managed spaces*](../Spaces/managing-managed-spaces.htm)
- Data manager limitations

  Not all connectors support connections in Data manager, and the tables available may vary from the tables available in the Data load editor and Script. See the specific connector page for details:

  - [*Data sources in Qlik Cloud Analytics*](../../Sense_Helpsites/Connectors_SaaS.htm)
  - [*Analytics sources in Qlik Cloud Analytics*](connect-analytics-sources.htm)

Related learning:

- [Reload data for analysis](/lnk/Reload_Data_Analysis_QS)
