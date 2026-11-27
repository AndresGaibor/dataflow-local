---
title: "Managing data files for tenant and analytics administrators"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/Admin/mc-administer-data-files.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Deploying and administering Qlik Cloud", "Administering Qlik Cloud", "Managing resources"]
---

# Managing data files for tenant and analytics administrators

If you are [tenant admin](#glossary-0 "Glossary term") or analytics admin, you can manage data files in the tenant in the Administration activity center, under Content > Data files.

## Administrator access levels for managing data files

Tenant and analytics administrators have different levels of access to data files:

- Tenant administrators: Can manage all data files in managed, shared, and personal spaces.
- Analytics administrators: Can manage data files in managed and shared spaces. Cannot manage data files in other users' personal spaces.

## Folder structures for data files

When managing data files as an administrator, you can view a path for each file and folder in the tenant. The path is structured differently than the path users see when managing data files at the space level.

In the Administration activity center, the path for a data file or folder always starts with the name of the space. Any subsequent folders in the hierarchy are folders that users have created within the space. All files located in a personal space will display as being located in the space Personal. Identify which user's personal space a file belongs to by looking at the Owner of the data file as shown in the table.

For information about the folder structure path you see when managing a specific space, see [*Folder structures in spaces*](../Spaces/manage-data-files-spaces.htm#SpaceFolderStructure).

## Navigation

In the Administration activity center, the Data files tab is located within the Content section. This interface allows you to administer file-based data content across the tenant. You can also add new data files to spaces in which you have sufficient permissions.

### Toolbar

The toolbar is located at the top of the interface above the path selector and table. In the toolbar, you can:

- Search for data files in the space.
- Filter files by owner.
- Upload files.

  [*Adding a data file*](#UploadFile)
- Create folders.

  [*Creating folders*](#NewFolder)
- Perform actions on multiple data files at a time.

  [*Performing actions on multiple files and folders*](#BulkActions)
- Change the sorting of the files and folders in your view.

  Change the sorting from the default Last modified option, and toggle between ![Ascending](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_ascending.svg) (ascending) and ![Descending](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_descending.svg) (descending) order.
- Change the appearance of the files and folders in your view.

  Select ![Tree view](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_tree_view.svg) for the hierarchy view, which presents files and folders with indentation to visually display hierarchies. Select ![List](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_list.svg) for the list view, where files and folders are shown with a flat structure in the table along with a separate column displaying their specific paths.

### Path selector

The path selector contains interactive breadcrumbs that show your current position in the folder structure. Select a folder in the path selector to navigate forward or backward in relation to the current path. Select the / at the leftmost side of the selector to return to the view of the entire tenant.

Select the empty area after the current path to see the spaces and folders contained within the current position, and to search for spaces and folders.

### Table

The table shows all the files and folders in the tenant, or in the selected space or folder. The table is where you manage the data files and folders. Select folders in the table to navigate to them in the path selector.

In the table, you can also view important information about items, such as their size, number of folders, time of last update, and ownership.

## Space permissions

For certain actions, the administrator does not need any space roles in the space where the data file or folder is located:

- Deleting
- Changing owner

For other actions, the administrator needs to have the correct space roles in the space where the data file or folder is located:

- Creating
- Renaming
- Moving
- Duplicating
- Opening other tools (Open dataset, Lineage, Impact analysis)

## Performing actions on multiple files and folders

You can use the options in the toolbar to perform the following actions on more than one file or folder at a time:

- ![Scissors](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_cut_outline.svg)
  (Cut)
- ![Copy](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_copy.svg)
  (Copy)
- ![Paste](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_paste.svg)
  (Paste)
- ![Change owner](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_group_outline.svg) (Change owner)
- ![Trash bin](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin_outline.svg) (Delete)

You can cut, copy, and paste items between spaces or to different locations within the same space. For example, you can cut multiple items and paste them into a different space.

Information note

Cut, copy, and paste actions can be used to move data files from one location to another. When changing file locations for data files referenced in load scripts, the load scripts need to be updated to reflect the new location. For more information, see [*Implications of moving data files used in load scripts*](#EffectsFileMove).

Folders have owners. When you change the owner of a folder, the owner of all data files within the folder is updated as well.

For information about what happens when you change the owner of a data file or folder, see [*Changing the owner of a data file or folder*](#ChangeOwner).

Do the following:

1. In Administration, go to Content.
2. Switch to the Data files tab.
3. In the table, select the items on which you want to perform an action.

   Tip note

   To select more than one item at a time, click the first item, and then use a combination of keyboard commands and clicking to select more files. For example:

   - Hold Shift and click the last item you want to select. This selects all items from the first to last item.
   - Hold Ctrl (Windows) or command (macOS) and click additional items one at a time. This selects each additional item individually.
4. In the toolbar, click an action. The available actions are listed earlier in this section.

When cutting and pasting items between spaces and folders, you need to navigate to the new location to perform the Paste action.

## Adding a data file

You can add data files as datasets. To upload a data file to a space, you need sufficient permissions in that space.

Data files can be up to 100 GB. However, when uploading very large data files (over 6 GB), you might experience constraints with engine capacity. These constraints are more likely to be encountered with QVD data files due to the memory usage necessary to load QVD files into the engine. For more information about increasing the capacity available, see [*Large application support*](large-app-support.htm).

Do the following:

1. In the Administration activity center, go to Content.
2. Switch to the Data files tab.
3. In the toolbar within the Data files tab, click ![Upload](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_upload.svg) to upload a file.
4. Drag and drop your data files into the Add file dialog.

   Alternatively, click Browse and navigate to your data files.
5. Under Path, you can choose where in the space's folder structure to add the file.

   To add the file to a specific folder, click the path bar and select the folder from the drop down menu. Alternatively, type the path of the specific folder.
6. Click Upload.

Alternatively, click ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to a folder in the table and select ![Upload](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_upload.svg) Upload file to folder.

For additional ways to add data files, see [*Adding datasets*](../DataSource/add-datasets.htm).

## Creating folders

Create a folder within a space to organize content.

Do the following:

1. In Administration, go to Content.
2. Switch to the Data files tab.
3. In the toolbar, click ![New folder](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_new_folder.svg).
4. Define the name of the folder.
5. Under Path, you can choose where in the space's folder structure to add the new folder.
6. Click the path bar and select a containing folder from the drop down menu. Alternatively, type the path of a specific location where you want to add the folder.
7. Click Create.

Alternatively, add a folder by clicking ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to an existing folder in the table and selecting ![New folder](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_new_folder.svg) Add folder. The new folder is added within the existing folder.

## Renaming a data file or folder

Do the following:

1. In the Administration activity center, go to Content.
2. Switch to the Data files tab.
3. In the table, click ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to a file or folder.
4. Click ![Edit](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Rename.
5. Enter the new name for the file and click Save.

Any load scripts that reference the original file or folder name will need to be updated.

### Implications of renaming a data file

Any data file uploaded to Qlik Cloud exists in two forms: the underlying data file and a dataset. In Qlik Cloud, the difference between a data file and a dataset is that the data file is the underlying source for the dataset. When you rename a data file from Space settings > Data files, the name of its dataset may or may not be automatically updated at the same time, depending on whether or not the dataset name has been changed previously.

Updating the name of a data file will require changes to load scripts that use this data file. If you instead want to change only the name of the dataset for this file—that is, the resource that can be opened and analyzed with catalog, lineage, and impact analysis tools—you can instead rename the dataset from areas such as Catalog (general view), Home, Favorites, Collections, or when opening the dataset in Dataset view. Renaming a dataset simply adds an alias to the dataset and does not update the name of the underlying data file. It should be noted, however, that renaming a dataset causes the dataset name to become out of sync with the data file name.

For more information, see [*Distinctions between data files and datasets*](../Catalog/data-files-and-datasets.htm).

## Duplicating a data file or folder

Do the following:

1. In the Administration activity center, go to Content.
2. Switch to the Data files tab.
3. In the table, click ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to a file or folder.
4. Click ![Duplicate](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_duplicate_outline.svg) Duplicate.

## Performing cut, copy, and paste actions on a file or folder

Information note

Cut, copy, and paste actions can be used to move data files from one location to another. When changing file locations for data files referenced in load scripts, the load scripts need to be updated to reflect the new location. For more information, see [*Implications of moving data files used in load scripts*](#EffectsFileMove).

Do the following:

1. In a space, click Space settings and select Data files.
2. In the table, click ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to a file or folder.
3. Click ![Scissors](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_edit_outline.svg) Cut, ![Copy](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_copy.svg) Copy, or ![Paste](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_paste.svg) Paste.

   Tip noteAlternatively, you can use common keyboard shortcuts such as Ctrl+C (Windows) and command+C (macOS).

To perform these actions on more than one file or folder at a time, see [*Performing actions on multiple files and folders*](#BulkActions).

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

For more information about how to refer to space folder locations in load scripts, see [*Managing data files for tenant and analytics administrators*](#FolderStructureRefExamples).

## Deleting a data file or folder

Do the following:

1. In a space, click Space settings and select Data files.
2. In the table, click ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to a file or folder.
3. Click ![Trash bin](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_bin_outline.svg) Delete.
4. In the dialog, click Delete to confirm the deletion.

You can also delete multiple items at a time. See [*Performing actions on multiple files and folders*](#BulkActions).

## Changing the owner of a data file or folder

You can change the owner of a data file or a folder.

Folders have owners. When you change the owner of a folder, the owner of all data files within the folder is updated as well.

Do the following:

1. In Administration, go to Content.
2. Switch to the Data files tab.
3. In the table, click ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) next to a file or folder.
4. Click ![Change owner](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_group_outline.svg) Change owner.

You can also change the owner of multiple items at a time. See [*Performing actions on multiple files and folders*](#BulkActions).

### Data file ownership

In Qlik Cloud Analytics, the owner of a data file does not affect access control unless the data file is located in a user's [personal space](#glossary-1 "Glossary term").

For example, an application in a shared space could load data from a data file in the same space. If the owner of the data file is changed to a user who is not a member of the shared space, the application will continue to be able to access the file and load data from it. The same behavior can be expected for data files used in other resources, such as [knowledge bases](#glossary-3 "Glossary term"), Qlik Predict resources, and scripts.

On the other hand, when you change the owner of a data file in a user's personal space, the file is automatically moved to the personal space of the new owner. This affects file references in data load scripts and other access controls.

## Performing other actions on individual data files

In the Data files interface, you can also navigate directly to other tools for performing analysis of a specific file. The following options are available when you use the ![Three-dot menu](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) menu on a file:

- ![Impact analysis](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_impact_analysis.svg)
  Impact analysis: Investigate the potential effects of making changes to data in the dataset.

  [*Analyzing impact analysis in Analytics*](../Catalog/impact-analysis2.htm)
- ![Lineage](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_lineage.svg)
  Lineage: Understand more about the history of the dataset.

  [*Analyzing lineage in Analytics*](../Catalog/lineage.htm)
- ![Dataset](../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_data_set.svg) Open dataset: Open the file as a dataset, where you can access an overview and profile information for the file.

  [*Managing dataset metadata*](../Catalog/managing-dataset-metadata.htm)

## Distinctions between data files and datasets

File-based data sources stored locally within Qlik Cloud are, at their source, data files. Each data file also exists as a dataset that can be analyzed and edited using catalog, lineage, and impact analysis tools.

When you store a data file directly within Qlik Cloud, the resource is created as a data file. Across Qlik Cloud, the same file will be shown in two different ways:

- In Space settings > Data files, the underlying data file is shown.
- From the general overview in Catalog, as well as in Home, Favorites and Collections, the dataset is shown. Depending on your access and location in the user interface, you might also be able to view the underlying data file for a dataset.

- In Space settings > Data files, the underlying data file is shown.
- From the general overview in Catalog, as well as in Home, Favorites and Collections, the dataset is shown.

This distinction is important when you edit data files and datasets in Qlik Cloud Analytics. Editing a dataset—specifically, renaming it—does not rename the underlying data file. Instead, it simply adds an alias to the data file for the purposes of its use as a dataset. Because analytics content such as applications and scripts reference the underlying data file and not the dataset, you must rename the underlying data file and not its dataset if you need the references to function properly during application and script development.

For more information, see [*Distinctions between data files and datasets*](../Catalog/data-files-and-datasets.htm).

## Managing data files from the space

At the space level, you can manage the data files in a space that you have permission to manage. See [*Managing data files*](../Spaces/manage-data-files-spaces.htm).

## Learn more

- [*Distinctions between data files and datasets*](../Catalog/data-files-and-datasets.htm)
