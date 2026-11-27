---
title: "Creating a key driver analysis in Qlik Sense"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/KeyDrivers/use-key-driver-analysis.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "Uncovering the key influencers behind your data using key driver analysis"]
---

# Creating a key driver analysis in Qlik Sense

Key driver analysis is available within a Qlik Sense application. You can create key driver analyses in analysis or edit mode within sheet view. Manage analyses, and view analysis results, in analysis mode within sheet view.

You can create [key driver analyses](#glossary-0 "Glossary term") as an application developer or application consumer. If you have Can view access to an application in a shared space, you can create key driver analyses and begin exploring what is driving the data trends you are interested in. For more information about required permissions and entitlements, see [*Permissions*](#Permissi).

Expand the Assets panel from analysis mode in a sheet, and click ![Key driver analysis](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_key_driver_outline.svg) Key drivers. From here, you can create, view, and manage analyses.

Key driver analyses can be created directly from a visualization or from the assets panel in sheet view.

![Analysis mode in sheet view within an app, showing expanded assets panel and key drivers panel popout, where you create and manage your analyses](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_key-drivers-panel-rev.png "Click to view full size")

Create a new analysis and configure it to include the fields you are looking to analyze. After the analysis runs, you can open it to view and interpret the results.

## Activating key driver analysis in the application

Key driver analysis must be turned on in the application for you to be able to create one. It is turned on by default in applications. To learn how to turn it on or off for your application, see [*Turning off key driver analysis*](key-drivers-off.htm).

## Who can see a key driver analysis?

Key driver analyses that you create in the application are only visible to you.

## Creating and configuring a key driver analysis

You can create a key driver analysis using one of the following methods.

### Creating a key driver analysis in the assets panel

You can create key driver analyses in sheet view when the sheet is in analyze (view) mode.

Do the following:

1. In analysis mode within the sheet view of an application, expand the assets panel if not already expanded.
2. In the assets panel, click ![Key driver analysis](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_key_driver_outline.svg) Key drivers.
3. In the All analyses panel that opens, click Create new analysis.

### Creating a key driver analysis from a visualization

You can also create key driver analyses by interacting with a visualization in the [sheet](#glossary-2 "Glossary term") or [Insight Advisor](#glossary-3 "Glossary term"). When creating an analysis from a visualization on a sheet, you can be in either analyze (view) or edit mode.

Do the following:

1. From sheet view or Insight Advisor, find a [visualization](#glossary-4 "Glossary term").
2. Right-click inside the visualization, or use the ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) button to open its context menu.
3. Click ![Key driver analysis](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_key_driver_outline.svg)Key driver analysis.

### Configuring the key driver analysis

After you use either of the two above methods to create the analysis, you need to configure it by choosing the target and features.

Selecting a target and features for the analysis configuration

![Configuring a key driver analysis by selecting a target and features](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_key-driver-analysis-config.png "Click to view full size")

Before you get started, it is important to gain understanding about what each of the configuration parameters means. For more information, see [*How it works*](introduction-key-driver-analysis.htm#How).

Do the following:

1. Create a new key driver analysis using one of the above procedures.

   The analysis configuration dialog box opens.
2. Under Target, select the target column. This is the field in your application which you are looking to analyze the key drivers for.
3. Confirm the aggregation to use on the target. Use the drop down list to select a standard aggregation.

   For more advanced expressions, you can create a master item and select it directly from the list.
4. Under Features, select at least three features as the key drivers behind the analysis. The features are fields which you might suspect are driving (or not driving) the results seen in the target column data.
5. Click Start analysis.

You are notified if your selected target and features do not provide enough data to be able to perform the analysis, or if another issue results in an unsuccessfully completed analysis.

View the analysis details, and manage it, in the assets panel. For more information, see:

- [*Viewing and interpreting the results of a key driver analysis*](key-driver-analysis-results.htm)
- [*Managing your key driver analyses*](#Managing)

## Managing your key driver analyses

The key driver analyses you create are managed in the assets panel when you are in analysis mode for a sheet. Click ![Key driver analysis](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_key_driver_outline.svg) Key driver analysis to open the All analyses panel.

In this panel, you can view all analyses and open, edit, rerun, and delete them. See later sections on this page for more information on each available action.

The availability of the analyses shown in the panel are determined by the following:

- Editing a key driver analysis creates a new, separate analysis. The original analysis is left in the All analyses panel and will remain accessible.
- Rerunning a key driver analysis does not create a new analysis. The results of the previous run of the analysis are overwritten and will no longer be viewable.

## Viewing and interpreting results

After your analysis has run successfully, you can open it to view the results.

Do the following:

1. In analysis mode within the sheet view of an application, expand the assets panel if not already expanded.
2. In the assets panel, click ![Key driver analysis](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_key_driver_outline.svg)Key drivers.
3. In the All analyses panel that opens, click the analysis to view the results page.

When you open the results page, interpret the meaning of what is shown to improve and enhance your organization’s data awareness and decision making. To learn about how to interpret the results, see [*Viewing and interpreting the results of a key driver analysis*](key-driver-analysis-results.htm).

## Rerunning a key driver analysis

As the data in your application changes with future reloads, you might want to rerun a key driver analysis to get the most current understanding of the forces influencing the target. To do this, you can rerun the analysis. This keeps the existing configuration and runs it again with current data.

Rerunning a key driver analysis does not create a new analysis. The results of the previous run of the analysis are overwritten and will no longer be viewable.

Do the following:

1. Open a sheet in analysis mode.
2. In the assets panel, click ![Key driver analysis](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_key_driver_outline.svg)Key drivers.
3. In the All analyses panel that opens, click ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to the analysis you want to rerun.
4. Click Rerun analysis.

## Editing a key driver analysis

You might want to create a new analysis using a similar but different configuration. To do this, you can edit an existing key driver analysis.

Editing a key driver analysis creates a new, separate analysis. The original analysis is left in the All analyses panel and remains accessible.

Do the following:

1. Open a sheet in analysis mode.
2. In the assets panel, click ![Key driver analysis](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_key_driver_outline.svg)Key drivers.
3. In the All analyses panel that opens, click ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to the analysis you want to edit.
4. Click Edit analysis.

## Deleting a key driver analysis

Do the following:

1. Open a sheet in analysis mode.
2. In the assets panel, click ![Key driver analysis](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_key_driver_outline.svg)Key drivers.
3. In the All analyses panel that opens, click ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to the analysis you want to delete.
4. Click Delete analysis.

## Troubleshooting

When you create an analysis configuration, and later run it, there are various reasons why it might not run successfully. You are notified and possible solutions are provided accordingly.

### Common issues

A common issue is that the dataset created from the analysis configuration contains a subset of the application data rather than the entire data model. The data in the generated dataset depends on the target and features you choose, as well as the selections currently made in the application at the time of configuration. Parts of the data could be excluded or could look different than they might within existing application visualizations which rely on different subsets of data.

Here are some common errors you might encounter when configuring and running the analysis:

- The analysis dataset to be created from the target, features, and application selections does not contain enough data to reliably analyze key drivers.  The data you include must create a table with at least 400 cells.
- The results obtained from the analysis are insignificant, and could be misleading. Therefore, they are not available.
- The selected target contains a constant value across all records in the key drivers dataset.
- The target is based on categories rather than purely numeric data, and at least one unique category in the target appears in less than 10 rows in the generated dataset.
- The data type of the target or one or more features are not classified correctly. For example, you have numeric data that is not being identified as numeric data.
- The included target and features, and possibly the current application selections, produce an analysis [dataset](#glossary-5 "Glossary term") which contains too much data.

### Solutions

You can resolve many of the common issues with your analysis configuration with the following solutions:

- Re-configure the analysis to include different features.
- Change the target of the analysis.
- Revise the selections made in the application at the time you configured the analysis. Increasing or decreasing the available data can help with volume and classification issues.
- Return to data collection and preparation to ensure your data is properly entered and classified. You can return to Data manager, Data load editor, or Script to transform and bin the data so that it meets unique value and category requirements.

Additionally, your analysis might run successfully but the results are not to be considered reliable. For information about how to identify issues in your analysis results, see [*Identifying invalid results*](key-driver-analysis-results.htm#Identify).

## Permissions

To create and manage [key driver analyses](#glossary-6 "Glossary term") in an application, you must have the required roles in the space where the application is located.

- You need to have Can view or higher permissions in the [shared](#glossary-7 "Glossary term") or [managed space](#glossary-8 "Glossary term").
- You cannot use key driver analysis in a managed space if you only have the Can publish, Has restricted view, or Can consume data roles.
- If an application has been shared with you but you don't have corresponding space access, you need Can view access to the application to use key driver analysis.

For more information about the permissions for shared and managed spaces, see:

- [*Managing permissions in shared spaces*](../Spaces/managing-shared-spaces.htm)
- [*Managing permissions in managed spaces*](../Spaces/managing-managed-spaces.htm)

In shared and managed spaces, tenant and analytics administrators cannot create and manage key driver analyses in an application unless they also have the required space or application access.

You can use key driver analysis on an application in your [personal space](#glossary-9 "Glossary term") as long as you have the Private Analytics Content Creator user role in the tenant.

## Learn more

- [*Uncovering the key influencers behind your data using key driver analysis*](introduction-key-driver-analysis.htm)
- [*Viewing and interpreting the results of a key driver analysis*](key-driver-analysis-results.htm)
