---
title: "Building a data flow"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataFlow/Creating-data-flow.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "10/9/2026"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and preparing data with Data flow", "Working with data products"]
---
# Building a data flow

## Creating a data flow

Start by creating a new data flow.

1. From the launcher menu, select **Analytics > Create** or **Analytics > Prepare data**.
2. Click **Data flow**.

   The **Create a new data flow** dialog opens.
3. In the corresponding field, enter a **Name** for your data flow.
4. From the corresponding drop-down list, select in which **Space** you want to save the data flow.
5. Add a **Description** to document the purpose of the data flow.
6. Add some **Tags** to the data flow to make it easier to find.
7. Optionally select the **Open data flow** checkbox to directly view the data flow once it’s created.
8. Click **Create**.

Your empty data flow opens and you reach the **Overview** tab of the navigation header. The new data flow can also be found later in the **Analytics > Home** page of Qlik Cloud.

For more information on the information you can find in the overview of your data flow, see [*Navigating data flows*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataFlow/navigating-data-flows.htm).

To start designing your data flow, go to the **Editor** tab of the navigation header.

## Selecting a source

The first building block of your data flow is the source that contains the data you want to prepare. You can use any data from your catalog or from a connection.

### Adding data from a dataset

Datasets stored in your catalog can be based on files (.qvd, .xls, .csv, .parquet, .json, etc.) or tables from databases and data warehouses. See [File formats](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataSource/load-data-from-files.htm#anchor-1) for the list of supported formats.

Datasets created in Qlik Talend Data Integration as part of a data project can also be used to create data flows.

To select a dataset as source for your data flow:

1. From the **Sources** tab of the left panel, drag a **Datasets** source and drop it on the canvas.

   The **Data catalog** window opens, where you can browse for previously uploaded datasets, or click **Upload data file** to browse for files on your computer and upload them on the fly.

   > **Warning:** When uploading large files bigger than 300 MB, the process can take some time. Do not close the window, progress is displayed on a spinner that may look empty at the beginning.
2. Select the data you want to load.

   - To load all the data from a dataset or data product, select the checkbox corresponding to that row.
   - To load certain datasets from a data product, click the arrow next to the data product's name. Select the datasets you want to load.
   - To load certain tables or fields from a dataset, click **View fields** next to the dataset's name. Select the fields from the tables you want to load.
   - To upload files from your computer, click **Upload file** to browse for files on your computer and add them to the list of available datasets.
   > **Note:** You can filter the data by type (datasets or data products). Data products are available in some subscriptions only. For more information, see [*Working with data products*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/DataProducts/Data-products.htm).
3. Using the search and filters, select the checkbox in front of one or more datasets from your list and click **Next**.

   When selecting a dataset added from a connection in the catalog, and multiple connections match, you can use a drop down list to select the specific connection to use.

   ![Selecting a specific connection for a dataset.](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/connection_drop_down_2.png)
4. In the **Summary** tab, you can review the datasets you have selected, check the fields they contain, and exclude some if you want. Click **Load into data flow**.

   The source or sources are added to the canvas, with a warning saying you need to connect them to other nodes.

   ![A source just added to the canvas](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/add_source_data_flow.png)

Once a source is placed on the canvas, you can click it and access the **Properties** panel to edit the selected fields if needed, if the schema of the source has been updated for example.

#### Uploading and configuring a csv file

If you are using a csv file dataset as source, either previously uploaded to your catalog or directly uploaded during the process, and the data does not display properly in the preview, it could mean that the file is not properly formatted.

For example, this customer data that uses comma as separator displays in a single column.

![comma separated data that is wrongly displayed in a single column](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/dataflow_csv_parameters_2.png)

The file was either badly formatted, or the separator was not correctly detected during the upload. To troubleshoot this issue, you will need to go the dataset settings.

1. From the launcher menu, select **Analytics > Catalog**.
2. Open the dataset to fix.

   In the dataset overview, you can see a warning saying that there is a potential formatting error.
3. Click the link to the **File format settings** from the warning message or use the **More actions** menu on the top right of the overview.

   You can see that the delimiter was wrongfully set as **Semicolon**.

   ![csv file delimiter set as semicolon](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/dataflow_csv_parameters_4.png)
4. From the **Delimiter** dropdown list, select **Comma**.

   With the expected delimiter, the preview now correctly shows the different fields.

   ![File format settings menu for a csv file](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/dataflow_csv_parameters_3.png)
5. Click **Save**.
6. Back in your data flow, delete the outdated source if the canvas was not empty, and add it again. This time, the source will reflect the right dataset configuration.

### Adding data from a connection

Qlik Cloud and data flows support a variety of connections to data sources. See the [List of supported data sources](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Helpsites/Connectors_SaaS.htm#anchor-2) for more information.

The only connection types that are currently not supported are the following:

> **Note:** AI21 Labs (Amazon Bedrock), Advanced Analytics, Amazon Comprehend, Amazon SageMaker, Amazon Titan (Amazon Bedrock), Anthropic (Amazon Bedrock), Azure ML, Azure OpenAI, Cohere (Amazon Bedrock, DataRobot, Databricks MLflow, Google Ads, Google Calendar, Hugging Face, Meta (Amazon Bedrock), MeaningCloud, OData, OpenAI, Qlik Predict, Qlik Big Data Index (QBDI), Qlik GeoOperations, Qlik GeoOperations GeoJSON, Qlik GeoOperations Shapefile, Sentiment140, SMTP, Watson Natural Language Understanding, YouTube Analytics.

To select a connection as source for your data flow:

1. From the **Sources** tab of the left panel, drag a **Connections** source and drop it on the canvas.

   The **Select connection** window opens, where you can browse for previously created connections, or click **Create connection** to define a new one on the fly after authenticating.
2. Using the search and filters, select the checkbox in front of a connection from your list and click **Next**.
3. Depending on the connection, you will be able to browse files, enter a path to your data, or select tables from a database.
4. After selecting the source data, click **Save** or **Finish**.

   The source is added to the canvas, with a warning saying you need to connect it to another node.

   ![A connection type source just added to the canvas](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/add_source_connection_data_flow.png)

Once a source is placed on the canvas, you can click it and access the **Properties** panel to edit the selected fields if needed, if the schema of the source has been updated for example.

Additionally, when opening a data flow, sources are validated to ensure that the space, connection, and dataset or datafile are accessible. If a validation error is detected (for example, a missing connection or an unavailable space), the source displays an error indicator. To view details, select the source and check the **Properties** panel for the error message. After resolving the issue outside the data flow, such as adding a missing connection, updating permissions, or restoring a deleted resource, click **Retry** in the **Properties** panel to re-validate the source and clear the error.

## Adding processors

Processors are the building blocks that contain the different preparation functions available in a data flow. They receive the incoming data, and return the prepared data to the next step of the flow. Processors allow you to perform complex extract, improve and cleaning operations on diverse data with a live preview. See the full [*Data flow processors*](https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataFlow/List-of-data-flow-processors.htm) for more information on the available functions.

To connect a first processor to your data source:

1. You can either:

   - From the **Processors** tab of the left panel, drag the processor of your choice and drop it on the canvas next to your source.

     ![](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/add_processor_left_panel.png)

     You will need to manually connect the source and the processor. Create a link by clicking the dot on the right of the source node, holding, and dragging the link to the dot on the left of the processor node.

     ![Creating a link between a source and a processor](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/manually_connect_processors_data_flow.png)
   - Click the action menu of the source, select **Add processor**, and click the processor of your choice.

     ![](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/add_processor_menu.png)

     The processor is placed on the canvas and automatically connected to the source.
2. Click the processor to start configuring it in the right panel.

   The different functions available, and the parameters to configure, depend on each processor. See the individual processor documentation for more information.
3. Click **Save**.
4. Add and connect as many processors as needed to prepare your data.

   Activate the **Data preview** switch in the **Preview** panel to see the effects of a processor on a sample of your data. Click the cog icon to open the preview **Settings** and configure the sample size up to 10000 rows. You can also activate the **Script** switch to look at the Qlik Script equivalent of your data flow at this point.

## Selecting a target

To end the data flow, you need to connect the last processor to a target node. You can choose between two target types:

- **Data Files** for files stored in your catalog in Qlik Cloud.
- **Connections** to write in an external source added as connection in Qlik Cloud.

Both options allow you to export the prepared data as a .qvd, .parquet, .txt or .csv file.

To connect a target to the rest of the flow:

1. You can either:

   - From the **Targets** tab of the left panel, drag the target type of your choice, and drop it on the canvas next to the last processor.

     ![Adding a target via drag and drop](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/add_target_left_panel.png)

     Manually connect the last processor to the target in the same way you connected processors previously.
   - Click the action menu of the last processor, select **Add target**, and click the target of your choice.

     ![Adding a target via the action menu](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/add_target_menu.png)
2. Click the target to start configuring it in the right panel.

   > **Note:** In the case of **Data files**, you can write in a specific folder of the desired space. If you have created a folder called folder\_name in your personal space for example, use folder\_name/data\_flow\_output.qvd as file name for your target. The resulting file will be directly sent to your folder.
3. Click **Save**.

   With a minimum of one source, one target, and an optional processor, the data flow can now be run.

## Running the data flow

When all the nodes of your data flow are connected, configured, and marked as **OK**, a green check mark shows that the data flow is considered valid and can be run. At this point, it is possible to use the **Preview script** button on the top right of the canvas to look at the full script that will be generated behind the scene.

![A valid data flow ready to run](../../../../../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Dataflow/valid_data_flow.png)

1. Click **Run flow** to start processing the data.

   A notification opens to show the status of the run.
2. When the flow has successfully completed, the prepared data that has been output can be found at different places according to the target:

   - In your **Catalog** among your other assets, and in the **Outputs** section of the data flow **Overview** for data files
   - In the **Outputs** section of the data flow **Overview** for connection-based datasets.

     If the flow happens to fail, you can open the run log to help you identify what went wrong.

You can now use this prepared data as clean source to feed an Qlik Predict experiment, or in a visualization application.
