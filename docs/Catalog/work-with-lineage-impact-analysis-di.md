---
title: "Working with lineage and impact analysis in Data Integration"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Catalog/work-with-lineage-impact-analysis-di.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing your pipeline project", "Creating and managing data pipeline projects"]
---

# Working with lineage and impact analysis in Data Integration

A complicated data web can result when diverse data sources intersect across multiple systems. This web can be difficult to untangle in order to understand what is happening. [Lineage](#glossary-0 "Glossary term") provides simple visual flows, and views into these pipelines. The role of data lineage is valuable to business and development operations, providing the ability to understand where data originates, how it is transformed, and how it moves into, across, and outside your organization.

Data consumers can visually see the flow of each data [field](#glossary-1 "Glossary term") from original data source to end-user applications for every [data asset](#glossary-2 "Glossary term") that's managed in Qlik Cloud. This provides you with a detailed understanding of where and how data fields are being sourced or created. Field-level lineage helps you trust and understand your data at a deeper level, to create efficiencies in the [data pipeline](#glossary-3 "Glossary term").

Qlik Cloud makes a clear distinction between Lineage and Impact analysis:

## [*Analyzing lineage in Data Integration*](lineage-di.htm)

Lineage represents the origin of a field or dataset, back through applications and transforms, to the original data source. Lineage answers questions such as: Where does this dataset come from? What is the ultimate source? How was it calculated?

## [*Analyzing impact analysis in Data Integration*](impact-analysis-di.htm)

Impact analysis shows a downstream view of a data element’s dependencies - which data tasks, datasets, or applications would directly or indirectly be impacted if the value or structure of that particular field was changed. Impact analysis answers questions such as: Where else is this used? How much is this utilized? What is the impact if I make a change to this?

You can access  Lineage and Impact analysis graphs and views from several entry points in the data pipeline:

- You can select a task in the Data pipeline view of a pipeline project and access lineage and impact analysis. This provides lineage and impact analysis for every dataset in the data task.
- You can select a dataset in the Design view of a data task, and access lineage and impact analysis for that dataset.
- You can select a column in a dataset and access field-level lineage and impact analysis for that column.

Information note

For Replication projects, the gateway version must be upgraded and tasks must be reprepared before the Lineage option is available.

Tip noteFor information on accessing lineage and impact analysis in Qlik Cloud Analytics, see [*Working with lineage and impact analysis in Analytics*](work-with-lineage-impact-analysis.htm#The).
