---
title: "Select and load data from a Qlik Predict connection"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/ac-qlik-automl-connector-load.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Analytics sources in Qlik Cloud Analytics", "Qlik Predict analytics source"]
---

# Select and load data from a Qlik Predict connection

Once you have created a [connection](#glossary-0 "Glossary term"), you can select data and load it into a Qlik Sense application or script. You load data in [Data load editor](#glossary-2 "Glossary term") or Script.

Before a connection can be used, the application requires at least a source data table with a unique identifier and input fields which will contain the content to send to the models for machine learning problems and tasks. Make a note of the Table and Field name, you will need these in the Select dialog next.

Do the following:

1. Open Data load editor or Script.
2. In the Data sources panel on the right-hand side of the page, navigate to the saved connection and click ![Select data](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_ok.svg). This opens the Select data wizard.
3. Enter a Resident Table to be sent to the machine learning endpoints.

   The Resident Table should be the name of the resident table with source data that you have loaded into your application. You will find the resident table name in the [Data model viewer](#glossary-3 "Glossary term").
4. The available return table will automatically appear under Tables.

   The name of the return table is the one that has been configured in the connection.

   - Select Dynamically Load All Fields if you wish to load all fields returned from the model into your application and if you have created the Qlik Predict connection with the configuration to Load all available fields.
   - Select the column names to be loaded into the application if the connection was created without Load all available fields.
5. A script is automatically generated based on the selections.

   Click Insert script.
6. The new script will be seen in the text editor but needs additional editing.

   Complete the script by specifying the fields in the order the endpoint expects them. All fields must be available in the resident table.
7. Reload the application.

   When a reload of an application occurs it will first expect to load the source data as a resident table and use this as input to the request made to Qlik Predict endpoints.

## Requirements for auto-engineered date features

When you load data using a Qlik Predict analytics connection, you are running predictions with a Qlik Predict deployed model.

There are specific requirements for date formatting when running predictions from a model trained on date feature columns. For these columns, the data you provide to the Qlik Predict analytics connection must meet the following requirements:

- Date and datetime values must be strings formatted in accordance with ISO 8601 standards. Examples:

  - 2020-01-14
  - 2020-01-14T00:00:00.000Z
- The parent date—the feature from which the date parts were derived—must be included in its entirety. For example, your model might only use a Year feature but you still need to provide the date in ISO 8601-compliant format.
- Data within each column needs to be of the same time zone.

The above requirements:

- Only apply for features trained with date feature engineering. If the feature type is manually changed to the categorical feature type, these requirements do not apply. If the feature type has been changed to categorical, provide the column, in the date format in which it was originally used for training, in the apply data.
- Do not apply to time series models.

For more information about working with date features in predictions, see [*Working with date features in predictions*](../AutoML/date-features-predictions.htm).
