---
title: "Visualizations in the application"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/visualizations-in-app.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Understanding applications", "Tutorial - Beginning with the Basics"]
---

# Visualizations in the application

Visualizations are [charts](#glossary-0 "Glossary term"), extensions, and other objects that visualize your data for exploration in a [sheet](#glossary-1 "Glossary term").

## Start exploring charts to find insights

Each chart type is designed to help you see relationships, patterns, and trends in different ways. As you navigate through the sheets in this tutorial, you'll notice how making selections in one chart updates all the other charts. This is how you explore and uncover insights in the data.

## What you'll learn in this section

By the end of this lesson, you should be able to:

- Identify common chart types and what they show
- Understand why different charts are used for different types of data
- Predict how selections in one chart affect other charts

## Measures and dimensions

A [visualization](#glossary-2 "Glossary term") consists of at least one [measure](#glossary-3 "Glossary term") or one [dimension](#glossary-4 "Glossary term"). In most cases a visualization has both, and sometimes more than one dimension or measure.

Dimensions determine how the data in a visualization is grouped. Dimension values often refer to time, place, or category.

Measures are the result of some sort of calculation, often aggregations, such as Sum, Count, or Avg (average).

When dimensions and measures are combined in a visualization, it is possible to see, for example, how many bikes were sold in a certain area during a certain period of time.

## Dashboard visualizations

Different visualizations serve different purposes. The point of a visualization in general is to communicate its data in a quick and meaningful way while remaining 100% accurate.

Dashboard sheet with different visualizations.

![Dashboard sheet](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_DashboardSheet_dt_604x402.png "Click to view full size")

### Filter panes

**Use this to:** Narrow down the data you want to see. In the Dashboard sheet, you'll see filter panes on the left that let you select a time period or region. When you make a selection in a filter pane, all the charts on the sheet update instantly to show only the data you selected.

In the sheet Dashboard, there are two filter panes to the left: the time filter pane without title and Region. They are both filter panes, although they do not look the same. Region contains only one dimension, and shows the dimension values in a list. The time filter pane contains four dimensions, and because the space is limited, the lists are all compressed to panes. The purpose of the filter panes is to filter out a limited data set, which you can analyze and explore.

### Pie chart

**Use this to:** See the relationship between individual values and the total. The Sales per Region pie chart shows what portion of total sales comes from each region. Try clicking on a sector—the other charts on the sheet will update to show data for just that region.

Pie charts show the relationship between values, as well as the relation of a single value to the total. Each sector represents a value, and as long as there are a limited number of values (less than 10), you get a good overview of the relative size of the sectors. The values are ordered by size.

### Bar chart

**Use this to:** Compare multiple values side by side and see which is largest or smallest. The Top 5 Customers bar chart shows which customers have the highest sales. Click on a bar to focus on just that customer, and watch how the other charts change.

Bar charts are useful when you want to compare multiple values. The bars give information about the relationship between different values. Bars can be grouped or stacked, and be displayed horizontally or vertically.

### Combo chart

**Use this to:** Show trends over time and compare measures that have different scales. The Sales Trend chart combines sales figures with profit margin percentages so you can see if sales and margins move together.

Combo charts are usually used for displaying trends with bars and lines in the same visualization. A combo chart is especially useful when you want to combine values that normally are hard to combine, because they have totally different scales. The solution in the combo chart is to have two axes for the measures. In Sales Trend, the combo chart combines sales figures (millions of dollars, on the left axis) with margin (percent, on the right axis).

### KPI

**Use this to:** Track important numbers at a glance. The Total Sales and Margin KPI shows key performance metrics. Notice how the numbers update instantly when you make selections in other charts.

In a KPI visualization, you can show one or two measure values with text labels. You can add conditional colors and symbols to the values.

### Gauge

**Use this to:** See how a single value compares against a scale or target. The Profit Margin gauge shows whether profit margin is in a good range (the colors help you interpret the value at a glance).

A gauge is used to display a single key measure value. In this case it is the profit margin. The colors reinforce the interpretation of the value.

### Line chart

**Use this to:** Spot trends over time and see patterns in how a value changes. The Quarterly Trend line chart displays how sales and other measures change quarter by quarter, making it easy to see whether a trend is going up or down.

Line charts are often used to show trends, and this chart uses two dimensions, year and quarter that displays the trends for each quarter of the years 2012-2014.

## Product Details visualizations

Do the following:

- In the top right corner, click ![Next](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_right.svg) to go to the sheet Product Details.

Product Details sheet with different visualizations.

![Product Details sheet](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ProductDetailsSheet_dt_604x385.png "Click to view full size")

### Treemap

The second sheet, Product Details, contains one new visualization type compared to the sheet Dashboard, and that is the treemap. Treemaps are ideal when you want to display hierarchical data in a limited space. In this treemap the hierarchy consists of the dimensions Product Group, Product Type, and Item Desc. You start at the top level (Product Group), and when you make and confirm [selections](#glossary-5 "Glossary term") in the treemap you drill down to the next level (Product Type) to analyze the more detailed data. The items in the treemap are colored by measure. The darker the color, the higher the measure value.

The screenshot was taken in an application with reduced sheet width. As a consequence, the bar chart does not display all values at the same time. Therefore, it has a mini chart below the bar chart, which shows a miniature of the full chart. The mini chart has a scroll bar that can be used for navigation.

## Customer Details visualizations

Do the following:

- In the top right corner, click ![Next](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_right.svg) to go to the sheet Customer Details.

Customer Details sheet with different visualizations.

![Customer Details sheet](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_CustomerDetailsSheet_dt_604x400.png "Click to view full size")

The Customer Details sheet has two new visualizations, a scatter plot, Customer Sales and Quantity, and a pivot table, Customer KPIs.

### Scatter plot

With a scatter plot you can find potential relationships between values, and identify values that deviate from a group. The size of the bubbles can be used to show differences in values. In this scatter plot the bubbles show the relationship between sales and quantity, and each bubble is a dimension value: the customer.

### Pivot table

The pivot table Customer KPIs shows key customer figures. You can rearrange how the data is displayed, and analyze data by multiple dimensions and measures at the same time to get different views of the data.

## Customer Location visualizations

Do the following:

- In the top right corner, click ![Next](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_right.svg) to go to the sheet Customer Location.

Customer Location sheet with different visualizations.

![Customer Location sheet](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_CustomerLocationSheet_dt-rev.png "Click to view full size")

### Map

The fourth sheet, Customer Location, contains three filter panes and one new visualization: a map. You can create maps in applications that display data in layers such as point layers and area layers. The map we are using in this tutorial contains a point layer. A point layer is created using point coordinates (latitude and longitude) or location names to mark places of interest, for example cities.

Maps can, for example, be used for plotting sales data per region or per location. The map in this tutorial is used to show customer locations. You can filter by Region, City, or Customer. You can also make selections directly in the map by clicking on a point. If you hold down Shift before you make a selection you can select several areas to analyze.
