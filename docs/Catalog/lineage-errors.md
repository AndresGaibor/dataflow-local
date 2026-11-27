---
title: "Troubleshooting - Lineage messages"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Catalog/lineage-errors.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Modeling your data", "Working with lineage and impact analysis in Analytics"]
---

# Troubleshooting - Lineage messages

You may encounter one or more of the following messages when working with [lineage](#glossary-0 "Glossary term") and [impact analysis](#glossary-1 "Glossary term") in Qlik Cloud. This table is intended to provide more context and guidance to help you understand and resolve common issues around lineage.

| Lineage message | Explanation |
| --- | --- |
| No lineage data available | This message means that the node is not found in lineage data. This can happen if an associated application has not been reloaded, an associated data task has not been prepared, or if a resource is missing dependencies. |
| Resource has been deleted or never existed. | The ID of the resource is wrong or it has been deleted. |
| Resource is not available because application has not been reloaded or lineage could not be found. | Possible causes:   - An application related to this lineage has not been reloaded since the lineage feature was introduced . - There was an error generating the lineage. - A data task related to this lineage has not been prepared since the lineage feature was introduced in Qlik Talend Data Integration.   Examples:   - An application that does not write any data. - A [dataset](#glossary-3 "Glossary term") that is not being read. |
| Internal error | There was an internal error involving services that provide lineage. |
| No impacted resources exist for the selected base node. | The base node does not have any output registered that would generate lineage. An examples of this is an application or data task that does not write any data, or it produces a dataset that is not being read. |
| No upstream lineage data available | The base node does not read any data and is therefore not dependent on any nodes. |
