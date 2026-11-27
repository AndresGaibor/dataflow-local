---
title: "Viewing the distribution of data over intervals with a histogram"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Histogram/histogram-example.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations", "Creating histograms"]
---

# Viewing the distribution of data over intervals with a histogram

This example shows how to make a histogram to the distribution of data over intervals, using weather data.

![Histogram with the dimension Average of the 24 hourly temperature observations in degrees Celsius.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_gen_histogram_example.png)

## Dataset

In this example, we'll use the following weather data.

- Location: Sweden > Gällivare Airport
- Date range: all data from 2010 to 2017
- Measurement: Average of the 24 hourly temperature observations in degrees Celsius

The [dataset](#glossary-0 "Glossary term") that is loaded contains a daily average temperature measurement from a weather station in the north of Sweden during the time period of 2010 to 2017.

## Visualization

We add a histogram to the [sheet](#glossary-1 "Glossary term") and add the [field](#glossary-2 "Glossary term") Average of the 24 hourly temperature observations in degrees Celsius as [dimension](#glossary-3 "Glossary term").

The [visualization](#glossary-4 "Glossary term") creates a frequency [measure](#glossary-5 "Glossary term") automatically, and sorts the temperature measurements into a number of bars according to frequency distribution.

We can adjust the size of the bars to get even intervals by setting Bars to Custom and Bar width (x-axis) with a width of 5.
This adjusts the bars to be intervals of 5 degrees Celsius as shown below:

![Histogram with the dimension Average of the 24 hourly temperature observations in degrees Celsius.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ex_gen_histogram_example.png)

## Discovery

The histogram visualizes the frequency distribution of the temperature measurements. You can hover the mouse over a bar to see more details of the frequency.

We can see that most days, the temperature is between -5 and 15 degrees Celsius. There are days below -30, but they are not many.
