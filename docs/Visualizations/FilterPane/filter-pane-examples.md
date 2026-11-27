---
title: "Filter pane examples"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Visualizations/FilterPane/filter-pane-examples.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Working with visualizations", "Creating and editing visualizations", "Creating visualizations", "Creating filter panes"]
---

# Filter pane examples

This help topic provides several examples showing how you can customize styling and other properties in filter panes to achieve a number of functional purposes.

## Example 1 — Condensed design

You can add many listboxes to a filter pane, allowing refinement of data across many different dimensions.

To save space and prioritize other visualizations on your sheet, you can give your filter pane a condensed design where content is expanded and collapsed as needed.

Do the following:

1. Create a new application and paste the [*Example load script*](#ExampleData) into a new section in the [Data load editor](#glossary-0 "Glossary term"). Then, load the data.
2. Switch to sheet view. In the sheet properties, set Grid spacing to 42.
3. Drag a Filter pane onto the sheet.
4. Click Add dimension. Select Country.
5. In the properties panel, click Add field. Select Item Type.
6. Using the Add field button, add four other dimensions as listboxes:

   - Order Year
   - Order Priority
   - Region
   - Sales Channel
7. One by one, expand each listbox you just added and set Presentation > Collapse listbox to Always.
8. In the properties panel, expand Appearance > Presentation.
9. Click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg) Styling.
10. In the Filter pane tab, set the following properties:

    - Font size for Title: 18px
    - Font color for Title: Hex code #ffffff
    - Background color: Hex code #87205d
    - Shadow: Small, Hex code #000000
11. In the Listboxes tab, set the following properties:

    - Font size for Header: 14px
12. Resize the filter pane to a two-by-ten space on the sheet grid.

Switch to analysis mode. You can expand listboxes as needed to make selections.

Drawer-style filter pane in collapsed state

![Filter pane in analysis mode, in a fully collapsed state](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_filter-pane-example-1-collapsed.png "Click to view full size")

Drawer-style filter pane with dimensions list expanded

![Filter pane in analysis mode, with the dimensions list expanded](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_filter-pane-example-1-dimensions.png "Click to view full size")

## Example 2 — Rich design

Although a filter pane is mainly used to filter data, it can also be used to visualize data. Incorporating a rich design allows analyzers to gain insights as they make different selections.

Do the following:

