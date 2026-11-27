---
title: "Visualizing the sales forecasts"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/AutoML/time-series-tutorial-visualize.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Machine learning with Qlik Predict", "Tutorial – Predicting sales with multivariate time series forecasting"]
---

# Visualizing the sales forecasts

Now that predictions have been generated, create a simple analytics application to view and analyze the sales forecasts.

Do the following:

1. Go to the Create page of the Analytics [activity center](#glossary-0 "Glossary term") and select Analytics app.
2. Enter a name for your application, for example, Sales forecasting.
3. Choose a space for your application.
4. Click Create.
5. Under Get started adding data to your app, click Data catalog.
6. Find and select the ML - Sales predictions\_Prediction.parquet prediction dataset you just generated.
7. Click Next.
8. Under Select fields, click Select all. Click Next, and then Load into app.
9. In sheet view, add a Straight table to the sheet.
10. Add the following dimensions to the straight table:

    - date
    - store\_nbr
    - family
11. Add the following measure to the straight table: Sum (sales)
12. Expand the properties for the measure. Under Number formatting, select Money.

The table should contain forecasts starting three days after the end of the historical data, which was August 15, 2017. There should be seven unique dates in the table, with the Sum (sales) column containing the forecasts.

Visualizing sales forecasts in an analytics application

![](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ml_time-series-tutorial-forecasts-table.png "Click to view full size")

## Thank you!

You have reached the end of this tutorial. We hope that you have learned a few things about time series forecasting in Qlik Predict.
