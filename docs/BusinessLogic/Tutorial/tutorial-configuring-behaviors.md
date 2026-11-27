---
title: "Configuring your behaviors"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/BusinessLogic/Tutorial/tutorial-configuring-behaviors.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Managing your data", "Customizing logical models for Insight Advisor", "Tutorial – Customizing how Insight Advisor interprets data"]
---

# Configuring your behaviors

Now you will create a behavior. Behaviors enable you to set custom individual scope for how measure groups are used.

With behaviors, you can:

- Enforce required [selections](#glossary-0 "Glossary term") of values from a [field](#glossary-1 "Glossary term") with a measure group.
- Set which groups you prefer to be used with a measure group.
- Set which groups you do not want used with a measure group.
- Set a calendar period to be used by default with a measure group.

Behaviors are optional.

## Why configure behaviors?

Like packages, behaviors help you set the scope for how groups are used together. Behaviors enable you to set narrow scope for how individual measure groups are used with other groups.

For example, when we search for fields from the Sales group in Sheet [measure](#glossary-2 "Glossary term") results for Gross Profits are aggregated across all time. It would be more useful if you had a more recent period of time applied. You can create a behavior to use one of your calendar periods by default.

## Creating a default calendar period behavior

Do the following:

1. Click Create behaviors.
2. Under Applies to, select Sales.
3. Under Behavior type, select Default calendar period.
4. Under Calendar group, select Sales\_OrderDate.
5. Under Period, select Month comparison.
6. Click Create.

## Results

Go to Sheet in the app navigation menu and click ![Insight Advisor](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cognitive.svg). Search for what is the average sales by employee. The matching results now displays a bar chart that compares this month's sales for each employee to the sales from the same month last year. For [charts](#glossary-3 "Glossary term") that do not support comparisons, only the results for the current month are shown.

Insight Advisor analysis using the default calendar period

![An Insights chart displaying a bar chart that shows the average Sales by Employee name. A default calendar period has been applied, comparing 2021 sales for June to 2020 sales for this June.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial_behaviors-insights-search-saas.png "Click to view full size")

## Configure a behavior to use a default calendar period for Period over period analysis

You can also set a default calendar period behavior for a group that is applied to Period over period analysis. Period over period analysis type uses a line chart to compare a measure over the current period versus the previous period. It requires a default calendar period set for the group containing the measure in the [logical model](#glossary-4 "Glossary term").

First, create a Quarter over quarter calendar period.

Do the following:

1. Click Create calendar period.
2. Select Sales\_Order Date.
3. For Calendar period name, enter Quarter over quarter.
4. For Calendar period grain, select Quarter of year.
5. Select Use last sorted value.
6. Click Create.

Now in the Behaviors tab, set this calendar period as the default for the group Sales.

Do the following:

1. Click Create behavior.
2. Under Applies to, select Sales.
3. Under Behavior type, select Default calendar period.
4. Under Calendar group, select Sales\_OrderDate.
5. Under Period, select Quarter over quarter.
6. Click Create.

Navigate to Sheet and open Insight Advisor. Search for show me sales. The first chart that appears below the KPI is a Period over period analysis. Open this chart and navigate to the property Analysis period. Select it and note that the default calendar period Quarter over quarter was correctly selected to compare the most recent period to the previous period. In this tutorial those periods are 2026-Q3 (Period 1) and 2026-Q2 (Period 2). These selections can be changed by selecting different quarters from the drop-downs. A reference line indicates the current day in the current calendar period grain, which in this case is a quarter.

Period over period analysis applied to a Line chart

![Period over period analysis compares a measure over the current period versus the previous period. A line chart shows the comparison of the sum of sales for 2020 Q4 versus 2020 Q3.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/tutorial-calendar-period-over-period-analysis.png "Click to view full size")

You can change this default calendar period in Analysis period.
