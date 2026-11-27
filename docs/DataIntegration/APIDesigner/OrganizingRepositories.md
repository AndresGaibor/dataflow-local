---
title: "Organizing repositories"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/DataIntegration/APIDesigner/OrganizingRepositories.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Integrating data", "Designing API contracts", "API design"]
---

# Organizing repositories

## Creating a new repository

Create new repositories to better organize your APIs and folders.

1. In the left panel, click ![Menu](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/apis_menu.png) next to the repository area.
2. Click Create repository.
3. Enter a repository name and a description.

   ![Create New Repository window.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/create_repository.png)
4. Click Create.

   Your new repository appears in the selector at the top of the main
   area.
5. Create a new folder or API by clicking New folder or
   New API.

   For more information, see [Working with a new API](WorkingWithNewApi.htm) and [Organizing API folders](OrganizingApiFolders.htm "You can organize your APIs into folders.").

## Moving and copying an API or a folder to another repository

Quickly move or copy APIs, folders, or versions between repositories to keep your
work organized.

- You have at least two different repositories.
- The content you want to move or copy does not exist in the target
  repository.

1. In the left panel, click ![Menu](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/apis_menu.png) next to the folder or API you want to move.
2. Click Move/Copy to API repository.
3. Choose between MOVE and
   COPY.

   ![Move a folder to another repository window.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/moving-folder-to-repository.png)
4. Select a target repository.
5. Click MOVE or COPY.

The selected content now appears in the target repository.

## Moving and copying multiple APIs and folders to another repository

Copy or move multiple root-level APIs and folders to another repository in a single operation.

- You have at least one repository in addition to the Default repository.

1. In the left panel, click ![Menu](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/apis_menu.png) next to the source repository and click Move / Copy to repository.

   ![Repository context menu with the Move / Copy to repository option.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/move-copy-to-repository-menu.png)

   The Move or copy Folders/APIs to a repository dialog opens.
2. Select MOVE or COPY.

   Information noteNote: The MOVE and COPY options are unavailable once items are staged. To switch, click Remove to clear staged items first.
3. In the Target dropdown, select the target repository.

   Information noteRestriction: The Default repository cannot be selected as the target.
4. In the Source panel, select the check boxes next to the root-level APIs and folders you want to copy or move, or click Select all.

   Information noteNote: Only root-level folders and APIs can be selected. Selecting a folder includes all its contents, preserving the existing folder structure.

   ![Move or copy Folders/APIs to a repository dialog, showing Source and Target panels with Add and Remove buttons.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/api-move-copy-folder.png)
5. Click Add.
6. Click MOVE or COPY.

The selected items appear in the target repository.

Information noteNote: If any item being copied or moved has the same name as an existing item in the target repository, it is renamed by appending \_1, \_2, and so on.

Information noteNote: If you move a shared item, it is automatically unshared in the target repository. Copied items are not shared, regardless of the sharing status of the original.

## Deleting a repository

Delete repositories you no longer need. This action permanently removes all APIs
and data from the repository. Before deleting, make sure to move any content you want to
keep.

1. In the left panel, select the repository you want to delete.
2. Click the ![Menu](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/apis_menu.png) button next to the repository and click Delete repository.
3. Confirm by clicking Delete Repository.

   ![Delete Repository window.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ApiDesigner/delete-repository.png)

The repository and all its content have been permanently deleted and removed
from the left panel.
