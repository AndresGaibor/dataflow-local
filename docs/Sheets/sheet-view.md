---
title: "Sheet view"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Sheets/sheet-view.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Understanding applications", "Navigating in the application interface"]
---

# Sheet view

Application developers add [visualizations](#glossary-0 "Glossary term") and other elements to [sheets](#glossary-1 "Glossary term") in an application. Application consumers interact with the sheet for data analysis. Application developers and application consumers can interact with Insight Advisor to generate visualizations using natural language queries.

Click Sheets in the assets panel to select and open a sheet.

Develop sheets in edit mode. Interact with sheets in analysis mode. Explore your data with [Insight Advisor](#glossary-3 "Glossary term") in Insight Advisor.

Information noteYour user interface may look different from the interface shown in the screenshots below. For example, the application creator may have hidden the toolbar or sheet header. For more information, see [*Hiding toolbar, sheet header, and application navigation bar options*](../Apps/style-app.htm#Hiding).

## Toolbar

The toolbar contains options to create and navigate in your sheet and application. Within the toolbar, the selections bar contains options to make selections in your data and to clear those selections, and to search for data. The selections tool also displays all selections that have been made. The following buttons are available in the toolbar:

- Assets: Open or close the assets panel.
- Sheets: Open the assets panel to Sheets.
- Bookmarks: Open the assets panel to Bookmarks.
- ![Insight Advisor](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cognitive.svg): Open or close Insight Advisor.
- Smart search (![Smart search](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_selections_search.svg)): Search the entire dataset in your application.
- Selection buttons:

  - Step back(![Step back](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_selections_back.svg)): Step back in the current selection.
  - Step forward(![Step forward](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_selections_forward.svg)): Step forward in the current selection.
  - Clear all selections (![Clear all selections](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_clear_selections2.svg)): Clear all selections.
- Selections tool (![Selections tool](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_selections_tool.svg)): Open or close the selections tool
- Edit sheet: Open or close the edit mode. If the sheet cannot be edited, click Duplicate to edit a duplicate of the sheet.

## Edit

Click Edit sheet to edit a sheet.

Sheet view in edit mode

![Sheet view in edit mode.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Sheets/ui_gen_sheet_edit-cloud.png "Click to view full size")

You can do the following:

- Click Sheets to add a new sheet, or to navigate to a sheet.
- Click Assets to open the assets panel. Add assets to your sheet. For example, you can add a visualization to a sheet.

  For assisted creation of visualizations, click Use assisted explore to use Insight Advisor. See: [*Creating visualizations with Insight Advisor*](../Insights/insight-advisor-create-visualizations.htm)
- Click Properties to open the properties panel. Configure the properties for a sheet or visualization. For example, you can add dimensions and measures to a visualization. See: [*Properties*](#Properti2)

### Assets panel in edit mode

In edit mode, the assets panel contains:

- Sheets: View and edit sheets in the application.

  You can view all sheets in an application, or just the public, community, or private sheets.

  [*Working with sheets*](working-with-sheets.htm)
- Bookmarks: View and edit bookmarks in the application.

  You can view all bookmarks in an application, or just the public, community, or private bookmarks.

  [*Bookmarking selections*](../Bookmarks/keep-track-of-important-data.htm)
- Insight triggers: Define metrics to be used for insight generation in [feeds](#glossary-4 "Glossary term").

  [*Working with Discovery Agent insight triggers*](../DiscoveryAgent/insight-triggers.htm)
- Fields: Add data to visualizations from available fields.

  [*Using data assets in visualizations*](../Visualizations/data-in-your-visualization.htm)
- Master items: Add data to visualizations from available master items.

  [*Reusing assets with master items*](../Assets/work-with-master-items.htm)
- Charts: Add visualizations to the sheet.

  [*Working with visualizations*](../Visualizations/working-with-visualizations.htm)
- Analyses: Add analyses to the sheet.

  [*Creating and editing analyses*](../Analyses/creating-analyses.htm)
- Custom objects: Add custom objects to the sheet.

  [*Creating a visualization using a custom object*](../Visualizations/create-visualization-extensions.htm)
- App navigation links: Add links to build on-demand applications.

  [*Building an on-demand application*](../LoadData/creating-OnDemand-app.htm)
- Dynamic views: Connect a base application to a template application to use master visualizations from that application as dynamic charts in your sheets.

  [*Managing data with dynamic views*](../DynamicViews/dynamic-views.htm)

Assets panel in edit mode

![Asset panel with Charts selected.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Sheets/ui_sheet-assets-rev4.png "Click to view full size")

#### Fields

Fields represent the data that is available in your application. Drag a [field](#glossary-5 "Glossary term") under Data in Properties to add data to visualizations. Fields are marked with different icons to display what kind of data source they are classified as.

| Icon | Data type | Definition |
| --- | --- | --- |
| Number | Numeric data | Data containing only numeric values |
| Textr | Text strings | Data containing text strings |
| Date and time | Date and time | All date fields are marked with Date and time and can be expanded to use date and time attributes of the field. Date and time attributes are created automatically when you use [Data manager](#glossary-6 "Glossary term"). If you used [Data load editor](#glossary-7 "Glossary term") to load data, you need to create the date and time attributes using derived fields.  See: [*Date & time fields*](../Assets/date-time-fields.htm) |
| Geographic data | Geographic data | All fields recognized as geopoints or geoshapes in map visualizations are marked with Geographic data.  See: [*Loading your own map data*](../Visualizations/Map/load-map-data.htm) |

Additionally, right-click on fields to do the following:

- Create a new master dimension. See: [*Creating a master dimension from a field*](../Dimensions/create-master-dimension-from-field.htm)
- Create a new master measure. See: [*Creating a master measure from a field*](../Measures/create-master-measure-field.htm)
- View field settings. See: [*Always one selected value*](../DataSource/select-single-value.htm)

#### Master items

Create [dimensions](#glossary-8 "Glossary term") and [measures](#glossary-9 "Glossary term") as master items that can be re-used in your application.

Some master items may have associated glossary terms. You associated terms and their definition by clicking on the [master item](#glossary-10 "Glossary term") and hovering your cursor over the term. You can click on the term to view the full glossary entry for the term.

Master item with linked term

![The master measure Gross margin open showing the term for gross margin from the glossary.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_businessGlossary_master_measure.png "Click to view full size")

See:

- [*Reusing visualizations with a master visualization*](../Visualizations/create-master-visualization.htm)
- [*Reusing dimensions with master dimensions*](../Dimensions/create-master-dimension.htm)
- [*Reusing measures with master measures*](../Measures/create-master-measure.htm)

#### Charts

Drag [charts](#glossary-11 "Glossary term") onto your sheet to create visualizations.

See: [*Get started with visualizations*](../Visualizations/get-started-with-visualizations.htm)

#### Custom objects

Enhance your applications with custom-designed visualizations.

See: [*Creating a visualization using a custom object*](../Visualizations/create-visualization-extensions.htm)

#### Application navigation links

Build on-demand applications using application navigation links. On-demand applications load a subset of the data that is loaded in aggregate form by a selection application.

See: [*Building an on-demand application*](../LoadData/creating-OnDemand-app.htm)

#### Dynamic views

Create [dynamic views](#glossary-12 "Glossary term") to query and view relevant subsets of large data sets in charts that can be dynamically refreshed as [selections](#glossary-13 "Glossary term") are made.

See: [*Managing data with dynamic views*](../DynamicViews/dynamic-views.htm)

#### Variables

Click ![Variables](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_variables_outline.svg) to open the variables dialog.

See: [*Variables dialog*](variables-dialog.htm)

### Source table

You can preview data in the source table viewer. This allows you to view fields and values from the selected table in your application data. You can select values from the table to apply selections. You can show or hide the source table viewer by clicking Source table. You can pin it open by clicking ![Pin data preview](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_pin_outline.svg).

Source table viewer

![Source table viewer showing a table](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Sheets/ui_data-source-viewer-edit.png "Click to view full size")

### Properties

Configure properties for a sheet or visualization in the properties panel.

Click Properties in the toolbar of a sheet to open the properties panel. You have to be in edit mode.

Click on the sheet to view the properties for the sheet. Click on a visualization to view the properties for the visualization. The properties panel can be resized by clicking and dragging the border of the properties panel.

For sheets you can:

- Edit sheet title and description
- Add a thumbnail for a sheet
- Add a background color or image to a sheet
- Change the grid spacing, sheet size, and layout
- Apply alternate states to the sheet
- Add actions triggered when users navigate to the sheet

Depending on the visualization that you are editing, you have different options. Typically, you can do the following:

- Add dimensions and measures and specify how they are displayed
- Set the sorting order and sorting criteria
- Change the way the visualization appears
- Configure custom tooltips

See: [*Creating and editing visualizations*](../Visualizations/create-visualizations-overview.htm)

## Analysis

Interact with visualizations and data in a sheet.

Sheet view in analysis mode

![Sheet view in analysis mode.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_sheet_mode-analysis.png "Click to view full size")

You can do the following:

- Click Assets to create and manage assets for exploration of application content. This is a different assets panel than the one you see when you are editing a sheet. For more information about the assets panel in edit mode, see [*Assets panel in edit mode*](#Assets).
- Make selections in a visualization to explore insights based on selections. See: [*Exploring with selections*](../Selections/SelectionsToolbar/work-with-selections.htm)
- Create bookmarks based on selections. See: [*Bookmarking selections*](../Bookmarks/keep-track-of-important-data.htm)
- Smart search (![Smart search](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_selections_search.svg)): Search the entire dataset in your application. See: [*Using smart search*](../Search/use-smart-search-tool.htm)
- Click ![Insight Advisor](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cognitive.svg) to open Insight Advisor and generate recommendations for visualizations using natural language and simple configuration options. See: [*Insight Advisor*](#_bm)

Selection actions

| User interface item | Action |
| --- | --- |
| Selections - History | Step back in [selections](#glossary-14 "Glossary term"). |
| Selections - step forward | Step forward in selections. |
| Selections - Clear all | Clear all selections. |
| Selection search | Open smart search to search in the entire data set.  For more information, see: [*Using smart search*](../Search/use-smart-search-tool.htm) |
| Selections tool | Open the selections tool, which is an extension of the selections bar. |

### Assets panel in analysis mode

In analysis mode, click Assets to open a panel where you can create and manage the following:

- Sheets: View and navigate sheets in the application. Create and group sheets.

  You can view all sheets in an application, or just the public, community, or private sheets.

  [*Working with sheets*](working-with-sheets.htm)
- Bookmarks: View and navigate bookmarks in the application. Create new bookmarks.

  You can view all bookmarks in an application, or just the public, community, or private bookmarks.

  [*Bookmarking selections*](../Bookmarks/keep-track-of-important-data.htm)
- Insight triggers: Define metrics to be used for insight generation in [feeds](#glossary-15 "Glossary term").

  [*Working with Discovery Agent insight triggers*](../DiscoveryAgent/insight-triggers.htm)
- Notes: Capture and share insights.

  [*Capturing and sharing insights using Notes*](../Notes/notes-overview.htm)
- Key driver analysis: Create, manage, and view key driver analyses.

  [*Uncovering the key influencers behind your data using key driver analysis*](../KeyDrivers/introduction-key-driver-analysis.htm)
- Reports: Generate on-demand reports based on activated [templates](#glossary-16 "Glossary term"). This section is not visible unless at least one template has been activated for on-demand report generation.

  [*Creating on-demand reports*](../Reporting/OnDemand/reports-on-demand-create.htm)

The assets panel can be resized by clicking and dragging the border of the assets panel. To pin the assets panel open in analysis mode, click ![Pin assets](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_pin_outline.svg).

You can make Sheets or Bookmarks full screen by clicking ![Full screen](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_maximize.svg).

You can view Sheets as a grid or list. Sheets can also be grouped together. For more information, see [*Grouping sheets*](grouping-sheets.htm).

Assets panel in analysis mode

![An open assets panel showing the sheets in the app.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Sheets/ui_assets-analysis_cloud-panel.png "Click to view full size")

## Options menu

You can use the options menu to perform actions related to the visualization.

Options menu next to a chart

![Options menu for a chart.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Sheets/ui_options-menu-chart.png "Click to view full size")

You can open the options menu by:

- Right-clicking on a chart.
- Clicking the hover menu ![More](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg).

Menu options will be different depending on:

- Whether you are editing or analyzing (viewing) charts in an application.
- The chart type.
- The privileges that have been assigned to you by your administrator.
- Custom settings for visualization menus that have been configured by the application developer (see [*Hiding items in visualization menus*](../Apps/style-app.htm#HidingContext)).

Options menu for a chart with hover menu expanded

![Options menu when the 'more' icon next to a chart is selected.](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen-options-menu-opened-cloud.png "Click to view full size")

The menu looks different if you have touch screen mode enabled on a supported device. You can toggle touch support on and off by clicking or tapping the application navigation button (![Navigation](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg)) and using the toggle for ![Touch screen mode](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_touch_outline.svg) Touch screen mode.

### Options

Some of the available actions you might see in the options menu include:

Actions from the options menu

| Option | Sheet modes | Available actions |
| --- | --- | --- |
| Expand Full screen | Edit, analysis | Expand visualization to full-screen mode. |
| Insight triggers Create insight trigger | Edit, analysis | Configure [insight triggers](#glossary-17 "Glossary term") to set calculation conditions that are evaluated when data changes. Insight triggers help to identify anomalies and changing data, presenting insights in the form of a scrollable [feed](#glossary-18 "Glossary term").  See: [*Working with Discovery Agent insight triggers*](../DiscoveryAgent/insight-triggers.htm) |
| Key driver anaylsis Key driver analysis | Edit, analysis | Configure a key driver analysis using a measure or compatible dimension from the chart as the target. Add other dimensions and measures as features to compare their relative influence on the target. See: [*Uncovering the key influencers behind your data using key driver analysis*](../KeyDrivers/introduction-key-driver-analysis.htm) |
| Info icon Show details | Analysis | Show details: See the fields and master items that make up the visualization. You can view their dependencies to see the fields that comprise them and their sources, as well as any linked glossary terms.  Details can be turned on and off for visualizations in the visualization properties panel under Appearance > General > Show details.  For more about Details, see [*Viewing details for visualizations*](../UserInterface/show-details.htm). |
| Controls Exploration menu | Analysis | Change certain visualization properties, without making selections or editing the sheet. See: [*Visual exploration*](../UserInterface/visual-exploration-menu.htm)  Exploration menu is not available for analyses. |
| Table View data | Analysis | View the data for a visualization in a table.  View data offers an accessible option for viewing information in charts that are not optimized for accessibility. For more information about accessibility, see:   - [*Accessibility*](../UserInterface/accessibility.htm) - [*Best practices for designing accessible applications*](../Apps/accessibility-analytic-apps.htm)   View data is not available for analyses. |
| Forward Share | Analysis | Share the visualization in different ways, for example as an image, a link, or an embedded object. |
| Alert Alerts | Analysis | Create an alert for the data in the visualization, or open an existing alert that is already created for it. See: [*Monitoring data with alerts*](../Alerting/monitoring-changes-with-alerts.htm) |
| Mail Subscribe | Analysis | Subscribe to the visualization to receive automated reports indicating its current appearance and data. See: [*Scheduling reports with subscriptions*](../Reporting/Subscriptions/Subscription-reports.htm) |
| Analyze Monitor in activity centers | Analysis | Add the chart to your Qlik Cloud Analytics [activity center](#glossary-19 "Glossary term") for quicker access without opening the source application.  See: [*Monitoring visualizations*](../Hub/monitor-charts-hub.htm) |
| Note Notes | Analysis | Access the possible actions related to notes for the visualization. Your options might include Create note with snapshot, Find notes related to this chart, and Add snapshot to note. See: [*Capturing and sharing insights using Notes*](../Notes/notes-overview.htm) |
| Storytelling Storytelling snapshots | Analysis | Manage the storytelling snapshots available for the chart. For example, you can Take snapshot or access the Snapshot library. See: [*Collecting insights for stories using snapshots*](../StoryTelling/Story/collect-insights-for-story.htm) |
| Download Download | Analysis | Download the visualization in different formats, such as an image, PDF, or data file. |
| Link Add to master items, Unlink visualization | Edit | Add the visualization as a master visualization so it can be reused by you and other application developers. You can also unlink the chart from an existing master visualization. See: [*Reusing visualizations with a master visualization*](../Visualizations/create-master-visualization.htm) |
| Scissors Cut, Copy Copy, Paste Paste, Paste Paste and replace | Edit | Standard actions allowing copying and pasting of visualizations across sheets.  Cut, Copy, Paste, and Paste and replace are not available for analyses. |
| Garbage can Delete | Edit | Delete the visualization from the sheet. |
| Copy Copy style, Paste Paste style | Edit | Copy the custom styling for a visualization and paste it onto another visualization. See: [*Copying and pasting visualization styling*](../Visualizations/style-visualization.htm#Copying) |

## Insight Advisor

Click ![Insight Advisor](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cognitive.svg) to access Insight Advisor Search and Insight Advisor Analysis Types. You can ask a question in the Insights search field to generate visualizations with Insight Advisor Search.

Insight Advisor

![Insight Advisor open in a sheet](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen-insight-advisor_saas-rev3.png "Click to view full size")

For more information, see [*Creating visualizations with Insight Advisor*](../Insights/insight-advisor-create-visualizations.htm).

## Touch gestures in sheet view

Touch gestures

| Touch gesture | Action |
| --- | --- |
| Long-touch and release | Open the shortcut menu |
| Long-touch a visualization | Open the options menu |
| Swipe | Scroll lists and visualizations |
| Pinch | Zoom in or out on visualizations |
| Two-finger tap | Select an interval in a list, table or bar [chart](#glossary-20 "Glossary term") axis |
| Two-finger swipe | Pan a scatter plot visualization |
| Three-finger tap | Reset the zoom level of a scatter plot visualization |

Related learning:

- [Using the Default Sheet Editing View in the Cloud](/lnk/Using_default_sheet_editing_Cloud)
- [How do I configure charts using the simplified authoring interface?](/lnk/How_configure_charts_simplified_authoring)
