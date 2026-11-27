---
title: "Analyzing impact analysis in Analytics"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Catalog/impact-analysis2.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Modeling your data", "Working with lineage and impact analysis in Analytics"]
---

# Analyzing impact analysis in Analytics

Impact analysis shows the forward-looking, downstream view of dependencies for a database, resource, or [field](#glossary-0 "Glossary term"). It answers questions about which databases, applications, files, links, machine learning content, and other content would directly or indirectly be impacted if the value of a field changes. For many content types, you can also drill down to the particular fields that are impacted by the change.

Qlik Cloud provides an aggregated summary of downstream impact where you can interactively examine direct and indirect dependencies of a given field or object.

Downstream lineage is called impact analysis because it analyzes which objects will be impacted by changes to your data or analytics content; these objects are the dependents of the base node. Qlik Cloud provides information and counts by type of dependent objects in a summary view.

Business users examining a given field will have an aggregated summary of downstream impact that delivers insight into:

- Which object types would be impacted by a change to this field including databases, file storage, applications, and links
- Which Power BI reports and dashboards would be impacted
- Which Qlik NPrinting or Qlik Cloud reports would be impacted
- Which data models for Power BI and Tableau would be impacted
- What is the number of direct dependencies and indirect dependencies by type
- Who are the owners of the items that are impacted if you make a change
- Which machine learning workflows would be impacted

To view upstream lineage information such as inputs, transformations, and other historical information that can explain where your data came from and what operations have acted upon it, view its lineage. See [*Analyzing lineage in Analytics*](lineage.htm).

Information note

To use impact analysis, you also need View lineage set to Allowed through the default permissions or a custom security role.

## Impact analysis summary view

### The Impact analysis summary view

Open impact analysis from your activity center by selecting ![More icon](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on a supported item, and then selecting Tools > Impact analysis. For some content types, you can also open impact analysis when you have the item opened. Click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and Impact analysis.

You can access lineage (upstream) or impact analysis (downstream) for other nodes that appear in graphs by selecting ![More icon](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and then selecting Lineage or  Impact analysis (new base node).

In the summary view, you can filter on whether to display all or only direct dependencies. An example of a direct dependency is an application Application A that loads a particular dataset Datafile B. In this case, Application A directly depends upon Datafile B. An example of an indirect dependency is a [QVD](#glossary-1 "Glossary term") C.qvd  that is created by Application A, based on Datafile B. In this case, C.qvd is an indirect dependency of Datafile B.

Impact analysis summary view shows dependent fields in an application

![Impact analysis graph showing dependent fields in an app](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ImpactAnalysis_SummaryView.png "Click to view full size")

The base node being analyzed is outlined in blue. The dependents are listed in the left-hand overview with counts per type. When in focus and listed in the main grid, that type is outlined in a green box. Types of dependencies include databases, applications, file storage, databases, and links. The listed dependent objects for that type are listed in the main grid. Drill into these objects by selecting the row. For example, an application will drill down into table and then field-level.

To investigate impact of a field change, drill down from the base node object and select a field of interest to see dependencies for that field.

![Drill in to base node to view and select field to focus on that field](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ImpactAnalysis_BaseNodeDrilltoField2.png "Click to view full size")

Select ![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the row of the dependent object in focus to access a menu with the following actions:

- Details (see [*Node details*](#Node))
- Impact analysis (new base node)
- Lineage (for that object)
- Open

Actions that can be taken on dependent objects in impact analysis summary view

![Actions menu in depenedencies grid](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ImpactAnalysis_ActionsMenu.png "Click to view full size")

### Accessing impact analysis from a dataset

You can also access impact analysis from the overview of a dataset by switching to the Impact analysis tab.

## Impact analysis grid columns

Select columns of interest with the column-picker ![icon columns](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_columns.svg) in the top-right of the grid. Column options vary depending on the type of resource being viewed. The column options may include the following headings:

- Name
- Number of datasets | tables | fields
- Type
- Space
- Owner
- Last reload
- Last modified
- Open
- Number of models
- Number of configurations
- Number of versions
- ML Deployment

Impact analysis summary grid

![Impact analysis grid](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ImpactAnalysis_SummaryGrid.png "Click to view full size")

Information noteWhen Owner and Space columns have multiple values, a tool-tip appears listing the owners and spaces.

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

Impact analysis summary grid

![Details view from Impact analysis](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_ImpactAnalysis_Details1.png "Click to view full size")

## Impact analysis for machine learning content

With Impact analysis, you can identify downstream resources for your machine learning content. You can analyze ML experiments, ML deployments, and datasets in Impact analysis.

For example, you might want to identify which prediction datasets would be affected if you updated an apply dataset. You can also see how many learning resources appear as downstream dependencies for other content, such as analytics applications.

Machine learning assets are also shown in Lineage for comprehensive analysis of the origins of your predictive analytics content. For more information, see [*Analyzing lineage for machine learning content*](lineage.htm#MLLineage).

### Opening Impact analysis for machine learning content

Do one of the following:

- In your activity center, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to an ML experiment, ML deployment, or dataset, and select Tools > Impact analysis.
- In an ML experiment or ML deployment, click ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) in the navigation bar and select Impact analysis.

### Impact analysis and ML experiments

With an ML experiment set as the base node, it appears in the top left corner under Base node. Select the experiment ![ML experiment](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_experiment_green.svg) to drill down into experiment versions ![Fork](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_fork_outline.svg). A single experiment version ![Fork](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_fork_outline.svg) can then be selected for analysis as the base node. Finally, you can drill down within the version ![Fork](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_fork_outline.svg) to find a specific model ![ML model](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_ml_model_outline.svg) and set it as the base node.

Downstream dependencies for the experiment, or elements within it, include ML deployments, datasets, and analytics content such as applications, scripts, and data flows.

An ML experiment can also appear in the summary view when upstream content (for example, a dataset) is selected as the base node. When you have selected an experiment under Dependencies from basenode in the left panel, you can drill down within the experiment to show more information in the grid. An experiment ![ML experiment](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_experiment_green.svg) drills down into one or more versions ![Table](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table3.svg). An experiment version ![Table](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table3.svg) drills down into one or more models ![field](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_field.svg).

### Impact analysis and ML deployments

With an ML deployment set as the base node, it appears in the top left corner under Base node. Select the deployment ![ML deployment](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_proton_green.svg) to drill down into deployed models. A single model ![ML model](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_ml_model_outline.svg) can then be selected for analysis as the base node. Finally, you can drill down within the model to find a prediction output node. With the output node set as the base node, you can use the dependency grid to view a list of generated prediction datasets.

Downstream dependencies for the deployment, or elements within it, include datasets, and analytics content such as applications, scripts, and data flows.

An ML deployment can also appear in the impact analysis summary view when upstream content (for example, an ML experiment) is selected as the base node. When you have selected a deployment under Dependencies from basenode in the left panel, you can drill down within the deployment to show more information in the grid. A deployment ![ML deployment](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_proton_green.svg) drills down into one or more models ![Table](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table3.svg). A model ![Table](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table3.svg) drills down into one or more Configuration![field](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_field.svg) items, with each item representing a generated prediction dataset. These datasets can be analyzed individually by setting them as a base node.

### Impact analysis and ML datasets

ML datasets are datasets that are used in or created by ML experiments and ML deployments. They include:

- [Training datasets](#glossary-2 "Glossary term")
- Datasets exported from embedded analytics in an ML experiment (Compare and Analyze tabs)
- [Apply datasets](#glossary-3 "Glossary term")
- Prediction datasets

With an ML dataset set as the base node, it appears in the top left corner under Base node. Select the dataset to drill down into individual fields.

An ML dataset can also appear in the impact analysis summary view when upstream content (for example, an ML experiment or ML deployment) is selected as the base node. When you have selected a dataset in the grid, you can drill down within the dataset to show field-level information.

### Permissions

For information about permissions, see [*Permissions*](#Permissions).

### Example scenario

For an example scenario, see [*Example: Impact of changing a dataset used for predictions*](#ExampleML).

## Permissions

### Permissions for dependency analysis

Users without view permission will not be able to view dependent resource names, the Last reload column for dependent applications or the Last modified column for other resource types. Users without view [permissions](#glossary-4 "Glossary term") will also not be able to view the ![More icon](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) context menu or drill-in options for the resource.

### Permissions when an item is the base node

You must be able to view an item to open Impact analysis from your [activity center](#glossary-5 "Glossary term") , as well as to set the item as the base node in other ways. As stated in [*Permissions for dependency analysis*](#Dependency), dependent resources are shown with limited information if you do not have view access to the resources.

## Example use cases for analyzing impact analysis

### Example: Understanding the impact of making a change to a dataset

For a walk-through of a similar following example, see:

[Impact analysis use cases](https://share.vidyard.com/watch/U8aw1JHezbcCSEnkZVLhim)

As an application developer, you are responsible for a data source and are considering making a change to a dataset Sales data.xlsx by removing the field Price. The questions you have are: What will be impacted by making this change? What needs to be addressed? Who should I notify? You begin the investigation by selecting ![More icon](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the dataset tile and selecting Impact analysis.

Impact analysis summary view for the dataset Sales data.xlsx

![View downstream dependencies for apps and datasets with impact analysis summary view](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_ImpactAnalysis_Summary1.png "Click to view full size")

### Example: Impact of changing a dataset used for predictions

Suppose you are a machine learning contributor who has set up scheduled predictions from an ML deployment. You want to assess which workflows would be impacted if you change the calculation logic for a column in one of your [apply datasets](#glossary-6 "Glossary term").

Opening the apply dataset in Impact analysis, you can identify that the following content would be affected:

- An analytics application
- An ML deployment, within which there is one model that uses the apply dataset
- Several dataset outputs, which have been generated from the ML deployment on a scheduled basis

With this knowledge, you can make a more informed decision on whether to proceed with the update or create a new machine learning workflow.

Impact analysis for a machine learning apply dataset, analyzing the specific prediction datasets that would be impacted by changes to the apply dataset.

![View downstream dependencies for an apply dataset used for generating predictions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen-machine-learning-impact-analysis.png "Click to view full size")

## Deleted content

If an item is deleted, it may still be shown in the Impact analysis summary view when analyzing other nodes.

## Impact analysis in Data Integration

Impact analysis is also available in Data Integration. For more information, see [*Analyzing impact analysis in Data Integration*](impact-analysis-di.htm).
