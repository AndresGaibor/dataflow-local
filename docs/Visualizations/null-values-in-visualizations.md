---
title: "Null values in visualizations"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/null-values-in-visualizations.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations"]
---

# Null values in visualizations

Data is sometimes missing or cannot be calculated, because the fields contain values that are null or not a number (NaN). In the [visualizations](#glossary-0 "Glossary term") null and NaN values are displayed in different ways, according to the following table.

How Null and NaN values are displayed

| Visualization type | Null values in dimensions | NaN values in measures |
| --- | --- | --- |
| Bar chart | – | – ( when labels are enabled in the [properties](#glossary-1 "Glossary term") panel, otherwise empty) |
| Box plot | – | No representation |
| Combo chart | – | A combination of the NaN value for the bar and the line. |
| Distribution plot | – | No representation |
| Filter pane | No representation | N/A |
| Gauge | N/A | – |
| Histogram | – | No representation |
| KPI | N/A | – |
| Line chart | – | Empty |
| Map | No representation | Gray |
| Pie chart | – | Empty |
| Scatter plot | – | Empty |
| Table | – | – |
| Text & image | N/A | – |
| Treemap | – | Empty |
