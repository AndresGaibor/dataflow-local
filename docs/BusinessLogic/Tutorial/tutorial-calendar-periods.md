---
title: "Configuring your calendar periods"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/BusinessLogic/Tutorial/tutorial-calendar-periods.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Managing your data", "Customizing logical models for Insight Advisor", "Tutorial – Customizing how Insight Advisor interprets data"]
---

# Configuring your calendar periods

Calendar periods use your calendar groups to create default periods of time for analysis in Insight Advisor.

Calendar periods are used to define time periods for analysis in Insight Advisor analysis. You create calendar periods from your calendar groups. Depending on your data, [business logic](#glossary-0 "Glossary term") may automatically create calender periods from your data model. If you navigate to Calendar periods, you can see calendar periods have already been made. Calendar periods can be relative, covering a period relative to the current date. For example, you could create a relative period to cover the current month. Calendar periods can also use the last recorded value in your data. For example, the three calendar periods created when you activated business logic all use last recorded values to make calendar periods for the last year, month, and quarter. app users can apply the calendar periods to Insight Advisor analysis in Sheets.

You can also define default calendar periods for groups in behaviors. This ensures that by default, Insight Advisor uses that calendar period when creating any [charts](#glossary-2 "Glossary term") for fields in that group.

## Why define calendar periods?

Calendar periods are useful because they create specific periods of analysis for your data. If Insight Advisor is not given a specified time frame, such as in 2020 or for December, it will use the entirety of the data available. If you provide calendar periods, app users can more easily view and compare data for specific periods.

For example, you want to view sales by product. Navigate to Sheet, and search for show me sales by product.
If you want to view specific periods of sales, such as a data for this month compared to last month or a comparison of the current quarter to a previous quarter, you would need to enter a new query. By making calendar periods, you can view these periods for your query without making new queries. Business logic has already made last recorded value calendar periods for the last month, quarter, and year in the data. It does not have relative periods, however. You could create a comparison for the current month to the same month last yea. You could also make a comparison between the current quarter (x) and the quarter two quarters ago (x-2).

## Creating the Month comparison calendar period

This calendar period will display results for the most recent month in the data and compare it to the same month last year.

Do the following:

1. Click Create calendar period.
2. Under Calendar group, select Sales\_Order Date.
3. For Calendar period name, enter Month comparison.
4. For Calendar period grain, select Month of year.
5. Under Period comparison, select Year over year.
6. Select Last complete period.
7. Click Create.

## Creating the Quarter comparison calendar period

This calendar period will display results for the current quarter (x) and compares it to the quarter two quarters ago (x-2).

Do the following:

1. Click Create calendar period.
2. Select Sales\_Order Date.
3. For Calendar period name, enter Quarter comparison.
4. For Calendar period grain, select Quarter of year.
5. Click Custom.
6. For Offset, select 0.
7. For Compare offset, select 2.
8. Click Create.

## Results

Go to Sheet in the app navigation menu and click ![Insight Advisor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cognitive.svg). Search for show me sales by product.
Select the matching result. In Analysis properties, there is a new property available, Analysis period. Select it and select Month comparison to apply the period to the chart.

Month comparison calendar period applied to a chart

![Insights chart with Month comparison calendar period applied. A bar chart is displayed showing the sum of Sales by Product name. Products have two sum of Sales bars, one for the current month and one for the same month last year](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial_calendar-period-month-saas.png "Click to view full size")

Next, apply the Quarter comparison calendar period.

Quarter comparison calendar period applied to a chart

![Insights chart with Quarter comparison calendar period applied. A bar chart is displayed showing the sum of Sales by Product name. Products have two sum of Sales bars, one for the current quarter and one for the quarter two quarters previous](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial_calendar-period-quarter-saas.png "Click to view full size")

You can also adjust the time periods in an analysis period manually for individual charts in Insight Advisor by changing the values in Period 1 and Period 2. For example, under Period 1, change the value to the same quarter last year. The chart updates for the newly defined period.

Quarter comparison calendar period applied to a chart, now using 2025-Q3 and 2026-Q3

![Insights chart with Quarter comparison calendar period applied. The period has been manually changed to display 2021 Q2 and 2019 Q2. A bar chart is displayed showing the sum of Sales by Product name. Products have two sum of Sales bars, one for the current quarter and one for same quarter two years ago.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial_calendar-period-quarter-custom-saas.png "Click to view full size")

Additional analysis types are available in Insight Advisor when calendar periods are available: period changes, period changes (detailed), and period over period.
These provide a suite of charts for analyzing the period and its changes.

Click Explore analyses under Analysis period. There are two analyses to select from. First, choose Period changes and click Open analysis. Period changes shows a KPI and bar chart for the changes of the sum(Sales) delta between the two periods. When there is a small number of [dimensions](#glossary-3 "Glossary term"), a variance waterfall chart is displayed instead of a bar chart.

Period changes analysis

![A screenshot of the period changes analysis. A KPI shows the change in the sum(Sales) detla between 2020 December and 2020 November. A bar chart shows the changes for each product between 2020 November and 2020 December. A scatter plot shows the sum of sales changes by product name by overall contribution and amount between 2020 November and 2020 December.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial_calendar-period-period-analysis-saas.png "Click to view full size")

Click Close and scroll back to the bar chart. Click Explore analyses and now select Period analysis (detailed). This provides the period performance against a target. It displays four charts that [measure](#glossary-4 "Glossary term") if targets were met for this period. You can adjust the parameters to define what met, what almost met, and what did not meet the target in Analysis properties.

Period performance against target analysis

![Period performance against target analysis for the sum of Sales by product name. Four charts are displayed. A gauge shows how the target was met overall. A pie chart shows the percentage that met or missed the target. A table shows product name by product name the sales results and if they met or missed the target. A bar shart shows the change the sum of sales by productname for 2020 November and 2020 December.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial_calendar-period-detailed-period-analysis-saas.png "Click to view full size")

Under Parameters, adjust the limit for missing the target to 100 and the limit for meeting the target to 105. The detailed period analysis updates for the new targets.

Updated period performance against target analysis

![The updated performance against target analysis, showing the tables updated for the threshold of missing a target being 100 and the theshold of meeting a target being 105.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial_calendar-detailed-period-analysis-updated-saas.png "Click to view full size")

As you can see, calendar periods enable app users to quickly view different periods of interest in Insight Advisor.