1. Create a new application and paste the [*Example load script*](#ExampleData) into a new section in the [Data load editor](#glossary-1 "Glossary term"). Then, load the data.
2. Switch to sheet view and drag a Filter pane onto the sheet.
3. Click Add dimension. Select Item Type.
4. Click the Item Type listbox to expand its properties.
5. Expand Presentation.
6. Turn on the Histogram setting.
7. Use the Show frequency drop down menu to select Relative frequency (%).
8. Set Collapse listbox to Never.
9. Expand Sorting.
10. Set the Sorting to Custom.
11. Clear all options and turn on Sort by expression.
12. Select Descending.
13. Under Expression, enter the following expression:

    ```
    Count([Item Type])
    ```
14. In the properties panel, expand Appearance > General.
15. Turn off Show titles.
16. Expand Appearance > Presentation.
17. Click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
18. In the Listboxes tab, set the following properties:

    - Header:

      - Font: Inter, sans-serif
      - Font size: 18px
    - Content:

      - Font: Inter, sans-serif
19. Resize the filter pane to a small rectangular shape, for example, three by four squares.

Filter pane with rich design. The items in the filter pane are shown with value distribution histograms and relative percentages, and are sorted in descending order from highest to lowest occurrence.

![Filter pane in analysis mode, with histogram.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_filter-pane-example-2.png "Click to view full size")

## Example 3 — Focused design

How you design your filter pane can depend on how you want users to make selections. For example, you might want to restrict users from certain features to encourage more narrow, focused interaction with data.

Scenarios include:

- Filtering on your particular dimension brings most insight when values are selected one at a time, or selecting multiple values does not provide any meaningful insight. To guide analysis in this way, you can turn off range selection by using checkbox mode.
- Searching for values in the field either provides no insight, or is not desirable.
- You want to minimize distractions when filtering data—for example, the selections toolbar.

Do the following:

1. Create a new application and paste the [*Example load script*](#ExampleData) into a new section in the [Data load editor](#glossary-2 "Glossary term"). Then, load the data.
2. Switch to sheet view and drag a Filter pane onto the sheet.
3. Click Add dimension. Select Item Type.
4. Click the Item Type listbox to expand its properties.
5. Set Search to Hide.
6. Turn off Show Selection toolbar.
7. Expand Presentation.
8. Turn on Checkbox mode.
9. In the properties panel, expand Appearance > General.
10. Turn off Show titles.
11. Resize the filter pane to a small rectangular shape, for example, three by four squares.

Filter pane with focused design

![Filter pane in analysis mode, using checkbox mode.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_filter-pane-example-3.png "Click to view full size")

## Example 4 — Grid design

You can use grid mode for filter panes that use small, defined sets of data. A good example is organizing time-based dimensions in grids.

This example uses a text-based grid. For information about cell background images and other cell options, see [*Representing field values as images*](create-filter-panes.htm#Representation).

Do the following:

1. Create a new application and paste the [*Example load script*](#ExampleData) into a new section in the [Data load editor](#glossary-3 "Glossary term"). Then, load the data.
2. Switch to sheet view and drag a Filter pane onto the sheet.
3. Click Add dimension. Select Order Year.
4. Click the Order Year listbox to expand its properties.
5. Turn off Show title.
6. Expand Presentation.
7. Set Collapse listbox to Never.
8. For Show data in, select Grid.
9. Set Max visible columns to Custom.
10. Set Max columns to 3.
11. Add Order Quarter as a listbox in the filter pane.
12. Click the Order Quarter listbox to expand its properties.
13. Turn off Show titles.
14. Expand Presentation.
15. Set Collapse listbox to Never.
16. For Show data in, select Grid.
17. Set Order by to Columns.
18. Set Max visible rows to Custom.
19. Set Max row to 1.
20. Add Order Month as a listbox in the filter pane.
21. Click the Order Month listbox to expand its properties.
22. Turn off Show title.
23. Expand Presentation.
24. Set Collapse listbox to Never.
25. For Show data in, select Grid.
26. Set Max visible columns to Custom.
27. Set Max columns to 4.
28. In the properties panel, expand Appearance > General.
29. Turn off Show title.
30. In the properties panel, expand Appearance > Presentation.
31. Click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
32. In the Filter pane tab, set the following properties:

    - Background color: #83af9b
33. In the Listboxes tab, set the following properties:

    - Content:

      - Font: Fredoka One, fantasy
      - Text size: 15px
      - Text size: Bold
      - Text color: #000000
    - Selection state > Possible: #000000
    - Background color: #83af9b
34. Resize the filter pane to a size that works well for the display—for example, three by three.

Filter pane with grid design

![Filter pane in analysis mode, using grid mode.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_filter-pane-example-4.png "Click to view full size")

### Further enhancements: composite filter pane with the layout container

For further responsiveness and control, you could create the above filter pane as a series of three filter panes embedded within a layout container. The image below shows an example of what this might look like.

Grid-style filter panes embedded in a layout container

![Layout container with multiple grid-style filter panes.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_filter-pane-example-4-as-layout-container.png "Click to view full size")

## Example 5 — Aligning with organization's color palette

Filter panes can be styled in accordance with your organization's color palette. In addition to defining background and text color, you can set color schemes for the selection states in your filter pane. You might want selections to appear in your company's main brand colors rather than the default green color.

With custom themes, you can further apply your organization's color scheme by setting a color for selections across all visualizations and the selection toolbar. For more information, see [Custom themes](https://qlik.dev/extend/create-custom-themes/).

In this example, we create a filter pane reflecting the following brand colors:

- Main color: Hex code #3100ff
- Secondary color: Hex code #9ba7ff

Do the following:

1. Create a new application and paste the example data into a new section in the [Data load editor](#glossary-4 "Glossary term"). Then, load the data.
2. Switch to sheet view and drag a Filter pane onto the sheet.
3. Click Add dimension. Select Item Type.
4. In the properties panel, click Add field. Select Order Year.
5. Using the Add field button, add three other dimensions as listboxes:

   - Order Priority
   - Region
   - Sales Channel
6. In the properties panel, expand Appearance > General.
7. Turn off Show titles.
8. Expand Appearance > Presentation.
9. Click ![Palette](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_palette.svg)Styling.
10. In the Filter pane tab, set the following properties:

    - Shadow: Small, Hex code #000000
11. In the Listboxes tab, set the following properties:

    - Font size for Header: 14px
    - Selection state:

      - Selected: Hex code #3100ff
      - Alternative: Hex code #9ba7ff
      - Excluded: #bebebe
      - Selected excluded: #7b7a78
      - Possible: #ffffff
12. Resize the filter pane to a long rectangular shape on one side of the sheet—for example, three by twelve squares.

Switch to analysis mode. Make selections in the filter pane to view the color scheme.

Filter pane with selection states reflecting brand colors

![Filter pane with selection states reflecting brand colors](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_filter-pane-example-5.png "Click to view full size")

## Example load script

Data for examples

```
Sales:
LOAD
Dual([Order Month Text], [Order Month Num]) as [Order Month],

* INLINE [
Order ID,Order Date,Order Year,Order Quarter,Order Month Text,Order Month Num,Region,Country,Item Type,Sales Channel,Order Priority,Ship Date,Units Sold,Unit Price,Unit Cost,Total Revenue,Total Cost,Total Profit
522840487,2/8/2021,2021,Q1,Feb,2,Central America and the Caribbean,Honduras,Household,Offline,H,2/13/2017,8974,668.27,502.54,5997054.98,4509793.96,1487261.02
832401311,2/19/2021,2021,Q1,Feb,2,Asia,Mongolia,Personal Care,Offline,C,2/23/2014,4901,81.73,56.67,400558.73,277739.67,122819.06
419123971,11/19/2021,2021,Q4,Nov,11,Asia,Sri Lanka,Cosmetics,Offline,M,12/18/2016,6952,437.2,263.33,3039414.4,1830670.16,1208744.24
441619336,12/30/2021,2021,Q4,Dec,12,Asia,Turkmenistan,Household,Offline,L,1/20/2011,3830,668.27,502.54,2559474.1,1924728.2,634745.9
795490682,6/30/2022,2022,Q2,Jun,6,Central America and the Caribbean,Honduras,Snacks,Online,L,7/26/2016,2225,152.58,97.44,339490.5,216804,122686.5
158535134,10/27/2022,2022,Q4,Oct,10,Australia and Oceania,Australia,Office Supplies,Online,C,11/25/2015,2924,651.21,524.96,1904138.04,1534983.04,369155
955357205,1/5/2022,2022,Q1,Jan,1,Europe,United Kingdom,Household,Online,L,2/14/2012,282,668.27,502.54,188452.14,141716.28,46735.86
259353148,4/7/2022,2022,Q2,Apr,4,Sub-Saharan Africa,Djibouti,Cosmetics,Offline,H,4/19/2014,7215,437.2,263.33,3154398,1899925.95,1254472.05
450563752,6/9/2022,2022,Q2,Jun,6,Australia and Oceania,Australia,Cereal,Offline,H,7/2/2013,682,205.7,117.11,140287.4,79869.02,60418.38
705784308,10/30/2022,2022,Q4,Oct,10,Middle East and North Africa,Libya,Clothes,Offline,H,11/17/2010,6116,109.28,35.84,668356.48,219197.44,449159.04
505716836,10/13/2022,2022,Q4,Oct,10,Central America and the Caribbean,Haiti,Cosmetics,Offline,H,11/16/2013,1705,437.2,263.33,745426,448977.65,296448.35
807025039,7/25/2023,2023,Q3,Jul,7,Central America and the Caribbean,Belize,Clothes,Offline,M,9/7/2016,5498,109.28,35.84,600821.44,197048.32,403773.12
166460740,10/24/2023,2023,Q4,Oct,10,Europe,Lithuania,Office Supplies,Offline,H,11/17/2010,8287,651.21,524.96,5396577.27,4350343.52,1046233.75
462405812,4/23/2023,2023,Q2,Apr,4,Asia,Turkmenistan,Office Supplies,Online,M,5/20/2013,5010,651.21,524.96,3262562.1,2630049.6,632512.5
816200339,8/14/2023,2023,Q3,Aug,8,Middle East and North Africa,Libya,Fruits,Online,L,9/30/2015,673,9.33,6.92,6279.09,4657.16,1621.93
555990016,5/20/2023,2023,Q2,May,5,Sub-Saharan Africa,Djibouti,Cereal,Online,H,6/17/2017,8656,205.7,117.11,1780539.2,1013704.16,766835.04
231145322,7/5/2023,2023,Q3,Jul,7,Middle East and North Africa,Pakistan,Cosmetics,Offline,L,8/16/2013,9892,437.2,263.33,4324782.4,2604860.36,1719922.04
986435210,11/6/2023,2023,Q4,Nov,11,North America,Mexico,Household,Offline,C,12/12/2014,6954,668.27,502.54,4647149.58,3494663.16,1152486.42
217221009,10/28/2023,2023,Q4,Oct,10,Australia and Oceania,Federated States of Micronesia,Beverages,Online,C,11/15/2014,9379,47.45,31.79,445033.55,298158.41,146875.14
670854651,7/20/2024,2024,Q3,Jul,7,Australia and Oceania,Samoa,Cosmetics,Online,H,8/7/2013,9654,437.2,263.33,4220728.8,2542187.82,1678540.98
213487374,10/21/2024,2024,Q4,Oct,10,Europe,Spain,Household,Offline,L,11/30/2012,4513,668.27,502.54,3015902.51,2267963.02,747939.49
663110148,9/18/2024,2024,Q3,Sep,9,Middle East and North Africa,Lebanon,Clothes,Online,L,10/8/2012,7884,109.28,35.84,861563.52,282562.56,579000.96
827844560,3/18/2024,2024,Q1,Mar,3,Sub-Saharan Africa,Kenya,Vegetables,Online,L,4/7/2012,6457,154.06,90.93,994765.42,587135.01,407630.41
430915820,2/17/2024,2024,Q1,Feb,2,North America,Mexico,Personal Care,Offline,L,3/20/2012,6422,81.73,56.67,524870.06,363934.74,160935.32
240470397,7/7/2024,2024,Q3,Jul,7,Australia and Oceania,Australia,Beverages,Offline,H,7/11/2014,9389,47.45,31.79,445508.05,298476.31,147031.74
559427106,7/30/2024,2024,Q3,Jul,7,North America,Mexico,Personal Care,Offline,M,8/8/2015,5767,81.73,56.67,471336.91,326815.89,144521.02
665095412,2/10/2025,2025,Q1,Feb,2,Sub-Saharan Africa,Mozambique,Household,Offline,L,2/15/2012,5367,668.27,502.54,3586605.09,2697132.18,889472.91
];

drop fields [Order Month Text], [Order Month Num];
```
