---
title: "Always one selected value"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataSource/select-single-value.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Get started with visualizations", "Using data assets in visualizations", "Fields"]
---

# Always one selected value

You can select the Always one selected value for a [field](#glossary-0 "Glossary term") in an application. The value specifies that one, and only one, value is always selected for a field. You can use this value to specify, for example, that one currency is always selected for a field.

Consider the following when using the Always one selected value:

- You can use the Always one selected value on one or more fields.
- You cannot clear the Always one selected value setting when viewing a [sheet](#glossary-2 "Glossary term"). You can, however, clear the setting by editing the sheet in your workspace.
- When you publish an application with the Always one selected value selected, the value is applied to all sheets in the application. The application consumer cannot clear the value.
- When you duplicate an application, the Always one selected value is duplicated with the application.
- When you export an application without data, the Always one selected value is not exported with the application.
- The Always one selected value is not supported for derived fields.
- Always one selected value is a field setting within the data model. Therefore, if you want to turn this setting on or off for an application that has been published to a managed space, you need to make the change on the source application and then republish the application using the Include data option.

You can use the value with a default bookmark in to highlight specific selections for your application consumer. For an example, see [*Always one selected value and default bookmark example: Controlling selections to guide application consumers to insights*](#AlwaysOneExample).

For more information about default bookmarks, see [*Setting a default bookmark to create an application landing page*](../Bookmarks/set-default-bookmark.htm).

## Set the Always one selected value

Do the following:

1. Open a sheet in an application.
2. Click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Edit sheet.
3. Click Fields.
4. Right-click a field, and then click Field settings.
5. In the window that opens, select the Always one selected value check box, and then save.
6. Exit sheet edit mode. The value appears as a tab in the top toolbar. Unlike a [bookmark](#glossary-3 "Glossary term"), there is no option to clear the selection.

   The Always one selected value in the toolbar

   ![The value as a tab in the top toolbar.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_AlwaysOne.png "Click to view full size")

   The Always one selected value defaults to the first entry in the field. In the example above, the value is applied to Region. Asia is the region that is selected by default. You or your application consumer can change this selection, in this case to a different region.
7. To test that the Always one selected value is working properly, close and then reopen the application. The value should be shown in the top toolbar.

To remove the Always one selected value for a field, right-click the field in Edit mode, click Field settings, and deselect the  Always one selected value check box.

## Always one selected value and default bookmark example: Controlling selections to guide application consumers to insights

In this example, we set Always one selected value for a field. We then specify a default bookmark for the application. By specifying a default bookmark, and enabling Always one selected value, we control what our application consumers see when they open our published application.

1. Here is a sheet in our application before the Always one selected value and a default bookmark are applied. This should be the sheet that you want application consumers to see as a landing page when they open the application.

   Application in sheet analysis mode

   ![App with filter panes and conditional chart expression](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_AlwaysOne_ExampleApp.png "Click to view full size")

   The chart in the application is built using Country as a dimension, and Sum([Total Revenue]) as a measure.
2. To ensure that one, and only one, value is always selected for the Region field, we edit the sheet, click Fields, and then right-click Region.
3. Click Field settings.
4. We then select the Always one selected value checkbox and save.

   Turning on the Always one selected value setting

   ![Dialog box where the 'Always one selected value' checkbox has been checked](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_AlwaysOne_setting.png "Click to view full size")
5. When we close Edit mode for the sheet, the Always one selected value value appears as a tab in the top toolbar. The value defaults to the first entry in the field. In this case, the default value is Asia.

   Application in sheet view with default value selected for Always one selected value field

   ![App in sheet analysis mode, showing that the 'Always one selected value' setting is applied to 'Region' and the top value of 'Asia' is selected by default](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_AlwaysOne_Default.png "Click to view full size")
6. However, we want to show revenue for sub-Saharan Africa when the application is opened. So we select Sub-Saharan Africa from the Region field, and then click Bookmarks to create a new bookmark for Region("Sub-Saharan Africa"). We then right-click the Region("Sub-Saharan Africa") bookmark, and click Set as default bookmark.

Now, when we open the application, or publish the application for an application consumer, the application opens with one value selected, and the default bookmark is shown. The application is opened on the sheet of the bookmark instead of the application overview.

Application opened with default bookmark, using the defined selection Sub-Saharan Africa

![App in sheet analysis mode, showing modified selection of field configured with the 'Always one selected value' field setting](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_AlwaysOne_Bookmark.png "Click to view full size")

### Data used in example

Load script

You can add the paste the data table below into your load script to try this example out in your own application.

For more information about using inline loads, see [*Using inline loads to load data*](../Scripting/inline-loads-qs.htm).

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
