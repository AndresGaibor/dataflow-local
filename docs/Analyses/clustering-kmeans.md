---
title: "Clustering (k-means) analysis"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Analyses/clustering-kmeans.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing analyses"]
---

# Clustering (k-means) analysis

Show clusters of measures associated with a dimension using a statistical algorithm.

Clustering (k-means) clusters data points aggregated by similarities from two measures over a dimension using a machine learning k-means algorithm.

Clustering (k-means) analysis

![Clustering (Kmeans) analysis showing City clustered by the average cost of sale and average gross profit.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_analysis-clustering-kmeans.png "Click to view full size")

## Creating clustering (k-means) analysis

Do the following:

1. In Assets, click Analysis.
2. Drag and drop Clustering (k-means) into the sheet.
3. Click Add dimension and select a dimension.
4. Click Add measure and select a measure.
5. Click Add measure and select a second measure.
6. Optimally, to customize the clusters, do the following:

   1. In the properties panel, in Analysis properties, change Clusters from Auto to Custom.
   2. After Number of clusters, adjust the slider to set the clusters.
   3. After Normalization algorithm, select the algorithm to use. The following are available:

      - zscore: Z-score normalization normalizes data based on feature mean and standard deviation. Z-score does not ensure each feature has the same scale but it is a better approach than min-max when dealing with outliers.
      - minmax: Min-max normalization ensures that the features have the same scale by taking the minimum and maximum values of each and recalculating each datapoint.
      - none: No normalization.
7. Optionally, to add an analysis period, do the following:

   1. In the properties panel, under Analysis properties, turn on Analysis period.
   2. Under Calendar period, select the calendar period to use.
   3. Under Period, select a specific period to use.

   Information noteAnalysis periods requires calendar periods in the logical model. For more information, see [*Defining analysis periods with calendar periods in Insight Advisor*](../BusinessLogic/business-logic-calendar.htm).
8. Optionally, in the properties panel, under Appearance, adjust the appearance of the analysis.
