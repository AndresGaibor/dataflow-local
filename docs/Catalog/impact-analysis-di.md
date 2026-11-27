---
title: "Analyzing impact analysis in Data Integration"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Catalog/impact-analysis-di.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects", "Working with lineage and impact analysis in Data Integration"]
---

# Analyzing impact analysis in Data Integration

Impact analysis shows the forward-looking, downstream view of data task, dataset, or [field](#glossary-0 "Glossary term") dependencies. It answers questions about which datasets, data tasks, applications, and other resources would directly or indirectly be impacted by changes. You can also drill down to the particular fields that are impacted by the change.

Qlik Cloud provides an aggregated summary of downstream impact where you can interactively examine direct and indirect dependencies of a given object.

Downstream lineage is called impact analysis because it analyzes which objects will be impacted by changes to your data or application; these objects are the dependents of the base node. Qlik Cloud provides information and counts by type of dependent objects in a summary view.

Impact analysis provides an aggregated summary of downstream impact that delivers insight into:

- Which object types would be impacted by a change to this field?
- What is the number of direct dependencies and indirect dependencies by type
- Who are the owners of the items that are impacted if you make a change

To view upstream lineage information such as inputs, transformations, and other historical information that can explain where your data came from and what operations have acted upon it, view its lineage. See [*Analyzing lineage in Data Integration*](lineage-di.htm)

If there is analytics content based on the data, you will also see it in the impact analysis. For more information, see [*Analyzing impact analysis in Analytics*](impact-analysis2.htm).

Information note

To use impact analysis, you also need View lineage set to Allowed through the default permissions or a custom security role.

## Impact analysis summary view

You can access impact analysis by selecting Impact analysis in the context menu ![More icon](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on:

- A data task in a pipeline project. These are labeled as Data asset in the summary view.
- A Dataset in a data task.
- A Field in a dataset.

In the summary view, you can filter on direct dependencies only by selecting Show only direct dependencies.

- An example of a direct dependency is a landing data task lineage1\_\_Landing1 that is consumed by a storage task lineage1\_Storage1. In this case, lineage1\_Storage1 directly depends upon lineage1\_\_Landing1.
- An example of an indirect dependency is when a transform data task lineage1\_Transform consumes the aforementioned lineage1\_Storage1, based on lineage1\_\_Landing1. In this case, lineage1\_Transform is an indirect dependency of lineage1\_\_Landing1.

Impact analysis summary view

![Impact analysis summary view showing dependent fields in an app](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_impact_analysis_di.png "Click to view full size")

The base node being analyzed is outlined in blue. The dependents are listed in the left-hand overview with counts per type. When in focus and listed in the main grid, that type is outlined in a green box. Types of dependencies include data tasks, datasets, fields, analytics applications, and machine learning content. The listed dependent objects for that type are listed in the main grid. Drill into these objects by selecting the row. For example, a data task will drill down into dataset and then field-level.

To investigate impact of a field change, drill down from the base node object and select a field of interest to see dependencies for that field.

![Drill in to base node to view and select field to focus on that field](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_impact_analysis_drill_di.png "Click to view full size")

### Operations

Select ![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) on the row of the dependent object in focus to access a menu with the following actions:

- Details (see [*Node details*](#Node))
- Impact analysis (new base node)
- Lineage (for that object)
- Open project to return to the pipeline project.
- Open data task to return to the data task.

### Impact analysis grid columns

Select columns of interest with the column-picker ![Columns icon](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_columns.svg) in the top-right of the grid. Column options vary depending on the type of resource being viewed. The column options may include the following headings: Name, Number of datasets | tables | fields, Type, Space, Owner, Last modified, Actions.

Information noteWhen Owner and Space columns have multiple values, a tool-tip appears listing the owners and spaces.

### Node details

Details are limited by your access to that object. Details can provide the following information:

- Name
- Description
- Project
- Data store
- Space
- Owner
- Creator
- Last modified

## Permissions

You must have permission to view tasks in the data space of the data project to view impact analysis. This means that you need to have either of the following roles:

- Is owner
- Can view
- Can operate
- Can edit
