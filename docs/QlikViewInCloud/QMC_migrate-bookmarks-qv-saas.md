---
title: "Migrating bookmarks from QlikView to Qlik Cloud tenants"
source_url: https://help.qlik.com/en-US/cloud-services/Subsystems/Hub/Content/Sense_Hub/QlikViewInCloud/QMC_migrate-bookmarks-qv-saas.htm
guide: "Qlik Cloud"
product: "Qlik Cloud"
version: ""
last_updated: "2026-11-27"
breadcrumbs: ["Qlik Cloud", "Analyzing data", "Creating analytics and visualizing data", "QlikView applications in Qlik Cloud", "Publishing QlikView documents and links in Qlik Cloud", "Publishing a QlikView document in Qlik Cloud"]
---

# Migrating bookmarks from QlikView to Qlik Cloud tenants

QlikView Bookmark Migration Tool is a tool that migrates server bookmarks to QlikView applications in managed spaces in a Qlik Cloud tenant.

Server bookmarks are not included when QlikView documents are added to a Qlik Cloud tenant. QlikView can assign ownership of the bookmark between the Active Directory users on the QlikView Server and the users in the Qlik Cloud tenant. QlikView Bookmark Migration Tool maps these users so you can assign them ownership of server bookmarks. During the migration process, QlikView Bookmark Migration Tool contacts your Active Directory service and gets ID and email address information for your users and links them to users on the Qlik Cloud tenant by email address. You can also manually map users, so a bookmark can be owned by a different user. The bookmarks are stored in a QMT file and then migrated to an application in the Qlik Cloud tenant.

When you run QlikView Bookmark Migration Tool, you:

1. Copy shared files (.TShared or .Shared) with the bookmarks into a working folder.
2. Load files names and metadata into the working folder.
3. Select one shared file and select either all or a subset of bookmarks in the file. These are exported into a new shared file.
4. Upload the selected shared file to a QlikView application in your Qlik Cloud tenant.

You can migrate your bookmarks using a QlikView document, CloudMigrationApp, included with QlikView Bookmark Migration Tool. The CloudMigrationApp manages the scripts, files, and commands to migrate your bookmarks. You can also migrate your bookmarks using the Command Prompt to run the QlikView Bookmark Migration Tool files.

