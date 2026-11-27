---
title: "Adding a table of contents"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/Design/PixelPerfect/pixelperfect-toc-bookmarks.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Reporting from Qlik Cloud Analytics", "In-application reporting with Qlik Cloud Analytics", "Designing report templates", "Designing PixelPerfect report templates", "Adding content to your PixelPerfect report template", "Preparing your report template for output"]
---

# Adding a table of contents

You can add a table of contents to a header or footer band in your report. Selecting an item in the table of contents will bring the reader to the specified location in the PDF. Create a table of contents using PixelPerfect bookmarks and the ![Unordered list](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_list_outline.svg) Table of Contents object.

Table of contents

![Sample report showing a table of contents, with an entry in the list for each product group](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-table-of-contents-example.png "Click to view full size")

## Bookmarks

PixelPerfect bookmarks help with navigation through the structural arrangement of report elements. In particular, they are used as mappings for tables of contents.

You need to add a bookmark for each item you want to add to your table of contents. You can add a bookmark for essentially any type of data binding available in the designer.

For information about to create a bookmark and link it to a table of contents, see [*Workflow*](#Workflow).

## Table of Contents

The ![Unordered list](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_list_outline.svg) Table of Contents object is available from the toolbox panel on the left side of the PixelPerfect designer. You need to have at least one bookmark in your template for the table of contents to generate correctly.

The Table of Contents displays the text value of each bookmark you add for an object. When you use levels along with an object that is used as bookmark, the Table of Contents will contain a navigation item for each element cycled in the level.

The Table of Contents can only be placed in ReportHeader and ReportFooter bands. You can manually create one of those bands and drag and drop the object onto it. Alternatively, directly drag and drop the object onto the template and the ReportHeader band will be created automatically.

When you add a Table of Contents object, it is automatically separated onto its own pages by page breaks.

## Workflow

This is the recommended workflow for adding a table of contents to your report. Before you begin this workflow, it is assumed that you have at least one object in your report template that can be used as a bookmark.

### Part 1: Create a bookmark

Do the following:

1. Select an object in your template.
2. Click the bold f icon near the object to open the Expression Editor.
3. In the left panel in the Expression Editor, click Bookmark.
4. Enter an expression to define the bookmark.

Alternatively, you can create a bookmark by clicking the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_expression_outline.svg) icon on the right side of the designer. Enter the expression in the Bookmark menu field.

#### Tips for bookmark expressions

The expression you enter for your bookmark depends on what you want displayed in your table of contents.

For example, if the bookmark corresponds to a level created from a field named Product Group, you can type it as follows: [Product Group]

You can also add hard-coded text to the bookmark by typing something like the following: 'This is my hard-coded text'

### Part 2: Create the Table of Contents

Before you start, decide where you want to place the table of contents. If you want to add it in the report header, add a ReportHeader band. If you want to add it to the report footer, add a ReportFooter band.

Do the following:

- From the toolbox panel on the left side of the designer, drag a ![Unordered list](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_list_outline.svg) Table of Contents onto the ReportHeader or ReportFooter band.

After you add the Table of Contents, you can customize its look and feel. Here are some examples:

- Reposition the bar separating the title and contents, to add more or less space between them.
- Change the text of the title. Open the ![Gear](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties menu for the Table of Contents. Expand Behavior > Level Title, and insert your text in the Text box.
- Change the font and other appearance properties for:

  - Title area: Open the ![Gear](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties menu for the Table of Contents. Expand Behavior > Level Title, and configure Font and other settings.
  - Content entries: Open the ![Gear](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties menu for the Table of Contents. Expand Behavior > Level Default, and configure Font and other settings.

## Example - Table of contents with level

Refer to the example application sources here: [*Examples - In-application reporting*](../../InAppGeneral/reporting-example-material.htm). Upload the application and data files into a space, and then reload the application. You are ready to complete the example.

### Preparation: Create content

Create some content by adding a chart image, level, and label.

Do the following:

1. Create a new PixelPerfect template.
2. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu available from the right-side panel in the designer.

   Field List menu in the PixelPerfect designer

   ![The 'Field List' menu expanded from the right side panel in the PixelPerfect designer](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-gen-field-list.png "Click to view full size")
3. Click the plus icon next to Levels.
4. Expand Fields, and click the ![Plus](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) icon next to Region.

   The data binding is added.
5. You are brought back to the main ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu. Click the plus icon next to Images.
6. Expand the Dashboard sheet, and click the ![Plus](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_add.svg) icon next to the Top 5 Customers chart.

   The data binding is added.
7. Right-click the Detail1 band, and then click Insert Band > DetailReport.
8. To bind the DetailReport1 band to the level, select the band and then open the ![Gear](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cogwheel_outline.svg) Properties menu. Under Detail Report Tasks > Data Member, select the Region level.
9. Open the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu, and double-click Levels to expand it.
10. For Region, expand the level object and drag the Region field within it onto the DetailReport1 band.

    Position the label at the top of the band.
11. In the ![Database icon with plus symbol](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_database_add.svg) Field List menu, double-click Images to expand it.
12. Drag Top 5 Customers onto the DetailReport1 band, placing it below the label.

You can customize and style the content as desired.

### Part 1: Create a bookmark

Do the following:

1. Select the Region label you added earlier.
2. Click the bold f icon near the label to open the Expression Editor.
3. Select and copy the expression that is currently shown: [Region (Region\_Level).Region]
4. In the left panel in the Expression Editor, click Bookmark.
5. Paste the copied expression into the editor.

   Creating a PixelPerfect bookmark

   ![The Expression Editor showing the 'Bookmarks' configuration being edited. 'Bookmarks' is selected in the left side panel. The bookmark expression is entered in the editor as well](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-bookmark.png "Click to view full size")

The bookmark is created.

### Part 2: Create the Table of Contents

Do the following:

1. From the toolbox panel on the left side of the designer, drag a ![Unordered list](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_list_outline.svg) Table of Contents onto the design surface.

   The Table of Contents is added on a newly created ReportHeader band.
2. Style the object as desired (for example, you can adjust some of the properties mentioned [here](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Reporting/pixelperfect-toc-bookmarks.htm#Part2)).

   Report template with Table of Contents

   ![Report template showing a ReportHeader band that contains a Table of Contents placeholder. The Table of Contents will draw from the content in the DetailReport band (specifically the 'Region' level)](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-toc-blank.png "Click to view full size")
3. In the top right corner, click Save template.
4. Click Preview report. Download the report and open it.

Report preview with Table of Contents

![Generated report showing the Table of Contents, with items for each region value, along with their page numbers](../../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_reporting-pixelperfect-toc-example.png "Click to view full size")
