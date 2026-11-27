---
title: "Managing data files"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/manage-data-files-spaces.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Adding and managing your analytics data"]
---

# Managing data files

You can manage data files that have been stored locally within Qlik Cloud. The management of data files includes renaming, duplicating, moving, deleting, and adding new data files. Data file management is available for each space in Qlik Cloud.

This help topic focuses on the interface for managing data files in a space. To navigate to this interface, open a space in the catalog and click Space settings > Data files.

Data files interface for managing data files in a space

![Image showing the entire 'Data files' interface, including toolbar, path selector, and table](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_catalog_data-files-space.png "Click to view full size")

## Folder structures in spaces

Each space in Qlik Cloud Analytics contains its own structure of folders organized in a hierarchical fashion. Data files can be organized in a structure of nested folders. For example, within your personal space, you might want to have separate folders for Order Data and Budget Data.

The location of a file or folder within a space is shown in its path. The path uses / symbols to represent when a folder is nested within other folders.

For example, suppose that within your personal space, you have separate folders for Order Data and Budget Data. If you have a data file named Orders\_2024\_December.QVD in your Order Data folder, this file would be located in the following folder path within your personal space:

Personal/Order Data

## Applicable space types

You can organize data files in a hierarchical folder structure in the following types of spaces:

- Personal space
- Shared space
- Managed space
- Data space

### Spaces in Qlik Cloud Analytics

In Qlik Cloud Analytics, data files in personal, shared, and managed spaces can be organized in a hierarchical folder structure.

### Spaces in Data Integration

