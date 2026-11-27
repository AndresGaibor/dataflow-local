---
title: "Org chart"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/org-chart.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Choosing the right visualization", "Visualizations"]
---

# Org chart

You can use the org chart (Org chart) to create organization [charts](#glossary-0 "Glossary term") from data with a tree structure. You can navigate through the hierarchy by expanding and collapsing the tree. The org chart is included in the Visualization bundle.

Information noteOrg chart is included as a part of the Visualization bundle. Visualization bundle objects have additional limitations and may not have the same support as other visualizations. For more information, see [*Visualization bundle*](visualization-bundle.htm).

You need to use a data set with two [dimensions](#glossary-1 "Glossary term") that define the tree structure.

- The first dimension needs to be the ID of the node. This would typically be an employee ID in a traditional organization chart.
- The second dimension needs to be the ID of the parent node. This would typically be the employee ID of a manager.

  This connects to the first dimension to create a tree structure.

  If this value is empty or points to a node that does not exist, the node becomes a root node at the top of the tree.

Example data set for an org chart

| EmployeeID | ManagerID | Name | Title |
| --- | --- | --- | --- |
| A101 |  | Mary Bell | CEO |
| A102 | A101 | John Bialik | Executive secretary |
| O101 | A101 | Lee Mayer | COO |
| I101 | A101 | Wendy Sanderson | CIO |
| T101 | A101 | Asim Nawrat | CTO |
| T102 | T101 | Emily Diaz | VP Products |
| T103 | T101 | Christine Nemic | VP R & D |

You can also add a [measure](#glossary-2 "Glossary term") that is used as a card description.

## Preparing the dataset

There are some things you need to consider when preparing the [dataset](#glossary-3 "Glossary term") for an org chart.

- You need to use a dataset with less than 33000 rows.

  If you use a larger dataset, the excess rows will be ignored. This can result in a tree with incorrect structure. A message is displayed: The maximum data limit is reached. The tree may display incorrectly.
- Make sure that the data does not contain circular references.

  Circular references can result in nodes being omitted, or creation of multiple root nodes. One of these messages is displayed:

  Data contains circular references, nodes are omitted.

  No root node, check your data for circular references.
- If a node has more than 99 children, the excess children nodes will not be rendered.

  A message is displayed: Maximum number of child nodes reached, nodes are omitted.
- You should avoid having a large number of rows that do not have a parent node. These will be shown as root nodes. The maximum number of root nodes is 99.

## Limitations

For information about general limitations, see [*Limitations*](visualization-bundle.htm#Limitati).

Related learning:

- [How do I configure a Visualization Bundle Org chart?](/lnk/How_configure_Visualization_Bundle_Org_chart)