QlikView Bookmark Migration Tool is available from [Product Downloads](https://community.qlik.com/t5/Downloads/tkb-p/Downloads).

## Before you begin

Before you download and run QlikView Bookmark Migration Tool, make sure you meet the following requirements:

- You must have QlikView Desktop installed.
- You have added the QlikView documents to which you want to add the shared server bookmarks to the Qlik Cloud tenant.
- You must have a user with Professional entitlement.
- You have the Administration activity center access on your Qlik Cloud tenant.
- You must generate an API key in your Qlik Cloud tenant to use with QlikView Bookmark Migration Tool.
- You must have one of the following permissions in the destination managed space:

  - Is owner
  - Can view
  - Can contribute
  - Can manage
- You must have application IDs for the destination QlikView applications for the bookmarks. An application ID can be obtained from the string following document= in the application URL.

  For example, in the QlikView application URL https://example.qlik.com/opendoc.htm?document=e74ebae5-5659-4211-a4de-add8e49768f6, e74ebae5-5659-4211-a4de-add8e49768f6 is the application ID. Application IDs may vary slightly in format depending if they were published or directly uploaded to Qlik Cloud.
- QlikView Bookmark Migration Tool requires the Windows Active Directory Module. If it is not installed, QlikView Bookmark Migration Tool installs it automatically.

Information noteIf you suspect any shared file to be corrupt, run the SharedFile Cleaning Tool before migrating any bookmarks.

## Downloading and setting up the QlikView Bookmark Migration Tool

Do the following:

1. Download QlikView Bookmark Migration Tool from the [Product Downloads](https://community.qlik.com/t5/Downloads/tkb-p/Downloads).

   For more information, see [Downloading installation files](/en-US/qlikview/September2026/Subsystems/Server/Content/QV_Server/QlikView-Server/Download-install-files.htm).
2. Navigate to %ProgramData%\QlikTech.
3. Create a folder named QlikViewMigrationTool and copy the QlikView Bookmark Migration Tool files to that folder.
4. Optionally, create a folder and add the shared files containing the bookmarks you want to migrate to your tenant.

## Migrating bookmarks to a QlikView application with CloudMigrationApp

Warning noteDo not alter the load script in CloudMigrationApp.

Do the following:

1. Navigate to the unzipped QlikView Bookmark Migration Tool folder and open the CloudMigrationApp document in QlikView Desktop.
2. Read and agree to the QlikView Bookmark Migration Tool terms and conditions.
3. Click Settings > User preferences.
4. In the Save tab, select Save before reload. This will prevent QlikView from clearing input data after reloading.
5. In the Security tab, select the following settings and click OK:

   - Script (Allow Database Write and Execute Statements)
6. Follow the directions in the QlikView document for each sheet:

   1. In 1. Initialize, select the folder where you store shared files and the folder you want to output the copies uploaded to the tenant.
   2. In 2. Get User Data, set the parameters needed to match owners of shared bookmark with users in the Qlik Cloud tenant.
   3. In 3. View user mapping file, review the mapping.

      Optionally, edit the mapping in the file OnPremToCloudMap.csv. To map QlikView users to Qlik Cloud users, add the User ID and IdP subject values for the users from the Qlik Cloud Administration [activity center](#glossary-0 "Glossary term") to the QlikView user entries. When you are done, click Reload in the sheet.
   4. In 4. Overview, verify you have loaded the correct file.
   5. In 5. Filter metadata, optionally use the filters to narrow the scope of shared bookmarks to migrate to the tenant.
   6. In 6. Prepare new shared files for Cloud, select the shared file from the application whose bookmarks you want to migrate. Optionally, select the IDs of the bookmarks you want to include. If you select none, all available bookmarks will be included.
   7. In 7. Upload to Cloud, set the destination application in the tenant and upload the bookmarks.
7. Repeat steps 5. Filter metadata, 6. Prepare new shared files for Cloud, and 7. Upload to Cloud for each additional application to which you want to migrate bookmarks.
8. Save and close the CloudMigrationApp.

   CloudMigrationApp keeps inputs you have added to the application when you save it.

## Migrating bookmarks to a QlikView application from the Command Prompt

Do the following:

1. Open the Command Prompt as an administrator.
2. Navigate to the QlikView Bookmark Migration Tool folder: C:\ProgramData\QlikTech\QlikViewMigrationTool.
3. Enter the following command to copy the shared files and the metadata to the output folder: QMTMetaInfo.exe -InputFolder $(vInputFolder) -OutputFolder $(vOutputFolder)

   Replace the variables:

   - $(vInputFolder): – The path to the folder where the shared files are stored.
   - $(vOutputFolder): The path to the folder where you want to store migration files.
4. Enter the following command to get user data from Active Directory: QMTGetADUser.exe -DCServer "$(vDCServer)" -ADUsersFile "$(vADOutputfile)".

   Replace the following variables:

   - $(vDCServer): The Domain Controller server URL.
   - $(vADOutputfile): The file path to the folder for storing your list of QlikView Server users, including file name and .csv.
5. Enter the following command to get user data from the Qlik Cloud tenant: QMTGetUserInfo.exe -EndpointUri "$(vCloudURL)/api/v1/users" -ApiKey "$(vApiKey)" -CloudUsersFile "$(vUserIdMapLocation)".

   Replace the following variables:

   - $(vCloudURL): The URL of your Qlik Cloud tenant.
   - $(vApiKey). The API key from your Qlik Cloud tenant.
   - $(vUserIdMapLocation): The file path to the folder for storing your list of tenant users, including file name and .csv.
6. Create a new CSV file named OnPremToCloudMap.csv with the following columns:

   - Owner
   - subject
   - id
7. In OnPremToCloudMap.csv, add values from the Owner column in the file <app>.qvw.tshared.xlsx, present in the output folder in step 3 with the corresponding subject and id values from the .csv created in step 5.
8. Create a new CSV file and add a single column list of the bookmark IDs from the shared file you want to migrate to your Qlik Cloud tenant. You find the bookmark IDs in file <app>.qvw.tshared.xlsx, present in the output folder in step 3.
9. In the Command Prompt, create the QMT file containing the bookmarks that will be uploaded to the tenant by entering the following command: QMTFilter.exe -SharedFile "$(OriginalSharedFile)" -IdFilterFile "$(csvFile)" -UserIdMappingFile "$(OnPremToCloudMap.csv)" -UpdatedFolder "$(Updated)" -ApiKey "$(vApiKey)".

   Replace the following variables:

   - $(OriginalSharedFile): The full path, including file name, to where the shared file is located.
   - $(csvFile): The full path, including file name, to the CSV file containing the bookmark IDs.
   - $(OnPremToCloudMap.csv): The full path, including file name, to OnPremToCloudMap.csv.
   - $(Updated): The path to the folder where the QMT file will be stored.
   - $(vApiKey): The API key from your Qlik Cloud tenant.
10. Run the following command, replacing the variables: qlik\_qv\_export.exe -Mode migrate -CloudUrl "$(vCloudURL)" -AppId "$(vAppId)" -ApiKey "$(vApiKey)" -UploadPath "$(vSharedFileToUpload)" -HandledDirectory "$(vHandledDirectory)".

    Replace the following variables:

    - $(vCloudURL): The URL of your Qlik Cloud tenant.
    - $(vAppId): The application ID of the application to which you are migrating bookmarks.
    - $(vApiKey): The API key from your Qlik Cloud tenant.
    - $(vSharedFileToUpload): The full path, including the file name, to the QMT file containing the bookmarks.
    - $(vHandledDirectory): The full path of the folder where your QMT file will be stored once it is migrated to the cloud.

    Information noteA message is displayed: "Parameter log written to C:\ProgramData\QlikTech\QlikViewMigrationTool\qlik\_qv\_export\_log.txt". Check the log to ensure that the migration was successful.

## Limitations

QlikView Bookmark Migration Tool has the following limitations:

- QlikView Bookmark Migration Tool does not support migrating bookmarks to QlikView applications in personal spaces. You can migrate bookmarks to QlikView applications in shared spaces, but they are not available to users.
- UNC paths are not supported for the input or output folders. Shared folders mapped to local drives are supported.
- The number of XLSX files on sheet 4. Overview may differ compared to the number of actual files in the folder. This is because empty metadata files are not visible in the application.
- If you already migrated bookmarks from a shared file, you must delete the previously generated files from the handled directory before copying files from that shared file again.
- If you already migrated bookmarks from a shared file, you cannot migrate these again, if they have been shared in Qlik Cloud.
