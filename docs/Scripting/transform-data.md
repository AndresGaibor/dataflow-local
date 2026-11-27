---
title: "Transforming data"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Scripting/transform-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting", "Tutorial - Next steps in scripting"]
---

# Transforming data

You can transform and manipulate data in the [Data load editor](#glossary-0 "Glossary term") before using the data in your application.

One of the advantages of data manipulation is that you can choose to load only a subset of the data from a file, such as a few chosen columns from a table, to make the data handling more efficient. You can also load the data more than once to split up the raw data into several new logical tables. It is also possible to load data from more than one source and merge it into one table in Qlik Sense.

The following exercises will show you how to load data using the Crosstable prefix. You will also learn how to join tables, use inter-record functions such as Peek and Previous, and load the same row several times using While Load.
