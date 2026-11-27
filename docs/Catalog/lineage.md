---
title: "Analyzing lineage in Analytics"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Catalog/lineage.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Modeling your data", "Working with lineage and impact analysis in Analytics"]
---

# Analyzing lineage in Analytics

Lineage tracks data and data transformations backwards to the original source. Qlik Cloud provides a detailed visual representation of the history of this flow, where you can interactively examine the upstream lineage of analytics content. Lineage is available for content such as applications, scripts, data flows, table recipes, ML experiments, ML deployments, and datasets.

Information noteTo view lineage for analytics content, the underlying data must be stored in Qlik Cloud as a cataloged source.

Business users examining a given field have a view of lineage for the field that summarizes its most important dependencies:

- Fields that are used to derive it
- Direct associations and dependencies, including owner and space
- Original source (the first known source)

To view downstream or forward-looking dependencies, you can investigate what elements would be affected by a change to the object by viewing Impact analysis. See [*Analyzing impact analysis in Analytics*](impact-analysis2.htm).

For a visual demo of how to use lineage, see:

[Using lineage](https://share.vidyard.com/watch/axY6FxdLTMEfDEuyq3VCi8)

Information note

To use lineage, you also need View lineage set to Allowed through the default permissions or a custom security role.

## The lineage graph

The  Lineage graph shows the flow of data through analytics content in an interactive, graphical chart. A resource, table, or field is called a node in a lineage graph. When a node is the base node being investigated, it is said to be in focus and displays as the last element in the graph. At the most granular level, field-level lineage graphs show the data sources and transformations that a node is sourced from or dependent on.

Lineage graphs are useful to:

- Data experts working with the data
- Business specialists building applications
- Advanced business users consuming applications
- Users who work with machine learning models

Each node represents a step in the lineage of the selected content. This lineage information is compiled whenever an analytics asset refreshes its data. If your application, script, data flow, or table recipe has not be refreshed recently, the lineage may be incomplete or inaccurate.

Lineage is available for supported content types from the tile or row as they appear in your [catalog](#glossary-0 "Glossary term"). You can analyze lineage for the following analytics content:

- Dataset: Datasets are data sources, such as data loaded from connectors or data files. Datasets can be tables in a database, data that is uploaded to data storage or data that is generated from an application, such as a qvd file. Datasets usually have a single table each but some, such as Excel files, can have multiple tables.

  Datasets that were published from Talend Studio are indicated with ![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/catalog_lineage_talend_studio.png). You can go to the Talend Management Console Job that was used to generate the dataset by clicking Open TMC Job in the dataset ... menu. For more information, see [Publishing datasets and lineage to Qlik Cloud](/talend/en-US/studio-user-guide/8.0-R2025-04/publishing-datasets-and-lineage-to-qlik-cloud).
- App: Application nodes represent Qlik Sense analytic applications that use the data sources in the lineage. Application nodes display the application name and location of the application as Qlik Sense.
- Script: Script nodes represent scripts created in the Script interface.
- Data flow: Data flows can be inspected for better understanding of the data sources that they use and transform.
- Table recipe: Table recipes can be inspected for better understanding of the data source that they use and transform.
- ML experiment: You can understand the lineage of a machine learning experiment, which consists of the data sources that have come together to produce the training data for machine learning models.
- ML deployment: You can understand the lineage of an ML deployment and how it is being used in predictions. Lineage for ML deployments typically consists of ML experiments, experiment versions, models, and datasets.

Typical input nodes include data sources that are used by the base node, or applications that produce datasets. Field-level lineage allows for detailed investigation into how fields have been calculated and their specific origin across transforms and applications.

The nodes available in a lineage graph are the inputs to your selected content. Select an item to designate it as the base node. Input nodes are nodes that are upstream from the base node.

Field-level lineage graph

![Field-level lineage graph](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_LineageGraph_FieldLevel.png "Click to view full size")

The nodes available in a lineage graph are the inputs to your selected base node, in other words the node in focus. The base node is the singular node for which you want to retrieve lineage; for example, it could be an application, data flow, ML experiment, dataset, file, table, or field.

It will be the right-most node on your screen and outlined in blue. It is the focus of your investigation and only inputs to that base node will be presented.

While you explore the lineage, you can interactively change the base node to another table, application, field, or other item on the screen to focus your investigation.

Lineage base node

![The node in focus also called the base node will be to the right of your screen](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_Lineage_Node.png "Click to view full size")

The lines connecting the nodes are edges. Edges represent the relationship of a node to another node. They represent relationships indicating associations such as a dataset that is used by an application. They can also represent data that is produced as a by-product of an application. The collection of nodes and edges together make the lineage graph.

Lineage edges represent relationships

![Edges represent relationships between objects](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_Lineage_Edges.png "Click to view full size")

Nodes collapse or expand to reveal hierarchy levels from coarse to finer granularity beginning with the higher-level dataset group or application down to the most granular level which is the field level.

In this image of a node, the following hierarchy levels are shown, from highest (coarsest) to lowest (most granular): Data asset (application), resource (dataset), table, and fields.

![A node with asset, resource, table, and field levels](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_LineageGraph_Levels.png "Click to view full size")

## Opening the lineage graph

Do the following:

1. Open the Insights or Analytics activity center.
2. Select Tools > Lineage in the context menu ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on an item that supports lineage.

You can also access the lineage graph of some content when you have an item opened. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and Lineage.

## Node details

Details are limited by your access to that object. Details can provide the following information:

- Name
- Description
- Tags
- Location
- Space
- Owner
- Creator
- Last modified

## Navigating the lineage graph

Click and drag the graph to navigate and center the lineage graph. You can also use the navigation buttons. Select Home ![Home](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_home.svg) to center the lineage graph on the base node. Click back and forward to move around in your selections.

Lineage graph navigation

![Navigation buttons for the lineage graph.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_impact-analysis-lineage-navigation.png "Click to view full size")

The Lineage graph shows the upstream dependencies for your analytics content, which is presented as the default node when you open the graph for it. You can access lineage (upstream) or impact analysis (downstream) for other nodes that appear in the graph by selecting ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and Lineage (new base node) or  Impact analysis. Select a node to designate it as the base node.

Expand ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down.svg)or collapse ![arrow up](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_up.svg) the nodes to expand or collapse groups of objects at the same level.

Menu option to analyze different nodes

![Menu option to analyze different nodes](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/UI_LineageNavigation_NodeOptions.png "Click to view full size")

## Lineage summary view in an application

The lineage summary view in an application can give business users a high-level overview of the upstream dependencies in the application. For more information, see [*The in-application lineage summary view*](../Visualizations/chart-lineage-consumer-view.htm).

## Analyzing lineage for machine learning content

You can use the Lineage graph to analyze the origins of machine learning content, including ML experiments, ML deployments, and datasets. Use the graph for a holistic view of how machine learning models were created, the data they were trained on, and what they are used for in production scenarios.

Experiments, deployments, and datasets also appear as nodes when analyzing other content in the Lineage graph, such as downstream applications.

Machine learning assets are also shown in Impact analysis for comprehensive analysis of downstream content. For more information, see [*Analyzing impact analysis in Analytics*](impact-analysis2.htm).

### Opening Lineage for machine learning content

Do one of the following:

- In your activity center, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to an ML experiment, ML deployment, or dataset, and select Tools > Lineage.
- In an ML experiment or ML deployment, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) in the navigation bar and select Lineage.

