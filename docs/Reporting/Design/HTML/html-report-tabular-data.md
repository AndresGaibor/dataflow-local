---
title: "Adding tabular data to your HTML template"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/HTML/html-report-tabular-data.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing HTML report templates", "Adding content to your HTML report template"]
---

# Adding tabular data to your HTML template

You can add the source table from a chart in your application as tabular data in your HTML report template. Tabular data can be added either as an entire table or as one or more individual columns. Whether you add a chart as a single table tag or as a set of individual columns, the underlying object you create is a table. The table is added as an object in the objects panel, which you can return to at any time for editing and reuse.

Charts with straight type hypercubes can be added as tabular data. When you add a chart as a table, the underlying fields representing the chart's data are added as columns to the report.

You add tabular data in the ![Tables](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_outline.svg) Tables menu of the objects panel.

When selecting a table, refresh the list of available tables from the application by clicking ![Reload](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_reload.svg).

## Adding an entire chart

You can add an entire chart in tabular form with a single tag. The chart data is inserted in the report as a straight table.

Do the following:

1. In the HTML designer, place your cursor at the location in the code at which you want to insert the table.
2. Click ![Tables](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_outline.svg) in the objects panel.

   Tables menu in the objects panel within the HTML designer

   !['Tables' menu in HTML designer, from which you can modify existing tables you have added, or add a new table](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_html-add-table-objects-panel.png "Click to view full size")
3. Click Add table. A list of available sheets appears.
4. Expand the sheet containing the chart you want to add as a table. You can search the chart's name to refine the list of sheets if needed.

   You can preview the chart before adding it by clicking the chart's name.
5. Click the ![Plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) icon next to the chart.
6. In the drop down menu, select Table. This inserts the chart as a single item in the template.

   Selecting a chart to add as a table

   ![Selecting a chart to use as the source for the table](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_html-add-table-select-chart.png "Click to view full size")
