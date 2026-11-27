---
title: "Getting started with loading your data"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/Workflow/workflow.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data"]
---

# Getting started with loading your data

Expand/Collapse all

# Getting started with loading your data

Qlik Cloud Analytics offers a variety of ways to load and transform your data for use in Qlik Sense applications.

The best method of adding your data to Qlik Cloud and loading it into an application depends on the type of data you are working with.

This topic provides several workflows by data type.

- Existing data sources
- New data files
- New web, cloud, and database sources
- New manually-entered data

## Existing data sources

You may have access to existing data sources in Qlik Cloud. You may have already added these sources or they may be made available to you by others.

If you are using an existing [dataset](#glossary-1 "Glossary term"), such as an [QVD](#glossary-2 "Glossary term") or XLSX file, the [data catalog](#glossary-3 "Glossary term") is the best tool for loading your data into an application.

Loading existing datasets with the data catalog

1. Optionally, review your dataset with the catalog tools.

   Catalog tools help you improve your data efficiency while maintaining security and compliance standards.

   [*Understanding your data with catalog tools*](../../Catalog/catalog-overview.htm)
2. Create a new application or open an existing application.

   [*Creating applications and adding data*](../../Apps/create-app-cloud-hub.htm)
3. Select the data you want to load into your application using the data catalog.

   You can use the data catalog with either Data manager or Data load editor.

   [Data manager](#glossary-4 "Glossary term") provides a guided interface for adding and managing data in an application.

   Data load editor allows you to work directly with the application [load script](#glossary-5 "Glossary term"), adding and loading data using Qlik Sense scripting functions.

   [*Loading data from the data catalog*](../adding-data-catalog.htm)
4. Prepare the data in your application.

   If you are loading data with Data manager, do the following:

   1. Optionally, edit and transform your data in the application.

      [*Loading and managing data with Data Manager*](../managing-data.htm)

      [*Editing a table*](../editing-table.htm)
   2. Associate your tables.

      Associating tables links tables by key fields.

      [*Managing data associations*](../associating-data.htm)

   If you are loading data with Data load editor, do the following:

   1. Optionally, edit and transform the data you added with the data catalog.

      [*Using Data load editor*](../use-data-load-editor.htm)

      [*Understanding script syntax and data structures*](../understand-data-structures.htm)
   2. If your tables do not have key fields linking them together, change the [field](#glossary-6 "Glossary term") names to link them.

      Tables with identically named field will use those fields as key fields. You can view your associations with the data model viewer.

      [*Viewing and transforming the data model*](../../DataModeling/view-data-model.htm)
5. Optionally, if your loaded data includes geographic data, use GeoOperations to perform geographic calculations and functions.

   [*Qlik GeoOperations analytics sources*](../../../Global_Common/GeoOperationsFunctions/GeoOperations.htm)
6. Optionally, if you need to limit access to data in your application, add Section Access to your load script.

   Section Access is used to control the security of your applications. You add a security table to define which users can see what. Qlik Sense then uses that information to reduce data to the appropriate scope when each user opens the application.

   [*Managing data security with Section Access*](../../Scripting/Security/manage-security-with-section-access.htm)
7. Load your data and troubleshoot any issues.
8. Optionally, prepare your application's [logical model](#glossary-7 "Glossary term") for Insight Advisor.

   Insight Advisor uses a logical model to generate analyses. You can define your own logical model for the application rather than letting Insight Advisor make one from learned precedents.

   [*Building logical models for Insight Advisor with Business logic*](../../BusinessLogic/business-logic-logical-models.htm)
9. Optionally, add synonyms, custom analyses, or example questions for Insight Advisor.

   You can define synonyms for terms in your data for use with Insight Advisor. You can also define analyses that should be used when users search for specific things. You can define example questions to offer application users in Insight Advisor.

   [*Creating vocabularies for Insight Advisor*](../../BusinessLogic/business-logic-vocabulary.htm)

Your application is now ready for development.

If you are using an existing [connection](#glossary-8 "Glossary term"), you can add data using Data manager or Data load editor. Data manager offers a guided experience for adding data. Data load editor allows you to script the loading of your data.

Loading data from an existing connection

1. Create a new application or open an existing application.

   [*Creating applications and adding data*](../../Apps/create-app-cloud-hub.htm)
2. If you are loading data with Data manager, do the following:

   1. Add the data to your application.

      [*Adding data from an existing data source*](../adding-data-existing-source.htm)
   2. Optionally, edit and transform your data in the application.

      [*Loading and managing data with Data Manager*](../managing-data.htm)

      [*Editing a table*](../editing-table.htm)
   3. Associate your tables.

      Associating tables links tables by key fields.

      [*Managing data associations*](../associating-data.htm)
3. If you are loading data with Data load editor, do the following:

   1. Add the data to your application.

      [*Selecting data in load scripts*](../select-data-to-load.htm)
   2. Optionally, edit and transform the data you added with the data catalog.

      [*Using Data load editor*](../use-data-load-editor.htm)

      [*Understanding script syntax and data structures*](../understand-data-structures.htm)
   3. If your tables do not have key fields linking them together, change the field names to link them.

      Tables with identically named field will use those fields as key fields. You can view your associations with the data model viewer.

      [*Viewing and transforming the data model*](../../DataModeling/view-data-model.htm)
4. Optionally, if your loaded data includes geographic data, use GeoOperations to perform geographic calculations and functions.

   [*Qlik GeoOperations analytics sources*](../../../Global_Common/GeoOperationsFunctions/GeoOperations.htm)
5. Optionally, if you need to limit access to data in your application, add Section Access to your load script.

   Section Access is used to control the security of your applications. You add a security table to define which users can see what. Qlik Sense then uses that information to reduce data to the appropriate scope when each user opens the application.

   [*Managing data security with Section Access*](../../Scripting/Security/manage-security-with-section-access.htm)
6. Optionally, prepare your application's logical model for Insight Advisor.

   Insight Advisor uses a logical model to generate analyses. You can define your own logical model for the application rather than letting Insight Advisor make one from learned precedents.

   [*Building logical models for Insight Advisor with Business logic*](../../BusinessLogic/business-logic-logical-models.htm)
7. Optionally, add synonyms, custom analyses, or example questions for Insight Advisor.

   You can define synonyms for terms in your data for use with Insight Advisor. You can also define analyses that should be used when users search for specific things. You can define example questions to offer application users in Insight Advisor.

   [*Creating vocabularies for Insight Advisor*](../../BusinessLogic/business-logic-vocabulary.htm)

Your application is now ready for development.

## New data files

If you have data files stored on-premise that you want to use with your analytics applications, you need to add them to Qlik Cloud.

If the dataset is not likely to require regular updates, you can manually upload the dataset. Once it is uploaded, you can use the data catalog to add the data you your application.

Uploading your dataset to Qlik Cloud

1. Upload your dataset to Qlik Cloud.

   [*Adding and managing your analytics data*](../../Spaces/managing-data-resources-spaces.htm#Adding)
2. Optionally, review your dataset with the catalog tools.

   [*Understanding your data with catalog tools*](../../Catalog/catalog-overview.htm)
3. Create a new application or open an existing application.

   [*Creating applications and adding data*](../../Apps/create-app-cloud-hub.htm)
4. Select the data you want to load into your application using the data catalog.

   [*Loading data from the data catalog*](../adding-data-catalog.htm)
5. Prepare your data.

   If you are loading data with Data manager, do the following:

   1. Optionally, edit and transform your data in the application.

      [*Loading and managing data with Data Manager*](../managing-data.htm)

      [*Editing a table*](../editing-table.htm)
   2. Associate your tables.

      Associating tables links tables by key fields.

      [*Managing data associations*](../associating-data.htm)

   If you are loading data with Data load editor, do the following:

   1. Optionally, edit and transform the data you added with the data catalog.

      [*Using Data load editor*](../use-data-load-editor.htm)

      [*Understanding script syntax and data structures*](../understand-data-structures.htm)
   2. If your tables do not have key fields linking them together, change the field names to link them.

      Tables with identically named field will use those fields as key fields. You can view your associations with the data model viewer.

      [*Viewing and transforming the data model*](../../DataModeling/view-data-model.htm)
6. Optionally, if your loaded data includes geographic data, use GeoOperations to perform geographic calculations and functions.

   [*Qlik GeoOperations analytics sources*](../../../Global_Common/GeoOperationsFunctions/GeoOperations.htm)
7. Optionally, if you need to limit access to data in your application, add Section Access to your load script.

   Section Access is used to control the security of your applications. You add a security table to define which users can see what. Qlik Sense then uses that information to reduce data to the appropriate scope when each user opens the application.

   [*Managing data security with Section Access*](../../Scripting/Security/manage-security-with-section-access.htm)
8. Load your data and troubleshoot any issues.
9. Optionally, prepare your application's logical model for Insight Advisor.

   Insight Advisor uses a logical model to generate analyses. You can define your own logical model for the application rather than letting Insight Advisor make one from learned precedents.

   [*Building logical models for Insight Advisor with Business logic*](../../BusinessLogic/business-logic-logical-models.htm)
10. Optionally, add synonyms, custom analyses, or example questions for Insight Advisor.

    You can define synonyms for terms in your data for use with Insight Advisor. You can also define analyses that should be used when users search for specific things. You can define example questions to offer application users in Insight Advisor.

    [*Creating vocabularies for Insight Advisor*](../../BusinessLogic/business-logic-vocabulary.htm)

Your application is now ready for development.

If your local dataset is updated frequently, you can use Qlik DataTransfer to automatically transfer the dataset to Qlik Cloud as it is updated.

Uploading your datasets to Qlik Cloud with Qlik DataTransfer

1. Install Qlik DataTransfer.

   [*Installing Qlik DataTransfer*](../../QlikDataTransfer/install-Qlik-DataTransfer.htm)
2. Set up Qlik DataTransfer to upload datasets to Qlik Cloud.

   [*Uploading on-premises data with Qlik DataTransfer*](../../QlikDataTransfer/qlik-datatransfer.htm)
3. Optionally, review your dataset with the catalog tools.

   [*Understanding your data with catalog tools*](../../Catalog/catalog-overview.htm)
4. Create a new application or open an existing application.

   [*Creating applications and adding data*](../../Apps/create-app-cloud-hub.htm)
5. Select the data you want to load into your application using the data catalog.

   [*Loading data from the data catalog*](../adding-data-catalog.htm)
6. Prepare your data.

   If you are loading data with Data manager, do the following:

   1. Optionally, edit and transform your data in the application.

      [*Loading and managing data with Data Manager*](../managing-data.htm)

      [*Editing a table*](../editing-table.htm)
   2. Associate your tables.

      Associating tables links tables by key fields.

      [*Managing data associations*](../associating-data.htm)

   If you are loading data with Data load editor, do the following:

   1. Optionally, edit and transform the data you added with the data catalog.

      [*Using Data load editor*](../use-data-load-editor.htm)

      [*Understanding script syntax and data structures*](../understand-data-structures.htm)
   2. If your tables do not have key fields linking them together, change the field names to link them.

      Tables with identically named field will use those fields as key fields. You can view your associations with the data model viewer.

      [*Viewing and transforming the data model*](../../DataModeling/view-data-model.htm)
7. Optionally, if your loaded data includes geographic data, use GeoOperations to perform geographic calculations and functions.

   [*Qlik GeoOperations analytics sources*](../../../Global_Common/GeoOperationsFunctions/GeoOperations.htm)
8. Optionally, if you need to limit access to data in your application, add Section Access to your load script.

   Section Access is used to control the security of your applications. You add a security table to define which users can see what. Qlik Sense then uses that information to reduce data to the appropriate scope when each user opens the application.

   [*Managing data security with Section Access*](../../Scripting/Security/manage-security-with-section-access.htm)
9. Load your data and troubleshoot any issues.
10. Optionally, prepare your application's logical model for Insight Advisor.

    Insight Advisor uses a logical model to generate analyses. You can define your own logical model for the application rather than letting Insight Advisor make one from learned precedents.

    [*Building logical models for Insight Advisor with Business logic*](../../BusinessLogic/business-logic-logical-models.htm)
11. Optionally, add synonyms, custom analyses, or example questions for Insight Advisor.

    You can define synonyms for terms in your data for use with Insight Advisor. You can also define analyses that should be used when users search for specific things. You can define example questions to offer application users in Insight Advisor.

    [*Creating vocabularies for Insight Advisor*](../../BusinessLogic/business-logic-vocabulary.htm)

Your application is now ready for development.

## New web, cloud, and database sources

If you have data stored on the web, in the cloud, or in databases, you can access your data to Qlik Cloud using a connector. Qlik Sense has a range of connectors available.

Once you have added your connections to Qlik Cloud, you have two options:

- You can create a dataset from your connection. This creates a data file in Qlik Cloud that data from your connection is loaded into. This makes it faster to load data from connection data sources.
- You can load directly from the connection in your application.

You can create datasets from data accessed from your connections

Create a dataset from a new connection

1. Create a connector for your data source.

   [*Adding and managing your analytics data*](../../Spaces/managing-data-resources-spaces.htm#Adding4)

   For specific connection configuration, see:

   [Web-based data-sources](/en-US/cloud-services/Subsystems/Integrated_Web_Connectors_help/Content/Connectors_QWC_BuiltIn/Introduction/IntegratedWebConnectors.htm)

   [Web storage providers](/en-US/cloud-services/Subsystems/Web_Storage_Provider_Connectors_help/Content/Connectors_StorageProvider/Introduction/Web-Storage-Provider-Connectors-Introduction.htm)

   [JDBC databases](/en-US/cloud-services/Subsystems/JDBC_Connector_help/Content/Connectors_JDBC/Introduction/JDBC-connector.htm)

   [ODBC databases](/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/Introduction/ODBC-connector.htm)

   [REST data sources](/en-US/cloud-services/Subsystems/REST_Connector_help/Content/Connectors_REST/REST-connector.htm)

   [Salesforce](/en-US/cloud-services/Subsystems/Salesforce_Connector_help/Content/Connectors_Salesforce/Introduction/Salesforce-connector.htm)

   [SAP NetWeaver](/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Connectors_SAP/SAP-SQL-connector.htm)
2. Create a new application or open an existing application.

   [*Creating applications and adding data*](../../Apps/create-app-cloud-hub.htm)
3. Select the data you want to load into your application using the data catalog.

   You can use the data catalog with either Data manager or Data load editor.

   Data manager provides a guided interface for adding and managing data in an application.

   Data load editor allows you to work directly with the application load script, adding and loading data using Qlik Sense scripting functions.

   [*Loading data from the data catalog*](../adding-data-catalog.htm)
4. Prepare the data in your application.

   If you are loading data with Data manager, do the following:

   1. Optionally, edit and transform your data in the application.

      [*Loading and managing data with Data Manager*](../managing-data.htm)

      [*Editing a table*](../editing-table.htm)
   2. Associate your tables.

      Associating tables links tables by key fields.

      [*Managing data associations*](../associating-data.htm)

   If you are loading data with Data load editor, do the following:

   1. Optionally, edit and transform the data you added with the data catalog.

      [*Using Data load editor*](../use-data-load-editor.htm)

      [*Understanding script syntax and data structures*](../understand-data-structures.htm)
   2. If your tables do not have key fields linking them together, change the field names to link them.

      Tables with identically named field will use those fields as key fields. You can view your associations with the data model viewer.

      [*Viewing and transforming the data model*](../../DataModeling/view-data-model.htm)
5. Optionally, if your loaded data includes geographic data, use GeoOperations to perform geographic calculations and functions.

   [*Qlik GeoOperations analytics sources*](../../../Global_Common/GeoOperationsFunctions/GeoOperations.htm)
6. Optionally, if you need to limit access to data in your application, add Section Access to your load script.

   Section Access is used to control the security of your applications. You add a security table to define which users can see what. Qlik Sense then uses that information to reduce data to the appropriate scope when each user opens the application.

   [*Managing data security with Section Access*](../../Scripting/Security/manage-security-with-section-access.htm)
7. Load your data and troubleshoot any issues.
8. Optionally, prepare your application's logical model for Insight Advisor.

   Insight Advisor uses a logical model to generate analyses. You can define your own logical model for the application rather than letting Insight Advisor make one from learned precedents.

   [*Building logical models for Insight Advisor with Business logic*](../../BusinessLogic/business-logic-logical-models.htm)
9. Optionally, add synonyms, custom analyses, or example questions for Insight Advisor.

   You can define synonyms for terms in your data for use with Insight Advisor. You can also define analyses that should be used when users search for specific things. You can define example questions to offer application users in Insight Advisor.

   [*Creating vocabularies for Insight Advisor*](../../BusinessLogic/business-logic-vocabulary.htm)

Your application is now ready for development.

You can add a connection to a data source in Qlik Cloud and then directly load data through the connection.

Loading data from a new connector

1. Create a connector for your data source.

   [*Adding and managing your analytics data*](../../Spaces/managing-data-resources-spaces.htm#Adding3)

   For specific connection configuration, see:

   [Web-based data-sources](/en-US/cloud-services/Subsystems/Integrated_Web_Connectors_help/Content/Connectors_QWC_BuiltIn/Introduction/IntegratedWebConnectors.htm)

   [Web storage providers](/en-US/cloud-services/Subsystems/Web_Storage_Provider_Connectors_help/Content/Connectors_StorageProvider/Introduction/Web-Storage-Provider-Connectors-Introduction.htm)

   [JDBC databases](/en-US/cloud-services/Subsystems/JDBC_Connector_help/Content/Connectors_JDBC/Introduction/JDBC-connector.htm)

   [ODBC databases](/en-US/cloud-services/Subsystems/ODBC_Connector_help/Content/Connectors_ODBC/Introduction/ODBC-connector.htm)

   [REST data sources](/en-US/cloud-services/Subsystems/REST_Connector_help/Content/Connectors_REST/REST-connector.htm)

   [Salesforce](/en-US/cloud-services/Subsystems/Salesforce_Connector_help/Content/Connectors_Salesforce/Introduction/Salesforce-connector.htm)

   [SAP NetWeaver](/en-US/cloud-services/Subsystems/SAP_Connectors_Help/Content/Connectors_SAP/SAP-SQL-connector.htm)
2. Create a new application or open an existing application.

   [*Creating applications and adding data*](../../Apps/create-app-cloud-hub.htm)
3. If you are loading data with Data manager, do the following:

   1. Optionally, edit and transform your data in the application.

      [*Loading and managing data with Data Manager*](../managing-data.htm)

      [*Editing a table*](../editing-table.htm)
   2. Associate your tables.

      Associating tables links tables by key fields.

      [*Managing data associations*](../associating-data.htm)
4. If you are loading data with Data load editor, do the following:

   1. Optionally, edit and transform the data you added with the data catalog.

      [*Using Data load editor*](../use-data-load-editor.htm)

      [*Understanding script syntax and data structures*](../understand-data-structures.htm)
   2. If your tables do not have key fields linking them together, change the field names to link them.

      Tables with identically named field will use those fields as key fields. You can view your associations with the data model viewer.

      [*Viewing and transforming the data model*](../../DataModeling/view-data-model.htm)
5. Optionally, if your loaded data includes geographic data, use GeoOperations to perform geographic calculations and functions.

   [*Qlik GeoOperations analytics sources*](../../../Global_Common/GeoOperationsFunctions/GeoOperations.htm)
6. Optionally, if you need to limit access to data in your application, add Section Access to your load script.

   Section Access is used to control the security of your applications. You add a security table to define which users can see what. Qlik Sense then uses that information to reduce data to the appropriate scope when each user opens the application.

   [*Managing data security with Section Access*](../../Scripting/Security/manage-security-with-section-access.htm)
7. Load your data and troubleshoot any issues.
8. Optionally, prepare your application's logical model for Insight Advisor.

   Insight Advisor uses a logical model to generate analyses. You can define your own logical model for the application rather than letting Insight Advisor make one from learned precedents.

   [*Building logical models for Insight Advisor with Business logic*](../../BusinessLogic/business-logic-logical-models.htm)
9. Optionally, add synonyms, custom analyses, or example questions for Insight Advisor.

   You can define synonyms for terms in your data for use with Insight Advisor. You can also define analyses that should be used when users search for specific things. You can define example questions to offer application users in Insight Advisor.

   [*Creating vocabularies for Insight Advisor*](../../BusinessLogic/business-logic-vocabulary.htm)

Your application is now ready for development.

## New manually-entered data

You can manually enter data in Data manager, This is useful if you have a data source where you may want to edit some value in Qlik Sense or if you have data in a table in a PDF or other source that Qlik Sense cannot import data from.

Adding manually-entered data

1. Create a new application or open an existing application.

   [*Creating applications and adding data*](../../Apps/create-app-cloud-hub.htm)
2. Open Data manager and add your data manually.

   [*Adding data manually*](../adding-data-manually.htm)
3. Prepare the data in your application.

   If you are loading data with Data manager, do the following:

   1. Optionally, edit and transform your data in the application.

      [*Loading and managing data with Data Manager*](../managing-data.htm)

      [*Editing a table*](../editing-table.htm)
   2. Associate your tables.

      Associating tables links tables by key fields.

      [*Managing data associations*](../associating-data.htm)
4. Optionally, if your loaded data includes geographic data, use GeoOperations to perform geographic calculations and functions.

   [*Qlik GeoOperations analytics sources*](../../../Global_Common/GeoOperationsFunctions/GeoOperations.htm)
5. Optionally, if you need to limit access to data in your application, add Section Access to your load script.

   Section Access is used to control the security of your applications. You add a security table to define which users can see what. Qlik Sense then uses that information to reduce data to the appropriate scope when each user opens the application.

   [*Managing data security with Section Access*](../../Scripting/Security/manage-security-with-section-access.htm)
6. Load your data and troubleshoot any issues.
7. Optionally, prepare your application's logical model for Insight Advisor.

   Insight Advisor uses a logical model to generate analyses. You can define your own logical model for the application rather than letting Insight Advisor make one from learned precedents.

   [*Building logical models for Insight Advisor with Business logic*](../../BusinessLogic/business-logic-logical-models.htm)
8. Optionally, add synonyms, custom analyses, or example questions for Insight Advisor.

   You can define synonyms for terms in your data for use with Insight Advisor. You can also define analyses that should be used when users search for specific things. You can define example questions to offer application users in Insight Advisor.

   [*Creating vocabularies for Insight Advisor*](../../BusinessLogic/business-logic-vocabulary.htm)

Your application is now ready for development.

## Preparing data for other applications

You can use scripts to load, transform, and export data for use in applications. Scripts are useful when you need to transform data, but do not want to create a full analytics application.

1. Create a script in the Create page of the Analytics [activity center](#glossary-9 "Glossary term").

   [*Creating scripts*](../../ScriptEditor/using-the-script-editor.htm#Creating)
2. Add data sources to the script. Do one of the following:

   - Add existing datasets using Data Catalog.

     [*Loading data from the data catalog*](../adding-data-catalog.htm).
   - Add new datasets in Script.

     [*Selecting data in load scripts*](../select-data-to-load.htm)
   - Create a connector for your data source.

     [*Adding and managing your analytics data*](../../Spaces/managing-data-resources-spaces.htm#Adding4)
   - Add data from an existing connection.

     [*Selecting data in load scripts*](../select-data-to-load.htm)
3. Edit and transform the data you added to the scripts.

   [*Editing load scripts*](../edit-data-load-script.htm)

   [*Understanding script syntax and data structures*](../understand-data-structures.htm)

   [*Script syntax overview*](../../Scripting/script-syntax.htm)
4. Optionally, if your loaded data includes geographic data, use GeoOperations to perform geographic calculations and functions.
5. [*Qlik GeoOperations analytics sources*](../../../Global_Common/GeoOperationsFunctions/GeoOperations.htm)
6. Optionally, preview the data and troubleshoot any issue.

   [*Previewing data in load scripts*](../../ScriptEditor/previewing-scripts.htm)
7. Load and export your data.

   [*Running load scripts to export data in scripts*](../../ScriptEditor/run-script-export-data.htm)
8. Refresh the data export for the script by reloading it. Reloads can be triggered manually or can run on a schedule.

   [*Running scripts*](../../ScriptEditor/reloading-scripts.htm)

   [*Refreshing analytics data*](../../Refresh/refresh-analytics-data.htm)
