---
title: "The fifth and sixth sheets: Insights sheet and Manager dashboard"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Sheets/fifth-sheet-insight-advisor.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Tutorial - Build an analytics application"]
---

# The fifth and sixth sheets: Insights sheet and Manager dashboard

These sheets focus on alternative ways of creating visualizations with the assistance of Insight Advisor. You will auto-generate three visualizations and a new sheet by asking Insight Advisor questions.

Insight Advisor helps you quickly generate new [charts](#glossary-0 "Glossary term") or find existing charts in an application. If you are an analyst, you can extend analysis in an application to charts not currently present in an application. If you are an application creator, Insight Advisor helps you quickly build new charts and [visualizations](#glossary-2 "Glossary term") based on your specifications.

Insights sheet

![Insights sheet](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_InsightsSheet_Cloud.png "Click to view full size")

Insight Advisor can also create whole [sheets](#glossary-3 "Glossary term") containing multiple visualizations.

Manager dashboard sheet

![Manager dashboard sheet](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_ManagerDashboardSheet_Cloud-rev.png "Click to view full size")

## Creating a bar chart from a search

In the sheet, there is a search field labeled Ask Insight Advisor. You can enter a question here and Insight Advisor Search looks at your data and generates charts that can answer your question.

Tip noteNatural language searches work best when you use [field](#glossary-4 "Glossary term") and [master item](#glossary-5 "Glossary term") names.

Information note

Qlik Cloud supports several languages in Insight Advisor Search. For more information on supported languages in Insight Advisor Search, see [Supported languages](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Insights/insight-advisor-create-visualizations.htm#anchor-8).

If your browser is not set to a supported language, English is used. You can change the language used by Insight Advisor by selecting a language from the Language button.

Do the following:

1. In the Ask Insight Advisor search box, enter Who are the top five Managers for Sales and click ![Submit question](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_right_2.svg).
2. On the generated bar chart, click Add to sheet and select Insights.
3. Click ![Insight Advisor](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cognitive.svg) to return to the sheet.
4. Navigate to the Insights sheet and click Edit sheet.
5. Select the bar chart.
6. At the top of the visualization, add the title Top 5 Managers for Sales.
7. Click Edit sheet to stop editing.

## Creating a Multi KPI from a search

You can alter properties from generated insights to change the chart type. In this case, we will make a multi-kpi chart that shows the bottom 3 product groups for sales for the latest month compared to the previous month.

Do the following:

1. In the Ask Insight Advisor search box, enter what are the lowest 3 product groups for sales and click ![Submit question](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_arrow_right_2.svg).
2. Select the bar chart.
3. In the Analysis properties panel, under Analysis period, select YearMonth-last sorted value.
4. Click Bar chart (grouped) and select the multi KPI chart.
5. Click Add to sheet and select Insights.
6. Click ![Insight Advisor](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cognitive.svg) to return to the sheet.
7. Click Edit sheet.
8. Select the multi KPI chart.
9. In the properties panel, select the measure Sales 2026-Jun.
10. Under Number formatting, select Money.
11. Select the measure Sales 2026-May.
12. Under Number formatting, select Money.
13. Under Appearance > General, add the title Bottom 3 product groups for sales.
14. Click Edit sheet to stop editing.

## Creating charts from analysis types

With Insight Advisor Analysis Types, you select the type of analysis and the fields to use. Insight Advisor then generates charts that provide that analysis. Analysis types range from standard analyses, such as breakdowns or trends over time, to more advanced analyses, such as calculating mutual information between datasets or k-means clustering. This helps you quickly generate visualizations, narrative interpretations, and whole dashboards.

Do the following:

1. Click ![Insight Advisor](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cognitive.svg).
2. Click Create an analysis.
3. Select Clustering (k-means).
4. Select Sales and change the aggregation to avg.
5. Select Cost and change the aggregation to avg.
6. Select Customer.
7. On the generated scatter plot, click Add to sheet and select Insights.
8. Click ![Insight Advisor](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cognitive.svg) to return to the sheet.

Feel free to move and resize the visualizations to match the screen shot above.

## Create a sheet from analysis types

Some Insight Advisor analysis types, labeled as smart sheets, generate whole sheets of visualizations. Smart sheets help you quickly build dashboards for analysis. Some smart sheets require that time periods be defined in your application's load script, logical model, or autocalendar. For more information on getting started with smart sheets, see [*Using smart sheets in Insight Advisor for period-based analyses*](../Insights/insight-advisor-smart-sheets.htm).

To learn more about how application logical models impact Insight Advisor, see [*Tutorial – Customizing how Insight Advisor interprets data*](../BusinessLogic/Tutorial/tutorial-customizing-insight-advisor.htm).

Do the following:

1. Click ![Insight Advisor](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cognitive.svg).
2. Click Create an analysis.
3. Select Period changes (detailed).
4. Add GrossSales as the measure.
5. Add Manager as the dimension.
6. Add Date as the period base.
7. Click Open analysis.
8. In the analysis properties panel, under Parameters, change the almost limit to 100 and the met limit to 105.
9. Click Add to new sheet.
10. Click Insight Advisor.
11. Click Sheets and select My new sheet.
12. Click ![Insight Advisor](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cognitive.svg) to return to the sheet.
13. Navigate to your new sheet.
14. Click Edit sheet.
15. Rename the sheet to: Manager dashboard.
16. Click Edit sheet to stop editing.

These sheets are complete. Next, you will learn about filters. In the assets panel, click Sheets and click Create new sheet. Name the new sheet Filters and open it.