7. In the objects panel, you can adjust:

   - Name: Provide a unique name to the table so you can identify it later.
   - Description (optional): Add a description to the object if desired.
   - Filter: Add up to one filter to the object individually. This allows you to customize the data used in the table without affecting the data used in other template objects. Click Manage filters to configure the report filter you want to use. For more information about object-level filters, see [*Using object-level filters in report templates*](../../Generate/cloud-in-app-reports-filters.htm#ObjectLevel).

   Template design surface with table added as a single tag

   ![Tag representing an entire table shown in the HTML template](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_html-add-whole-table-result.png "Click to view full size")
8. You can adjust the properties of the table in the objects panel. For information about formatting properties for tabular data, see [*Formatting properties for tabular HTML data*](html-report-tabular-properties.htm).
9. You can re-use the table object at any time. Open ![Tables](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_outline.svg) in the options panel, and click ![Right-directional arrow](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_direction_right.svg) to open the object. Click Add table tag to add the table again.

## Adding a chart by column

A chart can also be added in tabular form as a set of single columns. This allows increased control over formatting within the report template.

The chart data is inserted in the report as a straight table.

Do the following:

1. In the HTML designer, place your cursor at the location in the code at which you want to insert the table columns.
2. Click ![Tables](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_outline.svg) in the objects panel.

   Tables menu in the objects panel within the HTML designer

   !['Tables' menu in HTML designer, from which you can modify existing tables you have added, or add a new table](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_html-add-table-objects-panel.png "Click to view full size")
3. Click Add table. A list of available sheets appears.
4. Expand the sheet containing the chart you want to add as a table. You can search the chart's name to refine the list of sheets if needed.

   You can preview the chart before adding it by clicking the chart's name.
5. Click the ![Plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) icon next to the chart.
6. In the drop down menu, select Individual columns.

   Selecting a chart to add as a table by column

   ![Selecting a chart to use as the source for the table, and adding it as a set of one or more individual columns](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_html-add-table-as-columns-select-chart.png "Click to view full size")
7. Select the columns you want to add, or click All to insert all columns from the chart.
8. The chart is added to the template as an table element, with each column denoted in the td element within it. If you add a single column, the column is instead added as a single item, [in the same way an entire table is added](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/html-report-tabular-data.htm#FullChartTable).

   In the objects panel, you can adjust:

   - Name: Provide a unique name to the table so you can identify it later.
   - Description (optional): Add a description to the object if desired.
   - Filter: Add up to one filter to the object individually. This allows you to customize the data used in the table without affecting the data used in other template objects. The filter is applied to all columns from the same source table.

     Click Manage filters to configure the report filter you want to use. For more information about object-level filters, see [*Using object-level filters in report templates*](../../Generate/cloud-in-app-reports-filters.htm#ObjectLevel).

   Template design surface with table added as a series of individual columns

   ![Item representing a chart added as a series of individual columns](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_html-add-table-as-columns-result.png "Click to view full size")
9. You can adjust other properties of the table in the objects panel. For information about formatting properties for tabular data, see [*Formatting properties for tabular HTML data*](html-report-tabular-properties.htm).
10. You can re-use the table object at any time. Open ![Tables](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_outline.svg) in the options panel, and click ![Right-directional arrow](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_direction_right.svg) to open the object. Click Add table tag to add a new instance of the table as a single item, or create a blank table structure and add each column reference individually into the td elements.

The set of columns is considered a single table object.

## Adding more columns from a chart

### Into a chart added by column

After adding some columns of a table individually, you can add more at any time. The required procedure depends on whether the original table consists of one column, or two or more columns.

#### Table with one existing column

If you have a table with just one column added individually, the process for adding new columns is more involved. In some cases, it might be easier to recreate the object by configuring multiple columns from the beginning. However, you can still add additional columns to a single-column table.

Do the following:

1. On the design surface, paste the following blank table element into an empty area:

   ```
     <table cellspacing="0" style="border-collapse: collapse">
     <tbody><tr>
     <td></td><td></td><td></td>
     </tr>
     </tbody></table>
   ```
2. Cut and paste the existing item for the individual column into one the td elements you just added. For example:

   ```
     <table cellspacing="0" style="border-collapse: collapse">
     <tbody><tr>
     <td>%%ProductCategory%%</td><td></td><td></td>
     </tr>
     </tbody></table>
   ```
3. Place your cursor on the existing individual column item.

   In the objects panel, the Tables menu opens with the column expanded.
4. Find the column you want to add under Columns. Expand it, configure its properties, and then click Add column tag.
5. Repeat steps 3 to 4 for each new column you want to add from the source table. You will need to add new <td></td> items as needed, and remove all unused (empty) <td></td> items before finishing.

When this procedure is performed, the table remains the same table object that is available from the objects panel.

#### Table with two or more existing columns

Do the following:

1. In the HTML code, select the td element for the column directly to the left of where you want to insert a column.

   In the objects panel, the Tables menu opens with the column expanded.
2. Create a new td element by pasting the following into your template:

   ```
   <td></td>
   ```

   Then, place your cursor between its opening and closing tags.
3. In the objects panel, configure the formatting properties for your column, and then click Add column tag.

   The reference to the column is inserted into the blank td element.

### From a chart added as entire table

You can add new instances of a chart that has already been added as a single table item. You can also add instances of individual columns that you originally added as a single table item.

Do the following:

1. In the HTML designer, place your cursor at the location in the code at which you want to insert the content.
2. Click ![Tables](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_table_outline.svg) in the objects panel.

   The Tables menu opens.
3. Click ![Right-directional arrow](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_direction_right.svg) next to the existing object.
4. Do one of the following:

   1. To add a new instance of the table as a single item, click Add table tag.
   2. To add single columns, click Expand columns. Configure the column properties and click Add column tag. If adding more than one column into a structure, you will need to create a blank table element first. See [*Table with one existing column*](#OneExisting).
