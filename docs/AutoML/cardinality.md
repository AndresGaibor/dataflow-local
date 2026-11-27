---
title: "Cardinality"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/cardinality.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Understanding machine learning", "Getting your dataset ready for training"]
---

# Cardinality

The cardinality is the uniqueness of data values in a column. Columns with too many unique values or no unique values have little variance. A machine learning model can't identify any sort of pattern in that data.

A high cardinality means a high number of unique values. To prevent high cardinality, you can bin, or group, similar values. You can also create new feature columns, for example, home addresses could be turned into distances to or from a specific location.

A column with only one unique value (constant) is not useful in identifying patterns.

Related learning:

- [Introduction to Qlik Predict](/lnk/Introduction_Qlik_AutoML)
