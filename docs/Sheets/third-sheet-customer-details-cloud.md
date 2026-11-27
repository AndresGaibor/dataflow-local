---
title: "The third sheet: Customer Details"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Sheets/third-sheet-customer-details-cloud.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Tutorial - Build an analytics application"]
---

# The third sheet: Customer Details

In the third [sheet](#glossary-0 "Glossary term") you will make a scatter plot and a pivot table that focus on customers. Then you will add filter panes so you can filter by date and manager.

By now you have so much experience from creating [dimensions](#glossary-1 "Glossary term"), [measures](#glossary-2 "Glossary term"), and [visualizations](#glossary-3 "Glossary term") that you do not need detailed procedures anymore. If you need reminders of what you have learned so far, you can refer back to the previous topics.

Customer Details sheet when finished

![Customer Details sheet](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_CustomerDetailsSheetCloud.png "Click to view full size")

You will start your work in edit mode.

## Adding the scatter plot

The next visualization is a scatter plot showing the Customer Sales and Quantity.

A scatter plot is used to visualize the relationship between two or three measures.

For more information, see [*Scatter plot*](../Visualizations/ScatterPlot/scatter-plot.htm).

In this case, the measures compared are Sales and Quantity. Each bubble represents a Customer dimension value.

Do the following:

1. In the assets panel, click Fields and right-click on Sales Qty and select Create measure.
2. In the Create new measure dialog, under Name enter Quantity.
3. Under Expression, enter Sum(Sales Qty).
4. Click Create.

   The measure is added as a master item.
5. Go to Charts, and under Visualizations, drag a scatter plot to the sheet.
6. Go to Fields and drag the Customer [field](#glossary-4 "Glossary term") to the scatter plot and add it as a dimension.
7. Go to Master items and add Sales and Quantity as measures.
8. In the properties panel, go to Appearance > Presentation. Under both X-axis and Y-axis:

   1. Set Range to Custom.
   2. Set Min to 0.

   This removes negative values.
9. Give the scatter plot a title: Customer Sales and Quantity.

## Adding the Customer KPIs pivot table

The pivot table presents dimensions and measures as rows and columns in a table. In a pivot table you can analyze data by multiple measures and in multiple dimensions at the same time.

You can rearrange the measures and dimensions to get different views of the data. The activity of moving measures and dimensions interchangeably between rows and columns is known as 'pivoting'.

One of the advantages of a pivot table is the interchangeability, that is, the ability to move row items to columns and column items to rows. This flexibility is very powerful and enables you to rearrange the data and have several different views of the same data set.

Depending on what you want to focus on, you move the dimensions and measures to bring forward data of interest and hide data that is either too detailed, or irrelevant for the analysis.

For more information, see [*Pivot table*](../Visualizations/PivotTable/pivot-table.htm).

Do the following:

1. In the assets panel, go to Charts.
2. Under Visualizations, drag a pivot table to the area below the previous chart.
3. Go to Fields and add Customer as a dimension.
4. Under Master items, add Sales and Quantity as measures by dragging both to the pivot table.
5. Give the pivot table a title: Customer KPIs.

Now you have a very simple pivot table.

### Adjusting the measure formatting

Next, you will format the measure numbers.

Do the following:

1. Go to Data > Measures.
2. Click Sum (Sales) and toggle off Master measure formatting. Set the following:

   - Number formatting to Money.
   - Label to Sales.
3. Click Quantity and toggle off Master measure formatting. Set the following:

   - Number formatting to Number (1,000).
   - Label to Quantity.

### Adding measures with expressions to the pivot table

Next, you will add some more complex measures as expressions. You will create the following measures:

- Margin Percent
- # of Invoices
- Average Sales per Invoice

Do the following:

1. Select the pivot table.
2. Go to Data > Measures.
3. To create the Margin Percent measure:

   1. Click Add and click ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg). Insert this expression:

      ```
      (Sum(Sales) - Sum(Cost)) / Sum(Sales)
      ```
   2. Click Apply.
   3. Under Label, type: Margin Percent.
   4. Set Number formatting to Number (12.3%).
4. To create the # of Invoices measure:

   1. Click Add and click ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg). Insert this expression:

      ```
      Count (Distinct [Invoice Number])
      ```
   2. Click Apply.
   3. Under Label, type: # of Invoices.
5. To create the Average Sales per Invoice measure:
   1. Click Add and click ![Expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg). Insert this expression:

      ```
      Sum(Sales)/Count(Distinct [Invoice Number])
      ```
   2. Click Apply.
   3. Under Label, type: Average Sales per Invoice.
   4. Set Number formatting to Money.

Tip note

The qualifier Distinct is used in two of the expressions. By using Distinct, you ensure that an invoice number is only counted once, even if it occurs several times in the data source. Distinct sorts out unique numbers. Note that Distinct must be followed by a space before the field name.

### Adding additional dimensions as rows

Do the following:

1. Go to Data > Dimensions. Under Row, click Add.
2. In the list, select Product Group.
3. Select Add again and add a Product Type row.

You are now able to look at the sales for individual customers by product group and type. Click Customer, Product Group or Product Type, or selecting individual items in the table, filter the [selections](#glossary-5 "Glossary term") viewed in the table. By moving Product Group or Product Type to Measures and filtering you can achieve differing views of the data presented.

## Adding filter panes

Now you will add two filter panes, so you can filter by time period and manager.

Do the following:

1. Add the filter pane Period.
2. Add a new filter pane with the dimension Manager.

This sheet is complete. In the assets panel, click Sheets and select Customer Location to move to that sheet.

Related learning:

- [Using the Default Sheet Editing View in the Cloud](/lnk/Using_default_sheet_editing_Cloud)
