---
title: "Trellis container advanced mode examples"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/VisualizationBundle/trellis-advanced-mode.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Choosing the right visualization", "Dashboard objects", "Trellis container"]
---

# Trellis container advanced mode examples

Expand/Collapse all

# Trellis container advanced mode examples

This help topic shows examples of how you can use a Trellis container in advanced mode to configure advanced expressions in your charts.

The following variables are shown in this help topic:

- $(vDim)
- $(vDimValue)
- $(vDimSetFull)

For additional examples, see [*Using advanced mode*](creating-trellis-container.htm#AdvMode).

## Example 1: Conditional measure expression

This example shows you how the $(vDimValue) variable can be added to measure expressions to make the Trellis container compatible with advanced expressions. The expression used in this chart is a conditional if expression.

### Add the data

Create a new application and add the load script below into the [Data load editor](#glossary-0 "Glossary term"). Then, load the data.

Load script

For more information about using inline loads, see [*Using inline loads to load data*](../../Scripting/inline-loads-qs.htm).

```
Sales:
					LOAD * INLINE [
					Region,Country,Item Type,Sales Channel,Order Priority,Order Date,Order ID,Ship Date,Units Sold,Unit Price,Unit Cost,Total Revenue,Total Cost,Total Profit
					Central America and the Caribbean,Honduras,Household,Offline,H,2/8/2017,522840487,2/13/2017,8974,668.27,502.54,5997054.98,4509793.96,1487261.02
					Asia,Mongolia,Personal Care,Offline,C,2/19/2014,832401311,2/23/2014,4901,81.73,56.67,400558.73,277739.67,122819.06
					Asia,Sri Lanka,Cosmetics,Offline,M,11/19/2016,419123971,12/18/2016,6952,437.20,263.33,3039414.40,1830670.16,1208744.24
					Asia,Turkmenistan,Household,Offline,L,12/30/2010,441619336,1/20/2011,3830,668.27,502.54,2559474.10,1924728.20,634745.90
					Central America and the Caribbean,Honduras,Snacks,Online,L,6/30/2016,795490682,7/26/2016,2225,152.58,97.44,339490.50,216804.00,122686.50
					Australia and Oceania,Australia,Office Supplies,Online,C,10/27/2015,158535134,11/25/2015,2924,651.21,524.96,1904138.04,1534983.04,369155.00
					Europe,United Kingdom,Household,Online,L,1/5/2012,955357205,2/14/2012,282,668.27,502.54,188452.14,141716.28,46735.86
					Sub-Saharan Africa,Djibouti,Cosmetics,Offline,H,4/7/2014,259353148,4/19/2014,7215,437.20,263.33,3154398.00,1899925.95,1254472.05
					Australia and Oceania,Australia,Cereal,Offline,H,6/9/2013,450563752,7/2/2013,682,205.70,117.11,140287.40,79869.02,60418.38
					Middle East and North Africa,Libya,Clothes,Offline,H,10/30/2010,705784308,11/17/2010,6116,109.28,35.84,668356.48,219197.44,449159.04
					Central America and the Caribbean,Haiti,Cosmetics,Offline,H,10/13/2013,505716836,11/16/2013,1705,437.20,263.33,745426.00,448977.65,296448.35
					Central America and the Caribbean,Belize,Clothes,Offline,M,7/25/2016,807025039,9/7/2016,5498,109.28,35.84,600821.44,197048.32,403773.12
					Europe,Lithuania,Office Supplies,Offline,H,10/24/2010,166460740,11/17/2010,8287,651.21,524.96,5396577.27,4350343.52,1046233.75
					Asia,Turkmenistan,Office Supplies,Online,M,4/23/2013,462405812,5/20/2013,5010,651.21,524.96,3262562.10,2630049.60,632512.50
					Middle East and North Africa,Libya,Fruits,Online,L,8/14/2015,816200339,9/30/2015,673,9.33,6.92,6279.09,4657.16,1621.93
					Sub-Saharan Africa,Djibouti,Cereal,Online,H,5/20/2017,555990016,6/17/2017,8656,205.70,117.11,1780539.20,1013704.16,766835.04
					Middle East and North Africa,Pakistan,Cosmetics,Offline,L,7/5/2013,231145322,8/16/2013,9892,437.20,263.33,4324782.40,2604860.36,1719922.04
					North America,Mexico,Household,Offline,C,11/6/2014,986435210,12/12/2014,6954,668.27,502.54,4647149.58,3494663.16,1152486.42
					Australia and Oceania,Federated States of Micronesia,Beverages,Online,C,10/28/2014,217221009,11/15/2014,9379,47.45,31.79,445033.55,298158.41,146875.14
					Australia and Oceania,Samoa,Cosmetics,Online,H,7/20/2013,670854651,8/7/2013,9654,437.20,263.33,4220728.80,2542187.82,1678540.98
					Europe,Spain,Household,Offline,L,10/21/2012,213487374,11/30/2012,4513,668.27,502.54,3015902.51,2267963.02,747939.49
					Middle East and North Africa,Lebanon,Clothes,Online,L,9/18/2012,663110148,10/8/2012,7884,109.28,35.84,861563.52,282562.56,579000.96
					Sub-Saharan Africa,Kenya,Vegetables,Online,L,3/18/2012,827844560,4/7/2012,6457,154.06,90.93,994765.42,587135.01,407630.41
					North America,Mexico,Personal Care,Offline,L,2/17/2012,430915820,3/20/2012,6422,81.73,56.67,524870.06,363934.74,160935.32
					Australia and Oceania,Australia,Beverages,Offline,H,7/7/2014,240470397,7/11/2014,9389,47.45,31.79,445508.05,298476.31,147031.74
					North America,Mexico,Personal Care,Offline,M,7/30/2015,559427106,8/8/2015,5767,81.73,56.67,471336.91,326815.89,144521.02
					Sub-Saharan Africa,Mozambique,Household,Offline,L,2/10/2012,665095412,2/15/2012,5367,668.27,502.54,3586605.09,2697132.18,889472.91
				];
```

### Create the master visualization

Do the following:

1. Open a sheet in edit mode.
2. Drag a bar chart onto the sheet.
3. Add Item Type as a dimension to the bar chart.
4. Add the following expression as a measure:

   ```
   =if(Sum([Units Sold])>=40000, Sum({<Region={$(vDimValue)}>} [Total Profit]), Sum({<Region={$(vDimValue)}>} [Units Sold]))
   ```

   In the Trellis container, this expression will show:

   - If there are 40,000 or more units sold: The total profit for each distinct region.
   - If there are less than 40,000 units sold, or if the data is null: The total number of units sold for each distinct region.

   For each chart in the container, the  $(vDimValue) variable will be replaced by the dimension value name for Region.
5. For the measure you just added, add the following Label:

   ```
   =if(Sum([Units Sold])>=40000, 'Total Profit', 'Items Sold')
   ```
6. In the properties panel, expand Sorting. Adjust the sorting so that the chart sorts primarily by the measure value in descending order.
7. In the properties panel, under Appearance, expand Colors and legend.
8. Set Colors to Custom and choose the option to color the chart By dimension.
9. Turn on Persistent colors.
10. Right-click the chart, or use the ![Three-dot menu](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) button, and click Add to master items.
11. Give the master item a Name (for example, BarChartExample), and click Add.

### Create the Trellis container

Do the following:

1. In the assets panel, open Charts and under Dashboard objects, drag a Trellis container onto the sheet.
2. Click Add dimension, and select Region.
3. Click Add master visualization. In the drop down menu, select the BarChartExample master item.
4. In the properties panel for the Trellis container, under Appearance, expand Trellis options.
5. Set Advanced mode to On.
6. In the properties panel for the Trellis container, under Appearance, expand General.
7. Toggle on Show titles if needed. Add the following expression for the Title of the chart:

   ```
   =if(Sum([Units Sold])>=40000, 'Total Profit, by Region and Item Type', 'Total Items Sold, by Region and Item Type')
   ```

Resize the Trellis container on the sheet so that it has enough space to show all data. Your chart should now look something like the following image.

Example result with no selections made in the application

![Trellis container containing a number of bar charts for each region. No selections are made in the app, so the charts show total profit](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_example_trellis-container-bar-no-selection.png "Click to view full size")

If you make selections in the application (for example, by selecting a specific Order Priority), the [measure](#glossary-1 "Glossary term") shown in the chart could change given the lower order volume.

Example result with a selection made in the application

![Trellis container containing a number of bar charts for each region. The app data has been considerably filtered by a selection, so the charts show total items shipped](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_example_trellis-container-bar-with-selection.png "Click to view full size")

## Example 2: Coloring on a map chart

This example will show you how to configure a Trellis container in Advanced mode to color a map chart by measure expression. Specifically, it shows the following:

- Using $(vDimSetFull) to color map charts by measure.
- Using $(vDim) and $(vDimValue) in text within the charts (in this case, for the chart subtitles).

### Add the data

Create a new application and the load script below into the [Data load editor](#glossary-2 "Glossary term"). Then, load the data.

Load script

For more information about using inline loads, see [*Using inline loads to load data*](../../Scripting/inline-loads-qs.htm).

```
SET DateFormat='MM/DD/YYYY';

					[Regional Sales]:

					Load RowNo() as OrderID, Year(OrderDate) as Year, * Inline [
					Country,OrderDate,Sales
					Peru,01/15/2022,227752.86
					India,09/24/2023,273204.8
					United Kingdom,10/12/2020,196509.42
					Brazil,04/09/2022,62936.87
					Peru,06/19/2023,343348.25
					France,10/08/2021,137087.24
					Brazil,04/02/2023,364144.83
					France,01/18/2021,147458.3
					France,07/31/2021,131735.39
					France,08/28/2021,175657.49
					Mexico,11/29/2023,347796.5
					Brazil,10/22/2021,156415.67
					United States,06/26/2022,71698.01
					Mexico,07/06/2021,302858.53
					United States,09/02/2023,380184.4
					Japan,12/17/2023,138012.27
					Spain,01/06/2022,360035.92
					Nigeria,07/26/2020,117583.51
					India,08/27/2022,319078.12
					Nigeria,05/10/2021,185315.61
					France,01/22/2021,79605.99
					Mexico,11/08/2022,410677.64
					United Arab Emirates,01/21/2022,304060.08
					Japan,05/01/2020,382370.67
					Peru,10/07/2020,163162.77
					Japan,10/28/2023,116031.67
					Japan,08/13/2021,202813.87
					Brazil,12/18/2020,116177.28
					France,08/05/2023,251482.97
					United States,11/30/2023,354524.01
					Brazil,02/27/2022,333082.0
					Japan,03/02/2024,272875.61
					Japan,10/05/2022,241957.76
					Mexico,10/13/2020,415713.42
					France,02/01/2021,278095.0
					Brazil,04/21/2023,32234.39
					United States,03/06/2020,31705.72
					Japan,10/16/2021,397489.08
					Peru,01/24/2021,164315.87
					Peru,08/10/2021,39399.43
					Japan,08/19/2021,55312.24
					United States,06/19/2021,47950.8
					France,04/05/2020,66698.87
					Chile,02/05/2023,209699.99
					Canada,04/03/2022,40362.07
					India,05/07/2023,448813.12
					France,11/21/2023,382234.7
					United States,05/22/2020,454589.09
					Brazil,12/20/2021,46482.62
					Peru,04/18/2023,196877.9
					Canada,12/22/2021,292966.22
					France,12/05/2020,441694.97
					Brazil,02/14/2023,172206.44
					Mexico,04/11/2022,302489.06
					Peru,05/12/2022,293993.12
					Peru,04/24/2022,248774.21
					Canada,06/04/2024,392124.04
					Mexico,03/04/2020,142287.51
					Japan,02/27/2022,75894.1
					Brazil,05/07/2021,52657.97
					Mongolia,01/31/2020,447353.36
					France,04/05/2022,275954.94
					Brazil,03/03/2022,86689.07
					United States,01/27/2023,304884.26
					Spain,05/03/2021,143572.48
					Australia,03/28/2022,132283.75
					Japan,04/20/2021,259819.31
					Canada,06/12/2020,366820.82
					France,09/15/2020,337837.91
					Japan,07/09/2020,95159.91
					Japan,10/19/2021,149382.85
					Brazil,09/09/2021,325617.68
					Mexico,06/06/2021,324661.14
					Brazil,09/28/2022,366444.31
					Mexico,05/26/2023,394055.4
					Japan,05/30/2021,77322.47
					Japan,02/06/2023,187484.72
					United States,11/13/2022,307780.43
					France,03/26/2022,438656.23
					Japan,03/16/2020,237080.43
					United Kingdom,12/31/2022,372867.22
					Mexico,12/23/2022,251630.19
					Kenya,09/11/2023,167978.34
					Peru,08/12/2022,174796.28
					Brazil,03/20/2020,360178.71
					Nigeria,06/04/2024,236178.16
					United States,06/19/2022,230182.87
					Brazil,12/30/2021,128965.58
					Nigeria,07/26/2023,96338.83
					Peru,05/16/2021,354580.5
					Spain,02/21/2024,107994.23
					Mongolia,05/19/2022,240049.35
					United States,10/20/2022,302237.71
					Brazil,02/11/2022,162125.17
					Brazil,02/20/2023,223010.48
					Nigeria,06/20/2024,206926.14
					Mexico,02/27/2023,378327.98
					France,03/07/2022,432543.14
					France,05/20/2020,61227.11
					Japan,08/26/2020,46839.45
					France,01/18/2024,193017.69
					France,11/25/2020,290340.4
					Canada,08/08/2022,385273.52
					United States,09/26/2021,204250.05
					United States,08/04/2022,223287.59
					Mexico,11/14/2022,256152.68
					Brazil,01/15/2020,242880.01
					Mexico,11/25/2020,430857.71
					United States,06/05/2021,378069.6
					France,01/03/2022,316563.84
					United Kingdom,05/19/2021,243918.77
					United States,05/17/2023,204355.25
					Nigeria,03/13/2020,293234.49
					Mongolia,06/24/2022,245425.64
					Australia,12/19/2020,379893.22
					United States,01/01/2021,288622.04
					Brazil,05/03/2022,242795.62
					Mexico,04/07/2021,227912.73
					Japan,11/26/2021,144015.86
					Canada,09/17/2020,126427.98
					Mexico,08/04/2021,170917.99
					Brazil,09/16/2021,302048.81
					Japan,12/16/2020,271152.67
					Peru,09/10/2021,384189.71
					United States,04/29/2020,454328.73
					Peru,08/27/2020,190456.76
					Canada,09/29/2022,296216.69
					United States,06/20/2020,293064.04
					Nigeria,07/21/2023,329696.64
					France,03/29/2022,125031.6
					Canada,11/28/2020,334136.19
					India,01/27/2023,364236.69
					United States,04/05/2024,146632.59
					Brazil,11/23/2021,442283.3
					Canada,09/17/2020,149007.7
					Brazil,03/15/2023,170612.37
					Peru,02/09/2021,156444.13
					Brazil,03/17/2021,217404.08
					Mongolia,04/26/2020,312406.89
					Canada,10/08/2020,381041.07
					Brazil,06/11/2022,347838.35
					Peru,01/24/2022,250253.73
					Canada,11/30/2020,54392.41
					Brazil,12/14/2020,301046.63
					United Kingdom,11/30/2023,23456.55
					United States,11/18/2021,411647.97
					Mexico,10/27/2022,35642.56
					Nigeria,01/12/2021,310103.2
					Mongolia,04/24/2023,66497.07
					Japan,03/01/2020,115616.07
					Brazil,11/11/2021,427971.79
					Australia,04/30/2020,224772.13
					Mongolia,10/31/2020,99216.73
					Peru,08/21/2020,403962.65
					Peru,01/30/2023,185795.36
					Japan,01/25/2023,123502.1
					Nigeria,01/12/2024,203772.15
					United States,11/13/2020,148393.65
					Brazil,12/06/2020,112804.31
					United States,07/14/2022,301281.13
					Peru,04/09/2020,250693.79
					Peru,05/21/2024,393405.04
					Japan,03/26/2022,52544.23
					Brazil,01/16/2023,90154.56
					Mexico,01/22/2023,26075.54
					Brazil,11/28/2021,23825.06
					Peru,11/09/2020,161572.89
					Mexico,07/28/2021,49412.07
					Japan,01/11/2021,307169.36
					Canada,09/06/2021,73335.63
					Nigeria,04/14/2023,1187523.85
					France,10/22/2021,72831.06
					Brazil,03/07/2020,369401.17
					Canada,06/04/2020,341681.27
					Brazil,06/20/2021,386016.82
					Peru,10/26/2022,32322.15
					Canada,04/16/2021,345333.21
					Japan,03/24/2020,205311.36
					Japan,09/29/2023,415385.44
					Nigeria,03/28/2023,449452.09
					France,10/04/2020,95167.1
					Japan,08/14/2021,358862.28
					Mongolia,06/24/2024,329040.71
					France,03/02/2023,132649.55
					France,09/20/2022,408825.94
					Canada,05/22/2021,423239.99
					Spain,09/06/2020,47063.8
					Brazil,05/11/2024,393786.01
					Mexico,06/02/2023,34370.17
					Brazil,01/31/2024,284225.11
					Peru,04/17/2023,404147.81
					Brazil,11/25/2022,190314.55
					Peru,12/03/2021,141599.92
					Chile,10/29/2021,244343.67
					Japan,09/11/2022,448202.62
					United States,02/11/2020,120006.54
					France,12/11/2021,97129.11
					Peru,01/30/2021,312698.45
					France,09/24/2023,195299.87
					France,04/10/2024,448665.96
				];
```

### Create the master visualization

Do the following:

1. Open a sheet in edit mode.
2. Drag a map chart onto the sheet.
3. In the properties panel, create a new area layer for the chart.
4. Add Country as the dimension for the area layer.
5. In the Country area layer, expand Colors.
6. Set Colors to Custom and select the By measure color setting.
7. Add the following expression for Select measure:

   ```
   =Sum($(vDimSetFull) Sales)
   ```
8. Add the following Label to the measure color: Total Sales
9. Expand the Appearance > General section in the properties panel.
10. Enter the following expression for the chart Subtitle:

    ```
    ='Total Sales, ' & $(vDim) & ': ' & $(vDimValue)
    ```

    This expression returns an error in the master visualization, but in the Trellis container, it functions intended. For each unique Year value, the title of the chart will be Total Sales, Year: <year>.
11. Right-click the chart, or use the ![Three-dot menu](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) button, and click Add to master items.
12. Give the master item a Name (for example, MapChartExample), and click Add.

### Create the Trellis container

Do the following:

1. In the assets panel, open Charts and under Dashboard objects, drag a Trellis container onto the sheet.
2. Click Add dimension, and select Year.
3. Click Add master visualization. In the drop down menu, select the MapChartExample master item.
4. In the properties panel for the Trellis container, under Appearance, expand Trellis options.
5. Set Advanced mode to On.
6. Set Number of columns to a value that works best for your sheet and screen size. To match the image below, set this to 5.
7. In the properties panel for the Trellis container, under Appearance, expand General.
8. Add the following Title for the chart: Total Sales by Country
9. Resize the chart if needed so that it occupies the entire length of the sheet.
10. Exit sheet edit mode.

To get the same color scheme as shown in the image below, set the application theme to Sense Classic.

Example result

![Trellis container containing 5 map charts, one for each year in the app data](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_example_trellis-container-map.png "Click to view full size")

## Learn more

- [*Trellis container*](trellis-container.htm)