### Navigating Lineage for machine learning content

You explore machine learning nodes in the same ways as for other content. For interface overviews, see:

- [*The lineage graph*](#Graph)
- [*Navigating the lineage graph*](#Navigating)

### Recognizing machine learning items in the Lineage graph

The following table outlines common items related to machine learning that appear in the Lineage graph.

Common lineage items for machine learning

| Item | Icon(s) | Explanation |
| --- | --- | --- |
| File storage | Folder | Not unique to machine learning content. Shows the location where a dataset is stored (in most cases, in a space). Relevant for training dataset, exports from embedded analytics in an experiment, apply datasets used for predictions, and prediction output datasets. |
| Dataset | Many (for example, QVD file type for QVD) | Not unique to machine learning content. Used to represent training datasets, exports from embedded analytics in an experiment, apply datasets, and prediction output datasets. |
| ML experiment | ML experiment | An ML experiment in which models are trained. |
| ML experiment version | Fork | The version within the ML experiment, in which one or more models have been trained. |
| ML model | ML model | An ML model trained within an experiment version. Used to represent trained models in an ML experiment, and deployed models in an ML deployment. |
| ML deployment | ML deployment | An ML deployment that contains one or more deployed models. |
| No icon | - | Prediction output nodes within an ML deployment do not have icons. Fields included in a prediction output dataset also do not have icons. |

### Lineage and ML experiments

ML experiments are presented in grouped arrangements. They expand as follows:

- An ML experiment expands into one or more experiment versions.
- An experiment version expands into one or ML models.

When a model trained in an experiment is deployed into an ML deployment, it appears in the lineage graph when downstream content (for example, predictions or ML deployments) is selected as the base node.

### Lineage and ML deployments

ML deployments are presented in grouped arrangements. They expand as follows:

- An ML deployment expands into one or more deployed models.
- If a model in the deployment has been used in batch predictions, the model expands to show each batch prediction output.

Field-level lineage is available for apply datasets and prediction output datasets that relate to an ML deployment.

Deployed models used for predictions are connected back to the experiment in which they were trained.

### Example scenario

For an example scenario, see [*Example: Investigating lineage of machine learning content*](#ExampleML).

## Limitations

The lineage chart has the following limitations:

- Applications that have not been reloaded after the release of lineage in Qlik Cloud may not have full lineage information available for them until after they reload. Details for some nodes may be limited if they have not been loaded after lineage was turned on for your [tenant](#glossary-1 "Glossary term").
- Node details for datasets outside of your tenant, such as SQL Server or Google Drive [connections](#glossary-2 "Glossary term"), are limited to the type of dataset and name. REST connections only display that it is REST data.
- If an item is deleted, it may still be shown in Lineage when analyzing other nodes.

## Permissions

You must be able to view an item to view its lineage from your [activity centers](#glossary-3 "Glossary term").
If you can see the lineage graph for a base node, you are able to see basic details and metadata for the upstream lineage objects.

## Security

- A user can only change to a base node that they have access to; otherwise the context menu is not available.
- If a user has access to the base node, they will have access to see all upstream lineage.

## Example use cases for analyzing lineage

For a walk-through of lineage analysis, see [Field-level lineage use cases](https://share.vidyard.com/watch/17bg3fny5xLck5eF6XJEKP).

### Example: Exploring where information comes from with the lineage summary view

As an analytics consumer looking at a bar chart in an application cars-data4-app, you would like to know where the information comes from. You make sure that Show details and Show expressions are turned on for the chart under the Appearance > General section of [properties](#glossary-4 "Glossary term"), then select switch to sheet analysis mode. Right-click the chart, or use the ![icon more actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) menu, and select Show details to show the lineage consumer view. Click Show dependencies.

You see that the dimension Car\_ID is dependent on the field Car\_ID which is found in three listed CSV sources. Select the ![icon more actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) menu on the field entry and select Lineage - Car\_ID / Cars to open a lineage graph for the field Car\_ID in the application.

Select a source or field to view lineage for that object

![Select the menu and then the option to view lineage for a source in the consumer lineage summary view](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_ViewLineage_SummaryView.png "Click to view full size")

The lineage graph is viewed right-to-left and shows that field Car\_ID is in the table Cars that was loaded into the application cars-data4-app. Expand ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down.svg) the nodes as you trace the field history back to the original file that was uploaded to Qlik Cloud. You see that the first relay back shows that a CSV cars-data.csv containing the field Car\_ID was loaded to the application cars-data4-app. The next node back is an application cars-data3-app from which the cars-data.csv was generated. Going back one more relay and expanding the node, you see that the original source file was a CSV file cars-data3.csv and it contained the field ID.

By expanding the tables and viewing fields, you are able to identify the original source file, table, and field of the bar chart dimension Car\_id-ID.

Expand the nodes to trace history of a field back to the source file

![Start with the node in focus and trace lineage history back to the original source](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_View_LineageGraph.png "Click to view full size")

### Example: Investigating the origins of a dataset and how it was created

As an application developer, you are considering using an existing dataset current\_customers\_analytics.xlsx for your application. You investigate the origins of this dataset so that you can understand where the data comes from. From the dataset tile or the row, select Lineage from the ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) menu to open the lineage graph. From the lineage graph, you view metadata for the dataset by selecting the ![icon more actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) menu on the XLSX current\_customers\_analytics.xlsx and Open the overview.

Open dataset overview from the lineage graph

![Dataset overview can be opened from the lineage graph](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_OpenDatasetOverview_Lineage.png "Click to view full size")

View tags, classifications, and other technical metadata from the dataset overview tab

![Dataset overviews can be accessed from the lineage graph](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_ViewOverview_FromLineage.png "Click to view full size")

Data profile is available from the Profile tab

![Fields profile tab is accessible from the lineage graph](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_ViewFieldsProfile_FromLineage.png "Click to view full size")

Click the browser back arrow to return to the lineage graph to explore the lineage graph for the dataset. Expand ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_down.svg) the current\_customers\_analytics.xlsx node, and click Select all, to view available fields. Do the same for all nodes. Note that each field provides the option to make it the base node of focus by selecting  Lineage (new base node) or select Impact analysis to view forward lineage and dependent objects that will be impacted by changes to the dataset.

Expanded Lineage graph for the dataset. Each field within each node will have options to open the application or data, view impact analysis, or change the node in focus

![Viewing lineage for a dataset](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_ViewDataset_Lineage.png "Click to view full size")

Following the lineage backwards and expanding the nodes, you can see that this XLSX dataset is the output of the Prep Current Customers Sales - Analytics application. Going back another relay and expanding the File storage node, you see that the sales analysis application had a CSV file loaded to it: rgb\_customers.csv. Field-level analysis reveals that the Tags field in the original source file was re-named to rgb\_customers.Tags in the sales analysis application. The original CSV file can be opened to the overview to reveal valuable metadata such as the owner, creator, usage metrics, tags, classifications, field profile, and impact analysis.

### Example: Investigating lineage of machine learning content

A casual business user or machine learning expert could use the Lineage graph to inspect the origins of certain predicted values. With the base node set to the prediction dataset, this user can see:

- The training data, including its sources and transformations
- The experiment, experiment version, and model
- Where the model was deployed, and how it has been used

Lineage graph with all nodes expanded. The graph shows an end-to-end flow from training data preparation to a prediction dataset.

![Lineage graph showing an end-to-end flow from training data preparation to a prediction dataset](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen-machine-learning-lineage.png "Click to view full size")

The image above shows the following process:

1. A data flow ![Data flow](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_data_flow.svg) loads and transforms data from a CSV dataset ![CSV file type](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_filetype_CSV.svg) stored in a personal space ![Folder](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_folder_outline.svg). The output is stored into a Parquet dataset ![Parquet file type](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_filetype_parquet.svg) in the same space.
2. The Parquet dataset ![Parquet file type](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_filetype_parquet.svg) is used in version 1 ![Fork](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_fork_outline.svg) of an ML experiment ![ML experiment](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_experiment_green.svg). This experiment version trains an ML model ![ML model](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_ml_model_outline.svg).
3. The ML model ![ML model](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_ml_model_outline.svg) is deployed into an ML deployment ![ML deployment](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_proton_green.svg).
4. Using a CSV dataset ![Parquet file type](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_filetype_CSV.svg) in a personal space ![Folder](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_folder_outline.svg) as the apply dataset, the ML deployment ![ML deployment](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_proton_green.svg) generates a prediction dataset in Parquet format ![Parquet file type](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_filetype_parquet.svg).

## Lineage in Data Integration

The Lineage graph is also available in Data Integration. For more information, see [*Analyzing lineage in Data Integration*](lineage-di.htm).
