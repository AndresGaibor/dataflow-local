---
title: "Working with lineage and impact analysis in Analytics"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Catalog/work-with-lineage-impact-analysis.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Modeling your data"]
---

# Working with lineage and impact analysis in Analytics

A complicated data web can result when diverse data sources intersect across multiple systems. This web can be difficult to untangle in order to understand what is happening. [Lineage](#glossary-0 "Glossary term") provides complete audit trails, simple visual flows, and views into these pipelines. The role of data lineage is valuable to business operations, providing the ability to understand where data originates, how it is transformed, and how it moves into, across, and outside your organization.

Data consumers can visually see the flow of each data [field](#glossary-1 "Glossary term") from original data source to end-user applications for every [data asset](#glossary-2 "Glossary term") that's managed in Qlik Cloud. This provides you with a detailed understanding of where and how data fields are being sourced or created. Field-level lineage helps you trust and understand your data at a deeper level, to create efficiencies in the [data pipeline](#glossary-3 "Glossary term").

Qlik Cloud makes a clear distinction between Lineage and Impact analysis:

- Lineage represents the history of a field or dataset, back through applications and transforms, to the original data source. Lineage answers questions such as: Where does this dataset come from? What is the ultimate source? How was it calculated?

  See [*Analyzing lineage in Analytics*](lineage.htm).
- Impact analysis shows a downstream view of a data element’s dependencies - which databases, applications, files or links would directly or indirectly be impacted if the value or structure of that particular field was changed. Impact analysis answers questions such as: Where else is this used? How much is this utilized? What is the impact if I make a change to this?

  See [*Analyzing impact analysis in Analytics*](impact-analysis2.htm).

Access Lineage and Impact analysis graphs and views from several entry points in Qlik Sense, including dataset or application tiles, or directly from a Qlik Cloud chart. For more information on accessing lineage from a chart, see [*Lineage summary view in an application*](lineage.htm#The).
