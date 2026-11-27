---
title: "Example - Applying filtering to a table"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/PixelPerfect/pixelperfect-example-filtered-table.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing PixelPerfect report templates", "Adding content to your PixelPerfect report template", "Visualizing application data in your report", "Creating highly formatted tables"]
---

# Example - Applying filtering to a table

You can add a filtered table to your PixelPerfect report using the PixelPerfect Filter Editor. In this example, you will use the [workflow for creating a highly formatted table](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/pixelperfect-highly-formatted-table.htm), and then edit the Filter String property for the band on which you have added the table.

Refer to the example application sources here: [*Examples - In-application reporting*](../../InAppGeneral/reporting-example-material.htm). Upload the application and data files into a space, and then reload the application. You are ready to complete the example.

## What you will do

In this example, we create a highly formatted table that is filtered to only show the sales for product types with sales exceeding $5,000,000.00.

## Step 1: Create a data binding

Do the following:

1. Create a new PixelPerfect template.
2. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu available from the right-side panel in the designer.

   Field List menu in the PixelPerfect designer

   ![The 'Field List' menu expanded from the right side panel in the PixelPerfect designer](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-gen-field-list.png "Click to view full size")
3. Hover your cursor over Levels, and then click ![Plus](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg).
4. Expand the Sales Tables sheet. Next to Sales by Product Type, click ![Plus](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg).

   The data binding is created.

## Step 2: Create the banded structure

We create a basic structure of bands that will contain the table.

Do the following:

1. On the design surface, right-click anywhere within the Detail1 band and click Insert Band > DetailReport.

   A new DetailReport band is inserted below Detail1.
2. Right-click the Detail2 band within the Detail Report band you just created. Click Insert Band > GroupHeader.

   The band is inserted above the Detail2 band.

## Step 3: Bind the content to the data source

Do the following:

1. Select the outermost DetailReport band in the structure (DetailReport1).
2. Click the gear icon at the edge of the design surface.

   Clicking the gear icon

   ![Close-up of the side of the design surface with a band selected, and the gear icon clicked, showing a popup menu for different settings](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-format-table-cog.png "Click to view full size")
3. In the menu, select the Sales by Product Type level as the Data Member.

   Tip noteAlternatively, click ![Cog wheel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) at the far right of the designer. Add the Data Member under Detail Report Tasks.
4. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu, and expand Levels.
5. Drag each of the fields within the Sales by Product Type level onto the Detail2 band.
6. Arrange the field items on the band so they resemble two adjacent rows in a table.

   Tip note

   To align objects precisely with the grid, resize them manually until they are as close to grid lines as possible. Then, right-click each object and select Layout > Size to Grid. You can also open the ![Cog wheel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties menu and adjust their size values numerically under Layout > Size.

   For more information, see [*Arranging content in your PixelPerfect report template*](pixelperfect-arrange-content.htm).
7. We need to format the Sales values as currency figures. Click the Sales label, and then click the gear icon that appears next to it.
8. In the popout menu, click the ellipsis (three dots) menu under Text Format String.
9. The Format String Editor dialog opens. Choose Currency, and adjust the decimal points. Click OK.

   Configuring number formatting

   ![The Format String Editor dialog showing the options available for formatting text content](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-format-table-numbers.png "Click to view full size")
10. Resize the Detail3 band, shrinking it so that it is only as small as the items in it.

## Step 4: Add column headers

Add column headers within the GroupHeader band by dragging objects onto the design surface.

Do the following:

1. From the toolbox on the left side of the designer, drag two ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_text.svg) Label objects (one for each column) onto the GroupHeader1 band.
2. Arrange the labels at the top of the GroupHeader1 band so that they are the same length as the table row labels.
3. Double-click each label and insert your own custom fixed text. In this case, you can use the field names.
4. Customize font as desired. For example, you might want column headers to stand out, so you could make them bold.
5. Change the band size so that the objects take up the entire band height.

Banded structure for table

![Banded structure for the PixelPerfect table](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-filtered-table-bands.png "Click to view full size")

## Step 5: Filter the table

Do the following:

1. Select the DetailReport1 band, and open the ![Cog wheel](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties menu.
2. Under Detail Report Tasks, click the three-dot icon for Filter String.

   The Filter Editor opens.
3. Move your cursor to the right of the And button. Click the plus symbol that appears.
4. Select Add Condition.

   A condition is created with some default parameters.
5. Change the Product Type field to Sales by clicking on it and using the drop down menu.
6. Change the Equals operator to Is greater than.
7. Select the <enter a value> item, and enter the value 5000000.
8. PixelPerfect Filter Editor with filter added

   ![Filter Editor with condition added in the graphical user interface: Sales Is greater than 5000000](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-example-filter-editor.png "Click to view full size")
9. Click OK.

Click Save template, and then click Preview report. Download the report and open it to see how it looks.

Report preview showing table with product types that have sales in excess of $5,000,000.00.

![Previewed report showing a filtered PixelPerfect table](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-filtered-table-preview.png "Click to view full size")

## Learn more

- [*Filtering data in your PixelPerfect report*](pixelperfect-filter-editor.htm)
