---
title: "Tutorial - Time series decomposition in Qlik Sense"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/ChartFunctions/RelationalFunctions/tutorial-time-series-decomposition.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Script syntax and chart functions", "Script and chart functions", "Relational functions"]
---

# Tutorial - Time series decomposition in Qlik Sense

This tutorial demonstrates using three chart functions to decompose a time series using the STL algorithm.

This tutorial uses time series data for the number of passengers using an airline per month to demonstrate the functionality of the STL algorithm. The STL\_Trend, STL\_Seasonal, and STL\_Residual chart functions will be used to create the visualizations. For more information about time series decomposition in Qlik Sense, see [*Time series decomposition functions*](relational-functions.htm#Time).

## Create an app

Start by creating a new app and importing the [dataset](#glossary-1 "Glossary term") into it.

Download this dataset:

[Tutorial - Time series decomposition](/en-US/cloud-services/tutorials/TimeSeriesDecompositionTutorial.zip)

This file contains data regarding an airline's number of passengers per month.

Do the following:

1. Go to the Create page of the Analytics [activity center](#glossary-2 "Glossary term") and select Dataset.
2. Click Upload data file.
3. Add Tutorial - Time series decomposition.csv using the dialog.
4. Select a space.
5. Click Upload and analyze. This creates a new app with the data in the selected space.

## Prepare and load the data

In order for Qlik Sense to interpret the YearMonth [field](#glossary-3 "Glossary term") correctly, you might need to use [Data manager](#glossary-4 "Glossary term") to recognize the field as a date field, not a field with string values. Typically this step is handled automatically, but in this case the dates are presented in the slightly uncommon YYYY-MM format.

1. In Data manager, select the table and click ![Edit table icon in Data manager.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) .
2. With the YearMonth field selected, click ![Edit table icon in Data manager.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_general_data_class.svg) and set the Field type to Date.
3. Under Input format, enter YYYY-MM.
4. Under Display format, enter YYYY-MM and click OK.

   The field should now show the calendar icon.
5. Click Load data.

Now you are ready to start using the STL functions to visually represent your data.

## Create the visualizations

Next, you will create two line [charts](#glossary-5 "Glossary term") to demonstrate the functionality of the STL\_Trend, STL\_Seasonal, and STL\_Residual chart functions.

Open a new [sheet](#glossary-6 "Glossary term") and give it a title. Toggle on the advanced options.

Add two line charts to the sheet. Resize and reposition the charts to match the following image.

Qlik Sense grid outline of blank app sheet

![Blank sheet in new app showing layout and grid size](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial_time-series-app-grid_cloud.png "Click to view full size")

### First line chart: Trend and seasonal components

Do the following:

1. Add the title Seasonal and Trend to the first line chart.
2. Add YearMonth as a [dimension](#glossary-7 "Glossary term") and label it Date.
3. Add the following [measure](#glossary-8 "Glossary term") and label it Passengers per month:

   =Sum(Passengers)
4. Under Data, expand the Passengers per month measure and click Add trend line.
5. Set the Type to Linear.

   You will compare this trend line to the smoothed output of the trend component.
6. Add the following measure to plot the trend component and label it Trend:

   =STL\_Trend(SUM(Passengers), 12)
7. Next, add the following measure to plot the seasonal component and label it Seasonal:

   =STL\_Seasonal(SUM(Passengers), 12)
8. Under Appearance > Presentation, set Scroll bar to None.
9. Keep the default colors, or change them to fit your preferences.

### Second line chart: Residual component

Next, configure the second line chart. This [visualization](#glossary-9 "Glossary term") will display the residual component of the time series.

Do the following:

1. Drag a line chart onto the sheet. Add the title Residual.
2. Add Date as a dimension.
3. Add the following measure and label it Residual:

   =STL\_Residual(SUM(Passengers), 12)
4. Under Appearance > Presentation, set Scroll bar to None.

Your sheet should now look like the one below.

Qlik Sense sheet for airline passenger analysis

![Sheet in an app showing separately processed trend, seasonal, and residual time series data.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-stl-time-series-sheet.png "Click to view full size")

## Interpreting and explaining the data

With the STL chart functions, we can gain a number of insights from our time series data.

### Trend component

The statistical information in the trend component is deseasonalized. This makes it easier to see general, non-repeating fluctuations over time. Compared to the straight, linear trend line for Passengers per month, the STL trend component does capture changing trends. It displays some clear deviations while still presenting the information in a readable fashion. The smoothing behaviors in the STL algorithm helped to capture this.

The drops in number of airline passengers that are visible in the STL trend graph can be explained as part of the economic impact of recessions that occurred during the 1950s.

### Seasonal component

The detrended seasonal component isolated recurring fluctuations throughout the time series, and removed general trend information from that part of the analysis. We started with a dataset consisting of year-month aggregations. With this data, it is implicit that we are segmenting the data into one-month granules. By defining a period value of 12, we set the chart to model seasonal patterns over the course of one-year (twelve-month) cycles.

In the data, there is a repeated seasonal pattern of surges in airline passengers in the summer months, followed by declines for the winter months. This is aligned with the idea that summer is typically a popular time to take vacations and travel. We also see that over the course of the time series, these seasonal cycles increase drastically in amplitude.

### Residual component

The chart for the residual component shows all the information that was not captured in the trend and seasonal decomposition. The residual component includes statistical noise, but it can also indicate an incorrect setting of the STL trend and seasonal function arguments. Generally, if there are periodic oscillations in the residual component of the signal, or the information displayed is clearly not random, it is usually a sign that there is information in the time series not currently captured in the seasonal or trend components. In this case, you need to revisit your definitions of each function argument and possibly change the periodicity.

### Smoother values

Since we did not specify any values for the trend and seasonal smoothers, the function will use the default values for these parameters. In Qlik Sense, the default smoother values in the STL algorithm produce effective results. As a result, in most cases, these arguments can be left out of the expressions.

Information noteSetting the seasonal or trend smoother arguments as 0 in either of the three STL functions makes the algorithim use default values, rather than values of 0.

The trend smoother value uses the dimension that is specified in the chart. Since the YearMonth field presents data by months, the trend smoother value will be the number of months. The seasonal smoother will reflect the periodicity defined. In this case, since we defined one period as lasting twelve months (one year), the seasonal smoother value is the number of years. This may sound confusing, but it really means that to find the seasonality, we need to look across a number of seasons. This number is the seasonal smoother.

### Other useful information

Given that the seasonal cycles increase in amplitude over time, a more advanced analytics approach could make use of logarithmic functions to create a multiplicative decomposition. In practice, a simple measure of relative amplitude can be created in Qlik Sense by dividing the seasonal by the trend component. When this is done, we notice that over time, the summer peaks of each cycle grow larger in relative amplitude. The amplitude of the winter low points, however, do not increase over time.