[Data spaces](#glossary-0 "Glossary term") are commonly used to store output files from Data Integration projects. Data files in data spaces can be used for analytics. From Qlik Cloud Analytics and Qlik Talend Data Integration, you can organize data files in data spaces in hierarchical folder structures. It should be noted, however, that data files in data spaces should only be re-organized into nested folders for the purposes of use in analytics. If a data file that is generated from a data pipeline is relocated to a folder within the data space, the file will continue to be saved to the top-level path in the space (rather than any nested folder) whenever the pipeline is run again.

The behavior for a personal space within Qlik Talend Data Integration is the same as for data spaces.

## Navigation

The Data files section of a space contains tools to help you organize and create file-based data content in the space.

### Toolbar

Toolbar in Data files interface

![Image showing the toolbar in the 'Data files' interface, where you can upload files, create folders, change the view of the table, and perform other actions](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_catalog_data-files-space_toolbar.png "Click to view full size")

The toolbar is located at the top of the interface above the path selector and table. In the toolbar, you can:

- Search for data files in the space.
- Filter files by owner.
- Upload files.

  [*Adding a data file to a space*](#UploadFile)
- Create folders.

  [*Creating folders in the space*](#NewFolder)
- Perform actions on multiple data files at a time.

  [*Performing actions on multiple files and folders*](#BulkActions)
- Change the sorting of the files and folders in your view.

  Change the sorting from the default Last modified option, and toggle between ![Ascending](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_ascending.svg) (ascending) and ![Descending](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_descending.svg) (descending) order.
- Change the appearance of the files and folders in your view.

  Select ![Tree view](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_tree_view.svg) for the hierarchy view, which presents files and folders with indentation to visually display hierarchies. In hierarchy view, you need to select or expand a space to perform actions on specific files or folders.

  Select ![List](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_list.svg) for the list view, where files and folders are shown with a flat structure in the table along with a separate column displaying their specific paths.

### Path selector

The path selector shows you what folder you currently have open. The breadcrumbs show you the folder hierarchy. Select a folder in the path selector to navigate forward or backward in relation to the current path. Select the empty area after the current path to see the folders contained within the current position, and to search for folders.

Path selector in Data files interface

![Path selector in the 'Data files' interface, which allows you to see the current folder shown in the table. This selector also allows you to step backward and forward in relation to the current path, and navigate to folders within the space](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_catalog_data-files-space_path-selector.png "Click to view full size")

### Table

The table shows all the files and folders in the space, or in the selected folder within the space. The table is where you manage the data files and folders. Select folders in the table to navigate to them in the path selector.

In the table, you can also view important information about items, such as their size, number of folders, time of last update, and ownership.

Table in Data files interface

![Table in the 'Data files' interface, which displays all the data files and folders contained within the currently selected path in the space](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_gen_catalog_data-files-space_table.png "Click to view full size")

## Creating folders in the space

Create a folder to organize content in any way you prefer.

Do the following:

1. In a space, click Space settings and select Data files.
2. In the toolbar within the Data files window, click ![New folder](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_new_folder.svg).
3. Define the name of the folder.
4. Under Path, you can choose where in the space's folder structure to add the new folder.
5. Click the path bar and select a containing folder from the drop down menu. Alternatively, type the path of a specific location where you want to add the folder.
6. Click Create.

Alternatively, add a folder by clicking ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to an existing folder in the table and selecting ![New folder](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_new_folder.svg)  Add folder. The new folder is added within the existing folder.

Folders are also automatically created in a space when they are referenced in Store statement. See [*Referencing space folder structure in application and script development*](#FolderStructureRefExamples).

## Performing actions on multiple files and folders

You can use the options in the toolbar to perform the following actions on more than one file or folder at a time:

- ![Scissors](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cut_outline.svg) (Cut)
- ![Copy](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_copy.svg) (Copy)
- ![Paste](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_paste.svg) (Paste)
- ![Trash bin](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin_outline.svg) (Delete)

You can cut, copy, and paste items between spaces or to different locations within the same space. For example, you can cut multiple items and paste them into a different space.

Information note

Cut, copy, and paste actions can be used to move data files from one location to another. When changing file locations for data files referenced in load scripts, the load scripts need to be updated to reflect the new location. For more information, see [*Implications of moving data files used in load scripts*](#EffectsFileMove).

Do the following:

1. In a space, click Space settings and select Data files.
2. In the table, select the items on which you want to perform an action.

   Tip note

   To select more than one item at a time, click the first item, and then use a combination of keyboard commands and clicking to select more files. For example:

   - Hold Shift and click the last item you want to select. This selects all items from the first to last item.
   - Hold Ctrl (Windows) or command (macOS) and click additional items one at a time. This selects each additional item individually.
3. In the toolbar, click an action. The available actions are listed earlier in this section.

When cutting and pasting items between spaces, you need to open the new space and open Space settings > Data files to perform the Paste action.

## Adding a data file to a space

You can add data files to the space.

Data files can be up to 100 GB. However, when uploading very large data files (over 6 GB), you might experience constraints with engine capacity. These constraints are more likely to be encountered with QVD data files due to the memory usage necessary to load QVD files into the engine. For more information about increasing the capacity available, see [*Large application support*](../Admin/large-app-support.htm).

Do the following:

1. In a space, click Space settings and select Data files.
2. In the toolbar within the Data files window, click ![Upload](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_upload.svg) to upload a file.
3. Drag and drop your data files into the Add file dialog.

   Alternatively, click Browse and navigate to your data files.
4. Under Path, you can choose where in the space's folder structure to add the file.

   To add the file to a specific folder, click the path bar and select the folder from the drop down menu. Alternatively, type the path of the specific folder.
5. Click Upload.

Alternatively, click ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to a folder in the table and select ![Upload](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_upload.svg) Upload file to folder.

For additional ways to add data files, see [*Adding datasets*](../DataSource/add-datasets.htm).

## Performing cut, copy, and paste actions on a file or folder

Information note

Cut, copy, and paste actions can be used to move data files from one location to another. When changing file locations for data files referenced in load scripts, the load scripts need to be updated to reflect the new location. For more information, see [*Implications of moving data files used in load scripts*](#EffectsFileMove).

Do the following:

1. In a space, click Space settings and select Data files.
2. In the table, click ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to a file or folder.
3. Click ![Scissors](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Cut, ![Copy](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_copy.svg) Copy, or ![Paste](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_paste.svg) Paste.

   Tip noteAlternatively, you can select a file and use common keyboard shortcuts such as Ctrl+C (Windows) and command+C (macOS).

To perform these actions on more than one file or folder at a time, see [*Performing actions on multiple files and folders*](#BulkActions).

## Renaming a data file or folder

Do the following:

1. In a space, click Space settings and select Data files.
2. In the table, click ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to a file or folder.
3. Click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Rename.
4. Enter the new name for the file and click Save.

Any load scripts that reference the original file or folder name will need to be updated.

### Implications of renaming a data file

Any data file uploaded to Qlik Cloud exists in two forms: the underlying data file and a dataset. In Qlik Cloud, the difference between a data file and a dataset is that the data file is the underlying source for the dataset. When you rename a data file from Space settings > Data files, the name of its dataset may or may not be automatically updated at the same time, depending on whether or not the dataset name has been changed previously.

Updating the name of a data file will require changes to load scripts that use this data file. If you instead want to change only the name of the dataset for this file—that is, the resource that can be opened and analyzed with catalog, lineage, and impact analysis tools—you can instead rename the dataset from areas such as Catalog (general view), Home, Favorites, Collections, or when opening the dataset in Dataset view. Renaming a dataset simply adds an alias to the dataset and does not update the name of the underlying data file. It should be noted, however, that renaming a dataset causes the dataset name to become out of sync with the data file name.

For more information, see [*Distinctions between data files and datasets*](../Catalog/data-files-and-datasets.htm).

## Duplicating a data file or folder

Do the following:

1. In a space, click Space settings and select Data files.
2. In the table, click ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to a file or folder.
3. Click ![Duplicate](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_duplicate_outline.svg) Duplicate.

## Moving a data file or folder

You can move files and folders. Files and folders can be moved to different spaces, or to different locations within the same space.

Do the following:

1. In a space, click Space settings and select Data files.
2. In the table, click ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to a file or folder.
3. Click ![Move](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_direction.svg) Move.
4. Under Path, select a space. This can be the current space or a new space.
5. Reselect the path bar, or click ![Arrow down](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_dropdown_arrow.svg), to define a specific folder within the selected space.

   Alternatively, type the path to define a specific folder.
6. To open to the new location after moving the data file, select Navigate to path.
7. Click Move.

You can also move multiple items at a time. To do this, use the Cut and Paste actions. See [*Performing actions on multiple files and folders*](#BulkActions).

### Implications of moving data files used in load scripts

If you move a data file to a new location within a space, any load scripts that reference that data file need to be updated to reference the new file path. The same consideration applies for files that are moved from one space to another.

For example, suppose the load script of your application or script references the following file in a personal space:

LOAD \* FROM [lib://DataFiles/orders.csv];

Now, suppose that you move the data files to the space TeamSharedSpace and move orders.csv into a new folder in the space, named Sales Analysis. All applications and scripts that load data from orders.csv need to have the file reference updated to the following in the load script:

LOAD \* FROM [lib://TeamSharedSpace:DataFiles/SalesAnalysis/orders.csv];

Otherwise, reloads will fail.

For more information about how to refer to space folder locations in load scripts, see [*Referencing space folder structure in application and script development*](#FolderStructureRefExamples).

## Deleting a data file or folder

Do the following:

1. In a space, click Space settings and select Data files.
2. In the table, click ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to a file or folder.
3. Click ![Trash bin](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin_outline.svg) Delete.

   Tip noteAlternatively, you can select a file and enter Delete on your keyboard.
4. In the dialog, click Delete to confirm the deletion.

You can also delete multiple items at a time. See [*Performing actions on multiple files and folders*](#BulkActions).

## Performing other actions on a data file

In the Data files interface, you can also navigate directly to other tools for performing analysis of a specific file. The following options are available when you use the ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) menu on a file:

- ![Impact analysis](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_impact_analysis.svg) Impact analysis: Investigate the potential effects of making changes to data in the dataset.

  [*Analyzing impact analysis in Analytics*](../Catalog/impact-analysis2.htm)
- ![Lineage](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_lineage.svg) Lineage: Understand more about the history of the dataset.

  [*Analyzing lineage in Analytics*](../Catalog/lineage.htm)
- ![Dataset](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_data_set.svg) Open dataset: Open the file as a dataset, where you can access an overview and profile information for the file.

  [*Managing dataset metadata*](../Catalog/managing-dataset-metadata.htm)

## Space permissions

Data files are a type of data source in Qlik Cloud Analytics.

Shared space members with any of the following roles can manage data sources in that space:

- Owner
- Can manage
- Can edit
- Can edit data in applications

Managed space members with any of the following roles can manage data sources in that space:

- Owner
- Can manage
- Can operate

Information noteFor user-based subscriptions, the Can operate role also requires a Professional user entitlement.

Space members with the Can consume data role can view data sources in the space, and they can consume the data sources where they have permission to create applications They can also edit user credentials for certain connections from the Data load editor or Script interface.

Information noteThe Can consume data role is a space-level role that gives members of a space permission to view and consume the data sources stored in that space. The benefit of this role is that you can allow users to access data files and data connections in your space, without giving them the elevated permissions they would normally require to access data sources inside a space.

For more information about the space role requirements for data source actions, see:

- [*Shared space permissions for Professional and capacity-based subscription users*](permissions-shared-space-prof-full.htm)
- [*Shared space permissions for users with Analyzer entitlement*](permissions-shared-space-analyzer.htm)
- [*Shared space permissions for administrators*](permissions-shared-space-admin.htm)
- [*Managed space permissions for Professional and capacity-based subscription users*](permissions-managed-space-prof-full.htm)
- [*Managed space permissions for users with Analyzer entitlement*](permissions-managed-space-analyzer.htm)
- [*Managed space permissions for administrators*](permissions-managed-space-admin.htm)

## Referencing space folder structure in application and script development

### Rules for valid space folder paths

The following list outlines rules for referencing data files in load scripts within Qlik Cloud Analytics:

- The syntax for referring to a file in the load script is:

  [lib://(space\_name):DataFiles/(folder\_name)/(file\_name)]
- If the space name is omitted, the current space is used. For examples, see [*Data sources for applications in managed spaces*](app-data-managed-spaces.htm).
- The full folder path must be provided. Relative paths are not supported.
- The folder path can include multiple folders in a hierarchical structure. Each folder\_name in the path must be delimited with / characters.
- The following are not allowed in the path when referencing files residing in a folder structure:

  - //
  - \
  - \\
  - /./
  - /../
- Trailing period symbols (.) in the space, folder, or file name are acceptable as long as they do not appear in the configurations in the above list.
- You need to reference the underlying data file, not the dataset for the file. A dataset can have a different name than its underlying data file. For more information about the differences between data files and datasets, see [*Distinctions between data files and datasets*](../Catalog/data-files-and-datasets.htm).

Examples: Non-compliant syntax

These examples are considered invalid syntax for the path:

Load [Transactions] from 'lib:\\Demo:DataFiles\Sales2024\France.qvd';

store [Transactions] into 'lib://Demo:DataFiles/Sales2024/./France.qvd';

Load [Transactions] from 'lib://Demo:DataFiles/Sales2024/../France.qvd';

store [Transactions] into 'lib://Demo:DataFiles//Sales2024//France.qvd';

Depending on the type of script statement being used, non-compliant syntax might cause reload failure, or could still be executed with different behavior. For specific details, see:

- [Loading data from files](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/manage-data-files-spaces.htm)
- [Storing data into files](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/manage-data-files-spaces.htm)

### Loading data from files

In Qlik Cloud Analytics, when loading data from a data file within a load script, you can use a LOAD statement or insert QVS code. In both cases, hierarchical space folder structures can be referenced in your script statement. Follow the rules for [valid space folder paths](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/manage-data-files-spaces.htm#PathRules). Additionally, the file and all referenced folders need to already exist in the specified location. Otherwise, the reload fails.

#### LOAD statements in the load script

Examples: Reference to file at the top-level path of a space

This example loads the file orders.csv from a personal space. The file is not located within any specific folder, but instead is located at the top-level path in the space.

```
LOAD * FROM [lib://DataFiles/orders.csv];
```

This example loads the file orders.csv from a [shared](#glossary-1 "Glossary term"), [managed](#glossary-2 "Glossary term"), or [data space](#glossary-3 "Glossary term"). The name of the space is TeamSharedSpace. The file is not located within any specific folder, but instead is located at the top-level path in the space.

```
LOAD * FROM [lib://TeamSharedSpace:DataFiles/orders.csv];
```

Examples: References to specific folder path within a space

This example loads the file orders\_Europe.csv from the folder Orders By Region within a personal space.

```
LOAD * FROM [lib://DataFiles/Orders By Region/orders_Europe.csv];
```

This example loads the file orders\_Europe.csv from the folder Orders By Region within a [shared](#glossary-4 "Glossary term"), [managed](#glossary-5 "Glossary term"), or [data space](#glossary-6 "Glossary term"). The name of the space is SalesSpace.

```
LOAD * FROM [lib://SalesSpace:DataFiles/Orders By Region/orders_Europe.csv];
```

#### Inserting QVS code

Example: Referencing QVS file at the top-level path of a space

In this example, the file test.qvs is referenced in the load script. The file is located in the space TeamSharedSpace. The file is not located within any specific folder, but instead is located at the top-level path in the space.

```
$(Must_Include=lib://TeamSharedSpace:DataFiles/test.qvs)
```

Example: Referencing QVS file in a specific folder path within a space

In this example, the file test.qvs is referenced in the load script. The file is located in the folder SalesData within the space TeamSharedSpace.

```
$(Must_Include=lib://TeamSharedSpace:DataFiles/SalesData/test.qvs)
```

### Storing data into files

When you use a Store statement in a load script in Qlik Cloud, you can reference the exact folder in a space where you want to store the created files. Follow the rules for [valid space folder paths](/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Spaces/manage-data-files-spaces.htm#PathRules). Additionally, the following behaviors also apply and are unique to Store statements:

- If the space exists but the specified folder path does not, the path will be created in the space. One or more folders might be created depending on the defined folder structure. The file is generated and stored there.
- If the space exists but the specified folder path uses invalid folder delimiters (for example, \, \\, //, /./, or /../), the Store statement is still executed. The output file is instead saved at the top-level path in the target space and will have a name that contains its full path, not only the specified name.
- If the space does not exist, the Store statement cannot be executed and returns an error.

The following examples demonstrate how to refer to a specific folder path in the space within your Store statement.

Example: Storing file at the top-level path of a space

In this example, the entire table mytable is exported into Qlik Cloud Analytics as a file named myfile.qvd. The file is added to the shared space TeamSharedSpace. The file is not located within any specific folder, but instead is located at the top-level path in the space.

```
Store * from mytable into [lib://TeamSharedSpace:DataFiles/myfile.qvd];
```

Example: Storing file to a specific folder path within a space

In this example, the entire table mytable is exported into Qlik Cloud Analytics as a file named myfile.qvd. The file is added to the folder SalesData within the space TeamSharedSpace.

```
Store * from mytable into [lib://TeamSharedSpace:DataFiles/SalesData/myfile.qvd];
```

## Administering data files

Tenant administrators and analytics administrators can manage all data files in the space from the Administration [activity center](#glossary-7 "Glossary term"). For more information, see [*Managing data files for tenant and analytics administrators*](../Admin/mc-administer-data-files.htm).

## Learn more

- [*Distinctions between data files and datasets*](../Catalog/data-files-and-datasets.htm)
