---
title: "Visualizing variations from a reference point in a bar chart"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/Bar-Chart/bar-chart-example3.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations", "Creating bar charts"]
---

# Visualizing variations from a reference point in a bar chart

In this example, you will create a horizontal stacked bar chart to present results from a customer satisfaction survey. The goal is to visualize data as positive or negative variations from 0, the fixed reference point.

Completed bar chart displaying survey results

![Completed bar chart showing survey results for happiness scores by country](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_example-bar-chart-survey-results.png "Click to view full size")

## What you will do

In this example, you will use survey data in a bar chart to rank overall satisfaction by customer. The data shows the satisfaction levels of each customer with an organization's products and services. Data is organized by survey batch and outlines what percentage of each customer's representatives fall into each of the predefined satisfaction levels grouped by the survey:

- Always
- Most of the time
- Sometimes
- Rarely
- Never
- Unknown

In the data, the fixed reference point 0 is the most neutral satisfaction score. Positive and negative variations from this reference point indicate higher and lower customer satisfaction, respectively.

## Preparations

Create a new application and paste the [*Example load script*](#ExampleData) into a new section in the [Data load editor](#glossary-0 "Glossary term"). Then, load the data.

After loading the data, switch to sheet view.

### Example load script

Data for example

```
[Customer Satisfaction]:
CrossTable (Satisfaction_Level,Satisfaction_Value,2)
LOAD RowNo() as Batch_ID, * INLINE [
Customer,Always,Most of the time,Sometimes,Rarely,Never,Unknown
B,6.7,28.7,36.6,19.2,4.2,4.5
L,20.8,60.5,14.4,2.2,2.0,0
I,10.1,36.8,30.3,15.3,5.3,2.2
J,30.5,43.6,18.8,5.4,1.6,0.0
N,17.4,53.1,22.3,5.0,1.7,0.6
D,16.1,34.3,37.2,9.0,1.9,1.5
K,9.7,46.4,31.0,11.1,1.6,0.2
F,3.8,26.2,38.6,21.2,7.5,2.7
G,7.8,38.1,34.6,11.1,2.0,6.4
A,15.4,61.1,17.0,5.5,1.0,0.0
M,11.1,47.3,32.2,6.7,2.2,0.5
C,13.9,51.4,24.1,6.9,2.7,0.8
H,16.4,58.8,18.5,4.7,1.6,0.0
E,10.7,41.2,36.1,9.7,1.8,0.6
B,7.2,27.4,36.2,20.5,4.7,4.1
L,14.1,66.0,15.0,3.6,1.2,0
I,9.8,36.3,31.0,16.1,4.8,2.0
J,26.5,42.4,22.3,6.7,2.1,0.0
N,14.1,51.6,24.9,6.1,2.5,0.8
D,16.6,31.2,37.4,10.9,2.4,1.5
K,8.0,45.4,33.2,11.4,1.9,0.1
F,4.3,26.9,39.0,21.2,6.5,2.2
G,8.3,36.9,33.5,14.1,2.1,5.0
A,13.5,61.9,17.7,6.1,0.9,0.0
M,9.2,50.2,31.1,7.4,1.6,0.5
C,11.6,52.3,24.4,7.8,2.4,1.6
H,12.9,62.5,18.8,4.9,0.9,0.0
E,11.5,40.0,34.4,11.0,2.5,0.6
];

[Satisfaction Levels]:
load * inline [
Satisfaction_Level,Satisfaction_Score,Satisfaction_Order,Satisfaction_Sign
Always,5,3,1
Most of the time,4,2,1
Sometimes,3,1,-1
Rarely,2,1,-1
Never,1,2,-1
Unknown,0,3,-1
];
```

## Part 1: Create a master dimension

Before creating the bar chart, add a master dimension to set the specific colors needed in the chart. The colors can range from red to green as customer satisfaction scores increase.

Do the following:

1. Click ![Master items](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_link_outline.svg) Master items in the assets panel.
2. Click ![Create new](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) next to Dimensions to add a master dimension.
3. Select Satisfaction\_Level in the left side panel.
4. Under Name, enter Satisfaction Level.
5. Click Create.
6. Select the master dimension in the Dimensions list and click ![Edit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg). Click Continue.
7. In the dialog, switch to the Value colors tab.
8. In the list of field values, assign the following hex codes for each respective value:

   - Always: 276e27
   - Most of the time: 46c646
   - Never: f93f17
   - Rarely: f8981d
   - Sometimes: ffcf02
   - Unknown: b0afae

## Part 2: Configure chart data

Do the following:

1. Drag a bar chart onto the sheet.
2. Add Customer as the first dimension.
3. Add the Satisfaction Level master dimension as the second dimension.
4. Add the following measure:

   ```
   avg(Satisfaction_Value)*Satisfaction_Sign/100
   ```
5. For the measure you just added, enter Score as the Label.

## Part 3: Configure sorting

Sort the data in the chart to reflect the balance between survey results and the meanings of the satisfaction ranks. Additionally, use the Satisfaction\_Order field, which presents each of the satisfaction ranks in numeric order, to sort how the dimension values are stacked.

Do the following:

1. In the properties panel, expand Sorting.
2. Expand Customer.
3. Set Sorting to Custom, and check the Sort by expression checkbox.
4. Use the following Expression:

   ```
   avg(Satisfaction_Value*Satisfaction_Score)
   ```
5. Change the sorting to Descending.
6. Uncheck the Sort numerically and Sort alphabetically checkboxes.
7. Expand Satisfaction Level.
8. Set Sorting to Custom, and check the Sort by expression checkbox.
9. Use the following Expression:

   ```
   sum(Satisfaction_Order)
   ```
10. Uncheck the Sort numerically and Sort alphabetically checkboxes.
11. Expand Score.
12. Set Sorting to Custom.
13. Uncheck the Sort numerically and Sort alphabetically checkboxes.

## Part 4: Configure presentation

Now that the data and sorting have been defined, adjust the presentation of the chart.

Do the following:

1. In the properties panel, expand Appearance > General.
2. Add the Title Customer Satisfaction.
3. Expand Appearance > Presentation.
4. Switch from Grouped to Stacked presentation.
5. Switch from Vertical to Horizontal orientation.
6. Turn Value labels on.
7. Turn Segment labels on.
8. Turn Total labels on.
9. Click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.
10. Under General, set the Title font size to 22px.
11. Under Chart, set the following properties:

    - For Axis title, set the font size to 18px.
    - For Axis label, set the font size to 18px.
    - For Value labels, set the font size to 16px.
    - For Legend title, set the font size to 18px.
    - For Legend labels, set the font size to 16px.
12. Expand Appearance > Colors and legend.
13. Set Colors to Custom.
14. In the drop down menu, select By dimension and ensure the Satisfaction Level dimension is selected.

## Results

The completed bar chart should look like the following.

Completed bar chart displaying survey results

![Completed bar chart showing survey results for happiness scores by country](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_example-bar-chart-survey-results.png "Click to view full size")
