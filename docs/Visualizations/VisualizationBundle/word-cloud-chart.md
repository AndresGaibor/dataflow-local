---
title: "Word cloud chart"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/word-cloud-chart.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Choosing the right visualization", "Legacy"]
---

# Word cloud chart

The Word cloud chart (Word cloud) lets you visualize text data. Text values are displayed with their size based on a [measure](#glossary-0 "Glossary term") value. The measure can be anything you want to measure against, for example: times used, alphabetically, by importance, or by context. You can customize your chart with different shapes, fonts, layouts, and color schemes.

Information noteWord cloud is included as a part of the Visualization bundle. Visualization bundle objects have additional limitations and may not have the same support as other visualizations. For more information, see [*Visualization bundle*](visualization-bundle.htm).

A word cloud chart displaying food items in different sizes and colors.

![A word cloud chart displaying food items in different sizes and colours.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/w3_629x440.png "Click to view full size")

## Requirements

Word cloud [charts](#glossary-1 "Glossary term") must have one [dimension](#glossary-2 "Glossary term") and one measure.

## When to use the word cloud chart

A word cloud chart lets you visualize and identify the importance of a value against a measure. The more important the value is against the measure, the larger it displays in the cloud.

## Limitations

For information about general limitations, see [*Limitations*](visualization-bundle.htm#Limitati).

- The word cloud chart can handle maximum of 100 words per entry.
- Words that take up more space than the chart are not displayed. You can adjust the font size to show more values, but we do not recommend that you use fields with long text values.
- Word cloud charts cannot be used in Qlik NPrinting reports.

Related learning:

- [How do I configure a Visualization Bundle Word cloud chart?](/lnk/How_configure_Visualization_Bundle_Word_cloud_chart)
