---
title: "Creating reusable load script with QVS files"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/LoadData/QVS/create-common-scripting-qvs.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Loading and modeling analytics data", "Loading analytics data", "Loading and transforming data with scripting"]
---

# Creating reusable load script with QVS files

Create reusable blocks of load script using QlikView script (QVS) files.

You can add a block of Qlik load script to a text editor and save it as a QVS file. The QVS can then be uploaded to Qlik Cloud or added to a web storage provider. You can also download versions of script in History as QVS files. The QVS can be inserted into the load scripts of scripts and applications from your data files or web storage. This allows you to use a single script across multiple applications and scripts. For example, you could use a QVS to:

- Set variables.
- Define commonly used subroutines.
- Set color palettes.
- Define calendars.

In Catalog, you can view uploaded QVS files and filter them using the Scripts filter. Opening a QVS file opens QVS viewer. Uploaded QVS file access follows space permissions for data source access.

You can also reuse scripts within other scripts.

For more information, see [*Inserting other scripts into load scripts*](inserting-qvs-script-editor.htm).

## Navigating QVS viewer

In the Analytics [activity center](#glossary-0 "Glossary term"), you can open a QVS file to view it in QVS viewer. QVS viewer contain two sections: Overview and Preview.

Overview contains information about the script and a quick preview of the script. You can see the following information:

- Owner: Owner of the script.
- Creator: Creator of the script.
- Space: Space the script where the script is located.
- Created date: Date the script was created.
- File size: Size of the script.

Under Quick view, you can preview the script.

QVS viewer overview

![Overview of the QVS file Product.qvs, shoing QVS information and a quick view of the script.](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_qvs-catalog-overview.png "Click to view full size")

In Preview, you can view the script in more detail. You can open the search panel by clicking ![Open search panel](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_search_outline.svg). You can open the syntax help by clicking ![Help](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_help_outline.svg).

QVS viewer preview, with open search panel

![Preview](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/ui_qvs-catalog-preview.png "Click to view full size")

## Creating QVS files

Create QVS files in a text editor outside of Qlik Cloud. Load script history can also be downloaded as QVS files.

Do the following:

1. Create a block of load script in an application or script.

   Creating your load script in an application or script allows you to test the script first before adding it to a QVS file.

   Alternatively, find a block of load script you want to reuse.
2. In a text editor, copy and paste the block of load script you want to reuse.
3. Save the load script as a file with the QVS extension.

You can now upload the QVS file to Qlik Cloud or a web storage provider.

## Uploading QVS files

Do the following:

1. Go to the Create page of the Analytics activity center and select Upload.
2. Select Script.
3. Drag and drop your QVS files into the Drop your files here dialog.

   Alternatively, click Browse and navigate to your QVS files.
4. Select a destination space for the files.
5. Optionally, add tags to the QVS scripts.
6. Click Upload.

## Editing QVS files

You cannot edit a QVS file in Qlik Cloud. If a QVS file requires changes, make the changes to the file in a text editor and reupload the file. You can convert QVS files to scripts to allow for editing.

## Converting QVS files to scripts

You can duplicate and convert QVS files into scripts in the catalog.

Do the following:

1. In the Analytics activity center, navigate to Catalog.
2. On the QVS file you want to convert, click ![More actions](../../_images/en-US/cloud-services/Subsystems/Hub/Content/Resources/Images/Icons/ic_more.svg) and select Manage > Duplicate as script.

## Permissions

When inserting a QVS file into your load script, you need to have certain permissions for the space containing the QVS file. For more information, see [*Permissions for inserting scripts*](../../Scripting/SystemVariables/Include.htm#Permissions).

## Limitations

QVS files have the following limitations:

- Included scripts displays the first 50 scripts included in the load scripts. If there are more included scripts, they will be executed when the load script runs, but will not be listed in Included scripts.
- Preview for QVS files is not available on mobile.
- If you previously uploaded QVS load script as a TXT file, the files will still function. They will not be treated as QVS files however unless their file extension is changed to QVS.
