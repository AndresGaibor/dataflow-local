---
title: "Creating highly formatted tables"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/PixelPerfect/pixelperfect-highly-formatted-table.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing PixelPerfect report templates", "Adding content to your PixelPerfect report template", "Visualizing application data in your report"]
---

# Creating highly formatted tables

You can create highly formatted tables in your PixelPerfect report template. The PixelPerfect designer allows for extensive control and customization during table creation. Create highly formatted tables by inserting levels, labels, and other content individually. Creating these tables involves the use of a DetailReport band, and associated GroupHeader and GroupFooter bands. You need to use levels to achieve the desired output.

The representation of data-bound objects in a tabular format is achieved by the action of connecting a level data binding to a DetailReport band.

When you create a highly formatted table, you can optionally nest it within other levels, and add calculated totals, conditional formats, and calculated columns.

Highly formatted PixelPerfect table

![Example report showing a highly formatted PixelPerfect table. The table shows a three-column dataset with Categories, Sales, and Sales Perc. (percentage) as the columns, with totals and conditional formatting also used](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-highly-formatted-table.png "Click to view full size")

## Workflow

At a high level, the recommended workflow is the following. For a full example, see [*Example - highly formatted table with a level*](#Example).

### Step 1: Create a data binding

Under ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List > Levels, add a level data binding to define the information you want to present in the table.

Do the following:

1. Expand ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List in the right-side panel.
2. Click the plus icon next to Levels.
3. Find the item you want to add as a level, and click ![Plus](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) next to it.

### Step 2: Create the banded structure

To create a highly formatted table, you need to create a series of bands that have specific data bindings. The bands need to be organized in a hierarchical structure as follows:

1. First, create a DetailReport band.
2. Add a GroupHeader band within the DetailReport band. It will automatically be added at the top of the band.
3. Add a GroupFooter band within the DetailReport band. It will automatically be added at the bottom of the band.

### Step 3: Bind the structure to the data source

1. Use the Properties menu to add a Data Member for the DetailReport band you created in step 1.

   For more information, see [*Data binding*](pixelperfect-data-binding.htm).
2. Add the individual fields from the level data binding. Do this by dragging and dropping them from the Field List as labels onto the  Detail band that is located between the GroupHeader and GroupFooter.

### Step 4: Add the table headers

Add table headers within the GroupHeader band by dragging label objects from the toolbox. Define the text in the labels with your custom fixed text.

### Step 5 (optional): Add calculated totals for a column

If desired, you can add calculated totals into the GroupFooter.

1. Add a label for the field you want to aggregate onto the GroupFooter band.
2. Use the Properties menu to configure the label as a grouped aggregation. This is done under Text > Summary. Select Group in the Running drop down menu.
3. Define a formula for the label that incorporates a PixelPerfect summary function. You likely need to use sumSum().

### Other enhancements: Levels, conditional formatting, and calculated columns

If needed, you can apply conditional formatting to elements in your PixelPerfect table. If you need to add columns with calculations that are not defined in the Qlik Sense application, you can use the PixelPerfect tools to define new calculations and add them to your table.

You can also nest your highly formatted table within one or more data-bound DetailReport bands to create a series of tables cycled along, for example, the values in a dimension.

## Example - highly formatted table with a level

Refer to the example application sources here: [*Examples - In-application reporting*](../../InAppGeneral/reporting-example-material.htm). Upload the application and data files into a space, and then reload the application. You are ready to complete the example.

In this example, we create a highly formatted table that is nested within a Region level. You can also create a simpler report without nesting the table inside the Region level.

### Create data bindings

We will first create the data binding for the level on which the table iteration is cycled, then we will create the data binding for the table itself.

Do the following:

1. Create a new PixelPerfect template.
2. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu available from the right-side panel in the designer.

   Field List menu in the PixelPerfect designer

   ![The 'Field List' menu expanded from the right side panel in the PixelPerfect designer](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-gen-field-list.png "Click to view full size")
3. Hover your cursor over Levels, and then click ![Plus](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg).
4. Expand Fields. Click ![Plus](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) next to Region. The data binding is created.
5. You are brought back to the main menu in the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List. Hover your cursor over Levels again, and then click ![Plus](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg).
6. Expand the Dashboard sheet. Next to Top 5 Customers, click ![Plus](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg).

   The data binding is created.

### Create the banded structure

In this case, we use the same procedure as the general workflow, but add an extra step at the beginning to define the band that will be used to loop the creation of multiple tables.

Do the following:

1. On the design surface, right-click anywhere within the Detail1 band and click Insert Band > DetailReport.

   A new DetailReport band is inserted below Detail1.
2. Right-click the Detail2 band within the Detail Report band you just created. Click Insert Band > DetailReport.

   A new Detail Report band is inserted and nested within the first Detail Report band you created.
3. Right-click the Detail3 band within the second Detail Report band you just created. Click Insert Band > GroupHeader.

   The band is inserted above the Detail3 band.
4. Right-click the Detail3 band within the second Detail Report band you created earlier. Click Insert Band > GroupFooter.

   The band is inserted below the Detail3 band.

The structure should look like the following image.

Banded structure

![Image of the design surface showing the structure of nested bands that the user needs to create for the example](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-format-table-bands.png "Click to view full size")

### Bind the content to the data sources

We start by binding the top-level DetailReport band to the level on which we want to multiply table creation and filtering. Then, we bind the data source for the table itself.

Do the following:

1. Select the outermost DetailReport band in the structure (DetailReport1).
2. Click the gear icon at the edge of the design surface.

   Clicking the gear icon

   ![Close-up of the side of the design surface with a band selected, and the gear icon clicked, showing a popup menu for different settings](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-format-table-cog.png "Click to view full size")
3. In the menu, select the Region level as the Data Member. This will create a separate table for each region in the application.

   Tip noteAlternatively, click ![Cog wheel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) at the far right of the designer. Add the Data Member under Detail Report Tasks.
4. Next, select the DetailReport2 band, and again click the gear icon at the edge of the design surface.
5. In the menu, select the Top 5 Customers level as the Data Member. This binds the table structure to the chart's source data.
6. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu, and expand Levels.
7. Drag each of the fields within the Top 5 Customers level onto the Detail3 band that is located between the GroupHeader and GroupFooter.
8. Arrange the field items on the band so they resemble two adjacent rows in a table.

   Tip note

   To align objects precisely with the grid, resize them manually until they are as close to grid lines as possible. Then, right-click each object and select Layout > Size to Grid. You can also open the ![Cog wheel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties menu and adjust their size values numerically under Layout > Size.

   For more information, see [*Arranging content in your PixelPerfect report template*](pixelperfect-arrange-content.htm).
9. We need to format the Sales values as currency figures. Click the Sales label, and then click the gear icon that appears next to it.
10. In the popout menu, click the ellipsis (three dots) menu under Text Format String.
11. The Format String Editor dialog opens. Choose Currency, and adjust the decimal points. Click OK.

    Configuring number formatting

    ![The Format String Editor dialog showing the options available for formatting text content](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-format-table-numbers.png "Click to view full size")
12. Resize the Detail3 band, shrinking it so that it is only as small as the items in it.

    Labels containing Customer and Sales fields added to the template

    ![Template showing two labels, for Customer and Sales fields, in the Detail3 band. These labels are populated with data when the report is generated](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-format-table-rows.png "Click to view full size")

### Add titles and column headers

Add titles and table headers within the GroupHeader band by dragging objects onto the design surface.

Do the following:

1. Let's add a title for the level controlling the creation of separate tables. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu, and expand Levels.
2. Expand the Region level, and drag the Region field within it onto the Detail2 band.
3. Customize font properties in the ![Cog wheel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties menu under Appearance > Font.
4. Resize the object as desired and then change the band size so that the objects take up the entire band height.
5. Next, let's add column headers. From the toolbox on the left side of the designer, drag two ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_text.svg) Label objects (one for each column) onto the GroupHeader1 band.
6. Arrange the labels at the top of the GroupHeader1 band so that they are the same length as the table row labels.
7. Double-click each label and insert your own custom fixed text. In this case, you can use the field names.
8. Customize font as desired. For example, you might want columns headers to stand out, so you could make them bold.
9. Change the band size so that the objects take up the entire band height.
10. For the purposes of this example, reduce the sizes of the TopMargin1 and Detail1 bands.

    Report template after adding table titles and headers

    ![Template with the level (Region) title label and column headers (Customer, Sales) added](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-format-table-headers.png "Click to view full size")

Click Save template, and then click Preview report. Download the report and open it to see how it looks so far.

First report preview for the example

![Previewed report showing a series of highly formatted tables with section and column headers](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-format-table-first-preview.png "Click to view full size")

### Add calculated totals for a column

You can add calculated sales totals into the GroupFooter.

Do the following:

1. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu, and expand Levels.
2. Expand the Top 5 Customers level, and drag the Sales field within it onto the GroupFooter1 band.
3. To set the total to be calculated for a group, open the ![Cog wheel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties menu for the label and expand Text > Summary. Select Group in the Running drop down menu.

   Configuring group calculation for the totals row

   ![Designer interface showing a totals label added, along with the Properties for configuring the total calculations shown on the right side](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-format-group-calc.png "Click to view full size")
4. Click the bold f icon on the bottom right corner of the label to open the Expression Editor.
5. In the Expression Editor, expand the Functions node, select Summary, and double-click on sumSum(). The function is placed into the formula space. Be sure to include the field name between the parentheses. Click OK.

   Using a summary function in the Expression Editor

   ![Expression Editor dialog showing an expression entered for summarizing aggregations](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-format-table-exp-edit.png "Click to view full size")
6. Resize and reposition the label to be consistent with the other elements, and set its Text Format String and font as desired.
7. Reduce the size of the GroupFooter1 band. You might want to leave a bit more extra space on the bottom of the band to add spacing between each table in the level.
8. Save the template and run a preview.

Second preview for the example

![Previewed report showing the next version of the highly formatted table, which includes a total calculation at the bottom of each table](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-format-table-second-preview.png "Click to view full size")

### Add conditional formatting

It is possible to create conditional formatting rules with the Expression Editor. For example, you could highlight sales values under $200,000 in red.

Do the following:

1. Select the Sales label (not the sumSum([Sales]) label).
2. Click the bold f icon on the bottom right corner of the label to open the Expression Editor.
3. In the left side panel, click Foreground Color, expand the Functions tree in the bottom menu, and select Logical.
4. Double-click Iif(, ,) to insert the function into the editor.
5. In the expression, before the first comma, enter [Sales].
6. You can select Operators in the bottom menu and double-click on the < symbol. Alternatively, enter the symbol by typing it into the editor. Then, type 200000.
7. Next, reposition your cursor to just after the first comma. Define how to format the text when the condition is true. Select Values in the bottom menu, and scroll down until you reach Red.
8. Double-click Red to insert it.
9. Repeat the process for the text after the second comma, but instead select a value of Black. This is shown when the condition is false.
10. You should have the following formula:

    ```
    Iif( [Sales] < 200000, 'Red' , 'Black' )
    ```
11. Click OK.
12. Save the template and run a preview.

Third preview for the example

![Previewed report showing the next version of the report, including conditional formatting to color certain rows as red depending on sales values](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-format-table-third-preview.png "Click to view full size")

### Add a calculated column

You can create a calculated column with the percentage of each row calculated with respect to the total sales.

Do the following:

1. We first need to create a new field to store the total sales. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu, and expand Levels.
2. Next to the Top 5 Customers level, click the button for Add calculated field.

   Adding a calculated field

   ![Cropped image showing the icon to add a calculated field, which appears when hovering over a level you have created in the 'Field List' menu](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-format-table-add-calc-field.png "Click to view full size")
3. For the newly created calculatedField1, click the pencil icon to edit it.
4. Insert TotalSales as the Name, and click on the ellipsis (three dots) icon on the right of Expression.
5. Insert this expression into the Expression Editor:

   ```
   [].Sum( [Sales] )
   ```

   Tip noteThe expression can also be added with the menu by clicking Aggregate under Functions, and double-clicking Sum(). Finally, click Fields and double-click Sales.
6. Click OK.
7. From the toolbox panel on the left, draft a ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_text.svg) Label object onto the Detail3 band. Place it to the right of the Sales field.
8. Open the Expression Editor for the label, and insert the following formula:

   ```
   [Sales] / [TotalSales]
   ```
9. Click OK.
10. Click on the gear icon that appears next to the new label and insert this Text Format String:

    ```
    {0:0.00 %}
    ```
11. With the label selected, open the ![Cog wheel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties menu.
12. Under Appearance, switch the horizontal Text Alignment to right-aligned.
13. Further configure the font, and adjust the size and positioning of the label.
14. Add another column header label and align it above the new column (see [*Add titles and column headers*](#AddHeaders) for instructions). Add the fixed text Perc. for the label.

    Final look at the template before preview

    ![Template with calculated column, and its associated column header, added to the right of the existing columns already created](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-format-table-final-template.png "Click to view full size")
15. Save the template and run a preview of the final report.

Final preview for the example

![Previewed report showing calculated percentage-based column added to the report](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-format-table-final-preview.png "Click to view full size")
