---
title: "Visualizing range and distribution of numerical data with a box plot"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/BoxPlot/box-plot-example.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations", "Creating box plots"]
---

# Visualizing range and distribution of numerical data with a box plot

This example shows how to make a box plot to visualize range and distribution of numerical data using daily temperature measurements.

![Box plot visualization. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_gen_box_plot_example.png)

## Dataset

In this example, we'll use the following weather data.

- Location: Sweden > Gällivare Airport
- Date range: all data from 2010 to 2017
- Measurement: Average of the 24 hourly temperature observations in degrees Celsius

The [dataset](#glossary-0 "Glossary term") that is loaded contains a daily average temperature measurement from a weather station in the north of Sweden during the time period of 2010 to 2017.

## Measure

We use the average temperature measurement in the dataset as the [measure](#glossary-1 "Glossary term"), by creating a .measure in Master items with the name Temperature degrees Celsius, and the expression Avg([Average of the 24 hourly temperature observations in degrees Celsius]).

## Visualization

We add a box plot to the [sheet](#glossary-2 "Glossary term") and set the following data [properties:](#glossary-3 "Glossary term")

- Dimension: Date (date) and Year (year). The order is important; Date needs to be the first [dimension](#glossary-4 "Glossary term").
- Measure: Temperature degrees Celsius; the measure that was created as a master item.

In this example we use the default box plot preset, Standard (Tukey) with the whisker length 1.5 interquartile range.

![Box plot visualization. ](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_gen_box_plot_example.png)

## Discovery

The box plot visualizes the distribution of the daily temperature measurements. The [visualization](#glossary-5 "Glossary term") is sorted in mean temperature order. The mean temperature for each year is illustrated by the middle line in each box. The box stretches from the first quartile to the third quartile, and the whiskers stretch 1.5 inter-quartile ranges. There are also a number of outlier values, the points that are placed outside the whiskers. You can hover the mouse pointer over an outlier point and view the details.

In the box plot we can see that the year 2010 has the longest box and whiskers. That shows that the year 2010 has the largest distribution of temperatures measured. It also seems to be the coldest year in average.

The range of 2017 is small, as the dataset only contains measurements from the first months of the year.
